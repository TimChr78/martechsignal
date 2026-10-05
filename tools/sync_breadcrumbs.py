#!/usr/bin/env python3
"""r23 H-2 (2026-10-05): breadcrumb graph normalizer. Runs after every builder.

Guarantees two invariants on every rendered HTML page:
  1. Every BreadcrumbList node carries @id ({page}#breadcrumb).
  2. Every WebPage node carries a pure {"@id"} breadcrumb edge at it.

Why a post-pass instead of per-builder fixes: the 57 @id-less nodes lived in
four different emitters (blog template x2, guides, utility pages) while
page_shell already patched its own callers. Chasing emitters one by one is
how r22's fix closed the metric by deleting the edge on 293 pages instead of
completing the rollout. This pass owns the invariant in one place.

Why the edge is safe to restore: the r22 deletion was premised on "Google
parses the pointer as a BreadcrumbList missing itemListElement" (52-page GSC
error, 2026-09-30). The pointer was always a pure {"@id"} reference with no
@type - it cannot parse as a BreadcrumbList. The GSC errors coincided with
the 56 BreadcrumbLists that carried no @id, i.e. references that genuinely
did not resolve. With every node named, the edge resolves everywhere.

Falsifiability (auditor's own): count(BreadcrumbList without @id) == 0 and
count(pages with a WebPage.breadcrumb edge) == page count.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://martechsignal.com"

LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def _page_url(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return SITE + "/"
    return SITE + "/" + rel[: -len("/index.html")] + "/"


def _walk(node, crumbs, webpages):
    if isinstance(node, dict):
        t = node.get("@type")
        if t == "BreadcrumbList" or (isinstance(t, list) and "BreadcrumbList" in t):
            crumbs.append(node)
        if t == "WebPage" or (isinstance(t, list) and "WebPage" in t):
            webpages.append(node)
        for v in node.values():
            _walk(v, crumbs, webpages)
    elif isinstance(node, list):
        for v in node:
            _walk(v, crumbs, webpages)


def _crumb_id_for(page_url, crumb):
    items = crumb.get("itemListElement") or []
    if items and isinstance(items[-1], dict) and items[-1].get("item"):
        return items[-1]["item"].rstrip("/") + "/#breadcrumb"
    return page_url + "#breadcrumb"


def _reemit(html, matches, parsed):
    parts = []
    last = 0
    for m, data in zip(matches, parsed):
        parts.append(html[last:m.start()])
        if data is None:
            parts.append(m.group(0))
        else:
            parts.append('<script type="application/ld+json">'
                         + json.dumps(data, indent=2, ensure_ascii=False) + "</script>")
        last = m.end()
    parts.append(html[last:])
    return "".join(parts)


def normalize(path):
    try:
        html = path.read_text()
    except Exception:
        return False
    if "BreadcrumbList" not in html and "WebPage" not in html:
        return False
    page_url = _page_url(path)
    matches = list(LD_RE.finditer(html))
    parsed = []
    for m in matches:
        try:
            parsed.append(json.loads(m.group(1)))
        except Exception:
            parsed.append(None)
    # Page-wide census: crumbs and WebPage nodes usually live in DIFFERENT
    # script blocks, so the edge must be resolved across blocks, not per block.
    crumbs, webpages = [], []
    for data in parsed:
        if data is not None:
            _walk(data, crumbs, webpages)
    if not crumbs and not webpages:
        return False
    changed = False
    for c in crumbs:
        if "@id" not in c:
            c["@id"] = _crumb_id_for(page_url, c)
            changed = True
    if crumbs and webpages:
        target = _crumb_id_for(page_url, crumbs[0])
        for w in webpages:
            b = w.get("breadcrumb")
            if not (isinstance(b, dict) and b.get("@id") == target and len(b) == 1):
                w["breadcrumb"] = {"@id": target}
                changed = True
    if not crumbs and webpages:
        # No trail anywhere but a WebPage exists: append a minimal trail
        # derived from the URL so the edge always has a target.
        segs = [s for s in page_url.replace(SITE, "").strip("/").split("/") if s]
        names = ["Home"] + [s.replace("-", " ").title() for s in segs]
        urls = [SITE + "/"] + [SITE + "/" + "/".join(segs[: i + 1]) + "/" for i in range(len(segs))]
        cid = page_url + "#breadcrumb"
        crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "@id": cid,
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                     for i, (n, u) in enumerate(zip(names, urls))]}
        for w in webpages:
            w["breadcrumb"] = {"@id": cid}
        html = html.replace("</head>",
                            '<script type="application/ld+json">' + json.dumps(crumb, ensure_ascii=False)
                            + "</script>\n</head>", 1)
        path.write_text(_reemit(html, matches, parsed))
        return True
    if not changed:
        return False
    path.write_text(_reemit(html, matches, parsed))
    return True


def main():
    n = 0
    for p in sorted(ROOT.rglob("index.html")):
        if "deploy-out" in p.parts or "node_modules" in p.parts:
            continue
        if normalize(p):
            n += 1
    print(f"breadcrumbs normalized on {n} pages")


if __name__ == "__main__":
    sys.exit(main() or 0)
