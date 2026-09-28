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
pat = re.compile(rb"/style\.css\?v=[a-f0-9]{8}")
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

