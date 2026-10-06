# ProspectOS review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- ProspectOS
Re-check pending: pricing last verified 2026-08-31 (36 days ago).

## ProspectOS review (2026): pricing, AI features, verdict

Open-source lead prospecting CRM with Google Maps and Instagram scraping

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit ProspectOS →](https://github.com/nando0x/ProspectOS)

[How we review](/methodology/) · No affiliate links

**Verdict:** ProspectOS is a tool in CRM with free and open source. The catalog documents 2 AI features, 2 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-08-31. This is a desk review, not a hands-on test. Desk-reviewed

[Visit ProspectOS →](https://github.com/nando0x/ProspectOS)

## MartechSignal Score: 29/60

ProspectOS is MIT lead prospecting with Google Maps and Instagram scraping built in. It is early, and the scraping APIs carry their own costs and risks.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free under MIT self-hosted with scraping API costs called out as the run expense (the vendor pricing page: [pricing section](https://github.com/nando0x/ProspectOS), verified 2026-08-31). |
| Feature depth | 4/10 | Lead discovery and contact enrichment cover the prospecting loop (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Integrations | 3/10 | Google Maps and Instagram documented as data sources plus an API (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| AI capability | 3/10 | Lead discovery and enrichment run as data automation more than model work (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with full self-hosting (the source repository: [repository](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Operational maturity | 2/10 | Founded 2026 as an early project (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

ProspectOS is a local lead-prospecting tool for agencies and freelancers who sell websites or digital services to small businesses. It scans Google Maps by niche and city (or by pin and radius), checks each company's website to separate no-site from slow-or-insecure-site, scores the results, and generates an AI-written outreach message plus a PDF diagnosis per lead, all tracked in a visual kanban CRM. The stack is Flask, React 19, TypeScript, and SQLite, runs locally on Windows, and the repo shows 230 passing tests. The honest catch is in the project's own warnings: it is a scraping tool, Google Maps and Instagram scraping can violate those platforms' terms, and the Instagram module logs in with a personal account via instagrapi, which carries a real risk of checkpoint or ban. The README recommends a secondary account and moderate use. MIT-licensed with a few hundred stars, it is a working codebase for learning and prospecting at small scale, sold to nobody and hosted by you, with the compliance question deliberately left in your hands.

ProspectOS homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Lead discovery
- Contact enrichment
## Key Integrations

- Google Maps
- Instagram
## Pricing

ProspectOS is free to self-host under the MIT licence.

Free and open source (MIT). Self-hosted; scraping APIs may have their own costs.

Current plans and limits live on the [ProspectOS pricing section](https://github.com/nando0x/ProspectOS).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

The README is unusually candid: a dedicated 'before you use' section spells out that the tool scrapes Google Maps and Instagram, that Instagram access uses your personal account through instagrapi with a documented risk of security checkpoints or bans, and that the WhatsApp cockpit only passively reads a chat window you open yourself. That transparency makes evaluation easier, since the operational risks are the product's most important features. All claims here come from the repository documentation.

The scope is deliberately narrow and local: businesses without websites or with poor ones, approached via WhatsApp with an AI-drafted message and a PDF diagnosis. For a web-design freelancer that is a genuine end-to-end workflow. The Instagram module is optional but account-risk-bearing, and the tool runs on your machine by design, so there is no SaaS convenience layer or team features.

## Verdict

A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (228 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: lead discovery | ✗ Short native integration list - plan for API work |
| ✓ Native integrations include Google Maps, Instagram (2 listed) |  |

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is ProspectOS?**
ProspectOS: Open-source lead prospecting CRM with Google Maps and Instagram scraping. ProspectOS ships with lead discovery. The public repository carries 228 stars.

**How much does ProspectOS cost?**
ProspectOS is open source - MIT licensed and free to self-host; the public repository carries 228 stars. You pay in server time and maintenance, not licences.

**Is ProspectOS a good self-hosted CRM tool in 2026?**
A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS.

## Similar Tools

- [Chatfuel](/tools/chatfuel/): AI chatbot platform for automating customer conversations on messaging channels
- [Line Harness](/tools/line-harness/): Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control
- [Cordys CRM](/tools/cordys-crm/): Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [HubSpot CRM](/tools/hubspot-crm/): Free AI-powered CRM platform with sales, service, and marketing tools unified
## Related reading

- [The guardrails Google won't ship for your AI ad account](/blog/google-ads-ai-guardrails/)
- [Your Dashboard Can't See AI Search, Here's the 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/)
- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 228
- **Founded:** 2026
- **HQ:** Open source
- **API:** Yes
- **Repository checked:** 2026-10-06
- **Page updated:** 2026-08-31

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
