#!/usr/bin/env python3
"""weekly_ctr_apply.py — apply approved CTR title/meta changes.

Reads /home/hermes/.hermes/data/weekly-ctr-state.json.
For each entry in approved[] (or pending with explicit --slugs), applies:

  tool pages: update tools/tools.json seo_title / seo_description, then rebuild tools
  blog pages: update content/drafts/<slug>.md or blog/<slug>/source frontmatter

Then:
  - rebuilds site (build_tools.py + build_blog.py; optional)
  - optionally deploys (deploy.sh) and git commits
  - requests indexing via gsc_inspect.py (if GSC SA key present)
  - moves entries approved -> deployed, records ctr_before snapshot, notes deploy date

Usage:
  python3 tools/weekly_ctr_apply.py --approve cordys-crm              # pending -> approved
  python3 tools/weekly_ctr_apply.py --approve-all                     # all pending -> approved
  python3 tools/weekly_ctr_apply.py --reject cordys-crm --reason "too long"
  python3 tools/weekly_ctr_apply.py --apply                           # apply all approved (no deploy)
  python3 tools/weekly_ctr_apply.py --apply --deploy                  # apply + build + deploy + git
  python3 tools/weekly_ctr_apply.py --status                          # print state summary

The Telegram approval flow is intentionally file-based: the weekly cron agent
writes pending entries; Tim replies "CTR approve <slug>" in Telegram; a small
Telegram handler (or manual CLI) flips pending->approved; next --apply consumes.
For now this is manual via CLI or via the Hermes agent interpreting Telegram replies.

State shape (weekly-ctr-state.json):
{
  "pending":   [{week, query, slug, page_type, page_url, old_title, new_title, old_meta, new_meta, new_h1?, impressions, ctr, position, cannibalization_note, created_at}],
  "approved": [{... same ...}],
  "deployed": [{... same ..., deployed_at, ctr_before: {impressions, ctr, position}}],
  "rejected": [{... same ..., rejected_at, reason}],
  "deltas":   [{week, slug, query, before: {...}, after: {...}, delta_ctr, delta_pos, measured_at}]
}
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
TOOLS_JSON = ROOT / "tools" / "tools.json"
STATE_FILE = Path("/home/hermes/.hermes/data/weekly-ctr-state.json")
DRAFTS_DIR = ROOT / "content" / "drafts"
BLOG_DIR = ROOT / "blog"

def load_state():
    if not STATE_FILE.exists():
        return {"pending": [], "approved": [], "deployed": [], "rejected": [], "deltas": []}
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception as e:
        print(f"ERROR reading state: {e}", file=sys.stderr)
        sys.exit(2)

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2) + "\n")
    tmp.rename(STATE_FILE)
    print(f"State written to {STATE_FILE}")

def find_entry(bucket, slug):
    state = load_state()
    for i, e in enumerate(state.get(bucket, [])):
        if e.get("slug") == slug:
            return i, e
    return None, None

def cmd_approve(slugs, approve_all=False):
    state = load_state()
    moved=[]
    if approve_all:
        for e in list(state.get("pending", [])):
            state["approved"].append(e)
            moved.append(e["slug"])
        state["pending"]=[]
        print(f"Approved all: {', '.join(moved) if moved else '(none pending)'}")
    else:
        for slug in slugs:
            idx, entry = None, None
            for i, e in enumerate(state.get("pending", [])):
                if e.get("slug")==slug:
                    idx, entry = i, e
                    break
            if entry is None:
                print(f"SKIP {slug}: not in pending (check state).", file=sys.stderr)
                continue
            state["pending"].pop(idx)
            state["approved"].append(entry)
            moved.append(slug)
            print(f"Approved {slug}")
    if moved:
        save_state(state)

def cmd_reject(slug, reason=""):
    state = load_state()
    idx, entry = None, None
    for i, e in enumerate(state.get("pending", [])):
        if e.get("slug")==slug:
            idx, entry = i, e
            break
    if entry is None:
        print(f"SKIP {slug}: not in pending", file=sys.stderr)
        return
    state["pending"].pop(idx)
    entry["rejected_at"]=datetime.now(timezone.utc).isoformat()
    entry["reason"]=reason
    state.setdefault("rejected", []).append(entry)
    save_state(state)
    print(f"Rejected {slug}: {reason}")

def validate_lengths(title, meta):
    errs=[]
    if title is not None and len(title)>60: errs.append(f"title {len(title)}ch>60")
    if meta is not None and len(meta)>155: errs.append(f"meta {len(meta)}ch>155")
    return errs

def apply_entry(entry, do_build=True):
    slug = entry["slug"]
    pt = entry.get("page_type", "tool")
    new_title = entry.get("new_title")
    new_meta = entry.get("new_meta")
    new_h1 = entry.get("new_h1")
    errs = validate_lengths(new_title, new_meta)
    if errs:
        print(f"  ✗ length check failed for {slug}: {', '.join(errs)} — SKIP", file=sys.stderr)
        return False
    if pt == "tool":
        tools = json.loads(TOOLS_JSON.read_text())
        found=False
        for t in tools:
            if t["slug"]==slug:
                found=True
                # keep old for audit
                entry["old_seo_title"]=t.get("seo_title")
                entry["old_seo_description"]=t.get("seo_description")
                if new_title: t["seo_title"]=new_title
                if new_meta: t["seo_description"]=new_meta
                # optional H1 is handled via name? For tools, H1 is the name; skip unless explicitly provided and different
                if new_h1 and new_h1 != t.get("name"):
                    print(f"  note: tool H1 tweak '{new_h1}' — tools use name as H1; updating name field too.", file=sys.stderr)
                    t["name"]=new_h1
                break
        if not found:
            print(f"  ✗ tool slug {slug} not found in tools.json", file=sys.stderr)
            return False
        TOOLS_JSON.write_text(json.dumps(tools, indent=2) + "\n")
        print(f"  ✓ tools.json updated for {slug}: title={new_title!r} ({len(new_title) if new_title else 0}ch), meta {len(new_meta) if new_meta else 0}ch")
        if new_h1:
            print(f"    H1: {new_h1!r}")
        return True
    else:
        # blog: try drafts first, fallback to a shadow frontmatter patch on the built dir is NOT the source — warn
        candidates = [
            DRAFTS_DIR / f"{slug}.md",
        ]
        # also check if draft exists with date prefix
        for p in DRAFTS_DIR.glob("*.md"):
            if p.stem == slug or p.stem.endswith(f"-{slug}") or slug in p.stem:
                if p not in candidates:
                    candidates.append(p)
        target=None
        for p in candidates:
            if p.exists():
                target=p; break
        if target is None:
            print(f"  ✗ blog draft not found for {slug} — checked: {', '.join(str(c) for c in candidates)}", file=sys.stderr)
            print(f"    Blog posts on martechsignal are published from content/drafts/*.md via build_blog.py.", file=sys.stderr)
            print(f"    If this post is already published (blog/{slug}/index.html exists) but has no draft, create content/drafts/{slug}.md first or edit the source draft.", file=sys.stderr)
            return False
        text = target.read_text()
        # parse frontmatter
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                raw, body = parts[1], parts[2]
                meta={}
                for line in raw.strip().splitlines():
                    m=re.match(r'(\w+):\s*(.+)', line)
                    if m: meta[m.group(1)]=m.group(2).strip().strip('"').strip("'")
                old_title = meta.get("title","")
                # replace title line
                if new_title:
                    if re.search(r'^title:\s*.*', raw, flags=re.MULTILINE):
                        raw = re.sub(r'^title:\s*.*', f'title: "{new_title}"', raw, flags=re.MULTILINE)
                    else:
                        raw = f'title: "{new_title}"\n' + raw
                    print(f"  ✓ {target.name}: title {old_title!r} -> {new_title!r}")
                # blog meta: we store proposed meta as frontmatter seo_description if present, else rely on build_blog excerpt
                # Introduce optional seo_description frontmatter field (build_blog.py should be patched to prefer it, but for now we just record it)
                if new_meta:
                    if "seo_description" in raw:
                        raw = re.sub(r'^seo_description:\s*.*', f'seo_description: "{new_meta}"', raw, flags=re.MULTILINE)
                    else:
                        raw += f'\nseo_description: "{new_meta}"'
                    print(f"  ✓ {target.name}: seo_description set ({len(new_meta)}ch)")
                target.write_text(f"---{raw}---{body}")
                entry["draft_path"]=str(target)
                return True
        print(f"  ✗ could not parse frontmatter for {target}", file=sys.stderr)
        return False

def cmd_apply(do_deploy=False, slugs=None):
    state = load_state()
    approved = state.get("approved", [])
    if not approved:
        print("Nothing approved — run --approve <slug> or --approve-all first.")
        return
    if slugs:
        approved = [e for e in approved if e["slug"] in set(slugs)]
        if not approved:
            print(f"No approved entries match slugs {slugs}", file=sys.stderr)
            return
    print(f"Applying {len(approved)} approved page(s)...")
    ok_slugs=[]
    failed=[]
    # cap guard: still enforce 5/week even at apply time
    week = datetime.now().strftime("%G-W%V")
    already_deployed_this_week = sum(1 for e in state.get("deployed", []) if e.get("week")==week)
    budget = 5 - already_deployed_this_week
    if len(approved) > budget:
        print(f"CAP: {already_deployed_this_week}/5 already deployed this week {week}; budget={budget} but {len(approved)} approved. Trimming to budget.", file=sys.stderr)
        approved = approved[:budget]
    for entry in list(approved):
        print(f"- {entry['slug']} ({entry.get('page_type')}) query='{entry.get('query')}'")
        if apply_entry(entry):
            ok_slugs.append(entry["slug"])
            # snapshot ctr_before if present
            entry["deployed_at"]=datetime.now(timezone.utc).isoformat()
            entry.setdefault("ctr_before", {"impressions": entry.get("impressions"), "ctr": entry.get("ctr"), "position": entry.get("position")})
            state.setdefault("deployed", []).append(entry)
        else:
            failed.append(entry["slug"])
    # remove applied from approved (only successes)
    state["approved"] = [e for e in state.get("approved", []) if e["slug"] not in set(ok_slugs)]
    save_state(state)
    if not ok_slugs:
        print("No pages applied (all failed).", file=sys.stderr)
        sys.exit(1)
    print(f"Applied: {', '.join(ok_slugs)}" + (f" | failed: {', '.join(failed)}" if failed else ""))

    # rebuild
    print("\n--- Rebuild ---")
    try:
        out = subprocess.run(["python3", str(ROOT / "tools" / "build_tools.py")], cwd=str(ROOT), capture_output=True, text=True, timeout=60)
        print(out.stdout[-2000:])
        if out.returncode!=0: print(out.stderr[-2000:], file=sys.stderr)
    except Exception as e:
        print(f"build_tools.py error: {e}", file=sys.stderr)
    # blog build if any blog entry was applied
    if any(s for s in ok_slugs if any(e.get("slug")==s and e.get("page_type")=="blog" for e in state.get("deployed", []))):
        try:
            out = subprocess.run(["python3", str(ROOT / "tools" / "build_blog.py")], cwd=str(ROOT), capture_output=True, text=True, timeout=60)
            print(out.stdout[-2000:])
            if out.returncode!=0: print(out.stderr[-2000:], file=sys.stderr)
        except Exception as e:
            print(f"build_blog.py error: {e}", file=sys.stderr)

    if do_deploy:
        print("\n--- Deploy (Cloudflare Pages + IndexNow + git) ---")
        env=dict(__import__("os").environ)
        # deploy.sh sources .env itself
        try:
            out = subprocess.run(["bash", str(ROOT / "deploy.sh")], cwd=str(ROOT), capture_output=True, text=True, timeout=300)
            print(out.stdout[-4000:])
            if out.returncode!=0:
                print(out.stderr[-4000:], file=sys.stderr)
                print("Deploy failed — deployed entries remain tracked but site not updated.", file=sys.stderr)
                sys.exit(out.returncode)
        except Exception as e:
            print(f"deploy error: {e}", file=sys.stderr)
            sys.exit(1)
        # GSC indexing (best-effort)
        gsc = ROOT / "gsc_inspect.py"
        if gsc.exists():
            urls=[f"https://martechsignal.com/{'tools' if e.get('page_type')=='tool' else 'blog'}/{e['slug']}/" for e in state.get("deployed", []) if e["slug"] in set(ok_slugs)]
            if urls:
                print(f"\n--- GSC Indexing ({len(urls)} URLs) ---")
                try:
                    out = subprocess.run(["python3", str(gsc)] + urls, cwd=str(ROOT), capture_output=True, text=True, timeout=120)
                    print(out.stdout[-3000:])
                    if out.returncode!=0: print(out.stderr[-2000:], file=sys.stderr)
                except Exception as e:
                    print(f"GSC inspect error (non-fatal): {e}", file=sys.stderr)
            else:
                print("No URLs for GSC inspection.")
    print("\nDone. Next Monday the loop will measure CTR deltas for these slugs.")

def cmd_status():
    state = load_state()
    import json as _j
    week = datetime.now().strftime("%G-W%V")
    used = sum(1 for b in ("pending","approved","deployed") for e in state.get(b,[]) if e.get("week")==week)
    print(f"Week {week}: {used}/5 used (pending+approved+deployed this week)")
    for bucket in ("pending","approved","deployed","rejected"):
        items=state.get(bucket, [])
        print(f"  {bucket}: {len(items)}")
        for e in items[-6:]:
            print(f"    - {e.get('week')} {e.get('slug')} ({e.get('page_type')}) q='{e.get('query')}' {len(e.get('new_title',''))}ch/{len(e.get('new_meta',''))}ch")
    if state.get("deltas"):
        print(f"  deltas: {len(state['deltas'])} measured")

def main():
    ap=argparse.ArgumentParser(description="Apply CTR loop approvals")
    ap.add_argument("--approve", nargs="+", help="move pending slug(s) -> approved")
    ap.add_argument("--approve-all", action="store_true")
    ap.add_argument("--reject", help="reject a pending slug")
    ap.add_argument("--reason", default="")
    ap.add_argument("--apply", action="store_true", help="apply approved -> deployed (and rebuild)")
    ap.add_argument("--deploy", action="store_true", help="with --apply, also run deploy.sh + GSC indexing")
    ap.add_argument("--slugs", nargs="*", help="limit --apply to these slugs")
    ap.add_argument("--status", action="store_true")
    args=ap.parse_args()

    if args.status:
        cmd_status(); return
    if args.approve or args.approve_all:
        cmd_approve(args.approve or [], approve_all=args.approve_all)
    if args.reject:
        cmd_reject(args.reject, reason=args.reason)
    if args.apply:
        cmd_apply(do_deploy=args.deploy, slugs=args.slugs)
    if not any([args.approve, args.approve_all, args.reject, args.apply, args.status]):
        ap.print_help()
        cmd_status()

if __name__=="__main__":
    main()
