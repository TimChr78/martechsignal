#!/usr/bin/env python3
"""build_homepage.py — regenerate the front page Tool index section with grounded data.

Grounding: GSC impressions (28d, primary) then GitHub stars (secondary).
Counts: ALL {N} TOOLS + "+{N-8} MORE TOOLS" derived from tools.json active count.

Reads:
  - tools/tools.json            (active slugs, names, categories, taglines)
  - tools/github-history.json   (latest snapshot stars)
  - /opt/data/gsc-pages-28d.json (per-page GSC impressions; optional — falls back to stars-only)

Writes:
  - index.html (Tool index section + homepage-link counts only; LATEST section untouched)

Usage: python3 tools/build_homepage.py [--dry-run]
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
GH_HISTORY = ROOT / "tools" / "github-history.json"
GSC_FILE = Path("/opt/data/gsc-pages-28d.json")
INDEX = ROOT / "index.html"

SHOW = 8  # tool rows shown on the front page

# Tag mapping (category -> front-page tag label, matches existing style)
TAGS = {
    "workflow-automation": "AUTOMATION", "email-marketing": "EMAIL", "crm": "CRM",
    "analytics": "ANALYTICS", "seo": "SEO", "agent-skills": "AGENT SKILLS",
    "marketing-automation": "MARKETING AUTO", "personalization": "PERSONALIZATION",
    "advertising": "ADS", "social-media": "SOCIAL", "content-ai": "CONTENT AI",
    "chatbots": "CHATBOTS", "open-source": "OPEN SOURCE",
}

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
        gsc = json.load(open(GSC_FILE))

    rows = []
    for t in active:
        slug = t["slug"]
        if slug == "tools":
            continue
        impr = gsc.get(f"https://martechsignal.com/tools/{slug}/", {}).get("impressions", 0)
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
        tag = TAGS.get(r["cat"], r["cat"].upper())
        take = r["tagline"] or f"{r['name']} review"
        lines.append(
            f'    <a class="tool-row" href="/tools/{r["slug"]}/"><span class="name">{r["name"]}</span>'
            f'<span class="take">{take}</span><span class="tag">{tag}</span></a>')
    section = f'''<section class="section">
  <div class="section-head">
    <h2>Tool index</h2>
    <a href="/tools/">ALL {total} TOOLS →</a>
  </div>
  <div class="tool-index">
{chr(10).join(lines)}
  </div>
  <a class="more-tools" href="/tools/">+{total - SHOW} MORE TOOLS →</a>
</section>'''

    html = INDEX.read_text()
    new_html, n = re.subn(
        r'<section class="section">\s*<div class="section-head">\s*<h2>Tool index</h2>.*?</section>',
        section, html, count=1, flags=re.S)
    if n != 1:
        print("ERROR: Tool index section not found")
        sys.exit(1)
    # sanity: no other stale counts in headers
    new_html = new_html.replace('tools/">+92', f'tools/">+{total - SHOW}')

    if dry:
        print(section)
        return
    INDEX.write_text(new_html)
    print(f"Homepage tool index rewritten: {total} total, top rows: "
          + ", ".join(f"{r['slug']}({r['impr']} impr/{r['stars']}*)" for r in picks))

if __name__ == "__main__":
    main()
