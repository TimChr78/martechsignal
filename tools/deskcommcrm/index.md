# DeskcommCRM review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- DeskcommCRM
Re-check pending: pricing last verified 2026-09-14 (22 days ago).

## DeskcommCRM review (2026): pricing, AI features, verdict

Self-hosted open-source CRM with AI agents that sell through WhatsApp

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit DeskcommCRM →](https://deskcomm.com.br)

[How we review](/methodology/) · No affiliate links

**Verdict:** DeskcommCRM is a tool in CRM with free and open source. The catalog documents 7 AI features, 10 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-14. This is a desk review, not a hands-on test. Desk-reviewed

[Visit DeskcommCRM →](https://deskcomm.com.br)

## MartechSignal Score: 41/60

DeskcommCRM is WhatsApp selling as self-hosted MIT software: RAG knowledge per tenant and seven pre-send guardrails. You run the VPS and the AI keys; the agents do the qualifying.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free under MIT with no paid tiers; run costs are a 4GB VPS, Supabase and your AI keys, stated plainly (the vendor pricing page: [pricing page](https://deskcomm.com.br/#preco), verified 2026-09-14). |
| Feature depth | 6/10 | Lead qualification agents, pipeline movement and per-tenant RAG cover WhatsApp-based selling (vendor documentation: [vendor site](https://deskcomm.com.br), verified 2026-09-28). |
| Integrations | 7/10 | WhatsApp via WAHA and the official Cloud API, Supabase, Nuvemshop, Zapier, n8n, OpenRouter and MCP (vendor documentation: [vendor site](https://deskcomm.com.br), verified 2026-09-28). |
| AI capability | 7/10 | RAG-backed agents with seven-check pre-send guardrails show real production thinking (vendor documentation: [vendor site](https://deskcomm.com.br), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with full self-hosting (the source repository: [repository](https://github.com/melgarafael/DeskcommCRM), verified 2026-09-28). |
| Operational maturity | 4/10 | Agent-side support noted for paid plans (vendor documentation: [vendor site](https://deskcomm.com.br), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

DeskcommCRM is a Brazilian open-source project that packages a WhatsApp sales CRM with AI agents that answer customers, qualify leads, and move deals through a funnel. It is MIT licensed, self-hosted, and pitched as the open alternative to Kommo, Octadesk, and Intercom for businesses that sell by chat. It started as an ecommerce CRM and the community dragged it into clinics, real estate, infoproducts, and agencies; funnel vocabulary is configurable per pipeline, so a lead can become a "patient" or a "buyer" without forking the code. The AI work is more built-out than most repos at this star count. Agents retrieve from a per-tenant knowledge base (RAG on Postgres pgvector), so answers come from your catalog and policies instead of model imagination. Every outbound message passes seven checks before sending: unsubscribe status, LGPD rules, anti-ban throttling, text variation, deterministic and semantic promise detection, and an automation disclosure. When the agent is about to promise a 24-hour delivery you do not offer, the check blocks it and logs what it would have said. Handoff to a human comes with a summary of the conversation rather than the raw transcript. Resolved conversations feed back into the knowledge base, and the system proposes prompt improvements to itself that a human has to approve. The whole CRM is exposed over MCP, so external agents can operate it too. You pick the AI provider at install (OpenRouter, Anthropic, OpenAI, or Google) and can swap it per subsystem later, with a spending cap per organization. Pricing is the easy part: there is none. The full product is free under MIT, with no paid tier and no locked features, and agencies may host it for clients and charge for that. What you pay for is infrastructure: a VPS (4 GB RAM recommended; the stack boots on 2 GB but runs tight at 7 containers, and each WhatsApp session costs around 150 MB), a Supabase project for Postgres, auth, and storage, plus your own AI API keys. Installation is one script that generates secrets, applies the schema, and sets up the cron jobs the automations depend on, and updates back up the database first and roll back automatically if the new version comes up broken. The update path is tested in CI, which is more than most commercial vendors can say. The closest comparison in this directory is WaCRM, another self-hosted Supabase-based WhatsApp CRM at a similar star count. WaCRM builds only on the official Meta Cloud API and calls itself a template; DeskcommCRM supports both the official API and QR-code connection through WAHA (faster to start, multi-number, with anti-ban throttling), and adds automation rules, RBAC, multi-tenancy with RLS isolation tests, and LGPD tooling. Against hosted players like ManyChat or Chatfuel the trade is the familiar one: you own the data and skip per-contact pricing, but you run the server. It is sales-first, unlike Chatwoot, which is support-first. Two cautions. Documentation and community are Brazilian-Portuguese first (English and Spanish READMEs exist, but the depth is in Portuguese), and the project leans heavily on one maintainer. The QR-code WhatsApp connection is also unofficial, which is great for getting started and a ban risk the official Meta channel does not carry. If you want a polished SaaS or your team cannot operate Docker, stay with Kommo or ManyChat. If you sell through WhatsApp and want the whole operation on your own server, this is the most complete open option right now.

## AI Capabilities

- Per-tenant RAG knowledge base for WhatsApp agents
- AI agents that qualify leads and move the sales funnel
- Seven-check pre-send guardrails (LGPD, anti-ban, promise detection)
- Audited AI-to-human handoff with conversation summary
- Self-improving agents: resolved conversations feed the knowledge base
- Per-organization AI spend caps and per-subsystem provider choice
- MCP server exposing the CRM to external agents
## Key Integrations

- WhatsApp (WAHA QR-code)
- WhatsApp Cloud API (Meta official)
- Supabase
- Nuvemshop
- Zapier
- n8n
- OpenRouter
- Anthropic
- OpenAI
- MCP
## Pricing

DeskcommCRM is free to self-host under the MIT licence.

Free and MIT licensed, no paid tier or locked features. You pay for a VPS (4 GB RAM recommended), a Supabase project, and your own AI API keys. Agencies may host it for clients and charge.

Current plans and limits live on the [DeskcommCRM pricing page](https://deskcomm.com.br/#preco).

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ AI capabilities: per-tenant RAG knowledge base for WhatsApp agents |  |
| ✓ Active public repository (4,410 GitHub stars counted at last check) |  |
| ✓ Native integrations include WhatsApp (WAHA QR-code), WhatsApp Cloud API (Meta official), Supabase (10 listed) |  |

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is DeskcommCRM?**
DeskcommCRM: Self-hosted open-source CRM with AI agents that sell through WhatsApp. DeskcommCRM ships with per-tenant RAG knowledge base for WhatsApp agents. The public repository carries 4,410 stars.

**How much does DeskcommCRM cost?**
DeskcommCRM is open source - MIT licensed and free to self-host; the public repository carries 4,410 stars; native integrations cover WhatsApp (WAHA QR-code), WhatsApp Cloud API (Meta official), Supabase. You pay in server time and maintenance, not licences.

**Is DeskcommCRM a good self-hosted CRM tool in 2026?**
Strengths include 4,410 GitHub stars, MIT licensing with free self-hosting, an API for custom integrations. DeskcommCRM documents 10 integrations

## Similar Tools

- [WaCRM](/tools/wacrm/): Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations
- [Cordys CRM](/tools/cordys-crm/): Open-source AI CRM with built-in agents, conversational analytics, and private deployment
- [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/): MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4
- [Khoj](/tools/khoj/): Self-hosted AI research and writing assistant that chats with your documents and automates content workflows
## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Before your next automation, run the blast radius audit](/blog/automation-blast-radius-audit/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 4410
- **HQ:** Brazil
- **API:** Yes
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-09-14

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
