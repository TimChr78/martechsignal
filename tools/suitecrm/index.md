# SuiteCRM review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | Free self-hosted open source with paid cloud hosting available; the hosting prices are not itemized in the catalog (the vendor pricing page: [vendor site](https://www.suitecrm.com), verified 2026-09-07). |
| Feature depth | 7/10 | Sales, marketing and support automation across one codebase covers the full CRM triangle, the reason it persists (vendor documentation: [vendor site](https://www.suitecrm.com), verified 2026-09-28). |
| Integrations | 3/10 | No named integrations in the catalog; APIs and community modules carry the extension story (vendor documentation: [vendor site](https://www.suitecrm.com), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://www.suitecrm.com), verified 2026-09-28). |
| Openness | 9/10 | AGPL-3.0 self-hosted with 5.7k GitHub stars and the whole suite free (the source repository: [repository](https://github.com/SuiteCRM/SuiteCRM), verified 2026-09-28). |
| Operational maturity | 7/10 | A SugarCRM fork with years of production deployments and a stable release cadence (vendor documentation: [vendor site](https://www.suitecrm.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ AGPL-3.0 licence with free self-hosting | ✗ No hands-on test - this assessment is based on vendor documentation and the public repository |
| ✓ API access for custom integrations |  |
| ✓ Active public repository (5,774 GitHub stars counted at last check) |  |

**What is SuiteCRM?**
SuiteCRM: Enterprise-grade open-source CRM with sales, marketing, and support automation. The public repository carries 5,774 stars. SuiteCRM offers a public API for custom integrations.

**How much does SuiteCRM cost?**
SuiteCRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 5,774 stars. You pay in server time and maintenance, not licences.

**Is SuiteCRM a good self-hosted CRM tool in 2026?**
The established open-source CRM workhorse: unmatched module depth and free core workflows, with no AI, no mobile app, and a migration path that needs planning. Current, maintained, and still the default on-premise choice.

**Does SuiteCRM have AI features?**
No native ones. The documented feature set, release notes, roadmap, and user guide contain no AI, machine learning, or predictive capability, and there is no AI add-on in the vendor's price list; SuiteASSURED and the support tiers cover hosting, fixes, and guarantees. Teams that want scoring or prediction build it themselves against the documented V8 API with OAuth, or run enrichment and scoring in an external tool and write results back to records. Any vendor claiming AI-driven SuiteCRM features is describing custom work.

**How do you migrate from SuiteCRM 7 to SuiteCRM 8?**
As a fresh installation, not an in-place patch. The docs require the latest 7.x release as the source (migrating from an older 7.x will fail or produce unstable results), then a new SuiteCRM 8 install with three console commands: ./bin/console suitecrm:app:setup-legacy-migration, ./bin/console suitecrm:app:upgrade -t with the migration package, for example SuiteCRM-8.7.0, and ./bin/console suitecrm:app:upgrade-finalize. The 7 codebase is copied into public/legacy and continues to serve the legacy surface. Test on a copy, since 8.10 also removed the SOAP portal as a breaking change.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 5774
- **HQ:** Stirling, Scotland, UK
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** SuiteCRM is a tool in CRM with free and open source. The catalog documents a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Django CRM

Multi-tenant open-source CRM on Django with leads, campaigns, and self-hosting

EspoCRM

Lightweight open-source CRM with sales automation, marketing tools, and customer management

Cordys CRM

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

Krayin CRM

Free open-source Laravel CRM for SMEs and enterprises with full customer lifecycle management

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- SuiteCRM
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## SuiteCRM review (2026): pricing, AI features, verdict

Enterprise-grade open-source CRM with sales, marketing, and support automation

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit SuiteCRM →](https://www.suitecrm.com)

[How we review](/methodology/) · No affiliate links

[Visit SuiteCRM →](https://www.suitecrm.com)

## MartechSignal Score: 34/60

SuiteCRM is the safe long-liver of open-source CRM: sales, marketing and support automation on one AGPL codebase. The AI era has not really arrived on it yet.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

SuiteCRM is the AGPLv3 open-source CRM that forked SugarCRM Community Edition and outlived it, maintained by SuiteCRM Ltd from Stirling, Scotland. Two release lines are current: 8.10.2 and 7.15.2 shipped on the same day in July 2026 as a joint security release, and 7.15 is an extended support release with security fixes published into 2028. The module set is the deepest in this directory's CRM category: leads, accounts, contacts, opportunities, quotes, invoices, contracts, PDF templates, campaigns with target lists and confirmed opt-in, surveys, events, cases with a knowledge base, bugs, reports with scheduled runs, calendar, projects, and document management, plus Studio for no-code layout changes and Module Builder for new entities from six templates. Workflow automation is free in the core, with calculated fields, which is the main structural difference from EspoCRM, where workflows are a paid extension. What SuiteCRM does not have matters too: there is no native AI anywhere in the documented feature set, and no official mobile app. Elasticsearch is an optional search backend, and Redis or RabbitMQ are optional message transports for background jobs beyond a single server. Two APIs are documented, the newer V8 API with OAuth and the legacy V4. Requirements are PHP 8.2 to 8.4 with MariaDB 10.6 or later, or MySQL 8.0 or later, on Apache 2.4. Installation is a pre-built zip with a permissions pass, then a browser wizard or a CLI installer with flags for the admin user, database, and demo data. Migrating from 7.x to 8.x is a documented fresh install with three console commands, not a patch. Commercial support is GBP-priced: hosting from 50 pounds monthly with unlimited users, and SuiteASSURED from 3,350 pounds a year carrying warranties and indemnities. This assessment is from the repository, the docs, and the vendor site.

SuiteCRM homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

SuiteCRM is free to self-host under the AGPL-3.0 licence.

Free open-source self-hosted; paid cloud hosting available

## How to install

- Download the pre-built package from suitecrm.com (the docs direct you to pre-built installables rather than composer), unzip into the web root, then run the documented permissions pass: find . -type d -not -perm 2755 -exec chmod 2755 {} \; , find . -type f -not -perm 0644 -exec chmod 0644 {} \; , find . ! -user www-data -exec chown www-data:www-data {} \; , and chmod +x bin/console.
- Install from the CLI in one command: ./bin/console suitecrm:app:install, or pass everything as flags, for example -u "admin" -p "pass" -U "root" -P "dbpass" -H "mariadb" -N "suitecrm" -S "https://yourcrm.com/" -d "yes", where -d controls demo data. The browser installer is the alternative.
- For the 7.15 line the flow is unzip, chown -R www-data:www-data, chmod 755 with 775 on cache, custom, modules, themes, data, upload, and config_override.php, then open install.php and step through license, system check, database, and site config.
- Scheduled jobs need cron on both lines: * * * * * cd /var/www/html; php -f cron.php > /dev/null 2>&1.
- Front-end development has extra requirements (Node 20.11, yarn 4, Angular CLI 18) that the docs mark as not required for production, since you install a pre-built package.
## Requirements

SuiteCRM 8.10 supports PHP 8.2, 8.3, and 8.4 with MariaDB 10.6, 10.11, 11.4, or 11.8, or MySQL 8.0 or 8.4, on Apache 2.4. The 7.15 line adds PHP 8.1 and supports IIS 10 and Windows Server 2019 or later, plus SQL Server 2019 as a database option. Elasticsearch is optional for search; RabbitMQ or Redis are optional transports for asynchronous tasks, with the default transport your existing database through Doctrine.

## Best for

Organizations that need a full-module, on-premise CRM with no per-seat fees and workflow automation included free: sales, service, and campaign operations in one PHP application, with a UK-based vendor available for hosting, support, and an indemnity-carrying build. Long-lived 7.x installs get an ESR with security fixes into 2028.

## Not for

Teams shopping for AI features: there is no native AI capability in the documented product, so lead scoring and prediction mean building on the API or pairing another tool. Also reconsider if your team lives on mobile, since no official mobile app is documented, or if you want a product where upgrades are patches rather than planned migrations.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the repository, docs.suitecrm.com, and suitecrm.com. Not a hands-on review. The maintenance picture is the strongest signal: both release lines shipped security releases on the same day in July 2026, 8.x minor releases arrive roughly every eight weeks per the roadmap, and 7.15 carries published ESR dates. This is a project that still engineers, not a zombie fork.

The correction that matters most against our earlier record: SuiteCRM has no native AI. Scanning the 8.9 and 8.10 release notes, the 8.x user guide index, the roadmap, and the what-is-SuiteCRM page turns up no AI, LLM, machine learning, or predictive feature; the closest phrase is a marketing header, Actionable Intelligence, that refers to charts and reports. Earlier claims of AI lead scoring and predictive analytics were wrong, and any scoring or prediction work would be your own build on the V8 API.

Version 8.10.0 is a substantial release: image fields, PDF generation including bulk output, campaign error handling, asynchronous tasks, and the merge of the 7.15 code line into 8.10, which brought PHP 8.4 support, advanced calendar integration and sync, and OAuth authorization code grant for the V8 API. Version 8.10.2 then removed the SOAP portal as a breaking change and added a V4 API query configuration flag that defaults to on, so read the release notes before upgrading rather than assuming drop-in compatibility.

The 7.x to 8.x migration is documented and is deliberately not a patch: you stand up a new SuiteCRM 8 install, migrate from the latest 7.x release only, and run three console commands, setup-legacy-migration, upgrade with a target package such as SuiteCRM-8.7.0, and upgrade-finalize. The 7 codebase ends up copied into public/legacy. The docs warn that migrating from an older 7.x will fail or produce unstable results, which is the step teams skip.

Commercial pricing is published in GBP on suitecrm.com: fully managed hosting from 50 pounds monthly, hosted tiers at 143,198, and 308 pounds monthly (130,180, and 280 annually) with unlimited users, Quick Start implementation from 2,520 pounds, standard support at 1,200 pounds for ten hours, and SuiteASSURED from 3,350 pounds a year for ten care hours with warranties, indemnities, and performance guarantees.

## Verdict

The established open-source CRM workhorse: unmatched module depth and free core workflows, with no AI, no mobile app, and a migration path that needs planning. Current, maintained, and still the default on-premise choice.

## Pros and cons

## Related concepts

- [CRM](/glossary/crm/)
- [Lead scoring](/glossary/lead-scoring/)
- [MQL / SQL](/glossary/mql-sql/)
- [Customer journey](/glossary/customer-journey/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

SuiteCRM: Enterprise-grade open-source CRM with sales, marketing, and support automation. The public repository carries 5,774 stars. SuiteCRM offers a public API for custom integrations.

SuiteCRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 5,774 stars. You pay in server time and maintenance, not licences.

The established open-source CRM workhorse: unmatched module depth and free core workflows, with no AI, no mobile app, and a migration path that needs planning. Current, maintained, and still the default on-premise choice.

No native ones. The documented feature set, release notes, roadmap, and user guide contain no AI, machine learning, or predictive capability, and there is no AI add-on in the vendor's price list; SuiteASSURED and the support tiers cover hosting, fixes, and guarantees. Teams that want scoring or prediction build it themselves against the documented V8 API with OAuth, or run enrichment and scoring in an external tool and write results back to records. Any vendor claiming AI-driven SuiteCRM features is describing custom work.

As a fresh installation, not an in-place patch. The docs require the latest 7.x release as the source (migrating from an older 7.x will fail or produce unstable results), then a new SuiteCRM 8 install with three console commands: ./bin/console suitecrm:app:setup-legacy-migration, ./bin/console suitecrm:app:upgrade -t with the migration package, for example SuiteCRM-8.7.0, and ./bin/console suitecrm:app:upgrade-finalize. The 7 codebase is copied into public/legacy and continues to serve the legacy surface. Test on a copy, since 8.10 also removed the SOAP portal as a breaking change.

## Similar Tools

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
## Also featured in

- [Best open-source CRM tools (2026)](/best/open-source-crm/) — Best for teams that want the widest free feature set.
- [Best Open-Source Marketing Tools (2026): 8 compared](/best/open-source-marketing-tools/) — Sales teams that want a mature, enterprise-shaped CRM they control
### Quick Facts

Related guides: [SuiteCRM in Hubspot Crm alternatives](/alternatives/hubspot-crm/) · [Open Source Crm](/best/open-source-crm/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/suitecrm/#app",
    "name": "SuiteCRM",
    "description": "Enterprise-grade open-source CRM with sales, marketing, and support automation",
    "image": "https://martechsignal.com/og/tools/suitecrm.png",
    "url": "https://martechsignal.com/tools/suitecrm/",
    "sameAs": [
      "https://www.suitecrm.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/suitecrm/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.suitecrm.com",
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
        "name": "CRM",
        "item": "https://martechsignal.com/categories/crm/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "SuiteCRM",
        "item": "https://martechsignal.com/tools/suitecrm/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is SuiteCRM?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "SuiteCRM: Enterprise-grade open-source CRM with sales, marketing, and support automation. The public repository carries 5,774 stars. SuiteCRM offers a public API for custom integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much does SuiteCRM cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "SuiteCRM is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 5,774 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is SuiteCRM a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The established open-source CRM workhorse: unmatched module depth and free core workflows, with no AI, no mobile app, and a migration path that needs planning. Current, maintained, and still the default on-premise choice."
        }
      },
      {
        "@type": "Question",
        "name": "Does SuiteCRM have AI features?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No native ones. The documented feature set, release notes, roadmap, and user guide contain no AI, machine learning, or predictive capability, and there is no AI add-on in the vendor's price list; SuiteASSURED and the support tiers cover hosting, fixes, and guarantees. Teams that want scoring or prediction build it themselves against the documented V8 API with OAuth, or run enrichment and scoring in an external tool and write results back to records. Any vendor claiming AI-driven SuiteCRM features is describing custom work."
        }
      },
      {
        "@type": "Question",
        "name": "How do you migrate from SuiteCRM 7 to SuiteCRM 8?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "As a fresh installation, not an in-place patch. The docs require the latest 7.x release as the source (migrating from an older 7.x will fail or produce unstable results), then a new SuiteCRM 8 install with three console commands: ./bin/console suitecrm:app:setup-legacy-migration, ./bin/console suitecrm:app:upgrade -t with the migration package, for example SuiteCRM-8.7.0, and ./bin/console suitecrm:app:upgrade-finalize. The 7 codebase is copied into public/legacy and continues to serve the legacy surface. Test on a copy, since 8.10 also removed the SOAP portal as a breaking change."
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
    "reviewBody": "SuiteCRM is the safe long-liver of open-source CRM: sales, marketing and support automation on one AGPL codebase. The AI era has not really arrived on it yet.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/suitecrm/#app",
      "name": "SuiteCRM",
      "url": "https://martechsignal.com/tools/suitecrm/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 34,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
