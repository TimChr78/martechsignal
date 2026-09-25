# SuiteCRM | MartechSignal review

Enterprise-grade open-source CRM with sales, marketing, and support automation

- Page: https://martechsignal.com/tools/suitecrm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-07

SuiteCRM is the AGPLv3 open-source CRM that forked SugarCRM Community Edition and outlived it, maintained by SuiteCRM Ltd from Stirling, Scotland. Two release lines are current: 8.10.2 and 7.15.2 shipped on the same day in July 2026 as a joint security release, and 7.15 is an extended support release with security fixes published into 2028. The module set is the deepest in this directory's CRM category: leads, accounts, contacts, opportunities, quotes, invoices, contracts, PDF templates, campaigns with target lists and confirmed opt-in, surveys, events, cases with a knowledge base, bugs, reports with scheduled runs, calendar, projects, and document management, plus Studio for no-code layout changes and Module Builder for new entities from six templates. Workflow automation is free in the core, with calculated fields, which is the main structural difference from EspoCRM, where workflows are a paid extension. What SuiteCRM does not have matters too: there is no native AI anywhere in the documented feature set, and no official mobile app. Elasticsearch is an optional search backend, and Redis or RabbitMQ are optional message transports for background jobs beyond a single server. Two APIs are documented, the newer V8 API with OAuth and the legacy V4. Requirements are PHP 8.2 to 8.4 with MariaDB 10.6 or later, or MySQL 8.0 or later, on Apache 2.4. Installation is a pre-built zip with a permissions pass, then a browser wizard or a CLI installer with flags for the admin user, database, and demo data. Migrating from 7.x to 8.x is a documented fresh install with three console commands, not a patch. Commercial support is GBP-priced: hosting from 50 pounds monthly with unlimited users, and SuiteASSURED from 3,350 pounds a year carrying warranties and indemnities. We have not run SuiteCRM; this assessment is from the repository, the docs, and the vendor site.
