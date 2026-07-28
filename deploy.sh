#!/usr/bin/env bash
set -euo pipefail

# Deploy martechsignal.com to Cloudflare Pages via wrangler.
# Requires: CLOUDFLARE_API_KEY (Pages:Edit) and CLOUDFLARE_ACCOUNT_ID env vars.

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
