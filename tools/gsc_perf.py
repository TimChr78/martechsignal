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

Requires: GSC_SERVICE_ACCOUNT_KEY env var or ~/.hermes/gsc-service-account.json
(the SA email must be a user/owner on the property). Read-only; no OpenSEO credits.
"""
import json, os, sys, datetime as dt

PROPERTY = os.environ.get("GSC_PROPERTY", "sc-domain:martechsignal.com")
KEY_PATH = os.environ.get("GSC_SERVICE_ACCOUNT_KEY",
                          "/home/hermes/.hermes/gsc-service-account.json")
CACHE = "/opt/data/gsc-pages-28d.json"


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


def main():
    days = 28
    write_cache = "--no-cache" not in sys.argv
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


if __name__ == "__main__":
    main()
