# C-0 Distribution Play — Staged Drafts (NOT published)

Status: DRAFTS ONLY. Nothing here goes out without Tim's explicit OK.
Created: 2026-08-28 night shift. Source: final audit C-0 (zero external citation
footprint: Common Crawl/Wayback/HN all empty — the ceiling on every ranking ambition).

---

## 1. IndexNow (Bing/Yandex/Seznam/Naver) — mechanical, no voice needed

- Script: `tools/indexnow_submit.py` (in repo, tested logic, not yet run)
- To activate:
  1. `python3 -c "import secrets;print(secrets.token_hex(16))"` → save to `tools/.indexnow-key`
  2. Deploy the same key as `/.well-known/indexnow-<key>.txt` (add to repo root, deploy)
  3. Run `python3 tools/indexnow_submit.py https://martechsignal.com/` as smoke test
  4. Optional: append the submit call to deploy.sh (changed-URLs mode) — recommend YES,
     it's one line and free.
- Effect: faster Bing discovery. Won't move Google rankings directly, but Bing feeds
  ChatGPT search + Copilot — real AI-search visibility for a young domain.

## 2. Show HN draft (needs Tim's account + judgment on timing)

Title options:
- "Show HN: I ran an open-source SEO auditor on my own site and it found a sitewide 404 my pipeline shipped"
- "Show HN: MartechSignal – independent AI-marketing-tool reviews, built in public"

Draft body (350 words, Tim's voice skeleton — needs his personal touches marked [TIM]):

> I run martechsignal.com solo — reviews of AI marketing automation tools. It's a
> 12K-site on a Cloudflare Pages static build, no backend.
>
> Two weeks ago I ran an open-source SEO audit skill (Claude SEO, MIT, 14K stars)
> against my own site. It found a sitewide og:image 404 that my own deploy pipeline
> had shipped [TIM: 1-2 sentences of color — the feeling of your own tooling shipping
> a bug you then blog about]. I wrote the teardown up, kept re-running it, and the
> score went 61 → 66 → 72 → 74.6 across two days of fixes [TIM: confirm numbers].
>
> Three things I didn't expect:
> 1. The audit found real schema bugs (price:0 emitted for enterprise tools —
>    Google can read that as a factual price claim)
> 2. The strictest findings were strategic, not technical — "you argue for owning
>    a quotable number but publish none" is a fair hit
> 3. Scores are only comparable within one grader version; across versions they're
>    noise [TIM: this is the calibration point]
>
> Stack: Python builders → static HTML, sitemap bound to content hashes, GSC URL
> Inspection wired into deploys. No framework, no JS on content pages.
>
> [TIM: closing — what feedback you want: schema? the scoring-policy question?
> the directory-vs-review positioning?]

Timing note: post Tue-Thu 07:00-09:00 CET. Do NOT post the same day as the
Wikipedia push or any other community activity.

## 3. Reddit r/selfhosted draft (Tim's account)

Title: "I built a self-hosted-friendly directory of open-source martech tools (115 tools, no tracking)"

> Long-time lurker, first post here. I've been cataloguing open-source and
> self-hostable marketing tools — CRMs (EspoCRM, Twenty, Monica, Frappe), email
> (Listmonk, Mailcow-adjacent stuff), analytics (Matomo, Plausible, Umami, Snowplow),
> automation (n8n, Activepieces-style workflow tools). 115 tools, each with what it
> costs to actually run, license, and who it fits.
>
> It started as my own notes for client work. The rule: no pay-to-play, no fake
> review scores — if we don't have hands-on notes on a tool, the page says so.
>
> Would love feedback from people running these tools in production — especially
> where my write-ups are wrong. [TIM: add 1 line about which tools he personally runs]
>
> Link: https://martechsignal.com/tools/ (static site, no tracking scripts beyond
> self-hosted Plausible-style analytics)

Note: r/selfhosted rules check needed on post day (self-promo rules). The
open-source angle + genuine question framing is the right shape.

## 4. LinkedIn post draft (Tim's account — his professional network)

(Full text in linkedin-post-draft.md — needs Tim's voice; core hook: "I audited
my own site with an AI SEO tool. The most useful finding wasn't technical.")

## 5. Momentum-tracker data page (site content — can ship without Tim)

- Data: tools/github-history.json already snapshots 52 repos weekly
- Plan: /data/open-source-momentum/ — weekly star deltas, "fastest-growing OSS
  martech tools" table with citations to GitHub API (it's public data, citable)
- This creates the linkable asset C-0 wants: journalists/newsletter writers get
  quotable numbers (ties to H16 if Tim picks the MartechSignal Score option)

## 6. Sequencing (proposed)

Week 1: IndexNow + momentum data page shipped
Week 2: LinkedIn post (softest landing) → Reddit r/selfhosted
Week 3: Show HN (strongest community, needs the momentum page live as the artifact)
Ongoing: pitch individual tools' maintainer communities ONLY where hands-on notes
are genuine ("we listed your tool — here's what we got right/wrong" = good-faith
link magnet that actually earns links)
