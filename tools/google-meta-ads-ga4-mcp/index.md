# Google Ads + Meta Ads + GA4 MCP pricing


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: 250+ MCP tools for campaign management, analytics, and optimization |  |
| &#10003; Established community (1,672 GitHub stars) |  |
| &#10003; Native integrations include Google Ads, Meta Ads, GA4 (11 listed) |  |

**What is Google Ads + Meta Ads + GA4 MCP?**
MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. It ships with 250+ MCP tools for campaign management, analytics, and optimization, 1,672 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Google Ads + Meta Ads + GA4 MCP cost?**
Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 1,672 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences.

**Is Google Ads + Meta Ads + GA4 MCP worth it past the free tier?**
High-value tooling for performance teams already running agents and MCP. Keep human approval on every write.

**How many tools does the Google Ads + Meta Ads + GA4 MCP server expose?**
The README claims 250+ tools across three APIs: 150+ for Google Ads, covering campaign management, Keyword Planner research, bidding and budgets, audiences, extensions, experiments, negative keywords, labels, and conversion tracking; 80+ for Meta Ads, covering campaigns, ad sets, creatives, audiences, lead gen, catalogs, and insights; and 20+ for GA4, covering reporting, audiences, property config, attribution, and key events. A separate six tool research set handles search, webpage analysis, stock images, and landing page fetches. Those are the README&#x27;s own numbers, not a tool by tool count of ours.

**What credentials do I need to set it up?**
Fewer than three ad APIs would suggest. There is no Google Ads client file, no Meta access token, and no GA4 service account JSON to manage. Setup points your client at the hosted endpoint connector.get-ryze.ai/mcp, and auth is OAuth 2.1 with PKCE, so you connect your Google and Meta accounts on first use. The README states the server stores no ad data or credentials. It is MIT licensed, but no self host path is documented; the repo reads as a hosted endpoint rather than a local install.

**Can it edit campaigns, or is it read only?**
The README claims full read and write across all three platforms and contrasts that with the official Google Ads MCP, which it describes as read only. Writes are gated: the README says the server is read only by default and that write operations require explicit confirmation. That is documented rather than independently tested, so keep a human approving anything that moves budget.

**How much does it cost?**
Two layers. The repo is MIT licensed and its pricing FAQ states the MCP server itself is free, with you paying only for the AI assistant you use and your ad spend. The hosted endpoint is run by Ryze AI, whose own plans start at $89 a month for Paid ads Autopilot with a 7 day free trial and scale to $1,499 for Ecom Autopilot. If you want only the MCP connection and not Ryze&#x27;s managed services, confirm what the free path covers before you build on it.

- **Pricing:** Freemium
- **Category:** [Agent Skills](/categories/agent-skills/)
- **GitHub:** ★ 1672
- **Founded:** 2026
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Google Ads + Meta Ads + GA4 MCP is a freemium in Agent Skills, a public API, self-hosting. The catalog documents 5 AI features, 11 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Claude Ads

Paid-media operations skill for Claude Code covering 12 ad platforms

OpenClaw Marketing Skills

37 marketing skills for OpenClaw agents with live data connectors

Claude SEO

Open-source SEO skill for Claude Code with 25 sub-skills and 18 parallel agents

Albert AI

Autonomous AI platform that manages and optimizes digital advertising campaigns

[More Agent Skills Tools →](/categories/agent-skills/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Agent Skills](/categories/agent-skills/)
- Google Ads + Meta Ads + GA4 MCP
KIND: Utility (not an end-to-end platform)

## Google Ads + Meta Ads + GA4 MCP review (2026): pricing, AI features, verdict

MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4

Agent Skills · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[How we review](/methodology/) · No affiliate links

[Visit Google Ads + Meta Ads + GA4 MCP &#8594;](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

google-meta-ads-ga4-mcp is an MCP server that lets AI assistants manage Google Ads, Meta Ads, and GA4 from one conversation. Instead of jumping between three dashboards, you ask Claude or ChatGPT to pull campaign performance, pause ad sets, build audiences, or reconcile ad spend against GA4 conversions. It exposes 250+ tools: roughly 150 for Google Ads (campaign CRUD across Search, Display, Shopping, PMax, and Video, Keyword Planner data, bidding and budget controls, experiments, conversion tracking), 80+ for Meta Ads (campaigns, ad sets, creatives, lookalikes, lead forms, product catalogs), and 20+ for GA4 (standard and realtime reports, audiences, attribution settings, key events). Day to day, the value is in cross-platform work that usually means exporting CSVs. You can compare Google versus Meta spend side by side, correlate ad cost with GA4 conversion events, and ask for a unified ROAS read across both networks. The repo ships with 60+ example prompts and an n8n workflow template. Write access is a deliberate choice: the official Google MCP server is read-only, while this one can create, pause, and delete campaigns. That power means you should gate it carefully. Give it a test account first, and keep a human approving anything that touches budgets. Setup is remote rather than local. You add an endpoint URL to claude_desktop_config.json, Cursor, Windsurf, ChatGPT connectors, or n8n&#x27;s MCP node. There&#x27;s no local code to run and no API keys to manage in config files, but the endpoint comes from Ryze AI (Meow AI, LLC), the company behind the repo. The code is MIT licensed and free, but the hosted server is tied to Ryze&#x27;s trial and paid plans, so treat this as freemium infrastructure rather than a standalone open-source deployment. The repo launched in April 2026 and picked up over 1,000 stars quickly; most of that momentum is marketing from Ryze&#x27;s blog, which is worth keeping in mind. Versus the official Google Ads MCP server, this one trades vendor independence for reach and write access. Versus the Claude Ads skill pack already in this directory, the roles differ: Claude Ads is the analyst that audits and plans, while this MCP server is the plumbing that lets any MCP-compatible agent reach live accounts. If you run an agent stack around n8n or Claude Code and manage spend on both Google and Meta, it&#x27;s the fastest way to give your agents hands on the ad accounts. Just remember that hands can also delete things.

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

MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. It ships with 250+ MCP tools for campaign management, analytics, and optimization, 1,672 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 1,672 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences.

High-value tooling for performance teams already running agents and MCP. Keep human approval on every write.

The README claims 250+ tools across three APIs: 150+ for Google Ads, covering campaign management, Keyword Planner research, bidding and budgets, audiences, extensions, experiments, negative keywords, labels, and conversion tracking; 80+ for Meta Ads, covering campaigns, ad sets, creatives, audiences, lead gen, catalogs, and insights; and 20+ for GA4, covering reporting, audiences, property config, attribution, and key events. A separate six tool research set handles search, webpage analysis, stock images, and landing page fetches. Those are the README&#x27;s own numbers, not a tool by tool count of ours.

Fewer than three ad APIs would suggest. There is no Google Ads client file, no Meta access token, and no GA4 service account JSON to manage. Setup points your client at the hosted endpoint connector.get-ryze.ai/mcp, and auth is OAuth 2.1 with PKCE, so you connect your Google and Meta accounts on first use. The README states the server stores no ad data or credentials. It is MIT licensed, but no self host path is documented; the repo reads as a hosted endpoint rather than a local install.

The README claims full read and write across all three platforms and contrasts that with the official Google Ads MCP, which it describes as read only. Writes are gated: the README says the server is read only by default and that write operations require explicit confirmation. That is documented rather than independently tested, so keep a human approving anything that moves budget.

Two layers. The repo is MIT licensed and its pricing FAQ states the MCP server itself is free, with you paying only for the AI assistant you use and your ad spend. The hosted endpoint is run by Ryze AI, whose own plans start at $89 a month for Paid ads Autopilot with a 7 day free trial and scale to $1,499 for Ecom Autopilot. If you want only the MCP connection and not Ryze&#x27;s managed services, confirm what the free path covers before you build on it.

## Similar Tools

## Related reading

- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Fifty days of open-source MarTech, audited](/blog/oss-martech-50-day-checkin/)
- [Zapier vs. Make: Two Ways to Buy the Same Workflow Debt](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
### Quick Facts

Related guides: [Agent Skills Tools](/best/agent-skills-tools)

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
    "dateModified": "2026-09-07",
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
          "text": "MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4. It ships with 250+ MCP tools for campaign management, analytics, and optimization, 1,672 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Google Ads + Meta Ads + GA4 MCP cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Google Ads + Meta Ads + GA4 MCP is open source - MIT licensed and free to self-host; the public repository carries 1,672 stars; native integrations cover Google Ads, Meta Ads, GA4. You pay in server time and maintenance, not licences."
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
  }
]
```
