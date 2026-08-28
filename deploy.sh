#!/usr/bin/env bash
set -euo pipefail

# Deploy martechsignal.com to Cloudflare Pages via wrangler.
# Requires: CLOUDFLARE_API_KEY (Pages:Edit) and CLOUDFLARE_ACCOUNT_ID env vars.
#
# Usage:
#   ./deploy.sh              build + deploy to Cloudflare + IndexNow + git commit/push
#   ./deploy.sh --no-build   skip the build step (upload current files as-is)
#   ./deploy.sh --no-git     skip the git commit/push step
#
# The build step regenerates blog posts, tool/category pages, sitemap, and the
# homepage latest-signals block from source (content/drafts/*.md, tools.json).
# It runs BEFORE upload so the live site always reflects current source — this
# closes the "deployed stale HTML" footgun where edits to a draft never reached
# the site because deploy.sh used to only upload pre-built files.

# ── Flags ──────────────────────────────────────────────────────────
DO_GIT=1
DO_BUILD=1
for arg in "$@"; do
    case "$arg" in
        --no-git)   DO_GIT=0 ;;
        --no-build) DO_BUILD=0 ;;
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

# ── Build from source (skip with --no-build) ───────────────────────
# Regenerate all generated HTML so the upload reflects current source.
# Under `set -e`, a build failure aborts the deploy (don't ship half-built site).
if [ "$DO_BUILD" -eq 1 ]; then
    echo "── Build ───────────────────────────────────────────────"
    python3 tools/build_blog.py
    python3 tools/build_tools.py
    # Per-post OG cards (Pillow venv; skip silently if venv missing)
    if [ -x /home/hermes/.hermes/venvs/imggen/bin/python ]; then
        /home/hermes/.hermes/venvs/imggen/bin/python tools/generate_og.py || echo "  (og generation skipped)"
        /home/hermes/.hermes/venvs/imggen/bin/python tools/generate_media.py || echo "  (media generation skipped)"
    fi
    echo ""
fi

CLOUDFLARE_API_TOKEN="$CLOUDFLARE_API_KEY" \
CLOUDFLARE_ACCOUNT_ID="$ACCOUNT_ID" \
npx wrangler pages deploy . --project-name="$PROJECT" --commit-dirty=true

# ── IndexNow ping (Bing / Yandex / Seznam / Naver via api.indexnow.org) ──
# tools/indexnow_submit.py: submits the most recently changed URLs (from the
# content-hash lastmod store) with the deployed key file. Non-fatal: an
# IndexNow hiccup must never fail a deploy.
if [ -f tools/indexnow_submit.py ]; then
    python3 tools/indexnow_submit.py || echo "⚠ IndexNow submit failed (non-fatal)"
fi

# ── Git commit + push (skip with --no-git) ─────────────────────────
# Runs last so a successful deploy is never blocked by a git hiccup.
if [ "$DO_GIT" -eq 1 ]; then
    echo ""
    echo "── Git sync ────────────────────────────────────────────"
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit -m "deploy: $(date -u +%Y-%m-%d\ %H:%M) UTC — rebuild + publish" >/dev/null
            echo "Committed pending changes."
        else
            echo "Working tree clean — nothing to commit."
        fi
        # Push any local commits ahead of origin (non-fatal on failure)
        if git push origin HEAD 2>&1 | tail -2; then
            :
        else
            echo "⚠ git push failed — deploy succeeded, push manually later." >&2
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
