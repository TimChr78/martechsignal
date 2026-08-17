# Weekly CTR Optimisation Loop — martechsignal.com

**Board:** `seo` · **Task:** `t_cbb75200` (P7) · **Blocked on:** `t_a82d5503` diagnostic (now unblocked 2026-08-17)
**Cadence:** Every Monday 09:15 — after GSC report (Mon 08:00, `b6xsdR4vhiztABT0`) and cannibalization monitor (Mon 08:30, `Sxkkb3p3fQiaoXA5`)
**Cap:** 5 pages/week (hard). One variant per query per week. Prefer blog posts over tool pages.

## Why

Impressions without clicks is fixable without new content — title + meta are the lever. `t_759372a2` (indexing, sitemap) is done; SERP presentation isn't optimised. This is the CTR complement to the gap analysis pipeline.

As of 2026-08-17 GSC snapshot (28d):
- 379 queries, 1427 impressions, **0 clicks** — CTR problem is across the board.
- Only one "opportunity" meets `impr≥20 & CTR<3% & pos<20`: `cordys crm` (27 impr, pos 7.3).
- Most impressions sit at pos 50–99 (not yet competitive) — CTR fixes apply once pages enter pos <20. The loop still runs to build the habit and catch early movers.

## Architecture

```
Mon 08:00  n8n: SEO GSC Weekly Keyword Report (b6xsdR4vhiztABT0)   — writes /mnt/cache/appdata/n8n/data/reports/gsc-keywords-YYYY-MM-DD.md
Mon 08:30  n8n: SEO Keyword Cannibalization Monitor (Sxkkb3p3fQiaoXA5) — Telegram report, LLM clusters
Mon 09:15  Hermes cron: Weekly CTR Loop (this task)                — collects context, agent drafts diffs, Telegram approval
  Human: Telegram thumbs up/down per page (reply "CTR approve <slug>")
  On approval: weekly_ctr_apply.py rebuilds → deploys → GSC URL Inspection
Mon+7d     Next Mon's run diffs GSC deltas for last week's URLs and posts CTR before/after
```

Choose Hermes cron over pure n8n for this loop: n8n does the data plumbing well, but title/meta drafting wants a full Hermes agent (web_search, file edits, build+deploy) and a single approval surface (Telegram) that Tim already uses.

## Files

| Path | Purpose |
|---|---|
| `/home/hermes/.hermes/scripts/weekly-ctr-loop.sh` | Cron `script` — context collector, prints state + GSC report + inventory into the agent prompt |
| `/mnt/user/dev/martechsignal/tools/weekly_ctr_check.py` | Validator: `--query`, `--title/--meta` lengths, `--cap-check`, `--list-inventory` |
| `/mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py` | Approval state machine: `--approve/--approve-all/--reject/--apply/--deploy` |
| `/home/hermes/.hermes/data/weekly-ctr-state.json` | Approvals state (pending/approved/deployed/rejected/deltas). ISO-week scoped cap. |
| `/mnt/user/dev/martechsignal/docs/weekly-ctr-loop.md` | This doc |
| `/mnt/user/dev/martechsignal/tools/build_tools.py` | Tool page builder (helpers `_seo_title_for`, `_seo_description_for` enforce ≤60/≤155) |
| `/mnt/user/dev/martechsignal/tools/build_blog.py` | Blog builder (title → `— Martech Signal`, excerpt → `meta description`) |
| `/mnt/user/dev/martechsignal/deploy.sh` | Cloudflare Pages + IndexNow + git push |

## Cron job

Managed in `/home/hermes/.hermes/cron/jobs.json`. Create/update via Hermes CLI or DB.

Required shape:
- `id`: `weekly-ctr-loop` (or auto)
- `name`: `Weekly CTR Optimisation Loop`
- `schedule`: `15 9 * * 1` (Mon 09:15 Europe/Copenhagen — cron is UTC on the host, so use UTC-adjusted time; see other Monday jobs for convention)
- `script`: `weekly-ctr-loop.sh`
- `no_agent`: `false` — agent must run to draft titles/metas
- `enabled_toolsets`: `["terminal","file","web"]` (needs reads, writes, and web_search for title research)
- `deliver`: `telegram:8327252566` (DM)
- `prompt`: see § Agent prompt below

Existing Monday timings for reference: GSC 08:00, cannibal 08:30, Tool Discovery 06:00, Competitor 06:30, Blog Topic Scanner Sun 16:00.

## Agent prompt (paste into jobs.json)

```
You are the Weekly CTR optimisation loop for martechsignal.com (Mon 09:15).

The shell script output above is your context. It contains:
- Cap status (5/week, ISO week)
- The latest GSC report (top 10 opportunities: impr≥20 & CTR<3% & pos<20; winners; rising)
- Cannibalization state + page inventory
- SEO constraints (≤60ch title, ≤155ch meta, no hype, dark-theme/Archivo voice)
- Pending approvals awaiting Telegram thumbs up

Do this, in order:

1. GUARD: If CAP_REACHED is printed or remaining budget is 0, send a one-line Telegram notice and STOP — do not draft.
   If GSC report is MISSING, report that and stop.

2. DELTA: If deployed entries exist from last week (state file), re-query GSC for those queries (or re-read the latest report) and post a compact before→after CTR delta table for each (query, page, old pos/CTR, new pos/CTR). Append deltas to state file's deltas[].

3. PICK: From the GSC opportunities bucket, pick up to REMAINING_BUDGET pages (max 5/week, fewer if fewer opportunities exist):
   - Sort by impressions descending.
   - Prefer blog posts over tool pages (blog titles are easier to make click-worthy without keyword-stuffing).
   - Skip any page from earlier weeks that is still pending approval.
   - For each candidate, run: python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --query "<query>"
     If result is HIGH cannibalization risk, SKIP that candidate and take the next.
     If no opportunities meet impr≥20, fall back to the top-impressions queries from "All Queries" (still check pos<20 where possible; otherwise take pos 50+ as future pipeline input).

4. DRAFT: For each picked page (≤5):
   - Resolve the query → page slug via tools.json/blog inventory (or grep).
   - Read the current <title> and meta description from the built HTML (or source).
   - Draft: new <title> (≤60ch, one clear argument/question, not listicle), new meta (≤155ch, outcome + specificity), optional H1 tweak.
     Tool pages: meta must end with "Compare AI features, integrations & top alternatives."
     Blog posts: outcome + specificity, no generic filler.
   - Keep dark-theme/Archivo voice; no hype.
   - Validate: python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --title "<t>" --meta "<m>"
     If OVER, shorten — do not ship a truncated title/meta.
   - Also call the helpers in build_tools.py as a cross-check for tool pages.

5. POST FOR APPROVAL: Write each draft to the state file's pending[] via a python heredoc (read state, append entry, write back — never hand-edit JSON with echo). Entry shape:
   {week, query, slug, page_type: "tool"|"blog", page_url, old_title, new_title, old_meta, new_meta, new_h1?, impressions, ctr, position, cannibalization_note, created_at}
   Then post a Telegram message with a per-page diff:
     **Page 1/3 — cordys crm → /tools/cordys-crm/ — 27 impr, 0% CTR, pos 7.3**
     Old title (47ch): "..."
     New title (53ch): "..."
     Old meta (143ch): "..."
     New meta (132ch): "..."
     Cannibal: low — 1 page overlaps, single owner — safe.
     Reply `CTR approve cordys-crm` to ship, `CTR reject cordys-crm — reason` to skip.
   Use Telegram markdown. After posting, STOP — do not auto-apply. Await Tim.

6. APPROVAL (separate trigger):
   When Tim replies "CTR approve <slug>" (handled by the next run or a manual apply), run:
     python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --approve <slug> --apply --deploy
   This edits tools.json/content/drafts/*.md, rebuilds tools+blog, runs deploy.sh, git commit/pushes, and requests GSC indexing for the 5 URLs. On success, the entry moves pending→deployed with ctr_before snapshotted.

7. If fewer than 5 opportunities exist this week, say so explicitly and only draft what exists (1–2 is fine). Do not invent candidates.

8. Guardrails: one variant per query per week; no cannibalization — check weekly_ctr_check.py before every draft; cap at 5/week so you can attribute changes.

Keep the whole weekly post under 80 lines. No pipe tables — use bullet lists.
```

## Manual operator commands

```bash
# Check cap + state
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --cap-check
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --status

# Cannibal + length checks
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --query "claude seo"
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --title "New Title" --meta "New meta..."

# Approval flow (normally triggered by Telegram reply, but operable via CLI)
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --approve cordys-crm
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --approve-all
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --reject cordys-crm --reason "too long, needs shorten"
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --apply            # rebuild only
python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --apply --deploy   # rebuild + deploy + GSC inspect

# Full cron dry-run (no agent)
bash /home/hermes/.hermes/scripts/weekly-ctr-loop.sh | head -300
```

## Verification

- `bash /home/hermes/.hermes/scripts/weekly-ctr-loop.sh` exits 0 and prints cap + GSC + inventory blocks.
- `python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --cap-check` shows remaining budget for ISO week.
- `python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_check.py --query "claude seo"` correctly flags HIGH (multiple overlapping tool pages) while `--query "cordys crm"` is LOW (single owner).
- `python3 /mnt/user/dev/martechsignal/tools/weekly_ctr_apply.py --status` shows pending/approved/deployed counts.
- Title ≤60, meta ≤155 enforced; violations cause distinct exit codes (2 for length, 1 for cap/cannibal).

## Ready for recurring runs

- n8n GSC report (b6xsdR4vhiztABT0) is INACTIVE per backup; re-activation requires Google OAuth2 credential (GOOGLE_CRED_ID). Local fallback reads `/mnt/cache/appdata/n8n/data/reports/gsc-keywords-*.md` which currently has a 2026-08-17 snapshot. The cron collector tolerates missing reports (prints MISSING and instructs agent to stop gracefully).
- Cannibalization monitor (Sxkkb3p3fQiaoXA5) is ACTIVE (Mon 08:30) and provides the weekly Telegram cluster digest; the local `weekly_ctr_check.py` heuristic is the pre-draft gate aligned with it.
- The weekly-ctr-loop.sh cron must be installed at Mon 09:15 to complete the chain. Until installed, runs are manual via the script + agent interpretation.

## Done when

Loop runs 2 consecutive weeks with measured CTR deltas posted; backlog handled via Kanban queue. After 2 weeks, archive `t_cbb75200` or convert to ongoing ops.
