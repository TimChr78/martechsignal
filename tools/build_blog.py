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

ROOT = Path(__file__).resolve().parent.parent
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
        if colon:  # a key — a quoted token followed by ':'
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
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|-\s|:::\s|[-—]{2,}$)', lines[i]):
                if '</' in lines[i] and not ('</' in html_lines[-1]):
                    html_lines.append(lines[i])
                    i += 1
                    if '>' in lines[i-1]:
                        break
                    continue
                break
            out.append('\n'.join(html_lines))
            continue

        # Horizontal rule (--- or —)
        if re.match(r'^[-—]{2,}$', line.strip()):
            out.append('<hr>')
            i += 1
            continue

        # Blockquote-like (lines starting with >)
        # Paragraph (collect until blank line)
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|-\s|[-—]{2,}$)', lines[i]):
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
    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)

    # Em dash
    text = text.replace('--', '—')
    text = text.replace(' — ', ' — ')

    return text



def _build_toc_and_chip(body_html: str, categories=None):
    """Audit M-9/M-8: anchored mini-TOC on long posts + 'Filed under' category chips."""
    import re as _re
    words = len(_re.findall(r"\b\w+\b", _re.sub(r"<[^>]+>", " ", body_html)))
    chip_html = ""
    if categories:
        links = " · ".join(
            f'<a href="/categories/{c}/">{str(c).replace("-", " ").title()}</a>'
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
    """Word-boundary meta excerpt with terminal punctuation; no mid-word cuts (audit H-3)."""
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    sp = text.rfind(" ", 0, limit - 1)
    text = text[:sp] if sp > 60 else text[:limit - 3]
    return text.rstrip(" ,;:.—-") + "."

def build_post(meta: dict, body_html: str) -> str:
    """Generate the full HTML page for a blog post."""
    title = meta.get('title', 'Untitled')
    body_html, extras = _build_toc_and_chip(body_html, meta.get('categories') or meta.get('category'))
    # SEO title: optional frontmatter override (<=60ch) for <title>/og:title; H1 keeps full title
    seo_title = meta.get('seo_title') or title
    date_str = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
    date_display = datetime.strptime(date_str, '%Y-%m-%d').strftime('%b %d, %Y').upper()
    slug = meta.get('slug') or slugify(title)

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
        tlinks = ''.join('<li><a href="' + html.escape(item['url'], quote=True) + '">' + html.escape(item['name'], quote=False) + '</a> — ' + html.escape(item.get('tagline',''), quote=False) + '</li>' for item in related_tools)
        body_html += '<section class="related-tools"><h2>Related tools</h2><ul>' + tlinks + '</ul></section>'
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

    # First paragraph as excerpt (strip HTML tags)
    first_p = re.search(r'<p>(.+?)</p>', body_html, re.DOTALL)
    excerpt = re.sub(r'<[^>]+>', '', first_p.group(1))[:200] if first_p else ''

    # Read time from word count (~200 wpm), tags as kicker
    words = len(re.sub(r'<[^>]+>', ' ', body_html).split())
    read_min = max(1, round(words / 200))
    tags = meta.get('tags', [])
    kicker = ' · '.join(t.upper() for t in tags[:2]) if tags else 'DEEP DIVE · MARTECH'
    # Human byline — the site's named author (see footer/about); org stays in JSON-LD
    byline = 'Tim Christensen'

    # JSON-LD: Article + BreadcrumbList (Google starter guide: structured data for title/breadcrumb)
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": _clean_excerpt(excerpt),
        "author": {"@type": "Person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]},
        "publisher": {"@type": "Organization", "name": "MartechSignal", "url": "https://martechsignal.com", "logo": {"@type": "ImageObject", "url": "https://martechsignal.com/og.png"}},
        "datePublished": date_str,
        "dateModified": date_str,
        "mainEntityOfPage": f"https://martechsignal.com/blog/{slug}/",
        "image": f"https://martechsignal.com/og/{slug}.png",
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
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23080E1A'/%3E%3Crect x='9' y='7' width='14' height='18' rx='2' fill='%23FFB224'/%3E%3C/svg%3E">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Martech Signal">
<meta property="og:title" content="{html.escape(seo_title)}">
<meta property="og:description" content="{html.escape(_clean_excerpt(excerpt))}">
<meta property="og:url" content="https://martechsignal.com/blog/{slug}/">
<meta property="og:image" content="https://martechsignal.com/og/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://martechsignal.com/blog/{slug}/">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet"></noscript>
<script type="application/ld+json">
{json.dumps(article_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(breadcrumb_schema, indent=2)}
</script>
<link rel="stylesheet" href="/style.css?v=69b0f800">
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
</head>
<body class="page-post">
<div class="bg" aria-hidden="true"></div>
<div id="progress" aria-hidden="true"></div>
<header class="masthead">
  <div class="mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="cursor">▮</span></a>
    <nav class="mast-nav"><a href="/tools/">TOOLS</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
<a class="back" href="/blog/">← ALL WRITING</a>
<article>

<p class="kicker">{kicker} · {read_min} MIN</p>
<h1>{html.escape(title)}</h1>
<p class="meta">{date_display}</p>
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
    <p><b>MartechSignal</b> — written by <a href="/authors/tim-christensen/" style="color:inherit">Tim Christensen</a></p>
    <nav class="foot-links"><a href="/blog/">WRITING</a><a href="/rss.xml">RSS</a><a href="/tools/">TOOLS</a><a href="/authors/tim-christensen/">AUTHOR</a><a href="/about/">ABOUT</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</footer>
<script>
(function(){{
  var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bar=document.getElementById('progress');
  if(bar){{addEventListener('scroll',function(){{var h=document.documentElement;bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';}},{{passive:true}});}}
  if('IntersectionObserver' in window){{
    var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.1}});
    document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el);}});
  }}else{{document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}});}}
}})();
</script>
</body>
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

        entries.append(f"""    <li class="reveal"><a class="sig" href="/blog/{slug}/">
      <span class="idx">{idx:02d}</span>
      <span><h2>{html.escape(title, quote=False)}</h2>
      <span class="sub">{date}</span>
      <p class="excerpt">{html.escape(excerpt[:180], quote=False)}</p></span>
      <span class="arrow">→</span>
    </a></li>""")

    blog_list = '\n'.join(entries)

    # Blog + ItemList structured data (the only page that lacked ld+json)
    item_list = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "MartechSignal Blog",
        "url": "https://martechsignal.com/blog/",
        "description": "Deep-dives, tool teardowns, and hot takes on AI in marketing automation.",
        "publisher": {"@type": "Organization", "name": "MartechSignal", "url": "https://martechsignal.com/"},
        "blogPost": [
            {
                "@type": "BlogPosting",
                "headline": p['title'],
                "url": f"https://martechsignal.com/blog/{p.get('slug', slugify(p['title']))}/",
                "datePublished": p['date'],
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
<title>Blog — Martech Signal</title>
<meta name="description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23080E1A'/%3E%3Crect x='9' y='7' width='14' height='18' rx='2' fill='%23FFB224'/%3E%3C/svg%3E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Martech Signal">
<meta property="og:title" content="Blog — Martech Signal">
<meta property="og:description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<meta property="og:url" content="https://martechsignal.com/blog/">
<meta property="og:image" content="https://martechsignal.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Blog — Martech Signal">
<meta name="twitter:description" content="Deep-dives, tool teardowns, and hot takes on AI in marketing automation.">
<meta name="twitter:image" content="https://martechsignal.com/og.png">
<link rel="canonical" href="https://martechsignal.com/blog/">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="alternate" type="application/rss+xml" title="Martech Signal" href="/rss.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet"></noscript>
<link rel="stylesheet" href="/style.css?v=69b0f800">
{schema_tag}
<script defer src="https://analytics.martechsignal.com/script.js" data-website-id="11b28e66-3570-4781-b369-2134c7c372ab"></script>
</head>
<body class="page-blog-index">
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="cursor">▮</span></a>
    <nav class="mast-nav"><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
  <div class="page-head reveal">
    <p class="kicker">// THE BLOG — DEEPER THAN THE NEWSLETTER</p>
    <h1>Long-form signal.</h1>
    <p>Tool teardowns, workflow recipes, and vendor moves decoded — published between newsletter issues.</p>
  </div>
  <div class="sub-strip reveal">
    <div>
      <h3>Prefer it in your inbox?</h3>
      <p>The best of this, curated weekly. Free, 5-minute read.</p>
    </div>
    <a class="btn" href="/#subscribe" data-umami-event="Blog subscribe click">Subscribe</a>
  </div>
  <ul class="post-list">
{blog_list}
  </ul>
</main>
<footer>
  <div class="foot-in">
    <p>© {datetime.now().year} Martech Signal · by Tim Christensen</p>
    <nav class="foot-links"><a href="/blog/">BLOG</a><a href="/rss.xml">RSS</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</footer>
<script>
if('IntersectionObserver' in window){{
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.1}});
  document.querySelectorAll('.reveal').forEach(function(el){{io.observe(el);}});
}}else{{document.querySelectorAll('.reveal').forEach(function(el){{el.classList.add('in');}});}}
</script>
</body>
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
        m = re.search(r'<title>(.+?)(?:\s+—\s+Martech\s+Signal)?</title>', html_content)
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
        excerpt = html.escape(post.get('excerpt', ''), quote=False)
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
        print("⚠ LATEST markers not found in index.html — homepage not updated.")
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
    <title>MartechSignal — AI Marketing Automation, Audited</title>
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
        print("No drafts found — refreshing index/homepage from existing posts.")

    # Process each draft
    for draft_path in sorted(drafts):
        print(f"Building: {draft_path.name}")

        text = draft_path.read_text()
        meta, body_md = parse_frontmatter(text)

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

        # Extract excerpt
        first_p = re.search(r'<p>(.+?)</p>', body_html, re.DOTALL)
        excerpt = re.sub(r'<[^>]+>', '', first_p.group(1))[:180] if first_p else ''

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
