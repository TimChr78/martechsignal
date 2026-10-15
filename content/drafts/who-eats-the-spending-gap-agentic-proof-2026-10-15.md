---
title: "Who eats the spending gap when agentic spend outpaces proof?"
seo_title: "Who eats the spending gap when agentic spend outpaces proof?"
slug: who-eats-the-spending-gap-agentic-proof
date: 2026-10-15
author: Tim Christensen
tags: [AI Agents, Measurement, Ad Tech]
categories: [analytics]
excerpt: "An agent can sit inside its budget, buy on clean signals, log every call, and still overspend. The proof gap has a dollar figure and an owner."
seo_description: "The proof gap: spend committed while evidence is still pending. Four mechanisms, a per-run metering ledger, and who owns the miss."
---

Last week this blog walked the [rogue agents debate](/blog/rogue-ai-agents-trust-debate/) to a flat conclusion: your agent did not go rogue, your configuration did what it was configured to allow. That sentence is comfortable for about a week. It says nothing about money. An agent can hold every permission correctly, buy on signals from sources you approved, act inside the authority you granted, and log every decision, and still spend too much. Nothing misbehaves. The evidence just arrives after the money.

Evgeny Popov put a number on that problem in an [October 7 AdExchanger column](https://www.adexchanger.com/data-driven-thinking/who-eats-the-spending-gap-when-agentic-spend-outpaces-proof-of-impact). He calls it the proof gap: spend committed while the evidence needed to assess a change is still pending. The rogue debate argued about intent. This is a measurement problem with a balance attached, which makes it more useful to anyone actually running agents.

## The arithmetic first

His example: a brand hands an agent $200,000 and lets it move $1,000 an hour into a new mix of CTV and retail media. The first sales readout fit to judge that change needs 48 hours to mature. By then, $48,000 has gone into a decision nobody has assessed, and the readout does not settle the $48,000 either. It produces an estimate, with error bars, about a change that is already two days old.

The two controls most stacks trust never enter that math. The budget caps total spend. Pacing caps the rate. Neither caps how much can ride on a single untested change while the test is open. An agent can keep both green and buy blind the whole time. This site argued in August that [stack budgets bleed when nobody meters them](/blog/martech-budget-bleeding-nobody-measuring/); subscriptions at least bleed at human speed. An agent bleeds by the hour.

### Pacing poses as validation

The first mechanism is the one above, stated as a failure mode. Green pacing with a pending readout is not control, it is spend with a clean complexion. Teams read "on budget, on pace" as "under management" because the dashboard has no column for money committed ahead of its evidence.

### The clock does not match the goal

A model reprices in milliseconds. A business outcome takes weeks to become real. Popov's point, which he developed in [an earlier column in the series](https://www.adexchanger.com/data-driven-thinking/why-agentic-measurement-will-reprice-the-ad-market/), is that faster measurement narrows the gap but never closes it. The 48-hour readout is not truth arriving late. It is a rough estimate arriving exactly on time, and treating it as a verdict is how teams talk themselves into scaling a guess.

### Changes compound faster than they can be isolated

An agent does not move one variable. It shifts bids, audiences, and channel mix at once, so the same weak guess ends up driving spend across several budgets, which is Popov's compounding point. When the readout finally lands, it prices the bundle, not the pieces. Anyone who has watched a multi-touch model hand credit to a channel it could not actually see knows how that story goes; [attribution precision was always partly a fiction](/blog/multi-touch-attribution-was-always-a-fiction/). The agent version is the same fiction at machine speed.

### The cap sits inside the objective

Popov's rule for any test allowance: a ceiling the agent is rewarded for reaching stops being a ceiling. If the agent is optimized for delivery and spend throughput, the allowance is a target with extra steps. The count also resets quietly when spend moves to a new channel or a second agent takes the handoff. Caps an agent can route around are pacing with better paperwork.

::: callout
**The number your stack does not have.** Marketing stacks measure spend and pacing beautifully. Almost none of them can answer a simpler question at any given hour: how many dollars are committed right now to changes whose evidence is still pending? Call that the proof-gap ledger. Until it exists, "in budget" and "under control" look identical on the dashboard and mean different things in the P&L.
:::

## A ledger that fits on one line per run

Popov's buying-side proposal is a risk budget: the most an agent may commit under an unvalidated change before it must show agreed evidence or obtain fresh approval. His worked example grants $12,000 to test a new mix, nothing more until the readout clears a threshold both sides set in advance. That policy converts into fields you can log on every agent run:

<table class="cmp">
<tr><th>Field</th><th>What it holds</th><th>What it catches</th></tr>
<tr><td><strong>change</strong></td><td>What moved: bids, audience, mix, budget</td><td>Bundles no readout can unbundle</td></tr>
<tr><td><strong>committed_pending</strong></td><td>Dollars spent on this change while its evidence window is open</td><td>The $48,000 figure, live instead of discovered after the fact</td></tr>
<tr><td><strong>evidence_standard</strong></td><td>Pixel event, causal estimate with stated uncertainty, or agent confidence, named before the first bid</td><td>A log entry getting praised as a verdict</td></tr>
<tr><td><strong>clock</strong></td><td>How long until this goal can honestly be read</td><td>48-hour gates on work built to pay back in months</td></tr>
<tr><td><strong>allowance</strong></td><td>The risk budget for this test, and who may raise it</td><td>Agents grading their own homework</td></tr>
<tr><td><strong>resets</strong></td><td>Channel moves or handoffs that would restart the count</td><td>Cap evasion by relay</td></tr>
<tr><td><strong>miss_owner</strong></td><td>Who eats a shortfall, by name or by clause</td><td>A gap that everyone owns, so nobody does</td></tr>
</table>

On the evidence standard, Popov is blunt: a pixel records an event, a sound causal test estimates how much the ads changed outcomes with stated uncertainty, and the agent's own confidence score is not independent validation.

The readouts come from your measurement layer. Attribution platforms such as [Northbeam](/tools/northbeam/) or [Triple Whale](/tools/triple-whale/) for ecommerce produce the sales-side estimates, and experiment tooling such as [PostHog](/tools/posthog/) runs the holdouts that produce causal reads with error bars. None of them keeps the ledger, and none should. The ledger is policy: an allowance and an evidence standard agreed before the first bid. Vendors can sell you the readout. The restraint has to be yours.

## Two instruments, routinely mistaken for one

The second half of the column is about who holds the losses. Markets that trade ahead of proof lean on two tools: a risk budget that limits what you commit while you learn, and a contract that assigns a defined loss to someone else when a defined part of the test goes wrong. Popov's warning is that the industry is about to treat them as one instrument. They are not.

<table class="cmp">
<tr><th></th><th>Risk budget</th><th>Underwritten guarantee</th></tr>
<tr><td><strong>Limits</strong></td><td>What you commit while you learn</td><td>What you lose when the test misses</td></tr>
<tr><td><strong>Set by</strong></td><td>The buyer, before the first bid</td><td>The contract, negotiated per condition</td></tr>
<tr><td><strong>Costs</strong></td><td class="oss-price">Nothing; it is restraint</td><td class="com-price">A fee, priced for the risk transferred</td></tr>
<tr><td><strong>Cash behind it</strong></td><td>None; the money is simply unspent</td><td>A funded counterparty balance sheet</td></tr>
</table>

The precedents he cites are already live. [Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html) has backed AI vendors' performance guarantees with a reinsurer's balance sheet since 2018. [TikTok](https://ads.tiktok.com/resources/help/article/about-roi-protection-for-gmv-max-campaigns?lang=en) hands eligible GMV Max campaigns ad credits when ROI falls below 90% of the daily target. One is third-party capital paid in cash. The other is the seller's own count, paid in credits, behind exclusions that include the day a campaign is paused. His summary line survives retelling: coverage does not validate the strategy. It changes who eats the miss.

## The ownership answer

Popov traces the family history to the early 1990s sequential liability fight, when the question was whether an agency owed the publisher before the brand had paid the agency. That was credit risk: who eats the loss if the money never arrives. The agentic version is proof risk: who eats the loss if the outcome never arrives. His closing split is clean. The standard of proof belongs in the test. The promise to pay belongs in the contract. The cash behind the promise belongs on someone's balance sheet.

For a marketing stack, the answer this year is unglamorous. The agent cannot validate itself, and the vendor's credits do not validate your strategy, so until a contract names a counting source and a funded remedy, the brand eats the gap by default, quietly, inside a pacing report that reads as success. Popov predicts that by the end of 2027 at least one media deal between independent firms will settle from escrow, with terms naming the source used to count results and a cash remedy for a counting error. I would take that bet at "at least one." The part that should nag a deployer is simpler: if that clause landed on your desk next quarter, your stack would have to produce the evidence it demands. Until it can, the ledger above is the whole job.

::: verdict loss
<div class="verdict-label">✗ Loser: the pacing dashboard as a governance instrument</div>
A pacing report answers one thing: whether spend is on schedule. It was never asked how much money was committed ahead of its own evidence, and it cannot say. An agent can hold budget and pace perfectly and still put $48,000 into an unassessed change in two days. Governance starts where the ledger starts: dollars committed while evidence is pending, an evidence standard fixed before the first bid, and a named owner for the miss. Budget compliance is none of those.
:::

*Sources: [AdExchanger, "Who Eats The Spending Gap When Agentic Spend Outpaces Proof Of Impact?", Evgeny Popov, October 7, 2026](https://www.adexchanger.com/data-driven-thinking/who-eats-the-spending-gap-when-agentic-spend-outpaces-proof-of-impact), [Popov on agentic measurement repricing the ad market](https://www.adexchanger.com/data-driven-thinking/why-agentic-measurement-will-reprice-the-ad-market/), [Munich Re insure:AI FAQ](https://www.munichre.com/en/solutions/for-industry-clients/insure-ai/faq.html), [TikTok ROI protection for GMV Max campaigns](https://ads.tiktok.com/resources/help/article/about-roi-protection-for-gmv-max-campaigns?lang=en). Every figure in this post traces to one of these pages, checked October 15, 2026.*

*Tools linked in this post:* [Northbeam](/tools/northbeam/) | [Triple Whale](/tools/triple-whale/) | [PostHog](/tools/posthog/)
