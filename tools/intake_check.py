#!/usr/bin/env python3
"""Intake gate — a tool record may not land in tools.json half-wired.

WHY THIS EXISTS (2026-10-23)
    tools.json is edited by hand at intake: tools/discover_tools.py and
    tools/discover_rising.py only ever write candidates.json. Nothing downstream
    re-derives the surfaces that are supposed to follow a record, so a record can
    be added while categories.json membership, the hub group split, the intro
    count and the currency field all stay as they were. mailcheap (2026-10-19)
    and sendportal (2026-10-15) landed exactly that way, and seven Build & Test
    cases went red days later — the failure surfaced in CI, not at intake.

    So: run this before you consider a record added. It fails loudly and
    non-zero. `--fix` repairs only the mechanical parts (category membership,
    tool_count); anything that needs an editorial decision (which hub group a
    tool belongs to, what currency a price is in, which star count a sentence
    means) is reported and left alone.

USAGE
    python3 tools/intake_check.py                  # check the whole directory
    python3 tools/intake_check.py --slug sendportal
    python3 tools/intake_check.py --fix            # mechanical repairs, then recheck

Exit codes: 0 clean, 1 problems found.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

# same shape r9/r15 use, so a literal that fools one cannot pass the other
APPROX = re.compile(r"(around|about|over|more than|nearly|roughly|approx|\+|-plus|\bplus\b|up to)\s*$", re.I)
EXACT_STARS = re.compile(r"\b(\d{1,3},\d{3})\b(?= (?:GitHub )?stars)")
ANY_STARS = re.compile(r"([\d,]+\.?\d*k?)\s*(?:GitHub\s+)?stars?\b|★\s*([\d,]+\.?\d*k?)\b")
COUNT_IN_COPY = re.compile(r"\b(\d+)\s+(systems|entries|tools)\b", re.I)


def load():
    tools = json.loads((TOOLS / "tools.json").read_text())
    doc = json.loads((TOOLS / "categories.json").read_text())
    cats = doc if isinstance(doc, list) else doc.get("categories", doc)
    return tools, cats, doc


def strings(obj, path="$"):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings(v, f"{path}[{i}]")


def members(cat, active):
    if cat["slug"] == "open-source":
        return sorted(t["slug"] for t in active if t.get("open_source"))
    return sorted(t["slug"] for t in active if t.get("category") == cat["slug"])


def check(fix=False, only_slug=None):
    tools, cats, doc = load()
    active = [t for t in tools if t.get("status", "active") == "active"]
    by_slug = {t["slug"]: t for t in tools if isinstance(t, dict)}
    problems, fixes, advisories = [], [], []

    # 1. a price with no currency cannot be rendered as money
    for t in tools:
        if not isinstance(t, dict):
            continue
        if t.get("price_from") is not None and not t.get("currency"):
            if only_slug and t["slug"] != only_slug:
                continue
            problems.append(
                f"{t['slug']}: price_from={t['price_from']} but currency is missing — "
                f"the page renders a bare symbol. Read the vendor pricing page and set USD/EUR/etc."
            )

    # 2/4/5. category membership, tool_count, intro counts
    for cat in cats:
        mem = members(cat, active)
        listed = cat.get("tools") or []
        missing = [s for s in mem if s not in listed]
        extra = [s for s in listed if s not in mem]
        if missing or extra:
            problems.append(
                f"categories.json/{cat['slug']}: membership out of sync — missing {missing or 'none'}, "
                f"unknown {extra or 'none'} (member count {len(mem)}, listed {len(listed)})"
            )
            if fix and not extra:
                cat["tools"] = sorted(set(listed) | set(missing))
                fixes.append(f"categories.json/{cat['slug']}: appended {missing} and re-sorted")
        if cat.get("tool_count") is not None and cat["tool_count"] != len(mem):
            problems.append(f"categories.json/{cat['slug']}: tool_count={cat['tool_count']} but {len(mem)} active tools")
            if fix:
                cat["tool_count"] = len(mem)
                fixes.append(f"categories.json/{cat['slug']}: tool_count -> {len(mem)}")

        hub = cat.get("hub") or {}
        for key in ("meta", "lead", "intro", "description"):
            raw = hub.get(key, cat.get(key))
            for txt in ([raw] if isinstance(raw, str) else raw or []):
                if not isinstance(txt, str) or "{n}" in txt:
                    continue
                for m in COUNT_IN_COPY.finditer(txt):
                    if int(m.group(1)) != len(mem):
                        problems.append(
                            f"categories.json/{cat['slug']}.{key}: copy says '{m.group(0)}' but there are "
                            f"{len(mem)} members — use the {{n}} token, the builders substitute it"
                        )

        # 3. every member should sit in a hub group. Advisory, not fatal: the
        # builder renders unplaced tools into a "More <category> tools" bucket
        # (build_tools.py:2576), so a gap is taxonomy debt, not lost content.
        groups = hub.get("groups") or []
        if groups:
            placed = [s for g in groups for s in g.get("slugs") or []]
            unplaced = [s for s in mem if s not in placed]
            dupes = sorted({s for s in placed if placed.count(s) > 1})
            if unplaced or dupes:
                advisories.append(
                    f"categories.json/{cat['slug']}.hub.groups: unplaced {unplaced or 'none'}, "
                    f"duplicated {dupes or 'none'} — they render under 'More <category> tools'; "
                    f"decide the group by hand when you touch that hub"
                )

    # 6. prose star literals must agree with the record they sit in
    for t in tools:
        if not isinstance(t, dict):
            continue
        if only_slug and t["slug"] != only_slug:
            continue
        stars = t.get("github_stars")
        for path, txt in strings(t):
            if "star" not in txt.lower():
                continue
            for m in EXACT_STARS.finditer(txt):
                if APPROX.search(txt[max(0, m.start() - 20):m.start()]):
                    continue
                if stars is None or m.group(1) != f"{stars:,}":
                    problems.append(
                        f"tools.json/{t['slug']}{path[1:]}: prose says {m.group(1)} stars, "
                        f"record says {stars} — write it drift-proof (no figure, or the {stars:,} value)"
                    )
            for m in ANY_STARS.finditer(txt):
                raw = (m.group(1) or m.group(2) or "").replace(",", "")
                if not raw:
                    continue
                try:
                    val = int(float(raw[:-1]) * 1000) if raw.lower().endswith("k") else int(float(raw))
                except ValueError:
                    continue
                if stars and abs(val - stars) > max(2, stars * 0.02):
                    problems.append(
                        f"tools.json/{t['slug']}{path[1:]}: '{m.group(0).strip()}' is not this record's "
                        f"{stars} stars — a cross-tool star claim resolves against the owning record in CI"
                    )

    if fix and fixes:
        if isinstance(doc, list):
            (TOOLS / "categories.json").write_text(json.dumps(cats, indent=1, ensure_ascii=False) + "\n")
        else:
            (TOOLS / "categories.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")

    return problems, fixes, advisories, by_slug


def main(argv):
    fix = "--fix" in argv
    only = None
    if "--slug" in argv:
        only = argv[argv.index("--slug") + 1]
    problems, fixes, advisories, by_slug = check(fix=fix, only_slug=only)
    for f in fixes:
        print(f"FIXED  {f}")
    if fixes and fix:
        # the report above was computed before the repair — re-read the tree
        problems, _, advisories, by_slug = check(fix=False, only_slug=only)
    for a in advisories:
        print(f"WARN   {a}")
    if problems:
        print(f"INTAKE GATE: {len(problems)} problem(s)\n")
        for p in problems:
            print(f"  FAIL  {p}")
        print("\nFix these before the record ships. `--fix` handles membership and tool_count only.")
        return 1
    print(f"INTAKE GATE: clean ({len(by_slug)} records, {len(problems)} problems)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
