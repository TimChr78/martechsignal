# WaCRM | MartechSignal review

Self-hostable CRM for WhatsApp with shared inbox, sales pipelines, broadcasts, and automations

- Page: https://martechsignal.com/tools/wacrm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-07

WaCRM is a self-hostable CRM template built on the official Meta WhatsApp Business Cloud API, and it is explicit about what that means: the README calls it 'a template, not a product, ' licensed MIT under the instruction 'fork it, brand it, host it.' You get the code, your own Supabase project, your own domain, and your own data. The feature set covers WhatsApp-first sales: a shared inbox with per-conversation assignment, round-robin distribution, and internal notes; a contact hub with tags, custom fields, CSV import, and deduplication; unlimited Kanban pipelines with deals linked to conversations; broadcast campaigns using Meta-approved templates with delivery, read, and reply tracking; and a no-code automation builder whose triggers include inbound messages, new contacts, tag changes, keywords, and schedules. Two additions move it past the narrower project it was a year ago. An AI reply assistant takes your own OpenAI or Anthropic key, stored encrypted, drafts one-click replies in the inbox, and can run an auto-reply bot with a per-conversation cap and human handoff, grounded in an optional knowledge base that uses Postgres full-text or pgvector semantic retrieval. A public REST API with scoped, revocable keys and an MCP server let external tools and assistants read the CRM, read-only by default with writes as an opt-in. The stack is Next.js 16, React 19, TypeScript, and Tailwind v4 on Supabase. Getting there takes real setup: fork the repo, run npm install, set Supabase credentials plus an encryption key, run migrations, then paste a Meta phone number ID and access token and expose an HTTPS webhook. Because it uses the official API, broadcasts are limited to Meta-approved templates and your number must be approved by Meta first. For a small team in a WhatsApp-heavy market that is a fair trade; for anyone needing email, a dialer, or forecasting, it is the wrong tool.
