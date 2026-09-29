# Google Ads + Meta Ads + GA4 MCP pricing


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | MIT-licensed repo free; the hosted endpoint has a free trial then paid plans, both stated (the vendor pricing page: [pricing page](https://www.get-ryze.ai/payment-setup), verified 2026-09-07). |
| Feature depth | 7/10 | 250+ MCP tools spanning campaign management, analytics and optimization across three surfaces (vendor documentation: [vendor site](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), verified 2026-09-28). |
| Integrations | 8/10 | Google Ads, Meta Ads and GA4 plus nine named agent clients from Claude Code to n8n and Gemini CLI (vendor documentation: [vendor site](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), verified 2026-09-28). |
| AI capability | 7/10 | Natural-language campaign creation and pausing through MCP is the documented agent workflow (vendor documentation: [vendor site](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), verified 2026-09-28). |
| Openness | 8/10 | MIT-licensed with a self-hostable server (the source repository: [repository](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2026 with a hosted service forming behind it (vendor documentation: [vendor site](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: 250+ MCP tools for campaign management, analytics, and optimization |  |
| ✓ Active public repository (3,078 GitHub stars counted at last check) |  |
| ✓ Native integrations include Google Ads, Meta Ads, GA4 (11 listed) |  |

**What is Google Ads + Meta Ads + GA4 MCP?**
Google Ads + Meta Ads + GA4 MCP: MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. Google Ads + Meta Ads + GA4 MCP ships with 250+ MCP tools for campaign management, analytics, and optimization. The public repository carries 3,078 stars.

**How much does Google Ads + Meta Ads + GA4 MCP cost?**
Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 3,078 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences.

**Is Google Ads + Meta Ads + GA4 MCP worth it past the free tier?**
High-value tooling for performance teams already running agents and MCP. Keep human approval on every write.

**How many tools does the Google Ads + Meta Ads + GA4 MCP server expose?**
The README claims 250+ tools across three APIs: 150+ for Google Ads, covering campaign management, Keyword Planner research, bidding and budgets, audiences, extensions, experiments, negative keywords, labels, and conversion tracking; 80+ for Meta Ads, covering campaigns, ad sets, creatives, audiences, lead gen, catalogs, and insights; and 20+ for GA4, covering reporting, audiences, property config, attribution, and key events. A separate six tool research set handles search, webpage analysis, stock images, and landing page fetches. Those are the README's own numbers, not a tool by tool count of ours.

**What credentials do I need to set it up?**
Fewer than three ad APIs would suggest. There is no Google Ads client file, no Meta access token, and no GA4 service account JSON to manage. Setup points your client at the hosted endpoint connector.get-ryze.ai/mcp, and auth is OAuth 2.1 with PKCE, so you connect your Google and Meta accounts on first use. The README states the server stores no ad data or credentials. It is MIT licensed, but no self host path is documented; the repo reads as a hosted endpoint rather than a local install.

**Can it edit campaigns, or is it read only?**
The README claims full read and write across all three platforms and contrasts that with the official Google Ads MCP, which it describes as read only. Writes are gated: the README says the server is read only by default and that write operations require explicit confirmation. That is documented rather than independently tested, so keep a human approving anything that moves budget.

**How much does it cost?**
Two layers. The repo is MIT licensed and its pricing FAQ states the MCP server itself is free, with you paying only for the AI assistant you use and your ad spend. The hosted endpoint is run by Ryze AI, whose own plans start at $89 a month for Paid ads Autopilot with a 7 day free trial and scale to $1,499 for Ecom Autopilot. If you want only the MCP connection and not Ryze's managed services, confirm what the free path covers before you build on it.

- **Pricing:** Freemium
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 3078
- **Founded:** 2026
- **API:** Yes
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-07

**Verdict:** Google Ads + Meta Ads + GA4 MCP is a tool in Agent Skills with free and open source. The catalog documents 5 AI features, 11 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Claude Ads

Paid-media operations skill for Claude Code covering 12 ad platforms

OpenClaw Marketing Skills

37 marketing skills for OpenClaw agents with live data connectors

Claude SEO

Open-source SEO skill for Claude Code with 25 sub-skills and 20 specialist agents

Albert AI

Autonomous AI platform that manages and optimizes digital advertising campaigns

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Google Ads + Meta Ads + GA4 MCP
Re-check pending: pricing last verified 2026-09-07 (23 days ago).

KIND: Utility (not an end-to-end platform)

## Google Ads + Meta Ads + GA4 MCP review (2026): pricing, AI features, verdict

MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4

Agent Skills · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Google Ads + Meta Ads + GA4 MCP →](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)

[How we review](/methodology/) · No affiliate links

[Visit Google Ads + Meta Ads + GA4 MCP →](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)

## MartechSignal Score: 41/60

This MCP server gives agents read/write control of Google Ads, Meta Ads and GA4 through 250+ tools. The repo is MIT; the hosted endpoint is the business model, so self-host if that matters.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

google-meta-ads-ga4-mcp is an MCP server that lets AI assistants manage Google Ads, Meta Ads, and GA4 from one conversation. Instead of jumping between three dashboards, you ask Claude or ChatGPT to pull campaign performance, pause ad sets, build audiences, or reconcile ad spend against GA4 conversions. It exposes 250+ tools: roughly 150 for Google Ads (campaign CRUD across Search, Display, Shopping, PMax, and Video, Keyword Planner data, bidding and budget controls, experiments, conversion tracking), 80+ for Meta Ads (campaigns, ad sets, creatives, lookalikes, lead forms, product catalogs), and 20+ for GA4 (standard and realtime reports, audiences, attribution settings, key events). Day to day, the value is in cross-platform work that usually means exporting CSVs. You can compare Google versus Meta spend side by side, correlate ad cost with GA4 conversion events, and ask for a unified ROAS read across both networks. The repo ships with 60+ example prompts and an n8n workflow template. Write access is a deliberate choice: the official Google MCP server is read-only, while this one can create, pause, and delete campaigns. That power means you should gate it carefully. Give it a test account first, and keep a human approving anything that touches budgets. Setup is remote rather than local. You add an endpoint URL to claude_desktop_config.json, Cursor, Windsurf, ChatGPT connectors, or n8n's MCP node. There's no local code to run and no API keys to manage in config files, but the endpoint comes from Ryze AI (Meow AI, LLC), the company behind the repo. The code is MIT licensed and free, but the hosted server is tied to Ryze's trial and paid plans, so treat this as freemium infrastructure rather than a standalone open-source deployment. The repo launched in April 2026 and picked up thousands of stars quickly; most of that momentum is marketing from Ryze's blog, which is worth keeping in mind. Versus the official Google Ads MCP server, this one trades vendor independence for reach and write access. Versus the Claude Ads skill pack already in this directory, the roles differ: Claude Ads is the analyst that audits and plans, while this MCP server is the plumbing that lets any MCP-compatible agent reach live accounts. If you run an agent stack around n8n or Claude Code and manage spend on both Google and Meta, it's the fastest way to give your agents hands on the ad accounts. Just remember that hands can also delete things.

Google Ads + Meta Ads + GA4 MCP homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- 250+ MCP tools for campaign management, analytics, and optimization
- Natural-language campaign creation and pausing across Google and Meta
- Keyword Planner research with volume, CPC, and competition data
- Cross-platform ROAS analysis correlating ad spend with GA4 conversions
- Scheduled actions and audit reports via ChatGPT, Claude, or n8n
## Key Integrations

- Google Ads
- Meta Ads
- GA4
- ChatGPT
- Claude
- Claude Code
- Cursor
- Windsurf
- n8n
- Codex CLI
- Gemini CLI
## Pricing

Google Ads + Meta Ads + GA4 MCP is freemium, with a free tier to start.

MIT-licensed repo; hosted MCP endpoint provided through Ryze AI (free trial, then paid plans).

Current plans and limits live on the [Google Ads + Meta Ads + GA4 MCP pricing page](https://www.get-ryze.ai/payment-setup).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

This MCP server hands your AI agent read and write access to Google Ads, Meta Ads, and GA4: roughly 150 Google Ads tools for campaign, keyword, bidding, budget, and conversion work, 80-plus Meta tools across campaigns, creatives, lookalikes, and lead forms, and GA4 reporting to reconcile spend against conversions. You ask for a performance summary or a paused ad set and it executes, no dashboard hopping.

The power cuts both ways. This is real spend and real changes executed from chat, so guardrails matter: review every write, keep human approval in the loop, and scope the API keys tightly. Setup means Google Cloud project work and a Meta app registration, so it is for teams comfortable with MCP plumbing. For those teams, the workflow compression is dramatic and the 1,000-plus stars show rapid adoption.

## Verdict

High-value tooling for performance teams already running agents and MCP. Keep human approval on every write.

## Pros and cons

## Related concepts

- [MCP](/glossary/mcp/)
- [Agentic Marketing](/glossary/agentic-marketing/)
- [AI Agent](/glossary/ai-agent/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Google Ads + Meta Ads + GA4 MCP: MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. Google Ads + Meta Ads + GA4 MCP ships with 250+ MCP tools for campaign management, analytics, and optimization. The public repository carries 3,078 stars.

Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 3,078 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences.

High-value tooling for performance teams already running agents and MCP. Keep human approval on every write.

The README claims 250+ tools across three APIs: 150+ for Google Ads, covering campaign management, Keyword Planner research, bidding and budgets, audiences, extensions, experiments, negative keywords, labels, and conversion tracking; 80+ for Meta Ads, covering campaigns, ad sets, creatives, audiences, lead gen, catalogs, and insights; and 20+ for GA4, covering reporting, audiences, property config, attribution, and key events. A separate six tool research set handles search, webpage analysis, stock images, and landing page fetches. Those are the README's own numbers, not a tool by tool count of ours.

Fewer than three ad APIs would suggest. There is no Google Ads client file, no Meta access token, and no GA4 service account JSON to manage. Setup points your client at the hosted endpoint connector.get-ryze.ai/mcp, and auth is OAuth 2.1 with PKCE, so you connect your Google and Meta accounts on first use. The README states the server stores no ad data or credentials. It is MIT licensed, but no self host path is documented; the repo reads as a hosted endpoint rather than a local install.

The README claims full read and write across all three platforms and contrasts that with the official Google Ads MCP, which it describes as read only. Writes are gated: the README says the server is read only by default and that write operations require explicit confirmation. That is documented rather than independently tested, so keep a human approving anything that moves budget.

Two layers. The repo is MIT licensed and its pricing FAQ states the MCP server itself is free, with you paying only for the AI assistant you use and your ad spend. The hosted endpoint is run by Ryze AI, whose own plans start at $89 a month for Paid ads Autopilot with a 7 day free trial and scale to $1,499 for Ecom Autopilot. If you want only the MCP connection and not Ryze's managed services, confirm what the free path covers before you build on it.

## Similar Tools

## Related reading

- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [MCP Rewrites the Integration Economics of Your Marketing Stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
## Also featured in

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/) — Best for performance teams that want Google Ads, Meta Ads and GA4 reachable from one MCP server, free to self-host.
### Quick Facts

Related guides: [Agent Skills Tools](/best/agent-skills-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/#app",
    "name": "Google Ads + Meta Ads + GA4 MCP",
    "description": "MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4",
    "image": "https://martechsignal.com/og/tools/google-meta-ads-ga4-mcp.png",
    "url": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/",
    "sameAs": [
      "https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-08-17",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.get-ryze.ai/payment-setup",
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
        "name": "Agent Skills",
        "item": "https://martechsignal.com/categories/agent-skills/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Google Ads + Meta Ads + GA4 MCP",
        "item": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Google Ads + Meta Ads + GA4 MCP?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Google Ads + Meta Ads + GA4 MCP: MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. Google Ads + Meta Ads + GA4 MCP ships with 250+ MCP tools for campaign management, analytics, and optimization. The public repository carries 3,078 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Google Ads + Meta Ads + GA4 MCP cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 3,078 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Google Ads + Meta Ads + GA4 MCP worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "High-value tooling for performance teams already running agents and MCP. Keep human approval on every write."
        }
      },
      {
        "@type": "Question",
        "name": "How many tools does the Google Ads + Meta Ads + GA4 MCP server expose?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The README claims 250+ tools across three APIs: 150+ for Google Ads, covering campaign management, Keyword Planner research, bidding and budgets, audiences, extensions, experiments, negative keywords, labels, and conversion tracking; 80+ for Meta Ads, covering campaigns, ad sets, creatives, audiences, lead gen, catalogs, and insights; and 20+ for GA4, covering reporting, audiences, property config, attribution, and key events. A separate six tool research set handles search, webpage analysis, stock images, and landing page fetches. Those are the README's own numbers, not a tool by tool count of ours."
        }
      },
      {
        "@type": "Question",
        "name": "What credentials do I need to set it up?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Fewer than three ad APIs would suggest. There is no Google Ads client file, no Meta access token, and no GA4 service account JSON to manage. Setup points your client at the hosted endpoint connector.get-ryze.ai/mcp, and auth is OAuth 2.1 with PKCE, so you connect your Google and Meta accounts on first use. The README states the server stores no ad data or credentials. It is MIT licensed, but no self host path is documented; the repo reads as a hosted endpoint rather than a local install."
        }
      },
      {
        "@type": "Question",
        "name": "Can it edit campaigns, or is it read only?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The README claims full read and write across all three platforms and contrasts that with the official Google Ads MCP, which it describes as read only. Writes are gated: the README says the server is read only by default and that write operations require explicit confirmation. That is documented rather than independently tested, so keep a human approving anything that moves budget."
        }
      },
      {
        "@type": "Question",
        "name": "How much does it cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Two layers. The repo is MIT licensed and its pricing FAQ states the MCP server itself is free, with you paying only for the AI assistant you use and your ad spend. The hosted endpoint is run by Ryze AI, whose own plans start at $89 a month for Paid ads Autopilot with a 7 day free trial and scale to $1,499 for Ecom Autopilot. If you want only the MCP connection and not Ryze's managed services, confirm what the free path covers before you build on it."
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
    "reviewBody": "This MCP server gives agents read/write control of Google Ads, Meta Ads and GA4 through 250+ tools. The repo is MIT; the hosted endpoint is the business model, so self-host if that matters.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/#app",
      "name": "Google Ads + Meta Ads + GA4 MCP",
      "url": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 41,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/", "breadcrumb": {"@id": "https://martechsignal.com/tools/google-meta-ads-ga4-mcp/#breadcrumb"}, "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
