#!/usr/bin/env python3
"""Automatic pricing re-verification for the MartechSignal catalog.

Efficient/intelligent by design, not a blind crawl:
  - TRIAGE: every record scored by overdue_days x traffic x money-citation.
    Only the top --cap records are fetched per run. Backlog clears
    highest-value-first instead of oldest-first.
  - CHEAP FIRST: conditional GET (ETag/Last-Modified). A 304 means the
    vendor page is byte-identical -> confirm-bump with ~1KB transferred.
  - COMPARE, NEVER INVENT: catalog figures must appear on the vendor page.
    Match -> date_updated=today (drops the "Re-check pending" note on the
    next rebuild). Anything else -> evidence queue for agent review.
    This script NEVER writes a price. Only dates move automatically.
  - POLITE: robots.txt respected, per-domain gap, real UA with contact URL,
    2MB cap, bounded run time. JS-rendered pages are marked needs-render
    (30d backoff), not hammered.

Outputs (all under tools/):
  .reverify-cache.json  per-slug fetch state (etag, lastmod, backoff, status)
  .reverify-queue.json  mismatch/needs-render/error items with evidence
  tools.json            date_updated bumps on CONFIRM only

Exit 1 when the queue is non-empty so the cron status surfaces it.
Stdlib only. Safe for no_agent cron.
"""
import argparse
import json
import math
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.robotparser as robotparser
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
CACHE_JSON = ROOT / "tools" / ".reverify-cache.json"
QUEUE_JSON = ROOT / "tools" / ".reverify-queue.json"
GSC_JSON = Path("/opt/data/gsc-pages-28d.json")

UA = "MartechSignal-Reverify/1.0 (+https://martechsignal.com/methodology/)"
TIMEOUT = 20
MAX_BYTES = 2_000_000
DOMAIN_GAP = 10  # seconds between requests to the same domain
UNIT_WORDS = ("user", "seat")

FIG_RES = {
    "$": re.compile(r"\$\s?([\d,]+(?:\.\d+)?)"),
    "€": re.compile(r"€\s?([\d,]+(?:\.\d+)?)"),
    "£": re.compile(r"£\s?([\d,]+(?:\.\d+)?)"),
    "USD": re.compile(r"USD\s?([\d,]+(?:\.\d+)?)", re.I),
    "EUR": re.compile(r"EUR\s?([\d,]+(?:\.\d+)?)", re.I),
    "GBP": re.compile(r"GBP\s?([\d,]+(?:\.\d+)?)", re.I),
}
CUR_OF = {"USD": "$", "EUR": "€", "GBP": "£"}
TAG_RE = re.compile(r"<(script|style|noscript|svg)[^>]*>.*?</\1>", re.S)


def norm_num(s):
    s = str(s).replace(",", "").strip()
    try:
        return f"{float(s):.2f}"
    except (ValueError, TypeError):
        return ""


def expected_figures(t):
    figs = set()
    for k in ("price_from", "paid_from"):
        v = t.get(k)
        if v:
            n = norm_num(v)
            if n and n != "0.00":
                figs.add(n)
    return figs


def page_figures(text):
    """r29 reverify (2026-10-06): per-currency figure sets. A USD record
    checked against a geo-rendered EUR page is a currency-geo event, not
    a price mismatch (attio: catalog $29 correct per vendor llms.txt)."""
    out = {}
    for sym, rx in FIG_RES.items():
        got = {norm_num(m.group(1)) for m in rx.finditer(text or "")} - {""}
        if got:
            out[sym] = got
    return out


def text_of(html):
    if isinstance(html, bytes):
        try:
            html = html.decode("utf-8", errors="ignore")
        except Exception:
            return ""
    html = TAG_RE.sub(" ", html)
    html = re.sub(r"<[^>]+>", " ", html)
    import html as _h
    return _h.unescape(re.sub(r"\s+", " ", html))


def money_slugs():
    slugs = set()
    for f in ("tools/bestx-content.json", "tools/vsx-content.json",
              "tools/alternatives-content.json"):
        try:
            d = json.loads((ROOT / f).read_text())
        except (OSError, ValueError):
            continue
        for p in d.get("pages", []):
            for k in ("a_slug", "b_slug", "c_slug"):
                if p.get(k):
                    slugs.add(p[k])
            for it in p.get("items", []) or []:
                if isinstance(it, dict) and it.get("slug"):
                    slugs.add(it["slug"])
    return slugs


def impressions():
    try:
        d = json.loads(GSC_JSON.read_text())
    except (OSError, ValueError):
        return {}
    rows = d.get("rows", d) if isinstance(d, dict) else d
    out = {}
    try:
        items = rows if isinstance(rows, list) else rows.values()
        for r in items:
            if not isinstance(r, dict):
                continue
            url = r.get("url") or r.get("page") or ""
            m = re.search(r"/tools/([^/]+)/", url)
            if m:
                out[m.group(1)] = out.get(m.group(1), 0) + (r.get("impressions") or 0)
    except Exception:
        pass
    return out


class PoliteFetcher:
    def __init__(self):
        self.last_hit = {}
        self.robots = {}
        self.read_ok = set()

    def allowed(self, url):
        try:
            from urllib.parse import urlsplit
            origin = "{0.scheme}://{0.netloc}".format(urlsplit(url))
        except Exception:
            return False
        rp = self.robots.get(origin)
        if rp is None:
            rp = robotparser.RobotFileParser()
            rp.set_url(origin + "/robots.txt")
            try:
                # fetch with our own UA: RobotFileParser.read() sends
                # Python-urllib/3.x, which bot walls challenge -> zero
                # entries parsed -> false "denied" for the whole domain.
                req = urllib.request.Request(origin + "/robots.txt",
                                             headers={"User-Agent": UA})
                body = urllib.request.urlopen(req, timeout=TIMEOUT).read(100000)
                rp.parse(body.decode("utf-8", errors="ignore").splitlines())
                if getattr(rp, "entries", []) or getattr(rp, "allow_all", False):
                    self.read_ok.add(origin)
            except Exception:
                pass  # no robots.txt readable: no policy to enforce
            self.robots[origin] = rp
        if origin not in self.read_ok:
            return True
        try:
            return rp.can_fetch(UA, url)
        except Exception:
            return True

    def get(self, url, etag=None, lastmod=None):
        from urllib.parse import urlsplit
        host = urlsplit(url).netloc
        wait = DOMAIN_GAP - (time.time() - self.last_hit.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        if etag:
            req.add_header("If-None-Match", etag)
        if lastmod:
            req.add_header("If-Modified-Since", lastmod)
        try:
            r = urllib.request.urlopen(req, timeout=TIMEOUT)
            body = r.read(MAX_BYTES + 1)
            self.last_hit[host] = time.time()
            return r.status, dict(r.headers.items()), body[:MAX_BYTES]
        except urllib.error.HTTPError as e:
            self.last_hit[host] = time.time()
            if e.code == 304:
                return 304, {}, b""
            return e.code, {}, b""
        except Exception as e:
            return "ERR:" + type(e).__name__, {}, b""


def check_record(t, cache, fetcher, today):
    slug = t["slug"]
    st = cache.get(slug, {})
    if st.get("backoff_until", "") > today:
        return "skipped-backoff", None
    url = t.get("pricing_url") or ""
    if not url and t.get("website"):
        url = t["website"].rstrip("/") 
        # homepage fetch: look for a pricing link (transient use only)
        if not fetcher.allowed(url):
            st.update({"status": "robots-denied", "backoff_until": str(date.fromisoformat(today) + timedelta(days=90))})
            cache[slug] = st
            return "robots-denied", None
        status, _, body = fetcher.get(url, st.get("etag"), st.get("lastmod"))
        if status != 200:
            st.update({"status": f"homepage-{status}", "errors": st.get("errors", 0) + 1,
                       "backoff_until": str(date.fromisoformat(today) + timedelta(days=7))})
            cache[slug] = st
            return f"homepage-{status}", None
        m = re.search(r'href="([^"]*pric[^"]*)"', body.decode("utf-8", errors="ignore")[:200000], re.I)
        if not m:
            st.update({"status": "no-pricing-link", "backoff_until": str(date.fromisoformat(today) + timedelta(days=90))})
            cache[slug] = st
            return "no-pricing-link", None
        from urllib.parse import urljoin
        url = urljoin(url, m.group(1))
    if not url:
        st.update({"status": "no-url", "backoff_until": str(date.fromisoformat(today) + timedelta(days=90))})
        cache[slug] = st
        return "no-url", None
    if not fetcher.allowed(url):
        st.update({"status": "robots-denied", "backoff_until": str(date.fromisoformat(today) + timedelta(days=90))})
        cache[slug] = st
        return "robots-denied", None
    status, headers, body = fetcher.get(url, st.get("etag"), st.get("lastmod"))
    if status == 304:
        st.update({"status": "confirmed-304", "last_check": today, "errors": 0,
                   "backoff_until": ""})
        cache[slug] = st
        return "confirmed-304", None
    if status != 200 or not body:
        errs = st.get("errors", 0) + 1
        st.update({"status": f"fetch-{status}", "errors": errs, "last_check": today,
                   "backoff_until": str(date.fromisoformat(today) + timedelta(days=7 if errs < 3 else 30))})
        cache[slug] = st
        ev = {"slug": slug, "name": t.get("name"), "kind": "fetch-error",
              "url": url, "detail": f"HTTP {status}", "queued_at": today}
        return f"fetch-{status}", ev
    lh = {k.lower(): v for k, v in headers.items()}
    st["etag"] = lh.get("etag", st.get("etag", ""))
    st["lastmod"] = lh.get("last-modified", st.get("lastmod", ""))
    text = text_of(body)
    bycur = page_figures(text)
    if not bycur:
        st.update({"status": "needs-render", "last_check": today,
                   "backoff_until": str(date.fromisoformat(today) + timedelta(days=30))})
        cache[slug] = st
        ev = {"slug": slug, "name": t.get("name"), "kind": "needs-render",
              "url": url, "detail": "no currency figures in static HTML (likely JS-rendered)",
              "queued_at": today}
        return "needs-render", ev
    sym = CUR_OF.get((t.get("currency") or "USD"))
    code = (t.get("currency") or "USD")
    figs = set(bycur.get(sym, ())) | set(bycur.get(code, ()))
    if not figs:
        st.update({"status": "currency-geo", "last_check": today,
                   "backoff_until": str(date.fromisoformat(today) + timedelta(days=30))})
        cache[slug] = st
        ev = {"slug": slug, "name": t.get("name"), "kind": "currency-geo",
              "url": url, "detail": f"page renders {sorted(bycur)} figures but none in record currency {code} (geo-pricing?); verify via vendor llms.txt/help docs",
              "queued_at": today}
        return "currency-geo", ev
    want = expected_figures(t)
    missing = {f for f in want if f not in figs}
    if not missing:
        st.update({"status": "confirmed", "last_check": today, "errors": 0, "backoff_until": ""})
        cache[slug] = st
        return "confirmed", None
    st.update({"status": "mismatch", "last_check": today,
               "backoff_until": str(date.fromisoformat(today) + timedelta(days=30))})
    cache[slug] = st
    ev = {"slug": slug, "name": t.get("name"), "kind": "mismatch", "url": url,
          "detail": f"catalog expects {sorted(want)} ({code}); page shows {sorted(figs)[:12]}; missing {sorted(missing)}",
          "queued_at": today}
    return "mismatch", ev


def _sync_rationale_dates(slugs, today):
    """Move pricing-transparency evidence dates with confirmed records."""
    n = 0
    for f in ("tools/score-content-a.json", "tools/score-content-b.json"):
        p = ROOT / f
        try:
            dd = json.loads(p.read_text())
        except (OSError, ValueError):
            continue
        for t in dd.get("tools", []):
            if t.get("slug") not in slugs:
                continue
            try:
                ev = t["pillars"]["pricing_transparency"]["evidence"]
            except KeyError:
                continue
            new = re.sub(r"verified \d{4}-\d{2}-\d{2}", f"verified {today}", ev)
            if new != ev:
                t["pillars"]["pricing_transparency"]["evidence"] = new
                n += 1
        p.write_text(json.dumps(dd, indent=1, ensure_ascii=False))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, default=12)
    ap.add_argument("--budget-seconds", type=int, default=600)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    today = date.today().isoformat()

    tools = json.loads(TOOLS_JSON.read_text())
    recs = [t for t in tools if isinstance(t, dict) and t.get("status") == "active"]
    try:
        cache = json.loads(CACHE_JSON.read_text())
    except (OSError, ValueError):
        cache = {}
    try:
        queue = json.loads(QUEUE_JSON.read_text())
        queue = queue if isinstance(queue, list) else []
    except (OSError, ValueError):
        queue = []

    cited = money_slugs()
    impr = impressions()
    scored = []
    for t in recs:
        du = (t.get("date_updated") or "")[:10]
        try:
            overdue = max(0, (date.fromisoformat(today) - date.fromisoformat(du)).days - 21)
        except ValueError:
            overdue = 999
        w = 1 + math.log10(1 + impr.get(t["slug"], 0))
        cited_boost = 2.0 if t["slug"] in cited else 1.0
        scored.append((overdue * w * cited_boost, t))
    scored.sort(key=lambda x: -x[0])

    fetcher = PoliteFetcher()
    results = {}
    new_evidence = []
    n = 0
    for score, t in scored:
        if n >= args.cap or time.time() - t0 > args.budget_seconds:
            break
        if score <= 0 and (cache.get(t["slug"], {}).get("backoff_until", "") > today):
            continue
        if score <= 0:
            # still fresh and never problematic: only check when overdue
            stale = cache.get(t["slug"], {})
            if not stale.get("errors") and (t.get("date_updated") or "")[:10] >= str(date.fromisoformat(today) - timedelta(days=21)):
                continue
        status, ev = check_record(t, cache, fetcher, today)
        results[status] = results.get(status, 0) + 1
        if ev:
            new_evidence.append(ev)
        n += 1

    # queue maintenance: drop items resolved since (record re-verified after queueing)
    by_slug = {t["slug"]: t for t in recs}
    queue = [q for q in queue
             if (by_slug.get(q.get("slug"), {}).get("date_updated") or "")[:10] <= (q.get("queued_at") or "")]
    seen = {q.get("slug") for q in queue}
    for ev in new_evidence:
        if ev["slug"] not in seen:
            queue.append(ev)
            seen.add(ev["slug"])
    queue = queue[-60:]

    confirmed = [t["slug"] for _, t in scored[:n]
                 if cache.get(t["slug"], {}).get("status", "").startswith("confirmed")]
    if not args.dry_run:
        if confirmed:
            for t in recs:
                if t["slug"] in confirmed:
                    t["date_updated"] = today
            TOOLS_JSON.write_text(json.dumps(tools, indent=1, ensure_ascii=False))
            # r31 H-7 (2026-10-06): the rationale cache lagged record updates
            # as a class (9 date-stale cells). A confirmed re-verification
            # moves the scoring rationale's evidence date with the record —
            # figures confirmed unchanged, so date-only sync is honest.
            _synced = _sync_rationale_dates(set(confirmed), today)
            print(f"- rationale evidence dates synced: {_synced}")
        CACHE_JSON.write_text(json.dumps(cache, indent=1, ensure_ascii=False))
        QUEUE_JSON.write_text(json.dumps(queue, indent=1, ensure_ascii=False))

    print(f"# pricing reverify — {today} (checked {n}, cap {args.cap}{' DRY-RUN' if args.dry_run else ''})")
    for k in sorted(results):
        print(f"- {k}: {results[k]}")
    print(f"- confirmed (date bumped): {len(confirmed)}")
    print(f"- queue depth: {len(queue)}")
    for q in queue[:10]:
        print(f"  ! [{q['kind']}] {q['slug']}: {q['detail'][:100]}")
    if queue:
        print("\nQUEUE-NONEMPTY")
        return 1
    print("\nAll clear.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
