# Budibase review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Self-host free with unlimited actions, apps, agents and users in one workspace; Cloud Pro $19/mo annual published above it (the vendor pricing page: [pricing page](https://budibase.com/pricing), verified 2026-09-07). |
| Feature depth | 7/10 | Apps, automations and AI agents over your databases cover the internal operations platform job (vendor documentation: [vendor site](https://budibase.com), verified 2026-09-28). |
| Integrations | 7/10 | Twelve named datasources from PostgreSQL and Oracle to Snowflake, S3, Sheets and REST (vendor documentation: [vendor site](https://budibase.com), verified 2026-09-28). |
| AI capability | 6/10 | AI agents with tools, memory and structured outputs, model-agnostic across seven providers (vendor documentation: [vendor site](https://budibase.com), verified 2026-09-28). |
| Openness | 8/10 | GPLv3 core with 28.3k GitHub stars and a BSL pro folder kept separate (the source repository: [repository](budibase/budibase), verified 2026-09-28). |
| Operational maturity | 6/10 | 28.3k stars with priced cloud tiers and beta-quality agent features shipping fast (vendor documentation: [vendor site](https://budibase.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; Open-source licensing with free self-hosting | &#10007; Paid plans start at $19/mo once past the free tier |
| &#10003; AI capabilities: AI agents with tools, memory and structured outputs (beta since March 2026) |  |
| &#10003; Active public repository (28,267 GitHub stars counted at last check) |  |
| &#10003; Native integrations include PostgreSQL, MySQL, MongoDB (12 listed) |  |

**What is Budibase?**
Budibase: Open-source operations platform for building AI agents, apps and automations on your own data. Budibase ships with AI agents with tools, memory and structured outputs (beta since March 2026). The public repository carries 28,267 stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Budibase cost?**
Budibase has a free tier; paid plans start at $19/mo. Self-host open source free: unlimited actions, apps, agents and users in 1 workspace (GPLv3 core, pro folder BSL). Cloud Pro $19/mo billed annually, Premium $49, Business $299; end users $5/user/mo, creators $50/creator/mo. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Budibase a good self-hosted Workflow Automation tool in 2026?**
The most interesting agent story in the open-source internal-tools class, wrapped in a layered license. A strong pick if you want agents acting over your own data and can accept the operational fine print that comes with them.

**Is Budibase free to self-host?**
Yes. The open-source self-hosted tier has unlimited actions, apps, automations, agents and users in one workspace, and the repo&#x27;s licensing guidelines put the core under GPLv3 with client and component libraries under MPL 2.0. The paid parts live in a packages/pro folder under a Business Source License that converts to GPLv3 four years after publication, and paid self-hosted tiers validate their license against Budibase&#x27;s account portal over the network. Staying on the free tier means nothing phones home for licensing, though Budibase AI features do call external endpoints and knowledge features need a GEMINI_API_KEY.

**Budibase vs NocoBase: which should marketing ops pick?**
They solve adjacent problems. NocoBase is data-model-first: you define the schema, then assemble pages and server-side workflows around it, which suits systems that must match your organization&#x27;s data model exactly. Budibase gets you a working CRUD app faster on top of an existing datasource and adds an agents layer, an LLM with tools, permissions and Slack or Teams escalation, that NocoBase does not offer in the same form. Choose NocoBase when the data model and approval logic are the product; choose Budibase when you want apps and agents quickly over Postgres, MySQL or REST, and can live with row triggers that only fire on rows written through Budibase.

**Which AI models can Budibase agents use?**
It is model-agnostic and bring-your-own-key: the docs list Anthropic, OpenAI, Google, Mistral, Groq and OpenRouter, plus a custom provider option that accepts any OpenAI-compatible base URL, which is how locally hosted models connect. Two requirements surprise people. Knowledge sources, meaning retrieval over your own documents, currently support pgvector as the only vector store and require a GEMINI_API_KEY in the environment. And the primary agent channels are Slack and Microsoft Teams, since in-app agent chat is deprecated and the Discord and Telegram channels were removed in v3.44.1.

- **Pricing:** Free tier
- **Category:** [Workflow Automation](/categories/workflow-automation/)
- **GitHub:** ★ 28267
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Budibase is a tool in Workflow Automation with free and open source. The catalog documents 3 AI features, 12 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

ToolJet

Open-source low-code platform for internal tools: prompt or build admin panels, dashboards and operational apps

n8n

Open-source workflow automation platform with AI agent capabilities and 400+ nodes

Appsmith

Open-source platform for building admin panels and internal dashboards on your existing databases and APIs

Tray.io

AI-powered integration platform for building custom automation and AI agents

Pipedream

Workflow automation with 2,500+ integrations, built around data-driven triggers and HTTP steps

[More Workflow Automation Tools →](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Workflow Automation](/categories/workflow-automation/)
- Budibase
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Budibase review (2026): pricing, AI features, verdict

Open-source operations platform for building AI agents, apps and automations on your own data

Workflow Automation · Free tier · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Budibase &#8594;](https://budibase.com)

[How we review](/methodology/) · No affiliate links

[Visit Budibase &#8594;](https://budibase.com)

## MartechSignal Score: 42/60

Budibase is the open-source operations platform where AI agents, apps and automations meet your own data. The self-hosted free tier is unusually complete: unlimited everything in one workspace.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Budibase is an open-source operations platform for building internal apps, automations and AI agents on your own data, and its 2026 direction is agents first: the repo now bills it as AI agents, automations and apps that run your operations, model agnostic. You connect data sources, build interfaces in a visual builder, wire multi-step automations and, since the agents beta of March 2026, define agents as an LLM with instructions, tools, memory and structured outputs that can read rows, write rows and trigger automations, with per-tool run-as permissions and Slack or Microsoft Teams escalation when a human needs to approve. Model support is open rather than bundled: Anthropic, OpenAI, Google, Mistral, Groq, OpenRouter or any OpenAI-compatible endpoint, including locally hosted models. Licensing is layered: the repo&#x27;s own guidelines say Budibase is GPLv3 overall, the client and component libraries are MPL 2.0, paid features live in a packages/pro folder under a Business Source License that converts to GPLv3 after four years, and apps you build are not GPL-restricted. Self-hosting free is real: one all-in-one Docker image rated at 2 cores and 6 GB of RAM, a compose cluster for production, or a Helm chart published to an OCI registry. Marketing teams reach for it on the same builds as its peers: lead-routing consoles, campaign budget trackers, content approval queues and dashboards that join ad platform data with CRM records. One behavior to plan around: automations trigger on rows written through Budibase, not on rows inserted directly into an external Postgres or MySQL. External data sources documented include PostgreSQL, MySQL, MongoDB, SQL Server, Oracle, Snowflake, Elasticsearch, DynamoDB, Firestore, S3, Google Sheets and REST. Cloud plans start at $19 monthly billed annually with metered actions, and self-hosted open source has unlimited actions and users in a single workspace. This assessment is based on the documented architecture and public materials.

Budibase homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI agents with tools, memory and structured outputs (beta since March 2026)
- Model-agnostic: Anthropic, OpenAI, Google, Mistral, Groq, OpenRouter, custom OpenAI-compatible
- Automation AI steps: classify, translate, summarize, extract document data
## Key Integrations

- PostgreSQL
- MySQL
- MongoDB
- SQL Server
- Oracle
- Snowflake
- Elasticsearch
- DynamoDB
- Firestore
- S3
- Google Sheets
- REST API
## Pricing

Budibase is open core: the self-hosted version is free, paid plans start at $19/mo as of 2026-09.

Self-host open source free: unlimited actions, apps, agents and users in 1 workspace (GPLv3 core, pro folder BSL). Cloud Pro $19/mo billed annually, Premium $49, Business $299; end users $5/user/mo, creators $50/creator/mo.

Current plans and limits live on the [Budibase pricing page](https://budibase.com/pricing).

## How to install

- All-in-one Docker: docker run -d -t --name=budibase -p 10000:80 -v /local/path/data:/data --restart unless-stopped budibase/budibase:latest. The docs rate this at 2 cores and 6 GB of RAM for most uses, and the UI lands on port 10000.
- Before production, set the environment variables the docs call out: CUSTOM_DOMAIN, INTERNAL_API_KEY, JWT_SECRET, MINIO_ACCESS_KEY and MINIO_SECRET_KEY, REDIS_PASSWORD, and COUCHDB_USER with COUCHDB_PASSWORD. If unset, the image seeds them with generated UUIDs into an .env file in the mounted volume.
- Production compose cluster: download docker-compose.yaml, .env and litellm_config.yaml from the repo&#x27;s hosting folder, then docker-compose up -d. You get CouchDB, MinIO, Nginx, the Budibase worker and the Budibase server as separate services; Linux is the recommended host, with setup scripts under hosting/scripts/linux.
- Kubernetes: helm install --create-namespace --namespace budibase budibase oci://ghcr.io/budibase/charts/budibase. The charts moved to an OCI registry, so older instructions pointing at budibase.github.io need updating. Docs recommend nodes with at least 1 GB of memory and more for volume.
- Agents and AI environment: set GEMINI_API_KEY for knowledge features, BBAI_LITELLM_KEY on every agent-running service for Budibase AI, and configure a pgvector connection under Settings if you want retrieval over your own documents.
- Licensing network access: paid self-hosted tiers validate against account.budibase.app over HTTPS 443, and self-hosted Budibase AI reaches Budibase cloud IPs, so both need outbound allowances; air-gapped deployment is an enterprise add-on.
## Best for

Marketing ops teams that want self-hosted internal apps plus agents that can act on that data, bringing their own LLM keys and even local models, with Slack or Teams as the approval surface.

## Not for

Teams whose automations must fire on rows written by other systems, organizations that need a single OSI license (the pro folder is BSL), and buyers who cannot permit any outbound license validation or AI traffic.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Budibase builds data-first: connect a datasource, then generate screens against it, then add automations. The internal Budibase DB (CouchDB-backed) is the default when nothing external exists, and the connector list covers Postgres, MySQL, MongoDB, SQL Server, Oracle, Snowflake, Elasticsearch, DynamoDB, Firestore, Redis, S3, Google Sheets and REST, plus custom datasource plugins. One documented behavior catches teams that connect a live database: row-based automations fire on rows written through Budibase, so rows inserted externally into your Postgres or MySQL do not trigger anything. Plan a webhook or a polling step for that case.

The agents are the reason to look again if you evaluated Budibase before 2026. Each workspace gets an Agents tab, and an agent is an LLM configured with instructions, tools, memory and structured outputs. Tools are discovered from your datasources and automations and granted per operation, with a run-as setting that executes either as the requesting user or as an admin, and field-level exclusions for link and formula fields. Escalation pauses the agent and asks a human in Slack or Teams before resuming. Docs also document an Agent step inside automations, agent activity monitoring, and a testing flow for evaluating agents against scenarios before production. Access went channel-first: Slack and Microsoft Teams are the primary surfaces, in-app agent chat is deprecated, and the Discord and Telegram channels were removed in v3.44.1.

The licensing is three layers rather than one, and reading the repo&#x27;s own guidelines settles most questions. The core is GPLv3 overall, the client and component libraries are MPL 2.0, and paid features live in packages/pro under a Business Source License that converts to GPLv3 four years after publication; apps you build are not GPL-restricted. Two operational consequences: paid self-hosted tiers validate their license against Budibase&#x27;s account portal over HTTPS, so plan outbound access (offline licenses are an enterprise add-on), and Budibase AI on self-host calls Budibase&#x27;s cloud endpoints, so SSL inspection can break it.

Agent and knowledge features have their own requirements, and they are the difference between a demo and a deployment. Knowledge sources (retrieval over your documents) currently support pgvector as the only vector store, and they require a GEMINI_API_KEY in the environment or the knowledge actions are disabled. Budibase AI on self-host needs BBAI_LITELLM_KEY configured on every agent-running service, including the automation worker. If you bring your own model through the custom provider option, an OpenAI-compatible base URL plus key is the contract, which is how Ollama-style local models connect.

This assessment is based on the repository, docs.budibase.com and release notes. Calibration: releases are roughly weekly (v3.44.1 shipped September 7, 2026, the day this was written), the agents beta arrived in March 2026, and the project&#x27;s own usage claims do not reconcile (docs say over 200,000 teams, the homepage says 300K), so treat scale claims as marketing. Cloud pricing meters actions, defined as agent tool calls plus automation node executions plus row saves, updates and deletes, with hard monthly limits and no overage billing, so a busy automation estate needs a plan check each quarter.

## Verdict

The most interesting agent story in the open-source internal-tools class, wrapped in a layered license. A strong pick if you want agents acting over your own data and can accept the operational fine print that comes with them.

## Pros and cons

## Related concepts

- [Workflow automation](/glossary/workflow-automation/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [MCP](/glossary/mcp/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Budibase: Open-source operations platform for building AI agents, apps and automations on your own data. Budibase ships with AI agents with tools, memory and structured outputs (beta since March 2026). The public repository carries 28,267 stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Budibase has a free tier; paid plans start at $19/mo. Self-host open source free: unlimited actions, apps, agents and users in 1 workspace (GPLv3 core, pro folder BSL). Cloud Pro $19/mo billed annually, Premium $49, Business $299; end users $5/user/mo, creators $50/creator/mo. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The most interesting agent story in the open-source internal-tools class, wrapped in a layered license. A strong pick if you want agents acting over your own data and can accept the operational fine print that comes with them.

Yes. The open-source self-hosted tier has unlimited actions, apps, automations, agents and users in one workspace, and the repo&#x27;s licensing guidelines put the core under GPLv3 with client and component libraries under MPL 2.0. The paid parts live in a packages/pro folder under a Business Source License that converts to GPLv3 four years after publication, and paid self-hosted tiers validate their license against Budibase&#x27;s account portal over the network. Staying on the free tier means nothing phones home for licensing, though Budibase AI features do call external endpoints and knowledge features need a GEMINI_API_KEY.

They solve adjacent problems. NocoBase is data-model-first: you define the schema, then assemble pages and server-side workflows around it, which suits systems that must match your organization&#x27;s data model exactly. Budibase gets you a working CRUD app faster on top of an existing datasource and adds an agents layer, an LLM with tools, permissions and Slack or Teams escalation, that NocoBase does not offer in the same form. Choose NocoBase when the data model and approval logic are the product; choose Budibase when you want apps and agents quickly over Postgres, MySQL or REST, and can live with row triggers that only fire on rows written through Budibase.

It is model-agnostic and bring-your-own-key: the docs list Anthropic, OpenAI, Google, Mistral, Groq and OpenRouter, plus a custom provider option that accepts any OpenAI-compatible base URL, which is how locally hosted models connect. Two requirements surprise people. Knowledge sources, meaning retrieval over your own documents, currently support pgvector as the only vector store and require a GEMINI_API_KEY in the environment. And the primary agent channels are Slack and Microsoft Teams, since in-app agent chat is deprecated and the Discord and Telegram channels were removed in v3.44.1.

## Similar Tools

## Related reading

- [Budibase next to NocoBase and NocoDB: choosing between the three](/blog/nocobase-vs-nocodb-vs-budibase/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [Multi-Touch Attribution Was Always a Fiction](/blog/multi-touch-attribution-was-always-a-fiction/)
### Quick Facts

Related guides: [Budibase in Zapier alternatives](/alternatives/zapier/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/budibase/#app",
    "name": "Budibase",
    "description": "Open-source operations platform for building AI agents, apps and automations on your own data",
    "image": "https://martechsignal.com/og/tools/budibase.png",
    "url": "https://martechsignal.com/tools/budibase/",
    "sameAs": [
      "https://budibase.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/budibase/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-09-05",
    "offers": {
      "@type": "Offer",
      "price": 19,
      "priceCurrency": "USD",
      "url": "https://budibase.com/pricing",
      "priceValidUntil": "2026-12-31"
    }
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
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Workflow Automation",
        "item": "https://martechsignal.com/categories/workflow-automation/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Budibase",
        "item": "https://martechsignal.com/tools/budibase/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Budibase?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Budibase: Open-source operations platform for building AI agents, apps and automations on your own data. Budibase ships with AI agents with tools, memory and structured outputs (beta since March 2026). The public repository carries 28,267 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Budibase cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Budibase has a free tier; paid plans start at $19/mo. Self-host open source free: unlimited actions, apps, agents and users in 1 workspace (GPLv3 core, pro folder BSL). Cloud Pro $19/mo billed annually, Premium $49, Business $299; end users $5/user/mo, creators $50/creator/mo. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Budibase a good self-hosted Workflow Automation tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most interesting agent story in the open-source internal-tools class, wrapped in a layered license. A strong pick if you want agents acting over your own data and can accept the operational fine print that comes with them."
        }
      },
      {
        "@type": "Question",
        "name": "Is Budibase free to self-host?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. The open-source self-hosted tier has unlimited actions, apps, automations, agents and users in one workspace, and the repo's licensing guidelines put the core under GPLv3 with client and component libraries under MPL 2.0. The paid parts live in a packages/pro folder under a Business Source License that converts to GPLv3 four years after publication, and paid self-hosted tiers validate their license against Budibase's account portal over the network. Staying on the free tier means nothing phones home for licensing, though Budibase AI features do call external endpoints and knowledge features need a GEMINI_API_KEY."
        }
      },
      {
        "@type": "Question",
        "name": "Budibase vs NocoBase: which should marketing ops pick?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "They solve adjacent problems. NocoBase is data-model-first: you define the schema, then assemble pages and server-side workflows around it, which suits systems that must match your organization's data model exactly. Budibase gets you a working CRUD app faster on top of an existing datasource and adds an agents layer, an LLM with tools, permissions and Slack or Teams escalation, that NocoBase does not offer in the same form. Choose NocoBase when the data model and approval logic are the product; choose Budibase when you want apps and agents quickly over Postgres, MySQL or REST, and can live with row triggers that only fire on rows written through Budibase."
        }
      },
      {
        "@type": "Question",
        "name": "Which AI models can Budibase agents use?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It is model-agnostic and bring-your-own-key: the docs list Anthropic, OpenAI, Google, Mistral, Groq and OpenRouter, plus a custom provider option that accepts any OpenAI-compatible base URL, which is how locally hosted models connect. Two requirements surprise people. Knowledge sources, meaning retrieval over your own documents, currently support pgvector as the only vector store and require a GEMINI_API_KEY in the environment. And the primary agent channels are Slack and Microsoft Teams, since in-app agent chat is deprecated and the Discord and Telegram channels were removed in v3.44.1."
        }
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "author": {
      "@type": "Person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://martechsignal.com/#organization",
      "name": "MartechSignal"
    },
    "datePublished": "2026-09-26",
    "reviewBody": "Budibase is the open-source operations platform where AI agents, apps and automations meet your own data. The self-hosted free tier is unusually complete: unlimited everything in one workspace.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/budibase/#app",
      "name": "Budibase",
      "url": "https://martechsignal.com/tools/budibase/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 42,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
