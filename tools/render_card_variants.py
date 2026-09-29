"""r11 L-7/L-8 (2026-09-29): the fact-card renditions were generated once via
ad-hoc uv scripts; the webp variants 670w and the srcset wiring now get a
durable home here. Adds a 480w step too (335px slot at DPR 1.4-1.5), which
the audit measured as the actual served size on mobile. Idempotent."""
import glob
import os

from PIL import Image

ROOT = "/mnt/user/dev/martechsignal"

made670 = made480 = skipped = 0
for png in glob.glob(os.path.join(ROOT, "og", "tools", "*.png")):
    stem = png[:-4]
    for w, tag in ((670, "670"), (480, "480")):
        out = f"{stem}-{tag}.webp"
        if os.path.exists(out):
            skipped += 1
            continue
        im = Image.open(png)
        h = round(im.size[1] * w / im.size[0])
        im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=82)
        if tag == "670":
            made670 += 1
        else:
            made480 += 1

print(f"made 670w: {made670}, made 480w: {made480}, already present: {skipped}")
