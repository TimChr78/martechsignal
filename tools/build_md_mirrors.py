#!/usr/bin/env python3
"""Real markdown mirrors for every page family without a genuine one (A3 M-6/M-7).

The tool and category mirrors are generated from catalog data in build_tools and
are left alone. Everything else (homepage, blog index and posts, hubs, listings,
author, hand pages) previously got 6-line stubs that self-described as mirrors,
and /index.md was a byte-copy of llms.txt. This derives each mirror from the
page's own rendered HTML: title, lead paragraphs, headings and list items.
Run after the page builders in deploy.sh.
"""
import html as _html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_PREFIXES = ()  # H10: every page family gets a real mirror

def html_to_md(html: str) -> str:
    """H10 (2026-09-27): >=95% parity extractor. Tables become pipe tables,
    details/summary become Q/A pairs, dl rows become bullets, inline emphasis kept."""
    title = re.search(r"<title>([^<]+)</title>", html)
    title = _html.unescape(title.group(1)).split("|")[0].split("\u00b7")[0].strip() if title else "MartechSignal"
    src = re.sub(r"<(script|style|head)[^>]*>.*?</\1>", " ", html, flags=re.S)

    def inline(x):
        x = re.sub(r"<(strong|b)[^>]*>(.*?)</\1>", r"**\2**", x, flags=re.S)
        x = re.sub(r"<(em|i)[^>]*>(.*?)</\1>", r"*\2*", x, flags=re.S)
        x = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", x, flags=re.S)
        x = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", x, flags=re.S)
        x = re.sub(r"<[^>]+>", "", x)
        # H-8 (r10, 2026-09-29): entities must not leak into the markdown
        # (&#10003; instead of ✓). Unescape after tag-stripping; JSON-LD
        # blocks bypass inline() and stay byte-exact.
        return _html.unescape(re.sub(r"\s+", " ", x).strip())

    out = [f"# {title}", ""]
    # r20 M-3 (2026-10-02): single position-sorted pass in document order.
    # The old per-category passes hoisted <dl> bullets above the headings
    # that precede them (empty "## Who should pick which" on all vs mirrors).
    # Events fully contained in a larger emitted span are skipped (kills the
    # old table-cell <p> doubles too).
    _events = []
    for tm in re.finditer(r"<table[^>]*>(.*?)</table>", src, flags=re.S):
        _events.append((tm.start(), tm.end(), "table", tm))
    for dm in re.finditer(r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>", src, flags=re.S):
        _events.append((dm.start(), dm.end(), "details", dm))
    for dlm in re.finditer(r"<dl[^>]*>(.*?)</dl>", src, flags=re.S):
        _events.append((dlm.start(), dlm.end(), "dl", dlm))
    for m2 in re.finditer(r"<(h1|h2|h3|h4|p|li|blockquote|figcaption)[^>]*>(.*?)</\1>", src, flags=re.S):
        _events.append((m2.start(), m2.end(), "flow", m2))
    # r21 M-8 (2026-10-02): card grids (glossary index, hubs) carry their
    # content in nested divs the flow pass cannot see - emit cards as
    # linked bullets in document order instead of dropping them.
    for cm in re.finditer(r'<a class="tool-card" href="([^"]+)">(.*?)</a>', src, flags=re.S):
        _events.append((cm.start(), cm.end(), "card", cm))
    _events.sort(key=lambda e: (e[0], -(e[1] - e[0])))
    _covered_until = -1
    for _start, _end, _kind, _m in _events:
        if _start < _covered_until:
            continue
        if _kind == "table":
            rows = re.findall(r"<tr[^>]*>(.*?)</tr>", _m.group(1), flags=re.S)
            grid = [[inline(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.S)] for r in rows]
            grid = [g for g in grid if g]
            if len(grid) >= 2:
                w = max(len(g) for g in grid)
                grid = [g + [""] * (w - len(g)) for g in grid]
                tbl = ["| " + " | ".join(grid[0]) + " |",
                       "| " + " | ".join("---" for _ in range(w)) + " |"]
                tbl += ["| " + " | ".join(g) + " |" for g in grid[1:]]
                out += ["", *tbl, ""]
                _covered_until = _end
        elif _kind == "details":
            out += [f"**{inline(_m.group(1))}**", inline(_m.group(2)), ""]
            _covered_until = _end
        elif _kind == "dl":
            for dt in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", _m.group(1), flags=re.S):
                out += [f"- **{inline(dt.group(1))}:** {inline(dt.group(2))}"]
            out += [""]
            _covered_until = _end
        elif _kind == "card":
            _cn = re.search(r'<div class="name"[^>]*>(.*?)</div>', _m.group(2), flags=re.S)
            _ct = re.search(r'<div class="tagline"[^>]*>(.*?)</div>', _m.group(2), flags=re.S)
            _clabel = inline(_cn.group(1)) if _cn else _m.group(1).strip("/").split("/")[-1]
            _cline = f"- [{_clabel}]({_m.group(1)})"
            if _ct and inline(_ct.group(1)):
                _cline += f": {inline(_ct.group(1))}"
            out += [_cline]
            _covered_until = _end
        else:
            tag, inner = _m.group(1), _m.group(2)
            text = inline(inner)
            if not text:
                continue
            if tag in ("h2", "h1"):
                out += ["## " + text, ""]
            elif tag in ("h3", "h4"):
                out += ["### " + text, ""]
            elif tag == "li":
                out += ["- " + text]
            elif tag == "blockquote":
                out += ["> " + text, ""]
            else:
                out += [text, ""]
    for lv in re.finditer(r"<(div|section|header|footer|aside)[^>]*>((?:(?!<)[^<]|<(?:/?(?:strong|b|em|i|code|span|br|a|sup|sub|svg|path)\b[^>]*>))*?)</\1>", src, flags=re.S):
        t2 = inline(lv.group(2))
        if t2:
            out += [t2, ""]
    for jl in re.finditer(r'<script type="application/ld[+]json">(.*?)</script>', html, flags=re.S):
        out += ["", "```json", jl.group(1).strip(), "```"]
    return "\n".join(out).strip() + "\n"

def main():
    n = 0
    for idx in sorted(ROOT.glob("*/index.html")) + sorted(ROOT.glob("*/*/index.html")):
        rel = str(idx.parent.relative_to(ROOT))
        if rel == "." or rel.split("/")[0] + "/" in SKIP_PREFIXES:
            continue
        md_path = idx.parent / "index.md"
        md_path.write_text(html_to_md(idx.read_text()))
        n += 1
    home = ROOT / "index.html"
    (ROOT / "index.md").write_text(html_to_md(home.read_text()))
    print(f"markdown mirrors: {n} pages + homepage derived from HTML")

if __name__ == "__main__":
    main()
