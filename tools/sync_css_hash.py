#!/usr/bin/env python3
"""R2 M-9 (2026-09-08): sync the CSS cache-bust hash across every HTML file, including
the 6 hand-authored pages that the builders never regenerate. Hash = md5(style.css)[:8].
Run after build, before deploy. Idempotent; rewrites only files whose ref is stale."""
import hashlib
import re
from pathlib import Path

ROOT = Path("/mnt/user/dev/martechsignal")
css = (ROOT / "style.css").read_bytes()
want = hashlib.md5(css).hexdigest()[:8]
pat = re.compile(rb"/style(?:\.min)?\.css\?v=[a-f0-9]{8}")
fixed = 0
for f in ROOT.rglob("index.html"):
    if "node_modules" in f.parts:
        continue
    b = f.read_bytes()
    new = pat.sub(f"/style.css?v={want}".encode(), b)
    if new != b:
        f.write_bytes(new)
        fixed += 1
# 404.html too
f404 = ROOT / "404.html"
if f404.exists():
    b = f404.read_bytes()
    new = pat.sub(f"/style.css?v={want}".encode(), b)
    if new != b:
        f404.write_bytes(new)
        fixed += 1
print(f"css-hash sync: want {want}, fixed {fixed} files")

# M25 (2026-09-28): one consistent outbound-link policy. Every external <a> that
# carries no rel gets rel="nofollow" (vendors we score must not receive editorial
# link equity; the previous 4-of-53 mix was inconsistent). Internal links skipped.
tag_pat = re.compile(rb"<a\s[^>]*>")
ext_pat = re.compile(rb'href="https?://(?!www\.?martechsignal\.com)')
nf_fixed = 0
for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
    if "node_modules" in f.parts or not f.exists():
        continue
    b = f.read_bytes()
    def _add_nf(m):
        global nf_fixed
        tag = m.group(0)
        if not ext_pat.search(tag):
            return tag
        rel_m = re.search(rb'rel="([^"]*)"', tag)
        if rel_m:
            rels = rel_m.group(1).split()
            if b"nofollow" in rels:
                return tag
            rels.append(b"nofollow")
            tag = tag[:rel_m.start(1)] + b" ".join(rels) + tag[rel_m.end(1):]
        else:
            tag = tag[:2] + b' rel="nofollow"' + tag[2:]
        nf_fixed += 1
        return tag
    new = tag_pat.sub(_add_nf, b)
    if new != b:
        f.write_bytes(new)
print(f"nofollow sweep: {nf_fixed} external links marked")

# M29 (2026-09-28): primary-nav parity. Generated pages get CATEGORIES and
# GLOSSARY from page_shell; the hand-authored pages are normalized here so the
# primary nav matches everywhere (the audit found them footer-only).
nav_pat = re.compile(rb'(<nav class="mast-nav"[^>]*>)(.*?)(</nav>)', re.S)
nav_fixed = 0

def _fix_nav(m):
    global nav_fixed
    inner = m.group(2)
    if b'href="/categories/"' in inner:
        return m.group(0)
    anchor = b'<a href="/alternatives/">ALTERNATIVES</a>'
    if anchor not in inner:
        return m.group(0)
    inner = inner.replace(
        anchor, anchor + b'<a href="/categories/">CATEGORIES</a><a href="/glossary/">GLOSSARY</a>', 1)
    nav_fixed += 1
    return m.group(1) + inner + m.group(3)

for f in list(ROOT.rglob("index.html")) + [ROOT / "404.html"]:
    if "node_modules" in f.parts or not f.exists():
        continue
    b = f.read_bytes()
    new = nav_pat.sub(_fix_nav, b)
    if new != b:
        f.write_bytes(new)
print(f"nav sweep: {nav_fixed} primary navs updated")

