# Macro review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Macro
## Macro review (2026): pricing, AI features, verdict

Open source workspace with a self-updating, agent-driven CRM and shared AI team memory

CRM · Freemium from $40/seat/mo · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Macro →](https://macro.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** Macro is a tool in CRM with free and open source. The catalog documents 8 AI features, 4 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-10-06. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Macro →](https://macro.com)

## MartechSignal Score: 36/60

Macro is the agent-driven CRM that builds itself from your team's email, plus shared AI memory. AGPL and open source, but team seats start at $40 and there is no free team plan.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | Free for personal use with limits stated; Teams $40/seat/mo for the first 5 seats then $80/seat published, no free team plan (the vendor pricing page: [pricing page](https://macro.com/pricing), verified 2026-09-28). |
| Feature depth | 6/10 | Self-updating contact and company records from email with company-level pipeline stages (vendor documentation: [vendor site](https://macro.com), verified 2026-09-28). |
| Integrations | 4/10 | Gmail, Google Workspace, GitHub and MCP documented (vendor documentation: [vendor site](https://macro.com), verified 2026-09-28). |
| AI capability | 7/10 | Agents that build and maintain CRM records from email, plus shared team memory (vendor documentation: [vendor site](https://macro.com), verified 2026-09-28). |
| Openness | 8/10 | AGPL-3.0 with full source access (the source repository: [repository](https://github.com/macro-inc/macro), verified 2026-09-28). |
| Operational maturity | 5/10 | Founded 2020 with priced team tiers (vendor documentation: [vendor site](https://macro.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Macro is an open-source workspace that folds email, chat, docs, tasks, calls, and a CRM into one app, built in Rust and SolidJS with the speed obsession to show for it. The premise is that AI agents are only as good as the context they can see, and team context is scattered across a dozen SaaS tools. The whole product sits in the repo: the README says fully open source, not open core, under AGPL-3.0, a switch from the Business Source License made on May 31, 2026, so the license is only months old. The CRM is the part marketing teams will ask about first, and the docs are precise about what it is. Contact and company records build themselves from your team's email: a contact appears when a teammate messages an external person, and companies roll up by email domain. There is no separate deal entity. Pipeline stages from Lead through Customer and Churned live on company records with Stage, Owner, Revenue, and Last Interaction properties, and the docs state plainly that while records create themselves, stages are all manual. Around the CRM sit Signal and Noise email triage, drafting in your voice that sends only on approval, team memory rebuilt nightly from the day's activity, agents that take a task and report back, calls recorded and transcribed into that memory, and an MCP server outside agents reach with a one-line connection command. Pricing is free for personal use and $40 per seat per month for the first five seats, then $80 per seat, with no free team plan; team-level agent memory and auto-shared email and CRM are paid features. The security posture is unusually strong for a project this young: SOC 2 Type II, ISO 27001, HIPAA with a BAA, GDPR, and US plus EU data regions. This assessment is from the repository, the docs, and the site.

Macro homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Agent-driven CRM that builds contact and company records from your team's email
- Pipeline stages on company records (no deal entity); stage moves are manual
- Team-level agent memory rebuilt nightly from workspace activity (paid)
- Signal/Noise email triage with auto-tagging
- Email drafting in your voice that sends only on approval
- Agents that take tasks, close them, and report back, on a schedule if you want
- Calls recorded and transcribed into team memory
- MCP server exposing unified workspace search, including PDFs parsed from attachments
## Key Integrations

- Gmail
- Google Workspace
- GitHub
- MCP
## Pricing

Macro is freemium, with a free tier to start, paid plans start at $40/seat/mo as of 2026-10.

Free for personal use (Sent with Macro signature, storage and AI limits). Teams: $40/seat/mo for the first 5 seats, then $80/seat; no free team plan. Team memory and shared email/CRM are paid. Self-hosting is free under AGPL-3.0.

Current plans and limits live on the [Macro pricing page](https://macro.com/pricing).

## How to install

- Self-hosting is Nix-first: docs/RUNNING_LOCALLY.md names Nix as the only hard host dependency. Steps are git clone https://github.com/macro-inc/macro.git, cd macro, nix develop, then just doctor-local and just run_local --no-doppler.
- The local stack brings up Postgres, Redis, LocalStack, OpenSearch, Kafka, and FusionAuth in Docker with dummy AWS credentials, and builds the Rust services on the host with cargo zigbuild. Compose is driven through just recipes; no raw docker compose commands are documented.
- Login codes land in Mailpit at localhost:8025 rather than a real inbox, so first-run sign-in works offline.
- Release artifacts ship monthly under dated tags: v2026.9.7.0 includes a macOS .dmg, a Linux AppImage, and tarballs for the macrod agent daemon.
- The README points commercial or managed-hosting arrangements to self-host at macro.com, and licensing at macro.com handles alternative licensing.
## Requirements

A Nix-managed environment plus Docker for the backing services (Postgres, Redis, LocalStack, OpenSearch, Kafka, FusionAuth) and a Rust toolchain for the services, which build with cargo zigbuild. The monorepo holds 167 Rust crates, 42 deployable services, and a SolidJS app for web and desktop. Two components are sublicensed rather than in-repo, so a self-hosted instance either maintains licenses for LiveKit (video calls), FusionAuth (authentication), and PostHog (analytics) or disables those features.

## Best for

Teams that want to collapse email, chat, docs, tasks, and calls into one tool and let the CRM assemble itself from their outbound email: relationship-driven sales, founder-led selling, and agency or studio work where the conversation history is the deal context. Agent-heavy teams get the most, since MCP support and scheduled agent runs are first-class.

## Not for

Teams that manage pipeline as a discipline: there is no deal entity, stages sit on company records, and stage progression is entirely manual, so there is no weighted forecast or pipeline reporting. Also skip it for campaign automation and lifecycle email, which it does not attempt, and for self-hosting if you need a vendor-supported deployment.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, docs.macro.com, and macro.com. Not a hands-on review. The repo is unusually legible for its size: apps/web for the SolidJS client, crates/ for the Rust libraries, services/ for the deployable units, infra/ in Pulumi, and docker/ plus nix/ for local environments. Nothing in local development asks for a license key, which matches the fully-open-source claim.

The CRM is deliberately thin, and the docs say so. Records create themselves from email, but the docs note that stages are all manual: there is no deal entity, no weighted forecast, and no automation that moves a company from Demo to Negotiation. Email sync is per company, so marking a company as synced is what makes its threads team-visible. For a team whose pipeline discipline lives in spreadsheets today this is a step up; for a sales org with stage-gated forecasting it is not a CRM yet.

The license history matters for anyone evaluating on open-source grounds. Macro shipped source-available under the Business Source License and moved to AGPL-3.0 on May 31, 2026, per the FAQ, which calls the change fully open source rather than open core. The AGPL network-copyleft obligation is real for anyone modifying it and serving users, and the self-hosting story is honest about friction: three key components are sublicensed third-party services you must license or disable.

The agent surface is broader than the CRM label suggests. There is a model picker across OpenAI, Google, and Anthropic, a BYO agent harness through the macrod daemon, scheduled agent runs such as daily inbox summaries, and an MCP server the docs connect with claude mcp add --transport http macro https://mcp-server.macro.com/mcp. Security documentation claims SOC 2 Type II, ISO 27001, HIPAA with a BAA, GDPR compliance, US and EU data regions, no training on customer data, and zero-retention arrangements with model providers; agents inherit user permissions.

## Verdict

A genuinely open-source workspace whose CRM is a byproduct of team email: real for contact capture and context, not yet a pipeline tool. The license is new, the pace is fast, and the compliance posture is far ahead of the project's age.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ Paid plans start at $40/seat/mo once past the free tier |
| ✓ AI capabilities: agent-driven CRM that builds contact and company records from your team's email |  |
| ✓ Active public repository (4,577 GitHub stars counted at last check) |  |

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Macro?**
Macro: Open source workspace with a self-updating, agent-driven CRM and shared AI team memory. Macro ships with agent-driven CRM that builds contact and company records from your team's email. The public repository carries 4,577 stars.

**How much does Macro cost?**
Macro has a free tier; paid plans start at $40/seat/mo. Free for personal use (Sent with Macro signature, storage and AI limits). Teams: $40/seat/mo for the first 5 seats, then $80/seat; no free team plan. Team memory and shared email/CRM are paid. Self-hosting is free under AGPL-3.0. We last checked both ends of that split on 2026-10-06. The pricing section above shows what the free tier actually covers.

**Is Macro worth it past the free tier?**
A genuinely open-source workspace whose CRM is a byproduct of team email: real for contact capture and context, not yet a pipeline tool. The license is new, the pace is fast, and the compliance posture is far ahead of the project's age.

**Macro vs Attio: which should a sales team pick?**
Attio is a dedicated CRM: deal objects, pipeline views, enrichment, and integrations built around managing a sales process. Macro is a workspace where the CRM emerges from email, with company records, stages, and revenue properties but no deal entity and manual stage moves. Pick Attio if pipeline management and forecasting are the job, or if you need a CRM to drop into an existing stack. Pick Macro if your team would rather replace its email, chat, docs, and task tools with one app and accept lighter pipeline mechanics in exchange for records that maintain themselves.

**Can you self-host Macro?**
Yes, under AGPL-3.0, and the FAQ is candid that it has not been the primary focus. Self-hosting runs through Nix with a Compose stack for Postgres, Redis, OpenSearch, Kafka, and FusionAuth, and it carries a real caveat: LiveKit for calls, FusionAuth for authentication, and PostHog for analytics are sublicensed third-party services, so an independent deployment must maintain those licenses or cut the features. Managed hosting and commercial arrangements go through self-host at macro.com.

## Similar Tools

- [Freshsales](/tools/freshsales/): AI-powered CRM with built-in phone, email, and chat for sales teams
- [Pipedrive](/tools/pipedrive/): Sales-focused CRM with AI-powered pipeline management and deal forecasting
- [Paperclip](/tools/paperclip/): Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit
- [Eve Marketing Team Template](/tools/eve-marketing-team/): Open-source team of marketing agents on eve: lead, content, social, SEO, email
- [Cordys CRM](/tools/cordys-crm/): Open-source AI CRM with built-in agents, conversational analytics, and private deployment
## Related reading

- [The AI-search funnel map GA4 won't give you](/blog/ai-search-funnel-map-ga4-wont-give-you/)
- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
### Quick Facts

- **Pricing:** Freemium from $40/seat/mo
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 4577
- **Founded:** 2020
- **HQ:** New York, NY, USA
- **API:** Yes
- **Repository checked:** 2026-10-07
- **Page updated:** 2026-10-06

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
