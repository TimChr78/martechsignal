---
title: "Four Graders, One Site: What Five Claude SEO Scores Measure"
seo_title: "Five Claude SEO Scores, Four Graders: None Compare"
slug: claude-seo-v231-four-graders
date: 2026-09-18
author: Tim Christensen
tags: [AI, SEO, Agent Skills, Open Source]
categories: [agent-skills]
---

We have pointed the open-source Claude SEO skill at martechsignal.com five times since August. Scores: 83, 61, 74.6, 80, 76.6. None of them compare.

That last sentence is the whole argument, so here is the defense. Four grading setups produced those five numbers: v2.2.4, v2.2.5, the September R2 re-audit, and v2.3.1. [Claude SEO](/tools/claude-seo/) rewrites its gates, specialists, and rubric weights with most releases, so every version bump changes what the number means. Treat the score like a credit rating and you will read a tool upgrade as your site getting worse. We made that mistake publicly in August. Five audits later, we have a cleaner model: the score is an instrument reading, and instruments get recalibrated.

## The five scores, and which grader produced them

| Date | Version | Score | What changed |
|---|---|---|---|
| Aug 23 | v2.2.4 | 83 | First full audit of our own production domain |
| Aug 26 | v2.2.5 | 61 | Same site, stricter gates, 22-point drop |
| Aug 27 | v2.2.5 | 74.6 | One day of remediation, same grader |
| Sep 8 | R2 re-audit | 80 | Two more weeks of fixes, re-scored |
| Sep 16 | v2.3.1 | 76.6 | New rubric plus a Backlinks specialist |

(v2.2.4 also scored us 92 and then 96 across two August re-runs as we fixed what it found. That run-up, and the 61 that followed the upgrade, are covered in [the 61-vs-92 post](/blog/claude-seo-v225-rescore-61-vs-92/). The first audit itself is in [the original teardown](/blog/claude-seo-teardown-martechsignal/).)

Only one pair in that table shares a grader: 61 and 74.6, both v2.2.5, one day apart. That delta is real. We fixed things and the same instrument measured the improvement. Every other step mixes site changes with rubric changes, and nobody can decompose that after the fact.

The 80 to 76.6 step is the sneaky one. Between September 8 and September 16 we shipped fixes, not regressions, yet the number went down because v2.3.1 grades differently and brought a new specialist that found something ugly. If we had been watching only the aggregate, we would have spent that week hunting for damage that did not exist.

## What v2.3.1 actually said

Category scores from the September 16 run:

| Category | Score |
|---|---|
| Core Web Vitals | 92 |
| Technical SEO | 88 |
| Content quality | 68 |
| Topic clusters | 58 |
| SXO (search experience) | 46 |
| Backlinks | 5 (unweighted) |

The E-E-A-T breakdown: Expertise 82, Trust 76, Experience 62, Authoritativeness 48.

Authoritativeness is the ceiling holding the rest down. The tool can verify our markup, our page speed, and our content structure from the crawl. It cannot verify that anyone else considers this site worth citing, and 48 is its way of saying there is no external evidence yet.

## The 5/100 that mattered more than the 76.6

v2.3.1 added a Backlinks specialist. Ours found five referring domains, traced all five to a single spam network, and counted zero legitimate links in the site's first five months. The category is unweighted in the aggregate, so the 76.6 barely moved. We think that weighting choice is wrong for a site our age, because it let the headline number bury the most consequential finding in the report.

Five months live and zero real links is a distribution problem, not a technical SEO problem. No amount of schema repair fixes it. The aggregate had been flattering us for a month, and the one number that got no weight was the one we keep thinking about.

## v2.2.6 through v2.3.1: fixes self-hosters should read

Between our August and September audits the project shipped three releases of security work. If you run audits on a cloud VM, some of these were credential-theft paths, not theoretical bugs.

| Version | Change | Why it matters |
|---|---|---|
| v2.2.6 | Path traversal fixed in the `commoncrawl_graph.py` cache filename | A crafted Common Crawl URL could write files outside the cache directory |
| v2.2.6 | Unvalidated WHOIS referral fixed in `domain_history.py` | The audit followed referral URLs to attacker-chosen hosts |
| v2.2.6 | RFC 6598 range (100.64.0.0/10) now refused | Closes the Alibaba Cloud metadata endpoint; 169.254.169.254 was not the only metadata IP in play |
| v2.2.6 | Requires WeasyPrint 70.0+ and requests 2.34.2+ | Both dependencies carry their own security fixes |
| v2.3.0 | Configured HTTP proxy validated against the hostname blocklist | Before this, `HTTPS_PROXY=http://169.254.169.254:3128` turned every outbound audit request into a cloud-metadata read |
| v2.3.0 | `CLAUDE_SEO_LOCAL_TARGETS` allowlist | Explicit opt-in for auditing localhost and staging hosts |
| v2.3.0 | 13 community PRs merged | Outside security review is getting taken seriously |
| v2.3.1 | Five judgment-heavy agents moved to Opus | Grading consistency where the rubric asks for judgment instead of arithmetic |
| v2.3.1 | Keywords Everywhere (Open PageRank) as free backlinks fallback | The Backlinks specialist now works without paid API keys |

The proxy fix is the one to underline. Before v2.3.0, if that environment variable pointed at a hostile value on the machine where you audit, the tool itself became the SSRF payload. Update before the next run, not after.

## What we fixed on our own site within a day

The September 16 report produced four changes we shipped inside 24 hours.

1. Our tool pages emitted AggregateRating schema with `reviewCount: 0`. Star ratings with no reviews behind them are a manual-action risk under Google's structured data policy. The template now gates that markup so it cannot ship again.

2. Our Semrush review contained a paragraph describing hands-on use of Semrush. We have never run it. The audit flagged the claim as unsupported, we deleted the paragraph, and the review now states what we did and did not test. This is the second time the grader caught something our own editorial pass missed, and the first time what it caught was a fabrication. Publishing that admission is the point of this site.

3. Seventy-six pages rendered large numbers as "150, 000", with a stray space after the comma. A locale artifact in the generator, fixed at the source.

4. We dropped self-serving Review schema from our own pages. Marking up our directory's reviews as if they were third-party endorsements is the kind of thing Google's guidelines name explicitly.

## Who should run this tool

::: verdict warn
Run [Claude SEO](/tools/claude-seo/) if you want a prioritized, evidence-linked audit and can treat each grader version as a new baseline. Pin your comparisons: re-run within one version to measure your fixes, and when the tool upgrades, do not diff the new score against the old one. Read the unweighted specialists, since the aggregate buried our worst number for a month. Skip it if you need a single score that stays comparable across quarters; that is a job for a deterministic crawler with fixed rules, not a judgment grader.
:::

Five audits in, the pattern is consistent: the findings keep giving us work we act on, and the score keeps being the least dependable part of the report.

One sourcing note. Every score in this post comes from an audit we ran against our own production site, and the category and E-E-A-T figures are from the saved September 16 v2.3.1 report.
