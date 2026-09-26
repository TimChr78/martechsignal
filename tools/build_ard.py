#!/usr/bin/env python3
"""A-3 (v2.4.0 audit): build the ARD manifest (Agentic Resource Discovery, spec 1.0).

Emits /.well-known/ard.json (canonical) and /.well-known/ai-catalog.json
(predecessor name, kept as a courtesy copy per spec §5.1).

Entry shape (spec §4.2): identifier (urn:air:<publisher>:<namespace>:<name>,
Appendix C), displayName, type (IANA media type), exactly one of url/data,
SHOULD carry 2-5 representativeQueries.

Validate before deploying (audit: a schema-ERRORING catalog flips Lighthouse's
ard-schema audit from N/A into a counted failure):
    uv run --with jsonschema python tools/build_ard.py --validate
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
CATS_JSON = ROOT / "tools" / "categories.json"
OUT_DIR = ROOT / ".well-known"
PUBLISHER = "martechsignal.com"


def tool_queries(t):
    """2-5 queries this page genuinely answers (spec: the discovery signal)."""
    name = t["name"]
    q = [f"{name} pricing", f"{name} alternatives"]
    if t.get("open_source"):
        q.insert(0, f"open source {name.lower()}")
    if t.get("category"):
        q.append(f"{t['category'].replace('-', ' ')} tools like {name}")
    return q[:5]


def cat_queries(c):
    n = c["name"].lower()
    return [f"best {n} tools", f"{n} comparison", f"{n} software"]


def build():
    tools = [t for t in json.loads(TOOLS_JSON.read_text())
             if t.get("status", "active") == "active"]
    cats = json.loads(CATS_JSON.read_text())
    entries = []
    for t in sorted(tools, key=lambda x: x["slug"]):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:tools:{t['slug']}",
            "displayName": f"{t['name']} pricing & plans",
            "type": "text/html",
            "url": f"https://martechsignal.com/tools/{t['slug']}/",
            "description": (t.get("tagline") or "")[:200],
            "representativeQueries": tool_queries(t),
        })
    for c in sorted(cats, key=lambda x: x["slug"]):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:categories:{c['slug']}",
            "displayName": c["name"],
            "type": "text/html",
            "url": f"https://martechsignal.com/categories/{c['slug']}/",
            "description": (c.get("description") or "")[:200],
            "representativeQueries": cat_queries(c),
        })
    # Machine-readable data sources (url reference, value-or-reference §4.3).
    # Served as root catalog-*.json (llms-full.txt siblings): /data/ is correctly
    # closed by .assetsignore (pipeline state), so manifest urls must not point there.
    for fname in ("tools.json", "categories.json"):
        entries.append({
            "identifier": f"urn:air:{PUBLISHER}:data:{fname.replace('.', '-')}",
            "displayName": f"MartechSignal {fname} (machine-readable)",
            "type": "application/json",
            "url": f"https://martechsignal.com/catalog-{fname}",
            "representativeQueries": ["martechsignal tool catalog data",
                                      "ai marketing tools dataset"],
        })
    manifest = {
        "specVersion": "1.0",
        "publisher": f"https://{PUBLISHER}/",
        "entries": entries,
        "trustManifest": {"identity": f"https://{PUBLISHER}/about/"},
    }
    return manifest


def validate(manifest):
    """Validate against the authoritative schema (ard-entry.schema.json)."""
    import urllib.request
    schema_url = ("https://raw.githubusercontent.com/ards-project/ard-spec/main/"
                  "spec/schemas/ard-entry.schema.json")
    schema = json.loads(urllib.request.urlopen(schema_url, timeout=30).read())
    from jsonschema import Draft202012Validator
    v = Draft202012Validator(schema)
    errs = sorted(v.iter_errors(manifest), key=lambda e: e.path)
    # The schema defines ArdEntry/ArdManifest as $defs; validate via the manifest def
    defs = schema.get("$defs") or schema.get("definitions") or {}
    target = None
    for name in ("ArdManifest", "ardManifest", "ArdEntry"):
        if name in defs:
            target = {**schema, "$ref": f"#/$defs/{name}" if "$defs" in schema else f"#/definitions/{name}"}
            break
    if target:
        errs = sorted(Draft202012Validator(target).iter_errors(manifest),
                      key=lambda e: list(e.absolute_path))
    if errs:
        for e in errs[:10]:
            print("SCHEMA ERROR:", list(e.absolute_path), e.message[:160])
        return False
    # Discovery constraints (§D.2): URN format + query sizing (warnings only)
    warn = 0
    for e in manifest["entries"]:
        ident = e["identifier"]
        parts = ident.split(":")
        if not (ident.startswith("urn:air:") and len(parts) >= 5):
            print("WARN urn format:", ident); warn += 1
        rq = e.get("representativeQueries", [])
        if not 2 <= len(rq) <= 5:
            print("WARN queries count:", ident, len(rq)); warn += 1
        if ("url" in e) == ("data" in e):
            print("WARN value-or-reference:", ident); warn += 1
    print(f"VALID: {len(manifest['entries'])} entries, {warn} warnings")
    return True


if __name__ == "__main__":
    m = build()
    if "--validate" in sys.argv:
        if not validate(m):
            sys.exit(1)
    OUT_DIR.mkdir(exist_ok=True)
    text = json.dumps(m, ensure_ascii=False, indent=1)
    (OUT_DIR / "ard.json").write_text(text)
    (OUT_DIR / "ai-catalog.json").write_text(text)  # predecessor courtesy copy
    # the two data-entry urls must resolve (root copies; /data/ stays private)
    (ROOT / "catalog-tools.json").write_text(TOOLS_JSON.read_text())
    (ROOT / "catalog-categories.json").write_text(CATS_JSON.read_text())
    print(f"ard.json + ai-catalog.json written ({len(m['entries'])} entries, {len(text)} bytes)")
