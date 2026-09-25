# Chatwoot | MartechSignal review

Open-source customer engagement suite with Captain AI and full self-hosting

- Page: https://martechsignal.com/tools/chatwoot/
- Category: Chatbots & Conversational AI
- Pricing: Open Source
- Open source: yes (None)
- Last verified: 2026-09-07

Chatwoot is an open-source customer engagement platform that folds website live chat, email, WhatsApp, Telegram, Facebook, Instagram, SMS, LINE, TikTok, and an API channel into one team inbox, self-hostable or rented as cloud. The stack is Ruby on Rails with Vue, Sidekiq, Redis, and Postgres 16 with pgvector, and the repo sits near 36,600 GitHub stars with v4.17.1 released in August 2026. Self-hosting is genuinely first-class: the Docker guide pulls chatwoot/chatwoot:latest, fetches the production compose file and .env example from the repo, runs db:chatwoot_prepare, then docker compose up -d, and a Linux installer script (cwctl) targets Ubuntu 24.04 with Heroku and DigitalOcean one-click paths documented. Documented sizing is 4GB RAM and 4 cores for up to 10,000 conversations a day, doubling for 20,000. AI arrives as Captain, positioned as the AI agent for customer support: an Assistant that answers first-response questions from your help centre, a Copilot that drafts and translates replies for agents, Memories that keep per-customer notes, reply suggestions, summarization, and content gap detection that surfaces questions your help centre does not answer. Captain is credit-metered, 1 credit per message, with 300,500, and 800 monthly credits on the paid cloud tiers and extra credits at $20 per 1,000; on self-hosted installs it requires Enterprise Edition with a paid plan plus your own OpenAI API key. Cloud pricing per agent per month billed annually is $0 (Hacker, 2 agents, 500 conversations), $19 (Startups), $39 (Business), and $99 (Enterprise with SSO and audit logs). Documented integrations are thinner than our earlier record claimed: Slack, Linear, Dialogflow, Google Translate, Cloudflare RealtimeKit, and LeadSquared are live, with Shopify and HubSpot listed for Q4 2026, so plan on the REST API and webhooks for the rest.
