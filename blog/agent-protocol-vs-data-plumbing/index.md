# Agent protocol vs data plumbing: what actually fails

TC **[Tim Christensen](/authors/tim-christensen/)**

AUTOMATION · AI AGENTS · 8 MIN

## Your agent protocol matters less than your data plumbing

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Your agent protocol matters less than your data plumbing

SEP 23, 2026 · Updated SEP 27, 2026

Filed under [Workflow Automation](/categories/workflow-automation/)

MCP keeps winning the protocol argument while 85% of enterprises, by [Fivetran's count](https://www.fivetran.com/resources/reports/the-2026-agentic-ai-readiness-index), run agents on data that cannot support them. The plumbing is the problem.

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

[Fivetran's Agentic AI Readiness Index 2026](https://www.fivetran.com/resources/reports/the-2026-agentic-ai-readiness-index) supplies the stat of the season: 85% of enterprises lack the data foundation to run agentic AI at scale. When I covered Fivetran in August I pushed back on the idea that you need to [buy a new data stack](/blog/you-dont-need-new-data-stack-fivetran/) to fix this, and I would write the same post again today. Vendor research selling data plumbing will find plumbing problems. Fair.

But strip out the pitch and the underlying breakdown is hard to argue with, because it matches what practitioners report. Fivetran surveyed enterprises and found 41% already run agents in production. Asked what holds them back, 42% said data quality and lineage, 39% said sovereignty and compliance, 39% said security and privacy. Talent and strategy ranked lower. [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), separately, estimates over 40% of agentic AI projects will be canceled by end of 2027, mostly because companies moved into use cases their data could not support.

The most damning correlation in the index: among the 15% of organizations that call themselves fully prepared, 98% report strong confidence in agent ROI. Among the least prepared, confidence is 16%. Preparation and payoff move together, and the preparation Fivetran measures is automated data movement, lineage, interoperability, and governance. Three of those four are plumbing. None of them are protocol choices.

## What to do before you pick anything

If you are mid-evaluation of agent tooling, the honest order of operations looks like this. First, pick the three or four entities your agent will actually act on: customers, orders, campaigns, inventory, whatever your use case touches. For each one, write down which system is the source of truth and how stale its data is allowed to be before a decision becomes wrong. If you cannot answer those two questions on paper, no protocol saves you.

Second, get the freshness real. A nightly batch feed into a table an agent reads every five minutes is not a real time data source, it is a lie with a cron schedule. Third, give the agent a narrow interface shaped around outcomes, the way the WorkOS article prescribes and the way Salesforce's hybrid architecture ended up working. Fourth, and only fourth, decide how that interface is transported. By then MCP versus API is a small question with an obvious answer, usually both.

You can do most of this without enterprise money. A self-hosted stack like the one in our [open source martech guide](/blog/open-source-martech-stack/) covers the movement and storage layers, and a tool like [NocoBase](/tools/nocobase/) gives you governed, lineage-visible business data that an MCP server can sit on top of without a data warehouse project. The bottleneck was never the software budget. It is the discipline of deciding what is true.

## What good plumbing looks like first

Before any protocol choice, the data layer needs properties that are boring to list and expensive to skip. Stable identifiers that mean the same customer in the CRM, the billing system, and the event stream. Timestamps with timezones attached, so an agent does not send the Tuesday campaign on Monday evening. An event vocabulary agreed before the tools are picked, because "trial started" and "trial_activated" in two systems is two different stories. Contracts tested like code, so schema drift fails a pipeline instead of a customer.

Each item prevents one specific agent failure: the wrong-customer send, the timezone drift, the duplicate record, the confident wrong answer. None of these make a good demo. All of them decide whether an agent run at scale is an asset or an incident queue.

## The failure mode nobody demos

The expensive failure is not the agent that crashes. Crashes are honest and visible. It is the agent that succeeds at the wrong task because the data was internally consistent and wrong, a duplicated account, a mislabeled subscription tier, a currency column without its unit. The run reports success, the dashboard turns green, and the error compounds quietly until a human notices in a report three weeks later.

That failure is invisible to every protocol benchmark, and it is the one the plumbing work is actually for.

## Verdict

The protocol layer won. MCP launched a persistent file store, a memory server, and a Gantt tool in one week without anyone relitigating the standard. Pick MCP where dynamic agent access matters, plain APIs where batches and machine-to-machine writes are enough, and stop treating that choice as strategic.

The data layer is still losing. 85% of enterprises are not ready, the top blocker is data quality and lineage, and Gartner expects 40% of agent projects canceled by 2027. Every one of those failures will get blamed on AI. Most of them will be stale fields, duplicate records, and nobody knowing which system was right.

The connectivity debate turned out to be the easy half, and most teams have quietly finished having it. The data plumbing is the project that is still open, and it is the one Gartner's cancellation wave will actually be about. More on keeping the automation layer honest lives in our [workflow automation coverage](/categories/workflow-automation/).

## Related reading

- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
## Related tools

- [Pipedream](/tools/pipedream/) - Workflow automation with 2,500+ integrations, built around data-driven triggers and HTTP steps
- [Workato](/tools/workato/) - Enterprise AI governance plus integration and automation on one platform
- [Writer](/tools/writer/) - Enterprise AI platform with Palmyra models, brand governance, and agents
## Comparison guides

- [Best AI Marketing Automation tools (2026): 8 compared](/best/ai-marketing-automation-tools/)
- [Best AI Personalization &amp; CDP tools (2026): 8 compared](/best/ai-personalization-tools/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
- [MCP](/glossary/mcp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [AdCreative.ai](/tools/adcreative-ai/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)


```json
{
  "@context": "https://schema.org",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelectors": [
      "h1",
      "article h2"
    ]
  },
  "@type": "BlogPosting",
  "headline": "Your agent protocol matters less than your data plumbing",
  "description": "MCP keeps winning the protocol argument while 85% of enterprises, by Fivetran's count, run agents on data that cannot support.",
  "author": {
    "@id": "https://martechsignal.com/authors/tim-christensen/#person"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://martechsignal.com/#organization",
    "name": "MartechSignal",
    "url": "https://martechsignal.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://martechsignal.com/logo.png"
    }
  },
  "datePublished": "2026-09-23",
  "dateModified": "2026-09-27",
  "mainEntityOfPage": "https://martechsignal.com/blog/agent-protocol-vs-data-plumbing/",
  "image": {
    "@type": "ImageObject",
    "url": "https://martechsignal.com/og/agent-protocol-vs-data-plumbing.png",
    "width": 1200,
    "height": 630
  },
  "citation": [
    {
      "@type": "CreativeWork",
      "name": "Fivetran Agentic AI Readiness Index 2026",
      "url": "https://www.fivetran.com/resources/reports/the-2026-agentic-ai-readiness-index"
    },
    {
      "@type": "CreativeWork",
      "name": "Gartner: 40% of agentic AI projects canceled by 2027",
      "url": "https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027"
    }
  ],
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 1586,
  "articleSection": "workflow-automation"
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://martechsignal.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://martechsignal.com/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Your agent protocol matters less than your data plumbing",
      "item": "https://martechsignal.com/blog/agent-protocol-vs-data-plumbing/"
    }
  ]
}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
