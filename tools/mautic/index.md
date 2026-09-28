# Mautic review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | Free under GPL-3.0 self-hosted; managed hosting by Dropsolid from EUR 247.50/mo with a 14-day no-card trial published (the vendor pricing page: [pricing page](https://www.mautic.org/pricing), verified 2026-09-28). |
| Feature depth | 6/10 | Email, campaigns and lead management cover the marketing automation core (vendor documentation: [vendor site](https://www.mautic.org), verified 2026-09-28). |
| Integrations | 7/10 | Ten named integrations from Salesforce and HubSpot to Twilio, GTM, S3 and Zapier plus an API (vendor documentation: [vendor site](https://www.mautic.org), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://www.mautic.org), verified 2026-09-28). |
| Openness | 9/10 | GPL-3.0 with 10.5k GitHub stars and full self-hosting (the source repository: [repository](mautic/mautic), verified 2026-09-28). |
| Operational maturity | 7/10 | Founded 2014 with an official hosting partner and a long deployment history (vendor documentation: [vendor site](https://www.mautic.org), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; GPL-3.0 licence with free self-hosting | &#10007; Paid plans start at $247.5/mo once past the free tier |
| &#10003; Active public repository (10,472 GitHub stars counted at last check) |  |
| &#10003; Native integrations include Salesforce, HubSpot, Pipedrive (10 listed) |  |

**What is Mautic?**
Mautic: Open-source marketing automation platform with email, campaigns, and lead management. The public repository carries 10,472 stars. Mautic offers a public API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Mautic cost?**
Mautic has a free tier; paid plans start at €247.5/mo. Free and open source (GPL-3.0), self-hosted. Managed hosting by official partner Dropsolid from € 247.50/mo with a 14-day no-card trial; paid Extended Long Term Support (ELTS) sold by the project for old versions. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Mautic a good self-hosted Marketing Automation tool in 2026?**
The most complete open-source answer to HubSpot if you have the ops capacity to run it: real campaigns, segments, and scoring under GPL-3.0, no AI, and no shortcuts on maintenance.

**Can I update Mautic from the browser?**
No. The update-in-UI feature was deprecated in 4.2 and, per the 7.1 upgrade docs, completely removed from Mautic 5.0, partly because it required significant resources and could fail mid-update. Updates now run at the command line: php bin/console mautic:update:find to check, mautic:update:apply to install, and mautic:update:apply --finish to complete, or cache:clear plus doctrine:migration:migrate on Composer installs. The docs also warn never to update without a working, up-to-date backup.

**What are the system requirements for Mautic 7?**
PHP 8.2, 8.3, 8.4, or 8.5 with the xml, mysql, imap, zip, intl, curl, gd, mbstring, and bcmath extensions, npm (required since 5.0), and, since the 7.0 upgrade raised the floors, MySQL 8.4.0+ or MariaDB 10.11.0+. max_execution_time must be at least 240 seconds and admin passwords must meet a complexity rule since 5.1. The requirements page still states MySQL 5.7 and MariaDB 10.2 minimums, which lag the UPGRADE-7.0 document, and shared hosting is discouraged outright.

**How does Mautic handle GDPR compliance?**
The features page describes IP anonymization for visitor records, site tracking that can be placed behind a cookie consent gate, automated cleanup of anonymous visitors, audit logs, and inactive contacts after a configurable time frame, and CCPA do-not-sell list syncing through MaxMind-powered cron jobs (mautic:max-mind:purge and mautic:donotsell:download). Contacts get a preference center and frequency rules. Worth knowing: the documentation itself has no dedicated GDPR page, so these capabilities live on a marketing page and the implementation work stays with whoever operates the instance.

- **Pricing:** Open Source
- **Category:** [Marketing Automation](/categories/marketing-automation/)
- **GitHub:** ★ 10472
- **Founded:** 2014
- **HQ:** Community project; fiscal host Open Source Collective
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Mautic is a tool in Marketing Automation with free and open source. The catalog documents 10 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

HubSpot Marketing Hub

All-in-one marketing automation with AI-powered content, email, and campaign tools

ActiveCampaign

AI-powered marketing automation and CRM for small to mid-size businesses

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

Albert AI

Autonomous AI platform that manages and optimizes digital advertising campaigns

Adobe Marketo Engage

Enterprise B2B marketing automation with AI-driven lead management and engagement

[More Marketing Automation Tools →](/categories/marketing-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Marketing Automation](/categories/marketing-automation/)
- Mautic
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Mautic review (2026): pricing, AI features, verdict

Open-source marketing automation platform with email, campaigns, and lead management

Marketing Automation · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Mautic &#8594;](https://www.mautic.org)

[How we review](/methodology/) · No affiliate links

[Visit Mautic &#8594;](https://www.mautic.org)

## MartechSignal Score: 38/60

Mautic is the open-source marketing automation standard: 10.5k stars under GPL with managed hosting from EUR 247.50/mo. No AI features documented, and the campaign engine does not need them.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Mautic is the longest-running open-source marketing automation platform: email, landing pages, forms, segments, campaigns, contact scoring, and multi-channel messaging across email, SMS, web notifications, and mobile push, all self-hosted under GPL-3.0. Started in 2014, it has been community-governed since Acquia acquired Mautic Inc. in May 2019; the trademark is now held by fiscal host Open Source Collective and operations run through an elected Mautic Council, with Acquia and Dropsolid the largest funders. Around 10,472 GitHub stars, eleven bundled plugin packages, and translations into 70 languages reflect that community. The current line is 7.x (7.2.0 shipped in September 2026) and its requirements are serious: PHP 8.2 or newer, minimums raised to MySQL 8.4 and MariaDB 10.11 in the 7.0 release, npm for asset builds, mandatory cron jobs for segments, campaigns, and the email queue, and command-line-only updates, since browser updating was removed in 5.0. Shared hosting is explicitly discouraged. Campaigns, segments, and points-based lead scoring are deterministic rule engines; there is no AI anywhere, and the project&#x27;s AI Manifesto states plainly that it hosts or maintains no AI services and remains AI-agnostic, so any Mautic AI pitch is a third-party layer rather than a product feature. Integrations are plugin-based: Salesforce, HubSpot, Pipedrive, Zoho, and Dynamics among CRMs, plus WordPress, Twilio, Mailchimp, Gmail and Outlook connectors, Google Tag Manager, Amazon S3, and Zapier. The project&#x27;s own comparison page positions Mautic for organizations whose automation grows more complex over time and that need control over data governance and infrastructure with predictable costs rather than contact-based fees, while conceding HubSpot for teams that want a polished hosted experience. The software is free; money enters through partner Dropsolid&#x27;s managed hosting (from € 247.50 a month, 14-day trial, no card) and paid Extended Long Term Support for older versions. The honest costs are operational: upgrades, backups, deliverability, and cron management are yours, and campaigns cannot be moved between instances.

Mautic homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Key Integrations

- Salesforce
- HubSpot
- Pipedrive
- Zoho
- WordPress
- Twilio
- Mailchimp
- Google Tag Manager
- Amazon S3
- Zapier
## Pricing

Mautic is free to self-host under the GPL-3.0 licence, paid plans start at €247.5/mo as of 2026-09.

Free and open source (GPL-3.0), self-hosted. Managed hosting by official partner Dropsolid from € 247.50/mo with a 14-day no-card trial; paid Extended Long Term Support (ELTS) sold by the project for old versions.

Current plans and limits live on the [Mautic pricing page](https://www.mautic.org/pricing).

## How to install

- Composer is the canonical path since Mautic 6: composer create-project mautic/recommended-project:^7.0 some-dir --no-interaction, then php bin/console mautic:install https://m.example.com with database, mailer, and admin flags. The 7.1 install docs still show the older ^5 template, so follow the 7.x recommended-project README.
- Requirements (mautic.org/mautic-requirements): PHP 8.2 to 8.5 with the xml, mysql, imap, zip, intl, curl, gd, mbstring, and bcmath extensions, npm from 5.0 onward, and, per UPGRADE-7.0.md, MySQL 8.4+ or MariaDB 10.11+ (the requirements page still says 5.7/10.2 and lags the release). max_execution_time needs at least 240 seconds, and admin passwords must be complex since 5.1.
- Docker: docker pull mautic/mautic (apache and fpm variants, about 615 MB) with compose roles for mautic_web, mautic_worker, and mautic_cron; CLI commands run as www-data inside the mautic_web container, for example docker compose exec --user www-data --workdir /var/www/html mautic_web php ./bin/console mautic:install https://mautic.example.com.
- Cron is mandatory, not optional: mautic:segments:update, mautic:campaigns:update, and mautic:campaigns:trigger (the docs suggest 15-minute offsets), messenger:consume email for the queue, and optional jobs for broadcasts, imports, webhooks, and IP lookup downloads.
- Updates are CLI-only: mautic:update:find, then mautic:update:apply and mautic:update:apply --finish, or on Composer installs cache:clear plus doctrine:migration:migrate. The docs&#x27; own warning applies before any of it: never update without a working, up-to-date backup. For local development the documented route is DDEV (ddev start).
## Requirements

A VPS or dedicated server: the requirements page says shared hosting can impair performance, cause update failures, and limit functionality, and that community support is unlikely for shared hosting setups. Add PHP 8.2+ with nine documented extensions, npm, MySQL 8.4+ or MariaDB 10.11+, and cron as part of the deployment rather than an option. Budget the operational work too: backups before every update, deliverability configuration (bounce management, monitored inboxes, and S/MIME signing are all documented), and the fact that campaigns cannot be moved between instances, so staging strategy needs deciding early.

## Best for

Organizations that expect automation and integrations to grow more complex over time and need control over data governance and infrastructure, in the project&#x27;s own words: in-house marketing ops with developers nearby, agencies running client instances, and regulated or privacy-conscious teams that cannot put contact data in a vendor&#x27;s cloud and prefer costs tied to real usage rather than contact-based fees.

## Not for

Teams without technical staff: browser updates are gone, cron is mandatory, shared hosting is discouraged, and the marketplace does not yet verify plugin version compatibility, so blind plugin installs are warned against. Also not for anyone shopping for AI features, which the project explicitly does not provide, and not for teams that need to copy campaigns between staging and production, which the roadmap lists as currently impossible.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from mautic.org, docs.mautic.org (the 7.1 line), the GitHub repo, Packagist, and Docker Hub (September 2026). Not a hands-on review. The release cadence is healthy: 7.2.0 shipped September 2, 2026 and 7.1.3 on July 7, with a stated cadence of monthly patches, quarterly minors, and a major every two years, plus published support windows including a 7.3 LTS due December 2026.

The correction that matters: our earlier record listed AI-powered lead scoring, AI email personalization, and AI campaign optimization. None exist. The project&#x27;s AI Manifesto states that it does not currently host or maintain any AI services as part of the Mautic project and that Mautic is strictly AI-agnostic. Lead scoring is a deterministic points rule engine. We have emptied the AI feature list rather than soften it.

Second correction: governance and integrations. Our Raleigh, North Carolina headquarters claim has no source anywhere on mautic.org; Mautic has been community-governed since Acquia bought Mautic Inc. in 2019, with the trademark held by Open Source Collective and operations under an elected council. Slack, Google Analytics, and Stripe appeared in our integration list with no docs page or official plugin repo behind them (plugin-slack and plugin-stripe return 404); we replaced them with documented plugins.

Vendor numbers deserve caution on this listing: the homepage claims both 40,000+ and 200K+ companies use Mautic, and its stat counters render placeholder zeros, so we quote neither. The verifiable scale markers are the star count, the 70-language translation effort, and the eleven bundled plugin packages in the core repository.

## Verdict

The most complete open-source answer to HubSpot if you have the ops capacity to run it: real campaigns, segments, and scoring under GPL-3.0, no AI, and no shortcuts on maintenance.

## Pros and cons

## Related concepts

- [Marketing automation](/glossary/marketing-automation/)
- [Customer journey](/glossary/customer-journey/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Mautic: Open-source marketing automation platform with email, campaigns, and lead management. The public repository carries 10,472 stars. Mautic offers a public API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Mautic has a free tier; paid plans start at €247.5/mo. Free and open source (GPL-3.0), self-hosted. Managed hosting by official partner Dropsolid from € 247.50/mo with a 14-day no-card trial; paid Extended Long Term Support (ELTS) sold by the project for old versions. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

The most complete open-source answer to HubSpot if you have the ops capacity to run it: real campaigns, segments, and scoring under GPL-3.0, no AI, and no shortcuts on maintenance.

No. The update-in-UI feature was deprecated in 4.2 and, per the 7.1 upgrade docs, completely removed from Mautic 5.0, partly because it required significant resources and could fail mid-update. Updates now run at the command line: php bin/console mautic:update:find to check, mautic:update:apply to install, and mautic:update:apply --finish to complete, or cache:clear plus doctrine:migration:migrate on Composer installs. The docs also warn never to update without a working, up-to-date backup.

PHP 8.2, 8.3, 8.4, or 8.5 with the xml, mysql, imap, zip, intl, curl, gd, mbstring, and bcmath extensions, npm (required since 5.0), and, since the 7.0 upgrade raised the floors, MySQL 8.4.0+ or MariaDB 10.11.0+. max_execution_time must be at least 240 seconds and admin passwords must meet a complexity rule since 5.1. The requirements page still states MySQL 5.7 and MariaDB 10.2 minimums, which lag the UPGRADE-7.0 document, and shared hosting is discouraged outright.

The features page describes IP anonymization for visitor records, site tracking that can be placed behind a cookie consent gate, automated cleanup of anonymous visitors, audit logs, and inactive contacts after a configurable time frame, and CCPA do-not-sell list syncing through MaxMind-powered cron jobs (mautic:max-mind:purge and mautic:donotsell:download). Contacts get a preference center and frequency rules. Worth knowing: the documentation itself has no dedicated GDPR page, so these capabilities live on a marketing page and the implementation work stays with whoever operates the instance.

## Similar Tools

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Google Doesn't Need Your Site Anymore. You Taught It Everything It Knows.](/blog/google-doesnt-need-your-site-anymore-you-taught-it-everything-it-knows/)
- [Your AI Marketing Agent Doesn't Need Better Prompts](/blog/ai-agents-need-campaign-state/)
## Also featured in

- [Best Open-Source Marketing Tools (2026): 8 compared](/best/open-source-marketing-tools/) &mdash; Marketing teams that want HubSpot-class automation they can host themselves
### Quick Facts

Related guides: [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/mautic/#app",
    "name": "Mautic",
    "description": "Open-source marketing automation platform with email, campaigns, and lead management",
    "image": "https://martechsignal.com/og/tools/mautic.png",
    "url": "https://martechsignal.com/tools/mautic/",
    "sameAs": [
      "https://www.mautic.org"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/mautic/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 247.5,
      "priceCurrency": "EUR",
      "url": "https://www.mautic.org/pricing",
      "priceValidUntil": "2026-12-31"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://martechsignal.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Marketing Automation",
        "item": "https://martechsignal.com/categories/marketing-automation/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Mautic",
        "item": "https://martechsignal.com/tools/mautic/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Mautic?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mautic: Open-source marketing automation platform with email, campaigns, and lead management. The public repository carries 10,472 stars. Mautic offers a public API for custom integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Mautic cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mautic has a free tier; paid plans start at \u20ac247.5/mo. Free and open source (GPL-3.0), self-hosted. Managed hosting by official partner Dropsolid from \u20ac 247.50/mo with a 14-day no-card trial; paid Extended Long Term Support (ELTS) sold by the project for old versions. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Mautic a good self-hosted Marketing Automation tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most complete open-source answer to HubSpot if you have the ops capacity to run it: real campaigns, segments, and scoring under GPL-3.0, no AI, and no shortcuts on maintenance."
        }
      },
      {
        "@type": "Question",
        "name": "Can I update Mautic from the browser?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. The update-in-UI feature was deprecated in 4.2 and, per the 7.1 upgrade docs, completely removed from Mautic 5.0, partly because it required significant resources and could fail mid-update. Updates now run at the command line: php bin/console mautic:update:find to check, mautic:update:apply to install, and mautic:update:apply --finish to complete, or cache:clear plus doctrine:migration:migrate on Composer installs. The docs also warn never to update without a working, up-to-date backup."
        }
      },
      {
        "@type": "Question",
        "name": "What are the system requirements for Mautic 7?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "PHP 8.2, 8.3, 8.4, or 8.5 with the xml, mysql, imap, zip, intl, curl, gd, mbstring, and bcmath extensions, npm (required since 5.0), and, since the 7.0 upgrade raised the floors, MySQL 8.4.0+ or MariaDB 10.11.0+. max_execution_time must be at least 240 seconds and admin passwords must meet a complexity rule since 5.1. The requirements page still states MySQL 5.7 and MariaDB 10.2 minimums, which lag the UPGRADE-7.0 document, and shared hosting is discouraged outright."
        }
      },
      {
        "@type": "Question",
        "name": "How does Mautic handle GDPR compliance?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The features page describes IP anonymization for visitor records, site tracking that can be placed behind a cookie consent gate, automated cleanup of anonymous visitors, audit logs, and inactive contacts after a configurable time frame, and CCPA do-not-sell list syncing through MaxMind-powered cron jobs (mautic:max-mind:purge and mautic:donotsell:download). Contacts get a preference center and frequency rules. Worth knowing: the documentation itself has no dedicated GDPR page, so these capabilities live on a marketing page and the implementation work stays with whoever operates the instance."
        }
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "author": {
      "@type": "Person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://martechsignal.com/#organization",
      "name": "MartechSignal"
    },
    "datePublished": "2026-09-26",
    "reviewBody": "Mautic is the open-source marketing automation standard: 10.5k stars under GPL with managed hosting from EUR 247.50/mo. No AI features documented, and the campaign engine does not need them.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/mautic/#app",
      "name": "Mautic",
      "url": "https://martechsignal.com/tools/mautic/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 38,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
