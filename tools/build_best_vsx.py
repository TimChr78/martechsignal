#!/usr/bin/env python3
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

from build_tools import page_shell, esc, ROOT, pricing_label

BESTX = ROOT / "tools" / "bestx-content.json"
VSX = ROOT / "tools" / "vsx-content.json"
BEST_DIR = ROOT / "best"
VS_DIR = ROOT / "vs"


def _load_tools():
    tools = json.loads((ROOT / "tools" / "tools.json").read_text())
    return {t["slug"]: t for t in tools}


def build_best():
    data = json.loads(BESTX.read_text())
    tools_by_slug = _load_tools()
    built = []
    for page in data["pages"]:
        items = page["items"]
        for it in items:
            assert it["slug"] in tools_by_slug, f"unknown tool slug {it['slug']}"
        body = ['<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / '
                f'<span>{esc(page["title"])}</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")

        # Comparison table with verdicts (the card's spec) from catalog facts only.
        rows = []
        for it in items:
            t = tools_by_slug[it["slug"]]
            oss = "Yes" if t.get("open_source") else "No"
            rows.append(
                f'<tr><td><a href="/tools/{t["slug"]}/">{esc(t["name"])}</a></td>'
                f'<td>{esc(pricing_label(t))}</td><td>{oss}</td>'
                f'<td>{esc(it["verdict"])}</td></tr>')
        body.append(
            '<div class="table-wrap"><table><thead><tr><th>Tool</th><th>Pricing</th>'
            '<th>Open source</th><th>Verdict</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")

        for it in items:
            t = tools_by_slug[it["slug"]]
            body.append(f"""<section class="best-item" id="{esc(t['slug'])}">
  <h2><a href="/tools/{t['slug']}/">{esc(t['name'])}</a></h2>
  <p>{esc(it['assessment'])}</p>
  <p><strong>Verdict:</strong> {esc(it['verdict'])}</p>
  <p><strong>{esc(it['skip_if'])}</strong></p>
</section>""")
        body.append(
            '<p class="alt-back">Every price quoted here comes from the vendor\'s own '
            'pricing page as catalogued on the tool page. Browse <a href="/tools/">all '
            f'{len([t for t in tools_by_slug.values() if t.get("status") == "active"])} tools</a> '
            'or read <a href="/methodology/">how we evaluate</a>.</p>')

        schema = {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": page["title"],
            "numberOfItems": len(items),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1,
                 "name": tools_by_slug[it["slug"]]["name"],
                 "url": f"https://martechsignal.com/tools/{it['slug']}/"}
                for i, it in enumerate(items)],
        }
        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Tools",
                 "item": "https://martechsignal.com/tools/"},
                {"@type": "ListItem", "position": 3, "name": page["title"],
                 "item": f"https://martechsignal.com/best/{page['slug']}/"},
            ],
        }
        out_dir = BEST_DIR / page["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_shell(
            page["seo_title"], page["meta"], f"/best/{page['slug']}/",
            "\n".join(body), [schema, breadcrumb]))
        built.append(page["slug"])
    print(f"best pages built: {len(built)} ({', '.join(built)})")
    return built


def _plabel(t):
    try:
        from build_tools import pricing_label
        return pricing_label(t)
    except Exception:
        return str(t.get("price_notes") or t.get("price_from") or "see page")


def build_vs():
    data = json.loads(VSX.read_text())
    tools_by_slug = _load_tools()
    built = []
    for page in data["pages"]:
        a = tools_by_slug[page["a_slug"]]
        b = tools_by_slug[page["b_slug"]]
        body = ['<nav class="crumb"><a href="/">Home</a> / <a href="/tools/">Tools</a> / '
                f'<span>{esc(page["title"])}</span></nav>',
                f'<h1>{esc(page["title"])}</h1>']
        for para in page["intro"]:
            body.append(f"<p>{esc(para)}</p>")
        body.append(f'<p class="vs-links"><a href="/tools/{a["slug"]}/">{esc(a["name"])} assessment</a> · '
                    f'<a href="/tools/{b["slug"]}/">{esc(b["name"])} assessment</a></p>')
        # A2 H6 (2026-09-26): the copy promises "the catalog numbers below" - this
        # table is those numbers, straight from the catalog (no invented figures).
        rows = [
            ("Pricing", _plabel(a), _plabel(b)),
            ("Open source", "yes" if a.get("open_source") else "no",
             "yes" if b.get("open_source") else "no"),
            ("Integrations listed", str(a.get("integrations") or "not listed"),
             str(b.get("integrations") or "not listed")),
            ("Public API", "yes" if a.get("api_available") else "no",
             "yes" if b.get("api_available") else "no"),
        ]
        body.append('<div class="table-wrap"><table><thead><tr>'
                    f'<th scope="col">Dimension</th><th scope="col">{esc(a["name"])}</th>'
                    f'<th scope="col">{esc(b["name"])}</th></tr></thead><tbody>')
        for label, av, bv in rows:
            body.append(f'<tr><th scope="row">{esc(label)}</th><td>{esc(str(av))}</td><td>{esc(str(bv))}</td></tr>')
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
        body.append(f'<h2>Who should pick which</h2>')
        body.append('<dl class="vs-verdict">'
                    f'<dt>Pick {esc(a["name"])} if</dt><dd>{esc(page["pick_a_if"])}</dd>'
                    f'<dt>Pick {esc(b["name"])} if</dt><dd>{esc(page["pick_b_if"])}</dd></dl>')
        body.append('<p class="alt-back">Prices and features here come from each vendor\'s '
                    'own published materials as catalogued on the tool pages. Read '
                    '<a href="/methodology/">how we evaluate</a>.</p>')

        breadcrumb = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": "https://martechsignal.com/"},
                {"@type": "ListItem", "position": 2, "name": "Tools",
                 "item": "https://martechsignal.com/tools/"},
                {"@type": "ListItem", "position": 3, "name": page["title"],
                 "item": f"https://martechsignal.com/vs/{page['slug']}/"},
            ],
        }
        # A2 H6: the comparison page declares its primary entity pair (plain
        # references - the offers-gated state machine governs product typing).
        entity = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": page["title"],
            "url": f"https://martechsignal.com/vs/{page['slug']}/",
            "inLanguage": "en",
            "about": [
                {"@type": "Thing", "name": a["name"], "url": a.get("website", "")},
                {"@type": "Thing", "name": b["name"], "url": b.get("website", "")},
            ],
        }
        out_dir = VS_DIR / page["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page_shell(
            page["seo_title"], page["meta"], f"/vs/{page['slug']}/",
            "\n".join(body), [entity, breadcrumb]))
        built.append(page["slug"])
    print(f"vs pages built: {len(built)} ({', '.join(built)})")
    return built


if __name__ == "__main__":
    build_best()
    build_vs()
