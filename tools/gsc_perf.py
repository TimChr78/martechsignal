#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["google-api-python-client>=2.100", "google-auth>=2.23"]
# ///
"""Pull Google Search Console Search Analytics (read-only) for martechsignal.com.

Closes a real gap: tools/build_homepage.py reads a cached
/opt/data/gsc-pages-28d.json to re-ground the homepage featured tools in real
impressions, but nothing in the repo produced that file. This script writes it.

Usage:
    uv run tools/gsc_perf.py                 # 28-day report + write the cache
    uv run tools/gsc_perf.py --days 90       # custom window
    uv run tools/gsc_perf.py --no-cache      # report only
    uv run tools/gsc_perf.py --keywords-report
        # also write gsc-keywords-<YYYY-MM-DD>.md for the weekly CTR loop
    uv run tools/gsc_perf.py --keywords-report --out-dir /some/dir

The --keywords-report markdown is the data source the weekly CTR optimisation
loop consumes. It replaces the n8n workflow that used to emit it, so the loop
no longer depends on n8n being up.

Requires: GSC_SERVICE_ACCOUNT_KEY env var or ~/.hermes/gsc-service-account.json
(the SA email must be a user/owner on the property). Read-only; no OpenSEO credits.
"""
import json, os, sys, datetime as dt

PROPERTY = os.environ.get("GSC_PROPERTY", "sc-domain:martechsignal.com")
KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY",
                          "/home/hermes/.hermes/gsc-service-account.json")
CACHE = "/opt/data/gsc-pages-28d.json"
# Repo-owned output dir for the weekly CTR loop (was /mnt/cache/appdata/n8n/...).
REPORTS_DIR = os.environ.get("GSC_REPORTS_DIR", "/home/hermes/.hermes/data/reports")
# Max rows per section in the markdown, keeps the report readable for the LLM.
SECTION_CAP = 40


def service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    creds = service_account.Credentials.from_service_account_file(
        KEY_PATH, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    return build("searchconsole", "v1", credentials=creds)


def q(svc, dims, start, end, limit=1000):
    body = {"startDate": start, "endDate": end, "dimensions": dims,
            "rowLimit": limit, "type": "web"}
    rows = []
    start_row = 0
    while True:
        body["startRow"] = start_row
        r = svc.searchanalytics().query(siteUrl=PROPERTY, body=body).execute()
        batch = r.get("rows", []) or []
        rows.extend(batch)
        if len(batch) < limit or start_row > 20000:
            break
        start_row += limit
    return rows


def agg(rows):
    c = sum(r["clicks"] for r in rows)
    i = sum(r["impressions"] for r in rows)
    pos = (sum(r["position"] * r["impressions"] for r in rows) / i) if i else 0
    return c, i, (c / i if i else 0), pos


def qpage(svc, start, end):
    """Pull dimensions ['query','page'] and map query -> top page by impressions.

    Returns {query: {"page": url, "page_count": n}} where page is the
    highest-impression page for that query in the window.
    """
    mapping = {}
    for r in q(svc, ["query", "page"], start, end):
        query, page = r["keys"][0], r["keys"][1]
        slot = mapping.setdefault(query, {"page": None, "page_count": 0,
                                          "_best_i": -1})
        slot["page_count"] += 1
        if r["impressions"] > slot["_best_i"]:
            slot["_best_i"] = r["impressions"]
            slot["page"] = page
    for slot in mapping.values():
        slot.pop("_best_i", None)
    return mapping


def _md_escape(s):
    return str(s).replace("|", "\\|")


def _pct(clicks, impressions):
    return f"{(clicks / impressions * 100):.2f}%" if impressions else "0.00%"


def build_keywords_markdown(svc, start, end, p_start, p_end):
    """Render the gsc-keywords markdown the weekly CTR loop reasons over."""
    s, e = start.isoformat(), end.isoformat()
    cur_rows = q(svc, ["query"], s, e)
    prev_rows = q(svc, ["query"], p_start.isoformat(), p_end.isoformat())
    prev_impr = {r["keys"][0]: r["impressions"] for r in prev_rows}
    page_map = qpage(svc, s, e)

    # Totals from the DATE dimension, not the query dimension. GSC withholds some
    # queries (privacy thresholds) and anonymises others, so summing query rows
    # understates the property: on the 2026-08-14..09-10 window the query rows gave
    # 1,866 impressions while the date dimension gave 3,287 (and 2 clicks vs 4).
    # The loop reads these numbers, so report the authoritative ones and keep the
    # query-row count separate.
    try:
        _dr = q(svc, ["date"], s, e)
        total_c = sum(r["clicks"] for r in _dr)
        total_i = sum(r["impressions"] for r in _dr)
    except Exception:
        total_c = sum(r["clicks"] for r in cur_rows)
        total_i = sum(r["impressions"] for r in cur_rows)

    # opportunities: impressions >= 20, CTR < 3%, position < 20
    opps = [r for r in cur_rows
            if r["impressions"] >= 20
            and (r["clicks"] / r["impressions"] if r["impressions"] else 0) < 0.03
            and r["position"] < 20]
    opps.sort(key=lambda r: -r["impressions"])

    # winners: clicks > 0 and CTR >= 3%
    winners = [r for r in cur_rows
               if r["clicks"] > 0
               and (r["clicks"] / r["impressions"] if r["impressions"] else 0) >= 0.03]
    winners.sort(key=lambda r: (-r["clicks"], -r["impressions"]))

    # rising: impressions grew vs the immediately preceding equal-length window
    rising = []
    for r in cur_rows:
        pv = prev_impr.get(r["keys"][0], 0)
        if r["impressions"] > pv:
            rising.append((r, pv, r["impressions"] - pv))
    rising.sort(key=lambda t: -t[2])

    L = []
    L.append(f"# GSC Weekly Keyword Report (window ending {e})")
    L.append("")
    L.append(f"**Property:** {PROPERTY}")
    L.append(f"**Window:** {s} to {e} (28 days, ends 3 days back for GSC lag)")
    L.append(f"**Previous window:** {p_start.isoformat()} to {p_end.isoformat()}")
    L.append(f"**Totals:** {total_c} clicks, {total_i} impressions across all queries"
             f" (date dimension). {len(cur_rows)} queries returned query-dimension rows.")
    L.append(f"**Source:** tools/gsc_perf.py --keywords-report (live Search Analytics API)")
    L.append("")

    L.append("## Opportunities")
    L.append("")
    L.append("Queries with impressions >= 20, CTR < 3%, position < 20."
             f" {len(opps)} matched, showing top {min(len(opps), SECTION_CAP)} by impressions."
             " Page is the top page by impressions for that query; Pages is how many"
             " pages received impressions for it.")
    L.append("")
    L.append("| Query | Impr | Clicks | CTR | Pos | Page | Pages |")
    L.append("|---|---|---|---|---|---|---|")
    for r in opps[:SECTION_CAP]:
        query = r["keys"][0]
        m = page_map.get(query, {})
        page = (m.get("page") or "n/a").replace("https://martechsignal.com", "") or "/"
        L.append(f"| {_md_escape(query)} | {r['impressions']:.0f} | {r['clicks']:.0f} "
                 f"| {_pct(r['clicks'], r['impressions'])} | {r['position']:.1f} "
                 f"| {_md_escape(page)} | {m.get('page_count', 0)} |")
    if not opps:
        L.append("| (none in this window) | | | | | | |")
    L.append("")

    L.append("## Winners")
    L.append("")
    L.append("Queries with clicks > 0 and CTR >= 3%."
             f" {len(winners)} matched, showing top {min(len(winners), SECTION_CAP)}."
             " Repeat what works here; do not rewrite these titles or metas.")
    L.append("")
    L.append("| Query | Clicks | Impr | CTR | Pos |")
    L.append("|---|---|---|---|---|")
    for r in winners[:SECTION_CAP]:
        L.append(f"| {_md_escape(r['keys'][0])} | {r['clicks']:.0f} | {r['impressions']:.0f} "
                 f"| {_pct(r['clicks'], r['impressions'])} | {r['position']:.1f} |")
    if not winners:
        L.append("| (none in this window) | | | | |")
    L.append("")

    L.append("## Rising")
    L.append("")
    L.append("Queries whose impressions grew versus the immediately preceding"
             f" equal-length window. {len(rising)} grew, showing top"
             f" {min(len(rising), SECTION_CAP)} by impression gain.")
    L.append("")
    L.append("| Query | Impr | Prev Impr | Growth | Clicks | CTR | Pos |")
    L.append("|---|---|---|---|---|---|---|")
    for r, pv, gain in rising[:SECTION_CAP]:
        L.append(f"| {_md_escape(r['keys'][0])} | {r['impressions']:.0f} | {pv:.0f} "
                 f"| {gain:+.0f} | {r['clicks']:.0f} "
                 f"| {_pct(r['clicks'], r['impressions'])} | {r['position']:.1f} |")
    if not rising:
        L.append("| (none in this window) | | | | | | |")
    L.append("")

    return "\n".join(L), {"queries": len(cur_rows), "opportunities": len(opps),
                          "winners": len(winners), "rising": len(rising)}


def write_keywords_report(svc, start, end, p_start, p_end, out_dir, today):
    md, counts = build_keywords_markdown(svc, start, end, p_start, p_end)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"gsc-keywords-{today.isoformat()}.md")
    with open(path, "w") as f:
        f.write(md)
    print(f"\nwrote {path}")
    print(f"  queries {counts['queries']} | opportunities {counts['opportunities']} "
          f"| winners {counts['winners']} | rising {counts['rising']}")
    return path


def main():
    days = 28
    write_cache = "--no-cache" not in sys.argv
    keywords_report = "--keywords-report" in sys.argv
    out_dir = REPORTS_DIR
    if "--out-dir" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out-dir") + 1]
    if "--days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--days") + 1])

    if not os.path.exists(KEY_PATH):
        print(f"SKIP: no service account key at {KEY_PATH}"); sys.exit(0)

    svc = service()
    # GSC has ~2-3 days of lag; end the window 3 days back to avoid partial days.
    end = dt.date.today() - dt.timedelta(days=3)
    start = end - dt.timedelta(days=days - 1)
    p_end = start - dt.timedelta(days=1)
    p_start = p_end - dt.timedelta(days=days - 1)
    s, e = start.isoformat(), end.isoformat()

    print(f"=== martechsignal.com | GSC web | {s} .. {e} ({days}d) ===\n")

    cur = agg(q(svc, ["date"], s, e))
    prev = agg(q(svc, ["date"], p_start.isoformat(), p_end.isoformat()))
    def delta(a, b, pct=True):
        if not b: return "n/a"
        d = (a - b) / b * 100
        return f"{d:+.1f}%"
    print("PERIOD vs PREVIOUS")
    print(f"  clicks      {cur[0]:>8,.0f}   prev {prev[0]:>8,.0f}   {delta(cur[0], prev[0])}")
    print(f"  impressions {cur[1]:>8,.0f}   prev {prev[1]:>8,.0f}   {delta(cur[1], prev[1])}")
    print(f"  CTR         {cur[2]*100:>7.2f}%   prev {prev[2]*100:>7.2f}%   {delta(cur[2], prev[2])}")
    print(f"  avg pos     {cur[3]:>8.1f}   prev {prev[3]:>8.1f}   {(cur[3]-prev[3]):+.1f}")

    dates = sorted(q(svc, ["date"], s, e), key=lambda r: r["keys"][0])
    print("\nDAILY (clicks / impressions / avg position)")
    for r in dates:
        print(f"  {r['keys'][0]}  {r['clicks']:>4.0f}  {r['impressions']:>6.0f}  {r['position']:>5.1f}")

    pages = sorted(q(svc, ["page"], s, e), key=lambda r: -r["clicks"])
    print(f"\nTOP PAGES by clicks ({len(pages)} with any impression)")
    for r in pages[:25]:
        u = r["keys"][0].replace("https://martechsignal.com", "")
        print(f"  {r['clicks']:>4.0f}c {r['impressions']:>6.0f}i  pos {r['position']:>5.1f}  {u}")

    queries = q(svc, ["query"], s, e)
    print(f"\nTOP QUERIES by impressions ({len(queries)} total)")
    for r in sorted(queries, key=lambda x: -x["impressions"])[:30]:
        print(f"  {r['clicks']:>4.0f}c {r['impressions']:>6.0f}i  pos {r['position']:>5.1f}  {r['keys'][0][:70]}")

    # GSC cannot filter by position, so filter striking distance client-side.
    strike = [r for r in queries if 4 <= r["position"] <= 20 and r["impressions"] >= 3]
    strike.sort(key=lambda r: -r["impressions"])
    print(f"\nSTRIKING DISTANCE (position 4-20, >=3 impressions): {len(strike)} queries")
    for r in strike[:30]:
        print(f"  {r['impressions']:>6.0f}i pos {r['position']:>5.1f} {r['clicks']:>3.0f}c  {r['keys'][0][:70]}")

    if write_cache:
        cache = [{"page": r["keys"][0], "clicks": r["clicks"],
                  "impressions": r["impressions"], "position": r["position"]} for r in pages]
        try:
            with open(CACHE, "w") as f:
                json.dump(cache, f, indent=1)
            print(f"\nwrote {CACHE} ({len(cache)} pages) for tools/build_homepage.py")
        except Exception as ex:
            print(f"\ncould not write cache: {ex}")

    if keywords_report:
        try:
            write_keywords_report(svc, start, end, p_start, p_end, out_dir,
                                  dt.date.today())
        except Exception as ex:
            print(f"\ncould not write keywords report: {ex}")
            sys.exit(1)


if __name__ == "__main__":
    main()
