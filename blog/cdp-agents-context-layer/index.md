# The CDP is being rebuilt as an agent's context layer

CDP · AI Agents · 8 min read

## The CDP is being rebuilt as an agent's context layer, and no vendor will call it that

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · The CDP is being rebuilt as an agent's context layer, and no vendor will call it that

29 Oct 2026

Filed under [Analytics & Attribution](/categories/analytics/) · [Marketing Automation](/categories/marketing-automation/)

Jackson Engles keeps saying the quiet part out loud. Minerva, the startup he co-founded, raised $20 million in June on the strength of an identity graph covering 270 million consumers, and when AdExchanger asked him this month whether that data is a competitive edge, he declined the layup. "Yes, sure, we have data that can help create better outcomes," he said. "But is it a long-term, durable moat? Probably not."

A founder talking down his own moat is rare enough. The label he refuses is the more telling part. Minerva sits between a brand's CRM, its warehouse and its campaign tools, joins that first-party data with the graph, and lets AI agents act on the result. Functionally that is a customer data platform with the dashboards swapped for agents. AdExchanger called it an "agentic CDP." Engles won't market it that way, because his buyers hear "CDP" and think "system I already regret buying." His framing: "Customers want the outcome of a CDP; they want their data to be more queryable by less technical users."

The category name is dead. The job description got promoted.

Customer data platforms promised a single view of the customer and left most marketing teams with one more system to maintain. The original sin was the assumption about who consumes that view: a human, opening a dashboard, building segments. The rebuild keeps the plumbing and swaps the consumer. The reader of your unified customer data is increasingly software that reads it, reasons about it and acts on it, and the interesting fight in martech right now is over whose governed context the agent acts on.

## Three October announcements, one machine

Qlik placed its Model Context Protocol server in Anthropic's Claude Directory this month, a distribution move we covered [yesterday](/blog/mcp-distribution-channel-2026-10-28/). The quieter half of the announcement is the product. Claude can query governed Qlik Cloud data, inspect lineage and trust signals, and run selected analytics workflows. Authentication runs over OAuth and maps onto the permissions a company already has in Qlik Cloud. Josh Good, Qlik's VP of corporate strategy, described the request he actually hears from buyers: "Customers adopting Claude want more than an LLM hooked to raw records. They want Claude to work with governed business context, existing metrics, and data workflows with enterprise controls."

Read that as a CDP requirements document. Single view of the customer, check. Permissions and lineage, check. The only thing that changed is the customer in "customer data": it is Claude now, not a campaign manager.

Salesforce sells the same machine at platform scale and does not pretend otherwise. The first IDC MarketScape for worldwide agentic AI platforms, published in October, evaluated 25 vendors and named Salesforce a Leader. Of the strengths Salesforce says IDC highlighted, two are context-and-control claims: a "native, grounded data foundation," meaning agents built directly on Data 360 and Customer 360 with zero-copy federation to Snowflake, Databricks and BigQuery, and "hybrid reasoning with deterministic control," the Atlas Reasoning Engine plus the open-source Agent Script for auditable constraints on autonomous agents. The Winter '27 Marketing Cloud release, more than 60 features, is mostly agents riding that foundation. Campaign Agent is generally available now. Headless Marketing, shipping in October, exposes Marketing Cloud and Data 360 through an MCP server so ChatGPT, Gemini, Claude or Slack can run campaigns against them.


| Vendor | What shipped | Where the context lives | Who governs it |
| --- | --- | --- | --- |
| Minerva | Agent layer over brand data plus its graph of 270 million consumers; $20 million raised in June | Minerva's middle layer joining CRM and warehouse data | Minerva's platform; the brand owns the first-party half |
| Qlik | MCP server in Anthropic's Claude Directory | Qlik Cloud apps, datasets, metrics, lineage | Existing Qlik Cloud permissions, OAuth per connection |
| Salesforce | Leader slot in the first IDC agentic platforms MarketScape; Winter '27 agents | Data 360 / Customer 360, zero-copy to Snowflake, Databricks, BigQuery | Salesforce roles, which the company markets as the point |

A startup that refuses the CDP label, an analytics vendor that ships context with the audit trail attached, and a platform vendor whose agentic pitch reduces to "grounded data plus control over how agents act." Nobody in that set is selling a CDP. All three are selling governed context for agents, because that is what the buyer now needs and the old name would only remind the buyer of the last purchase.

## If context is the moat, check the expiration date

Every agentic vendor converges on the same line: context is the moat, because models are commoditizing and the durable advantage is your data plus the rules around it. Engles gives the data half of that argument a couple of years at best, and he knows his own graph better than anyone quoting him.

He is probably right, and the consequence is uncomfortable for everyone selling context as the moat. If a 270-million-consumer identity graph plus a brand's first-party data is not durable, your governed warehouse is not either. The part that survives commoditization is the other half of every pitch above: the control surface. Lineage, permissions, audit, revocation, deterministic constraints. Salesforce's MarketScape strengths are literally that list. Governance is not the moat around the product. Governance is the product, because it is the only layer a vendor can keep improving after everyone's context looks similar.

Engles makes the same point from the product side without naming it. Marketers, he told AdExchanger, should not be "using Claude and bringing in random data"; they should start from an opinionated view of which data is relevant. That opinionated narrowing is a governance decision. The value of Minerva's layer is the curation of what an agent is allowed to see. The size of the graph is the part Engles expects to fade.

## Three questions before your agent's memory moves in

For a marketing ops team deciding where its agent's memory lives, the feature checklist matters less than three jurisdiction questions.

Who can read it? Qlik's server inherits your existing Qlik Cloud permissions; Salesforce grounds agents in Data 360 roles. The failing pattern is the god credential, one API key that lets the agent see every table because segmenting access was somebody else's problem. If the vendor's answer to "who can read this" is "the agent," keep shopping.

Who can revoke it? An agent that reads your customer context builds a memory of it. Revocation has to be per connection and per agent, it has to actually cut access, and the audit log has to show what was read before the cut. OAuth per connection is the floor, not the ceiling. Ask what happens to everything the agent already absorbed.

What happens when two agents disagree about the same customer? Your retention agent reads churn risk, your support agent reads upsell intent, both are "grounded in governed context," and they act in opposite directions. No vendor in this wave has an arbitration story. Until one exists, a human is the arbitration layer, and the honest vendors admit it. We have walked this class of problem before, from [protocols versus data plumbing](/blog/agent-protocol-vs-data-plumbing/) to [what agents remember about your campaigns](/blog/procedural-memory-agents/); the two-agents-one-customer case is the one nobody has closed.

## The label contest nobody wants to enter

We [ran a label contest for autonomous marketing platforms](/blog/autonomous-marketing-platform-label-contest/) and nobody won, because every candidate name scares a different buyer. The agentic CDP has the inverse problem: the accurate name describes a purchase most marketing teams already made once and will not repeat. So the function gets rebuilt under outcome language, "context layer," "data foundation," "trusted business context," and the category comes back as something a buyer will sign for.

The CDP did not die. It got demoted from the system your marketers log into to the memory your software acts on. That is a better job and a harder purchase, because the questions that decide it concern jurisdiction: who can read the memory, who can revoke it, and who breaks the tie when two agents disagree about the same customer.

**Context is a moat with a two-year half-life.** The durable part of the agentic stack is the control surface around the context: permissions, lineage, audit, revocation. Buy the governance, rent the graph.

Mapping this onto your own stack: our [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) and [Twilio Segment](/tools/segment/) profiles cover both ends of the CDP-to-context-layer spectrum, and [the CDP reckoning](/blog/cdp-reckoning-warehouse-native/) is the warehouse-native version of the same argument. We also publish our own small agent surface, a machine-readable manifest documenting what agents may read on this site, spelled out in [our AI policy](/ai-policy/). Even a one-person publisher has a context layer now. Yours should at least have a permissions model.

## Related reading

- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
## Related tools

- [Mixpanel](/tools/mixpanel/) - Product analytics platform with AI-powered insights for user behavior tracking
- [Snowplow](/tools/snowplow/) - Customer context infrastructure: behavioral event pipeline for warehouses and AI agents
- [Cordys CRM](/tools/cordys-crm/) - Open-source AI CRM with built-in agents, conversational analytics, and private deployment
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Matomo vs PostHog (2026): web analytics or product analytics](/vs/matomo-vs-posthog/)
## Glossary terms

- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Instagram Skills](/tools/instagram-skills/)
