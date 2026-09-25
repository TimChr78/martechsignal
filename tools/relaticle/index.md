# Relaticle | MartechSignal review

Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel & Filament

- Page: https://martechsignal.com/tools/relaticle/
- Category: CRM
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-07

Relaticle is an open-source CRM you run on your own server under the AGPL-3.0 license, built on Laravel 13, Filament 5, Livewire 4, and PHP 8.5. The repository was created in September 2024, the first stable release shipped in April 2025, and development moves fast: 86 releases so far, 74 of them in the twelve months to September 2026, with v3.5.7 landing on September 6, 2026 alongside 1,610 GitHub stars and a claimed 2,000+ automated tests. The feature set covers companies, people, opportunities with custom pipeline stages and win/loss analysis, tasks, notes, and an activity log, on a customizable data model with 22 field types, conditional visibility, per-field encryption, and no schema migrations. AI is the pitch rather than an afterthought: a 37-tool MCP server at mcp.relaticle.com authenticates with OAuth 2.1 and PKCE or a personal access token, exposing search, fetch, and full create-read-update-delete across companies, people, opportunities, tasks, and notes to Claude, ChatGPT, Cursor, and other MCP clients, with destructive actions gated behind approval cards and requests capped at 120 per minute. There is also Rela, a built-in chat interface that answers questions about your records with model choices and one-click undo on approved destructive actions. Developers get a REST API v1 with twelve paths and a published OpenAPI 3.1 spec at api.relaticle.com, plus CSV import up to 10,000 rows and 10MB per file with column mapping and record-ID matching for updates. The business model outgrew the original no-premium-tiers promise: self-hosting is still free with unlimited users, but the site now sells Cloud Pro at $19 per workspace per month with 2,000 AI credits and an Enterprise tier from $20,000 a year. Per-seat pricing never arrived. Requirements are PostgreSQL 17 and Redis 7, with no MySQL path documented.
