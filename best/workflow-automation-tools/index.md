# Best workflow automation tools (2026)


| Tool | Pricing | Open source | Public API | Verdict |
| --- | --- | --- | --- | --- |
| [n8n](/tools/n8n/) | Open Source | Yes | yes | Best for self-hosted workflows with code steps and AI agents. |
| [Zapier](/tools/zapier/) | Freemium | No | yes | Best for breadth and onboarding speed on niche integrations. |
| [Make](/tools/make/) | Freemium | No | yes | Best for branching visual workflows on a small-team budget. |
| [Pipedream](/tools/pipedream/) | Freemium | No | no | Best for developer teams wanting code steps and MCP endpoints. |
| [Workato](/tools/workato/) | Enterprise | No | yes | Best for enterprises governing agents and integration in one platform. |
| [Tray.io](/tools/tray-io/) | Enterprise | No | yes | Best for AI app governance plus integration on one platform. |

[Open-Source Tools](/categories/open-source/)[Workflow Automation](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Best workflow automation tools (2026)

n8n suits teams that self-host and want code steps plus AI agents in their workflows. Zapier wins on breadth and fast onboarding for niche apps. Make is the budget pick for visual branching in small teams. All three connect thousands of apps, so decide on hosting, price curve, and how much code you want to write.

**Our top pick: [n8n](#n8n)** — Best for self-hosted workflows with code steps and AI agents. [Try n8n](https://n8n.io)

Last verified 2026-09-28.

## How we picked

This list is for marketing and operations teams buying automation in 2026: moving form submissions into a CRM, syncing campaign data between tools, and wiring AI agents into the same pipelines. The six picks come from the catalog workflow-automation category because automation is their core job, not a feature of an app builder.

The set spans the market on purpose: two no-code giants, a visual middleweight priced under 10 dollars, a developer platform, and two enterprise iPaaS vendors. These entries disagree about almost everything except the promise that software should talk to software without a human in the middle.

Three things decide the outcome. The billing unit: tasks, credits, compute time, or negotiated usage can change the cost of one workflow by an order of magnitude. Who runs the instance: self-hosting moves maintenance onto you and metered volume off the bill. And the AI meter, since agent activity is often billed apart from core automation.

## What we checked and when

Pricing checked 2026-09-28 against each vendor's own pricing page · API availability confirmed from public documentation · Integrations read from vendor listings and source repositories. Not installed and not benchmarked: this is desk research with dates on it.

What we could not verify is called out under each tool below.

## Browse the hubs behind these picks

**Guide:** [MCP and agent protocols](/guides/mcp-agent-protocols/) · [automation strategy](/guides/workflow-automation-strategy/)

## Open-source momentum, with receipts

Star counts we snapshot ourselves every morning — check any of them against GitHub in one click.

- n8n — 206,232 stars, +3,829 in the 36-snapshot window to 2026-09-29 202,403→206,232 [verify on GitHub](https://github.com/n8n-io/n8n)
[All movers on the trending page](/trending/).

## [n8n](/tools/n8n/)

n8n is the open-source end of this list: self-hosted at no cost under a fair-code license, with cloud plans at 20 dollars monthly on Starter and 50 dollars on Pro. The visual builder runs on more than 400 nodes covering Slack, Gmail, Salesforce, HubSpot, Shopify, Stripe, Google Sheets, and Notion, with API access and custom code steps beyond the catalog. AI sits inside workflows: AI agent nodes run on LangChain, alongside documented AI data transformation, AI content generation, and AI-powered integrations. With 206,232 GitHub stars it has the largest community in this category by a wide margin. Founded 2019 in Berlin and deployable in the cloud or on your own servers, it trades vendor convenience for control.

**Verdict:** Best for self-hosted workflows with code steps and AI agents.

Vendor: [Official site](https://n8n.io) · [Pricing](https://n8n.io/pricing/) · [GitHub](https://github.com/n8n-io/n8n)

**Skip it if you want zero maintenance and instant breadth.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Zapier](/tools/zapier/)

Zapier is the catalog play: more than 9,000 app integrations, still the widest in this directory, and niche martech tools that lack an n8n node usually still ship a Zapier integration. Pricing is task-based and the definition matters: a task counts when an action successfully moves data, triggers and failed actions do not, but every step in a Zap counts, so a twenty-step workflow consumes about twenty tasks per run. Free covers 100 tasks monthly and two-step Zaps; Professional starts at 19.99 dollars monthly billed annually at the 750-task tier (29.99 dollars monthly), Team at 69 dollars with 2,000 tasks and 25 seats. Polling runs 15 minutes on Free, 2 on Professional, 1 on Team. Agents, Chatbots, Canvas, MCP, and Copilot sit on every plan, with agent activity billed separately at 400 activities a month free.

**Verdict:** Best for breadth and onboarding speed on niche integrations.

Vendor: [Official site](https://zapier.com) · [Pricing](https://zapier.com/pricing)

**Skip it if task billing would punish your run volume.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Make](/tools/make/)

Make, the platform formerly known as Integromat, is the visual middleweight: scenarios are drawn as a graph, so branching, looping, and error handling are visible instead of buried in configuration. Billing moved to credits in August 2026, and router modules plus the five error handlers consume none, which is kind to branching workflows. Free covers 1,000 credits monthly with 2 active scenarios; Core costs 9 dollars monthly, Pro 16 dollars, Teams 29 dollars, each including 10,000 credits with a slider up to 8 million, and unused credits expire at the billing term's end. AI Agents run on all plans, alongside Maia by Make, the AI Toolkit, and a Make MCP Server. Founded in Prague in 2012 and part of Celonis since 2020, it sits between Zapier and n8n.

**Verdict:** Best for branching visual workflows on a small-team budget.

Vendor: [Official site](https://www.make.com) · [Pricing](https://www.make.com/en/pricing)

**Skip it if credit expiry beats a flat or self-hosted bill.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Pipedream](/tools/pipedream/)

Pipedream is the developer platform: more than 3,000 APIs behind a builder where any step can be a no-code action or arbitrary Node.js, Python, or Go code, plus 10,000 pre-built triggers and actions, a key-value data store, and GitHub Sync for version-controlled deployment. Pricing is credit-based because you pay for compute time: Free includes 100 credits monthly and 1 million AI tokens, Basic 29 dollars monthly with 2,000 credits, Advanced 49 dollars with unlimited workflows and accounts plus control-flow operators, Connect 99 dollars for teams embedding integrations in their own products. Any workflow can deploy as an MCP server that AI coding agents call directly. Founded 2019 and acquired by Workday in 2026, with SOC 2 Type II, HIPAA, and GDPR attestations on record.

**Verdict:** Best for developer teams wanting code steps and MCP endpoints.

Vendor: [Official site](https://pipedream.com) · [Pricing](https://pipedream.com/pricing)

**Skip it if nobody will write code inside an automation step.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Workato](/tools/workato/)

Workato is the enterprise option, and the first thing to know is that pricing is fully demo-gated: the public page carries no numbers, just a usage-based model with a platform edition fee plus a usage fee in one billing unit across four cumulative editions, Standard through Workato One, the last adding agentic capabilities. The product splits into a Control Plane governing agents with role-based access, audit, and approval gates, and an Execution Plane doing integration, automation, API management, EDI, and document processing. The docs claim more than 1,000 connectors spanning Salesforce, Slack, SAP, Workday, NetSuite, ServiceNow, Snowflake, and HubSpot. The AI layer is substantial: Agent Studio, role-based Genies for IT, Sales, HR, Support, and Marketing, the Acumen data scientist agent, and governed Enterprise MCP servers for Claude Desktop, ChatGPT, and Cursor.

**Verdict:** Best for enterprises governing agents and integration in one platform.

Vendor: [Official site](https://www.workato.com) · [Pricing](https://www.workato.com/pricing)

**Skip it without an enterprise budget and a sales process.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Tray.io](/tools/tray-io/)

Tray.io trades as Tray.ai now and calls itself an AI orchestration platform rather than an iPaaS, and the 2026 shipping record backs the repositioning: Tray Headless arrived in June with plugins for Claude Code and Codex, MCP dynamic authentication and a Sync CLI followed in August, and Tray Helix is a managed runtime that puts AI-built apps into production with security controls and a named owner. The automation core stays familiar: service triggers, webhooks, or scheduled polls, conditional logic, callable workflows, and a data mapper over 700-plus pre-built connectors, with a connector SDK for gaps and on-premise connectivity. Pricing is not public: three tiers (Pro, Team, Enterprise) metered in Tasks across integration, automation, MCP, and agents. AI Palette ships on every plan; Merlin Agent Builder is a paid add-on.

**Verdict:** Best for AI app governance plus integration on one platform.

Vendor: [Official site](https://tray.ai) · [Pricing](https://tray.ai/pricing/)

**Skip it if transparent pricing or self-hosting is required.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

Every price quoted here comes from the vendor's own pricing page as catalogued on the tool page. Browse [all 163 tools](/tools/) or read [how we evaluate](/methodology/), or download the [machine-readable catalog](/catalog-tools.json).

## Should I self-host n8n or pay for Zapier?

Self-host n8n if you have a server and want code steps plus AI agent nodes with no per-task bill. Pay for Zapier if you want the widest app coverage and the fastest onboarding. One saves money, the other saves setup time.

## What is the cheapest visual automation tool for a small team?

Make. Its visual builder handles branching logic that Zapier charges more for, and small-team budgets stretch further on its plans. Start on the free tier and check whether your monthly operations fit before you commit.

## Which automation platform suits developers?

Pipedream. Code steps are first-class instead of bolted on, and it exposes MCP endpoints for agent workflows. n8n is the open alternative if your team would rather self-host than pay per execution.

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Best workflow automation tools (2026)",
    "datePublished": "2026-09-26",
    "dateModified": "2026-09-28",
    "author": {
      "@type": "Person",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/"
    },
    "numberOfItems": 6,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "n8n",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/n8n/#app",
          "url": "https://martechsignal.com/tools/n8n/",
          "name": "n8n"
        }
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Zapier",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/zapier/#app",
          "url": "https://martechsignal.com/tools/zapier/",
          "name": "Zapier"
        }
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Make",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/make/#app",
          "url": "https://martechsignal.com/tools/make/",
          "name": "Make"
        }
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Pipedream",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/pipedream/#app",
          "url": "https://martechsignal.com/tools/pipedream/",
          "name": "Pipedream"
        }
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "Workato",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/workato/#app",
          "url": "https://martechsignal.com/tools/workato/",
          "name": "Workato"
        }
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Tray.io",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/tray-io/#app",
          "url": "https://martechsignal.com/tools/tray-io/",
          "name": "Tray.io"
        }
      }
    ]
  },
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
        "name": "Best-of lists",
        "item": "https://martechsignal.com/best/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Best workflow automation tools (2026)",
        "item": "https://martechsignal.com/best/workflow-automation-tools/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
