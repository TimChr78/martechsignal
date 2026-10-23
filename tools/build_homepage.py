#!/usr/bin/env python3
"""build_homepage.py - regenerate the front page Tool index section with grounded data.

Grounding: GSC impressions (28d, primary) then GitHub stars (secondary).
Counts: "All {N} tools" in the section head and "See all {N} tools" link,
both derived from the tools.json active count.

Reads:
  - tools/tools.json            (active slugs, names, categories, taglines)
  - tools/github-history.json   (latest snapshot stars)
  - /opt/data/gsc-pages-28d.json (per-page GSC impressions; optional - falls back to
    stars-only). Written by tools/gsc_perf.py as a list of {page, clicks,
    impressions, position} rows; a {url: {...}} dict is also accepted.

Writes:
  - index.html (Tool index section + homepage-link counts only; LATEST section untouched)

Usage: python3 tools/build_homepage.py [--dry-run]
"""
import json, re, sys
import html as _html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
GH_HISTORY = ROOT / "tools" / "github-history.json"
GSC_FILE = Path("/home/hermes/.hermes/data/gsc-pages-28d.json")  # durable (opt/data is wiped on Hermes updates)
INDEX = ROOT / "index.html"

SHOW = 8  # tool rows shown on the front page

# Tag mapping (category -> front-page label, sentence case for the redesign)
TAGS = {
    "workflow-automation": "Automation", "email-marketing": "Email", "crm": "CRM",
    "analytics": "Analytics", "seo": "SEO", "agent-skills": "Agent skills",
    "marketing-automation": "Marketing automation", "personalization": "Personalization",
    "advertising": "Advertising", "social-media": "Social", "content-ai": "Content AI",
    "chatbots": "Chatbots", "open-source": "Open source",
}

def load_gsc_impressions(path):
    """GSC page cache -> {url: impressions}.

    tools/gsc_perf.py writes this cache as a LIST of rows
    ({"page", "clicks", "impressions", "position"}); an earlier revision used a
    {url: {...}} dict, so accept both. Returning {} just falls back to the
    stars-only ranking, which is why this bug was silent for so long.
    """
    try:
        raw = json.load(open(path))
    except Exception as ex:
        print(f"  (GSC cache unreadable: {ex} - ranking on stars only)")
        return {}
    out = {}
    if isinstance(raw, dict):
        for url, val in raw.items():
            if isinstance(val, dict):
                out[url] = val.get("impressions", 0) or 0
            elif isinstance(val, (int, float)):
                out[url] = val
    elif isinstance(raw, list):
        for row in raw:
            if not isinstance(row, dict):
                continue
            url = row.get("page") or row.get("url")
            if not url:
                keys = row.get("keys")
                url = keys[0] if isinstance(keys, list) and keys else None
            if url:
                out[url] = row.get("impressions", 0) or 0
    else:
        print(f"  (GSC cache has unexpected type {type(raw).__name__} - ranking on stars only)")
        return {}
    return out


def main():
    dry = "--dry-run" in sys.argv
    tools = json.load(open(TOOLS_JSON))
    tl = tools if isinstance(tools, list) else tools.get("tools", [])
    active = [t for t in tl if t.get("status", "active") == "active"]
    total = len(active)

    # stars from latest snapshot
    stars = {}
    if GH_HISTORY.exists():
        gh = json.load(open(GH_HISTORY))
        if gh:
            stars = gh[-1].get("repos", {})

    # GSC impressions (optional)
    gsc = {}
    if GSC_FILE.exists():
        gsc = load_gsc_impressions(GSC_FILE)
        print(f"  GSC: {len(gsc)} pages in {GSC_FILE.name}")
    else:
        print(f"  GSC: {GSC_FILE} missing - ranking on stars only")

    rows = []
    for t in active:
        slug = t["slug"]
        if slug == "tools":
            continue
        impr = gsc.get(f"https://martechsignal.com/tools/{slug}/", 0)
        st = stars.get(slug, {}).get("stars", 0) or t.get("github_stars") or 0
        rows.append({"slug": slug, "name": t.get("name", slug), "impr": impr, "stars": st,
                     "cat": t.get("category", ""), "tagline": t.get("tagline", "")})

    # Primary rank: GSC impressions; secondary: stars. Tools with zero on both rank last (never shown).
    ranked = sorted(rows, key=lambda r: (-r["impr"], -r["stars"]))
    picks = [r for r in ranked if r["impr"] > 0][:SHOW]
    if len(picks) < SHOW:  # backfill with star power
        for r in ranked:
            if r not in picks and r["stars"] > 0:
                picks.append(r)
            if len(picks) == SHOW:
                break

    lines = []
    for r in picks:
        tag = TAGS.get(r["cat"], r["cat"].replace("-", " ").capitalize())
        take = _html.escape(r["tagline"] or f"{r['name']} review", quote=False)
        name = _html.escape(r["name"], quote=False)
        star_disp = f"{int(r['stars']):,}" if r["stars"] else "n/a"
        lines.append(
            f'      <tr><td class="name"><a href="/tools/{r["slug"]}/">{name}</a></td>'
            f'<td class="desc">{take}</td><td><span class="tag">{tag}</span></td>'
            f'<td class="num">{star_disp}</td></tr>')
    section = f'''<section class="section">
  <div class="sec-head"><h2>Tool index</h2><a href="/tools/">All {total} tools →</a></div>
  <table class="tindex">
    <thead><tr><th>Tool</th><th class="desc">What it is</th><th>Category</th><th class="num">GitHub stars</th></tr></thead>
    <tbody>
{chr(10).join(lines)}
    </tbody>
  </table>
  <a class="more-tools" href="/tools/">See all {total} tools →</a>
</section>'''

    html = INDEX.read_text()
    new_html, n = re.subn(
        r'<section class="section">\s*<div class="sec-head"><h2>Tool index</h2>.*?</section>',
        section, html, count=1, flags=re.S)
    if n != 1:
        print("ERROR: Tool index section not found")
        sys.exit(1)
    # hero stat + twitter meta were hand-maintained and rotted at 133; derive from total
    new_html = re.sub(r'(id="s1">)\d+', rf'\g<1>{total}', new_html, count=1)
    # SX-4: the posts stat was hand-maintained at 33; count published posts from blog/
    n_posts = sum(1 for p in (ROOT / "blog").iterdir()
                  if p.is_dir() and (p / "index.html").exists()) if (ROOT / "blog").is_dir() else 0
    new_html = re.sub(r'(id="s2">)\d+', rf'\g<1>{n_posts}', new_html, count=1)
    new_html = re.sub(r'(twitter:description" content=")\d+( AI marketing tools)',
                      rf'\g<1>{total}\g<2>', new_html, count=1)

    if dry:
        print(section)
        return
    # A2 L1 (2026-09-26): the homepage cache-bust literal went stale again; sync it
    # to the same md5[:8] scheme page_shell uses so it can never drift.
    import hashlib as _h
    _cv = _h.md5((ROOT / "style.css").read_bytes()).hexdigest()[:8]
    new_html = re.sub(r'style\.css\?v=[a-f0-9]+', f'style.css?v={_cv}', new_html, count=1)
    INDEX.write_text(new_html)
    print(f"Homepage tool index rewritten: {total} total, top rows: "
          + ", ".join(f"{r['slug']}({r['impr']} impr/{r['stars']}*)" for r in picks))

if __name__ == "__main__":
    main()
