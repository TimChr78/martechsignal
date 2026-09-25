# AlphOne | MartechSignal review

Plugin-first CRM (source-available, Elastic 2.0) written in Go

- Page: https://martechsignal.com/tools/alphone/
- Category: CRM
- Pricing: Open Source
- Open source: yes (Elastic License 2.0)
- Last verified: 2026-09-06

AlphOne is a plugin-first CRM with a Go backend exposing both GraphQL and REST APIs, a React single-page frontend, and a design that treats automation as an external concern: there is no built-in rules engine, because everything the UI does is available over HTTP with a token. Features ship as plugins with their own repositories; the current in-repo set covers fields, an importer, and a WhatsApp Cloud API channel that lands customer conversations in a shared inbox attached to the right contact. For marketing ops the notable part is how deliberately the project meets agents where they already work: it speaks MCP (Model Context Protocol) natively, so any MCP client can ask about today's tasks or waiting contacts, and there is a community n8n node (n8n-nodes-alphone) with documented end-to-end workflows, such as an inbound WhatsApp message creating a write-back task on the right contact. The same API-first logic works with Activepieces, Windmill, Node-RED, or a cron job with curl. Licensing needs a look before you commit: the Go backend and SQL migrations carry the Elastic License 2.0, which forbids offering AlphOne to third parties as a hosted service, while the frontend, tests, and docs are AGPLv3. That split is workable for a company extending a self-hosted CRM in Go, and rules out SaaS vendors reselling hosted CRM. At 176 stars the community is early-stage, but the repo ships with code coverage, sqlc, GraphQL codegen, and an active commit log. Evaluate it as an API-first foundation for an n8n- or agent-driven stack, not a finished SuiteCRM replacement.
