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
