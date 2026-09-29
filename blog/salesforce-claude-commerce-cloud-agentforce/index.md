# Salesforce puts Claude in Commerce Cloud: a quiet admission


|  | Build it (Claude on MCP) | Buy it (native agents) |
| --- | --- | --- |
| **Where the agent runs** | Outside Salesforce, on the model you pick | Inside Commerce Cloud, Salesforce-managed |
| **Model choice** | "Claude or any model you choose" | Whatever Agentforce ships (Salesforce doesn't say) |
| **Surface** | Your interface: Claude, Slack, ChatGPT, or custom | Storefront Shopper Agent, back-office Merchant Agent |
| **Evidence offered** | Anthropic's blueprint: weeks of work cut to days | 86% faster merchant tasks; Cacau Show +32% conversion |
| **Guardrails** | MCP access "within guardrails" (details thin) | "Governed, embedded, and human-in-the-loop by design" |

TC **[Tim Christensen](/authors/tim-christensen/)**

Verdict: a win for merchants, a confession from Salesforce

AI AGENTS · SALESFORCE · 8 MIN

## Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough

SEP 29, 2026

Filed under [Marketing Automation](/categories/marketing-automation/)

On September 22, Salesforce published two blog posts. One, from the Commerce Cloud team, is titled "Build Agents Your Way with Claude and Commerce Cloud." It invites merchants to build commerce agents on Anthropic's Claude, and it names Claude as an intelligence layer that can sit on top of Salesforce's Commerce MCP server. The other, the [Dreamforce IT announcements recap](https://www.salesforce.com/blog/dreamforce-2026-top-it-announcements/), leads with AIforce, a platform layer that reaches every surface, where "Agentforce, Claude, or another agent of your choice" can take action inside your Salesforce permissions.

The Claude in both posts is Anthropic's model. Salesforce, the company that has sold Agentforce since 2024 as the way to build agents on its platform, is now publishing instructions for building agents on a competitor's model, working directly against Salesforce data through MCP.

That's not a partnership announcement. It's an admission about where agent building actually happens.

## What the Commerce Cloud post actually says

The post, by Katja Franz, Head of Merchant Experience at Salesforce Commerce Cloud, opens with Anthropic's [blueprint for building commerce agents on Claude](https://claude.com/blog/claude-for-commerce-agents). The kit ships reference code, guardrails, and best practices for two agents: a shopping agent that browses, compares, and buys, and a merchant agent that handles inventory, pricing, and promotions. Salesforce's own assessment of the kit: it "cuts weeks of engineering work down to days."

Here's the part worth reading twice. When the vendor that sells Agentforce evaluates Anthropic's kit, it doesn't say "use Agentforce instead." It offers a menu:

Salesforce's framing, from the post itself: "Build it: Our catalog, cart, checkout, and merchant APIs are open via MCP. Build your own agent experience with Claude or any model you choose." And: "Buy it: Commerce Cloud ships with Shopper Agent and Merchant Agent natively, out-of-the-box." The build path routes around Agentforce entirely. Model, agent loop, interface, memory, tool calls: all outside Salesforce. Only data and APIs stay in.

The "build" path never commits to a default model. Claude gets named in the intro and again in the build/buy list, and the official offer is "Claude or any model you choose." That's a signal without a commitment. Vendors name the model they want named, and Salesforce named Claude twice in one post on its own blog.

## The numbers Salesforce chose to share

All figures below come from the Franz post itself, reported by Salesforce, not independently measured. They're still worth taking seriously, because they show which story Salesforce wants merchants to believe.

For the native Merchant Agent: "Commerce Cloud customers using our Merchant Agent are already seeing early success... On average, this cuts time-to-task completion by over 86%." For the native Shopper Agent: "Cacau Show saw a 32% increase in conversion and a 50% increase in revenue after launching Shopper Agent on its site." No methodology, no sample size, no dates for either claim. That's normal for vendor blogs, and it's exactly why the "build" path exists: merchants with real operational data will eventually want to measure agents themselves.

The post also cites Salesforce's State of Commerce research: consumer use of agentic search as the first stop in shopping grew 200% year-over-year, and 90% of commerce leaders believe LLMs will be essential to product discovery by 2027. The number that matters operationally is the boring one: B2C Commerce exposes an MCP server to all merchants, so any agentic layer can read catalog, inventory, and pricing data within guardrails.

## Build path vs buy path, as Salesforce describes it

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

If you run Commerce Cloud, the MCP server plus Anthropic's blueprint is a real option, and Salesforce just told you so in writing. The native agents still make sense for teams that want Salesforce to own the loop, and the vendor-reported numbers are the only evidence on that side. But the "build it" menu item wouldn't exist if Agentforce had closed the question. My read: it's on the menu because customers kept asking for the model they already use.

Vendor pages checked September 29, 2026. All performance figures are Salesforce's own claims from the linked posts.

Tools linked in this post: [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) | [Salesforce CRM](/tools/salesforce-crm/) | [Anthropic Claude](https://claude.com) | [OpenAI ChatGPT](https://chatgpt.com) | [Slack](https://slack.com)

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
## Related tools

- [Writer](/tools/writer/) - Enterprise AI platform with Palmyra models, brand governance, and agents
- [Cordys CRM](/tools/cordys-crm/) - Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [Bloomreach](/tools/bloomreach/) - AI-powered commerce experience platform with search, personalization, and CDP
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Best workflow automation tools (2026)](/best/workflow-automation-tools/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
- [MCP](/glossary/mcp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

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
  "headline": "Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough",
  "description": "On September 22, Salesforce published two blog posts. One, from the Commerce Cloud team, is titled \"Build Agents Your Way with Claude and Commerce.",
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
  "datePublished": "2026-09-29",
  "dateModified": "2026-09-29",
  "mainEntityOfPage": "https://martechsignal.com/blog/salesforce-claude-commerce-cloud-agentforce/",
  "image": {
    "@type": "ImageObject",
    "url": "https://martechsignal.com/og/salesforce-claude-commerce-cloud-agentforce.png",
    "width": 1200,
    "height": 630
  },
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 1506,
  "articleSection": "marketing-automation"
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
      "name": "Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough",
      "item": "https://martechsignal.com/blog/salesforce-claude-commerce-cloud-agentforce/"
    }
  ]
}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
