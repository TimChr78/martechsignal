# EspoCRM | MartechSignal review

Lightweight open-source CRM with sales automation, marketing tools, and customer management

- Page: https://martechsignal.com/tools/espocrm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-07

EspoCRM is a self-hosted CRM under AGPLv3 that has been in development since 2011, started in Ukraine and now owned by EspoCRM, Inc., a Delaware corporation, and it moves fast: 10.0.7 shipped on September 3, 2026, three months after the 10.0 line landed. The free core covers accounts, contacts, leads, opportunities, cases, a knowledge base, customer portals, mass email campaigns with target lists and mail merge, web-to-lead forms, kanban, and a formula engine with dynamic logic for calculated fields and conditional UI; version 10 added multiple pipelines, record locking, and categories for custom entity types. What the free edition leaves out matters when you compare it with commercial CRMs: workflow automation, the business process management designer, and reports are paid extensions sold together as the Advanced Pack, as are VoIP and Twilio telephony, Google Workspace and Outlook sync, and the AI add-on. That add-on, called Intelligence and first released in August 2026, connects to OpenAI, Gemini, Claude, or any OpenAI-compatible provider and adds summarization, intelligent paste, an AI email composer, and formula functions for classification, data extraction, and summaries, which is the only AI surface in the product. Integration work is well served: a documented REST API at api/v1 with an OpenAPI spec since version 9.3 and official API clients in PHP, JavaScript, Python, Rust, Java, Go, and Zig. Requirements are PHP 8.3 through 8.5 with MySQL 8 or later, MariaDB 10.3 or later, or PostgreSQL 15 or later, plus an optional WebSocket daemon for real-time updates. Installation is an archive with a browser wizard, a shell script with Let's Encrypt options, or Docker. Vendor-hosted cloud plans run from € 12.90 per user monthly on Basic to € 59 on Ultimate, each including the Advanced Pack. This assessment is from the repository, the docs, and the vendor site.
