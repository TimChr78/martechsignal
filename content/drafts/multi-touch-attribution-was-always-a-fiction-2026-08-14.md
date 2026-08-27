---
title: "Multi-Touch Attribution Was Always a Fiction"
seo_title: "Multi-Touch Attribution Was Always a Fiction"
slug: multi-touch-attribution-was-always-a-fiction
date: 2026-08-14
author: MartechSignal
tags: [Analytics, Attribution, AI, Privacy]
categories: [analytics]
---

On Sept. 2, the MarTech Conference runs a free session called "Marketing without signals: How to perform when the data disappears." The copy tells the story the industry has settled on. For years, marketing teams built their playbooks on an abundance of granular signals: clicks, third-party cookies, device identifiers, deterministic conversion paths. Privacy rules, platform walled gardens, and AI intermediaries ate all of it. Now teams have to learn to perform without the data.

It's a clean story. I don't buy it. Signal loss did not break marketing measurement. It made visible what multi-touch attribution never actually measured in the first place.

## The same conversion, six different truths

Search Engine Land ran a piece in July that should be pinned to every marketing ops Slack channel. Ann Robison walks through a single $100 conversion spread across four touchpoints: display, paid social, organic search, email. Then she runs it through the standard models.

First-touch gives display the entire $100. Last-touch gives display nothing and email everything. Linear splits it $25 each. Position-based hands $40 to the first and last touchpoints. Time-decay gives the most credit to whichever touchpoint sat closest to the purchase. Data-driven distributes it by each touchpoint's estimated contribution.

Six models, one conversion, six different answers. The same purchase is worth $100 to display or $0 to display, depending on which model you picked before the data arrived. That's not measurement. That's a policy choice wearing a lab coat. You decide in advance what you believe about the journey, and the model confirms it.

## The definition assumed the problem away

The standard definition of attribution, courtesy of Wikipedia, runs like this: identify the set of user actions that contributed to a desired outcome, then assign a value to each. Notice what it assumes: that you can see the actions. The entire discipline was built on a premise of full observability that never held.

The evidence against it was public the whole time. Wikipedia's own article on marketing attribution carries a section titled "Limitations and divergence from experimental results." Studies comparing MTA outputs to randomized experiments found substantial discrepancies, with attribution models systematically misallocating credit across channels. Because attribution models rest on observational correlations rather than experimental manipulation, they overestimate the causal impact of touchpoints that are merely associated with high-converting users. Selection bias does the dirty work: a touchpoint looks effective because it was shown to people already likely to convert. The Platform Incrementality Evaluation framework showed that attribution-based optimization allocates budget less efficiently than decisions guided by experimental lift.

This is not obscure academic trivia. It's on Wikipedia, and it has been for years. The people selling attribution software knew. The people buying it suspected. The industry kept paying for the number anyway.

## Why the theater survived

Pressure explains it. The 2025 CMO Survey found that 63% of marketing leaders report increased pressure from CFOs, up from 52% the year before, with CEO and board scrutiny rising alongside it. Attribution gave finance a number. It converted "we don't know what works" into "display is worth $30 of every $100." Ugly as that number was, it was a number, and it could go in a deck.

Attribution was answering a political question, not an empirical one: which channel gets the credit? Budget meetings need an answer, and the answer was whatever model you picked. Every vendor could produce one. Nobody got fired for a dashboard that flattered the platform that sold it.

## What signal loss actually exposed

The gap between buyer behavior and what marketing tools observe was always there. Journeys were always cross-device, partially offline, partially unlogged. MTA never measured the journey. It measured the trackable slice of the journey and extrapolated with confidence. The slice kept shrinking: browsers blocked the cookies, platforms walled off their data, and now AI assistants buy things on behalf of people without generating a single touchpoint you can see. MarTech's own copy concedes the point in one phrase. Instead of "chasing elusive multi-touch attribution models," teams are turning to high-probability modeling built on first-party signals.

Elusive. The house organ of the measurement category just told you the category was a chase.

## What to track instead

Which channel gets credit was never the useful question. The useful question was whether the marketing moved the outcome. That's incrementality, and it has a method: split the audience, expose one group, hold the other back, compare. The Search Engine Land example: the exposed group completes 1,000 purchases, the control completes 800. The campaign's lift is 200. An attribution model could claim all 1,000.

The same article carries the warning that matters for anyone still trusting platform reports: automated campaigns can increase the number of conversions credited to a campaign without increasing total sales. Platforms optimize toward credited conversions, not incremental ones. If your ROAS comes from a platform's own report, you are reading a scoreboard the platform built and operates.

Track the things that survive contact with reality:

- **Incrementality**, at whatever scale you can afford. Geo holdouts for the big channels, audience holdouts for the rest. A lift number is the only revenue claim worth defending in a budget cut.
- **Outcomes you can verify in your own systems.** Pipeline, revenue, retention, deal velocity. First-party, auditable, hard to argue with.
- **Decisions.** Salesforce's marketing blog put it plainly: data should do more than explain what happened, it should help you decide what to do next. A number that can't change a decision is decoration.
- **Attribution itself, demoted to directional.** One model, frozen, used to compare a channel against itself over time. Never as truth. High-probability modeling over first-party data, which is where the MarTech session lands, is at least honest about being an estimate.

::: verdict warn
**⚠️ The verdict: multi-touch attribution was always theater. Signal loss didn't break it, it exposed it.** The industry is mourning a measurement it never had, and the vendors are selling the mourning. The teams that come out of this era in good shape will be the ones that admit the number was never real and start tracking the two things that survive: whether the outcome happened, and whether marketing moved it.
:::

The honest objection is that incrementality is expensive and slow, and you can't run a holdout on every campaign. True. But that argues for treating attribution as a hypothesis generator, not an accounting system. Hypotheses get tested. Accounting gets trusted. The line between the two is where the signal loss actually drew blood.

The session's framing has it backwards. The data didn't disappear; it was never there in the form the dashboards claimed. The job now is to stop pretending otherwise and measure the two things that were always real: the outcome, and marketing's effect on it. The rest was a model's opinion dressed up as a measurement.

<div class="cta-strip">
<h3>Analytics and attribution tools, cataloged</h3>
<p>Attribution platforms, CDPs, and analytics tools with pricing and AI features compared side by side. Find the ones that measure outcomes instead of opinions.</p>
<a class="btn" href="/categories/analytics/">BROWSE ANALYTICS & ATTRIBUTION TOOLS →</a>
</div>

**Sources:** [MarTech: Marketing without signals: How to perform when the data disappears](https://martech.org/marketing-without-signals-how-to-perform-when-the-data-disappears/) · [Search Engine Land: Attribution vs. incrementality: Why you need both](https://searchengineland.com/attribution-vs-incrementality-both-483741) · [Wikipedia: Attribution (marketing)](https://en.wikipedia.org/wiki/Attribution_%28marketing%29) · [MarTech: What is marketing attribution? Models and best practices](https://martech.org/what-is-marketing-attribution/) · [Salesforce: Why Marketers Need to Move Beyond Attribution and Embrace Agentic Optimization](https://www.salesforce.com/blog/agentic-marketing-optimization/)
