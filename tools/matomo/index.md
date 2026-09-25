# Matomo | MartechSignal review

Open-source web analytics platform with full data ownership and AI-powered insights

- Page: https://martechsignal.com/tools/matomo/
- Category: Analytics & Attribution
- Pricing: Open Source
- Open source: yes (GPL-3.0)
- Last verified: 2026-09-06

Matomo is an open-source web analytics platform you run on your own infrastructure, licensed GPL v3 or later, with 5.13.0 released in August 2026 and an active 6.x branch. Installation is a documented nine-step wizard: download matomo.zip from builds.matomo.org, upload it to a directory or subdomain, set permissions on tmp and config, then walk through a system check, database setup, superuser creation, first-site setup, and the JavaScript tracking tag. The README asks for PHP 8.1 or newer with MySQL 8 or MariaDB 10.6, which is stricter than the requirements page on matomo.org, still telling PHP 7.2.5 users that Matomo 5 works well with PHP 8. Sites above a few hundred visits a day need an archiving cron job.

The feature split matters more than the feature list. Core analytics, ecommerce tracking, goals, segments, a customizable dashboard, and an API are free. Funnels, cohorts, custom reports, form analytics, media analytics, A/B testing, heatmaps and session recordings, multi-channel attribution, roll-up reporting, and users flow are paid premium plugins, sold individually or in bundles. Matomo Tag Manager and the Google Analytics Importer are free. On-Premise bundles run 275 euros a month for Team, 1,450 for Business, and 3,400 for Enterprise, while Cloud starts at 22 euros a month for 50,000 hits and scales into four figures at hundreds of millions of hits.

Privacy is the reason teams pick it. Matomo claims 100 percent data ownership, unsampled reporting on every plan, adherence to GDPR, HIPAA, CCPA, LGPD, and PECR, and a CNIL listing it says allows consent-free use. Cloud data stays in Europe, and the vendor commits to keeping self-hosting free permanently.

Matomo's AI work measures AI traffic rather than adding AI analytics. Version 5.12.0 added AI chatbot content-request and real-time reports, an AIAgents plugin ships enabled on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT, Claude, and other MCP clients, with write actions gated behind approval.
