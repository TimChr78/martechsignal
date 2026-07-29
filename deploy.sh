#!/usr/bin/env bash
set -euo pipefail

# Deploy martechsignal.com to Cloudflare Pages via wrangler.
# Requires: CLOUDFLARE_API_KEY (Pages:Edit) and CLOUDFLARE_ACCOUNT_ID env vars.

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
