"""
Sprinklr Reporting API Export Tool

Pull data from any Sprinklr reporting engine/report and save to CSV.
Handles pagination, token refresh, and multi-engine discovery.

Usage:
    python export.py discover                    # List all engines + reports
    python export.py query <engine> <report>     # Pull data from a report
    python export.py dashboards                  # List all dashboards
    python export.py widget <widget_id>          # Pull data from a widget

Examples:
    python export.py query OUTBOUND_MESSAGE OUTBOUND_MESSAGE
    python export.py query PLATFORM POST_INSIGHTS --days 30 --page-size 100
    python export.py query INBOUND_MESSAGE INBOUND_MESSAGE --dimensions ACCOUNT_ID,CHANNEL_TYPE
    python export.py query SERVICE_ANALYTICS CASE_LEVEL_ANALYTICS --metrics CASE_COUNT
"""

import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────

BASE_URL = os.environ.get("SPRINKLR_BASE_URL", "https://api3.sprinklr.com/prod2")
API_KEY = os.environ["SPRINKLR_API_KEY"]
ACCESS_TOKEN = os.environ["SPRINKLR_ACCESS_TOKEN"]
REFRESH_TOKEN = os.environ.get("SPRINKLR_REFRESH_TOKEN", "")
CLIENT_ID = os.environ.get("SPRINKLR_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SPRINKLR_CLIENT_SECRET", "")

OUTPUT_DIR = Path(__file__).parent / "exports"
CURL_TIMEOUT = 30

# Common dimensions and metrics per engine (starter set)
ENGINE_DEFAULTS = {
    "OUTBOUND_MESSAGE": {
        "dimensions": ["ACCOUNT_ID"],
        "metrics": [("TOTAL_ENGAGEMENT", "SUM")],
    },
    "INBOUND_MESSAGE": {
        "dimensions": ["ACCOUNT_ID"],
        "metrics": [("INBOUND_COUNT", "SUM")],
    },
    "PLATFORM": {
        "dimensions": ["ACCOUNT_ID"],
        "metrics": [("FOLLOWERS_COUNT", "SUM")],
    },
    "LISTENING": {
        "dimensions": ["SENTIMENT"],
        "metrics": [("MENTIONS", "SUM")],
    },
    "SERVICE_ANALYTICS": {
        "dimensions": [],
        "metrics": [("CASE_COUNT", "SUM")],
    },
    "SPR_TASK": {
        "dimensions": [],
        "metrics": [("TASK_COUNT", "SUM")],
    },
}


def curl_json(method, url, headers=None, data=None, form_data=None):
    """Make HTTP request via curl, return parsed JSON."""
    cmd = ["curl", "-s", "-X", method, url, "-m", str(CURL_TIMEOUT)]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    if data:
        cmd += ["-d", json.dumps(data)]
    if form_data:
        for k, v in form_data.items():
            cmd += ["--data-urlencode", f"{k}={v}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if not result.stdout.strip():
        print(f"  ✗ Empty response from {url}", file=sys.stderr)
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  ✗ Invalid JSON from {url}: {result.stdout[:200]}", file=sys.stderr)
        return None


def api_headers():
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Key": API_KEY,
        "Content-Type": "application/json",
    }


def refresh_access_token():
    """Refresh the access token using the refresh token."""
    global ACCESS_TOKEN, REFRESH_TOKEN
    print("  ↻ Refreshing access token...")
    resp = curl_json("POST", f"{BASE_URL}/oauth/token", form_data={
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }, headers={"Content-Type": "application/x-www-form-urlencoded"})
    if resp and "access_token" in resp:
        ACCESS_TOKEN = resp["access_token"]
        REFRESH_TOKEN = resp.get("refresh_token", REFRESH_TOKEN)
        print(f"  ✓ Token refreshed, expires in {resp.get('expires_in', '?')}s")
        return True
    print(f"  ✗ Token refresh failed: {resp}", file=sys.stderr)
    return False


# ── Commands ────────────────────────────────────────────────────────────────

def cmd_discover():
    """List all reporting engines and their reports."""
    print("Discovering reporting engines...\n")
    resp = curl_json("GET", f"{BASE_URL}/api/v2/reports/engines", headers=api_headers())
    if not resp or "data" not in resp:
        print("Failed to fetch engines")
        return

    engines = resp["data"]
    print(f"{'Engine ID':<45} {'Name':<35} {'Reports'}")
    print("─" * 120)

    for engine in sorted(engines, key=lambda e: e["name"]):
        eid = engine["id"]
        ename = engine["name"]
        rresp = curl_json("GET", f"{BASE_URL}/api/v2/reports/reports/{eid}", headers=api_headers())
        reports = [r["name"] for r in rresp.get("data", [])] if rresp else []
        report_str = ", ".join(reports[:5])
        if len(reports) > 5:
            report_str += f" (+{len(reports) - 5} more)"
        print(f"  {eid:<43} {ename:<35} {report_str}")

    print(f"\nTotal: {len(engines)} engines")


def cmd_dashboards():
    """List all reporting dashboards."""
    print("Fetching dashboards...\n")
    resp = curl_json("GET", f"{BASE_URL}/api/v1/reports/dashboard/list", headers=api_headers())
    if not resp:
        # Try v2
        resp = curl_json("GET", f"{BASE_URL}/api/v2/reports/dashboard/list", headers=api_headers())
    if not resp or "data" not in resp:
        print(f"Failed to fetch dashboards: {resp}")
        return

    dashboards = resp["data"]
    print(f"Found {len(dashboards)} dashboards\n")
    for d in dashboards[:50]:
        did = d.get("id", d.get("dashboardId", "?"))
        name = d.get("name", d.get("dashboardName", "?"))
        dtype = d.get("type", d.get("dashboardType", "?"))
        print(f"  {did:<30} {dtype:<20} {name}")


def cmd_query(engine, report, dimensions=None, metrics=None, days=7, page_size=50, max_pages=10, timezone="America/Los_Angeles"):
    """Query a reporting engine/report and export to CSV."""
    now = int(time.time() * 1000)
    start = int((datetime.now() - timedelta(days=days)).timestamp() * 1000)

    # Build dimensions (groupBys)
    dim_list = dimensions or ENGINE_DEFAULTS.get(engine, {}).get("dimensions", ["ACCOUNT_ID"])
    group_bys = [
        {"heading": d, "dimensionName": d, "groupType": "FIELD", "details": None}
        for d in dim_list
    ]

    # Build metrics (projections)
    metric_list = metrics or ENGINE_DEFAULTS.get(engine, {}).get("metrics", [("TOTAL_ENGAGEMENT", "SUM")])
    projections = []
    for m in metric_list:
        if isinstance(m, tuple):
            name, agg = m
        else:
            name, agg = m, "SUM"
        projections.append({
            "heading": name,
            "measurementName": name,
            "aggregateFunction": agg,
        })

    payload = {
        "reportingEngine": engine,
        "report": report,
        "startTime": str(start),
        "endTime": str(now),
        "timeZone": timezone,
        "pageSize": str(page_size),
        "page": "0",
        "groupBys": group_bys,
        "projections": projections,
        "projectionDecorations": [],
        "additional": {
            "showTotal": "true",
            "chartType": "TABLE",
            "showRolloverTrends": "false",
            "TABULAR": "true",
        },
        "skipResolve": False,
        "jsonResponse": False,
    }

    print(f"Querying {engine}/{report}")
    print(f"  Time range: {days} days")
    print(f"  Dimensions: {dim_list}")
    print(f"  Metrics: {[m[0] if isinstance(m, tuple) else m for m in metric_list]}")
    print(f"  Page size: {page_size}, max pages: {max_pages}\n")

    all_rows = []
    api_headings = []
    page = 0
    has_more = True

    while has_more and page < max_pages:
        payload["page"] = str(page)
        resp = curl_json("POST", f"{BASE_URL}/api/v2/reports/query", headers=api_headers(), data=payload)

        if not resp:
            print(f"  ✗ No response on page {page}")
            break

        if resp.get("errors"):
            err = resp["errors"]
            print(f"  ✗ API error: {json.dumps(err, indent=2)}")
            # Try token refresh on auth errors
            if any("token" in str(e).lower() or "auth" in str(e).lower() for e in err):
                if refresh_access_token():
                    continue
            break

        data = resp.get("data", {})
        rows = data.get("rows", [])
        has_more = data.get("hasMore", False)
        total = data.get("totalItems", "?")

        # Capture headings from first response
        if not api_headings and "headings" in data:
            api_headings = data["headings"]

        all_rows.extend(rows)
        print(f"  Page {page}: {len(rows)} rows (total available: {total}, hasMore: {has_more})")
        page += 1

    if not all_rows:
        print("\n  No data returned.")
        return

    # Save to CSV
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{engine}_{report}_{ts}.csv"
    filepath = OUTPUT_DIR / filename

    # Use headings from API response if available, else build from config
    csv_headers = api_headings if api_headings else dim_list + [m[0] if isinstance(m, tuple) else m for m in metric_list]

    # Extract headers from first row
    if isinstance(all_rows[0], dict):
        csv_headers = list(all_rows[0].keys())
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(all_rows)
    else:
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
            for row in all_rows:
                writer.writerow(row)

    print(f"\n  ✓ Saved {len(all_rows)} rows → {filepath}")
    return filepath


def cmd_widget(widget_id, days=7, page_size=50, max_pages=10):
    """Query using widget ID (no payload needed)."""
    now = int(time.time() * 1000)
    start = int((datetime.now() - timedelta(days=days)).timestamp() * 1000)

    payload = {
        "startTime": start,
        "endTime": now,
        "page": 0,
        "pageSize": page_size,
        "skipResolve": False,
        "jsonResponse": True,
        "timeZone": "America/Los_Angeles",
    }

    print(f"Querying widget {widget_id}")
    print(f"  Time range: {days} days\n")

    all_rows = []
    page = 0
    has_more = True

    while has_more and page < max_pages:
        payload["page"] = page
        resp = curl_json("POST", f"{BASE_URL}/api/v2/reports/query/{widget_id}",
                         headers=api_headers(), data=payload)
        if not resp or resp.get("errors"):
            print(f"  ✗ Error: {resp}")
            break

        data = resp.get("data", {})
        rows = data.get("rows", [])
        has_more = data.get("hasMore", False)
        all_rows.extend(rows)
        print(f"  Page {page}: {len(rows)} rows (hasMore: {has_more})")
        page += 1

    if not all_rows:
        print("\n  No data returned.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = OUTPUT_DIR / f"widget_{widget_id}_{ts}.csv"

    if isinstance(all_rows[0], dict):
        headers = list(all_rows[0].keys())
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(all_rows)
    else:
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            for row in all_rows:
                writer.writerow(row)

    print(f"\n  ✓ Saved {len(all_rows)} rows → {filepath}")


# ── CLI ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "discover":
        cmd_discover()

    elif cmd == "dashboards":
        cmd_dashboards()

    elif cmd == "query":
        if len(sys.argv) < 4:
            print("Usage: python export.py query <engine> <report> [options]")
            return
        engine = sys.argv[2]
        report = sys.argv[3]

        # Parse optional args
        kwargs = {}
        args = sys.argv[4:]
        i = 0
        while i < len(args):
            if args[i] == "--days" and i + 1 < len(args):
                kwargs["days"] = int(args[i + 1]); i += 2
            elif args[i] == "--page-size" and i + 1 < len(args):
                kwargs["page_size"] = int(args[i + 1]); i += 2
            elif args[i] == "--max-pages" and i + 1 < len(args):
                kwargs["max_pages"] = int(args[i + 1]); i += 2
            elif args[i] == "--dimensions" and i + 1 < len(args):
                kwargs["dimensions"] = args[i + 1].split(","); i += 2
            elif args[i] == "--metrics" and i + 1 < len(args):
                kwargs["metrics"] = [(m, "SUM") for m in args[i + 1].split(",")]; i += 2
            elif args[i] == "--timezone" and i + 1 < len(args):
                kwargs["timezone"] = args[i + 1]; i += 2
            else:
                print(f"Unknown arg: {args[i]}")
                i += 1

        cmd_query(engine, report, **kwargs)

    elif cmd == "widget":
        if len(sys.argv) < 3:
            print("Usage: python export.py widget <widget_id> [--days N]")
            return
        widget_id = sys.argv[2]
        days = 7
        if "--days" in sys.argv:
            idx = sys.argv.index("--days")
            days = int(sys.argv[idx + 1])
        cmd_widget(widget_id, days=days)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
