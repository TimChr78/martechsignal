# DeskcommCRM | MartechSignal review

Self-hosted open-source CRM with AI agents that sell through WhatsApp

- Page: https://martechsignal.com/tools/deskcommcrm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-14

DeskcommCRM is a Brazilian open-source project that packages a WhatsApp sales CRM with AI agents that answer customers, qualify leads, and move deals through a funnel. It is MIT licensed, self-hosted, and pitched as the open alternative to Kommo, Octadesk, and Intercom for businesses that sell by chat. It started as an ecommerce CRM and the community dragged it into clinics, real estate, infoproducts, and agencies; funnel vocabulary is configurable per pipeline, so a lead can become a "patient" or a "buyer" without forking the code.

The AI work is more built-out than most repos at this star count. Agents retrieve from a per-tenant knowledge base (RAG on Postgres pgvector), so answers come from your catalog and policies instead of model imagination. Every outbound message passes seven checks before sending: unsubscribe status, LGPD rules, anti-ban throttling, text variation, deterministic and semantic promise detection, and an automation disclosure. When the agent is about to promise a 24-hour delivery you do not offer, the check blocks it and logs what it would have said. Handoff to a human comes with a summary of the conversation rather than the raw transcript. Resolved conversations feed back into the knowledge base, and the system proposes prompt improvements to itself that a human has to approve. The whole CRM is exposed over MCP, so external agents can operate it too. You pick the AI provider at install (OpenRouter, Anthropic, OpenAI, or Google) and can swap it per subsystem later, with a spending cap per organization.

Pricing is the easy part: there is none. The full product is free under MIT, with no paid tier and no locked features, and agencies may host it for clients and charge for that. What you pay for is infrastructure: a VPS (4 GB RAM recommended; the stack boots on 2 GB but runs tight at 7 containers, and each WhatsApp session costs around 150 MB), a Supabase project for Postgres, auth, and storage, plus your own AI API keys. Installation is one script that generates secrets, applies the schema, and sets up the cron jobs the automations depend on, and updates back up the database first and roll back automatically if the new version comes up broken. The update path is tested in CI, which is more than most commercial vendors can say.

The closest comparison in this directory is WaCRM, another self-hosted Supabase-based WhatsApp CRM at a similar star count. WaCRM builds only on the official Meta Cloud API and calls itself a template; DeskcommCRM supports both the official API and QR-code connection through WAHA (faster to start, multi-number, with anti-ban throttling), and adds automation rules, RBAC, multi-tenancy with RLS isolation tests, and LGPD tooling. Against hosted players like ManyChat or Chatfuel the trade is the familiar one: you own the data and skip per-contact pricing, but you run the server. It is sales-first, unlike Chatwoot, which is support-first.

Two cautions. Documentation and community are Brazilian-Portuguese first (English and Spanish READMEs exist, but the depth is in Portuguese), and the project leans heavily on one maintainer. The QR-code WhatsApp connection is also unofficial, which is great for getting started and a ban risk the official Meta channel does not carry. If you want a polished SaaS or your team cannot operate Docker, stay with Kommo or ManyChat. If you sell through WhatsApp and want the whole operation on your own server, this is the most complete open option right now.
