---
title: "SQREEM is betting the behavioral model beats the LLM: if it's right, your AI media budget bought the wrong thing"
seo_description: "SQREEM claims a state-space behavioral model beats LLMs at predicting buyers. The evidence is vendor-grade, but the gap is real."
seo_title: "SQREEM's bet: behavior beats language"
slug: sqreem-behavioral-model-vs-llm
date: 2026-10-02
author: Tim Christensen
tags: [AI, Advertising, Analytics, Predictive]
categories: [advertising, analytics]
excerpt: SQREEM says a state-space behavioral model predicts buyers better than LLMs. The evidence is vendor-grade, but the psychology gap it exploits is real.
---

On September 23, 2026, the behavioral intelligence company SQREEM appointed Stephen Yap as CEO and handed him a contrarian pitch to sell: the company's Large Behavioral Model, a predictive engine built on state-space mathematics rather than machine learning, is the engine marketers should actually trust. [AdExchanger reported the story under a title that doubles as the thesis](https://www.adexchanger.com/ai/sqreem-touts-the-large-behavioral-model-not-the-llm-as-the-winning-predictive-engine/): "SQREEM Touts The Large Behavioral Model – Not The LLM – As The Winning Predictive Engine."

The technical claims are interesting and, for now, unverifiable from the outside. The reason the pitch will land anyway is much better documented, and it says something uncomfortable about how AI marketing budgets get spent.

## What SQREEM actually claims

The Large Behavioral Model (LBM) runs on state-space models, which AdExchanger describes as mathematical models that track how a set of variables changes over time. Founder René Raiss framed the difference as input choice: the platform ignores "what is written or what people say" because "we're interested in what they do."

The examples in the piece are all behavior chains. People who buy travel insurance purchase green tea 22% more often than the average person, according to Raiss, and the model walks a search journey from green tea to antioxidants to skin care to sunscreen to vacation to travel insurance. The company says the system auto-generates audience personas from these correlations, using real-time social platform data, open-web data, and open-web traffic that Raiss says cannot be traced back to an individual.

One footnote matters. The "no machine learning" framing has an asterisk: AdExchanger notes LBMs can contain machine learning or LLMs as components, though neither is innate to the architecture. The claim is more "a different core" than "a clean room."

## Why the pitch will land regardless of the math

[HubSpot](/tools/hubspot-crm/) published a piece on September 21 by Phill Agnew about why AI products show their working. Anthropic [gives three official reasons](https://www.anthropic.com/news/visible-extended-thinking) for visible reasoning, and the third is, in the company's own words, that it's interesting to watch. Agnew argues there's a fourth reason vendors won't put on a slide: visible effort makes output feel more valuable.

The evidence he cites is the labor-illusion literature. In a 2011 study in Management Science, 266 participants used a travel search site. One group saw a blank loading wheel. The other watched airlines being searched and fares stacking up in real time. The transparent version was rated 8.1% higher in perceived value, and people preferred it even when it took 50 seconds longer to return the same results. A 2022 follow-up in Information and Management repeated the test with 306 car-search users and 294 dating-app users: seven seconds of a "calculating results" spinner made identical recommendations rate as significantly higher quality.

Now apply that to a predictive-audience pitch. Both an LLM and an LBM can walk a marketer through why an audience looks promising. Both produce a fluent story. The buyer has no practical way to check the underlying probabilities, so the demo rewards whichever story sounds smarter. The industry is choosing its prediction engines the way those travel-site users chose results, by watching the loader spin.

::: callout
**The demo is the product until a benchmark shows up.** An LLM pitch and an LBM pitch look identical in the room: a confident walkthrough, a persona materializing on screen, a tidy story about why this audience converts. The labor-illusion studies say the show alone raises perceived value even when the underlying results are identical. Fluency is the one signal both model classes can fake, so it is the one signal worth discounting.
:::

## The part of your budget this touches

The execution layer of paid media is already agentic. We covered how [Google handed campaign controls to AI agents](/blog/google-ad-agents-control-gap/), and how [OpenAI is building agents that spend ad money without a human in the loop](/blog/openai-agent-ads-spending-without-you/). Into that world, SQREEM's bet puts the value upstream of the executing agent, in the model that prices the audience. Execution is plumbing. Prediction decides where the money goes, and plumbing is cheap to swap once the prediction exists.

The builder community is converging on the same stack from the other side. A developer posting in r/MarketingAutomation on September 22, 2026 described an "AI OS" for digital marketing agencies where agents manage Google and Meta ads end to end. The thread collected one upvote and one comment, which asked where the system sits between generating reports and autonomously pausing creatives and adjusting bids. The builder's full answer: "Complete end to end." A small sample, and an honest answer. The plumbing is being built whether or not anyone has solved prediction. Tools like [Claude Ads](/tools/claude-ads/), a paid-media operations skill for Claude Code, and an [MCP server for Google Ads, Meta Ads, and GA4](/tools/google-meta-ads-ga4-mcp/) that lets an assistant manage all three from one conversation, are the same layer aimed at smaller teams.

There's also an older argument hiding inside SQREEM's pitch. Multi-touch attribution sold marketers a story about click paths, and the story never survived contact with how people actually buy ([our take](/blog/multi-touch-attribution-was-always-a-fiction/)). "Watch behavior, not words" is that same instinct arriving as a product category. The instinct is sound. The risk is the repeat: the last behavioral model the industry bought turned out to be a fiction with a dashboard.

## What would have to be true

<table class="cmp">
<tr><th></th><th>The demo answers</th><th>The budget answers</th></tr>
<tr>
  <td><strong>Core question</strong></td>
  <td class="com-price">Does the story sound smart?</td>
  <td class="oss-price">Does it predict the next purchase?</td>
</tr>
<tr>
  <td><strong>What gets optimized</strong></td>
  <td class="com-price">The explanation</td>
  <td class="oss-price">Incremental lift</td>
</tr>
<tr>
  <td><strong>Proof it can fake</strong></td>
  <td class="com-price">Fluency</td>
  <td class="oss-price">None</td>
</tr>
<tr>
  <td><strong>Where the evidence lives</strong></td>
  <td class="com-price">Vendor decks and walkthroughs</td>
  <td class="oss-price">A holdout on your own spend</td>
</tr>
</table>

If SQREEM is right, the money flowing into LLM-based marketing agents is aimed one layer too low: summarizing and executing instead of predicting. If SQREEM is wrong, the LBM is a rebrand of audience modeling with better timing. Both can be checked, but only with data the vendor has to release or the buyer has to generate.

::: verdict loss
<div class="verdict-label">Verdict: credible critique, unproven engine, no reason to move budget yet</div>

<p>SQREEM's critique of LLM-based prediction holds up: a language model learns from what people write, and purchase behavior is not writing. But every number in the pitch, the 22% green-tea lift included, traces back to the vendor. There is no published benchmark, no public pricing, and no third-party test to date. The honest response to a claim this big is the boring one: run a holdout on your own spend, or wait for someone else's, before any budget moves.</p>
:::

**Sources:** [AdExchanger: "SQREEM Touts The Large Behavioral Model – Not The LLM – As The Winning Predictive Engine" by Joanna Gerber, September 23, 2026](https://www.adexchanger.com/ai/sqreem-touts-the-large-behavioral-model-not-the-llm-as-the-winning-predictive-engine/) · [HubSpot Blog: "The psychology behind why AI shows it's working" by Phill Agnew, updated September 21, 2026](https://blog.hubspot.com/marketing/why-ai-shows-loadtime) · [r/MarketingAutomation: "i am building ai os for digital marketing agency where ai agents can manage google ads meta ads clients and automate workflows", September 22, 2026](https://www.reddit.com/r/MarketingAutomation/comments/1wn3pxy/i_am_building_ai_os_for_digital_marketing_agency/)

Tools linked in this post: [HubSpot CRM](/tools/hubspot-crm/) · [Claude Ads](/tools/claude-ads/) · [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/)
