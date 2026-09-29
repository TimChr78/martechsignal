#!/usr/bin/env python3
def _bestx_li(rec, i):
    """r8 M13 (2026-09-28): retired packs live under /guides/ now; the old
    /tools/ URL 301s and its #app dangles. Route each item to its real home."""
    if rec.get("kind") == "Guide" or rec.get("status") != "active":
        return {"@type": "ListItem", "position": i + 1, "name": rec["name"],
                "item": {"@type": "SoftwareApplication",
                         "@id": f"https://martechsignal.com/guides/{rec['slug']}/#app",
                         "url": f"https://martechsignal.com/guides/{rec['slug']}/",
                         "name": rec["name"]}}
    # r11 M-13 (2026-09-29): bare @id stubs upgraded to typed nodes — same
    # modelling as /categories/ inlines, so all hub families agree.
    return {"@type": "ListItem", "position": i + 1, "name": rec["name"],
            "item": {"@type": "SoftwareApplication",
                     "@id": f"https://martechsignal.com/tools/{rec['slug']}/#app",
                     "url": f"https://martechsignal.com/tools/{rec['slug']}/",
                     "name": rec["name"]}}


"""Best-X and /vs/ page builders (2026-09-26, decided by Tim).

- /best/<slug>/: "best X for Y" list pages (F-C3 pilot, 3 pages).
- /vs/<slug>/: hand-built comparison pages (H9+F-H15 pilot, 3 pages).

Content lives in tools/bestx-content.json and tools/vsx-content.json
(writer-produced, grounded in tools.json); this script only renders it.

Runs BEFORE build_tools.py in deploy.sh so the sitemap scan sees the pages.

Schema discipline (R5, 2026-09-24/26): list items use name+url ListItem
nodes, never bare Product/SoftwareApplication - a product-typed node must
carry offers/review/aggregateRating or GSC flags the whole page.
"""
import json
from pathlib import Path

from build_tools import page_shell, esc, ROOT, pricing_label, out_links, _tool_fact_img
from build_tools import CATEGORY_GUIDES, _pilot_shot

_MOMENTUM_ROWS = None


def _momentum_rows():
    """r11 H-3 (2026-09-29): per-repo star history, computed from the same
    daily snapshots as /trending/ (never hand-copied). Cached per build."""
    global _MOMENTUM_ROWS
    if _MOMENTUM_ROWS is None:
        try:
            import sys as _sys
            _sys.path.insert(0, str(ROOT / "tools"))
            import build_trending as _bt
            _hist, _rows, _s, _e = _bt.load_data()
            _MOMENTUM_ROWS = ({r["slug"]: r for r in _rows}, _s, _e)
        except (OSError, ValueError, SystemExit):
            _MOMENTUM_ROWS = ({}, "", "")
    return _MOMENTUM_ROWS


def _momentum_block(slugs):
    """H-3: one checkable-receipt line per open-source tool with snapshot
    history: stars now, delta over the window, snapshot count, /trending/
    link. Empty when no featured tool has history."""
    _rows, _start, _end = _momentum_rows()
    if not _rows:
        return ""
    import sys as _sys
    _sys.path.insert(0, str(ROOT / "tools"))
    import build_trending as _bt
    _lis = []
    for slug in slugs:
        r = _rows.get(slug)
        if not r:
            continue
        _sign = "+" if r["delta"] >= 0 else ""
        _lis.append(
            f'<li>{esc(r["name"])} - {r["stars"]:,} stars, '
            f'{_sign}{r["delta"]:,} in the {r["days"]}-snapshot window '
            f'to {_end} {_bt.spark_svg(r["series"])} '
            f'<a href="https://github.com/{esc(r["repo"])}" rel="noopener">verify on GitHub</a></li>')
    if not _lis:
        return ""
    return (
        '<section class="hub-links"><h2>Open-source momentum, with receipts</h2>'
        '<p>Star counts we snapshot ourselves every morning - check any of them against GitHub in one click.</p>'
        f'<ul class="momentum">{"".join(_lis)}</ul>'
        '<p><a href="/trending/">All movers on the trending page</a>.</p></section>')

BESTX = ROOT / "tools" / "bestx-content.json"
VSX = ROOT / "tools" / "vsx-content.json"
BEST_DIR = ROOT / "best"
VS_DIR = ROOT / "vs"


def _load_tools():
    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    out = {t["slug"]: t for t in tools}
    # r6 M-2: guides resolve too (they may appear in /best/ lineups), but the
    # platform count excludes them (kind == "Guide").
    gp = ROOT / "tools" / "guides.json"
    if gp.exists():
        out.update({t["slug"]: t for t in json.loads(gp.read_text())})
    return out


def build_best():
    data = json.loads(BESTX.read_text())
    tools_by_slug = _load_tools()
    built = []
    for page in data["pages"]:
        items = page["items"]
        for it in items:
            assert it["slug"] in tools_by_slug, f"unknown tool slug {it['slug']}"
        body = ['<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><a href="/best/">Best-of lists</a> / '
                f'<span>{esc(page["title"])}</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        # M24 (r9, 2026-09-28): 40-60 word direct answer directly under the H1
        # (5/6 analysed SERPs show AI Overview; the site is cited in none).
        if page.get("direct_answer"):
            body.append(f'<p class="direct-answer">{esc(page["direct_answer"])}</p>')
        # M23 (r9, 2026-09-28): methodology prose demoted below the table under
        # a 'How we picked' H2; captured here, emitted after the table.
        _intros = [f"<p>{esc(para)}</p>" for para in page["intro"]]

        # r8 H4 (2026-09-28): the honesty is the differentiator - say exactly what
        # was checked and when, above the first tool entry. Never fabricated testing.
        _verify_box = ('<aside class="verify-box"><h2>What we checked and when</h2>'
            '<p>Pricing checked 2026-09-28 against each vendor\'s own pricing page · '
            'API availability confirmed from public documentation · Integrations read from '
            'vendor listings and source repositories. Not installed and not benchmarked: '
            'this is desk research with dates on it.</p>'
            '<p>What we could not verify is called out under each tool below.</p></aside>')

        # Comparison table with verdicts (the card's spec) from catalog facts only.
        # M22 (r9, 2026-09-28): per-page column sets from catalog variance.
        # A column burned on a constant (geo's all-No Open source) is dropped;
        # Public API appears only where it varies. SOC2/seats/contract terms
        # are NOT columns: the catalog carries no such fields and procurement
        # facts are never invented (omission honesty beats a fuller-looking
        # table of unverifiable claims).
        _trio = [tools_by_slug[it["slug"]] for it in items]
        _show_oss = len({bool(t.get("open_source")) for t in _trio}) > 1
        _show_api = len({bool(t.get("api_available")) for t in _trio}) > 1
        _head = '<tr><th>Tool</th><th>Pricing</th>'
        if _show_oss:
            _head += '<th>Open source</th>'
        if _show_api:
            _head += '<th>Public API</th>'
        _head += '<th>Verdict</th></tr>'
        rows = []
        for it in items:
            t = tools_by_slug[it["slug"]]
            _cells = (f'<tr><td><a href="/tools/{t["slug"]}/">{esc(t["name"])}</a></td>'
                      f'<td>{esc(pricing_label(t))}</td>')
            if _show_oss:
                _cells += f'<td>{_oss_label(t)}</td>'
            if _show_api:
                _cells += f'<td>{"yes" if t.get("api_available") else "no"}</td>'
            _cells += f'<td>{esc(it["verdict"])}</td></tr>'
            rows.append(_cells)
        body.append(
            '<div class="table-wrap"><table><caption>Best picks at a glance</caption><thead>'
            + _head + '</thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")
        # r10 H-11 (2026-09-29): one verdict-led CTA above the fold. The top
        # pick is items[0] (rank order); the verdict is our own published
        # editorial and the vendor URL comes from the catalog record.
        _top = tools_by_slug[items[0]["slug"]]
        _top_url = _top.get("website", "")
        body.append(
            f'<p class="top-pick"><strong>Our top pick: '
            f'<a href="#{esc(_top["slug"])}">{esc(_top["name"])}</a></strong>'
            f' &mdash; {esc(items[0]["verdict"])}'
            + (f' <a class="btn-cta" href="{esc(_top_url)}" rel="noopener">Try {esc(_top["name"])}</a>' if _top_url else "")
            + "</p>")
        # r10 H-1 (2026-09-29): visible freshness stamp (dateModified exists
        # in JSON-LD but was invisible on every money page).
        _du = page.get("date_updated", "")
        if _du:
            body.append(
                f'<p class="meta">Last verified <time datetime="{esc(_du)}">{esc(_du)}</time>.</p>')
        body.append('<h2>How we picked</h2>')
        body.extend(_intros)
        body.append(_verify_box)
        # r10 H-2 (2026-09-29): money pages link back up to the hubs whose
        # Compare rows link down here (symmetric with M26). Categories derive
        # from the featured tools' own records; guide bits reuse the shared
        # editorial map. No link sinks.
        _hub_cats = sorted({tools_by_slug[it["slug"]].get("category", "")
                            for it in items} - {""})
        if any(tools_by_slug[it["slug"]].get("open_source") for it in items):
            _hub_cats = sorted(set(_hub_cats) | {"open-source"})
        if _hub_cats:
            _cat_names = {}
            try:
                _cat_names = {c["slug"]: c["name"] for c in json.loads(
                    (ROOT / "tools" / "categories.json").read_text())}
            except (OSError, ValueError, KeyError):
                pass
            _pills = "".join(
                f'<a class="cat-pill" href="/categories/{c}/">'
                f'{esc(_cat_names.get(c, c.replace("-", " ").title()))}</a>'
                for c in _hub_cats)
            _gbits = " &middot; ".join(
                CATEGORY_GUIDES[c] for c in _hub_cats if c in CATEGORY_GUIDES)
            body.append(
                '<section class="hub-links"><h2>Browse the hubs behind these picks</h2>'
                f'<div class="cat-nav">{_pills}</div>'
                + (f'<p style="margin:.6rem 0 0;font-size:.92rem">{_gbits}</p>' if _gbits else "")
                + "</section>")
        body.append(_momentum_block([it["slug"] for it in items]))

        for it in items:
            t = tools_by_slug[it["slug"]]
            body.append(f"""<section class="best-item" id="{esc(t['slug'])}">
  <h2><a href="/tools/{t['slug']}/">{esc(t['name'])}</a></h2>
  {_tool_fact_img(t)}
  {_pilot_shot(t["slug"], t["name"])}
  <p>{esc(it['assessment'])}</p>
  <p><strong>Verdict:</strong> {esc(it['verdict'])}</p>
  {out_links(t)}
  <p><strong>{esc(it['skip_if'])}</strong></p>
  <p class="meta unverified"><strong>What we could not verify:</strong> {esc(it.get('unverified', 'installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.'))}</p>
</section>""")
        body.append(
            '<p class="alt-back">Every price quoted here comes from the vendor\'s own '
            'pricing page as catalogued on the tool page. Browse <a href="/tools/">all '
            f'{len([t for t in tools_by_slug.values() if t.get("status") == "active" and t.get("kind") != "Guide"])} tools</a> '
            'or read <a href="/methodology/">how we evaluate</a>, '
            'or download the <a href="/catalog-tools.json">machine-readable catalog</a>.</p>')
        # r10 H-1 pilot (2026-09-29): 3 question-form H2s with direct answers
        # (humanizer-passed, catalog-grounded) on flagged pages only.
        for _qa in (page.get("pilot_faq") or []):
            body.append(f'<h2>{esc(_qa["q"])}</h2><p>{esc(_qa["a"])}</p>')

        schema = {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": page["title"],
            "datePublished": page.get("date_published", ""), "dateModified": page.get("date_updated", ""),
            "author": {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/"},
            # r15 M-2 (2026-09-29): money-template graphs join publisher + site.
            "publisher": {"@id": "https://martechsignal.com/#organization"},
            "isPartOf": {"@id": "https://martechsignal.com/#website"},
            "numberOfItems": len(items),
            "itemListElement": [
                _bestx_li(tools_by_slug[it["slug"]], i)
                for i, it in enumerate(items)],
        }
        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Best-of lists",
                 "item": "https://martechsignal.com/best/"},
                {"@type": "ListItem", "position": 3, "name": page["title"],
                 "item": f"https://martechsignal.com/best/{page['slug']}/"},
            ],
        }
        out_dir = BEST_DIR / page["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_shell(
            page["seo_title"], page["meta"], f"/best/{page['slug']}/",
            "\n".join(body + [_SUB_INLINE]), [schema, breadcrumb]))
        built.append(page["slug"])
    print(f"best pages built: {len(built)} ({', '.join(built)})")
    return built


def _oss_label(t):
    """Open-source label, license-aware (R3/H1: a bool rendered 'Yes' for
    fair-code software is a claim the page's own prose contradicts)."""
    lic = str(t.get("license") or "").strip()
    low = lic.lower()
    if "fair-code" in low or "source-available" in low or "sustainable use" in low:
        return "Source-available (fair-code)"
    if t.get("open_source"):
        return f"Yes ({lic})" if lic else "Yes"
    return "No"


def _plabel(t):
    try:
        from build_tools import pricing_label
        return pricing_label(t)
    except Exception:
        return str(t.get("price_notes") or t.get("price_from") or "see page")


_SUB_INLINE = '<section class="subscribe sub-inline" id="subscribe"><h2>Get the next teardown</h2><p>One email when a new tool review lands, nothing else.</p><form class="sub-form" action="https://app.kit.com/forms/9136291/subscriptions" method="post" data-sv-form="9136291" data-uid="f315181f90" target="_blank"><input type="hidden" name="newsletter[subscriber][first_name]" value=""><input type="email" name="email_address" autocomplete="email" placeholder="you@company.com" aria-label="Email address" required><button type="submit">SUBSCRIBE</button></form></section>'


def _integ_cell(t):
    """r7 C3: show integration names readably, never a raw Python list repr."""
    v = t.get("integrations")
    if not v:
        return "not listed"
    if isinstance(v, list):
        names = ", ".join(str(i) for i in v[:4])
        more = f" (+{len(v) - 4} more)" if len(v) > 4 else ""
        return f"{len(v)} listed: {names}{more}"
    return str(v)


def build_vs():
    data = json.loads(VSX.read_text())
    tools_by_slug = _load_tools()
    built = []
    for page in data["pages"]:
        a = tools_by_slug[page["a_slug"]]
        b = tools_by_slug[page["b_slug"]]
        # r8 H3 (2026-09-28): optional third column for real 3-way pages
        c = tools_by_slug[page["c_slug"]] if page.get("c_slug") else None
        trio = (a, b) if c is None else (a, b, c)
        body = ['<nav class="crumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><a href="/vs/">Head-to-head comparisons</a> / '
                f'<span>{esc(page["title"])}</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")
        # r8 H3 (2026-09-28): the target SERPs reward multi-way framing, so the
        # quick-decision table for the whole family comes first on every pair page.
        df = page.get("decision_first")
        if df:
            body.append(f'<h2>{esc(df["heading"])}</h2>')
            body.append('<div class="table-wrap"><table class="cmp"><thead><tr>'
                        '<th scope="col">Tool</th><th scope="col">Starts at</th>'
                        '<th scope="col">Pick it when</th></tr></thead><tbody>')
            for row_slug, pick_when in df["rows"]:
                _rt = tools_by_slug[row_slug]
                body.append(f'<tr><th scope="row">{esc(_rt["name"])}</th><td>{esc(_plabel(_rt))}</td>'
                            f'<td>{esc(pick_when)}</td></tr>')
            body.append('</tbody></table></div>')
            for link in df.get("links", []):
                body.append(f'<p class="alt-back">{esc(link["text"])} '
                            f'<a href="{esc(link["href"])}">{esc(link["label"])}</a>.</p>')
        body.append(f'<p class="vs-links"><a href="/tools/{a["slug"]}/">{esc(a["name"])} assessment</a> · '
                    f'<a href="/tools/{b["slug"]}/">{esc(b["name"])} assessment</a></p>')
        # r15 M-8 (2026-09-29): first shot is the LCP element — eager/high.
        _first = True
        for _vt in [t for t in (a, b) if t]:
            _shot = _pilot_shot(_vt["slug"], _vt["name"], slot=500, priority=_first)
            if _shot:
                _first = False
                body.append(f'<div class="vs-shot">{_shot}</div>')
        for _vt in trio:
            _ol = out_links(_vt)
            if _ol:
                body.append(_ol.replace("Vendor:", f"{esc(_vt['name'])}:"))
        # H8 (r9, 2026-09-28): one media element per compared tool, above the
        # verdict block below.
        body.append('<div class="vs-figures">'
                    + ''.join(f'<figure>{_tool_fact_img(_vt)}'
                              f'<figcaption>{esc(_vt["name"])}</figcaption></figure>' for _vt in trio)
                    + '</div>')
        # A2 H6 (2026-09-26): the copy promises "the catalog numbers below" - this
        # table is those numbers, straight from the catalog (no invented figures).
        rows = [
            ("Pricing", [_plabel(t) for t in trio]),
            ("Open source", [_oss_label(t).lower() for t in trio]),
            ("Integrations listed", [_integ_cell(t) for t in trio]),
            ("Public API", ["yes" if t.get("api_available") else "no" for t in trio]),
        ]
        head = ''.join(f'<th scope="col">{esc(t["name"])}</th>' for t in trio)
        body.append('<div class="table-wrap"><table><caption>Side-by-side comparison</caption><thead><tr>'
                    f'<th scope="col">Dimension</th>{head}</tr></thead><tbody>')
        for label, vals in rows:
            tds = ''.join(f'<td>{esc(str(v))}</td>' for v in vals)
            body.append(f'<tr><th scope="row">{esc(label)}</th>{tds}</tr>')
        body.append('</tbody></table></div>')
        pt = page.get("price_table")
        assert not (pt and c), f'{page["slug"]}: price_table is a two-column template'
        if pt:
            body.append('<h2>Priced at volume</h2>')
            body.append(f'<p class="alt-back">{esc(pt["unit"])}. All figures checked '
                        f'{esc(pt.get("checked", "2026-09-27"))} on vendor pricing pages.</p>')
            body.append('<div class="table-wrap"><table class="cmp"><thead><tr>'
                        f'<th scope="col">Scenario</th><th scope="col">{esc(a["name"])}</th>'
                        f'<th scope="col">{esc(b["name"])}</th></tr></thead><tbody>')
            for label, av, bv in pt["rows"]:
                body.append(f'<tr><th scope="row">{esc(label)}</th><td>{esc(av)}</td><td>{esc(bv)}</td></tr>')
            body.append('</tbody></table></div>')
        for sec in page["sections"]:
            # A2 L17: a content section repeating the verdict heading broke
            # heading-based navigation; fold it under a distinct heading.
            h = sec["heading"]
            if h.strip().lower() == "who should pick which":
                h = "Decision notes"
            body.append(f'<h2>{esc(h)}</h2>')
            body.append(f'<p><strong>{esc(a["name"])}:</strong> {esc(sec["a"])}</p>')
            body.append(f'<p><strong>{esc(b["name"])}:</strong> {esc(sec["b"])}</p>')
            if sec.get("c") and c:
                body.append(f'<p><strong>{esc(c["name"])}:</strong> {esc(sec["c"])}</p>')
        if page.get("migration"):
            body.append('<h2>Migration cost</h2>')
            for para in page["migration"]:
                body.append(f'<p>{esc(para)}</p>')
        if page.get("neither"):
            # r8 H10 (2026-09-28): honest exit for readers who fit neither tool
            body.append('<h2>When neither is the right answer</h2>')
            body.append(f'<p>{esc(page["neither"])}</p>')
        body.append(f'<h2>Who should pick which</h2>')
        _picks = [(a, page["pick_a_if"]), (b, page["pick_b_if"])]
        if c and page.get("pick_c_if"):
            _picks.append((c, page["pick_c_if"]))
        body.append('<dl class="vs-verdict">'
                    + ''.join(f'<dt>Pick {esc(t["name"])} if</dt><dd>{esc(v)}</dd>' for t, v in _picks)
                    + '</dl>')
        # r11 H-4 (2026-09-29): same 3-question FAQ rollout as best pages.
        for _qa in (page.get("pilot_faq") or []):
            body.append(f'<h2>{esc(_qa["q"])}</h2><p>{esc(_qa["a"])}</p>')
        body.append('<p class="alt-back">Prices and features here come from each vendor\'s '
                    'own published materials as catalogued on the tool pages. Read '
                    '<a href="/methodology/">how we evaluate</a> or download the '
                    '<a href="/catalog-tools.json">machine-readable catalog</a>.</p>')
        # r10 H-1 (2026-09-29): visible freshness stamp on vs pages too.
        _vdu = page.get("date_updated", "")
        if _vdu:
            body.append(
                f'<p class="meta">Last verified <time datetime="{esc(_vdu)}">{esc(_vdu)}</time>.</p>')
        # r10 H-2 (2026-09-29): vs pages link their tools' hubs too.
        _vs_cats = sorted({t.get("category", "") for t in (a, b) if t} - {""})
        if any(t.get("open_source") for t in (a, b) if t):
            _vs_cats = sorted(set(_vs_cats) | {"open-source"})
        if _vs_cats:
            _vs_names = {}
            try:
                _vs_names = {c["slug"]: c["name"] for c in json.loads(
                    (ROOT / "tools" / "categories.json").read_text())}
            except (OSError, ValueError, KeyError):
                pass
            _vs_pills = "".join(
                f'<a class="cat-pill" href="/categories/{c}/">'
                f'{esc(_vs_names.get(c, c.replace("-", " ").title()))}</a>'
                for c in _vs_cats)
            _vs_g = " &middot; ".join(
                CATEGORY_GUIDES[c] for c in _vs_cats if c in CATEGORY_GUIDES)
            body.append(
                '<section class="hub-links"><h2>Browse the hubs behind this comparison</h2>'
                f'<div class="cat-nav">{_vs_pills}</div>'
                + (f'<p style="margin:.6rem 0 0;font-size:.92rem">{_vs_g}</p>' if _vs_g else "")
                + "</section>")
            body.append(_momentum_block([t["slug"] for t in (a, b) if t]))

        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Head-to-head comparisons",
                 "item": "https://martechsignal.com/vs/"},
                {"@type": "ListItem", "position": 3, "name": page["title"],
                 "item": f"https://martechsignal.com/vs/{page['slug']}/"},
            ],
        }
        # A2 H6: the comparison page declares its primary entity pair (plain
        # references - the offers-gated state machine governs product typing).
        entity = {
            "@context": "https://schema.org",
            "@type": "Article",
            # r16 L-7 (2026-09-29): #webpage bound to Article here but to
            # WebPage everywhere else. The typed node takes #article; the
            # WebPage node (unfragmented page URL, guides pattern) is added
            # by the M9 injector.
            "@id": f"https://martechsignal.com/vs/{page['slug']}/#article",
            "datePublished": page.get("date_published", ""), "dateModified": page.get("date_updated", ""),
            "author": {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/"},
            # r15 M-2 (2026-09-29): money-template graphs join publisher + site.
            "publisher": {"@id": "https://martechsignal.com/#organization"},
            "isPartOf": {"@id": "https://martechsignal.com/#website"},
            "name": page["title"],
            "url": f"https://martechsignal.com/vs/{page['slug']}/",
            "inLanguage": "en",
            # r10 H-4 (2026-09-29): Article headline (= H1) + page image.
            "headline": page["title"],
            "image": f"https://martechsignal.com/og/vs/{page['slug']}.png",
            # r7 M7 (2026-09-28): plain #app references for the compared pair
            # (the offers-gated state machine governs product typing) and the
            # pair declared as an ItemList.
            "about": [
                {"@id": f"https://martechsignal.com/tools/{t['slug']}/#app"} for t in trio
            ],
            "mainEntity": {
                "@type": "ItemList",
                "name": " vs ".join(t["name"] for t in trio),
                # r15 M-9 (2026-09-29): bare {@id,url} stubs upgraded to typed
                # nodes with names — same modelling as /best/ leaves.
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": t["name"], "item": {
                        "@type": "SoftwareApplication",
                        "@id": f"https://martechsignal.com/tools/{t['slug']}/#app",
                        "url": f"https://martechsignal.com/tools/{t['slug']}/",
                        "name": t["name"]}}
                    for i, t in enumerate(trio)
                ],
            },
        }
        out_dir = VS_DIR / page["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_shell(
            page["seo_title"], page["meta"], f"/vs/{page['slug']}/",
            "\n".join(body + [_SUB_INLINE]), [entity, breadcrumb],
            og_image=f"og/vs/{page['slug']}.png"))
        built.append(page["slug"])
    print(f"vs pages built: {len(built)} ({', '.join(built)})")
    return built


if __name__ == "__main__":
    build_best()
    build_vs()
