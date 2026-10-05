---
title: "The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent"
seo_title: "19 open-source MCP servers, one marketing agent"
slug: open-source-agentic-martech-stack-mcp
date: 2026-10-05
author: Tim Christensen
tags: [Open Source, MCP, AI Agents]
categories: [open-source, agent-skills]
excerpt: "Nineteen of the 81 open-source tools in our catalog ship an MCP server, enough to compose a complete agentic loop with no SaaS in the path."
---

An agent can now run a marketing loop end to end on open source. We counted this morning from the [directory](/tools/): 19 of the 81 open-source tools we track list an MCP server among their AI features. Five of them cover the whole loop. A CRM holds the records, an automation platform does the sends, analytics watches the results, a flagging tool runs the experiments, and one gateway reaches the two platforms that have no open path at all, Google Ads and Meta Ads. The software costs nothing. The bill is hosting time and supervision.

## What the count covers

A number like this is only as good as its counting rule, so here is ours. A tool is in if its catalog record names an MCP server as one of its AI features. That gives 19, listed below. Four more tools document working MCP servers in their research notes without the headline listing, and three mentions fail the test outright. Those edge cases get their own section further down, because they are where sloppy counts go wrong.

| Tool | The MCP claim in its catalog record |
|---|---|
| [Twenty](/tools/twenty/) | Native MCP server on Cloud workspaces (vendor site claim) |
| [Relaticle](/tools/relaticle/) | 37-tool MCP server |
| [Activepieces](/tools/activepieces/) | MCP and API access, free tier |
| [Matomo](/tools/matomo/) | Official MCP Server plugin |
| [Jitsu](/tools/jitsu/) | MCP server for agent-driven setup |
| [GrowthBook](/tools/growthbook/) | MCP server for Claude, Cursor, and VS Code |
| [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/) | 250+ MCP tools across the three platforms |
| [Open Mercato](/tools/open-mercato/) | MCP server exposing about 70 tools |
| [NocoDB](/tools/nocodb/) | MCP server for record-level agent access |
| [Flagsmith](/tools/flagsmith/) | MCP server for natural-language flag management |
| [ToolJet](/tools/tooljet/) | MCP server (beta) for Claude Code, Codex, and Cursor builds |
| [Cordys CRM](/tools/cordys-crm/) | MCP server with 11 tools for external AI agents |
| [DeskcommCRM](/tools/deskcommcrm/) | MCP server exposing the CRM to external agents |
| [Dolibarr ERP/CRM](/tools/dolibarr/) | Experimental MCP server and AI assistant (24.0) |
| [Email Marketing Bible](/tools/email-marketing-bible/) | ESP control via MCP: Klaviyo, Mailchimp, Resend, beehiiv, Omnisend |
| [Line Harness](/tools/line-harness/) | MCP server for Claude Code: scenarios, inbox, broadcasts |
| [Macro](/tools/macro/) | MCP server exposing unified workspace search |
| [React Email Editor](/tools/react-email-editor/) | Unlayer MCP server (beta), 14 documented tools |
| [WaCRM](/tools/wacrm/) | MCP server for Claude and Cursor |

## The loop, layer by layer

Here is the stack the brief promises, with the role each server plays. The agent harness on top can be any MCP client: Claude Code, Cursor, a custom script. The catalog does not gate on which one.

<table class="cmp">
<tr><th>Layer</th><th>Pick</th><th>Cost to start</th></tr>
<tr>
  <td><strong>Records</strong></td>
  <td class="oss-price"><a href="/tools/twenty/">Twenty</a> (Cloud) or <a href="/tools/relaticle/">Relaticle</a> (self-hosted)</td>
  <td class="oss-price">$0 self-hosted; Twenty Cloud Pro $9/user/mo</td>
</tr>
<tr>
  <td><strong>Hands</strong></td>
  <td class="oss-price"><a href="/tools/activepieces/">Activepieces</a></td>
  <td class="oss-price">Free tier, 100 credits/day</td>
</tr>
<tr>
  <td><strong>Eyes</strong></td>
  <td class="oss-price"><a href="/tools/matomo/">Matomo</a> + <a href="/tools/jitsu/">Jitsu</a></td>
  <td class="oss-price">$0; Jitsu free tier 200k events/mo</td>
</tr>
<tr>
  <td><strong>Experiments</strong></td>
  <td class="oss-price"><a href="/tools/growthbook/">GrowthBook</a></td>
  <td class="oss-price">Starter free, 3 users</td>
</tr>
<tr>
  <td><strong>Paid gateway</strong></td>
  <td class="oss-price"><a href="/tools/google-meta-ads-ga4-mcp/">google-meta-ads-ga4-mcp</a></td>
  <td class="oss-price">$0, MIT licensed</td>
</tr>
<tr>
  <td><strong>Stack total</strong></td>
  <td class="oss-price">License cost of the five layers</td>
  <td class="oss-price">$0 + hosting</td>
</tr>
<tr>
  <td><strong>SaaS anchors</strong></td>
  <td class="com-price"><a href="/tools/zapier/">Zapier</a> Professional $19.99/mo, <a href="/tools/klaviyo/">Klaviyo</a> from ~$20/mo, <a href="/tools/segment/">Segment</a> Team $120/mo</td>
  <td class="com-price">$160/mo and up, before a CRM or experiments suite</td>
</tr>
</table>

In practice, Matomo's plugin exposes reports to MCP clients, with write actions gated, so the agent reads traffic itself instead of waiting for a screenshot. Jitsu's server is for setup rather than queries: the agent wires new event pipelines in plain language. GrowthBook exposes flag and experiment management to the same client, so the agent can read an experiment result and, with permissions set carefully, ship the winner. Activepieces is the hands: its flows become callable tools over MCP, which is how a decision turns into an email that goes out. Twenty's site says every Cloud workspace ships with a native MCP server that reads and writes CRM data; Relaticle's server exposes 37 tools if you would rather keep the records on your own box.

::: callout
**The ad platforms are the exception, and one server covers them.** Nothing open source replaces a Google or Meta ads account; both stay paid and closed. The way in is [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/): 250-plus tools for campaign reads, pauses, budget moves, and spend reconciliation across Google Ads, Meta Ads, and GA4 in one place. The record counts roughly 150 Google Ads tools and 80-plus Meta tools inside that total. One MCP registration replaces the tab-juggling.
:::

## Tool counts are the real story

Nineteen is the headline, but the interesting number is granularity. MCP servers vary widely in what they expose; some offer a handful of tools and some offer hundreds.

[Relaticle](/tools/relaticle/) documents 37 tools. [Open Mercato](/tools/open-mercato/), an MIT-licensed commerce and CRM framework, exposes about 70. The ads gateway carries 250-plus. At the thin end, [Cordys CRM](/tools/cordys-crm/) ships 11. When you plan an agent's responsibilities, this matters more than the count of servers: a server with 11 tools can read records but will not run your lifecycle marketing. Depth, not presence, is the selection criterion, and it is the reason the five-layer stack above picks one deep server per layer instead of ten shallow ones.

## The edge cases, stated plainly

Four tools document real MCP servers without carrying the headline listing: [PostHog](/tools/posthog/), whose official hosted server [lives in its own repo](https://github.com/PostHog/mcp) and ships flag, analytics, and error-tracking tools to any MCP client; [AlphOne](/tools/alphone/), which has spoken MCP natively since version 0.9.0; [OpenSEO](/tools/openseo/), which added a server in May 2026; and [Warpdrive](/tools/warpdrive/), which exposes 29 OAuth-protected tools over its API. Count those and the total becomes 23. We keep the headline at 19 because the counting rule has to come from one field in the record, and the rule is stated before the number.

Three mentions do not count at all. [Django CRM](/tools/django-crm/) shipped an MCP server and removed it, on the stated grounds that it covered eight entities and added nothing its API lacked. [Promptfoo](/tools/promptfoo/)'s MCP proxy belongs to its hosted cloud product, not the MIT-licensed repo. [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/) consumes Zapier's MCP for its actions rather than shipping a server. A naive grep for "MCP" would have counted all three.

## What this stack asks of you

The licensing is free; nothing else about it is free.

Someone hosts the CRM, the automation engine, and the analytics. Someone updates them. Someone writes the agent's permissions so that "read the experiment" and "pause the campaign" sit at different trust levels, because in this stack they are technically one tool call apart. The servers also vary in maturity: Dolibarr's arrives in version 24.0 with the word "experimental" [in the project's own changelog](https://github.com/Dolibarr/dolibarr/blob/develop/ChangeLog), and Twenty ties its native server to Cloud workspaces rather than self-hosted installs. An MCP server is a tool interface, not autonomy. The judgment still has to live in the harness, the permissions, and whoever reviews the agent's week.

::: verdict win
<div class="verdict-label">✓ Where this holds up</div>

For a team already comfortable with Docker and an agent CLI, the five-layer loop is assembleable this week at zero license cost, and every layer has a catalog page documenting exactly what its server exposes. The honest comparison is not "$0 vs $160/mo"; it is $0 plus real operational work versus $160/mo plus someone else's uptime. Teams without an ops person should buy the SaaS. Teams with one should start with the deepest server in the layer they trust least.
:::

**Tools linked in this post:** [Twenty](/tools/twenty/) | [Relaticle](/tools/relaticle/) | [Activepieces](/tools/activepieces/) | [Matomo](/tools/matomo/) | [Jitsu](/tools/jitsu/) | [GrowthBook](/tools/growthbook/) | [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/) | [Open Mercato](/tools/open-mercato/) | [NocoDB](/tools/nocodb/) | [Flagsmith](/tools/flagsmith/) | [ToolJet](/tools/tooljet/) | [Cordys CRM](/tools/cordys-crm/) | [DeskcommCRM](/tools/deskcommcrm/) | [Dolibarr ERP/CRM](/tools/dolibarr/) | [Email Marketing Bible](/tools/email-marketing-bible/) | [Line Harness](/tools/line-harness/) | [Macro](/tools/macro/) | [React Email Editor](/tools/react-email-editor/) | [WaCRM](/tools/wacrm/) | [Zapier](/tools/zapier/) | [Klaviyo](/tools/klaviyo/) | [Segment](/tools/segment/) | [PostHog](/tools/posthog/) | [AlphOne](/tools/alphone/) | [OpenSEO](/tools/openseo/) | [Warpdrive](/tools/warpdrive/) | [Django CRM](/tools/django-crm/) | [Promptfoo](/tools/promptfoo/) | [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/)

**Related reading:** [Open-source martech stack vs subscriptions](/blog/open-source-martech-stack/) - the cost side of the same decision: when self-hosting beats SaaS pricing.
