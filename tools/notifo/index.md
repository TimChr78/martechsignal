# Notifo | MartechSignal review

Self-hosted multi-channel notification service for email, SMS, and web push

- Page: https://martechsignal.com/tools/notifo/
- Category: Email Marketing
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-07

Notifo is an open-source notification service that puts email, SMS, web push, mobile push, in-app sockets and a WhatsApp messaging channel behind one API, with a management UI for templates, users, subscriptions and projects. It comes from the Squidex team: the README says it was originally developed for Squidex Headless CMS, and the license is MIT. The feature set is practitioner-grade rather than campaign-grade: MJML and Liquid email templates, hierarchical topic subscriptions (a user can follow a path like clothes/shoes/nike and set preferences per topic), per-channel message queues with retries, configurable send delays that work as aggregation windows, confirmation modes from none to explicit, and read and confirmed tracking. Provider support is specific rather than pluggable: Amazon SES for email, MessageBird for SMS, Firebase for mobile push, a custom-built web-push implementation, and sockets for real-time in-page delivery; a JavaScript plugin adds a notification overlay to your web app. Storage is MongoDB only, with Redis optional as a SignalR backplane. The integration surface is documented and live: a REST API with an OpenAPI spec served by the app, a .NET SDK on NuGet (Notifo.SDK 1.7.5) and a TypeScript SDK on npm (@notifo/notifo 2.0.2). The maintenance picture needs a hard look before you build on it. Code commits continue (the most recent, a security fix, landed in August 2026, and the backend moved to .NET 10 in June), but the last tagged release and the published Docker images date to November 2022, so the squidex/notifo image you can pull is years behind main, and the wiki's notifo/notifo image name no longer exists on Docker Hub. A hosted instance runs at app.notifo.io and the marketing site mentions usage-based pricing, but no pricing page is live, so treat self-hosting as the only documented path. This assessment is based on the repository, wiki and published documentation.
