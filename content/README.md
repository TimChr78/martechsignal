# content/

Two folders, and the difference matters:

- **`drafts/` is AUTO-PUBLISH.** `tools/build_blog.py` turns every `.md` in this
  folder into a live page at `/blog/<slug>/`, and `deploy.sh` rebuilds and
  publishes the whole tree (it also runs `git add -A`). Dropping a file here is
  publishing it on the next deploy. There is deliberately no code gate - the rule
  is that only posts Tim has approved, from a one-shot cron he armed, may sit in
  this folder.
- **`pending-approval/` is never published.** Nothing reads this folder; it is
  where unapproved or parked drafts live.

Before any deploy, check that every file in `drafts/` belongs to a live post:

    python3 - <<'EOF'
    import pathlib, re
    d = pathlib.Path("content/drafts"); blog = pathlib.Path("blog")
    for f in sorted(d.glob("*.md")):
        base = re.sub(r"-\d{4}-\d{2}-\d{2}$", "", f.stem)
        if not (blog / base / "index.html").exists():
            print("WOULD PUBLISH:", f.name)
    EOF

A file listed as `WOULD PUBLISH` is about to go live without approval.

_Added 2026-09-13 after three unapproved posts (claude-seo-vs-*) were published by
a deploy that rebuilt everything sitting in `drafts/`._
