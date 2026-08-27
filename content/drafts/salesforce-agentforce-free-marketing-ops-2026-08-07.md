---
title: "Salesforce Made Agentforce Free. What Marketing Ops Can Build With It."
seo_title: "Agentforce Is Free: What Marketing Ops Can Build"
slug: salesforce-agentforce-free-marketing-ops
date: 2026-08-07
author: MartechSignal
tags: [Salesforce, AI Agents, Marketing Ops]
categories: [crm]
---
Salesforce spent the last two years selling Agentforce as an enterprise conversation, at enterprise prices. Then at the end of July it quietly changed the math. Salesforce Foundations, the free add-on bundled into existing Enterprise contracts, now includes Agentforce: 200,000 Flex credits, Prompt Builder, generative AI responses, and one agent skill, with no new line item on the invoice.

The catch arrives in the same sentence. "Free" here means free if you already pay for Salesforce Enterprise Edition or higher. If your org runs on Sales or Service Enterprise, Foundations is a free upgrade you can switch on from Setup this afternoon. If you're not a Salesforce customer at all, this post is entertainment, not an offer.

For the marketing ops people reading this from inside a Salesforce org, the interesting question isn't whether it's really free. It's what 200,000 credits actually buys, and which agent is worth building before the counter runs out.

## What you actually get for nothing

Salesforce published the bundle breakdown on July 30, and the marketing ops line items are the ones worth circling:

- **Agentforce**: 200,000 Flex credits, generative AI responses, Prompt Builder, one AI agent skill
- **Marketing**: drag-and-drop email builder, up to 2,000 email sends per month, built-in campaign analytics
- **Data**: unified customer profiles, segmentation across up to five data streams, 10,000 segmentation credits per year
- **Also in the box**: sales quoting, service case macros, one U.S.-only commerce storefront, and free trials of 25+ partner apps through AgentExchange (Docusign, RingCentral, ZoomInfo and friends)

::: callout
The honest framing: Salesforce handed existing Enterprise customers roughly $1,000 of agent runway and a small email engine, then called it an upgrade. That's a real budget for experimentation. It is not an unlimited one, and the word "free" is doing contract work in every headline this week.
:::

## The credit math, because it decides everything

Agentforce pricing runs on Flex credits since May 2025. One agent action consumes 20 credits, which Salesforce prices at $0.10 per action. Run the division on the free allotment:

- 200,000 credits / 20 per action = **10,000 actions**
- At list price that's about $1,000 of agent work
- When the credits run out, you buy more. There is no free refill.

Ten thousand actions sounds like a lot until you point an agent at something chatty. A lead-qualification agent that touches every inbound form fill will eat that in a quarter if your volume is real. A scoped internal tool, like a brief generator used twenty times a week, barely dents it. The free tier doesn't decide what you build. Your action budget does, so pick the use case before you open Agent Builder, not after.

## Build #1: A lead routing agent that earns its credits

This is the highest-leverage use of the free allotment because it replaces work someone is doing by hand right now.

::: wf-step
**The workflow.** Inbound lead lands in the CRM. The agent checks the fields that matter for routing: company size, region, product interest, whatever your scoring logic uses. It assigns an owner or queue, sets the priority, and posts to the right Slack channel. Humans handle the conversation; the agent handles the ten minutes of triage before it.
:::

Scope it hard. One agent skill is all Foundations includes, so this agent gets one job description. "Route and enrich inbound leads" is a job. "Manage our funnel" is a wish. The routing logic itself can live in flows the agent invokes, which keeps the agent's reasoning surface small and your credit burn predictable.

At 20 credits a pop, routing 500 leads a month costs 10,000 credits. The free pool covers ten months of that before anyone sees an invoice.

## Build #2: Campaign brief generator with Prompt Builder

Prompt Builder ships in the free bundle, which makes this the cheapest build on the list. No agent required, so no Flex credit burn on every use beyond the standard response costs.

::: wf-step
**The workflow.** A prompt template pulls live CRM fields into a draft brief: campaign name, target segment from your Data 360 streams, last campaign's performance, product notes. The marketing ops lead clicks, reads, edits, ships. The brief stops being a blank-page problem and becomes a review problem.
:::

Two rules make this useful instead of embarrassing. First, wire the template to real fields, not to vibes; a brief generated from empty merge fields reads like a ransom note assembled from a wiki. Second, keep a human as the last step. Salesforce's own small business content makes the same point in its human-AI collaboration material: people handle judgment and voice, the model handles the first draft. Nobody's campaign strategy ever survived an unedited LLM output, and this isn't the quarter to start trusting one.

## Build #3: Slack and MCP, where it gets genuinely interesting

At the end of July, Salesforce's architecture blog laid out three ways to connect Agentforce agents and Slackbot to external systems over MCP:

1. Connect an Agentforce agent to an external MCP server, when the agent needs CRM context and external context in one reasoning chain
2. Connect Slackbot directly to an external MCP server, for Slack-native tasks that don't need Salesforce at all
3. Route Slackbot through an Agentforce agent's subagents, when you want the agent's logic and the connection it already has

::: wf-step
**The marketing ops version.** Your team lives in Slack. Slackbot's MCP client is now generally available, with 20+ partner apps live in the Slack Marketplace registry: Notion, Atlassian, Box, Canva, Docusign, Linear, Zoom. Point Slackbot at your Notion MCP server and "pull the launch checklist for campaign X" becomes a question in a thread instead of a tab hunt. Option 2 is the one that fits most marketing ops requests, because most of them never needed a CRM hop.
:::

The identity part is where people get hurt, so the design rules from Salesforce's own architects are worth repeating. External MCP servers have to support OAuth 2.0. Per-user authentication means every teammate needs their own account in the external system, and the agent inherits whatever access that person already has, nothing narrower. A service account fixes the scope but applies to everyone equally, so treat it as all-or-nothing. And when someone changes roles or leaves, the stored token does not revoke itself. A stale token is a live credential nobody watches.

## Build #4: The quiet one, segmentation plus 2,000 sends

Less exciting, possibly the best ROI per dollar-not-spent. Foundations includes unified profiles across your systems, segmentation over up to five data streams with 10,000 credits a year, and 2,000 email sends a month through the built-in builder.

For a small marketing ops team that currently exports CSVs from three places to run one nurture sequence, this collapses real manual work: build the segment from unified data, send the nurture inside the same system, read the analytics without a BI ticket. Two thousand sends won't run your whole lifecycle program. It will run your highest-intent slice, which is the one you should be hand-tending anyway.

## Free versus paid, side by side

<table class="cmp">
<tr><th>What you get</th><th>Foundations (free with Enterprise)</th><th>When you start paying</th></tr>
<tr><td>Agentforce actions</td><td>200,000 Flex credits (~10,000 actions)</td><td>More credits at ~$0.10 per action list price</td></tr>
<tr><td>Agent skills</td><td>One</td><td>Additional skills and agents are paid Agentforce</td></tr>
<tr><td>Prompt Builder + generative responses</td><td>Included</td><td>Scales with your Agentforce contract</td></tr>
<tr><td>Email</td><td>2,000 sends/month, basic analytics</td><td>Marketing Cloud tiers when you outgrow it</td></tr>
<tr><td>Segmentation</td><td>5 data streams, 10,000 credits/year</td><td>Data 360 expansions</td></tr>
<tr><td>Partner integrations</td><td>Free trials, 25+ apps on AgentExchange</td><td>Full licenses from each vendor</td></tr>
</table>

## The limitations nobody puts on slide one

The free tier has edges, and pretending otherwise wastes the runway:

- **You must already be an Enterprise customer.** Foundations is an add-on to an existing contract, not a free CRM. Starter Suite is a separate product for people starting from zero.
- **One agent skill.** The free bundle funds exactly one agent's job description. Pick it deliberately.
- **Credits burn on every action.** A chatty customer-facing agent can exhaust the pool in weeks. Internal, scoped tools stretch it across quarters.
- **MCP means OAuth homework.** Every external connection needs its own auth design, per-user or service account, and Salesforce's own guidance says to audit the external system's permissions separately because your CRM access review doesn't cover it.
- **It's Salesforce-ecosystem-first.** The value compounds if your data already lives in the CRM. If your real marketing stack sits elsewhere, the agent spends its first thousand actions just reaching your data.
- **Usage overages are real.** Salesforce's FAQ is explicit that going past the included limits costs money, for credits and for payment processing.

::: verdict warn
**⚠️ The trap: building a customer-facing chatbot first.** It's the demo everyone imagines, and it's the fastest way to burn 200,000 credits on angry edge cases. Internal tools, routing, and drafts first. Put the agent in front of customers only after it has a track record on your own team.
:::

::: verdict win
**✅ The winning move: one scoped agent, one sprint.** Activate Foundations in Setup, spend a day on the Agentblazer Champion trail on Trailhead (free, like all of it; the first AI Associate and Agentforce Specialist exam attempts are free too), then build the routing agent or the brief generator and measure the hours it saves. Ten thousand actions is plenty for proof.
:::

::: verdict lose
**❌ The losing move: letting the credits expire unmeasured.** This allotment is Salesforce's way of showing you what paid Agentforce feels like. If you activate it, log the actions consumed and the hours saved from week one. Otherwise the renewal conversation next year happens with the vendor holding all the numbers.
:::

## What this really is

Strip the marketing off and Foundations reads as a land-grab with good manners. Salesforce is betting that once your team builds one working agent on free credits, the second agent gets budgeted instead of debated. For marketing ops, the bet can work in your favor, because the free pool is genuinely enough to settle the "should we even try agents" argument with evidence instead of opinions.

The teams that come out ahead will treat this like what it is: a funded experiment with a hard cap. Build the smallest agent that removes a weekly chore, count the hours, and keep the credit meter in the same spreadsheet as everything else you measure.

Browse the [MartechSignal tools directory](/tools/) for what's competing with Agentforce in your category before you decide the free credits settle the question. Free changes the risk. It doesn't change the due diligence.
