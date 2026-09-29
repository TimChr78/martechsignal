

import json as _h9j
_H9_ENTITY = _h9j.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Organization", "@id": "https://martechsignal.com/#organization",
         "name": "MartechSignal", "url": "https://martechsignal.com/",
         "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo",
                  "url": "https://martechsignal.com/logo.png"},
         "sameAs": ["https://github.com/timchr78"]},
        {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person",
         "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/",
         "image": "https://martechsignal.com/authors/tim-christensen/avatar.png",
         "worksFor": {"@id": "https://martechsignal.com/#organization"},
         "sameAs": ["https://github.com/timchr78"]},
    ],
})
_H9_TAG = '<script type="application/ld+json">' + _H9_ENTITY + '</script>'

def _png_dims(src):
    import struct
    try:
        p = ROOT / src.lstrip("/")
        with open(p, "rb") as f:
            head = f.read(24)
        if head[12:16] == b"IHDR":
            return struct.unpack(">II", head[16:24])
    except Exception:
        pass
    return 1200, 630
#!/usr/bin/env python3
"""Build blog posts from drafts and regenerate the blog index.

Reads content/drafts/*.md → generates blog/{slug}/index.html
Updates blog/index.html with all published posts.

Run from /opt/data/martechsignal/: python3 tools/build_blog.py
"""

import re
import html
import json
import email.utils
from pathlib import Path
from datetime import datetime, timezone
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import suggest_links

try:  # canonical category names (MUSE-11); falls back to the old label
    from build_tools import _category_display as _cat_display
except Exception:  # pragma: no cover
    def _cat_display(slug):
        return str(slug).replace("-", " ").title()

try:  # M1 (r9, 2026-09-28): shared critical-CSS tags; falls back to plain link
    from build_tools import _stylesheet_tags as _shared_tags
except Exception:  # pragma: no cover
    def _shared_tags():
        return f'<link rel="stylesheet" href="/style.min.css?v={_css_v()}">'

ROOT = Path(__file__).resolve().parent.parent


def _css_v() -> str:
    """Cache-bust hash for style.css, computed from the file itself (R3-M18/L2:
    the literal went stale and new rules never shipped to returning visitors)."""
    import hashlib as _h
    return _h.md5((ROOT / "style.css").read_bytes()).hexdigest()[:8]

DRAFTS_DIR = ROOT / "content" / "drafts"
BLOG_DIR = ROOT / "blog"


def slugify(title: str) -> str:
    """Convert a title to a URL-friendly slug."""
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s.strip('-')


def parse_frontmatter(text: str):
    """Parse YAML-style frontmatter block. Returns (meta dict, body text)."""
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    raw = parts[1].strip()
    body = parts[2].strip()
    meta = {}
    for line in raw.split('\n'):
        m = re.match(r'(\w+):\s*(.+)', line)
        if not m:
            continue
        key = m.group(1)
        val = m.group(2).strip().strip('"').strip("'")
        if val.startswith('[') and val.endswith(']'):
            val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
        meta[key] = val
    return meta, body


def highlight_json(code: str) -> str:
    """Syntax-highlight a JSON string (keys amber, string values green, punctuation dim).
    Single pass over quoted tokens so keys are never re-wrapped as values."""
    esc = html.escape(code, quote=True)  # " -> &quot;

    def tok(m: re.Match) -> str:
        quoted, ws, colon = m.group(1), m.group(2) or '', m.group(3)
        if colon:  # a key - a quoted token followed by ':'
            return f'<span class="k">{quoted}</span>{ws}<span class="p">:</span>'
        return f'<span class="s">{quoted}</span>{ws}'

    # One pass: each quoted token classified exactly once (key vs value)
    s = re.sub(r'(&quot;[^&]*?&quot;)(\s*)(:)?', tok, esc)
    # Structural braces/brackets (never inside this content's string values)
    s = re.sub(r'([{}\[\]])', r'<span class="p">\1</span>', s)
    # Booleans / null
    s = re.sub(r'\b(true|false|null)\b', r'<span class="k">\1</span>', s)
    return s


def fenced_code_block(lang: str, code: str) -> str:
    """Render a fenced code block as a styled panel with a filename/lang bar."""
    lang = (lang or '').strip().lower()
    label = {'json': 'JSON', 'python': 'PYTHON', 'bash': 'SHELL', 'sh': 'SHELL',
             'yaml': 'YAML', 'yml': 'YAML', 'js': 'JS', 'javascript': 'JS'}.get(lang, lang.upper() or 'CODE')
    if lang == 'json':
        body = highlight_json(code)
    else:
        body = html.escape(code, quote=False)
    return (f'<div class="codeblock">\n'
            f'<div class="cb-bar"><span class="cb-dots"><i></i><i></i><i></i></span>'
            f'<span class="cb-lang">{label}</span></div>\n'
            f'<pre><code>{body}</code></pre>\n</div>')


def markdown_to_html(md: str) -> str:
    """Convert basic markdown to HTML. Handles h1-3, paragraphs, lists, links,
    bold, italic, inline code, blockquotes, fenced divs (::: type), and raw HTML."""
    lines = md.split('\n')
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Blank line
        if not line.strip():
            out.append('')
            i += 1
            continue

        # Heading
        m = re.match(r'^(#{1,3})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            text = inline_format(m.group(2))
            out.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # Fenced code block: ```lang ... ```
        m = re.match(r'^```(\w*)\s*$', line)
        if m:
            lang = m.group(1)
            code_lines = []
            i += 1
            while i < len(lines) and not re.match(r'^```\s*$', lines[i]):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```
            out.append(fenced_code_block(lang, '\n'.join(code_lines)))
            continue

        # Pipe table: header row | a | b | + separator row |---|---|
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s:|-]+$', lines[i + 1]):
            def _cells(row):
                return [c.strip() for c in row.strip().strip('|').split('|')]
            headers = _cells(lines[i])
            i += 2  # skip header + separator
            body_rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = _cells(lines[i])
                # pad/truncate to header width so ragged rows stay valid HTML
                cells = (cells + [''] * len(headers))[:len(headers)]
                body_rows.append([inline_format(c) for c in cells])
                i += 1
            head_html = ''.join(f'<th>{inline_format(h)}</th>' for h in headers)
            rows_html = ''.join(
                '<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in body_rows)
            out.append(f'<div class="table-wrap"><table><thead><tr>{head_html}</tr></thead>'
                       f'<tbody>{rows_html}</tbody></table></div>')
            continue

        # Unordered list
        if re.match(r'^-\s', line):
            items = []
            while i < len(lines) and re.match(r'^-\s', lines[i]):
                item_text = inline_format(re.sub(r'^-\s', '', lines[i]))
                items.append(f'<li>{item_text}</li>')
                i += 1
            out.append('<ul>\n' + '\n'.join(items) + '\n</ul>')
            continue

        # Fenced divs: ::: callout / ::: verdict win / ::: wf-step
        m = re.match(r'^:::\s+(.+)$', line)
        if m:
            classes = m.group(1).strip()
            inner_lines = []
            i += 1
            while i < len(lines) and not re.match(r'^:::$', lines[i].strip()):
                inner_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # skip closing :::
            inner_md = '\n'.join(inner_lines)
            inner_html = markdown_to_html(inner_md)
            out.append(f'<div class="{classes}">\n{inner_html}\n</div>')
            continue

        # Raw HTML passthrough (lines starting with < and ending with >)
        if re.match(r'^\s*<[a-zA-Z/]', line) and '>' in line:
            html_lines = [line]
            i += 1
            # Collect multi-line HTML blocks
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|-\s|:::\s|[--]{2,}$)', lines[i]):
                if '</' in lines[i] and not ('</' in html_lines[-1]):
                    html_lines.append(lines[i])
                    i += 1
                    if '>' in lines[i-1]:
                        break
                    continue
                break
            # r7 C4 (2026-09-27): markdown inside raw HTML blocks (notably <td>
            # cells) never reaches inline_format; convert links/bold without
            # escaping, since the block is already HTML.
            _blk = '\n'.join(html_lines)
            _blk = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', _blk)
            _blk = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', _blk)
            # r7 H10 (2026-09-28): raw <table class="cmp"> blocks overflow mobile
            # columns (378px measured in a 350px column). Give them the same
            # .table-wrap scroll container the pipe-table renderer emits.
            if '<table' in _blk and 'table-wrap' not in _blk:
                # M26 (2026-09-28): author-written tables often carry <th> rows
                # outside a <thead>. Wrap the header row so the markup matches
                # what the pipe-table renderer emits.
                if '<thead' not in _blk:
                    _m = re.search(r'<tr[^>]*>.*?</tr>', _blk, re.S)
                    if _m and '<th' in _m.group(0):
                        _blk = (_blk[:_m.start()] + '<thead>' + _m.group(0)
                                + '</thead>' + _blk[_m.end():])
                _blk = '<div class="table-wrap">' + _blk + '</div>'
            out.append(_blk)
            continue

        # Horizontal rule (--- or -)
        if re.match(r'^[--]{2,}$', line.strip()):
            out.append('<hr>')
            i += 1
            continue

        # Blockquote-like (lines starting with >)
        # Paragraph (collect until blank line)
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|-\s|[--]{2,}$)', lines[i]):
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            text = inline_format(' '.join(para_lines))
            out.append(f'<p>{text}</p>')
            continue

        i += 1

    return '\n'.join(out)


def inline_format(text: str) -> str:
    """Handle inline markdown: **bold**, *italic*, `code`, [links](url)."""
    # Escape HTML
    text = html.escape(text, quote=False)

    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # Images (M-16: posts can carry figures; L2: real width/height from the PNG)
    def _img_repl(_m):
        _w, _h = _png_dims(_m.group(2))
        # r6 M-11: responsive variants alongside the source (same stem, -480/-800).
        _srcset = ""
        _img_p = Path(_m.group(2).lstrip("/"))
        if (ROOT / _img_p.parent / (_img_p.stem + "-480" + _img_p.suffix)).exists():
            _d, _n, _x = _img_p.parent.as_posix(), _img_p.stem, _img_p.suffix
            _srcset = (f' srcset="/{_d}/{_n}-480{_x} 480w, /{_d}/{_n}-800{_x} 800w, '
                       f'{_m.group(2)} {_w}w" sizes="(max-width:700px) 100vw, 1100px"')
        return (f'<img class="post-figure" width="{_w}" height="{_h}"{_srcset} '
                f'src="{_m.group(2)}" alt="{_m.group(1)}" loading="lazy">')
    text = re.sub(r'!\[(.+?)\]\((.+?)\)', _img_repl, text)
    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)

    # Em dash
    text = text.replace('--', '-')
    text = text.replace(' - ', ' - ')

    return text



def _build_toc_and_chip(body_html: str, categories=None):
    """Audit M-9/M-8: anchored mini-TOC on long posts + 'Filed under' category chips."""
    import re as _re
    words = len(_re.findall(r"\b\w+\b", _re.sub(r"<[^>]+>", " ", body_html)))
    chip_html = ""
    if categories:
        links = " · ".join(
            f'<a href="/categories/{c}/">{_cat_display(c)}</a>'
            for c in (categories if isinstance(categories, list) else [categories])
        )
        chip_html = f'<p class="meta filed-cat">Filed under {links}</p>'
    toc_html = ""
    if words >= 1200:
        items = []
        def _add(m):
            text = _re.sub(r"<[^>]+>", "", m.group(2))
            anchor = _re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            items.append((anchor, text))
            return f'<h2 id="{anchor}"{m.group(1)}>{m.group(2)}</h2>'
        new_body = _re.sub(r"<h2([^>]*)>(.*?)</h2>", _add, body_html, flags=_re.S)
        if len(items) >= 3:
            links = " \u00b7 ".join(f'<a href="#{a}">{t}</a>' for a, t in items[:8])
            toc_html = ('<nav class="mini-toc" style="margin:0 0 1.8rem;padding:.9rem 1.1rem;'
                        'border:1px solid var(--line);border-radius:10px;font-size:.85rem">'
                        '<b style="letter-spacing:.08em;font-size:.7rem">ON THIS PAGE</b><br>'
                        f"{links}</nav>")
            body_html = new_body
    return body_html, chip_html + toc_html


def _clean_excerpt(text, limit=155):
    """Word-boundary meta excerpt with terminal punctuation; no mid-word cuts (audit H-3).
    L3 (r9): callers escape the result into the meta tag, so quotes expand to
    entities after clipping. Re-shrink until the ESCAPED text fits the limit."""
    text = " ".join((text or "").split())
    if len(html.escape(text)) <= limit:
        return text
    while True:
        sp = text.rfind(" ", 0, limit - 1)
        text = text[:sp] if sp > 60 else text[:limit - 3]
        text = text.rstrip(" ,;:.--") + "."
        if len(html.escape(text)) <= limit or len(text) < 40:
            return text
        limit = len(text) - 5

def _date_modified(meta, date_str):
    """R2 M-7 (2026-09-08): dateModified must reflect real edits. Use the last git commit
    that touched the draft; fall back to file mtime, then the publish date."""
    import subprocess as _sp, os as _os
    dp = meta.get('_draft_path')
    if dp and _os.path.exists(dp):
        try:
            out = _sp.run(['git', 'log', '-1', '--format=%cI', '--', dp],
                          capture_output=True, text=True, timeout=10,
                          cwd=_os.path.dirname(_os.path.abspath(dp)) or '.')
            if out.returncode == 0 and out.stdout.strip():
                return out.stdout.strip()[:10]
        except Exception:
            pass
        try:
            import datetime as _dt
            return date_str  # r6 M-5: mtime is not a copy change; publish date is the honest floor
        except Exception:
            pass
    return date_str


def build_post(meta: dict, body_html: str) -> str:
    """Generate the full HTML page for a blog post."""
    title = meta.get('title', 'Untitled')
    body_html, extras = _build_toc_and_chip(body_html, meta.get('categories') or meta.get('category'))
    # SEO title: optional frontmatter override (<=60ch) for <title>/og:title; H1 keeps full title
    seo_title = meta.get('seo_title') or title
    date_str = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
    date_display = datetime.strptime(date_str, '%Y-%m-%d').strftime('%b %d, %Y').upper()
    # A3 H-2 (2026-09-26): when dateModified differs from published, SHOW both
    # dates on the page so the visible date and the schema can never contradict.
    _dm = _date_modified(meta, date_str)
    if _dm and _dm != date_str:
        _ud = datetime.strptime(_dm, '%Y-%m-%d').strftime('%b %d, %Y').upper()
        upd = f' · Updated <time datetime="{_dm}">{_ud}</time>'
    else:
        upd = ''
    slug = meta.get('slug') or slugify(title)
    # CL-2 (2026-09-25): optional frontmatter canonical override (cluster consolidation)
    canon = meta.get('canonical') or f"https://martechsignal.com/blog/{slug}/"
    # L16 (r9, 2026-09-28; CORRECTED r10 C-1, 2026-09-29): posts about Claude SEO
    # carry a third-party disclosure, NOT an ownership claim. The 2026-09-26
    # corrections entry retracted ownership: third-party MIT project by
    # AgriciDaniel, no affiliation. Never re-assert "we make this".
    _made_box = ""
    if slug.startswith("claude-seo-") or slug == "claude-seo":
        _made_box = ('<p class="made-badge">Independent tool: Claude SEO is a third-party MIT project by '
                     'AgriciDaniel; we have no affiliation with its author. Coverage here is held to the same '
                     'verification standard as other tools. See the <a href="/corrections/">corrections log</a>.</p>')

    related = suggest_links.suggest_for_text(body_html, max_suggestions=3, exclude_slug=slug)
    if related:
        links = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['title'], quote=False) + '</a></li>' for item in related)
        body_html += '<section class="related-reading"><h2>Related reading</h2><ul>' + links + '</ul></section>'

    # Blog -> Tools: suggest 2-3 relevant tools via keyword overlap
    try:
        existing_tool_slugs = set(__import__('re').findall(r'/tools/([^/"\'\?#]+)/', body_html))
    except Exception:
        existing_tool_slugs = set()
    _post_cats = meta.get('categories') or meta.get('category')
    _src_cat = (_post_cats[0] if isinstance(_post_cats, list) and _post_cats else _post_cats) if _post_cats else None
    related_tools = suggest_links.suggest_tools_for_text(body_html, max_suggestions=3, exclude_slugs=existing_tool_slugs, source_category=_src_cat)
    if related_tools:
        tlinks = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['name'], quote=False) + '</a> - ' + html.escape(item.get('tagline',''), quote=False) + '</li>' for item in related_tools)
        body_html += '<section class="related-tools"><h2>Related tools</h2><ul>' + tlinks + '</ul></section>'

    # A2 C1 (2026-09-26): comparison guides join the post-linking layer (the
    # /best/ + /vs/ + /alternatives/ pages were orphaned with zero inlinks).
    commercial = suggest_links.suggest_commercial_for_text(body_html, max_suggestions=2)
    if commercial:
        clinks = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['title'], quote=False) + '</a></li>' for item in commercial)
        body_html += '<section class="related-reading"><h2>Comparison guides</h2><ul>' + clinks + '</ul></section>'
        existing_tool_slugs.update(item['slug'] for item in related_tools)

    # Blog -> Glossary: suggest up to 2 glossary terms via keyword overlap
    # (audit M7: 0/17 blog posts linked to any glossary page)
    try:
        existing_glossary_slugs = set(__import__('re').findall(r'/glossary/([^/"\'\\?#]+)/', body_html))
        related_glossary = suggest_links.suggest_glossary_for_text(body_html, max_suggestions=2)
        related_glossary = [g for g in related_glossary if g['slug'] not in existing_glossary_slugs][:2]
        if related_glossary:
            glinks = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['name'], quote=False) + '</a></li>' for item in related_glossary)
            body_html += '<section class="related-glossary"><h2>Glossary terms</h2><ul>' + glinks + '</ul></section>'
    except Exception:
        pass

    # Directory coverage: 1-2 "More from the directory" links to unlinked tools
    # sharing the post's dominant category. Keeps every tool page reachable
    # from at least one editorial post (no orphans).
    try:
        more_links = suggest_links.suggest_category_fill(body_html, max_suggestions=8, exclude_slugs=existing_tool_slugs, post_slug=slug)
    except Exception:
        more_links = []
    if more_links:
        mlinks = ' · '.join('<a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['name'], quote=False) + '</a>' for item in more_links)
        body_html += '<p class="more-tools" style="font-size:.85rem;color:var(--muted)">More from the directory: ' + mlinks + '</p>'

    # First paragraph as excerpt (strip HTML tags). r11 M-7 (2026-09-29):
    # word-boundary cut with ellipsis — the raw [:200] slice ended mid-word
    # on the homepage ("specification c", "actually me").
    first_p = re.search(r'<p>(.+?)</p>', body_html, re.DOTALL)
    _raw_ex = re.sub(r'<[^>]+>', '', first_p.group(1)) if first_p else ''
    excerpt = (_raw_ex[:200].rsplit(' ', 1)[0].rstrip(' ,;:') + '\u2026'
               if len(_raw_ex) > 200 else _raw_ex)

    # Read time from word count (~200 wpm), tags as kicker
    words = len(re.sub(r'<[^>]+>', ' ', body_html).split())
    read_min = max(1, round(words / 200))
    tags = meta.get('tags', [])
    # L11 (r9): 'recovered' is a pipeline-internal tag (recovered drafts); it
    # must never render as a kicker. Display it as Updated.
    _kick = [('Updated' if t.lower() == 'recovered' else t) for t in tags[:2]]
    kicker = ' · '.join(t.upper() for t in _kick) if _kick else 'DEEP DIVE · MARTECH'
    # Human byline - the site's named author (see footer/about); org stays in JSON-LD
    byline = 'Tim Christensen'

    # M6 (2026-09-27): cited works from frontmatter `sources: [name|url, ...]`
    _srcs = meta.get("sources") or []
    if isinstance(_srcs, str):
        _srcs = [_srcs.strip("[]")]
    _cit_list = [{"@type": "CreativeWork", "name": x.split("|", 1)[0].strip().strip("'\""),
                  "url": x.split("|", 1)[1].strip().strip("'\"")}
                 for x in _srcs if "|" in x]

    # JSON-LD: Article + BreadcrumbList (Google starter guide: structured data for title/breadcrumb)
    article_schema = {
        "@context": "https://schema.org",
        "speakable": {"@type": "SpeakableSpecification", "cssSelectors": ["h1", "article h2"]},
        "@type": "BlogPosting",
        "headline": title,
        "description": _clean_excerpt(excerpt),
        "author": {"@type": "Person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]},
        "publisher": {"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com", "logo": {"@type": "ImageObject", "url": "https://martechsignal.com/logo.png"}},
        "datePublished": date_str,
        "dateModified": _date_modified(meta, date_str),
        "mainEntityOfPage": f"https://martechsignal.com/blog/{slug}/",
        "image": {"@type": "ImageObject", "url": f"https://martechsignal.com/og/{slug}.png", "width": 1200, "height": 630},
        **({"citation": _cit_list} if _cit_list else {}),
        # A2 M7 (2026-09-26): link the post into the Blog node and carry the
        # article fields Google's article cluster reads.
        "isPartOf": {"@type": "Blog",
                     "@id": "https://martechsignal.com/blog/#blog"},
        "inLanguage": "en",
        # r8 M23 (2026-09-28): count prose only - the TOC and filed-under chips
                # are scaffolding and made schema drift +121..+272 from the body.
                "wordCount": len(re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<nav\b.*?</nav>|<p class=\"meta[^\"]*\"[^>]*>.*?</p>", " ", body_html)).split()),
        "articleSection": ", ".join(meta.get("categories") or ([meta["category"]] if meta.get("category") else []) or []),
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://martechsignal.com/blog/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"https://martechsignal.com/blog/{slug}/"},
        ],
    }
    schema = article_schema  # compat alias for tests that import schema

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(seo_title)}</title>
<meta name="description" content="{html.escape(_clean_excerpt(excerpt))}">
<link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<link rel="alternate" type="text/plain" title="MartechSignal catalog for AI systems" href="/llms.txt">
<meta property="og:site_name" content="MartechSignal">
<meta property="og:title" content="{html.escape(seo_title)}">
<meta property="og:description" content="{html.escape(_clean_excerpt(excerpt))}">
<meta property="og:url" content="https://martechsignal.com/blog/{slug}/">
<meta property="og:image" content="https://martechsignal.com/og/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canon}">
<link rel="alternate" type="text/markdown" href="https://martechsignal.com/blog/{slug}/index.md">
<link rel="ard ai-catalog" href="https://martechsignal.com/.well-known/ard.json">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://analytics.martechsignal.com" crossorigin>
<link rel="dns-prefetch" href="https://analytics.martechsignal.com">
<link rel="preload" href="/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-black-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/spline-sans-mono-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/spline-sans-mono-600.woff2" as="font" type="font/woff2" crossorigin>{_shared_tags()}<script type="application/ld+json">
{json.dumps(article_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(breadcrumb_schema, indent=2)}
</script>
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
<script src="/site.js" defer></script>
</head>
<body class="page-post">
<div class="bg" aria-hidden="true"></div>
<div id="progress" aria-hidden="true"></div>
<header class="masthead">
  <div class="mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="pulse-dot"></span></a>
    <nav class="mast-nav"><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/categories/">CATEGORIES</a><a href="/glossary/">GLOSSARY</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
<a class="back" href="/blog/">← ALL WRITING</a>
<article>

<p class="kicker">{kicker} · {read_min} MIN</p>
<h1>{html.escape(title)}</h1>
{_made_box}
<img class="post-hero" src="/og/hero-{slug}.webp" alt="{title}" width="1200" height="630" srcset="/og/hero-{slug}-480.webp 480w, /og/hero-{slug}-800.webp 800w, /og/hero-{slug}.webp 1200w" sizes="(max-width:700px) 100vw, 1100px" fetchpriority="high" decoding="async" style="width:100%;height:auto;border-radius:10px;margin:.4rem 0 1.2rem">\n<p class="disclosure-strip"><a href="/methodology/">How we review</a> \u00b7 No affiliate links</p>
<p class="meta"><a href="/">Home</a> · <a href="/blog/">Blog</a> · {title}</p>
<p class="meta"><time datetime="{date_str}">{date_display}</time>{upd}</p>
<div class="byline">
  <span class="av">TC</span>
  <span class="who"><b><a href="/authors/tim-christensen/" style="color:inherit;text-decoration:none;border-bottom:1px dotted var(--amber)">{byline}</a></b></span>
</div>

{extras}
{body_html}

<div class="cta-strip">
<h3>One email. <span class="amber">Every Friday.</span></h3>
<p>The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.</p>
<a class="btn" href="/#subscribe" data-umami-event="Blog subscribe click">SUBSCRIBE →</a>
</div>

</article>
</main>
<footer>
  <div class="foot-in">
    <p><b>MartechSignal</b>, written by <a href="/authors/tim-christensen/" style="color:inherit">Tim Christensen</a></p>
    <nav class="foot-links"><a href="/">HOME</a><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/blog/">BLOG</a><a href="/trending/">TRENDING</a><a href="/glossary/">GLOSSARY</a><a href="/checklist/">CHECKLIST</a><a href="/authors/tim-christensen/">Tim Christensen</a><a href="/about/">ABOUT</a><a href="/contact/">CONTACT</a><a href="/privacy/">PRIVACY</a><a href="/terms/">TERMS</a><a href="/ai-policy/">AI POLICY</a><a href="/methodology/">METHODOLOGY</a><a href="/rss.xml">RSS</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</footer>

{_H9_TAG}</body>
</html>"""


def build_index(posts: list) -> str:
    """Build the blog index page listing all posts in reverse chronological order."""
    # Sort by date descending
    posts_sorted = sorted(posts, key=lambda p: p['date'], reverse=True)

    entries = []
    for idx, post in enumerate(posts_sorted, start=1):
        title = post['title']
        date = post['date']
        slug = post.get('slug', slugify(title))
        excerpt = post.get('excerpt', '')

        # R2 L-4 (2026-09-09): the card wrapped its <h2> in a <span>, which is invalid
        # (span cannot contain heading content) and cost the outline its structure.
        entries.append(f"""    <li class="reveal"><a class="sig" href="/blog/{slug}/">
      <span class="idx">{idx:02d}</span>
      <h2>{html.escape(title, quote=False)}</h2>
      <span class="sub">{date}</span>
      <p class="excerpt">{html.escape((excerpt[:180].rsplit(' ', 1)[0].rstrip(' ,;:') + '\u2026') if len(excerpt) > 180 else excerpt, quote=False)}</p>
      <span class="arrow">→</span>
    </a></li>""")

    blog_list = '\n'.join(entries)

    # MUSE 5: the blog index was a link silo (0 links to /tools/* or /categories/*).
    # Count active tools for the directory strip below.
    try:
        _tdata = json.loads((Path(__file__).resolve().parent.parent / "tools" / "tools.json").read_text())
        _tlist = _tdata if isinstance(_tdata, list) else _tdata.get("tools", [])
        all_tools = sum(1 for _t in _tlist if _t.get("status") == "active")
    except Exception:
        all_tools = 129

    # Blog + ItemList structured data (the only page that lacked ld+json)
    item_list = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": "https://martechsignal.com/blog/#blog",
        "name": "MartechSignal Blog",
        "url": "https://martechsignal.com/blog/",
        "description": "Deep-dives, tool teardowns, and hot takes on AI in marketing automation.",
        "inLanguage": "en",
        "publisher": {"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/"},
        "blogPost": [
            {
                "@type": "BlogPosting",
                "headline": p['title'],
                "url": f"https://martechsignal.com/blog/{p.get('slug', slugify(p['title']))}/",
                "datePublished": p['date'],
                "isPartOf": {"@id": "https://martechsignal.com/blog/#blog"},
            }
            for p in posts_sorted
        ],
    }
    import json as _json
    schema_tag = f'<script type="application/ld+json">{_json.dumps(item_list, indent=2)}</script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog | MartechSignal</title>
<meta name="description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MartechSignal">
<link rel="alternate" type="text/plain" title="MartechSignal catalog for AI systems" href="/llms.txt">
<meta property="og:title" content="Blog | MartechSignal">
<meta property="og:description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<meta property="og:url" content="https://martechsignal.com/blog/">
<meta property="og:image" content="https://martechsignal.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Blog | MartechSignal">
<meta name="twitter:description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<meta name="twitter:image" content="https://martechsignal.com/og.png">
<link rel="canonical" href="https://martechsignal.com/blog/">
<link rel="ard ai-catalog" href="https://martechsignal.com/.well-known/ard.json">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="alternate" type="application/rss+xml" title="MartechSignal" href="/rss.xml">
<link rel="preconnect" href="https://analytics.martechsignal.com" crossorigin>
<link rel="dns-prefetch" href="https://analytics.martechsignal.com">
{_shared_tags()}
{schema_tag}
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"}}, {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://martechsignal.com/blog/"}}]}}</script>
  <script src="/site.js" defer></script>
  </head>
<body class="page-blog-index">
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="pulse-dot"></span></a>
    <nav class="mast-nav"><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/categories/">CATEGORIES</a><a href="/glossary/">GLOSSARY</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
  <div class="page-head reveal">
    <p class="kicker">// THE BLOG | DEEPER THAN THE NEWSLETTER</p>
    <h1>Long-form signal.</h1>
    <p>Tool teardowns, workflow recipes, and vendor moves decoded | published between newsletter issues.</p>
  </div>
  <div class="sub-strip reveal">
    <div>
      <h2>Prefer it in your inbox?</h2>
      <p>The best of this, curated weekly. Free, 5-minute read.</p>
    </div>
    <a class="btn" href="/#subscribe" data-umami-event="Blog subscribe click">Subscribe</a>
  </div>
  <section class="cat-strip reveal" aria-label="Browse the tool directory">
    <h2>Browse the tool directory</h2>
    <p>Browse the directory these teardowns draw from:</p>
    <p class="integ-list">
      <a href="/categories/marketing-automation/">Marketing automation</a>
      <a href="/categories/workflow-automation/">Workflow automation</a>
      <a href="/categories/crm/">CRM</a>
      <a href="/categories/analytics/">Analytics</a>
      <a href="/categories/seo/">SEO</a>
      <a href="/categories/open-source/">Open source</a>
    </p>
    <p class="integ-list">
      <a href="/tools/nocobase/">NocoBase</a>
      <a href="/tools/amplitude/">Amplitude</a>
      <a href="/tools/claude-seo/">Claude SEO</a>
      <a href="/tools/segment/">Segment</a>
      <a href="/tools/matomo/">Matomo</a>
      <a href="/tools/alphone/">AlphOne</a>
      <a href="/tools/">All {all_tools} tools &#8594;</a>
    </p>
    <p>Before you buy: the <a href="/checklist/">marketing automation checklist</a> scores your stack on the 12 things that decide whether AI can run any of it.</p>
  </section>
  <ul class="post-list">
{blog_list}
  </ul>
</main>
<footer>
  <div class="foot-in">
    <p>© {datetime.now().year} MartechSignal · by Tim Christensen</p>
    <nav class="foot-links"><a href="/">HOME</a><a href="/tools/">TOOLS</a><a href="/best/">BEST</a><a href="/vs/">VS</a><a href="/alternatives/">ALTERNATIVES</a><a href="/blog/">BLOG</a><a href="/trending/">TRENDING</a><a href="/glossary/">GLOSSARY</a><a href="/checklist/">CHECKLIST</a><a href="/authors/tim-christensen/">Tim Christensen</a><a href="/about/">ABOUT</a><a href="/contact/">CONTACT</a><a href="/privacy/">PRIVACY</a><a href="/terms/">TERMS</a><a href="/ai-policy/">AI POLICY</a><a href="/methodology/">METHODOLOGY</a><a href="/rss.xml">RSS</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</footer>

{_H9_TAG}</body>
</html>"""


def apply_fill_to_legacy_posts():
    """Inject directory-fill links into hand-crafted posts that bypass build_post."""
    plan = getattr(suggest_links, "_CATEGORY_FILL_PLAN", {})
    if not plan:
        return 0
    applied = 0
    by_slug = {t["slug"]: t for t in suggest_links.json.loads(suggest_links.TOOLS_JSON.read_text())}
    for f in sorted(BLOG_DIR.glob("*/index.html")):
        slug = f.parent.name
        slugs_to_link = plan.get(slug, [])
        if not slugs_to_link:
            continue
        html_src = f.read_text()
        # strip any previous fill line so we always render the current plan
        # preserve already-rendered fill links; the plan adds missing ones
        kept = re.findall(r'More from the directory:(.*?)</p>', html_src, flags=re.S)
        kept_slugs = set(re.findall(r'/tools/([^/"]+)/', kept[0])) if kept else set()
        html_src = re.sub(r'<p class="more-tools"[^>]*>More from the directory:.*?</p>\n?', "", html_src, flags=re.S)
        links = []
        # re-render kept links first (they were stripped above)
        for s in sorted(kept_slugs):
            tmeta = by_slug.get(s)
            if tmeta and tmeta.get("status") == "active":
                links.append(f'<a href="/tools/{s}/">{html.escape(tmeta["name"], quote=False)}</a>')
        for s in slugs_to_link:
            tmeta = by_slug.get(s)
            if tmeta and tmeta.get("status") == "active" and f"/tools/{s}/" not in html_src and s not in kept_slugs:
                links.append(f'<a href="/tools/{s}/">{html.escape(tmeta["name"], quote=False)}</a>')
        if not links:
            continue
        mlinks = " \u00b7 ".join(links)
        line = f'<p class="more-tools" style="font-size:.85rem;color:var(--muted)">More from the directory: {mlinks}</p>'
        if "</article>" in html_src:
            html_src = html_src.replace("</article>", line + "\n</article>", 1)
        else:
            html_src = html_src.replace("</main>", line + "\n</main>", 1)
        f.write_text(html_src)
        applied += 1
        print(f"  + fill -> {slug}")
    return applied


def scan_existing_posts(draft_slugs: set) -> list:
    """Scan blog/ for existing posts not generated from drafts."""
    posts = []
    if not BLOG_DIR.is_dir():
        return posts

    for child in sorted(BLOG_DIR.iterdir()):
        if not child.is_dir():
            continue
        if child.name == 'index.html':
            continue

        slug = child.name
        if slug in draft_slugs:
            continue  # Will be rebuilt from draft

        post_file = child / 'index.html'
        if not post_file.exists():
            continue

        html_content = post_file.read_text()

        # Extract title from <title>...</title>
        m = re.search(r'<title>(.+?)(?:\s+-\s+Martech\s+Signal)?</title>', html_content)
        title = html.unescape(m.group(1).strip()) if m else slug.replace('-', ' ').title()

        # Extract date from meta line "JUL 28, 2026" or fallback to datePublished JSON-LD
        m = re.search(r'<p class="meta">([A-Z]{3}\s+\d{2},\s+\d{4})', html_content)
        if m:
            date_display = m.group(1)
            date_obj = datetime.strptime(date_display, '%b %d, %Y')
            date_str = date_obj.strftime('%Y-%m-%d')
        else:
            m = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', html_content)
            date_str = m.group(1) if m else '2026-01-01'

        # Extract excerpt from og:description or meta description
        m = re.search(r'<meta name="description" content="([^"]+)"', html_content)
        excerpt = html.unescape(m.group(1)[:180]) if m else ''
        if not excerpt:
            m = re.search(r'<meta property="og:description" content="([^"]+)"', html_content)
            excerpt = html.unescape(m.group(1)[:180]) if m else ''

        posts.append({
            'title': title,
            'date': date_str,
            'slug': slug,
            'excerpt': excerpt,
        })

    return posts


def update_homepage(posts: list, count: int = 4) -> bool:
    """Regenerate the 'Latest signals' block in the hand-crafted homepage.

    Replaces only the content between <!-- LATEST:START --> and
    <!-- LATEST:END --> markers in index.html, leaving the rest of the
    hand-maintained page untouched. Returns True if the page changed.
    """
    homepage = ROOT / "index.html"
    if not homepage.exists():
        print("Homepage index.html not found, skipping latest-signals update.")
        return False

    posts_sorted = sorted(posts, key=lambda p: p['date'], reverse=True)[:count]
    if not posts_sorted:
        print("No posts to feature on homepage.")
        return False

    rows = []
    for idx, post in enumerate(posts_sorted, start=1):
        title = html.escape(post['title'], quote=False)
        slug = post.get('slug', slugify(post['title']))
        # r11 M-7 (2026-09-29): word-boundary cut with ellipsis — the old
        # raw excerpt ran mid-word ("specification c", "actually me").
        _raw = post.get('excerpt', '')
        _cut = _raw[:180].rsplit(' ', 1)[0] if len(_raw) > 180 else _raw
        excerpt = html.escape(_cut.rstrip(' ,;:') + ('\u2026' if len(_raw) > 180 else ''), quote=False)
        date_disp = post['date']
        rows.append(
            f'    <a class="story reveal" href="/blog/{slug}/">\n'
            f'      <div class="story-head"><span class="kicker">BLOG · {date_disp}</span><span class="no">{idx:02d}</span></div>\n'
            f'      <h3>{title}</h3>\n'
            f'      <p>{excerpt}</p>\n'
            f'      <span class="story-cta">READ →</span>\n'
            f'    </a>'
        )
    block = "\n".join(rows)

    content = homepage.read_text()
    pattern = re.compile(
        r'(<!-- LATEST:START -->\n).*?(\n\s*<!-- LATEST:END -->)',
        re.DOTALL,
    )
    if not pattern.search(content):
        print("⚠ LATEST markers not found in index.html - homepage not updated.")
        return False

    new_content = pattern.sub(lambda m: m.group(1) + block + m.group(2), content)
    if new_content == content:
        print("Homepage latest-signals already up to date.")
        return False

    homepage.write_text(new_content)
    print(f"Homepage: latest {len(posts_sorted)} posts updated in index.html")
    return True


def build_rss(posts: list) -> str:
    """Generate RSS 2.0 XML for the blog (newest first)."""
    site_url = "https://martechsignal.com"
    posts_sorted = sorted(posts, key=lambda p: p['date'], reverse=True)
    now = datetime.now(timezone.utc)
    last_build = email.utils.format_datetime(now)
    items = []
    for post in posts_sorted:
        title = post['title']
        slug = post.get('slug', slugify(title))
        link = f"{site_url}/blog/{slug}/"
        excerpt = post.get('excerpt', '')
        date_str = post.get('date', now.strftime('%Y-%m-%d'))
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            pub_date = email.utils.format_datetime(dt)
        except Exception:
            pub_date = last_build
        # Description as escaped HTML excerpt
        desc = html.escape(excerpt[:300], quote=False) if excerpt else html.escape(title, quote=False)
        items.append(
            f"    <item>\n"
            f"      <title>{html.escape(title, quote=False)}</title>\n"
            f"      <link>{link}</link>\n"
            f"      <guid isPermaLink=\"true\">{link}</guid>\n"
            f"      <pubDate>{pub_date}</pubDate>\n"
            f"      <description>{desc}</description>\n"
            f"    </item>"
        )
    items_xml = "\n".join(items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>MartechSignal | AI Marketing Automation, Audited</title>
    <link>{site_url}/</link>
    <description>Weekly analysis of AI marketing automation tools, agentic workflows, and vendor strategy.</description>
    <language>en-us</language>
    <lastBuildDate>{last_build}</lastBuildDate>
    <generator>build_blog.py</generator>
{items_xml}
  </channel>
</rss>
"""


def main():
    # Track which slugs have drafts
    draft_slugs = set()
    posts = []

    # Early plan: lets build_post render directory-fill inline for draft posts
    try:
        suggest_links.set_category_fill_plan(suggest_links.build_category_fill_plan(max_per_post=8))
    except Exception as e:
        print(f"  (early fill plan skipped: {e})")


    drafts = list(DRAFTS_DIR.glob('*.md')) if DRAFTS_DIR.is_dir() else []
    if not drafts:
        print("No drafts found - refreshing index/homepage from existing posts.")

    # Process each draft
    for draft_path in sorted(drafts):
        print(f"Building: {draft_path.name}")

        text = draft_path.read_text()
        meta, body_md = parse_frontmatter(text)
        meta['_draft_path'] = str(draft_path)  # R2 M-7: dateModified from git mtime

        if not meta.get('title'):
            print(f"  ⚠ No title in frontmatter, skipping")
            continue

        title = meta['title']
        date_str = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
        slug = meta.get('slug') or slugify(title)

        # Convert markdown to HTML
        body_html = markdown_to_html(body_md)

        # Generate post HTML
        post_html = build_post(meta, body_html)

        # Extract excerpt. r11 M-7 (2026-09-29): word-boundary cut with
        # ellipsis — the raw [:180] slice fed mid-word homepage cards.
        first_p = re.search(r'<p>(.+?)</p>', body_html, re.DOTALL)
        _raw_d = re.sub(r'<[^>]+>', '', first_p.group(1)) if first_p else ''
        excerpt = (_raw_d[:180].rsplit(' ', 1)[0].rstrip(' ,;:') + '\u2026'
                   if len(_raw_d) > 180 else _raw_d)

        # Write post
        out_dir = BLOG_DIR / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / 'index.html').write_text(post_html)
        print(f"  ✓ blog/{slug}/index.html")

        # Track for index
        draft_slugs.add(slug)
        posts.append({
            'title': title,
            'date': date_str,
            'slug': slug,
            'excerpt': excerpt,
        })

    # Add existing posts (hand-crafted HTML, not from drafts)
    existing = scan_existing_posts(draft_slugs)
    if existing:
        print(f"\nExisting posts scanned: {len(existing)}")
    posts.extend(existing)

    # Directory coverage pass: runs AFTER all Related-tools links are on disk,
    # so the plan sees true orphans. Patches every post in place (draft + legacy).
    # Re-plan + re-apply up to 3x so stragglers created mid-pass get picked up;
    # stops early when a pass assigns nothing new (converged).
    try:
        suggest_links.set_category_fill_plan(suggest_links.build_category_fill_plan(max_per_post=8))
        apply_fill_to_legacy_posts()
    except Exception as e:
        print(f"  (directory coverage skipped: {e})")

    # Build blog index
    index_html = build_index(posts)
    (BLOG_DIR / 'index.html').write_text(index_html)
    print(f"\nBlog index: {len(posts)} posts written to blog/index.html")

    # Refresh the hand-crafted homepage's "Latest signals" block
    update_homepage(posts)

    # Generate RSS feed
    rss_xml = build_rss(posts)
    (ROOT / "rss.xml").write_text(rss_xml)
    print(f"RSS: {len(posts)} items written to rss.xml", flush=True)


if __name__ == '__main__':
    main()
