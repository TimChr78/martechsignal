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

    body = [f'<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span>{esc(h1)}</span></nav>',
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
    # r25 L-19 (2026-10-05): visible hub child links are relative (site
    # convention, matching nav/crumb hrefs) - schema hasPart keeps absolute
    # URLs. Previously every hub mixed both forms.
    items = "".join(
        f'<li><a href="{c["url"].replace("https://martechsignal.com", "")}">{esc(c["title"])}</a><br>{esc(c["meta"])}</li>'
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
        "@id": base,  # r17 M-9: addressable hub node, joinable from children
        "name": h1,
        "url": base,
        "description": meta,
        # r25 L-16 (2026-10-05): the CollectionPage itself carries the
        # breadcrumb edge - previously only hasPart children did, pointing
        # at a BreadcrumbList the hub node never claimed.
        "breadcrumb": {"@id": base + "#breadcrumb"},
        "hasPart": [{"@type": "WebPage", "name": c["title"], "url": c["url"]}
                    for c in children],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "@id": base + "#breadcrumb",
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
    'instead of estimating. The pages state pick-conditions rather than '
    'crowning an overall winner - each leaf calls out where one side wins '
    'for a stated requirement, and the verdict block names who should pick '
    'which. Declarations without context hide the deployment, budget and '
    'licensing constraints that actually decide these choices.',

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
    # r14 M-10 (2026-09-29): counts derived from the children lists, not
    # hardcoded — "Three best-of lists" shipped while /best/ grew to 15.
    _num = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
            12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen"}
    _best_kids = _children(BESTX, "/best/")
    _vs_kids = _children(VSX, "/vs/")
    _alt_kids = _children(ALT, "/alternatives/")
    _nb = _num.get(len(_best_kids), str(len(_best_kids)))
    _nv = _num.get(len(_vs_kids), str(len(_vs_kids)))
    _na = _num.get(len(_alt_kids), str(len(_alt_kids)))
    # r15 M-6 (2026-09-29): the intro prose named 3 lists while the section
    # holds 15 — derive the live-list sentence (and its links) from the same
    # children that feed hasPart and the visible list below.
    _best_links = " ".join(
        f'<a href="{c["url"]}">{esc(c["title"])}</a>' + ("," if i < len(_best_kids) - 2 else " and" if i < len(_best_kids) - 1 else ".")
        for i, c in enumerate(_best_kids))
    _best_intro = [BEST_INTRO[0].split("Three lists are live:")[0] +
                   f"{_nb} lists are live: " + _best_links] + BEST_INTRO[1:]
    # r16 H-3 (2026-09-29): the /vs/ hub said "three comparisons" while
    # linking 7 of 10, and /alternatives/ said "three" while holding 4.
    # Same derived pattern as /best/: live-list sentence + links from the
    # same children that feed hasPart and the visible list. Short names
    # come from slugs (pair) or title prefixes (guide target).
    _brands = {"hubspot": "HubSpot", "nocodb": "NocoDB", "nocobase": "NocoBase"}
    def _pair(slug):
        return " ".join("vs" if w == "vs" else _brands.get(w, w.upper() if w == "crm" else w.capitalize())
                           for w in slug.split("-"))
    _vs_slugs = [c["url"].rstrip("/").split("/")[-1] for c in _vs_kids]
    _vs_links = " ".join(
        f'<a href="https://martechsignal.com/vs/{s}/">{_pair(s)}</a>' + ("," if i < len(_vs_slugs) - 2 else " and" if i < len(_vs_slugs) - 1 else ".")
        for i, s in enumerate(_vs_slugs))
    _vs_intro = [VS_INTRO[0].split("The three comparisons live now are")[0] +
                 f"{_nv} comparisons are live now: " + _vs_links +
                 " Each pair overlaps enough that teams genuinely weigh one "
                 "against the other; the pages exist because the choice is close."] + VS_INTRO[1:]
    import json as _json
    _alt_raw = _json.loads(ALT.read_text())["pages"]
    _alt_targets = [p["title"].replace("Best ", "").split(" (")[0] for p in _alt_raw]
    _alt_counts = [len(p.get("items") or []) for p in _alt_raw]
    _alt_links = " ".join(
        f'<a href="https://martechsignal.com/alternatives/{p["slug"]}/">{t} ({n} compared)</a>' + ("," if i < len(_alt_raw) - 2 else " and" if i < len(_alt_raw) - 1 else ".")
        for i, (p, t, n) in enumerate(zip(_alt_raw, _alt_targets, _alt_counts)))
    _alt_intro = [ALT_INTRO[0].split("Three are live:")[0] +
                  f"{_na} are live: " + _alt_links,
                  ALT_INTRO[1].replace(
                      "Each guide lists five alternatives drawn from the same category",
                      f"Each guide lists every credible alternative the catalog holds for its target "
                      f"(from {min(_alt_counts)} to {max(_alt_counts)} per guide), drawn from the same category"),
                  ALT_INTRO[2].replace("This is a deliberate set of three,",
                                       f"This is a deliberate set of {_na.lower()},"),
                  ALT_INTRO[3].replace("What it can do is narrow five credible options",
                                       "What it can do is narrow the field")]
    sections = [
        ("best", "Best-of lists",
         "Best-of lists (2026): open-source CRM, workflow, AI SEO",
         f"{_nb} best-of lists with catalog-grounded pricing, a verdict and "
         "a skip-it line per tool: open-source CRM, workflow automation "
         "platforms and AI SEO.",
         _best_intro, _best_kids),
        ("vs", "Head-to-head comparisons",
         "Head-to-head comparisons (2026)",
         f"{_nv} head-to-head comparisons of overlapping marketing tools, "
         "built on catalog facts with a clear pick for each team.",
         _vs_intro, _vs_kids),
        ("alternatives", "Alternatives guides",
         "Alternatives guides (2026)",
         f"{_na} alternatives guides: credible options besides "
         f"{', '.join(t.removesuffix(' alternatives') for t in _alt_targets[:-1])} and {_alt_targets[-1].removesuffix(' alternatives')}, with who each pick fits and vendor-published pricing.",
         _alt_intro, _alt_kids),
    ]
    for section, h1, seo_title, meta, intro, children in sections:
        assert children, f"hub /{section}/ has no live children"
        n = _hub(section, h1, seo_title, meta, intro, children)
        print(f"  wrote {section}/index.html ({n} children listed, "
              f"intro ~{sum(len(p.split()) for p in intro)} words)")
    _money_strip(_best_kids, _vs_slugs, _alt_raw)


def _money_strip(best_kids, vs_slugs, alt_pages):
    """r16 H-3 (2026-09-29): the homepage linked none of the 29 money
    leaves, so the pages built to rank were unreachable from the site's own
    entry point. Same marker pattern as the categories strip: a generated
    block between money-strip markers, counts and links derived from the
    same sources as the hubs. No new CSS (plain paragraphs, existing
    section shell)."""
    _brands = {"hubspot": "HubSpot", "nocodb": "NocoDB", "nocobase": "NocoBase"}
    def _pair(slug):
        return " ".join("vs" if w == "vs" else _brands.get(w, w.upper() if w == "crm" else w.capitalize())
                           for w in slug.split("-"))
    _best = ", ".join(
        f'<a href="https://martechsignal.com/best/{c["url"].rstrip("/").split("/")[-1]}/">'
        f'{esc(c["title"].split(" (")[0])}</a>' for c in best_kids)
    _vs = ", ".join(
        f'<a href="https://martechsignal.com/vs/{s}/">{_pair(s)}</a>' for s in vs_slugs)
    _al = ", ".join(
        f'<a href="https://martechsignal.com/alternatives/{p["slug"]}/">'
        f'{esc(p["title"].replace("Best ", "").split(" (")[0])}</a>' for p in alt_pages)
    strip = (
        "<!-- money-strip:start (generated by tools/build_hubs.py) -->\n"
        '<section class="section">\n'
        '  <div class="section-head">\n'
        '    <h2>Comparisons and best-of lists</h2>\n'
        '    <a href="/vs/">ALL COMPARISONS →</a>\n'
        '  </div>\n'
        '  <p style="max-width:62ch">Verdicts with receipts: every list below names what each tool costs '
        'from the vendor\u2019s own pricing page, what it fits worst, and who should skip it. '
        'The head-to-head comparisons state pick-conditions instead of a winner; '
        'the best-of lists and tool pages give the verdict. '
        'Start from the comparison or list that matches your shortlist, then read the linked tool pages for dated numbers.</p>\n'
        f'  <p style="max-width:78ch">{len(vs_slugs)} head-to-head comparisons: {_vs}. '
        f'More on the <a href="/vs/">comparisons hub</a>.</p>\n'
        f'  <p style="max-width:78ch">{len(best_kids)} best-of lists: {_best}. '
        f'More on the <a href="/best/">best-of hub</a>.</p>\n'
        f'  <p style="max-width:78ch">{len(alt_pages)} alternatives guides: {_al}. '
        f'More on the <a href="/alternatives/">alternatives hub</a>.</p>\n'
        "</section>\n"
        "<!-- money-strip:end -->"
    )
    p = ROOT / "index.html"
    html = p.read_text()
    start = "<!-- money-strip:start"
    end = "<!-- money-strip:end -->"
    anchor = '<section class="section">\n  <div class="section-head">\n    <h2>How to read the directory</h2>'
    if start in html and end in html:
        i = html.index(start)
        j = html.index(end) + len(end)
        html = html[:i] + strip + html[j:]
    else:
        assert anchor in html, "homepage anchor for money strip not found"
        html = html.replace(anchor, strip + "\n\n" + anchor, 1)
    p.write_text(html)
    print(f"  homepage money strip: {len(best_kids)}/{len(vs_slugs)}/{len(alt_pages)} links")


if __name__ == "__main__":
    build()
