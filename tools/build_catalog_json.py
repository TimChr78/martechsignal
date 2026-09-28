#!/usr/bin/env python3
"""r7 M11 (2026-09-28): publish the /categories.json catalog entry the ARD
advertises. Generated from tools/categories.json + tools/tools.json so counts
stay live. Also drops the retired 'open-source' pseudo-category (M10)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
cats = json.load(open(ROOT / "tools" / "categories.json"))
entries = cats if isinstance(cats, list) else cats.get("categories", [])
tools = json.load(open(ROOT / "tools" / "tools.json"))
active = [t for t in tools if t.get("status", "active") == "active"]
out = []
for c in entries:
    slug = c.get("slug")
    if not slug:
        continue
    if c.get("cross_cutting"):
        # r8 H2/H5 (2026-09-28): the open-source facet is a cross-cutting
        # landing page over every category; it counts licences, not members.
        n = sum(1 for t in active if t.get("open_source"))
    else:
        n = sum(1 for t in active if t.get("category") == slug)
    out.append({
        "slug": slug,
        "name": c.get("name", slug),
        "url": f"https://martechsignal.com/categories/{slug}/",
        "description": c.get("meta") or c.get("description") or "",
        "tool_count": n,
        **({"cross_cutting": True} if c.get("cross_cutting") else {}),
    })
(ROOT / "categories.json").write_text(
    json.dumps({"categories": out, "generated_from": "tools/categories.json"},
               indent=2, ensure_ascii=False))
print(f"categories.json: {len(out)} categories published")
