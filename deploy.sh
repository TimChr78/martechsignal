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
    echo ""
fi

CLOUDFLARE_API_TOKEN="$CLOUDFLARE_API_KEY" \
CLOUDFLARE_ACCOUNT_ID="$ACCOUNT_ID" \
npx wrangler pages deploy . --project-name="$PROJECT"

# ── IndexNow ping (Bing / Yandex) ──────────────────────────────────
INDEXNOW_KEY="ca0ff0788c47a161e772b2e9b073b2a4"
INDEXNOW_ENDPOINT="https://www.bing.com/indexnow"

# Collect URLs to submit: homepage + blog posts
URLS=("https://martechsignal.com/")

if [ -d "blog" ]; then
    for dir in blog/*/; do
        slug=$(basename "$dir")
        [ "$slug" = "index.html" ] && continue
        [ -f "$dir/index.html" ] && URLS+=("https://martechsignal.com/blog/$slug/")
    done
fi

if [ ${#URLS[@]} -gt 1 ]; then
    URLS_JSON=$(printf '"%s",' "${URLS[@]}" | sed 's/,$//')
    PAYLOAD="{\"host\":\"martechsignal.com\",\"key\":\"$INDEXNOW_KEY\",\"keyLocation\":\"https://martechsignal.com/${INDEXNOW_KEY}.txt\",\"urlList\":[$URLS_JSON]}"
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$INDEXNOW_ENDPOINT" \
        -H "Content-Type: application/json" -d "$PAYLOAD")
    echo "IndexNow: $HTTP_CODE (${#URLS[@]} URLs submitted)"
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
