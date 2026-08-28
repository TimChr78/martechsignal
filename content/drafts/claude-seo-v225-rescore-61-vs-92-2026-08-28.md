---
title: "Claude SEO v2.2.5 Re-Scored Our Site 61. A Week Ago It Said 92. Both Audits Were Right."
slug: claude-seo-v225-rescore-61-vs-92
date: 2026-08-28
author: MartechSignal
tags: [AI, SEO, Agent Skills, Quality]
---

On August 24, the open-source [Claude SEO](/tools/claude-seo/) skill scored martechsignal.com 92/100. We published the full teardown, patted ourselves on the back, and moved on. Two days later we updated the skill from v2.2.4 to v2.2.5 and ran it against the identical site. It came back with 61/100.

Nothing regressed in those two days. We know that because we shipped improvements during them, and because the 61 report itself says so: the site it crawled was mechanically sound. The score dropped 31 points because the grader changed, not because the site did. And here is the part that took us a day to accept: both scores were right.

This is part two of that story. [Part one](/blog/claude-seo-teardown-martechsignal/) covered what v2.2.4 found when we pointed it at our own production domain, including the sitewide og:image 404 our deploy pipeline had been shipping. This one is about what happens when your measuring instrument changes underneath you.

## The timeline, with receipts

| Date | Skill version | Score | What happened |
|---|---|---|---|
| Aug 23 | v2.2.4 | 83 | First audit. Found the og:image 404, thin glossary, templated tool pages |
| Aug 24 | v2.2.4 | 92 | Re-audit after nine same-day fixes, verified by independent re-crawl |
| Aug 25 | v2.2.4 | 96 | Third pass. Zero Critical, zero High findings, first time |
| Aug 25 | v2.2.5 released | n/a | GitHub release: "Reliability and Google Currency" |
| Aug 26 | v2.2.5 | 61 | Same site, new grader, 31-point drop |
| Aug 27 | v2.2.5 | 66, then 72, then 74.6 | Three re-audits across one day of remediation |

Every number in that table comes from a saved audit report or a commit on GitHub main. The v2.2.4 runs judged a site that had just fixed everything v2.2.4 knew how to complain about, and they judged it favorably. The v2.2.5 run judged the same pages against a rubric that did not exist a week earlier.

One honesty note before we go further: the original August 26 report and its specialist artifacts were lost when a container's /opt volume was rebuilt before our nightly backup ran. The 61 score, the finding IDs, and the category breakdown survive because the three follow-up audits reference them and the fix commits describe them. Everything from August 27 onward is on disk and linked in this post.

## What v2.2.5 measures that v2.2.4 never looked at

The [v2.2.5 release](https://github.com/AgriciDaniel/claude-seo/releases/tag/v2.2.5) describes itself as a reliability release: JSON-LD graph traversal that rejects malformed nodes safely, Google guidance refreshed through August 25 (including the August spam update and Preferred Sources), 439 tests passing against 410 in v2.2.4. That is the changelog version. The version we experienced is four new programmatic gates, and each one caught something real.

**Gate 1: content uniqueness with hard stops.** The new version runs shingle-overlap math across the whole corpus and applies a hard-stop threshold once a directory crosses 50 pages. Our 116-page tool directory is 2.3 times over that threshold, which means the gate runs at full strictness. The corpus passed the population test (median pairwise overlap around 4%, most pages 85%+ unique), but the gate found a localized cluster of stubs: Frappe CRM at 55 substantive words, overlapping the Dolibarr page by 0.419. v2.2.4 counted words. v2.2.5 measured whether the words were the same words.

**Gate 2: factual consistency between schema and page.** Our generator emitted `"price": 0` in the SoftwareApplication schema for enterprise-priced tools, while the page body said things like "$20 to $3,600 per month" (HubSpot's real range, verified from our own pricing data). The old version validated that the JSON-LD parsed. The new version checks whether what the schema says is true. A machine-readable claim of "free" next to a human-readable price of $890/mo is a lie with extra steps, and the audit called it that.

**Gate 3: off-site citation footprint.** The audit queried Common Crawl's web graph, the CC Index API across three crawl releases, Wayback's CDX index, and Hacker News. All four came back empty, which is what a 33-day-old domain should return. The report scored authority position at 12/100 and, to its credit, refused to guess a Domain Authority number when no Moz or Bing credentials were available. "NOT MEASURABLE" is a valid audit output. More tools should learn to print it.

**Gate 4: trust infrastructure.** No privacy policy, no terms, no contact page. We knew this. We had been putting it off because it is boring. The audit does not care what is boring.

## What was real, and we fixed the same day

Five findings went from report to production in one night, all on GitHub main where you can read them.

1. **Navigation missing on roughly 141 pages.** A wrapper div difference in our template dropped the sitewide nav from every tool, glossary, and category page. The homepage kept it, which is why none of our spot-checks ever noticed: we spot-check pages that work. Commit `2d12236`.
2. **The price-sentinel lie across 14 tools.** Thirteen enterprise tools plus one paid tool emitted `price: 0`. We fixed it at generation time, not page by page: non-numeric pricing now suppresses the price schema and the fake "free tier" FAQ line entirely. (NocoBase kept its zero because its free tier is real.) Commit `2d12236`.
3. **A CRM named "crm".** Our Frappe CRM page carried an H1 derived straight from the slug. The audit's name-consistency check wanted display names, and "crm" is not one. Same commit.
4. **"Open-Source Tools Tools".** A pluralization bug in the category hub title template. Fixed with the same guard our H1s already used, so it cannot come back in another template. Commit `c90115f`.
5. **Zero legal pages.** Privacy and terms went up with sitewide footer links in `2d12236`, contact page in `cd521a2`.

We also deepened four tool pages targeting queries our Search Console data said were winnable (`20283a0`), but that was GSC-driven work already in flight, not audit-driven.

The score responded the way scores should when fixes are real: 61, then 66, then 72, then 74.6, each from an independent re-audit on the same v2.2.5 version. That last number is where the site sits as of this writing, with Technical at 93 and the remaining damage concentrated in content strategy, not plumbing.

## The findings we rejected

An audit is a list of claims, not a list of orders. Two of v2.2.5's recommendations did not survive contact with our own data, and rejecting them out loud is the point of this post.

**"Deepen the glossary to match Wikipedia and Salesforce."** The audit measured our 31 glossary terms against 2,000-word vendor guides and encyclopedic incumbents and proposed lifting the top eight to match. We declined the blanket version. Our Search Console impressions say demand concentrates in a handful of terms, so ten terms got concrete "The numbers" sections with real benchmarks and prices, and the rest stay at uniform depth until data argues otherwise. Writing 2,000 words to match an incumbent's word count is a cost you pay to look like them, and we cannot out-Wikipedia Wikipedia.

**"Close the authority gap with links."** The backlink findings leaned toward footprint-building, which is the standard prescription for a 12/100 authority score. We published our objection on August 25: in [the post on link-building and AI answers](/blog/link-building-wont-get-you-into-ai-answers-2026-08-25/), we argued that the earnable asset for this site is a number an answer engine can quote, not a swapped link from a domain of similar weakness. DA-driven link swaps between two young sites move nothing we can measure and burn time we would rather spend on the rating methodology. If we are wrong, the 90-day GSC data will say so.

## What this means if you run AI audit skills

Pin your grader version. A score is a measurement against a specific rubric, and rubric changes are invisible if you only track the number. Our 83 to 92 to 96 climb was real signal because every step ran on v2.2.4. Our 61 to 66 to 72 to 74.6 climb is real signal because every step ran on v2.2.5. The 92 to 61 drop is not signal at all. That drop is two instruments looking at one site.

Diff the release before you re-run. We updated on August 26 and ran the audit the same day, which is the worst order. Reading the [release notes](https://github.com/AgriciDaniel/claude-seo/releases/tag/v2.2.5) first would have told us that JSON-LD validation got stricter and Google guidance got refreshed through the August spam update, so a lower score was the expected outcome. We would have skipped the half-day of wondering what we broke.

Treat new gates as feature additions. The instinct when a score drops 31 points is to distrust the tool. The right move is to check whether the new complaints are true. Four of four were. The nav bug had survived months of our own testing because we never looked at a tool page as a crawler sees it. The price-sentinel bug had survived because schema validation tells you a field parses, not whether it is honest.

::: verdict warn
Absolute scores are not comparable across grader versions. If you track an AI audit score over time, pin one version as your longitudinal baseline, log the version with every number you publish, and read only the deltas within a version as signal. Anything else is measuring the thermometer.
:::

## The verdict

v2.2.5 did not break our scorecard. It built us a harder one, and the harder one found a nav bar that was not there, prices that lied, and pages with no legal identity. The 92 was honest for what v2.2.4 could see. The 61 was honest for what v2.2.5 could see. From here on we only compare scores produced by the same version, and we say which version it was.

Full history: the [v2.2.4 teardown](/blog/claude-seo-teardown-martechsignal/), the [Claude SEO directory entry](/tools/claude-seo/), and everything else we have written about [agent skills](/categories/agent-skills/) and [SEO](/categories/seo/).
