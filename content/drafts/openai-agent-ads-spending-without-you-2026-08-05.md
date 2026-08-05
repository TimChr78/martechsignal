---
title: "OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You."
slug: openai-agent-ads-spending-without-you
date: 2026-08-05
author: MartechSignal
tags: [AI, Advertising, Agents, OpenAI]
---

When news broke last week that OpenAI is testing a new ad format in ChatGPT, much of the industry took one look and restarted the banner ad debate. Will ChatGPT show display ads? How intrusive will they be? Will they poison the answers?

Those are fair questions aimed at the wrong thing.

The format spotted inside ChatGPT Ads Manager does not send anyone to a webpage. The click does not open a landing page. It opens a conversation with an AI agent that works for the advertiser: answering questions, surfacing products, capturing leads. The person who clicked may never see a website at all.

That is not display advertising with extra steps. It is a different product wearing the ad label because that is the only category everyone currently understands.

## What's actually in ChatGPT Ads Manager

Search Engine Land's Anu Adegbola broke the story on July 31, after entrepreneur Juozas Kaziukėnas spotted the new ad type option and shared it on LinkedIn. The capability is live for a limited group of advertisers, and based on coverage from Search Engine Land and MarTech, the workflow has three parts:

- **Business profiling.** ChatGPT crawls the advertiser's website and auto-generates a business profile: common customer questions, support information, general context about the business.
- **Business agent creation.** The advertiser configures an agent on top of that profile with custom instructions, then connects it to product feeds, live business data via Model Context Protocol (MCP) tools, and custom lead-generation forms.
- **Agent-powered campaigns.** Campaigns point users straight into a conversation with the business agent instead of a URL. The conversation is the destination.

The underlying technology appears to be the same foundation that powers Custom GPTs, per MarTech.

One honest caveat before anyone rewrites their media plan: OpenAI has not announced this format publicly, and the end-user experience has not been widely observed. Nobody outside the test group knows exactly how these ads will appear inside ChatGPT. What is visible today is infrastructure, and companies build infrastructure when they intend to ship.

## The click survives. The human becomes optional.

Digital advertising has run one loop for decades: an ad generates a click, and the click opens a webpage. Every layer of the programmatic stack exists to serve that loop. The demand-side platform, the supply-side platform, the exchange, the viewability vendor: all of it routes a human eyeball toward a human decision and takes a toll for the trip.

OpenAI's prototype quietly drops the requirement that a human be at the receiving end. And it is not the only signal moving in that direction.

## IAB Tech Lab is writing the plumbing for agent-to-agent ads

On July 30, one day before the OpenAI story broke, IAB Tech Lab released version 2.3 of AAMP, its Agentic Advertising Management Protocols. Read the release notes and the ambition is hard to miss: this is governance for a world where AI agents plan, buy, negotiate, and commit ad spend.

AAMP 2.3 adds enterprise deployment options, privacy controls, platform integrations, and standardized workflows. The headline integrations are Amazon Bedrock AgentCore, Meta buying, and Google Ad Manager reporting. Privacy checks from the IAB Diligence Platform and SafeGuard Privacy are now built into buyer workflows, along with pricing guardrails meant to make automated transactions verifiable. Open-source contributions from HyperMindz and Mixpeek extend deal management and content classification.

As MarTech put it: "The question is no longer whether AI agents can automate advertising tasks. It's whether they can do it reliably enough for enterprise organizations to trust them with real budgets."

AAMP itself stands on three pillars, and each one targets a piece of the stack you already run:

- **Agentic Foundations.** ARTF, the Agentic Real Time Framework, defines how agent services operate inside real-time bidding environments. IAB Tech Lab claims it cuts latency by 80%, with an MCP interface built into the spec.
- **Agentic Protocols.** The schemas and SDKs that let buyer and seller agents discover each other, negotiate, and transact. Agentic Direct automates direct deals on top of the OpenDirect standard. The Deals API handles programmatic guaranteed and private marketplace deals with SSPs and DSPs. OpenRTB and AdCOM cover open bidding. Buyer and Seller Agent SDKs are open source on GitHub today.
- **Trust and Transparency.** An Agent Registry, free for members and non-members, that establishes identity and verification so participants know who or what they are transacting with.

The whole thing is built on top of Anthropic's MCP and Google's agent-to-agent protocol, wrapped around the standards the industry already runs on. IAB Tech Lab's COO has demoed the loop end to end: an agent takes a brief, builds a media plan, negotiates with a seller agent, confirms the transaction, and pushes it to Google Ad Manager. No human touched the deal between the brief and the insertion order.

## Two commerce flows, side by side

Here is the loop digital advertising has run since the 1990s:

<div class="flow-strip">
  <div class="flow-step"><span class="flow-label">AD SERVER</span><span class="flow-sub">creative + targeting</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">EXCHANGE / SSP</span><span class="flow-sub">auction</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">DSP</span><span class="flow-sub">bid decision</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">IMPRESSION</span><span class="flow-sub">a human sees the ad</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">CLICK</span><span class="flow-sub">a human decides</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step"><span class="flow-label">LANDING PAGE</span><span class="flow-sub">a human converts, maybe</span></div>
</div>

And here is the loop OpenAI's prototype and AAMP both point toward:

<div class="flow-strip">
  <div class="flow-step"><span class="flow-label">YOUR FEED + MCP</span><span class="flow-sub">structured catalog, live data</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step ai"><span class="flow-label">BUYER'S AGENT</span><span class="flow-sub">reads attributes, compares</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step ai"><span class="flow-label">YOUR SELLER AGENT</span><span class="flow-sub">negotiates via AAMP</span></div>
  <div class="flow-wire"><span class="flow-pulse"></span></div>
  <div class="flow-step ok"><span class="flow-label">TRANSACTION</span><span class="flow-sub">no human in the loop</span></div>
</div>

The second flow has no impression and nothing to persuade. It is a data exchange followed by a transaction. The ad impression was always a workaround for the absence of a machine buyer, and a machine buyer now exists.

<table class="cmp">
<tr><th></th><th>Traditional programmatic</th><th>Agent-to-agent commerce</th></tr>
<tr><td><strong>Who sees the ad</strong></td><td>A person</td><td>An agent, or nobody</td></tr>
<tr><td><strong>What the click opens</strong></td><td>A webpage</td><td>A conversation, or nothing</td></tr>
<tr><td><strong>What gets optimized</strong></td><td>Attention, CTR, viewability</td><td>Feed completeness, price, availability</td></tr>
<tr><td><strong>Who negotiates</strong></td><td>Humans through DSPs and SSPs</td><td>Agents through AAMP</td></tr>
<tr><td><strong>Where fraud lives</strong></td><td>Fake impressions and clicks</td><td>Unverified agents</td></tr>
</table>

::: verdict lose
**❌ Who loses: the martech middle**
The margin in the middle layer of the ad stack is a fee for human latency. Someone has to find the audience, judge the context, place the bid, verify the view. Buyer and seller agents transacting through the Deals API or Agentic Direct do all of that in milliseconds, and AAMP's reference flows show them working both through SSPs and DSPs and around them. The intermediaries that survive this will be execution pipes, not decision brokers. If your product's pitch starts with "we help media buyers," you should be paying very close attention.
:::

## Agents don't read your website. They read your feed.

The shopping data makes the same point from the other direction. In a March 2026 study, Tom Wells examined where ChatGPT's product carousels actually come from. Out of more than 43,000 products, 83% matched Google's top 40 organic Shopping results. The products AI shoppers see are not pulled from your product pages, your reviews, or the open web. They come from a single file most brands have not touched since they set up paid Shopping: the Google Merchant Center feed.

Profound reviewed more than 1 million ChatGPT shopping offers in June and found something sharper: of the product citations pulled directly from merchant feeds, about 99.9% appeared as the top product offer. Feed-sourced retrievals grew from 4.3% to roughly 20% of all ChatGPT shopping retrievals in six weeks. The reason is completeness. Feed-sourced offers carried brand, product image, and merchant details 100% of the time, versus 0% for page-scraped offers, and they earned ChatGPT's "best price" tag 100% of the time versus 21%.

The nuance matters, because the feed does not replace the page yet. Profound's analysis found that about 88% of ChatGPT product offers still come from web product detail pages, and even for merchants using feeds, around 76% of offers still came from the page. The feed decides whether you are in the selection and where you rank. The page is still where shoppers get convinced.

But the direction is clear, and the platforms are building for it. OpenAI says its product results are ranked by relevance signals like availability, price, quality, and whether a merchant is the primary seller. Those signals come from catalogs that now include Target, Sephora, Nordstrom, Best Buy, The Home Depot, and millions of Shopify merchants. At Google Marketing Live 2026, Google added conversational attributes to the Merchant Center spec for exactly this: structured Q&A pairs, related product fields like `often_bought_with` and `substitute`, document links for manuals and spec sheets, variant options, and a popularity rank so a model can answer "what's your best-selling running shoe?"

::: verdict win
**✅ Who wins: whoever owns the feed**
Your Merchant Center feed is now doing the job your landing page, ad creative, and sales pitch used to split between them, inside one structured file. Adobe's Q2 AI Traffic report scored product detail pages at just 63.5 for AI citation readability, well below homepages and buying guides. The pages holding the product data are the hardest for machines to read, and the feed is the bypass around them.
:::

## What marketing ops should do now

If the buyer side of your business is gradually becoming an agent, the work starts with the surfaces agents actually read:

- **Fix the feed before anything else.** Check Merchant Center diagnostics, fix GTIN errors and price mismatches. A disapproved product does not rank lower for AI agents. It does not exist for them.
- **Keep price and availability synced continuously.** AI shopping surfaces refresh constantly. A feed that updates once a day is already behind, and stale availability gets your products recommended, then refunded.
- **Add conversational attributes to your top SKUs.** Q&A pairs, related products, popularity rank. Start with the products that already generate revenue. You do not need to touch all 40,000 items this quarter.
- **Make pricing machine-readable.** Previsible analyzed 6.77 million AI-referred sessions and found that "contact us for pricing" gives an AI nothing to compare and nothing to recommend. In an agent-mediated market, opacity is the same as absence.
- **Expose live data over MCP.** OpenAI's agent ad format connects business agents to live data through MCP tools. If you want to exist inside that conversation, your systems need an interface an agent can call.
- **Watch for agent traffic and register your own agents.** The IAB Tech Lab Agent Registry is free. When agent buyers start showing up in your logs, you will want to know who you are transacting with, and your own agents will need verifiable identity to be trusted on the other side.

The business case is not hypothetical. Adobe found that traffic from AI sources to US retail sites grew 393% year over year in the first quarter, and by December it was up more than 1,150%. By March, AI-referred traffic converted 42% better than non-AI traffic. Salesforce tied about 20% of global online holiday sales, roughly $262 billion, to AI and agents. That traffic still arrives as sessions today. The next wave will not arrive as anything you can see in Analytics at all.

## The verdict

OpenAI insists its ads do not influence ChatGPT's answers, that conversations stay private from advertisers, and that advertisers only receive aggregate performance data. The public pilot that began in February, now expanding from the US to nine countries including the UK, Japan, and Brazil, is a labeled sponsored listing that behaves a lot like traditional advertising. All of that is real, and it is worth holding OpenAI to.

But the agent format sitting in Ads Manager and the AAMP standards maturing one layer down are the same bet placed from two directions: the future customer of your advertising is not always going to be a person. Marketing ops spent twenty years optimizing for human attention. The next decade belongs to whoever learns to market to the thing reading over the human's shoulder.

Start with the feed. Both futures already run through it, and it is the cheapest thing on this list to fix.

<div class="cta-strip">
<h3>The agent-era stack, cataloged</h3>
<p>Feed management, MCP servers, and the automation engines that keep you visible when the buyer stops being human. All in our directory with pricing and AI feature breakdowns.</p>
<a class="btn" href="/tools/">BROWSE THE TOOL DIRECTORY →</a>
</div>

**Sources:** [Search Engine Land on OpenAI's chatbot-native ads](https://searchengineland.com/openai-appears-to-be-building-chatbot-native-ads-that-launch-ai-agents-484107) · [MarTech on the OpenAI ad experiment](https://martech.org/openai-ad-experiment-could-change-what-happens-after-the-click/) · [OpenAI: Testing ads in ChatGPT](https://openai.com/index/testing-ads-in-chatgpt/) · [MarTech on IAB Tech Lab AAMP 2.3](https://martech.org/iab-tech-lab-gets-ai-agents-ready-for-real-advertising/) · [IAB Tech Lab: AAMP](https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/) · [Search Engine Land on AI shopping and product feeds](https://searchengineland.com/ai-shopping-product-feed-page-484060)
