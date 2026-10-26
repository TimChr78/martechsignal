#!/usr/bin/env bash
# Is /mnt/user/dev/martechsignal safe to work in right now?
#
# WHY: work arrives from several directions at once — merged pull requests on
# GitHub, the deploy pipeline, and other agents (tool-directory, pricing,
# CTR loop) editing the same checkout. A blog post drafted against a stale tree
# links to slugs that may no longer exist, and the deploy at the end of the run
# then hits a rebase it did not expect. This script answers two questions
# cheaply: am I current, and is somebody else mid-flight?
#
# Usage:
#   tools/sync_checkout.sh            check only, never writes
#   tools/sync_checkout.sh --apply    fast-forward to origin/main when safe
#
# Exit codes (a caller should branch on these, not on log text):
#   0  in sync with origin/main
#   2  could not reach origin (fetch failed) — current state unproven
#   3  parallel work in flight (deploy/build running, or uncommitted changes)
#   4  behind origin/main (check-only mode did not fix it)
#   5  fast-forward refused (diverged history) — needs a human
set -uo pipefail

APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1

cd "$(dirname "$0")/.." || exit 2

say() { printf '%s\n' "$*"; }

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    say "NOT A GIT REPO: $(pwd)"
    exit 2
fi

# ── Parallel work in flight? ───────────────────────────────────────
# A deploy rebuilds the tree and commits with `git add -A`; a build rewrites
# the generated pages. Either one makes the working tree a moving target.
if pgrep -xf "bash deploy.sh" >/dev/null 2>&1 || pgrep -xf "bash /mnt/user/dev/martechsignal/deploy.sh" >/dev/null 2>&1; then
    say "BUSY: a deploy.sh run is in flight — do not sync or build against this tree"
    exit 3
fi
if pgrep -f "tools/build_(blog|tools|homepage|indexes|hubs|md_mirrors)\.py" >/dev/null 2>&1; then
    say "BUSY: a site builder is running — do not sync or build against this tree"
    exit 3
fi

DIRTY="$(git status --porcelain | head -20)"
if [ -n "$DIRTY" ]; then
    say "BUSY: uncommitted changes in the working tree (another agent's pipeline state, or yours):"
    printf '%s\n' "$DIRTY" | sed 's/^/    /'
    if [ "$APPLY" -eq 1 ]; then
        # Never fast-forward over somebody's half-finished tree. deploy.sh owns
        # this case: it commits pipeline state first, then rebases.
        say "Refusing to sync over a dirty tree. Publish through deploy.sh (which commits, then rebases) or investigate first."
    fi
    exit 3
fi

# ── Current? ───────────────────────────────────────────────────────
if ! git fetch origin --quiet 2>/tmp/sync_checkout_fetch.err; then
    say "FETCH FAILED: cannot prove the checkout is current"
    sed 's/^/    /' /tmp/sync_checkout_fetch.err
    exit 2
fi

AHEAD="$(git rev-list --count origin/main..HEAD)"
BEHIND="$(git rev-list --count HEAD..origin/main)"
HEAD_SHA="$(git rev-parse --short HEAD)"
say "HEAD $HEAD_SHA | ahead of origin/main: $AHEAD | behind: $BEHIND"

if [ "$BEHIND" -eq 0 ]; then
    say "IN SYNC with origin/main"
    exit 0
fi

if [ "$APPLY" -eq 0 ]; then
    say "BEHIND by $BEHIND commit(s) — rerun with --apply to fast-forward"
    git log --oneline "HEAD..origin/main" | sed 's/^/    /'
    exit 4
fi

if [ "$AHEAD" -gt 0 ]; then
    say "Local commits exist ($AHEAD). That is deploy.sh's job to rebase, not this script's."
    exit 5
fi

if git merge --ff-only origin/main >/tmp/sync_checkout_ff.log 2>&1; then
    say "FAST-FORWARDED to $(git rev-parse --short HEAD)"
    exit 0
fi

say "FAST-FORWARD REFUSED — history diverged, needs a human"
sed 's/^/    /' /tmp/sync_checkout_ff.log
exit 5
