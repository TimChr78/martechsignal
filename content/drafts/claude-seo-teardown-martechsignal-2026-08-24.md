---
title: "I Ran Claude SEO on My Own Site. It Found What Our Pipeline Missed."
seo_title: "I Ran Claude SEO on My Own Site. It Found What"
slug: claude-seo-teardown-martechsignal
date: 2026-08-24
author: MartechSignal
tags: [Agent Skills, SEO]
---

This site reviews martech tools for a living. On August 23 we pointed a free, open-source [agent skill](/categories/agent-skills/) at our own production domain, and it found a sitewide og:image 404 that our deploy pipeline had been shipping for weeks. Every link to this site shared on X, LinkedIn, or Slack rendered as bare text. The build system missed it, and we missed it by eye too. A stranger's MIT-licensed script caught it in one crawl.

This is the teardown of that run: what it found, where it fell down, and the footer it appends to every deliverable that you should know about before pointing it at client work.

## What we actually ran

The tool is [Claude SEO](/tools/claude-seo/) (AgriciDaniel/claude-seo, v2.2.4, MIT, roughly 14.8K GitHub stars as of this writing): 25 sub-skills and 18 sub-agents covering technical SEO, schema, E-E-A-T, backlinks, and AI search readiness, packaged for Claude Code.

We did not pay Anthropic for this. Our Claude Code CLI is wired through OmniRoute to CommandCode's ox-alpha model, so the skill ran on third-party capacity with no subscription involved. The trade is speed: ox-alpha takes 60 to 160 seconds per turn. The skill also degrades honestly. With no Google API credentials it skips the agents that need them and says so in the report ("Credential Tier −1" is its phrase), and Common Crawl's free tier returned zero metrics for a domain this young. It audited what it could reach and told us what it could not.

## The marketing versus the runtime

The README's headline feature is 18 parallel agents. In practice our run executed them sequentially, an inline fallback the report itself labels as such. The full audit of 169 sitemap URLs took about two hours. If you are sizing one of these runs into a workday, plan for that number, not for a parallel speedup.

The output was more disciplined than most paid tools we have reviewed. Every finding carried evidence (the actual curl response, the word count, the link graph), a falsifiability check ("if impressions don't move in 8 weeks, the terms are too competitive"), and a leading indicator to watch. That framing is [technical SEO](/glossary/seo/) done the way we wish vendors did it: claims you can disprove, not vibes.

## What it caught that we missed

The headline score was 83/100, with the damage concentrated in three categories: Content Quality at 72, Images at 60, everything else in the high 80s. The findings that stung:

**The og:image 404.** All 36 pages carrying an og:image tag pointed at `/og.png`, which returned 404. Zero `twitter:image` tags anywhere. This site's growth plan is editorial content shared by readers, and every share arrived cardless. The fix is live now: [/og.png](/og.png) returns 200, and blog, tool, and category pages each carry their own generated image.

**A uniformly thin glossary.** All 26 glossary pages sat under 300 words, median 203, while targeting head terms like CRM and attribution where 1,000-word incumbents own the SERP. We expanded 11 of them same-day; [/glossary/cro/](/glossary/cro/) went from a stub to 529 words of actual definition and context.

**109 near-identical tool pages.** The audit measured what we suspected and ignored: identical 18-link blocks on every page, the same three-question FAQ on 108 of 109, one meta-description template. Post-HCU, that is a scaled-content profile. We added unique hands-on notes and verdicts to the 20 tools with real search demand first.

**Plumbing.** A broken homepage link to [/tools/segment/](/tools/segment/) (it pointed at a 404 slug), [/checklist/](/checklist/) live and linked but absent from the sitemap and llms.txt, every sitemap entry stamped with the same fake lastmod date, and no HSTS header. Each was a minutes-long fix that had been invisible to us for months.

**Internal linking and entity signals.** Blog posts linked to tools in 17 of 17 cases and to glossary pages in zero of 17. Our Article schema pointed the author at the homepage instead of a person. We added blog-to-glossary links (14 of 17 posts now have them) and built [/authors/tim-christensen/](/authors/tim-christensen/) with proper schema the same day.

## Where it fell down

The audit could not measure Core Web Vitals field data or lab scores because we had no PageSpeed API key configured, and it said so rather than inventing numbers. Common Crawl had nothing on a young domain. And because we were fixing things while it crawled, it audited a moving target: some findings described state that had already changed by the time the report rendered. Two hours of wall-clock time makes that unavoidable.

It also missed things the second pass caught, which is worth saying plainly. When we re-ran the audit on August 24 after the fixes, it surfaced two new High findings the first run never flagged: our FAQ schema existed only in JSON-LD with no visible FAQ content on the page, and every blog post emitted its Article schema twice. The Schema category score actually went down between runs, from 90 to 88. One audit is a snapshot, not a certification.

## The footer you should know about

Every major deliverable this skill produces ends with an appended block: "Built by agricidaniel, Join the AI Marketing Hub community," followed by links to the author's free and paid Skool communities. There is no disclosure of it, no flag, and no opt-out in the audit run. If you run this skill on a client's site and hand them the report, you are handing them an advertisement embedded in what looks like neutral analysis. The skill is MIT licensed and free, so this is not a scandal. It is a governance fact you should decide about consciously, especially in agency workflows where the deliverable carries your name.

## The receipts

<div class="flow-strip">
  <div class="flow-step"><span class="flow-label">AUDIT</span><span class="flow-sub">169 pages crawled, ~2 hours</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">FIND</span><span class="flow-sub">3 high, 9 medium, 7 low</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">FIX</span><span class="flow-sub">all 9 addressed same day</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step ai"><span class="flow-label">RE-AUDIT</span><span class="flow-sub">83 to 92, verified by re-crawl</span></div>
</div>

We addressed all nine actionable findings from the first audit the same day, across commits 547bedc through 1c6385e on August 23. The re-audit on August 24 re-crawled all 171 URLs (the site grew by two pages in the meantime) and scored it independently:

| Category | Weight | Aug 23 | Aug 24 | Delta |
|---|---|---|---|---|
| Technical SEO | 22% | 85 | 95 | +10 |
| Content Quality | 23% | 72 | 85 | +13 |
| On-Page SEO | 20% | 88 | 93 | +5 |
| Schema | 10% | 90 | 88 | −2 |
| Performance (CWV) | 10% | 92 | 92 | 0 |
| AI Search Readiness | 10% | 88 | 96 | +8 |
| Images | 5% | 60 | 98 | +38 |
| **Health score** | | **83** | **92** | **+9** |

::: verdict win
The audit worked. It found real defects our own pipeline shipped, every claim carried verifiable evidence, and the score moved when we fixed things, confirmed by a second independent crawl rather than self-report.
:::

::: verdict warn
The score is not the point. The remaining gaps the re-audit found (thin category hubs, an orphaned author page, duplicated schema) are the kind of things a second pass catches precisely because the first pass changed what it was looking at. Treat any single audit as a starting list, never a clean bill of health.
:::

## The verdict

Claude SEO is the strongest free [SEO](/categories/seo/) skill we have run, and it embarrassed our own deploy pipeline on our own site. Use it. Run it twice, a week apart, and assume the first report is incomplete. Strip the footer before it touches a client. We fixed everything the first audit named and the second crawl confirmed it, then found three new problems we still have to work through.

See the full tool review and alternatives in our [Claude SEO directory entry](/tools/claude-seo/), and our [conversion rate optimization glossary](/glossary/cro/) if the thin-content scoring is news to you.
