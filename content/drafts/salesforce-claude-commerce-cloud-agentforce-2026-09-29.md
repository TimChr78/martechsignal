---
title: "Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough"
seo_title: "Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough"
slug: salesforce-claude-commerce-cloud-agentforce
date: 2026-09-29
author: Tim Christensen
tags: [AI Agents, Salesforce, Anthropic]
categories: [marketing-automation]
excerpt: "Salesforce's own blog invites merchants to build commerce agents on Claude. The same day, Dreamforce's IT track told a story about one trusted platform. The two posts point in opposite directions, and the Commerce one is more honest."
---

On September 22, Salesforce published two blog posts. One, from the Commerce Cloud team, is titled "Build Agents Your Way with Claude and Commerce Cloud." It invites merchants to build commerce agents on Anthropic's Claude, and it names Claude as an intelligence layer that can sit on top of Salesforce's Commerce MCP server. The other, the [Dreamforce IT announcements recap](https://www.salesforce.com/blog/dreamforce-2026-top-it-announcements/), leads with AIforce, a platform layer that reaches every surface, where "Agentforce, Claude, or another agent of your choice" can take action inside your Salesforce permissions.

The Claude in both posts is Anthropic's model. Salesforce, the company that has sold Agentforce since 2024 as the way to build agents on its platform, is now publishing instructions for building agents on a competitor's model, working directly against Salesforce data through MCP.

That's not a partnership announcement. It's an admission about where agent building actually happens.

## What the Commerce Cloud post actually says

The post, by Katja Franz, Head of Merchant Experience at Salesforce Commerce Cloud, opens with Anthropic's [blueprint for building commerce agents on Claude](https://claude.com/blog/claude-for-commerce-agents). The kit ships reference code, guardrails, and best practices for two agents: a shopping agent that browses, compares, and buys, and a merchant agent that handles inventory, pricing, and promotions. Salesforce's own assessment of the kit: it "cuts weeks of engineering work down to days."

Here's the part worth reading twice. When the vendor that sells Agentforce evaluates Anthropic's kit, it doesn't say "use Agentforce instead." It offers a menu:

::: callout
Salesforce's framing, from the post itself: "Build it: Our catalog, cart, checkout, and merchant APIs are open via MCP. Build your own agent experience with Claude or any model you choose." And: "Buy it: Commerce Cloud ships with Shopper Agent and Merchant Agent natively, out-of-the-box." The build path routes around Agentforce entirely. Model, agent loop, interface, memory, tool calls: all outside Salesforce. Only data and APIs stay in.
:::

The "build" path never commits to a default model. Claude gets named in the intro and again in the build/buy list, and the official offer is "Claude or any model you choose." That's a signal without a commitment. Vendors name the model they want named, and Salesforce named Claude twice in one post on its own blog.

## The numbers Salesforce chose to share

All figures below come from the Franz post itself, reported by Salesforce, not independently measured. They're still worth taking seriously, because they show which story Salesforce wants merchants to believe.

For the native Merchant Agent: "Commerce Cloud customers using our Merchant Agent are already seeing early success... On average, this cuts time-to-task completion by over 86%." For the native Shopper Agent: "Cacau Show saw a 32% increase in conversion and a 50% increase in revenue after launching Shopper Agent on its site." No methodology, no sample size, no dates for either claim. That's normal for vendor blogs, and it's exactly why the "build" path exists: merchants with real operational data will eventually want to measure agents themselves.

The post also cites Salesforce's State of Commerce research: consumer use of agentic search as the first stop in shopping grew 200% year-over-year, and 90% of commerce leaders believe LLMs will be essential to product discovery by 2027. The number that matters operationally is the boring one: B2C Commerce exposes an MCP server to all merchants, so any agentic layer can read catalog, inventory, and pricing data within guardrails.

## Build path vs buy path, as Salesforce describes it

<table class="cmp">
<tr><th></th><th>Build it (Claude on MCP)</th><th>Buy it (native agents)</th></tr>
<tr>
  <td><strong>Where the agent runs</strong></td>
  <td class="oss-price">Outside Salesforce, on the model you pick</td>
  <td class="com-price">Inside Commerce Cloud, Salesforce-managed</td>
</tr>
<tr>
  <td><strong>Model choice</strong></td>
  <td class="oss-price">"Claude or any model you choose"</td>
  <td class="com-price">Whatever Agentforce ships (Salesforce doesn't say)</td>
</tr>
<tr>
  <td><strong>Surface</strong></td>
  <td class="oss-price">Your interface: Claude, Slack, ChatGPT, or custom</td>
  <td class="com-price">Storefront Shopper Agent, back-office Merchant Agent</td>
</tr>
<tr>
  <td><strong>Evidence offered</strong></td>
  <td class="oss-price">Anthropic's blueprint: weeks of work cut to days</td>
  <td class="com-price">86% faster merchant tasks; Cacau Show +32% conversion</td>
</tr>
<tr>
  <td><strong>Guardrails</strong></td>
  <td class="oss-price">MCP access "within guardrails" (details thin)</td>
  <td class="com-price">"Governed, embedded, and human-in-the-loop by design"</td>
</tr>
</table>

The two paths aren't equal in the post's own telling. The buy path gets the numbers and the governance language. The build path gets flexibility, and the named example of a competitor's model doing the work.

## The IT track tells the other story

The [Dreamforce IT recap](https://www.salesforce.com/blog/dreamforce-2026-top-it-announcements/), published the same day by Samantha Marsh, describes a different world. Its headline: "the future of work is all about humans and AI building side-by-side on a single, trusted foundation."

AIforce, the first of the top five announcements, is a "live, composable interface layer" powered by the Headless Toolkit, where "every capability is accessible via API, MCP, or CLI." The post says employees and agents work "using the same trusted data, logic, and governance your business already relies on," whether that agent is "Agentforce, Claude, or another agent of your choice."

Announcement five is MCP Security & Risk Scores: automatic scanning of MCP servers during Agentforce registration, checking for prompt injections, tool poisoning, and rug pull attacks, with a Low/Medium/High rating before a connection is authorized. Salesforce is simultaneously telling IT that external agents connecting through MCP are a risk surface to be scored and locked down, and telling merchants that connecting Claude through MCP is the flexible way forward. Both things can be true. The security framing exists because the external connections are already happening, with or without Salesforce's blessing.

## Agent Optimizer is the honest post of the three

A day earlier, on September 21, Salesforce published [Agent Optimizer: A Faster Path to Better Outcomes](https://www.salesforce.com/blog/agent-optimizer/). It's framed as a product announcement (the tool is in beta, available now) but it reads as a list of everything Agentforce wasn't when customers deployed it.

Aron Kale, VP of Product Management on the Agentforce team, writes: "Deploying an AI agent to production is not the finish line. Often, that's when you start to understand what you've actually built." The post describes today's loop as manual: read sessions, inspect failures, look for patterns, update instructions, test, check that the fix didn't break something else, then convert what you learned into regression tests. "Meanwhile, your agent is handling thousands more conversations."

The section heading "Building is the easy part" is the sentence Agentforce marketing has been avoiding for two years. The customer numbers it cites: agents at Engine, a travel management platform, resolve 50% of chat inquiries with 15% lower support handle time; Hibbett, a sporting goods retailer, uses agents to handle 90% of its core shopper journeys. Agent Optimizer then proposes to automate that iteration loop, with an "autonomy dial" for how much the agent does without sign-off.

Read together with the Commerce Cloud post, the picture is consistent. Native agents exist, they work in cases Salesforce selects, and the unglamorous work of operating them, measuring them, and fixing their failures is where the real cost lives. That's precisely the work a team takes in-house when it builds on MCP with its own model.

## Where this fits in the pattern

This is the fourth Salesforce story this site has followed, and each one has the same shape. [The third no-code promise](/blog/salesforce-third-no-code-promise/) covered Builder Central and Campaign Agent, two products promising marketing ops without specialists. [The Agentforce free tier](/blog/salesforce-agentforce-free-marketing-ops/) was a land grab for marketing ops teams. [Protocol vs plumbing](/blog/agent-protocol-vs-data-plumbing/) argued that protocols like MCP commoditize the connection layer while the plumbing underneath stays broken. And [Claude Cowork](/blog/claude-cowork-is-eating-the-edges-of-your-martech-stack/) described Anthropic pulling marketing ops work out of vendor platforms and onto the desktop.

The Commerce Cloud post is Salesforce conceding the Cowork argument for commerce. Anthropic shipped a blueprint that "cuts weeks of engineering work down to days," and Salesforce's response was to open the data layer and host the announcement on its own blog. The platform company keeps the system of record and lets the agent layer compete on top of it.

::: verdict win
<div class="verdict-label">Verdict: a win for merchants, a confession from Salesforce</div>

If you run Commerce Cloud, the MCP server plus Anthropic's blueprint is a real option, and Salesforce just told you so in writing. The native agents still make sense for teams that want Salesforce to own the loop, and the vendor-reported numbers are the only evidence on that side. But the "build it" menu item wouldn't exist if Agentforce had closed the question. My read: it's on the menu because customers kept asking for the model they already use.
:::

Vendor pages checked September 29, 2026. All performance figures are Salesforce's own claims from the linked posts.

Tools linked in this post: [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) | [Salesforce CRM](/tools/salesforce-crm/) | [Anthropic Claude](https://claude.com) | [OpenAI ChatGPT](https://chatgpt.com) | [Slack](https://slack.com)
