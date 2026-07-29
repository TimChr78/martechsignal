#!/usr/bin/env python3
"""Build blog posts from drafts and regenerate the blog index.

Reads content/drafts/*.md → generates blog/{slug}/index.html
Updates blog/index.html with all published posts.

Run from /opt/data/martechsignal/: python3 tools/build_blog.py
"""

import re
import html
import json
from pathlib import Path
from datetime import datetime

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


def build_post(meta: dict, body_html: str) -> str:
    """Generate the full HTML page for a blog post."""
    title = meta.get('title', 'Untitled')
    date_str = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
    date_display = datetime.strptime(date_str, '%Y-%m-%d').strftime('%b %d, %Y').upper()
    slug = slugify(title)

    # First paragraph as excerpt (strip HTML tags)
    first_p = re.search(r'<p>(.+?)</p>', body_html, re.DOTALL)
    excerpt = re.sub(r'<[^>]+>', '', first_p.group(1))[:200] if first_p else ''

    # JSON-LD
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": excerpt[:160],
        "author": {"@type": "Organization", "name": "MartechSignal"},
        "publisher": {"@type": "Organization", "name": "MartechSignal", "url": "https://martechsignal.com"},
        "datePublished": date_str,
        "dateModified": date_str,
        "mainEntityOfPage": f"https://martechsignal.com/blog/{slug}/"
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — Martech Signal</title>
<meta name="description" content="{html.escape(excerpt[:160])}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23080E1A'/%3E%3Crect x='9' y='7' width='14' height='18' rx='2' fill='%23FFB224'/%3E%3C/svg%3E">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Martech Signal">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(excerpt[:160])}">
<meta property="og:url" content="https://martechsignal.com/blog/{slug}/">
<meta property="og:image" content="https://martechsignal.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://martechsignal.com/blog/{slug}/">
<meta name="msvalidate.01" content="B3427474AF36B6861E22592403BA8B27">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script type="application/ld+json">
{json.dumps(schema, indent=2)}
</script>
<style>
:root{{
  --bg:#080E1A; --card:#0F1B31; --line:#1D2B47; --line2:#2A3D63;
  --text:#E9EEF8; --muted:#8FA1C0; --amber:#FFB224; --green:#3DDC97;
  --red:#F87171;
  --mono:'Spline Sans Mono',ui-monospace,monospace; --disp:'Archivo Black',sans-serif; --body:'Archivo',sans-serif;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:var(--body);line-height:1.7;-webkit-font-smoothing:antialiased}}
::selection{{background:var(--amber);color:#141005}}
a{{color:inherit}}
.bg{{position:fixed;inset:0;z-index:-1;
  background:
    radial-gradient(900px 520px at 88% -8%, rgba(255,178,36,.10), transparent 62%),
    radial-gradient(760px 560px at -12% 34%, rgba(61,220,151,.06), transparent 60%),
    var(--bg);}}
.bg::before{{content:"";position:absolute;inset:0;
  background-image:linear-gradient(rgba(140,165,210,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(140,165,210,.05) 1px,transparent 1px);
  background-size:46px 46px;
  mask-image:radial-gradient(ellipse 90% 70% at 50% 0%,#000 30%,transparent 100%);}}
.wrap{{max-width:720px;margin:0 auto;padding:0 1.25rem}}
.masthead{{border-bottom:1px solid var(--line)}}
.mast-in{{max-width:1080px;margin:0 auto;padding:1.1rem 1.25rem;display:flex;align-items:center;justify-content:space-between}}
.wordmark{{font-family:var(--disp);font-size:1.15rem;letter-spacing:.03em;text-decoration:none}}
.wordmark b{{color:var(--amber);font-weight:inherit}}
.cursor{{color:var(--amber);animation:blink 1.1s steps(2) infinite;margin-left:2px}}
@keyframes blink{{50%{{opacity:0}}}}
.mast-nav{{display:flex;gap:1.4rem}}
.mast-nav a{{font:600 .74rem var(--mono);letter-spacing:.14em;color:var(--muted);text-decoration:none;transition:color .2s}}
.mast-nav a:hover{{color:var(--amber)}}
.back{{display:inline-block;margin:2.4rem 0 0;font:600 .74rem var(--mono);letter-spacing:.14em;color:var(--muted);text-decoration:none;transition:color .2s}}
.back:hover{{color:var(--amber)}}
article{{padding:1.6rem 0 3rem}}
.kicker{{font:600 .72rem var(--mono);letter-spacing:.16em;color:var(--amber);margin-bottom:1rem}}
article h1{{font-family:var(--disp);font-weight:400;font-size:clamp(1.9rem,4.4vw,2.9rem);line-height:1.12;letter-spacing:-.015em;margin-bottom:1rem}}
.meta{{font:500 .74rem var(--mono);letter-spacing:.12em;color:var(--muted);margin-bottom:2.4rem;padding-bottom:1.4rem;border-bottom:1px solid var(--line)}}
.meta a{{color:var(--amber);text-decoration:none}}
.meta a:hover{{text-decoration:underline}}
article h2{{font-family:var(--disp);font-weight:400;font-size:1.45rem;letter-spacing:-.01em;margin:2.6rem 0 .9rem}}
article h3{{font:700 1.15rem var(--body);margin:2rem 0 .7rem}}
article p{{margin-bottom:1.15rem;font-size:1.05rem;color:#D5DDEB}}
article a{{color:var(--amber);text-decoration:none;border-bottom:1px solid rgba(255,178,36,.4);transition:border-color .2s}}
article a:hover{{border-color:var(--amber)}}
article ul,article ol{{margin:0 0 1.2rem 1.4rem}}
article li{{margin-bottom:.5rem;color:#D5DDEB}}
article blockquote{{border-left:3px solid var(--amber);background:var(--card);border-radius:0 8px 8px 0;padding:1.2rem 1.5rem;margin:1.6rem 0;color:var(--text);font-weight:500}}
article blockquote p{{margin:0;color:var(--text)}}
article strong{{color:var(--text)}}
article hr{{border:none;border-top:1px solid var(--line);margin:1.6rem 0}}
code{{font-family:var(--mono);font-size:.82rem;background:rgba(15,27,49,.8);padding:1px 6px;border-radius:3px;border:1px solid var(--line)}}
.cta-strip{{background:linear-gradient(180deg,rgba(255,178,36,.07),transparent 55%),var(--card);border:1px solid var(--line2);border-top:3px solid var(--amber);border-radius:10px;padding:1.8rem 1.9rem;margin:2.5rem 0 3.5rem}}
.cta-strip h3{{font-family:var(--disp);font-weight:400;font-size:1.25rem;margin-bottom:.4rem}}
.cta-strip p{{color:var(--muted);font-size:.95rem;margin-bottom:1.1rem}}
.btn{{display:inline-block;background:var(--amber);color:#141005;font:700 .92rem var(--body);text-decoration:none;padding:.75rem 1.5rem;border-radius:6px;transition:transform .2s,box-shadow .2s}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 10px 28px rgba(255,178,36,.3)}}
footer{{border-top:1px solid var(--line);padding:2.2rem 0}}
.foot-in{{max-width:1080px;margin:0 auto;padding:0 1.25rem;display:flex;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;align-items:center}}
.foot-in p{{color:var(--muted);font-size:.85rem}}
.foot-links{{display:flex;gap:1.4rem}}
.foot-links a{{font:600 .72rem var(--mono);letter-spacing:.12em;color:var(--muted);text-decoration:none}}
.foot-links a:hover{{color:var(--amber)}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}}
.reveal.in{{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important}}.reveal{{opacity:1;transform:none}}}}
</style>
</head>
<body>
<div class="bg" aria-hidden="true"></div>
<header class="masthead">
  <div class="mast-in">
    <a class="wordmark" href="/">MARTECH<b>SIGNAL</b><span class="cursor">▮</span></a>
    <nav class="mast-nav"><a href="/tools/">TOOLS</a><a href="/blog/">BLOG</a><a href="/#subscribe">SUBSCRIBE</a></nav>
  </div>
</header>
<main class="wrap">
<a class="back" href="/blog/">← ALL POSTS</a>
<article>

<p class="kicker">DEEP DIVE · MARTECH</p>
<h1>{html.escape(title)}</h1>
<p class="meta">{date_display} · BY <a href="/">MARTECHSIGNAL</a></p>

{body_html}

<div class="cta-strip">
<h3>Get the Weekly Signal</h3>
<p>One sharp email every Friday: the AI tools, workflows, and vendor moves that actually matter for marketing automation.</p>
<a class="btn" href="/#subscribe">SUBSCRIBE →</a>
</div>

</article>
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
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&family=Spline+Sans+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#080E1A; --card:#0F1B31; --line:#1D2B47; --line2:#2A3D63;
  --text:#E9EEF8; --muted:#8FA1C0; --amber:#FFB224; --green:#3DDC97;
  --mono:'Spline Sans Mono',ui-monospace,monospace; --disp:'Archivo Black',sans-serif; --body:'Archivo',sans-serif;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:var(--body);line-height:1.65;-webkit-font-smoothing:antialiased}}
::selection{{background:var(--amber);color:#141005}}
a{{color:inherit}}
.bg{{position:fixed;inset:0;z-index:-1;
  background:
    radial-gradient(900px 520px at 88% -8%, rgba(255,178,36,.10), transparent 62%),
    radial-gradient(760px 560px at -12% 34%, rgba(61,220,151,.06), transparent 60%),
    var(--bg);}}
.bg::before{{content:"";position:absolute;inset:0;
  background-image:linear-gradient(rgba(140,165,210,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(140,165,210,.05) 1px,transparent 1px);
  background-size:46px 46px;
  mask-image:radial-gradient(ellipse 90% 70% at 50% 0%,#000 30%,transparent 100%);}}
.mono{{font-family:var(--mono)}}
.masthead{{border-bottom:1px solid var(--line)}}
.mast-in{{max-width:1080px;margin:0 auto;padding:1.1rem 1.25rem;display:flex;align-items:center;justify-content:space-between}}
.wordmark{{font-family:var(--disp);font-size:1.15rem;letter-spacing:.03em;text-decoration:none}}
.wordmark b{{color:var(--amber);font-weight:inherit}}
.cursor{{color:var(--amber);animation:blink 1.1s steps(2) infinite;margin-left:2px}}
@keyframes blink{{50%{{opacity:0}}}}
.mast-nav{{display:flex;gap:1.4rem}}
.mast-nav a{{font:600 .74rem var(--mono);letter-spacing:.14em;color:var(--muted);text-decoration:none;transition:color .2s}}
.mast-nav a:hover{{color:var(--amber)}}
.wrap{{max-width:820px;margin:0 auto;padding:0 1.25rem}}
.page-head{{padding:3.6rem 0 2.4rem}}
.kicker{{font:600 .72rem var(--mono);letter-spacing:.16em;color:var(--amber);margin-bottom:1rem}}
h1{{font-family:var(--disp);font-weight:400;font-size:clamp(2rem,4.6vw,3rem);letter-spacing:-.015em;line-height:1.08}}
.page-head p{{color:var(--muted);margin-top:1rem;max-width:34rem;font-size:1.05rem}}
.post-list{{list-style:none;padding-bottom:3.5rem}}
.post-list li{{border-top:1px solid var(--line)}}
.post-list li:last-child{{border-bottom:1px solid var(--line)}}
.sig{{display:grid;grid-template-columns:auto 1fr auto;gap:1.4rem;align-items:baseline;padding:1.5rem .8rem;text-decoration:none;transition:background .25s,transform .25s}}
.sig:hover{{background:rgba(15,27,49,.75);transform:translateX(6px)}}
.sig .idx{{font:600 .82rem var(--mono);color:var(--amber)}}
.sig h2{{font:700 1.3rem/1.3 var(--body);letter-spacing:-.01em}}
.sig .sub{{font:500 .72rem var(--mono);letter-spacing:.1em;color:var(--muted);margin-top:.4rem}}
.sig .excerpt{{color:var(--muted);font-size:.93rem;margin-top:.45rem;max-width:38rem}}
.sig .arrow{{font-family:var(--mono);color:var(--amber);opacity:0;transform:translateX(-6px);transition:opacity .25s,transform .25s}}
.sig:hover .arrow{{opacity:1;transform:none}}
@media(max-width:560px){{.sig{{grid-template-columns:auto 1fr}}.sig .arrow{{display:none}}}}
.sub-strip{{background:linear-gradient(180deg,rgba(255,178,36,.07),transparent 55%),var(--card);border:1px solid var(--line2);border-top:3px solid var(--amber);border-radius:10px;padding:1.8rem 1.9rem;margin-bottom:3.5rem;display:flex;justify-content:space-between;align-items:center;gap:1.5rem;flex-wrap:wrap}}
.sub-strip h3{{font-family:var(--disp);font-weight:400;font-size:1.25rem;margin-bottom:.3rem}}
.sub-strip p{{color:var(--muted);font-size:.92rem}}
.btn{{display:inline-block;background:var(--amber);color:#141005;font:700 .92rem var(--body);text-decoration:none;padding:.75rem 1.5rem;border-radius:6px;transition:transform .2s,box-shadow .2s}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 10px 28px rgba(255,178,36,.3)}}
footer{{border-top:1px solid var(--line);padding:2.2rem 0}}
.foot-in{{max-width:1080px;margin:0 auto;padding:0 1.25rem;display:flex;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;align-items:center}}
.foot-in p{{color:var(--muted);font-size:.85rem}}
.foot-links{{display:flex;gap:1.4rem}}
.foot-links a{{font:600 .72rem var(--mono);letter-spacing:.12em;color:var(--muted);text-decoration:none}}
.foot-links a:hover{{color:var(--amber)}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}}
.reveal.in{{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important}}.reveal{{opacity:1;transform:none}}}}
</style>
</head>
<body>
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
    <a class="btn" href="/#subscribe">Subscribe</a>
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


def main():
    # Track which slugs have drafts
    draft_slugs = set()
    posts = []

    if not DRAFTS_DIR.is_dir():
        print("No drafts directory found. Nothing to build.")
        return

    drafts = list(DRAFTS_DIR.glob('*.md'))
    if not drafts:
        print("No drafts found.")
        return

    posts = []

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
        slug = slugify(title)

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

    # Build blog index
    index_html = build_index(posts)
    (BLOG_DIR / 'index.html').write_text(index_html)
    print(f"\nBlog index: {len(posts)} posts written to blog/index.html")


if __name__ == '__main__':
    main()
