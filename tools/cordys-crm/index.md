# Cordys CRM review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | Community edition free and self-hosted with a 1,000 calls/day API cap; Enterprise is published in CNY (30,000/60,000 per year) (the vendor pricing page: [pricing page](https://cordys.cn/pricing.html), verified 2026-09-07). |
| Feature depth | 6/10 | CRM core with built-in agents, embedded BI and conversational analytics covers the modern SMB promise (vendor documentation: [vendor site](https://cordys.cn), verified 2026-09-28). |
| Integrations | 4/10 | MaxKB, DataEase, MCP and Docker documented; the MCP server ships 11 tools but there is no marketplace (vendor documentation: [vendor site](https://cordys.cn), verified 2026-09-28). |
| AI capability | 7/10 | MaxKB sales agents over the API, a server-side AI agent in enterprise and an MCP server with 11 tools (vendor documentation: [vendor site](https://cordys.cn), verified 2026-09-28). |
| Openness | 8/10 | GPLv3-based licence with 2.7k GitHub stars and full self-hosting in the community edition (the source repository: [repository](1Panel-dev/CordysCRM), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2025 with 2.7k stars; enterprise subscriptions exist but the history is short (vendor documentation: [vendor site](https://cordys.cn), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; GPL-3.0 licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: maxKB sales agents connected over the API |  |
| &#10003; Active public repository (2,704 GitHub stars counted at last check) |  |

**What is Cordys CRM?**
Open-source AI CRM with built-in agents, conversational analytics, and private deployment. It ships with maxKB sales agents connected over the API, 2,704 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Cordys CRM cost?**
Cordys CRM is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,704 stars; native integrations cover MaxKB, DataEase, MCP. You pay in server time and maintenance, not licences.

**Is Cordys CRM worth it past the free tier?**
Watch it for self-hosted CRM needs. The feature ceiling is below Salesforce, but the cost floor is unbeatable.

**Is Cordys CRM really free?**
Yes. The community edition is free and self-hosted under a GPLv3-based license. The enterprise edition adds paid support tiers with annual subscription, still without per-seat fees.

**Who makes Cordys CRM?**
FIT2CLOUD, the Chinese software company behind 1Panel, JumpServer, and MaxKB, released Cordys CRM in 2025 as an open-source AI-native CRM for teams that want sales data on their own servers.

**Is Cordys CRM a good Salesforce alternative?**
For mid-size teams that can self-host a Java stack, it covers leads, contacts, opportunities, contracts, orders, and payments with AI agents built in. It lacks the third-party ecosystem and compliance certifications of Salesforce.

**What do I need to run Cordys CRM?**
A Linux host with at least 4 CPU cores, 8 GB of RAM, and 100 GB of disk, kernel 3.10 or newer, and Docker 23 or newer recommended. The web UI sits on port 8081 and the MCP server on 8082. MySQL and Redis are embedded by default and can be switched to external instances through cordys-crm.properties. The default login is admin with the password CordysCRM, which you should change before anything touches the network. The backend is Spring Boot with a Vue frontend.

**What can AI agents do through the Cordys MCP server?**
Eleven documented tools: a global search across objects, add and update for leads, accounts, and contacts, add and update for opportunities, and creation of follow records and follow plans. Auth is via X-Access-Key and X-Secret-Key headers over SSE or Streamable HTTP, and the input schema for each tool is generated from your tenant&#x27;s own dynamic form fields, including required lists and enum values. CORDYS AI, the built-in agent, is enterprise only and runs server side in the CRM&#x27;s trust domain, reusing RBAC, so deletes still need manual confirmation.

**How much does Cordys CRM cost for a company?**
The community edition is free and self-hosted under a GPLv3-based license, with two strings attached: no swapping out the logo or copyright notices, and an API capped at 1,000 calls a day. Enterprise is published at ¥30,000, ¥60,000, and ¥120,000 per year, tiered by company revenue, with unlimited API calls, custom branding, embedded DataEase, and a built-in AI workbench; flagship adds hot-standby and distributed high availability. Budget separately for a DataEase commercial edition if you want BI dashboards embedded.

- **Pricing:** Freemium
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 2704
- **Founded:** 2025
- **HQ:** China
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Cordys CRM is a tool in CRM with free and open source. The catalog documents 5 AI features, 4 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Twenty

The open-source alternative to Salesforce, designed for AI with modern CRM workflows

DeskcommCRM

Self-hosted open-source CRM with AI agents that sell through WhatsApp

Frappe CRM

Fully featured, open source CRM

Tealium

Enterprise customer data platform with real-time data orchestration and AI

Dolibarr ERP/CRM

Modular French open-source ERP/CRM: invoicing, stock, HR, and light CRM in one PHP app

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Cordys CRM
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Cordys CRM review (2026): pricing, AI features, verdict

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

CRM · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Cordys CRM &#8594;](https://cordys.cn)

[How we review](/methodology/) · No affiliate links

[Visit Cordys CRM &#8594;](https://cordys.cn)

## MartechSignal Score: 35/60

Cordys CRM is the agent-native open-source CRM for teams that want conversational analytics and private deployment in one stack. The enterprise edition prices in CNY, which tells you where its center of gravity is.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Cordys CRM is an open-source, AI-native CRM from FIT2CLOUD, the Chinese software company behind 1Panel, JumpServer, and MaxKB. It covers the full lead-to-cash cycle: lead capture and routing, customer and contact management, opportunities, contracts, orders, and payment collection. The pitch is a self-hosted Salesforce alternative for mid-size and large teams that want their sales data on their own servers. It&#x27;s Java (Spring Boot) on the backend with a Vue frontend, ships as a Docker install, and hit 100,000 downloads within 25 days of its August 2025 public beta. The AI part is real, not a bolted-on chatbot. The AI is assembled from outside rather than built in. MaxKB, FIT2CLOUD&#x27;s agent platform, connects over the API to run sales agents for lead triage and follow-up drafting. DataEase handles embedded BI dashboards, and that integration requires a DataEase commercial edition. Conversational SQL analytics is not part of the product: SQLBot appears only in FIT2CLOUD&#x27;s sibling product navigation, with no Cordys documentation behind it. CORDYS AI, added in v1.9.0, is the server-side agent, it is enterprise only, and it reuses the CRM&#x27;s RBAC so reads run directly, writes are permission checked, and deletes need manual confirmation. There&#x27;s also an MCP server, so outside agents (Claude, Cursor, and similar) can read and act on CRM data directly. Since v1.8.1 the free community edition exposes the API and MCP access too, capped at 1,000 API calls a day, which is unusual. The catch is that you&#x27;re really running three systems in a trench coat, and the setup and upkeep reflect that. Pricing skips per-seat fees entirely. The community edition is free and self-hosted under a GPLv3-based license (the FIT2CLOUD Open Source License) that bars you from swapping out the logo or copyright notices. The enterprise edition is an annual subscription in standard, professional, and flagship tiers, published at ¥30,000, ¥60,000, and ¥120,000 a year by company revenue, with flagship adding hot-standby and distributed high availability. The no-per-seat model can work out far cheaper than Salesforce or HubSpot for a 100-person sales team, but you&#x27;re trading license cost for hosting and ops effort. Against Twenty, the other big open-source CRM in this directory, Cordys goes deeper on native AI (Twenty&#x27;s AI is lighter and its community is more global) but feels less polished and skews heavily toward the Chinese market. EspoCRM is easier to stand up and lighter to run, but has no comparable AI layer. If you want Salesforce-style depth with AI agents baked in and no per-seat bill, and you&#x27;re comfortable self-hosting, Cordys is worth a serious look. Who should skip it: anyone who needs a SaaS product that just works without a server, teams outside China who want English-first docs and community support (the docs and forums are Chinese-first), and small teams that don&#x27;t have Java ops capacity. The stack is heavier than a typical PHP CRM, and the enterprise motion is built around Chinese enterprises. For a China-based sales team that wants private deployment and real AI features without per-seat fees, though, it&#x27;s one of the few open-source options that delivers both.

Cordys CRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- MaxKB sales agents connected over the API
- CORDYS AI server-side agent (enterprise edition)
- DataEase embedded BI dashboards
- MCP server with 11 tools for external AI agents
- AI lead routing and follow-up
## Key Integrations

- MaxKB
- DataEase
- MCP
- Docker
## Pricing

Cordys CRM is freemium, with a free tier to start.

Community edition free and self-hosted (GPLv3-based license, API capped at 1,000 calls/day). Enterprise edition: annual subscription published at ¥30,000 / ¥60,000 / ¥120,000 per year by company revenue, no per-seat fees, flagship adds hot-standby HA. DataEase embedding requires a DataEase commercial edition.

Current plans and limits live on the [Cordys CRM pricing page](https://cordys.cn/pricing.html).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Cordys CRM is an open-source, self-hosted CRM with AI features aimed at the Salesforce-alternative segment. It emphasizes lead-to-cash workflows and private deployment. The repo is active and the feature set is broad for the price (free). The UI is functional rather than slick, and enterprise-grade polish, like advanced permissions and audit depth, is still maturing.

GSC data shows &#x27;cordys crm&#x27; queries ranking this page around position 7 with impressions climbing, meaning name-brand demand exists. For a team that wants an owned CRM stack without per-seat fees, it is the credible open-source candidate.

## Verdict

Watch it for self-hosted CRM needs. The feature ceiling is below Salesforce, but the cost floor is unbeatable.

## Pros and cons

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source AI CRM with built-in agents, conversational analytics, and private deployment. It ships with maxKB sales agents connected over the API, 2,704 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Cordys CRM is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,704 stars; native integrations cover MaxKB, DataEase, MCP. You pay in server time and maintenance, not licences.

Watch it for self-hosted CRM needs. The feature ceiling is below Salesforce, but the cost floor is unbeatable.

Yes. The community edition is free and self-hosted under a GPLv3-based license. The enterprise edition adds paid support tiers with annual subscription, still without per-seat fees.

FIT2CLOUD, the Chinese software company behind 1Panel, JumpServer, and MaxKB, released Cordys CRM in 2025 as an open-source AI-native CRM for teams that want sales data on their own servers.

For mid-size teams that can self-host a Java stack, it covers leads, contacts, opportunities, contracts, orders, and payments with AI agents built in. It lacks the third-party ecosystem and compliance certifications of Salesforce.

A Linux host with at least 4 CPU cores, 8 GB of RAM, and 100 GB of disk, kernel 3.10 or newer, and Docker 23 or newer recommended. The web UI sits on port 8081 and the MCP server on 8082. MySQL and Redis are embedded by default and can be switched to external instances through cordys-crm.properties. The default login is admin with the password CordysCRM, which you should change before anything touches the network. The backend is Spring Boot with a Vue frontend.

Eleven documented tools: a global search across objects, add and update for leads, accounts, and contacts, add and update for opportunities, and creation of follow records and follow plans. Auth is via X-Access-Key and X-Secret-Key headers over SSE or Streamable HTTP, and the input schema for each tool is generated from your tenant&#x27;s own dynamic form fields, including required lists and enum values. CORDYS AI, the built-in agent, is enterprise only and runs server side in the CRM&#x27;s trust domain, reusing RBAC, so deletes still need manual confirmation.

The community edition is free and self-hosted under a GPLv3-based license, with two strings attached: no swapping out the logo or copyright notices, and an API capped at 1,000 calls a day. Enterprise is published at ¥30,000, ¥60,000, and ¥120,000 per year, tiered by company revenue, with unlimited API calls, custom branding, embedded DataEase, and a built-in AI workbench; flagship adds hot-standby and distributed high availability. Budget separately for a DataEase commercial edition if you want BI dashboards embedded.

## Similar Tools

## Related reading

- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/cordys-crm/#app",
    "name": "Cordys CRM",
    "description": "Open-source AI CRM with built-in agents, conversational analytics, and private deployment",
    "image": "https://martechsignal.com/og/tools/cordys-crm.png",
    "url": "https://martechsignal.com/tools/cordys-crm/",
    "sameAs": [
      "https://cordys.cn"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/cordys-crm/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-14",
    "datePublished": "2026-07-31",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://cordys.cn/pricing.html",
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
        "name": "CRM",
        "item": "https://martechsignal.com/categories/crm/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Cordys CRM",
        "item": "https://martechsignal.com/tools/cordys-crm/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Cordys CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source AI CRM with built-in agents, conversational analytics, and private deployment. It ships with maxKB sales agents connected over the API, 2,704 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Cordys CRM cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Cordys CRM is open source - GPL-3.0 licensed and free to self-host; the public repository carries 2,704 stars; native integrations cover MaxKB, DataEase, MCP. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Cordys CRM worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Watch it for self-hosted CRM needs. The feature ceiling is below Salesforce, but the cost floor is unbeatable."
        }
      },
      {
        "@type": "Question",
        "name": "Is Cordys CRM really free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. The community edition is free and self-hosted under a GPLv3-based license. The enterprise edition adds paid support tiers with annual subscription, still without per-seat fees."
        }
      },
      {
        "@type": "Question",
        "name": "Who makes Cordys CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "FIT2CLOUD, the Chinese software company behind 1Panel, JumpServer, and MaxKB, released Cordys CRM in 2025 as an open-source AI-native CRM for teams that want sales data on their own servers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Cordys CRM a good Salesforce alternative?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "For mid-size teams that can self-host a Java stack, it covers leads, contacts, opportunities, contracts, orders, and payments with AI agents built in. It lacks the third-party ecosystem and compliance certifications of Salesforce."
        }
      },
      {
        "@type": "Question",
        "name": "What do I need to run Cordys CRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A Linux host with at least 4 CPU cores, 8 GB of RAM, and 100 GB of disk, kernel 3.10 or newer, and Docker 23 or newer recommended. The web UI sits on port 8081 and the MCP server on 8082. MySQL and Redis are embedded by default and can be switched to external instances through cordys-crm.properties. The default login is admin with the password CordysCRM, which you should change before anything touches the network. The backend is Spring Boot with a Vue frontend."
        }
      },
      {
        "@type": "Question",
        "name": "What can AI agents do through the Cordys MCP server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Eleven documented tools: a global search across objects, add and update for leads, accounts, and contacts, add and update for opportunities, and creation of follow records and follow plans. Auth is via X-Access-Key and X-Secret-Key headers over SSE or Streamable HTTP, and the input schema for each tool is generated from your tenant's own dynamic form fields, including required lists and enum values. CORDYS AI, the built-in agent, is enterprise only and runs server side in the CRM's trust domain, reusing RBAC, so deletes still need manual confirmation."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Cordys CRM cost for a company?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The community edition is free and self-hosted under a GPLv3-based license, with two strings attached: no swapping out the logo or copyright notices, and an API capped at 1,000 calls a day. Enterprise is published at \u00a530,000, \u00a560,000, and \u00a5120,000 per year, tiered by company revenue, with unlimited API calls, custom branding, embedded DataEase, and a built-in AI workbench; flagship adds hot-standby and distributed high availability. Budget separately for a DataEase commercial edition if you want BI dashboards embedded."
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
    "reviewBody": "Cordys CRM is the agent-native open-source CRM for teams that want conversational analytics and private deployment in one stack. The enterprise edition prices in CNY, which tells you where its center of gravity is.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/cordys-crm/#app",
      "name": "Cordys CRM",
      "url": "https://martechsignal.com/tools/cordys-crm/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 35,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
