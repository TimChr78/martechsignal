#!/usr/bin/env bash
set -euo pipefail

# Deploy martechsignal.com to Cloudflare Pages via wrangler.
# Requires: CLOUDFLARE_API_KEY (Pages:Edit) and CLOUDFLARE_ACCOUNT_ID env vars.
#
# Usage:
#   ./deploy.sh              sync + build + deploy to Cloudflare + verify live + git push
#   ./deploy.sh --no-build   skip the build step (upload current files as-is)
#   ./deploy.sh --no-git     skip the final git commit/push step
#   ./deploy.sh --offline    skip the pre-deploy sync with origin/main (emergencies only)
#
# The pre-deploy sync exists because changes now arrive as merged pull requests on
# GitHub as well as from this pipeline (e.g. PR #2, the newsletter moving off Kit).
# Building from a checkout that is behind origin/main republishes the OLD site and
# then fails its push, so the tree is fast-forwarded/rebased BEFORE anything is
# built, and a tree that is still behind origin/main is never deployed.
#
# The build step regenerates blog posts, tool/category pages, sitemap, and the
# homepage latest-signals block from source (content/drafts/*.md, tools.json).
# It runs BEFORE upload so the live site always reflects current source — this
# closes the "deployed stale HTML" footgun where edits to a draft never reached
# the site because deploy.sh used to only upload pre-built files.
#
# Only the staged public subset is uploaded (deploy-out/, built by
# tools/stage_deploy.py). The repo itself is NOT the publish root any more.

# ── Flags ──────────────────────────────────────────────────────────
DO_GIT=1
DO_BUILD=1
DO_SYNC=1
VERIFY_FAILED=0
PUSH_FAILED=0
for arg in "$@"; do
    case "$arg" in
        --no-git)   DO_GIT=0 ;;
        --no-build) DO_BUILD=0 ;;
        --offline)  DO_SYNC=0 ;;
    esac
done

# Source secrets for cron runs (turn off -u, .env references $1 etc.)
set +u
set -a
source /home/hermes/.hermes/.env 2>/dev/null || true
set +a
set -u

PROJECT="martechsignal"
ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:?CLOUDFLARE_ACCOUNT_ID not set}"

if [ -z "${CLOUDFLARE_API_KEY:-}" ]; then
    echo "ERROR: CLOUDFLARE_API_KEY not set" >&2
    exit 1
fi

cd "$(dirname "$0")"

# ── Failure channel ────────────────────────────────────────────────
# A deploy that silently diverges is worse than a deploy that stops. Every fatal
# path below messages Tim on Telegram before exiting; `hermes send` needs no
# running gateway for bot-token platforms, and the raw Bot API is the fallback.
notify_tim() {
    local msg="$1"
    if /opt/hermes/bin/hermes send -t telegram "$msg" >/dev/null 2>&1; then
        echo "  → messaged Tim on Telegram"
        return 0
    fi
    if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_HOME_CHANNEL:-}" ]; then
        if curl -sS -m 20 -X POST \
            "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
            -d "chat_id=${TELEGRAM_HOME_CHANNEL}" --data-urlencode "text=${msg}" >/dev/null 2>&1; then
            echo "  → messaged Tim on Telegram (Bot API fallback)"
            return 0
        fi
    fi
    echo "  ⚠ could not reach Telegram — this failure is only in this log" >&2
    return 1
}

# ── One git user only ──────────────────────────────────────────────
# The checkout must be owned by whoever runs git here. A git command run as a
# second user half-updates .git (mixed-object ownership, stale index locks) and
# the next job sees a repo that disagrees with itself.
GIT_USER="$(whoami)"
REPO_OWNER="$(stat -c '%U' .)"
if [ "$REPO_OWNER" != "$GIT_USER" ]; then
    echo "⛔ repo is owned by '$REPO_OWNER' but git is running as '$GIT_USER'" >&2
    notify_tim "⛔ martechsignal deploy aborted: /mnt/user/dev/martechsignal is owned by '$REPO_OWNER' but deploy.sh ran as '$GIT_USER'. Nothing built, nothing deployed. Run git as one user."
    exit 1
fi
MIXED="$(find .git/objects -maxdepth 3 ! -user "$GIT_USER" 2>/dev/null | head -3)"
if [ -n "$MIXED" ]; then
    echo "⚠ .git holds object files owned by another user (read-only packfiles are harmless):" >&2
    echo "$MIXED" | sed 's/^/    /' >&2
fi
# Anything git must WRITE (refs, reflog, index) has to belong to the user running
# this script, or the commit dies with "unable to append to '.git/logs/HEAD'".
# That failure lands after the upload, which is exactly how GitHub and the live
# site diverge. Stop before the build instead.
FOREIGN_WRITABLE="$(find .git/refs .git/logs .git/index -maxdepth 4 ! -user "$GIT_USER" 2>/dev/null | head -5)"
if [ -n "$FOREIGN_WRITABLE" ]; then
    echo "⛔ git cannot write its own refs as '$GIT_USER' — the repo would publish but never push:" >&2
    echo "$FOREIGN_WRITABLE" | sed 's/^/    /' >&2
    echo "   fix: chown -R $(id -u):$(id -g) .git   (as root, e.g. docker exec -u 0 $(hostname) chown -R $(id -u):$(id -g) $(pwd)/.git)" >&2
    notify_tim "⛔ martechsignal deploy aborted before build: .git refs are owned by another user, so git cannot commit or push as '$GIT_USER'. Nothing deployed. Fix: chown -R $(id -u):$(id -g) .git"
    exit 1
fi

# ── Sync with origin/main BEFORE building ──────────────────────────
# This pipeline is no longer the only writer: feature work lands as merged pull
# requests on GitHub. Building from a stale checkout republishes the old site and
# makes the closing push fail, so sync first and refuse to deploy a tree that is
# behind origin/main.
if [ "$DO_SYNC" -eq 1 ]; then
    echo "── Sync with origin/main ───────────────────────────────"
    if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        echo "⛔ not a git repository — cannot sync (use --offline to deploy anyway)" >&2
        notify_tim "⛔ martechsignal deploy aborted: checkout is not a git repo, so it could not be synced with origin/main."
        exit 1
    fi
    # Pipeline state (tools/candidates.json, tools/github-history.json, rebuilt
    # pages) must be committed before any history rewrite, or the rebase refuses.
    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "data: pipeline state before deploy" >/dev/null
        echo "  committed pending pipeline state"
    else
        echo "  working tree clean"
    fi
    if ! git fetch origin --quiet 2>/tmp/deploy-fetch.err; then
        echo "⛔ git fetch failed — cannot prove the tree is current" >&2
        sed 's/^/    /' /tmp/deploy-fetch.err >&2
        notify_tim "⛔ martechsignal deploy aborted: git fetch origin failed, so I cannot prove the checkout is current. Nothing built, nothing deployed. (For an emergency, ./deploy.sh --offline.)"
        exit 1
    fi
    AHEAD="$(git rev-list --count origin/main..HEAD)"
    BEHIND="$(git rev-list --count HEAD..origin/main)"
    echo "  ahead of origin/main: $AHEAD   behind: $BEHIND"
    if [ "$BEHIND" -gt 0 ]; then
        if [ "$AHEAD" -gt 0 ]; then
            echo "  rebasing local commits onto origin/main"
            if ! git rebase origin/main >/tmp/deploy-rebase.log 2>&1; then
                CONFLICTS="$(git diff --name-only --diff-filter=U | tr '\n' ' ')"
                git rebase --abort >/dev/null 2>&1 || true
                echo "⛔ rebase conflict — aborted, nothing deployed" >&2
                echo "  conflicting files: ${CONFLICTS:-see /tmp/deploy-rebase.log}" >&2
                notify_tim "⛔ martechsignal deploy aborted: rebase onto origin/main conflicted, so nothing was built or deployed. Conflicting files: ${CONFLICTS:-see /tmp/deploy-rebase.log}"
                exit 1
            fi
        else
            echo "  fast-forwarding to origin/main"
            if ! git merge --ff-only origin/main >/dev/null 2>&1; then
                echo "⛔ fast-forward failed — aborted, nothing deployed" >&2
                notify_tim "⛔ martechsignal deploy aborted: could not fast-forward to origin/main. Nothing built, nothing deployed."
                exit 1
            fi
        fi
    fi
    # Hard gate: after syncing, origin/main MUST be an ancestor of HEAD.
    if ! git merge-base --is-ancestor origin/main HEAD; then
        echo "⛔ checkout is still behind origin/main — refusing to deploy stale source" >&2
        notify_tim "⛔ martechsignal deploy aborted: checkout is still behind origin/main after sync, refusing to publish stale source."
        exit 1
    fi
    echo "  in sync with origin/main ($(git rev-parse --short HEAD))"
else
    echo "⚠ --offline: skipping the origin/main sync — the deployed site may not match GitHub" >&2
fi

# ── Intake gate (always, even with --no-build) ─────────────────────
# A record added to tools.json by hand must have its derived surfaces in
# categories.json, its currency, and agreeing prose. If it does not, abort
# here rather than publishing a half-wired page and discovering it in CI.
if ! python3 tools/intake_check.py; then
    echo "⛔ intake gate failed — fix the records above before deploying" >&2
    exit 1
fi

# ── Build from source (skip with --no-build) ───────────────────────
# Regenerate all generated HTML so the upload reflects current source.
# Under `set -e`, a build failure aborts the deploy (don't ship half-built site).
if [ "$DO_BUILD" -eq 1 ]; then
    echo "── Build ───────────────────────────────────────────────"
    python3 tools/build_blog.py
    # Trending before build_tools: the sitemap (written by build_tools) includes the
    # trending page lastmod. Failure is non-fatal; sitemap falls back to file mtime.
    python3 tools/build_trending.py || echo "⚠ trending build failed (non-fatal)"
    # SX-6 pilot: alternatives pages must exist before build_tools (sitemap + interlink)
    python3 tools/build_alternatives.py
    # Best-X + /vs/ pilots (2026-09-26): same ordering rule
    python3 tools/build_best_vsx.py
    # H-4: /best/, /vs/, /alternatives/ section hub indexes must exist before
    # build_tools (the sitemap scan reads them). Same ordering rule again.
    # H10 (r9): glossary + /categories/ + /authors/ indexes also feed the
    # sitemap (and now carry source-truth dateModified), so they build here too.
    # Glossary hub + term pages reuse page_shell from build_tools. This was previously
    # NOT run by deploy, so glossary pages drifted and never picked up site-wide changes
    # (found as a stale 10-link footer during R2 M-6). Failure is non-fatal.
    python3 tools/build_glossary.py || echo "⚠ glossary build failed (non-fatal)"
    # /categories/ and /authors/ index pages (R2 L-7: both returned 404).
    python3 tools/build_indexes.py || echo "⚠ index build failed (non-fatal)"
    python3 tools/build_hubs.py
    # Newsletter result + internal test pages (noindex utility pages). Built
    # before build_tools so the sitemap/dateModified passes see the files; the
    # sitemap only lists known content URLs, so they stay excluded.
    python3 tools/build_subscribe_pages.py
    python3 tools/build_tools.py
    # r23 H-2: breadcrumb graph normalizer - every BreadcrumbList gets @id,
    # every WebPage gets its breadcrumb edge. Runs after every HTML builder.
    python3 tools/sync_breadcrumbs.py
    # 2026-10 redesign: normalize shared chrome on hand-authored pages too.
    python3 tools/sync_chrome.py
    python3 tools/build_md_mirrors.py
    # Homepage tool-index: re-ground featured tools in GSC impressions + stars.
    # Refresh the durable cache first (home/hermes/.hermes/data/gsc-pages-28d.json;
    # /opt/data is wiped on Hermes updates). Non-fatal: falls back to stars-only.
    if command -v uv >/dev/null 2>&1; then
        uv run tools/gsc_perf.py 2>&1 | tail -2 || echo "⚠ GSC cache refresh failed (using existing cache)"
    fi
    # A-3 (v2.4.0 audit): ARD manifest (validated at build; schema errors would
    # flip Lighthouse's ard-schema audit from N/A to failing)
    uv run --with jsonschema python tools/build_ard.py --validate || { echo "⚠ ARD manifest INVALID — aborting deploy"; exit 1; }
    python3 tools/build_homepage.py || echo "⚠ homepage tool-index update failed (non-fatal)"
    # Per-post OG cards (Pillow venv; skip silently if venv missing)
    if [ -x /home/hermes/.hermes/venvs/imggen/bin/python ]; then
        /home/hermes/.hermes/venvs/imggen/bin/python tools/generate_og.py || echo "  (og generation skipped)"
        /home/hermes/.hermes/venvs/imggen/bin/python tools/generate_media.py || echo "  (media generation skipped)"
    fi
    echo ""
fi

# Stage the public subset, then upload that. `wrangler pages deploy .` uploads the
# whole working tree, which put content drafts, pipeline scripts, pipeline JSON,
# docs/, .github/ and editor backups on the public web. Neither .gitignore nor
# .assetsignore is honoured by `pages deploy` (both verified 2026-09-13), so the
# upload directory itself has to be the boundary. See tools/stage_deploy.py, which
# refuses to stage if a known-public file would be missing.
python3 tools/stage_deploy.py

CLOUDFLARE_API_TOKEN="$CLOUDFLARE_API_KEY" \
CLOUDFLARE_ACCOUNT_ID="$ACCOUNT_ID" \
npx wrangler pages deploy deploy-out --project-name="$PROJECT" --commit-dirty=true

# ── Verify what actually went live ─────────────────────────────────
# "wrangler said it uploaded" is not proof. The production domain trails the
# direct upload (a git-connected build has to finish) and the homepage is edge
# cached for up to 5 minutes (s-maxage=300), so poll both signals instead of
# assuming: deploy-out/version.txt carries this build's commit SHA, and the
# homepage must carry the Agentic Marketing form and no trace of Kit.
echo ""
echo "── Live verification ──────────────────────────────────"
WANT_SHA="$(head -1 deploy-out/version.txt 2>/dev/null | awk '{print $1}')"
if [ -z "${WANT_SHA:-}" ]; then
    echo "⛔ deploy-out/version.txt is missing or empty — cannot verify the deploy" >&2
    notify_tim "⛔ martechsignal: the upload ran but deploy-out/version.txt is missing, so the deploy could not be verified against the live site."
    VERIFY_FAILED=1
else
    echo "  expecting commit $WANT_SHA"
    DEADLINE=$(( $(date +%s) + 600 ))
    SERVED=""
    LAST_SEEN=""
    while [ "$(date +%s)" -lt "$DEADLINE" ]; do
        LAST_SEEN="$(curl -sS --max-time 20 "https://martechsignal.com/version.txt?cb=${RANDOM}${RANDOM}" 2>/dev/null || true)"
        if printf '%s' "$LAST_SEEN" | grep -qF "$WANT_SHA"; then SERVED="$LAST_SEEN"; break; fi
        sleep 15
    done
    if [ -n "$SERVED" ]; then
        echo "  live /version.txt serves $WANT_SHA"
    else
        echo "⛔ after 10 minutes the live site still does not serve commit $WANT_SHA" >&2
        echo "   last seen: $(printf '%s' "${LAST_SEEN:-<no response>}" | head -2 | tr '\n' ' ')" >&2
        notify_tim "⛔ martechsignal: after 10 minutes the live /version.txt still does not serve commit $WANT_SHA. The upload may have gone to a different build, or the domain is serving a stale bundle. Check the Pages deployment."
        VERIFY_FAILED=1
    fi
fi

# Homepage markers: signups must go to the self-hosted Agentic Marketing form,
# and Kit must be gone (PR #2, merged 2026-10-26). Edge cache gives this 5 min.
HOME_DEADLINE=$(( $(date +%s) + 360 ))
HOME_OK=0
AM_HITS=0
KIT_HITS=0
while [ "$(date +%s)" -lt "$HOME_DEADLINE" ]; do
    HOME_HTML="$(curl -sS --max-time 25 "https://martechsignal.com/?cb=${RANDOM}${RANDOM}" 2>/dev/null || true)"
    AM_HITS=$(printf '%s' "$HOME_HTML" | grep -cF 'am.martechsignal.com/f/frm_' || true)
    KIT_HITS=$(printf '%s' "$HOME_HTML" | grep -ciF 'app.kit.com' || true)
    if [ "${AM_HITS:-0}" -ge 1 ] && [ "${KIT_HITS:-0}" -eq 0 ]; then
        HOME_OK=1
        break
    fi
    sleep 20
done
if [ "$HOME_OK" -eq 1 ]; then
    echo "  live homepage uses the am.martechsignal.com form, no app.kit.com"
else
    echo "⛔ homepage check failed: am form hits=${AM_HITS:-0}, app.kit.com hits=${KIT_HITS:-0}" >&2
    notify_tim "⛔ martechsignal: the live homepage check failed after 6 minutes (am.martechsignal.com form hits=${AM_HITS:-0}, app.kit.com hits=${KIT_HITS:-0}). Signups may not be reaching the self-hosted platform."
    VERIFY_FAILED=1
fi

# ── IndexNow ping (Bing / Yandex / Seznam / Naver via api.indexnow.org) ──
# tools/indexnow_submit.py: submits the most recently changed URLs (from the
# content-hash lastmod store) with the deployed key file. Non-fatal: an
# IndexNow hiccup must never fail a deploy.
if [ -f tools/indexnow_submit.py ]; then
    python3 tools/indexnow_submit.py || echo "⚠ IndexNow submit failed (non-fatal)"
fi

# ── Git commit + push (skip with --no-git) ─────────────────────────
# Runs last so a failed upload never leaves a commit nobody can explain. A failed
# PUSH, though, is a failure: if origin/main does not get this commit, GitHub and
# the live site have diverged and the next deploy builds from stale source.
if [ "$DO_GIT" -eq 1 ]; then
    echo ""
    echo "── Git sync ────────────────────────────────────────────"
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit -m "deploy: $(date -u +%Y-%m-%d\ %H:%M) UTC — rebuild + publish" >/dev/null
            echo "  committed pending changes"
        else
            echo "  working tree clean — nothing to commit"
        fi
        if git push origin HEAD 2>/tmp/deploy-push.err; then
            echo "  pushed $(git rev-parse --short HEAD) to origin/main"
        else
            echo "⛔ git push FAILED — GitHub and the live site have diverged" >&2
            sed 's/^/    /' /tmp/deploy-push.err >&2
            notify_tim "⛔ martechsignal: the site deployed but git push FAILED, so GitHub and the live site have diverged. Fix the push before the next deploy ($(head -2 /tmp/deploy-push.err | tr '\n' ' '))."
            PUSH_FAILED=1
        fi
    else
        echo "Not a git repo — skipping git sync."
    fi
fi

# ── Google Search Console URL Inspection ───────────────────────────
# Requests indexing for URLs changed in the last commit.
# Skips silently if no service account key is configured.
echo ""
echo "── GSC Indexing ───────────────────────────────────────"
if command -v uv >/dev/null 2>&1 && [ -f gsc_inspect.py ]; then
    uv run gsc_inspect.py --changed 2>&1 || echo "⚠ GSC inspection failed (non-fatal)"
else
    echo "Skipped (uv or gsc_inspect.py not found)"
fi

# ── Final status ───────────────────────────────────────────────────
# Verification and push are the two places where "it printed something" is not
# the same as "it worked", so they decide the exit code.
echo ""
if [ "$VERIFY_FAILED" -eq 0 ] && [ "$PUSH_FAILED" -eq 0 ]; then
    echo "✅ deploy complete: $(git rev-parse --short HEAD) live and pushed"
    exit 0
fi
[ "$VERIFY_FAILED" -eq 1 ] && echo "❌ deploy NOT verified against the live site (see above)" >&2 || true
[ "$PUSH_FAILED" -eq 1 ] && echo "❌ deploy committed locally but NOT pushed to GitHub" >&2 || true
exit 1

