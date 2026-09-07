"""
Scrape the entire Sprinklr Developer Portal (dev.sprinklr.com).

Usage:
    python scrape.py

Three-phase process:
  1. Discover all page slugs from the sitemap + documentation index pages.
  2. Fetch each page via the portal API, convert HTML to markdown, save as .md.
  3. Fetch the OpenAPI spec and save as JSON.
"""

import subprocess
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "articles"
SPEC_DIR = Path(__file__).parent / "data" / "specs"
SITEMAP_URL = "https://dev.sprinklr.com/sitemap.xml"
API_BASE = "https://dev.sprinklr.com/portals/api/sites/spr-apigee-prod-apiprodportal/liveportal"
MAX_WORKERS = 6      # dev portal rate-limits a fast fan-out; keep concurrency gentle
CURL_TIMEOUT = 20


class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts = []
        self._skip = False
        self._skip_depth = 0
        self._in_pre = False
        self._in_code = False
        self._row = []
        self._rows = []
        self._in_td = False
        self._td_text = ""
        self._in_a = False
        self._a_href = ""
        self._a_text = ""
        self._list_depth = 0

    _VOID_TAGS = frozenset({"br", "hr", "img", "input", "meta", "link", "area", "base", "col", "embed", "source", "track", "wbr"})

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag in ("script", "style"):
            self._skip = True
            return

        if self._skip:
            if tag in self._VOID_TAGS:
                return
            self._skip_depth += 1
            return

        style = attrs_dict.get("style", "")
        if "display: none" in style or "display:none" in style:
            if tag in self._VOID_TAGS:
                return
            self._skip = True
            self._skip_depth = 0
            return

        if tag == "pre":
            self._in_pre = True
            self._parts.append("\n```\n")
        elif tag == "h1":
            self._parts.append("\n# ")
        elif tag == "h2":
            self._parts.append("\n## ")
        elif tag == "h3":
            self._parts.append("\n### ")
        elif tag == "h4":
            self._parts.append("\n#### ")
        elif tag == "h5":
            self._parts.append("\n##### ")
        elif tag == "p":
            self._parts.append("\n")
        elif tag == "br":
            self._parts.append("\n")
        elif tag in ("strong", "b"):
            self._parts.append("**")
        elif tag in ("em", "i"):
            self._parts.append("*")
        elif tag == "code" and not self._in_pre:
            self._in_code = True
            self._parts.append("`")
        elif tag in ("ul", "ol"):
            self._list_depth += 1
        elif tag == "li":
            self._parts.append("\n" + "  " * (self._list_depth - 1) + "- ")
        elif tag == "a":
            self._in_a = True
            self._a_href = attrs_dict.get("href", attrs_dict.get("routerlink", ""))
            self._a_text = ""
        elif tag == "table":
            self._rows = []
        elif tag == "tr":
            self._row = []
        elif tag in ("td", "th"):
            self._in_td = True
            self._td_text = ""

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False
            self._skip_depth = 0
            return

        if self._skip:
            if tag not in self._VOID_TAGS:
                if self._skip_depth > 0:
                    self._skip_depth -= 1
                else:
                    self._skip = False
            return

        if tag == "pre":
            self._in_pre = False
            self._parts.append("\n```\n")
        elif tag in ("h1", "h2", "h3", "h4", "h5"):
            self._parts.append("\n")
        elif tag == "p":
            self._parts.append("\n")
        elif tag in ("strong", "b"):
            self._parts.append("**")
        elif tag in ("em", "i"):
            self._parts.append("*")
        elif tag == "code" and self._in_code:
            self._in_code = False
            self._parts.append("`")
        elif tag in ("ul", "ol"):
            self._list_depth = max(0, self._list_depth - 1)
        elif tag == "a":
            self._in_a = False
            href = self._a_href
            text = self._a_text.strip()
            if href and not href.startswith("#"):
                if href.startswith("/"):
                    href = f"https://dev.sprinklr.com{href}"
                self._parts.append(f"[{text}]({href})")
            else:
                self._parts.append(text)
        elif tag in ("td", "th"):
            self._in_td = False
            self._row.append(self._td_text.strip().replace("|", "\\|").replace("\n", " "))
        elif tag == "tr":
            if self._row:
                self._rows.append(self._row)
        elif tag == "table":
            if self._rows:
                max_cols = max(len(r) for r in self._rows)
                for i, row in enumerate(self._rows):
                    while len(row) < max_cols:
                        row.append("")
                    self._parts.append("\n| " + " | ".join(row) + " |")
                    if i == 0:
                        self._parts.append("\n| " + " | ".join(["---"] * max_cols) + " |")
                self._parts.append("\n")
                self._rows = []

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_a:
            self._a_text += data
        elif self._in_td:
            self._td_text += data
        else:
            self._parts.append(data)

    def handle_entityref(self, name):
        entities = {"amp": "&", "lt": "<", "gt": ">", "quot": '"', "apos": "'"}
        char = entities.get(name, f"&{name};")
        if self._in_a:
            self._a_text += char
        elif self._in_td:
            self._td_text += char
        elif not self._skip:
            self._parts.append(char)

    def handle_charref(self, name):
        try:
            char = chr(int(name, 16) if name.startswith("x") else int(name))
        except ValueError:
            char = f"&#{name};"
        if self._in_a:
            self._a_text += char
        elif self._in_td:
            self._td_text += char
        elif not self._skip:
            self._parts.append(char)

    def get_markdown(self):
        text = "".join(self._parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]+\n", "\n\n", text)
        return text.strip()


def curl_fetch(url, timeout=None):
    import time as _time
    t = timeout or CURL_TIMEOUT
    for attempt in range(3):
        result = subprocess.run(
            ["curl", "-sL", "--compressed", "-m", str(t), url],
            capture_output=True, text=True,
        )
        if result.stdout.strip():
            return result.stdout
        _time.sleep(1 + attempt * 2)
    return result.stdout


# Phase 1: Discover all page slugs

def fetch_sitemap_slugs():
    print("Fetching sitemap...")
    xml = curl_fetch(SITEMAP_URL)
    root = ET.fromstring(xml)
    ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text for loc in root.findall(".//ns:loc", ns) if loc.text]

    slugs = set()
    for url in urls:
        path = url.replace("https://dev.sprinklr.com/", "")
        if not path or path.startswith("docs/"):
            continue
        if "/" not in path:
            slugs.add(path)

    print(f"  Found {len(slugs)} unique page slugs from sitemap")
    return slugs


def discover_linked_slugs(index_slugs, existing_slugs):
    """Fetch index pages and extract any linked slugs not already known."""
    print(f"Scanning {len(index_slugs)} index pages for additional links...")
    new_slugs = set()

    for slug in index_slugs:
        try:
            raw = curl_fetch(f"{API_BASE}/page/{slug}")
            data = json.loads(raw)
            html = data["data"]["html"]

            router_links = re.findall(r'routerLink="(/[^"]+)"', html)
            href_links = re.findall(r'href="(/[^"]+)"', html)

            for link in router_links + href_links:
                s = link.lstrip("/")
                if s and "/" not in s and s not in existing_slugs:
                    new_slugs.add(s)
        except Exception:
            pass

    print(f"  Found {len(new_slugs)} additional slugs from index pages")
    return new_slugs


# Phase 2: Fetch and save articles

def fetch_article(slug):
    raw = curl_fetch(f"{API_BASE}/page/{slug}")
    data = json.loads(raw)

    if data.get("status") != "success":
        return None

    title = data["data"]["title"]
    html = data["data"]["html"]

    parts = html.split('<div class="content-container">')
    content_html = parts[1] if len(parts) > 1 else html

    parser = HTMLToMarkdown()
    parser.feed(content_html)
    md = parser.get_markdown()

    if not md or len(md) < 20:
        return None

    return {"slug": slug, "title": title, "markdown": md}


def save_article(article):
    filepath = DATA_DIR / f"{article['slug']}.md"
    content = f"""---
title: "{article['title'].replace('"', "'")}"
slug: {article['slug']}
url: https://dev.sprinklr.com/{article['slug']}
---

# {article['title']}

{article['markdown']}
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def _fetch_batch(slug_list, workers):
    """Fetch one batch at the given concurrency. Returns (saved, still_failed)."""
    saved = 0
    failed_slugs = []
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(fetch_article, s): s for s in slug_list}
        for future in as_completed(futures):
            done += 1
            if done % 50 == 0 or done == len(slug_list):
                print(f"  Fetched {done}/{len(slug_list)} — saved: {saved}, failed: {len(failed_slugs)}")
            try:
                result = future.result()
                if result:
                    save_article(result)
                    saved += 1
                else:
                    failed_slugs.append(futures[future])
            except Exception:
                failed_slugs.append(futures[future])
    return saved, failed_slugs


def fetch_and_save_all(slugs):
    slug_list = sorted(slugs)
    print(f"\nPhase 2: Fetching {len(slug_list)} pages...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    saved, failed_slugs = _fetch_batch(slug_list, MAX_WORKERS)
    # The portal throttles a fast fan-out (429s show up as failures partway through).
    # Retry the failures a few times, pausing and going gentler each round, which
    # recovers the throttled ones without a heavier dependency.
    rounds = 0
    while failed_slugs and rounds < 3:
        rounds += 1
        print(f"  retry {rounds}: {len(failed_slugs)} failed, pausing 10s then retrying gently...")
        time.sleep(10)
        recovered, failed_slugs = _fetch_batch(failed_slugs, 3)
        saved += recovered

    print(f"\nSaved {saved} articles to {DATA_DIR}")
    if failed_slugs:
        print(f"  ({len(failed_slugs)} still failed after {rounds} retries)")
        print(f"  Sample failures: {failed_slugs[:10]}")
    return saved


# Phase 3: Fetch OpenAPI spec

def fetch_spec():
    print("\nPhase 3: Fetching OpenAPI spec...")
    SPEC_DIR.mkdir(parents=True, exist_ok=True)

    raw = curl_fetch(f"{API_BASE}/apis/prod/spec", timeout=60)
    data = json.loads(raw)
    spec_str = data["data"]
    spec = json.loads(spec_str)

    outpath = SPEC_DIR / "openapi-prod.json"
    outpath.write_text(json.dumps(spec, indent=2), encoding="utf-8")

    n_schemas = len(spec.get("components", {}).get("schemas", {}))
    n_paths = len(spec.get("paths", {}))
    print(f"  Saved OpenAPI spec: {n_schemas} schemas, {n_paths} paths")
    print(f"  File: {outpath}")
    return outpath


def main():
    slugs = fetch_sitemap_slugs()

    doc_index_slugs = [
        "api2-0", "api1-0", "sprinklr-webhooks", "sdks", "community-apis",
        "live-chat-application-apis", "integration-blueprints",
        "sprinklr-postman-collection", "get-started", "api-overview",
        "getting-started", "rest-api-error-and-status-codes", "faqs", "changelog",
    ]
    extra = discover_linked_slugs(doc_index_slugs, slugs)
    slugs.update(extra)

    print(f"\nTotal unique slugs to fetch: {len(slugs)}")

    if not slugs:
        print("No slugs found. Exiting.")
        sys.exit(1)

    saved = fetch_and_save_all(slugs)
    # The OpenAPI spec is a bonus artifact, not one of the article .md files. A
    # throttled/non-JSON response here must not kill the whole scrape.
    try:
        fetch_spec()
    except Exception as e:
        print(f"  spec fetch skipped (non-fatal): {type(e).__name__}: {e}")

    print(f"\n{'='*60}")
    print(f"Scraping complete: {saved} articles + OpenAPI spec")
    print(f"Articles: {DATA_DIR}")
    print(f"Spec: {SPEC_DIR}")


if __name__ == "__main__":
    main()
