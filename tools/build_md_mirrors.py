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
    # r25 L-15 (2026-10-05): hub-group-label headings carry an empty <i></i>
    # spacer and an <em>count</em> the emphasis pass renders as ***2* stubs
    # (## CREATIVE GENERATION***2* across 15 mirrors). Normalize at the
    # source: empty inline spacers die, heading counts become (N).
    src = re.sub(r"<h([234]) class=\"hub-group-label\"><span>(.*?)</span><i></i><em>(\d+)</em></h\1>",
                 r"<h\1>\2 (\3)</h\1>", src)
    src = re.sub(r"<(i|em)></\1>", "", src)
    # r25 M-4 (2026-10-05): the tools-directory slug run ("Scored on the
    # six-pillar rubric: slug, slug, ...") is SEO boilerplate the card pass
    # now renders properly with names+taglines - drop it, keep "Related"
    # variants (real cross-links on tool pages).
    src = re.sub(r'<p class="alt-back">Scored on the six-pillar rubric:.*?</p>', "", src, flags=re.S)

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
    # r25 M-4/L-26 (2026-10-05): verdict/lead prose lives in bare divs the
    # flow pass cannot see (heap's hero verdict never reached its mirror).
    # Capture only known-prose div classes - never generic divs (layout noise).
    for vm in re.finditer(r'<(div) class="(?:verdict|lede|lead|deck|standfirst|tldr|key-takeaway)"[^>]*>(.*?)</\1>', src, flags=re.S):
        _events.append((vm.start(), vm.end(), "flow", vm))
    # r21 M-8 (2026-10-02): card grids (glossary index, hubs) carry their
    # content in nested divs the flow pass cannot see - emit cards as
    # linked bullets in document order instead of dropping them.
    # r24 M-8 (2026-10-05): same for cat-pill hub links (best/* "Browse the
    # hubs" sections) and tool-row homepage index rows - 28 empty ## sections.
    # r25 M-4/L-15 (2026-10-05): anchors carry data-* attributes between class
    # and href (<a class="tool-card" data-cat=... href=...>) - allow them, or
    # the whole tools directory grid goes missing from its own mirror.
    for cm in re.finditer(r'<a class="(?:tool-card|cat-pill|tool-row)"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', src, flags=re.S):
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
            # r27 N-2 (2026-10-05): category cards carry <h3 class="name">,
            # not div/span — the old pattern missed and the 60-char fallback
            # pasted name+description into link text. Match any tag.
            _cn = re.search(r'<[a-z0-9]+ class="name"[^>]*>(.*?)</[a-z0-9]+>', _m.group(2), flags=re.S)
            _ct = re.search(r'<[a-z0-9]+ class="(?:tagline|take)"[^>]*>(.*?)</[a-z0-9]+>', _m.group(2), flags=re.S)
            _clabel = inline(_cn.group(1)) if _cn else ""
            if not _clabel:
                # r27 N-2 (2026-10-05): the 60-char fallback cut link text
                # mid-word ("ad crea"). Break at a word boundary with ellipsis.
                # r28 N-7 (2026-10-06): the ellipsis fired unconditionally —
                # short related-link texts ("CRM", 3-25 chars) gained a
                # phantom "…" their pages never carry. Only cut long text.
                _full = inline(_m.group(2))
                if len(_full) <= 60:
                    _clabel = _full
                else:
                    _raw60 = _full[:60]
                    _sp = _raw60.rfind(" ")
                    _clabel = (_raw60[:_sp] + "…") if _sp > 30 else (_raw60 + "…")
            if not _clabel:
                _clabel = _m.group(1).strip("/").split("/")[-1]
            _cline = f"- [{_clabel}]({_m.group(1)})"
            if _ct and inline(_ct.group(1)):
                _cline += f": {inline(_ct.group(1))}"
            # r26 M-3 (2026-10-05): the tools mirror answered nothing about
            # cost (0 price tokens vs 92 in HTML). Carry the card's own price
            # tag - same catalog record the HTML renders.
            _cp = re.search(r'<span class="tag pricing"[^>]*>(.*?)</span>', _m.group(2), flags=re.S)
            if _cp and inline(_cp.group(1)):
                _cline += f" ({inline(_cp.group(1))})"
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
    # r22 H-2 (2026-10-02): the innermost-div pass re-emitted tool-card
    # name+tagline pairs that the card pass already rendered as bullets
    # (glossary definitions duplicated flat under the last letter heading).
    # Skip content covered by an emitted card.
    for lv in re.finditer(r"<(div|section|header|footer|aside)[^>]*>((?:(?!<)[^<]|<(?:/?(?:strong|b|em|i|code|span|br|a|sup|sub|svg|path)\b[^>]*>))*?)</\1>", src, flags=re.S):
        if lv.start() < _covered_until:
            continue
        t2 = inline(lv.group(2))
        if t2:
            out += [t2, ""]
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
