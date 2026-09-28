# Matomo review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | matomo.org/pricing publishes Cloud from 22 EUR per month for 50,000 hits up to 14,850 EUR per month at 100 million hits and On-Premise bundles at 275, 1,450 and 3,400 EUR per month next to the free self-hosted core, with the small caveat that the static page shows a stale 29 EUR figure before scripts load (the vendor pricing page). |
| Feature depth | 8/10 | Core analytics, ecommerce tracking, goals, segments and the dashboard are free while funnels, cohorts, heatmaps, session recordings, A/B testing and attribution make up deep premium plugin coverage (vendor documentation). |
| Integrations | 7/10 | An official WordPress plugin with 100,000-plus installs, Tag Manager, a Google Analytics importer, Shopify and BigQuery sit beside a public plugin marketplace and an API (vendor documentation). |
| AI capability | 7/10 | A free official MCP Server plugin connects Matomo to ChatGPT and Claude with write actions behind approval, joined by AI chatbot traffic reports, an AIAgents plugin and the AI Connector (vendor documentation). |
| Openness | 10/10 | The core is GPL-3.0, self-hostable with no licence fee, and the vendor commits to keeping self-hosting free permanently (the source repository). |
| Operational maturity | 8/10 | Founded in 2007 with 21,851 GitHub stars, releases through 5.13.0 in August 2026 plus an active 6.x branch, and a commercial Cloud operation behind it (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; GPL-3.0 licence with free self-hosting | &#10007; Paid plans start at $22/mo once past the free tier |
| &#10003; AI capabilities: AI chatbot traffic reports |  |
| &#10003; Active public repository (21,851 GitHub stars counted at last check) |  |
| &#10003; Native integrations include WordPress, Matomo Tag Manager, Google Tag Manager (8 listed) |  |

**What is Matomo?**
Open-source web analytics platform with full data ownership and AI-powered insights. It ships with AI chatbot traffic reports, 21,851 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Matomo cost?**
Matomo has a free tier; paid plans start at €22/mo. Self-hosted core free (GPL v3+). On-Premise premium bundles: Team 275 €/mo, Business 1,450 €/mo, Enterprise 3,400 €/mo, about 17% less billed annually. Cloud from 22 €/mo for 50,000 hits, scaling to 14,850 €/mo at 100 million. 21-day Cloud trial. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers.

**Is Matomo a good self-hosted Analytics &amp; Attribution tool in 2026?**
The analytics platform to pick when data residency and ownership are requirements rather than preferences. Budget for operations time and for the premium plugins you will use.

**What is the cheapest Matomo Cloud plan?**
The lowest tier is 22 euros per month for 50,000 hits, where a hit counts as a page view, event, download, outlink, onsite search, or content tracking request. Tiers scale to 1,600 euros per month at 10 million hits, and annual billing gives two months free. Watch the pricing page&#x27;s static HTML, which shows a stale 29-euro figure until JavaScript loads the tier table.

**Is Matomo really GDPR compliant?**
Matomo claims adherence to GDPR, HIPAA, CCPA, LGPD, and PECR, with IP anonymization, configurable data anonymization, an opt-out, first-party cookies by default, and tools to delete visitor data on request. It states that France&#x27;s CNIL lists it among tools usable without consent and that Cloud data stays in Europe. Those are vendor claims, and your compliance still depends on configuration, particularly cookie consent and retention.

**Matomo or Google Analytics 4?**
The differences that matter are ownership and sampling. Matomo stores data in your own database or its EU-based Cloud, generates unsampled reports on every plan, and exports raw data on request. GA4 keeps data in Google&#x27;s infrastructure and applies sampling, which is why European regulator rulings feature in Matomo&#x27;s comparisons. GA4 still wins on cost at low traffic and on Google Ads integration.

**Does Matomo have AI features?**
Yes, but they measure AI rather than behave like an AI analyst. Matomo 5.12.0 added reports for AI chatbot content requests and real-time chatbot traffic, an AIAgents plugin ships enabled on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT, Claude, and other MCP clients, with write actions requiring approval. There is no AI anomaly detection or predictive analytics in the product today.

- **Pricing:** Open Source
- **Category:** [Analytics &amp; Attribution](/categories/analytics/)
- **GitHub:** ★ 21851
- **Founded:** 2007
- **HQ:** Wellington, New Zealand
- **API:** Yes
- **Last verified:** 2026-09-06

**Verdict:** Matomo is a tool in Analytics &amp; Attribution with free and open source. The catalog documents 4 AI features, 8 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-06. This is a desk review, not a hands-on test. Desk-reviewed

Plausible Analytics

Lightweight, privacy-friendly open-source web analytics alternative to Google Analytics

PostHog

Open-source product analytics platform with session replay, feature flags, experiments, and surveys

Amplitude

AI-powered digital analytics platform for product and marketing teams

Triple Whale

AI-powered ecommerce analytics and attribution platform for DTC brands

[More Analytics &amp; Attribution Tools →](/categories/analytics/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Analytics &amp; Attribution](/categories/analytics/)
- Matomo
Re-check pending: pricing last verified 2026-09-06 (22 days ago).

## Matomo review (2026): pricing, AI features, verdict

Open-source web analytics platform with full data ownership and AI-powered insights

Analytics &amp; Attribution · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-06

Looking for options? [Best Matomo alternatives](/alternatives/matomo/)

[Visit Matomo &#8594;](https://matomo.org)

[How we review](/methodology/) · No affiliate links

[Visit Matomo &#8594;](https://matomo.org)

## MartechSignal Score: 49/60

The pick when analytics data residency is a requirement rather than a preference, with an open core and a real premium plugin business behind it. Budget both operations time for self-hosting and plugin fees for the headline behavioral features.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Matomo is an open-source web analytics platform you run on your own infrastructure, licensed GPL v3 or later, with 5.13.0 released in August 2026 and an active 6.x branch. Installation is a documented nine-step wizard: download matomo.zip from builds.matomo.org, upload it to a directory or subdomain, set permissions on tmp and config, then walk through a system check, database setup, superuser creation, first-site setup, and the JavaScript tracking tag. The README asks for PHP 8.1 or newer with MySQL 8 or MariaDB 10.6, which is stricter than the requirements page on matomo.org, still telling PHP 7.2.5 users that Matomo 5 works well with PHP 8. Sites above a few hundred visits a day need an archiving cron job. The feature split matters more than the feature list. Core analytics, ecommerce tracking, goals, segments, a customizable dashboard, and an API are free. Funnels, cohorts, custom reports, form analytics, media analytics, A/B testing, heatmaps and session recordings, multi-channel attribution, roll-up reporting, and users flow are paid premium plugins, sold individually or in bundles. Matomo Tag Manager and the Google Analytics Importer are free. On-Premise bundles run 275 euros a month for Team, 1,450 for Business, and 3,400 for Enterprise, while Cloud starts at 22 euros a month for 50,000 hits and scales into four figures at hundreds of millions of hits. Privacy is the reason teams pick it. Matomo claims 100 percent data ownership, unsampled reporting on every plan, adherence to GDPR, HIPAA, CCPA, LGPD, and PECR, and a CNIL listing it says allows consent-free use. Cloud data stays in Europe, and the vendor commits to keeping self-hosting free permanently. Matomo&#x27;s AI work measures AI traffic rather than adding AI analytics. Version 5.12.0 added AI chatbot content-request and real-time reports, an AIAgents plugin ships enabled on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT, Claude, and other MCP clients, with write actions gated behind approval.

Matomo homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI chatbot traffic reports
- MCP Server plugin
- AI Agent Overview report
- AI Connector (query analytics in plain language)
## Key Integrations

- WordPress
- Matomo Tag Manager
- Google Tag Manager
- Google Analytics Importer
- Shopify
- BigQuery
- OneTrust
- Cookiebot
## Pricing

Matomo is free to self-host under the GPL-3.0 licence, paid plans start at €22/mo as of 2026-09.

Self-hosted core free (GPL v3+). On-Premise premium bundles: Team 275 €/mo, Business 1,450 €/mo, Enterprise 3,400 €/mo, about 17% less billed annually. Cloud from 22 €/mo for 50,000 hits, scaling to 14,850 €/mo at 100 million. 21-day Cloud trial.

Current plans and limits live on the [Matomo pricing page](https://matomo.org/pricing/).

## How to install

- Download the latest release with wget https://builds.matomo.org/matomo.zip and unzip it. The docs warn against third-party sources and point to GPG signatures for verification.
- Upload the files to a directory such as yourdomain.org/analytics/ or to a subdomain, using SFTP or SCP, which the docs list as the preferred transfer method.
- Set permissions so the web server can read every file and only tmp/ and config/ are writable. Once installed, the docs recommend locking config/ back to read-only.
- Open the URL and follow the wizard: system check, MySQL setup (use a dedicated database and a restricted user, and put non-default ports after the hostname, as in localhost:3307), superuser account, first website, and the JavaScript tag placed before the closing head tag.
- If the site gets more than a few hundred visits per day, set up the auto-archiving cron job the docs recommend, so reports are pre-processed instead of computed on request.
- Prefer not to run it? Matomo ships an official WordPress plugin with 100,000-plus active installs and a Docker route, and a 21-day Cloud trial with a live demo at demo.matomo.cloud.
## Requirements

The GitHub README asks for PHP 8.1.0 or newer, MySQL 8.0+ or MariaDB 10.6+, and pdo_mysql or mysqli. Matomo&#x27;s own requirements page still says Matomo 4.x needs PHP 7.2.5+ and that Matomo 5 works well with PHP 8, so treat the README as the current floor. Apache, Nginx, IIS, and LiteSpeed all work, and the MySQL user needs grants including CREATE TEMPORARY TABLES and LOCK TABLES.

## Best for

Organizations with a compliance reason to keep analytics data in-house: EU-facing sites, healthcare, finance, and the public sector. Also a fit for anyone who needs unsampled raw data or wants to keep history when changing vendors.

## Not for

Teams that want analytics with no ops burden. Self-hosting means updates, backups, performance tuning, and the archiving cron, and most headline features beyond core reporting are paid plugins rather than inclusions.

## Review notes

Assessed from matomo.org, the plugin marketplace, and the GitHub repository rather than a self-hosted deployment. The install path is a nine-step wizard over a downloaded matomo.zip, and the requirements that matter are the ones in the README: PHP 8.1 or newer and MySQL 8 or MariaDB 10.6. Matomo&#x27;s own requirements page still describes the older PHP 7.2.5 floor, so read the README first.

The free-versus-paid split is the part most reviews gloss over. Core analytics, ecommerce tracking, goals, segments, the dashboard, and the API are free; funnels, cohorts, custom reports, form analytics, heatmaps, session recordings, A/B testing, attribution, and roll-up reporting are paid plugins, bundled at 275 to 3,400 euros a month depending on tier. Tag Manager and the Google Analytics importer are the notable free exceptions.

The AI story is about AI traffic, not AI analysis. Version 5.12.0 added reports for chatbot content requests, an AIAgents plugin ships on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT and Claude with write actions behind approval. For teams evaluating on privacy, the relevant claims, including the CNIL listing and ISO 27001, are the vendor&#x27;s own and deserve independent checking.

## Verdict

The analytics platform to pick when data residency and ownership are requirements rather than preferences. Budget for operations time and for the premium plugins you will use.

## Pros and cons

## Related concepts

- [Attribution models](/glossary/marketing-attribution-models/)
- [First-party data](/glossary/first-party-data/)
- [DMP](/glossary/dmp/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source web analytics platform with full data ownership and AI-powered insights. It ships with AI chatbot traffic reports, 21,851 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Matomo has a free tier; paid plans start at €22/mo. Self-hosted core free (GPL v3+). On-Premise premium bundles: Team 275 €/mo, Business 1,450 €/mo, Enterprise 3,400 €/mo, about 17% less billed annually. Cloud from 22 €/mo for 50,000 hits, scaling to 14,850 €/mo at 100 million. 21-day Cloud trial. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers.

The analytics platform to pick when data residency and ownership are requirements rather than preferences. Budget for operations time and for the premium plugins you will use.

The lowest tier is 22 euros per month for 50,000 hits, where a hit counts as a page view, event, download, outlink, onsite search, or content tracking request. Tiers scale to 1,600 euros per month at 10 million hits, and annual billing gives two months free. Watch the pricing page&#x27;s static HTML, which shows a stale 29-euro figure until JavaScript loads the tier table.

Matomo claims adherence to GDPR, HIPAA, CCPA, LGPD, and PECR, with IP anonymization, configurable data anonymization, an opt-out, first-party cookies by default, and tools to delete visitor data on request. It states that France&#x27;s CNIL lists it among tools usable without consent and that Cloud data stays in Europe. Those are vendor claims, and your compliance still depends on configuration, particularly cookie consent and retention.

The differences that matter are ownership and sampling. Matomo stores data in your own database or its EU-based Cloud, generates unsampled reports on every plan, and exports raw data on request. GA4 keeps data in Google&#x27;s infrastructure and applies sampling, which is why European regulator rulings feature in Matomo&#x27;s comparisons. GA4 still wins on cost at low traffic and on Google Ads integration.

Yes, but they measure AI rather than behave like an AI analyst. Matomo 5.12.0 added reports for AI chatbot content requests and real-time chatbot traffic, an AIAgents plugin ships enabled on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT, Claude, and other MCP clients, with write actions requiring approval. There is no AI anomaly detection or predictive analytics in the product today.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [NocoBase vs NocoDB vs Budibase: pick by team shape, not by spec sheet](/blog/nocobase-vs-nocodb-vs-budibase/)
- [Your agent protocol matters less than your data plumbing](/blog/agent-protocol-vs-data-plumbing/)
### Quick Facts

Related guides: [Alternatives to Matomo](/alternatives/matomo/) · [Matomo vs Plausible](/vs/matomo-vs-plausible/) · [Marketing Analytics Tools](/best/marketing-analytics-tools/) · [Open Source Marketing Tools](/best/open-source-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/matomo/#app",
    "name": "Matomo",
    "description": "Open-source web analytics platform with full data ownership and AI-powered insights",
    "image": "https://martechsignal.com/og/tools/matomo.png",
    "url": "https://martechsignal.com/tools/matomo/",
    "sameAs": [
      "https://matomo.org"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/matomo/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-06",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 22,
      "priceCurrency": "EUR",
      "url": "https://matomo.org/pricing/",
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
        "name": "Analytics & Attribution",
        "item": "https://martechsignal.com/categories/analytics/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Matomo",
        "item": "https://martechsignal.com/tools/matomo/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Matomo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source web analytics platform with full data ownership and AI-powered insights. It ships with AI chatbot traffic reports, 21,851 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Matomo cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Matomo has a free tier; paid plans start at \u20ac22/mo. Self-hosted core free (GPL v3+). On-Premise premium bundles: Team 275 \u20ac/mo, Business 1,450 \u20ac/mo, Enterprise 3,400 \u20ac/mo, about 17% less billed annually. Cloud from 22 \u20ac/mo for 50,000 hits, scaling to 14,850 \u20ac/mo at 100 million. 21-day Cloud trial. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Matomo a good self-hosted Analytics & Attribution tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The analytics platform to pick when data residency and ownership are requirements rather than preferences. Budget for operations time and for the premium plugins you will use."
        }
      },
      {
        "@type": "Question",
        "name": "What is the cheapest Matomo Cloud plan?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The lowest tier is 22 euros per month for 50,000 hits, where a hit counts as a page view, event, download, outlink, onsite search, or content tracking request. Tiers scale to 1,600 euros per month at 10 million hits, and annual billing gives two months free. Watch the pricing page's static HTML, which shows a stale 29-euro figure until JavaScript loads the tier table."
        }
      },
      {
        "@type": "Question",
        "name": "Is Matomo really GDPR compliant?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Matomo claims adherence to GDPR, HIPAA, CCPA, LGPD, and PECR, with IP anonymization, configurable data anonymization, an opt-out, first-party cookies by default, and tools to delete visitor data on request. It states that France's CNIL lists it among tools usable without consent and that Cloud data stays in Europe. Those are vendor claims, and your compliance still depends on configuration, particularly cookie consent and retention."
        }
      },
      {
        "@type": "Question",
        "name": "Matomo or Google Analytics 4?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The differences that matter are ownership and sampling. Matomo stores data in your own database or its EU-based Cloud, generates unsampled reports on every plan, and exports raw data on request. GA4 keeps data in Google's infrastructure and applies sampling, which is why European regulator rulings feature in Matomo's comparisons. GA4 still wins on cost at low traffic and on Google Ads integration."
        }
      },
      {
        "@type": "Question",
        "name": "Does Matomo have AI features?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, but they measure AI rather than behave like an AI analyst. Matomo 5.12.0 added reports for AI chatbot content requests and real-time chatbot traffic, an AIAgents plugin ships enabled on new instances, and a free official MCP Server plugin connects Matomo to ChatGPT, Claude, and other MCP clients, with write actions requiring approval. There is no AI anomaly detection or predictive analytics in the product today."
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
    "reviewBody": "The pick when analytics data residency is a requirement rather than a preference, with an open core and a real premium plugin business behind it. Budget both operations time for self-hosting and plugin fees for the headline behavioral features.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/matomo/#app",
      "name": "Matomo",
      "url": "https://martechsignal.com/tools/matomo/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 49,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
