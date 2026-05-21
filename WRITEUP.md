# Sprinklr API: What We Built & What's Possible

## What We Did

We connected to the Sprinklr Developer API and proved we can programmatically extract data from any client environment — no UI clicks, no manual exports, no dashboard dependencies.

### 1. Full API Knowledge Base (795 articles indexed)

We scraped and indexed the entire Sprinklr Developer Portal — every API endpoint, every authentication flow, every schema. This gives us a searchable reference for building any integration, without needing to navigate the docs site each time.

- 795 documentation articles saved as structured markdown
- Full OpenAPI spec (264 endpoints, 779 schemas)
- Covers Reporting, Publishing, Listening, Paid, Service, and more

### 2. Live Data Extraction — Starbucks Environment

Using OAuth 2.0 authentication against the Starbucks prod2 environment, we successfully pulled real data via the Reporting API.

**What we extracted:**

| Data Pull | Result |
|-----------|--------|
| All Starbucks social accounts (30-day engagement) | 166 accounts across FB, IG, TikTok, X, LinkedIn, YouTube |
| Engagement breakdown per account | Likes, shares, comments, reach per account per network |
| Starbucks India — every Instagram post (Mar 2025 – Apr 2026) | 1,769 posts with full captions, media type, engagement, reach, and direct IG links |

**Sample output — Starbucks India IG, top posts by engagement:**

| Date | Type | Engagement | Reach | Caption (preview) |
|------|------|-----------|-------|-------------------|
| Mar 01, 2026 | Carousel | 47,529 | 631,424 | Valencia Peach Orange Refresher launch |
| Jul 27, 2025 | Video | 38,950 | 1,458,751 | Genelia D'Souza x Imagine Foods collab |
| Aug 06, 2025 | Video | 37,975 | 1,322,249 | Imagine Foods menu promotion |
| Jan 24, 2026 | Video | 26,711 | 299,690 | Bearista Cup teaser |
| Mar 30, 2026 | Video | 20,800 | 203,394 | Harry Potter x Starbucks collab |

**30-day totals across all Starbucks accounts:**
- 3.95M total engagements
- 711.5M total reach
- Top accounts: Starbucks Global IG (1.15M engagement), Starbucks Global TikTok (525K), Starbucks Mexico IG (274K)

### 3. Reusable Export Tool

We built a CLI tool (`export.py`) that anyone on the team can use to pull data from any Sprinklr reporting engine:

```
python export.py query OUTBOUND_MESSAGE OUTBOUND_MESSAGE --days 30
python export.py query INBOUND_MESSAGE INBOUND_MESSAGE --days 90 --page-size 200
python export.py discover    # list all available engines and reports
```

Outputs CSV files ready for Sheets, Excel, or any BI tool.

---

## What's Possible

The Sprinklr API opens up 36 reporting engines with thousands of dimensions and metrics. Here's what we can build on top of this:

### For Client Delivery

- **Automated reporting** — Pull engagement, reach, impressions, and sentiment data on a schedule. No more manual dashboard exports.
- **Cross-platform content audits** — Extract every post a client published across all channels with captions, media, and performance data. What we did for Starbucks India IG (1,769 posts in seconds) can be done for any account on any channel.
- **Competitive benchmarking** — The Benchmarking engine has post-level stats and account facts for competitor analysis.
- **Listening & sentiment analysis** — The Listening engine surfaces mention volumes, sentiment breakdowns, theme tags, and topic trends.
- **Service analytics** — Case-level data, agent performance, SLA compliance, queue metrics — all exportable via API.
- **Paid media performance** — 250+ report types covering Facebook, Google, TikTok, LinkedIn, Pinterest, Snapchat, and more. Ad-level stats, audience breakdowns, conversion data.

### For Internal Tooling

- **Feed AI/LLM pipelines with real client data** — Instead of screenshots and manual summaries, we can programmatically feed post content and performance data into any analysis tool.
- **Custom dashboards** — Build tailored views that combine data from multiple engines in ways the Sprinklr UI can't.
- **Alerting & monitoring** — Set up automated checks for engagement drops, sentiment shifts, or SLA breaches.
- **Bulk operations** — The API also supports publishing, case management, user management, and webhook configuration — not just reading data.

### Available Reporting Engines (36 total)

| Engine | What It Covers |
|--------|---------------|
| Outbound Message | Published posts, engagement, reach, impressions |
| Inbound Message | Incoming messages, DMs, comments |
| Platform (Social Analytics) | Account insights, post insights, follower data |
| Listening | Brand mentions, sentiment, themes, topics |
| Paid | Ad performance across all paid channels |
| Service Analytics | Cases, agents, queues, SLAs, CSAT |
| Benchmarking | Competitor post stats, account benchmarks |
| Audience | Demographics, interests, activity |
| YouTube Analytics | Video insights, audience retention |
| WFM Reporting | Workforce scheduling, adherence, forecasting |

---

## Technical Details

- **Auth:** OAuth 2.0 code grant flow, tokens valid ~8 hours, auto-refreshable
- **Environment:** Starbucks is on prod2, customer ID 60624
- **Rate limits:** Handled with pagination (200 rows/page, auto-paginate until `hasMore: false`)
- **Output formats:** CSV and JSON, both ready for downstream consumption
- **Code location:** `~/Developer/sprinklr-dev-api-index/`

## Next Steps

1. **Pick a client use case** — e.g., monthly content performance report, competitive audit, listening trend analysis
2. **Automate it** — Schedule recurring data pulls and format the output for the client's preferred format
3. **Scale across clients** — The same tooling works for any Sprinklr environment we have API access to
