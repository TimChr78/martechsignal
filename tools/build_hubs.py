#!/usr/bin/env python3
"""Section hub index pages for /best/, /vs/ and /alternatives/ (audit H-4).

Before this, all three section hubs returned 404 while their child pages
(3 per section) were live and the sitemap listed the hub URLs: breadcrumb
entry points into each section died at the hub level.

Outputs (each section gets index.html + index.md):
  - best/index.html
  - vs/index.html
  - alternatives/index.html

Reuses page_shell from build_tools so head/masthead/footer stay canonical.
Child titles and one-line summaries are read from the same content JSONs the
child builders render (bestx-content.json, vsx-content.json,
alternatives-content.json), so a hub can never list a page the child builder
no longer produces - if a child is removed from the JSON, the hub drops it.

Schema (R5 rule: product typing requires offers/review/aggregateRating, so a
hub stays CollectionPage + plain WebPage hasPart entries) + a BreadcrumbList
matching the children's shape. Markdown mirrors match the generic extract
format build_tools writes for other pages.

Editorial guard: the hub body is asserted free of em/en dashes, curly quotes
and the banned filler words before it is written.

Runs BEFORE build_tools.py in deploy.sh: the sitemap scan reads the generated
index.html files.
"""
import json
from pathlib import Path

from build_tools import page_shell, esc, ROOT

BESTX = ROOT / "tools" / "bestx-content.json"
VSX = ROOT / "tools" / "vsx-content.json"
ALT = ROOT / "tools" / "alternatives-content.json"

# Editorial hard rules (site-wide + audit): none of these may reach a hub page.
BANNED = ("\u2014", "\u2013", "\u201c", "\u201d", "\u2018", "\u2019",
          "delve", "crucial", "leverage")


def _children(path, url_prefix):
    pages = json.loads(path.read_text())["pages"]
    return [{"title": p["title"], "meta": p["meta"],
             "url": f"https://martechsignal.com{url_prefix}{p['slug']}/"}
            for p in pages]


def _check_clean(text, where):
    low = text.lower()
    for bad in BANNED:
        assert bad not in low, f"banned token {bad!r} in {where}"


def _hub(section, h1, seo_title, meta, intro, children):
    base = f"https://martechsignal.com/{section}/"
    for text, where in ((h1, "h1"), (seo_title, "seo_title"), (meta, "meta")):
        _check_clean(text, f"{section}/{where}")

    body = [f'<nav class="crumb"><a href="/">Home</a> / <span>{esc(h1)}</span></nav>',
            f"<h1>{esc(h1)}</h1>"]
    for para in intro:
        _check_clean(para, f"{section}/intro")
        body.append(f"<p>{para}</p>")
    # M15 (2026-09-27): expanded guide sections (criteria, use cases, process).
    # Content lives in tools/hub-guides.json so the humanizer pass has one home.
    _guides = json.loads((Path(__file__).resolve().parent / "hub-guides.json").read_text())
    for _sec in _guides.get(section, []):
        _check_clean(_sec["h2"], f"{section}/guide-h2")
        body.append(f"<h2>{esc(_sec['h2'])}</h2>")
        for para in _sec["paras"]:
            _check_clean(para, f"{section}/guide-para")
            body.append(f"<p>{para}</p>")
    items = "".join(
        f'<li><a href="{c["url"]}">{esc(c["title"])}</a><br>{esc(c["meta"])}</li>'
        for c in children)
    body.append("<h2>Pages in this section</h2>")
    body.append(f'<ul class="hub-list">{items}</ul>')
    body.append('<p class="alt-back">Prices and features on every page in this '
                'section come from the vendor\'s own published materials, as '
                'catalogued on the tool pages. Read <a href="/methodology/">how '
                'we evaluate</a>.</p>')
    _check_clean("\n".join(body), f"{section}/body")

    schema = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": h1,
        "url": base,
        "description": meta,
        "hasPart": [{"@type": "WebPage", "name": c["title"], "url": c["url"]}
                    for c in children],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": h1, "item": base},
        ],
    }
    out_dir = ROOT / section
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(page_shell(
        seo_title, meta, f"/{section}/", "\n".join(body), [schema, breadcrumb]))
    (out_dir / "index.md").write_text("\n".join([
        f"# {seo_title}", "", meta, "",
        f"- Page: {base}",
        "- Format: markdown mirror of the page above", ""]))
    return len(children)


BEST_INTRO = [
    'Every page in this section is a best-of list with a verdict per tool: '
    'what it does well, what it costs by the vendor\'s own pricing page, and '
    'the setup it fits worst. Three lists are live: '
    '<a href="/best/open-source-crm/">best open-source CRM tools</a>, '
    '<a href="/best/workflow-automation-tools/">best workflow automation '
    'tools</a> and <a href="/best/ai-seo-tools/">best AI SEO tools</a>.',

    'The facts come from the tool directory itself. Every entry links to the '
    'tool\'s full page, where pricing, licence, integrations and AI features '
    'are itemized with a verification date. The verdicts hold to the same '
    'rule: prices only as the vendor publishes them, never a third-party '
    'estimate, and open-source licence claims you can check against the '
    'repository.',

    'Method, stated plainly: researched from public documentation, the '
    'source repository where one exists, and vendor materials. Not a '
    'hands-on review. <a href="/methodology/">How we evaluate</a> documents '
    'the standard each page follows, and the <a href="/corrections/">'
    'corrections page</a> records anything published here that turned out '
    'wrong.',

    'Use the lists to build a shortlist, not to close a decision. A verdict '
    'names the tool this catalog would assign to a specific job; the skip-it '
    'line names the buyer who should not bother with it. Read the two or '
    'three entries that match your situation, open the tool pages for those, '
    'and treat the dated numbers there as the source of truth if a list has '
    'drifted.',
]

VS_INTRO = [
    'A versus page answers one question: two tools overlap, so which one '
    'fits which team? The three comparisons live now are '
    '<a href="/vs/n8n-vs-zapier/">n8n vs Zapier</a>, '
    '<a href="/vs/nocodb-vs-nocobase/">NocoDB vs NocoBase</a> and '
    '<a href="/vs/matomo-vs-plausible/">Matomo vs Plausible</a>. Each pair '
    'overlaps enough that teams genuinely weigh one against the other; the '
    'pages exist because the choice is close.',

    'Each page has the same build. A fact table first: pricing as the '
    'vendors publish it, self-hosting, public API, and the integration '
    'counts the catalog holds. Then notes on the dimensions where the pair '
    'actually differs, and a closing section with the conditions: pick this '
    'one if your team looks like this, pick the other if it looks like '
    'that. Both tools\' full assessments are one click away.',

    'Numbers come from the catalog, never from a vendor\'s own comparison '
    'page, and where the catalog holds no verified figure the table says so '
    'instead of estimating. Neither side is declared the winner. '
    'Declarations hide the deployment, budget and licensing context that '
    'actually decides these choices, so the pages state conditions instead.',

    'Method: researched from public documentation, the source repository '
    'where one exists, and vendor materials. Not a hands-on review. If a '
    'decision stays close after reading a comparison, the two linked tool '
    'pages carry the fuller record, every number dated, with anything found '
    'wrong logged on the corrections page.',
]

ALT_INTRO = [
    'The alternatives guides cover the searches where vendor comparison '
    'pages are least trustworthy: someone shopping for options besides a '
    'tool they already know. Three are live: '
    '<a href="/alternatives/hubspot-crm/">HubSpot CRM alternatives</a>, '
    '<a href="/alternatives/zapier/">Zapier alternatives</a> and '
    '<a href="/alternatives/matomo/">Matomo alternatives</a>.',

    'Each guide lists five alternatives drawn from the same category as the '
    'target tool, so the options are actually comparable, and never includes '
    'the target itself. Every entry states who the alternative is best for, '
    'who should skip it, and why it earns a place. Pricing appears only as '
    'the vendor\'s own pricing page states it: a tool that quotes price on '
    'request stays quote-only here too. Open-source entries link to their '
    'repositories, so licence and maintenance claims can be checked.',

    'This is a deliberate set of three, not a generated sweep. New guides '
    'follow the same structure as the catalog grows, grounded in the same '
    '<a href="/tools/">tool directory</a> data the rest of the site runs on.',

    'The honest limits, before anything else: a guide cannot test migration '
    'effort, support quality, or how a tool behaves at your data volume, and '
    'it does not pretend to. What it can do is narrow five credible options '
    'down to two. Start from the two that survive, read their tool pages for '
    'dated pricing and licence facts, and read <a href="/methodology/">how '
    'we evaluate</a> for the standard the whole section follows.',
]


def build():
    sections = [
        ("best", "Best-of lists",
         "Best-of lists: open-source CRM, workflow automation, AI SEO (2026)",
         "Three best-of lists: open-source CRM, workflow automation platforms "
         "and AI SEO tools, each with catalog-grounded pricing, a verdict and "
         "a skip-it line per tool.",
         BEST_INTRO, _children(BESTX, "/best/")),
        ("vs", "Head-to-head comparisons",
         "Head-to-head comparisons: n8n, NocoDB and Matomo (2026)",
         "Eight head-to-head comparisons: n8n vs Zapier, NocoDB vs NocoBase "
         "and Matomo vs Plausible, built on catalog facts with a clear pick "
         "for each team.",
         VS_INTRO, _children(VSX, "/vs/")),
        ("alternatives", "Alternatives guides",
         "Alternatives guides: HubSpot CRM, Zapier, Matomo (2026)",
         "Three alternatives guides: options besides HubSpot CRM, Zapier and "
         "Matomo, with who each pick fits, who should skip it and "
         "vendor-published pricing.",
         ALT_INTRO, _children(ALT, "/alternatives/")),
    ]
    for section, h1, seo_title, meta, intro, children in sections:
        assert children, f"hub /{section}/ has no live children"
        n = _hub(section, h1, seo_title, meta, intro, children)
        print(f"  wrote {section}/index.html ({n} children listed, "
              f"intro ~{sum(len(p.split()) for p in intro)} words)")


if __name__ == "__main__":
    build()
