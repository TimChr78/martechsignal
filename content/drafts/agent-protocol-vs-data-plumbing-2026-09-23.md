---
title: "Your agent protocol matters less than your data plumbing"
seo_title: "Agent protocol vs data plumbing: what actually fails"
slug: agent-protocol-vs-data-plumbing
date: 2026-09-23
author: Tim Christensen
tags: [Automation, AI Agents, MCP]
categories: [workflow-automation]
---
MCP keeps winning the protocol argument while 85% of enterprises run agents on data that cannot support them. The plumbing is the problem.

In late July I argued that [MCP rewrites the integration economics of the marketing stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/). Pairwise connectors collapse into one registration per tool, the O(n²) tax goes away, and suite lock-in gets weaker. I still believe that. What I underestimated is how fast the protocol layer would settle while the layer underneath it stayed broken.

The past ten days proved the point from two directions at once. Hacker News filled up with MCP tooling: AgentDrive, persistent versioned file storage for agents, ProGantt, Gantt charts an agent can read and write, and Friday, a self-hosted persistent memory server for coding agents. Three launches inside a week, all speaking fluent MCP, none of them arguing about whether MCP is the right protocol. That debate is over in practice. Meanwhile WorkOS published the most useful MCP article of the month, and it is not about the protocol at all. It is about tokens, schemas, and the shape of your data.

## The Salesforce guide answers the wrong question well

Salesforce's architecture team published "Choosing Between MCP and APIs" in July, and it is genuinely good work. They walk a fictional B2B apparel brand through five requirements for exposing its systems to a third-party shopping agent: catalog data, pricing, live inventory, order placement, fulfillment updates.

Here is what makes the piece useful and slightly deflating at the same time. The final architecture is a hybrid. Catalog pushes run as a daily batch job over an API, because catalog data is static. Pricing goes through an API with a service account, then crosses an MCP bridge so the agent can query it dynamically. Inventory reads hit the warehouse management system through the same bridge, because they need to be real time. Orders route straight to the ERP over an API, skipping Salesforce entirely to cut failure points. Fulfillment updates push out as API webhooks.

Of those five decisions, almost none were protocol decisions. Every one of them was a data decision: which system holds the truth for this entity, how fresh it needs to be, and what path keeps it consistent. MCP versus REST was the last coat of paint. The architects spent their effort on where pricing lives and whether the warehouse system can answer in real time, and the protocol fell out of those answers.

That is the pattern I keep seeing in production stacks too. Teams agonize over MCP support in their vendor evaluation, then discover their product feed updates nightly, their CRM has four competing definitions of "active customer," and nobody can say which system wins. An agent pointed at that mess does not fail because of the transport. It fails confidently, at machine speed, on stale numbers.

## Even the protocol's own costs are a data-shape problem

The WorkOS piece, "What an MCP server costs you in tokens," landed September 18 and quotes Anthropic's numbers directly. A typical multi-server setup spanning GitHub, Slack, Sentry, Grafana, and Splunk burns roughly 55,000 tokens on tool definitions before the model reads your request. Tool selection accuracy starts dropping somewhere between 30 and 50 available tools. And the fix Anthropic recommends for the worst case is code execution against a filesystem-shaped tool catalog, which took one worked example from 150,000 tokens to 2,000.

That last number matters most. The biggest optimization in the MCP ecosystem right now is restructuring how tools and data are presented to the model. Not a new protocol, not a better client. Interface design around the shape of the data. The same article's rule for building servers is "design tools around what someone is trying to accomplish, not around your internal API structure," which is a data modeling instruction wearing a protocol costume.

## The 85% number, with its conflict of interest named

Fivetran's Agentic AI Readiness Index 2026 supplies the stat of the season: 85% of enterprises lack the data foundation to run agentic AI at scale. When I covered Fivetran in August I pushed back on the idea that you need to [buy a new data stack](/blog/you-dont-need-new-data-stack-fivetran/) to fix this, and I would write the same post again today. Vendor research selling data plumbing will find plumbing problems. Fair.

But strip out the pitch and the underlying breakdown is hard to argue with, because it matches what practitioners report. Fivetran surveyed enterprises and found 41% already run agents in production. Asked what holds them back, 42% said data quality and lineage, 39% said sovereignty and compliance, 39% said security and privacy. Talent and strategy ranked lower. Gartner, separately, estimates over 40% of agentic AI projects will be canceled by end of 2027, mostly because companies moved into use cases their data could not support.

The most damning correlation in the index: among the 15% of organizations that call themselves fully prepared, 98% report strong confidence in agent ROI. Among the least prepared, confidence is 16%. Preparation and payoff move together, and the preparation Fivetran measures is automated data movement, lineage, interoperability, and governance. Three of those four are plumbing. None of them are protocol choices.

## What to do before you pick anything

If you are mid-evaluation of agent tooling, the honest order of operations looks like this. First, pick the three or four entities your agent will actually act on: customers, orders, campaigns, inventory, whatever your use case touches. For each one, write down which system is the source of truth and how stale its data is allowed to be before a decision becomes wrong. If you cannot answer those two questions on paper, no protocol saves you.

Second, get the freshness real. A nightly batch feed into a table an agent reads every five minutes is not a real time data source, it is a lie with a cron schedule. Third, give the agent a narrow interface shaped around outcomes, the way the WorkOS article prescribes and the way Salesforce's hybrid architecture ended up working. Fourth, and only fourth, decide how that interface is transported. By then MCP versus API is a small question with an obvious answer, usually both.

You can do most of this without enterprise money. A self-hosted stack like the one in our [open source martech guide](/blog/open-source-martech-stack/) covers the movement and storage layers, and a tool like [NocoBase](/tools/nocobase/) gives you governed, lineage-visible business data that an MCP server can sit on top of without a data warehouse project. The bottleneck was never the software budget. It is the discipline of deciding what is true.

## Verdict

::: verdict win
The protocol layer won. MCP launched a persistent file store, a memory server, and a Gantt tool in one week without anyone relitigating the standard. Pick MCP where dynamic agent access matters, plain APIs where batches and machine-to-machine writes are enough, and stop treating that choice as strategic.
:::

::: verdict lose
The data layer is still losing. 85% of enterprises are not ready, the top blocker is data quality and lineage, and Gartner expects 40% of agent projects canceled by 2027. Every one of those failures will get blamed on AI. Most of them will be stale fields, duplicate records, and nobody knowing which system was right.
:::

The connectivity debate turned out to be the easy half, and most teams have quietly finished having it. The data plumbing is the project that is still open, and it is the one Gartner's cancellation wave will actually be about. More on keeping the automation layer honest lives in our [workflow automation coverage](/categories/workflow-automation/).
