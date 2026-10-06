"""r11 L-7/L-8 (2026-09-29): the fact-card renditions were generated once via
ad-hoc uv scripts; the webp variants 670w and the srcset wiring now get a
durable home here. Adds a 480w step too (335px slot at DPR 1.4-1.5), which
the audit measured as the actual served size on mobile. Idempotent.

r34 M-13 (2026-10-06): the webp layer shipped a stale vintage of the PNG
masters (sendgrid "Free tier", chatfuel $39, trakkr unit-stripped) because
this script never re-rendered an existing file. --force re-renders every
rung from the current masters; --only limits to comma-separated slugs.
The 1200w rung (previously ad-hoc) gets its durable home here too.
"""
import argparse
import glob
import os

from PIL import Image

ROOT = "/mnt/user/dev/martechsignal"
RUNGS = ((1200, "1200"), (670, "670"), (480, "480"))

ap = argparse.ArgumentParser()
ap.add_argument("--force", action="store_true",
                help="re-render even when the webp already exists")
ap.add_argument("--only", default="",
                help="comma-separated slugs to re-render (default: all)")
args = ap.parse_args()
only = {s.strip() for s in args.only.split(",") if s.strip()}

made = skipped = 0
for png in sorted(glob.glob(os.path.join(ROOT, "og", "tools", "*.png"))):
    if only and os.path.basename(png)[:-4] not in only:
        continue
    stem = png[:-4]
    for w, tag in RUNGS:
        out = f"{stem}-{tag}.webp"
        if os.path.exists(out) and not args.force:
            skipped += 1
            continue
        im = Image.open(png)
        h = round(im.size[1] * w / im.size[0])
        im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=82)
        made += 1

print(f"made: {made}, already present: {skipped}")
