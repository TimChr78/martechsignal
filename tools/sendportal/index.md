# SendPortal review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- SendPortal
Review · Email Marketing

## SendPortal review (2026): pricing, AI features, verdict

Self-hosted open-source email marketing: newsletters, segments, and tracking on your own server

By [Tim Christensen](/authors/tim-christensen/) · updated 2026-10-15 · Open Source Desk-reviewed

Not yet scored

- **Price:** Open Source
- **Licence:** MIT
- **GitHub stars:** 2,179

[How we review](/methodology/) · No affiliate links

**Verdict:** SendPortal is a tool in Email Marketing with free and open source. The catalog documents 9 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-10-15. This is a desk review, not a hands-on test. Desk-reviewed

## Catalog facts: SendPortal

Not yet scored against the rubric, so no verdict here. This is everything the catalog holds on the tool, verified against vendor sources.

- **Founded:** 2020
- **Headquarters:** London, UK
- **Licence:** MIT
- **Public API:** yes
- **Catalogued integrations:** 9
- **GitHub stars:** 2,179
- **Last release:** v4.0.0 (2026-10-12)

The full rubric is on the [methodology page](/methodology/).

## Overview

SendPortal is a self-hosted email marketing app under the MIT license, built on Laravel by Mettle, a London agency. The pitch is simple: run your newsletters from your own server and pay an email API per message instead of paying Mailchimp per subscriber. It covers subscriber lists, tags and segments, HTML templates, campaigns, per-message tracking of sends, opens, clicks, bounces and unsubscribes, and multiple workspaces, so an agency can run several clients from one install. The honest part first, because the AI question comes up with every tool in this directory: there is no AI here. No subject line generation, no send time optimization, no predictive anything. The docs list subscribers, tags, templates, campaigns, messages and workspaces, and that is the whole feature surface. There is also no automation builder, so drip sequences and triggered flows are out of scope. SendPortal is a campaign sending engine with clean reporting, and it does not pretend to be more. Pricing is the easy part. The software is free with no seat or subscriber limits, and there is no official hosted tier (sendportal.io has no pricing page at all). What you actually pay for is a PHP 8.3+ server and an email provider. It ships drivers for Amazon SES, Mailgun, SendGrid, Postmark, Mailjet, Postal and plain SMTP. Pointing it at SES is the cheap route at $0.10 per 1,000 emails, which is how the fraction-of-the-cost claim holds up: a 50,000 subscriber newsletter costs about $5 per send on SES versus hundreds of dollars a month on Mailchimp. The maintenance history deserves a straight look. Version 4.0.0 shipped on October 12, 2026, moving the app to Laravel 13 and PHP 8.3, and it was the first release since v3.0.1 in April 2024. A two and a half year gap between releases is a long silence, though the current code is fresh and the repo (2,173 stars, 468 forks) still gets fixes. The natural comparison in this directory is Listmonk, which has ten times the stars and runs as a single Go binary. SendPortal answers with the PHP ecosystem: MIT instead of AGPL, native multi-workspace support, and a sendportal-core Composer package that drops into an existing Laravel app. If your product already runs on Laravel with its own auth, you can add a newsletter feature without standing up a separate service, which Listmonk cannot do. Who should skip it: marketers who want AI copywriting or automation flows should look at BillionMail or Notifuse in this directory instead, and teams that do not run PHP are better off with Listmonk. Who should consider it: Laravel shops, agencies that want per-client workspaces on one install, and anyone tired of contact-based pricing.

## Key Integrations

- Amazon SES
- Mailgun
- SendGrid
- Postmark
- Mailjet
- Postal
- SMTP
- REST API
- CSV import
## Pricing

SendPortal is free to self-host under the MIT licence.

Free to self-host under MIT, with unlimited subscribers, campaigns, users and workspaces. No official hosted tier; you pay for your own PHP 8.3+ server plus an email provider (SES, Mailgun, SendGrid, Postmark, Mailjet, Postal or SMTP). SES is the cheapest route at $0.10 per 1,000 emails.

Current plans and limits live on the [SendPortal pricing section](https://github.com/mettle/sendportal).

## How to install

- Stand-alone: git clone --depth 1 --branch v4.0.0 https://github.com/mettle/sendportal.git, run composer install, set the database and mail service in .env, run the sp:install Artisan command (it creates the schema and admin user), and point nginx or Apache at the public/ directory.
- Package route: composer require mettle/sendportal-core inside an existing Laravel 13 app that already handles user authentication. The core package carries subscriber, campaign and tracking logic; the full SendPortal app is a wrapper around it.
- Database: MySQL 5.7 or later, or PostgreSQL 10 or later. Version support: v4 needs PHP 8.3+ and Laravel 13; v3 covers PHP 8.2 with Laravel 10/11; v2 covers PHP 7.3+ with Laravel 8+.
## Requirements

PHP 8.3 or newer, Composer, Git, MySQL 5.7+ or PostgreSQL 10+, and a web server (Apache or nginx) serving the public/ directory. Built on Laravel 13. An email delivery account with one of the supported providers: Amazon SES, Postmark, SendGrid, Mailgun, Mailjet, Postal, or any SMTP server.

## Best for

Laravel and PHP teams and agencies that want to own their newsletter stack: MIT license, unlimited subscribers, multiple workspaces for clients, and a REST API covering subscribers, tags, templates and campaigns. Especially strong when you want to embed email marketing into an existing Laravel product through the sendportal-core package.

## Not for

Marketers expecting AI content, send time optimization or automation sequences: none of that ships. Also not for teams that do not want to manage PHP hosting, or anyone who reads the April 2024 to October 2026 release gap as abandonment risk. Listmonk (Go, single binary, much larger community) is the safer self-hosted default.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the GitHub repository, the sendportal.io landing page and the v4 docs. Not a hands-on install test.

The feature surface is exactly what the docs list: subscribers, tags, templates, campaigns, messages and workspaces, plus a REST API for templates, subscribers, tags, tag-subscribers, subscriber-tags and campaigns. No AI features, no automation builder, and no drag-and-drop editor appear anywhere in the docs.

Delivery is bring-your-own-provider: AWS SES, Postmark, SendGrid, Mailgun, Mailjet, Postal or SMTP. Tracking covers sends, opens, clicks, bounces and unsubscribes per message, and subscribers import via CSV or API.

Release history: v4.0.0 on October 12, 2026 (Laravel 13 upgrade, plus a fix for sp:install skipping migrations), then nothing since v3.0.1 on April 19, 2024. 52 open issues, 468 forks, MIT license.

## Verdict

A clean, MIT-licensed self-hosted newsletter sender for PHP shops, freshly updated to Laravel 13 after a long quiet period. No AI and no automation, so the subscription money you save is paid back in features you do not get.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ Active public repository (2,179 GitHub stars counted at last check) |  |
| ✓ Native integrations include Amazon SES, Mailgun, SendGrid (9 listed) |  |

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is SendPortal?**
SendPortal: Self-hosted open-source email marketing: newsletters, segments, and tracking on your own server. The public repository carries 2,179 stars. SendPortal offers a public API for custom integrations.

**How much does SendPortal cost?**
SendPortal is open source - MIT licensed and free to self-host; the public repository carries 2,179 stars; native integrations cover Amazon SES, Mailgun, SendGrid. You pay in server time and maintenance, not licences.

**Is SendPortal a good self-hosted Email Marketing tool in 2026?**
A clean, MIT-licensed self-hosted newsletter sender for PHP shops, freshly updated to Laravel 13 after a long quiet period. No AI and no automation, so the subscription money you save is paid back in features you do not get.

**Does SendPortal have AI features?**
No. SendPortal has zero AI capabilities: no content generation, no subject line suggestions, no send time optimization, and no predictive segmentation. It is a campaign management and delivery tool. If AI is a requirement, the self-hosted alternatives in this directory that ship it are BillionMail and Notifuse.

**Is SendPortal really free?**
The software is free under the MIT license with unlimited subscribers, campaigns, users and workspaces, and there is no official hosted version to buy. Your costs are infrastructure: a PHP 8.3+ server with MySQL or PostgreSQL, plus an email delivery provider. Amazon SES is the cheapest supported option at $0.10 per 1,000 emails; Mailgun, SendGrid, Postmark and Mailjet bill at their standard rates.

**SendPortal vs Listmonk: which self-hosted email tool should you pick?**
Listmonk is the popular default: a single Go binary with PostgreSQL, AGPL licensed, around 23,800 GitHub stars against SendPortal's 2,173. Choose SendPortal when you run PHP: it is MIT licensed, which is friendlier than AGPL for embedding in commercial products, it supports multiple client workspaces, and its sendportal-core package installs into an existing Laravel app so your product can offer newsletters natively. Listmonk wins on community size and simpler operations.

**Is SendPortal still actively developed?**
The most recent release in our catalog is v4.0.0 (2026-10-12). For the full history, check the vendor changelog linked from the official site.

## Similar tools

- [Notifuse](/tools/notifuse/): Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations
- [Listmonk](/tools/listmonk/): Open-source self-hosted newsletter and mailing list manager with a fast Go backend
- [BillionMail](/tools/billionmail/): Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free
- [MailCheap](/tools/mailcheap/): Newsletter platform billed per email sent, with full MCP control for AI agents
- [Warmbly](/tools/warmbly/): Open-source cold email platform with warmup, campaigns, unified inbox, and CRM
## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
- [Amazon's Ad Agents Come With Instructions. Google's Came With Promises.](/blog/amazon-agentic-ad-formats-brand-controls/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 2179
- **Founded:** 2020
- **HQ:** London, UK
- **API:** Yes
- **Repository checked:** 2026-10-22
- **Page updated:** 2026-10-15

## Get the next teardown

One email when a new tool review lands, nothing else.

[More Email Marketing Tools →](/categories/email-marketing/)
