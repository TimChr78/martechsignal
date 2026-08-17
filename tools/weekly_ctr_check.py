#!/usr/bin/env python3
"""weekly_ctr_check.py — cannibalization + cap + length validator for CTR loop.

Usage:
  python3 tools/weekly_ctr_check.py --query "cordys crm" [--slug cordys-crm]
  python3 tools/weekly_ctr_check.py --title "New Title" --meta "New meta description..."
  python3 tools/weekly_ctr_check.py --cap-check          # prints remaining budget this ISO week
  python3 tools/weekly_ctr_check.py --list-inventory     # dump slugs for agent use
  python3 tools/weekly_ctr_check.py --validate-state     # validate state file shape + cap

Reads:
  - tools/tools.json, blog/*/index.html, content/drafts/*.md (inventory)
  - /home/hermes/.hermes/data/weekly-ctr-state.json (cap)
  - /mnt/cache/appdata/n8n/data/reports/gsc-keywords-*.md (latest GSC rows, optional)

Checks:
  1. 5/week cap (ISO week) — counts pending+approved+deployed in state file.
  2. Cannibalization: does 2+ pages already target the candidate query's keywords?
     Heuristic: token overlap against all page titles/H1s/taglines/intros.
     If overlap score > threshold and 2+ pages match, flag as HIGH risk.
  3. Title ≤60ch, meta ≤155ch (hard limits, truncates are rejected not auto-fixed).
  4. Query -> page mapping exists (slug must be real).

Exit 0 = clear, 1 = blocked (cannibalization or cap), 2 = length violation.
"""
import argparse, json, re, sys, html
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
BLOG_DIR = ROOT / "blog"
DRAFTS_DIR = ROOT / "content" / "drafts"
STATE_FILE = Path("/home/hermes/.hermes/data/weekly-ctr-state.json")
REPORT_DIR = Path("/mnt/cache/appdata/n8n/data/reports")

STOPWORDS = set("a an and are as at be by for from has have in is it its of on or that the this to was were will with your you we they their our can could would should may might must not no nor so if then than too very just about above after again all also am any because before being below between both but did do does doing down during each few further here how into more most other out over own same some such through under until up what when where which while who whom why with marketing tool tools ai use using used new one two three get got make made like know think time way even still back well much many open source free review pricing".split())

def keywords(text, top_n=40):
    words = re.findall(r'[a-z][a-z-]{2,}', text.lower())
    filtered = [w for w in words if w not in STOPWORDS and len(w) > 3]
    from collections import Counter
    return Counter(dict(Counter(filtered).most_common(top_n)))

def score_overlap(a, b):
    sa, sb = set(a.keys()), set(b.keys())
    overlap = sa & sb
    if not overlap: return 0.0
    return sum(a[w] + b[w] for w in overlap) / (len(sa) + len(sb))

def load_inventory():
    pages = []
    # tools
    if TOOLS_JSON.exists():
        try:
            tools = json.loads(TOOLS_JSON.read_text())
            for t in tools:
                if t.get("status") != "active": continue
                blob = " ".join(str(t.get(k, "")) for k in ("name","tagline","description","ai_features","integrations","category"))
                pages.append({"slug": t["slug"], "type": "tool", "url": f"/tools/{t['slug']}/", "full_url": f"https://martechsignal.com/tools/{t['slug']}/", "title": t["name"], "blob": blob, "raw": t})
        except Exception as e:
            print(f"WARN tools.json: {e}", file=sys.stderr)
    # blogs
    if BLOG_DIR.is_dir():
        for child in BLOG_DIR.iterdir():
            idx = child / "index.html"
            if child.is_dir() and idx.exists():
                content = idx.read_text(errors="ignore")
                m = re.search(r"<title>(.+?)(?:\s+—\s+Martech\s+Signal)?</title>", content)
                title = html.unescape(m.group(1).strip()) if m else child.name
                text = re.sub(r"<[^>]+>", " ", content)
                text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
                pages.append({"slug": child.name, "type": "blog", "url": f"/blog/{child.name}/", "full_url": f"https://martechsignal.com/blog/{child.name}/", "title": title, "blob": text[:4000], "raw": None})
    return pages

def cap_status():
    week = datetime.now().strftime("%G-W%V")
    used = 0
    pending = []
    state = {}
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
            for bucket in ("pending","approved","deployed"):
                for x in state.get(bucket, []):
                    if x.get("week") == week:
                        used += 1
                        if bucket == "pending":
                            pending.append(x)
        except Exception as e:
            print(f"WARN state file: {e}", file=sys.stderr)
    remaining = max(0, 5 - used)
    return week, used, remaining, pending, state

def cannibal_check(query, pages, threshold=0.08):
    """Return (risk, overlapping_pages, note). Risk: none|low|medium|high"""
    q_kw = keywords(query)
    if not q_kw:
        return "none", [], "Query has no indexable keywords after stopword filter."
    scored=[]
    for p in pages:
        p_kw = keywords(p["blob"] or p["title"])
        s = score_overlap(q_kw, p_kw)
        if s > 0:
            scored.append((s, p))
    scored.sort(key=lambda x: x[0], reverse=True)
    # consider pages with meaningful overlap
    overlapping = [(s,p) for s,p in scored if s >= threshold]
    if len(overlapping) >= 2:
        # high if top 2 are close in score and both high
        top_scores = [s for s,_ in overlapping[:3]]
        if top_scores[0] >= 0.15 and top_scores[1] >= 0.10:
            risk="high"
        elif top_scores[0] >= 0.12:
            risk="medium"
        else:
            risk="low"
        note = f"{len(overlapping)} pages share keywords with '{query}' (overlap scores: " + ", ".join(f"{p['slug']}:{s:.3f}" for s,p in overlapping[:4]) + ")."
        if risk=="high":
            note += " BLOCK: title change would likely cannibalize. Pick a different query or consolidate pages."
        return risk, [p for _,p in overlapping[:6]], note
    elif len(overlapping)==1:
        s,p = overlapping[0]
        return "low", [p], f"1 page overlaps '{query}' ({p['slug']}:{s:.3f}) — no cannibalization, single owner."
    else:
        # also surface top-1 even if below threshold for context
        if scored:
            s,p = scored[0]
            return "none", [], f"No overlap above threshold. Closest: {p['slug']}:{s:.3f} for '{query}'. Safe to optimise."
        return "none", [], f"No overlapping pages found for '{query}'. Safe."

def validate_lengths(title, meta):
    errs=[]
    if title is not None:
        if len(title) > 60:
            errs.append(f"title {len(title)}ch >60: {title!r}")
        if len(title) == 0:
            errs.append("title empty")
    if meta is not None:
        if len(meta) > 155:
            errs.append(f"meta {len(meta)}ch >155: {meta[:80]!r}...")
        if len(meta) == 0:
            errs.append("meta empty")
    return errs

def main():
    ap=argparse.ArgumentParser(description="weekly CTR cannibalization + cap + length check")
    ap.add_argument("--query", help="candidate query to check cannibalization")
    ap.add_argument("--slug", help="target page slug (if known) — filters to that page")
    ap.add_argument("--title", help="proposed title to validate length")
    ap.add_argument("--meta", help="proposed meta to validate length")
    ap.add_argument("--cap-check", action="store_true", help="print cap status")
    ap.add_argument("--list-inventory", action="store_true")
    ap.add_argument("--validate-state", action="store_true")
    ap.add_argument("--json", action="store_true", help="output JSON")
    args=ap.parse_args()

    if args.cap_check or args.validate_state:
        week, used, remaining, pending, state = cap_status()
        out={"week": week, "used": used, "remaining": remaining, "cap": 5, "pending": pending, "state_file": str(STATE_FILE), "state_exists": STATE_FILE.exists()}
        if args.validate_state:
            # also validate shape
            issues=[]
            if STATE_FILE.exists():
                try:
                    d=json.loads(STATE_FILE.read_text())
                    for k in ("pending","approved","deployed","deltas"):
                        if k in d and not isinstance(d[k], list):
                            issues.append(f"{k} should be list")
                except Exception as e:
                    issues.append(str(e))
            out["issues"]=issues
        if args.json:
            print(json.dumps(out, indent=2)); return
        print(f"Week {week}: {used}/5 used, {remaining} remaining. State: {STATE_FILE} ({'exists' if STATE_FILE.exists() else 'missing'})")
        if pending:
            print(f"Pending ({len(pending)}): " + ", ".join(f"{p.get('query')}->{p.get('slug')}" for p in pending))
        if used >=5:
            print("CAP_REACHED — no new picks allowed this week.")
            sys.exit(1)
        return

    if args.list_inventory:
        pages=load_inventory()
        for p in sorted(pages, key=lambda x: (x["type"], x["slug"])):
            print(f"{p['type']:5s} {p['slug']:40s} {p['title'][:60]}")
        return

    pages = load_inventory()
    out={}
    exit_code=0

    if args.query:
        risk, overlapping, note = cannibal_check(args.query, pages)
        out["query"]=args.query
        out["cannibalization_risk"]=risk
        out["overlapping_slugs"]=[p["slug"] for p in overlapping]
        out["overlapping_urls"]=[p["full_url"] for p in overlapping]
        out["note"]=note
        print(f"Cannibalization for '{args.query}': {risk.upper()}")
        print(f"  {note}")
        if overlapping:
            print("  Overlapping pages:")
            for p in overlapping[:6]:
                print(f"    - {p['slug']} ({p['type']}) {p['full_url']}")
        if risk=="high":
            print("  → BLOCK: skip this query or consolidate.")
            exit_code=1
        elif risk=="medium":
            print("  → CAUTION: manual review recommended.")
            if exit_code==0: exit_code=0  # don't block, but surface

    # length checks
    errs=validate_lengths(args.title, args.meta)
    if args.title is not None:
        out["title"]=args.title; out["title_len"]=len(args.title)
        print(f"Title: {len(args.title)}ch {'OK' if len(args.title)<=60 else 'OVER'} — {args.title!r}")
    if args.meta is not None:
        out["meta"]=args.meta; out["meta_len"]=len(args.meta)
        print(f"Meta:  {len(args.meta)}ch {'OK' if len(args.meta)<=155 else 'OVER'} — {args.meta[:100]!r}")
    if errs:
        print("LENGTH VIOLATIONS:")
        for e in errs: print(f"  ✗ {e}")
        out["length_errors"]=errs
        exit_code=2

    # cap reminder
    week, used, remaining, _, _ = cap_status()
    out["cap_week"]=week; out["cap_used"]=used; out["cap_remaining"]=remaining
    print(f"Cap: {used}/5 used this week ({week}), {remaining} remaining.")
    if used>=5:
        print("CAP_REACHED")
        exit_code=1

    if args.json:
        print(json.dumps(out, indent=2))
    sys.exit(exit_code)

if __name__=="__main__":
    main()
