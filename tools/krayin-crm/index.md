# Krayin CRM review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Krayin CRM
Re-check pending: pricing last verified 2026-09-07 (29 days ago).

## Krayin CRM review (2026): pricing, AI features, verdict

Free open-source Laravel CRM for SMEs and enterprises with full customer lifecycle management

CRM · Open Source from $1,799 one-time Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Krayin CRM →](https://krayincrm.com)

[How we review](/methodology/) · No affiliate links

**Verdict:** Krayin CRM is a tool in CRM with free and open source. The catalog documents 2 AI features, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Krayin CRM →](https://krayincrm.com)

## MartechSignal Score: 35/60

Krayin is the Laravel CRM for teams that want to own the code and extend it in PHP. MIT licensing is unusually permissive here; the paid multi-tenant SaaS module is the one visible upsell.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | Free to self-host under MIT with no user limits is perfectly clear; Webkul's extension prices are mostly unlisted beyond the $1,799 multi-tenant module (the vendor pricing page: [pricing section](https://krayincrm.com/extensions/), verified 2026-09-07). |
| Feature depth | 6/10 | Full customer lifecycle management with automation packages (triggers, conditions, actions) covers SME CRM needs; campaign machinery is thin (vendor documentation: [vendor site](https://krayincrm.com), verified 2026-09-28). |
| Integrations | 3/10 | No named integrations in the catalog; Laravel and Webkul extensions carry the connection story (vendor documentation: [vendor site](https://krayincrm.com), verified 2026-09-28). |
| AI capability | 5/10 | Magic AI lead creation from uploaded PDFs and images via an OpenRouter module is real but narrow (vendor documentation: [vendor site](https://krayincrm.com), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with no user limits on self-hosting (the source repository: [repository](https://github.com/krayin/laravel-crm), verified 2026-09-28). |
| Operational maturity | 6/10 | Backed by Webkul's extension business, giving it more runway than a solo project (vendor documentation: [vendor site](https://krayincrm.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Krayin CRM is an MIT-licensed, Laravel-native open-source CRM from Webkul, with 23,800-plus GitHub stars and a steady release rhythm: v2.2.5 shipped August 4, 2026, and the 2.2 branch took commits in September 2026. The current line requires PHP 8.3 or later and Laravel 12, with MySQL 8.0.32 or later, MariaDB 10.3 or later, and at least 3GB of RAM, so check the stack before installing. The feature set is broader than older reviews suggest: leads with multiple pipelines, quotes, activities, contacts and organizations, tags, products and warehouses, unlimited custom fields, role-based access control, embeddable web-to-lead forms, email templates, a marketing package, and an import-export layer, with dashboard support for multiple pipelines added in 2.2.4. Two corrections to the common criticisms. Krayin does ship a workflow engine: the Automation package provides event triggers, conditions, and actions plus webhooks, though documentation for it is thin. And it does have a genuine AI feature, Magic AI, which creates leads from uploaded PDFs and images using an OpenRouter API key and ships as an official module rather than in core. What is still absent is lead scoring and predictive analytics; the marketing copy mentions sales forecasting without documenting a forecasting engine. Email handling is inbound-focused: a SendGrid Inbound Parse webhook turns mail to your domain into HTTP posts, or an IMAP driver polls an existing mailbox, with outbound mail on Laravel configuration. The REST API is a separate composer package with Sanctum bearer tokens and Swagger documentation, not something the base install ships with. Installation is composer create-project plus an artisan installer that prompts for app and database settings and seeds an admin account. Paid extras include a multi-tenant SaaS extension at $1,799 and vendor cloud hosting with no published prices. This assessment is from the repository, the docs, and the site.

Krayin CRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Magic AI lead creation from uploaded PDFs and images (OpenRouter key, official module)
- Automation package: event triggers, conditions, actions, and webhooks
## Pricing

Krayin CRM is free to self-host under the MIT licence, paid plans start at $1,799 one-time as of 2026-09.

Free to self-host under MIT with no user limits. Paid: Webkul extensions (multi-tenant SaaS at $1,799 for Krayin 2.1.0; other extension prices unlisted) and vendor cloud hosting with no published prices.

Current plans and limits live on the [Krayin CRM pricing section](https://krayincrm.com/extensions/).

## How to install

- Create the project and run the installer: composer create-project krayin/laravel-crm, then php artisan krayin-crm:install. If no .env exists, the installer prompts for app name, URL, locale, currency, database connection, and admin credentials; otherwise edit APP_URL plus the mail and database parameters in .env yourself.
- The web root must point at laravel-crm/public/. The default admin signs in at /admin/login with the default admin email from the docs and admin123, so change both before anything touches the internet.
- For production the README recommends removing development dependencies with composer install --no-dev.
- The REST API is a separate package: composer require krayin/rest-api, then php artisan krayin-rest-api:install and php artisan l5-swagger:generate. Swagger UI lands at /api/admin/documentation, with Sanctum bearer-token endpoints such as POST /api/admin/login and GET /api/admin/leads.
- Magic AI is configured after install under Dashboard, Settings, Configuration, Magic AI, where you supply an OpenRouter API key; the docs show a free Llama model as the example.
## Requirements

PHP 8.3 or higher with the intl and gd extensions, Laravel 12 (the 2.2 branch composer.json pins ^8.3 and ^12.0), MySQL 8.0.32 or later or MariaDB 10.3 or later, Composer 2.5 or higher, and 3GB RAM or more per the docs requirements page. Note the master-branch README still says PHP 8.2 or higher; the 2.2 branch is the accurate source. Mail needs either a SendGrid account for inbound parse or an IMAP mailbox for the pull driver.

## Best for

Laravel shops that want a self-hosted CRM they can extend in PHP without license friction: MIT code, familiar artisan tooling, web-to-lead forms, multiple pipelines, custom fields, and a REST API you can add as a composer package. Also a fit for teams that need a second language locale trail (Korean and Japanese landed in the last two releases) and prefer paying for extensions rather than seats.

## Not for

Teams buying on AI: there is no lead scoring or predictive analytics, and Magic AI is document-to-lead extraction rather than pipeline intelligence. Also skip it if you need deep two-way Gmail or Outlook sync, a large native integration marketplace, or automation that is documented well enough to learn from the manual rather than the code.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, devdocs.krayincrm.com, and krayincrm.com. Not a hands-on review. Two corrections to our own earlier read: the Automation package is a real trigger, conditions, and actions engine with webhooks, and Magic AI is a documented AI feature that turns uploaded PDFs and images into leads through OpenRouter. Neither makes Krayin an AI CRM, but the flat no-automation claim that circulates in reviews is out of date.

Security history deserves attention before you expose an install. Version 2.2.5 fixed unauthenticated installer access and executable email attachment uploads; 2.2.4 fixed unrestricted file upload, stored XSS in notes, IDOR on agent access, and SQL injection in the lead filter, plus webhook validation rejecting internal endpoint URLs in 2.2.5. The pattern says the project patches, and also that running the latest release matters.

Documentation lag is the operational tax. The master README still says PHP 8.2 while the 2.2 branch requires 8.3, and the Automation package has no user-facing manual page, so expect to read source for workflow specifics. Release notes are informative where the docs are not: import and export for custom lead and person attributes, Google Contacts export, group-based view permissions, and quick attributes on lead forms all landed in the last two releases.

The commercial layer is a Webkul storefront rather than a core fork: extensions for VoIP, WhatsApp, purchase orders, and Google integration list on krayincrm.com without prices, the multi-tenant SaaS extension is published at $1,799 for Krayin 2.1.0, and cloud hosting advertises paying for servers rather than seats with no published rates. Budget discovery is a sales conversation.

## Verdict

A current, actively maintained Laravel CRM that is more capable than its reputation on automation and AI, thinner than its marketing on documentation, scoring, and integrations, and best treated as an extendable base.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Paid plans start at $1,799 one-time |
| ✓ API access for custom integrations |  |
| ✓ AI capabilities: magic AI lead creation from uploaded PDFs and images (OpenRouter key, official module) |  |
| ✓ Active public repository (23,971 GitHub stars counted at last check) |  |

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Krayin CRM?**
Krayin CRM: Free open-source Laravel CRM for SMEs and enterprises with full customer lifecycle management. Krayin CRM ships with magic AI lead creation from uploaded PDFs and images (OpenRouter key, official module). The public repository carries 23,971 stars.

**How much does Krayin CRM cost?**
Krayin CRM has a free tier; paid plans start at $1,799 one-time. Free to self-host under MIT with no user limits. Paid: Webkul extensions (multi-tenant SaaS at $1,799 for Krayin 2.1.0; other extension prices unlisted) and vendor cloud hosting with no published prices. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Krayin CRM a good self-hosted CRM tool in 2026?**
A current, actively maintained Laravel CRM that is more capable than its reputation on automation and AI, thinner than its marketing on documentation, scoring, and integrations, and best treated as an extendable base.

**Does Krayin CRM have AI features or lead scoring?**
It has one documented AI feature and no lead scoring. Magic AI creates leads from uploaded PDFs and images using an OpenRouter API key, configured under Settings, Configuration, Magic AI, and ships as an official module rather than in the core packages. There is no lead scoring, no predictive analytics, and no documented forecasting engine; the homepage phrase sales forecasting has no matching feature documentation. Treat Krayin as a traditional CRM with one document-parsing AI add-on.

**Can you import leads and contacts from a CSV or another CRM into Krayin?**
Yes, through the built-in import and export layer (the DataTransfer package), which covers leads, persons, and organizations, with support for custom attributes on leads and persons added in v2.2.5 along with Google Contacts export. There is no documented one-click migration from Salesforce or HubSpot, so plan a CSV path: export from the source system, map columns to Krayin attributes, and import. Custom fields you create in the target should exist before import so the attribute columns can map.

## Similar Tools

- [EspoCRM](/tools/espocrm/): Lightweight open-source CRM with sales automation, marketing tools, and customer management
- [Pipedrive](/tools/pipedrive/): Sales-focused CRM with AI-powered pipeline management and deal forecasting
- [Salesforce CRM](/tools/salesforce-crm/): Enterprise CRM platform with Einstein AI for sales, service, and marketing teams
- [BillionMail](/tools/billionmail/): Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free
## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
## Also featured in

- [Best open-source CRM tools (2026)](/best/open-source-crm/) — Best for Laravel shops that want room to extend a CRM.
### Quick Facts

- **Pricing:** Open Source from $1,799 one-time
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 23971
- **API:** Yes
- **Repository checked:** 2026-10-06
- **Page updated:** 2026-09-07

Related guides: [Open Source Crm](/best/open-source-crm/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
