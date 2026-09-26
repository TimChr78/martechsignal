---
title: "Where open-source martech momentum actually lives"
seo_title: "Open-source martech momentum: the agent-skills layer wins"
slug: oss-momentum-tracker-september-2026
date: 2026-09-26
author: Tim Christensen
tags: [Open Source, Data, GitHub]
categories: [agent-skills]
---
The fastest-accumulating open-source projects in our catalog are not platforms. They are packs of agent skills, and the gap is widening.

We track 79 active open-source tools in the [directory](/tools/). Sixteen of them name a public GitHub repository, and those sixteen now have a [published momentum dataset](/oss-momentum.json) behind them. Every number below is a snapshot or a snapshot-bounded delta as of 26 September 2026. Nothing is estimated.

## The top of the board

[claude-ads](/tools/claude-ads/) leads with 9,576 stars and 1,857 of them arrived in the last 57 days. [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/) is the sharper curve: 2,635 stars total, 1,577 of them inside a 40-day window. [ai-marketing-claude](/tools/ai-marketing-claude/) added 442 over 57 days to reach 2,684, and [aaron-marketing-skills](/tools/aaron-marketing-skills/) added 361 to reach 2,843.

Read those four together and the shape is hard to miss. All four are agent skill repositories: collections of instructions, prompts, and small tools that teach a coding or marketing agent to run campaigns, audit accounts, or interpret ad data. None of them is a platform you deploy. They are the layer you install into an agent you already run.

## The rest is quiet

The remaining projects in the tracked set moved slowly or not at all. Several sat within a few dozen stars of their earlier snapshot across the full window. One went backwards: [openclaw-marketing-skills](/tools/openclaw-marketing-skills/) dropped 30 stars over 57 days, from 1,075 to 1,045. Un-starring is real data, so it stays in the tracker.

That contrast is the finding. The platform layer of open-source martech, tools that store contacts, send campaigns, or analyze traffic, is where the durable value lives. It is not where the attention flows. In 2026 the adoption wave shows up as agent capability first.

## What we publish and how

The [dataset](/oss-momentum.json) gives, per repository: current stars, latest release date, a per-row growth figure with its own window, and the full snapshot history we measured. Two real sources back it. GitHub's repository API provided the fresh totals and release dates. The measurement series comes from the [git history of our own public catalog](https://github.com/TimChr78/martechsignal): every committed snapshot of the tools file, dated by its commit. Anyone can rerun that extraction and get the same series.

Two limits, stated plainly. GitHub's star-timestamp endpoints are not accessible to this project, so growth windows are bounded by our snapshot dates and each row says which window it covers. And only repositories named in a catalog entry are tracked; 63 open-source entries do not record a repository URL and sit outside the dataset rather than being guessed at.

We will refresh the tracker as the catalog snapshots accumulate. If a project in your stack is missing its repository URL, that is a fix worth sending us through the [contact page](/contact/).
