---
title: "The guardrails Google won't ship for your AI ad account"
seo_title: "AI ad account guardrails Google won't ship"
slug: google-ads-ai-guardrails
date: 2026-09-24
author: Tim Christensen
tags: [Google Ads, AI, Automation, Advertising]
categories: [advertising]
---

Google ships AI ad automation faster than its safety reporting, so the guardrails for an AI-managed account are still something you build yourself. Two pieces of practitioner advice landed in the same week to prove it, from opposite ends of the industry. On the PPC Live podcast, Mike Ryan of Smarter Ecommerce walked through what happens when AI Max meets an account nobody has fenced in. On MarTech, Optmyzr published a three-layer safety model for agents touching live ad budgets. Meanwhile Google itself spent the same stretch expanding AI Brief to seven more languages and promising a unified AI Max reporting view sometime later in 2026.

We made this argument in August when [Google handed your ad budget to AI agents and kept you on the hook](/blog/google-ad-agents-control-gap/). A month later the control gap hasn't closed. It has gotten more specific, which is progress of a sort. Practitioners are now describing what the control layer actually contains.

## Ryan's expensive lesson: the model doesn't know your truces

Ryan's clearest story is also his most uncomfortable one. AI Max dramatically expanded a client's traffic by matching onto a much larger competitor's searches. Performance metrics looked good. The advertiser had deliberately avoided that competitor for years to prevent a bidding war. The algorithm found the war, started it, and had no way to know it was forbidden ground.

That is the core failure mode of automated ad buying, and no model update fixes it, because the missing information never existed in the account. Business context lives in someone's head or in a strategy doc the bidder can't see. Ryan's countermeasure is unglamorous: trust but verify, meaning you read the search terms report from day one instead of assuming strong headline numbers mean everything underneath is healthy.

He also applied the guardrail to himself. After seeing several campaigns where AI Max appeared to favor the Search Partner Network, he posted the observation on LinkedIn. More data later showed it wasn't generally true, and he said so publicly. His point about that correction matters for anyone running AI-managed accounts: the original claim traveled further than the retraction, and advertisers had already made decisions based on it. Early observations from a few campaigns are not findings. Google's own guidance after the August 17 Smart Bidding change was to wait one to two conversion cycles, and most of the loud takes that week came before the first cycle finished.

::: callout
Ryan's research threshold for whether a campaign can support automated bidding at all: at least 30 conversions a month, ideally 60 or more. Below that floor, your structure is starving the algorithm you're blaming. He described one account carved into granular margin buckets by its CFO, each with its own ROAS target, sophisticated on a spreadsheet and too fragmented for Smart Bidding to hit any of the targets.
:::

## Optmyzr's three layers, minus the sales pitch

The Optmyzr piece is sponsored content and ends in a product pitch, so treat the vendor claims accordingly. The framework itself is sound and worth separating from the funnel.

Layer one is grounding. An agent connected to a thin data slice will answer your question fluently and confidently, based on the third of the account it can actually see. Every gap in visibility is a place it will invent, in the same tone as everything true it says. Their list of what a serious data layer needs includes full GAQL query access, GA4 alongside the ads data, complete change history across every actor, and negative keywords consolidated across all four levels where they actually live.

Layer two is the one most teams skip: policies that live on the account, not in the prompt. Their phrasing is the sharpest thing published on this topic all month. A rule that lives in the prompt is a rule the model can be talked out of, by a clever user, by an instruction hidden in a document it was asked to read, or by its own drift over a long session. A rule that lives on the account holds under every path in. No bid increase above 10% in one move. No budget change past a threshold. These campaigns don't get touched. No competitor brand terms added. And the override is deliberate and signed, because an override you can hit without noticing is a speed bump made of paint.

Layer three is a human review step with a real queue: every write becomes a change request, policies stamp a verdict on each row, a named person previews the exact deterministic change before it goes live. The side benefit is an audit trail. When a client asks in November why their target CPA moved in March, you have the proposal, the rationale, and the approver instead of a chat transcript.

## The checklist: lock, monitor, never delegate

Combining both sources with what Google actually ships today, here is the working guardrail set for an AI-managed account.

**Lock it structurally, in account settings, not in instructions:**

- Negative keyword lists maintained across all four levels, reviewed before any AI expansion feature is switched on
- Brand exclusions in AI Max, plus explicit competitor terms you have chosen not to bid on, with the reason written down where a successor can find it
- Search Partner Network settings chosen deliberately rather than inherited
- Bid and budget change limits, enforced by a script or rules engine that validates what the automation did before it sticks
- A do-not-touch campaign list for anything carrying business context the algorithm can't see

**Monitor it weekly, from day one of any AI feature:**

- Search terms report, the whole point of trust but verify
- AI Max match type and match source reporting, which shows exactly where expansion traffic comes from
- Change history across every actor: UI edits, scripts, third-party tools
- Conversion volume per campaign against Ryan's 30-a-month floor, because a campaign below it can't support the bidding strategy you assigned
- Custom labels carrying margin and return-rate data, the cheapest way to feed business context into optimization

**Never delegate:**

- Entering new competitive territory. The bidding war decision is a business decision.
- Account structure changes. Consolidation and segmentation determine whether the algorithm has enough data to work.
- Reactive target changes during platform rollouts. The August 17 panic, advertisers raising tROAS on campaigns that weren't even budget-limited, mostly handed share to whoever stayed calm.
- Final approval on any write. Reviewing change history afterward is not being in the loop.

## The trajectory problem

Here is the uncomfortable contrast. On September 23, Google expanded AI Brief, its written-instructions channel for AI Max, and described a future unified report connecting search term, creative, and landing page for AI-driven interactions. The reporting has no launch date beyond "later in 2026." The automation is live now.

::: verdict warn
Google's pattern is consistent: automation ships as the default, visibility arrives as the follow-up, and the guardrail layer is either DIY or a vendor product. AI Brief is itself a prompt-level control, which means it's exactly the kind of rule Optmyzr warns can be diluted or drifted. Useful for context, not sufficient as a fence.
:::

So the practical answer to "should we trust Google's AI?" is the wrong question, as Optmyzr argues and Ryan's career this month demonstrates. The right questions are what the system can see, what it is structurally prevented from doing, and who signs off before money moves. Two of those three answers don't exist until you build them.

If you're wiring your own agent into ad accounts rather than using the platform's, the same checklist applies with one addition: your data layer decides your agent's honesty. A thin MCP connection to Google Ads produces confident garbage the same way a thin report always has. We broke down what a full ads-plus-GA4 connection looks like in [the Google/Meta/GA4 MCP review](/tools/google-meta-ads-ga4-mcp/), and the broader control problem in [our August teardown](/blog/google-ad-agents-control-gap/). More advertising ops coverage lives under [the advertising category](/categories/advertising/).

The boring setup wins. You know what the AI can see, you know what it can't touch, and nothing reaches the account without a human confirming it. The excitement belongs in the search terms report, not in wondering what your budget did while you were at lunch.
