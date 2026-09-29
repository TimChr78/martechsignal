# Model Context Protocol (MCP)

n8n

Open-source workflow automation platform with AI agent capabilities and 400+ nodes

Make

Visual automation platform for building complex workflows with AI agents and apps

[Browse all tools →](/tools/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Model Context Protocol (MCP)

GLOSSARY

Definition last updated 2026-09-25

## Definition

The Model Context Protocol is an open standard for connecting AI models to external tools and data sources. An MCP server exposes capabilities - search a database, send an email, read a file - in a uniform format any MCP-compatible client can use. It replaces one-off integrations between each model and each tool with a single protocol on each side.

## Why it matters

Anthropic introduced MCP in late 2024 and open-sourced it; adoption spread quickly through developer tools and then marketing platforms. For marketing teams, MCP is how agents get hands: the CRM connector, the ad-account connector, the analytics connector that lets an agent act inside your stack.

## How it works

An MCP server is a small program that declares resources it can read and actions it can perform. The client - Claude Code, an agent runtime, an IDE - discovers those declarations and lets the model call them as structured tools. Sessions are stateful enough for context to persist across calls within a conversation. You install or host a server for each tool family you want agents to reach, then approve which clients may connect. Each server advertises a small catalog of resources and tools, and the model requests them by name during a session. The practical gain is that adding the tenth tool costs one server, not ten bespoke integrations.

## Practical uses

Marketing teams use MCP servers to give agents safe access to internal data: campaign performance reads, content draft writes, ticket lookups. The protocol's permission model means access can be scoped per server, which is how you give an agent analytics reads without handing over spend controls.

## How to choose

Prefer MCP servers that are idempotent and read-heavy for first deployments. A server that can only read and report cannot break production data; once trust is established, add write-capable servers one at a time.

## The numbers

Scale math: an agent that checks six data sources before each decision, running once per hour, makes roughly 4,300 tool calls per week per agent. Against metered MCP or search quotas, that is the difference between a rounding error and a budget line - design polling frequency before launch, not after. MCP servers are mostly free and open source, so the bill lands elsewhere: the API calls behind each tool and the model tokens spent deciding which tool to call. Those usage costs vary by vendor. When you compare this against a per-task iPaaS platform, count the developer time to host and patch the servers, because the license savings are real and the maintenance is yours.

## Common mistakes

Running unvetted third-party MCP servers with production credentials is the emerging horror story - a server with broad scopes is a supply-chain risk. Audit what scopes each server holds and rotate credentials separately. MCP is not a replacement for your integration platform. It standardizes how a model reaches tools, not how data syncs between business systems on a schedule. Teams also assume a server with a vendor's name in it is official. Anyone can publish one, so check who operates it and what scopes it requests. Connecting an agent to a tool is also not the same as granting it authority: decide which calls are read-only, which queue for approval, and which the agent may make alone.

## What changed with AI

MCP exists because of AI; the practical risk is quota economics. Hosted-model providers meter MCP tool calls separately from plain inference, and agentic workloads multiply call counts. Know your provider's metering before wiring an agent to a chatty tool.

## Tools in this space

## Related terms

[ABM](/glossary/abm/) · [Agentic Marketing](/glossary/agentic-marketing/) · [AI Agent](/glossary/ai-agent/) · [Lead scoring](/glossary/lead-scoring/) · [Marketing automation](/glossary/marketing-automation/)

## Seen in the wild

[OpenAI Isn&#x27;t Building Ads. It&#x27;s Building Agents](/blog/openai-agent-ads-spending-without-you/)

Sources: [Model Context Protocol](https://modelcontextprotocol.io/) · [n8n](https://n8n.io) · [Make](https://www.make.com)

### Categories

[Workflow Automation](/categories/workflow-automation/) [Best Workflow Automation tools](/best/workflow-automation-tools/) [MCP and agent protocols](/guides/mcp-agent-protocols/) [Automation strategy](/guides/workflow-automation-strategy/) [Marketing Automation](/categories/marketing-automation/) [Best Marketing Automation tools](/best/ai-marketing-automation-tools/) [Automation strategy](/guides/workflow-automation-strategy/)

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "DefinedTerm",
        "name": "Model Context Protocol (MCP)",
        "description": "The Model Context Protocol is an open standard for connecting AI models to external tools and data sources. An MCP server exposes capabilities - search a database, send an email, read a file - in a uniform format any MCP-compatible client can use. It replaces one-off integrations between each model and each tool with a single protocol on each side.",
        "dateModified": "2026-09-25",
        "datePublished": "2026-09-25",
        "inDefinedTermSet": {
          "@id": "https://martechsignal.com/glossary/#set"
        },
        "author": {
          "@type": "Person",
          "@id": "https://martechsignal.com/authors/tim-christensen/#person",
          "name": "Tim Christensen",
          "url": "https://martechsignal.com/authors/tim-christensen/"
        },
        "publisher": {
          "@id": "https://martechsignal.com/#organization"
        },
        "isPartOf": {
          "@id": "https://martechsignal.com/#website"
        },
        "url": "https://martechsignal.com/glossary/mcp/"
      },
      {
        "@type": "DefinedTermSet",
        "@id": "https://martechsignal.com/glossary/#set",
        "url": "https://martechsignal.com/glossary/",
        "name": "Martech Glossary"
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
        "name": "Glossary",
        "item": "https://martechsignal.com/glossary/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "MCP",
        "item": "https://martechsignal.com/glossary/mcp/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/glossary/mcp/", "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
