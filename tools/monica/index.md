# Monica review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Self-host free under AGPL; hosted is a single $9/mo or $90/yr plan with a 30-day trial and no card required, fully published (the vendor pricing page, verified 2026-09-28). |
| Feature depth | 5/10 | Contact timelines, reminders, notes and relationship tracking are deep for personal use, but there is no deal pipeline or campaign machinery (vendor documentation). |
| Integrations | 3/10 | The catalog lists no named integrations; a public API exists for your own wiring (vendor documentation). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation). |
| Openness | 9/10 | AGPL self-hosting with 25.3k GitHub stars and the full feature set available free on your own server (the source repository). |
| Operational maturity | 6/10 | 25.3k stars and years of steady maintenance, but it runs as a small project without enterprise support machinery (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; AGPL-3.0 licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; API access for custom integrations |  |
| &#10003; Established community (25,261 GitHub stars) |  |

**What is Monica?**
Open-source personal CRM for tracking friends, family, and business relationships. It ships with 25,261 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Monica cost?**
Monica is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 25,261 stars. You pay in server time and maintenance, not licences.

**Is Monica a good self-hosted CRM tool in 2026?**
The reference implementation of the personal CRM category, honest about its limits, and mid-rewrite. Value it for follow-up discipline, not for pipeline or automation.

**Does Monica have AI features?**
No. The README states plainly that Monica does not have built-in AI with integrations like ChatGPT and is not a smart assistant: it only sends the reminders you asked for. AI-assisted workflows are something you build yourself against the API.

**Is Monica a CRM for sales?**
No, and the project says so directly. It is a personal relationship manager for friends, family, colleagues, and neighbours, with no pipelines, deals, or campaigns. Sales teams should look at the sales CRM entries in this directory instead.

**Is Monica still maintained in 2026?**
The application code is not, in practical terms: the last commit to the main branch was August 30, 2025, the latest stable release remains v4.1.2 from May 2024, and no release of any kind has been published in over a year. The organization is active on the rebuild, with a Helm chart pushed in September 2026 and blog posts about the new version through September 2026, and the hosted service continues to run. Self-hosters should treat the current code as stable but frozen and evaluate the promised v3, due before the end of 2026, before committing new data.

**Should you self-host Monica or pay for the hosted plan?**
The hosted plan is $9 per month or $90 per year with unlimited contacts, notes, reminders, activities, and journal entries, managed backups, automatic updates, data export, and email support, on a 30-day trial with no credit card. Self-hosting is free under AGPL and runs as a container, but you inherit the operator work the plan buys: updates, backups, monitoring, and a version question, since the official Docker Hub latest tag still serves the 4.x line while the current code is the 5.0 beta on ghcr. If the value of Monica is remembering things about people rather than infrastructure, the hosted plan is the rational default; self-host when the data must stay on your hardware.

**Can you export your data out of Monica, and can you migrate from hosted to self-hosted?**
Yes on both. Export covers contacts, relationships, notes, reminders, activities, custom fields, and other supported account data with attachments, and the pricing FAQ states it plainly as a right rather than a premium feature, so it works on every plan and costs nothing. The same page confirms you can export from hosted Monica and import into a compatible self-hosted installation. Contacts also support per-contact vCard download. Verify the import path against your self-hosted version before cancelling the hosted account, since the two code lines differ.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 25261
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Monica is a tool in CRM with free and open source. The catalog documents a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Ever Gauzy

Open business management platform: ERP, CRM, HRM, ATS, and time tracking

Frappe CRM

Fully featured, open source CRM

Relaticle

Open-source CRM with native AI agent support, 37 MCP tools, REST API, Laravel &amp; Filament

Warpdrive

Self-hosted open-source Pipedrive alternative for BD teams: pipelines and Gmail on your own box

HubSpot CRM

Free AI-powered CRM platform with sales, service, and marketing tools unified

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- Monica
## Monica review (2026): pricing, AI features, verdict

Open-source personal CRM for tracking friends, family, and business relationships

CRM · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Monica &#8594;](https://monicahq.com)

[How we review](/methodology/) · No affiliate links

[Visit Monica &#8594;](https://monicahq.com)

## MartechSignal Score: 34/60

Monica is a personal CRM done honestly: relationships, reminders and notes, priced at one flat plan. It is not a sales pipeline tool, and it does not pretend to be.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Monica is an open-source personal relationship manager, the project&#x27;s own term is PRM, built for documenting people rather than selling to them: contacts and relationships between contacts, notes, journal entries, activities, tasks, reminders with automatic birthdays, addresses, custom fields and sections, pets, gifts, calls, files, and life events, organized into vaults with multiple users and, per the README, 27 languages. The README is explicit about what it is not: not a social network and never will be, no ads or tracking, not a smart assistant, and no built-in AI with integrations like ChatGPT, and reminders only cover what you asked for. For marketing work the fit is narrow: founder-led and community-led businesses whose channel is relationships and a newsletter, not sales teams. Two facts should shape an adoption decision. The app codebase is dormant: the last commit to the main branch landed August 30, 2025, the newest stable release is v4.1.2 from May 2024, and no release of any kind has shipped in more than a year, while the organization around it is clearly active, with a Helm chart pushed in September 2026 and a blog publishing rebuild posts through the same month. That blog is where Monica v3 lives: a rebuild from scratch, still open source, promised before the end of 2026, API-first, with community templates and native iOS and Android apps to follow, and with naming that has not settled, since marketing says v3, repository tags say 5.0.0-beta, and the Docker examples call the beta Chandler. The hosted service is one plan, $90 a year or $9 a month, with unlimited contacts, data export, managed backups, email support, and no enterprise tier. This assessment is from the repository, the docs, and the hosted site.

Monica homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

Monica is free to self-host under the AGPL-3.0 licence.

Self-host free under AGPL. Hosted Monica is a single plan: $9/month or $90/year (two months free on annual billing, 30-day trial, no credit card) with unlimited contacts, managed backups, data export, and email support. No enterprise tier.

## How to install

- The docs&#x27; quickest route is the container registry image: docker run -p 8080:80 ghcr.io/monicahq/monica-next:main, which runs on SQLite and serves http://localhost:8080.
- Add MAIL_MAILER=log to that command, because registration needs a working mailer and the log driver satisfies it without an SMTP server.
- The official Docker Hub image (library/monica) still packages the previous major version, per the docs. For database, queue, and other production setups, the docs point to the examples directory of the monicahq/docker repository.
- The hosted pricing page is explicit about what self-hosting costs you in practice: updates, backups, monitoring, security patches, and support are what the $90 per year hosted plan buys, so budget the operator time honestly.
- Production setups follow the examples in the monicahq/docker repository: full_v5 runs the v5 beta as fpm-alpine behind nginx with redis and separate cron and queue containers, and the supervisor variant pairs a MariaDB 11 container with one app container running supervisord for web, cron, and queue. Official-image setup runs docker-compose exec app php artisan setup:production.
- A Helm chart is maintained at monicahq/helm and was pushed in September 2026; it pins ghcr.io/monicahq/monica-next at tag main with appVersion 5.0.0, which makes it the most current packaged route and also the most bleeding-edge.
- Background queues need a worker in non-trivial installs: the docs&#x27; local development list includes php artisan queue:listen --queue=high,low,default.
## Requirements

A Laravel/PHP application distributed as a container. The quick-start image runs on SQLite with a mailer configured; production deployments follow the examples in monicahq/docker for database and queue setup. The 4.x branch is the stable line and main is the beta for the next major version.

## Best for

Individuals and founder- or community-led businesses that live on personal relationships and want a private, self-hostable record of people, conversations, gifts, and reminders. The project also notes positive reviews from users with Asperger syndrome and Alzheimer&#x27;s disease.

## Not for

Sales and marketing teams. There are no pipelines, deals, forecasts, or campaigns, and the README is categorical that Monica will never guess, recommend, or rank anything for you.

## Review notes

Assessed from the repository, the GitBook documentation, and the hosted site rather than a self-hosted instance. The docs publish an llms.txt and a Markdown version of every page, which makes them easy to work with programmatically.

The README&#x27;s &#x27;What Monica isn&#x27;t&#x27; section does the disqualifying work for you: no social features by design, no ads, no tracking, no smart assistant, and no built-in AI. Reminders are strictly the emails you asked for. Treat any AI claim about Monica as something someone built on top of the API, not a product feature.

Version state is the operational risk, and the naming has not settled. The main branch is the beta for the next version, tagged v5.0.0-beta.5 in April 2025; the 4.x branch is the stable line with its last tagged release at v4.1.2 in May 2024; the official Docker Hub image still serves 4.x as latest, though 5.0.0-beta tags exist there now; and the hosted site promotes the rebuild, branded Monica v3, as coming before the end of 2026. The Docker examples call the same beta v5, a.k.a. Chandler. Pin a release deliberately and plan the migration, because the lines are far apart.

The activity picture needs a correction to our earlier read: the last commit to the main branch is August 30, 2025, not April 2026, and the releases page shows nothing of any kind in more than a year, with the newest tag being the v5.0.0-beta.5 pre-release from April 2025. The organization is not idle: the Helm chart, marketing site repo, and a Laravel database tool all show 2026 pushes, and the blog published four posts between August 6 and September 2, 2026. The honest summary is a dormant application with an active rebuild behind it.

Feature facts verified from the repository and docs: two-factor authentication with TOTP, recovery codes, and WebAuthn or FIDO security keys; vCard download per contact; vaults that are private by design, so even an account administrator cannot open a vault they are not a member of; multiple users per account with administrator and regular permissions; custom activity types; and notification channels limited to email and Telegram. The README claims 27 translations while the lang directory holds 29 locales, so the number varies by source.

The API differs sharply between the stable and beta lines. The 4.x branch carries a real REST API with 67 route registrations behind Passport token auth, which the hosted marketing copy leans on for import and export. The beta on main exposes only user and vault endpoints behind Sanctum, with Scribe generating per-instance documentation at /docs, /docs.postman, and /docs.openapi. There is no public API documentation site, so API work on the beta means running an instance to read its generated docs.

Export and migration are a stated right rather than a paywall: the pricing FAQ says you can export contacts, relationships, notes, reminders, activities, custom fields, and other account data with attachments included, and import into a compatible self-hosted installation. Backup guidance stays thin on the self-host side; the 4.x upgrade doc says to back up and verify a backup without documenting the commands.

## Verdict

The reference implementation of the personal CRM category, honest about its limits, and mid-rewrite. Value it for follow-up discipline, not for pipeline or automation.

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

Open-source personal CRM for tracking friends, family, and business relationships. It ships with 25,261 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Monica is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 25,261 stars. You pay in server time and maintenance, not licences.

The reference implementation of the personal CRM category, honest about its limits, and mid-rewrite. Value it for follow-up discipline, not for pipeline or automation.

No. The README states plainly that Monica does not have built-in AI with integrations like ChatGPT and is not a smart assistant: it only sends the reminders you asked for. AI-assisted workflows are something you build yourself against the API.

No, and the project says so directly. It is a personal relationship manager for friends, family, colleagues, and neighbours, with no pipelines, deals, or campaigns. Sales teams should look at the sales CRM entries in this directory instead.

The application code is not, in practical terms: the last commit to the main branch was August 30, 2025, the latest stable release remains v4.1.2 from May 2024, and no release of any kind has been published in over a year. The organization is active on the rebuild, with a Helm chart pushed in September 2026 and blog posts about the new version through September 2026, and the hosted service continues to run. Self-hosters should treat the current code as stable but frozen and evaluate the promised v3, due before the end of 2026, before committing new data.

The hosted plan is $9 per month or $90 per year with unlimited contacts, notes, reminders, activities, and journal entries, managed backups, automatic updates, data export, and email support, on a 30-day trial with no credit card. Self-hosting is free under AGPL and runs as a container, but you inherit the operator work the plan buys: updates, backups, monitoring, and a version question, since the official Docker Hub latest tag still serves the 4.x line while the current code is the 5.0 beta on ghcr. If the value of Monica is remembering things about people rather than infrastructure, the hosted plan is the rational default; self-host when the data must stay on your hardware.

Yes on both. Export covers contacts, relationships, notes, reminders, activities, custom fields, and other supported account data with attachments, and the pricing FAQ states it plainly as a right rather than a premium feature, so it works on every plan and costs nothing. The same page confirms you can export from hosted Monica and import into a compatible self-hosted installation. Contacts also support per-contact vCard download. Verify the import path against your self-hosted version before cancelling the hosted account, since the two code lines differ.

## Similar Tools

## Related reading

- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
### Quick Facts

Related guides: [Open Source Crm](/best/open-source-crm) · [Ai Crm Tools](/best/ai-crm-tools)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/monica/#app",
    "name": "Monica",
    "description": "Open-source personal CRM for tracking friends, family, and business relationships",
    "image": "https://martechsignal.com/og/tools/monica.png",
    "url": "https://martechsignal.com/tools/monica/",
    "sameAs": [
      "https://monicahq.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/monica/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-08-21",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://monicahq.com",
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
        "name": "Monica",
        "item": "https://martechsignal.com/tools/monica/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Monica?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source personal CRM for tracking friends, family, and business relationships. It ships with 25,261 GitHub stars, an API for custom integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Monica cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Monica is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 25,261 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Monica a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The reference implementation of the personal CRM category, honest about its limits, and mid-rewrite. Value it for follow-up discipline, not for pipeline or automation."
        }
      },
      {
        "@type": "Question",
        "name": "Does Monica have AI features?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. The README states plainly that Monica does not have built-in AI with integrations like ChatGPT and is not a smart assistant: it only sends the reminders you asked for. AI-assisted workflows are something you build yourself against the API."
        }
      },
      {
        "@type": "Question",
        "name": "Is Monica a CRM for sales?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No, and the project says so directly. It is a personal relationship manager for friends, family, colleagues, and neighbours, with no pipelines, deals, or campaigns. Sales teams should look at the sales CRM entries in this directory instead."
        }
      },
      {
        "@type": "Question",
        "name": "Is Monica still maintained in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The application code is not, in practical terms: the last commit to the main branch was August 30, 2025, the latest stable release remains v4.1.2 from May 2024, and no release of any kind has been published in over a year. The organization is active on the rebuild, with a Helm chart pushed in September 2026 and blog posts about the new version through September 2026, and the hosted service continues to run. Self-hosters should treat the current code as stable but frozen and evaluate the promised v3, due before the end of 2026, before committing new data."
        }
      },
      {
        "@type": "Question",
        "name": "Should you self-host Monica or pay for the hosted plan?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The hosted plan is $9 per month or $90 per year with unlimited contacts, notes, reminders, activities, and journal entries, managed backups, automatic updates, data export, and email support, on a 30-day trial with no credit card. Self-hosting is free under AGPL and runs as a container, but you inherit the operator work the plan buys: updates, backups, monitoring, and a version question, since the official Docker Hub latest tag still serves the 4.x line while the current code is the 5.0 beta on ghcr. If the value of Monica is remembering things about people rather than infrastructure, the hosted plan is the rational default; self-host when the data must stay on your hardware."
        }
      },
      {
        "@type": "Question",
        "name": "Can you export your data out of Monica, and can you migrate from hosted to self-hosted?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes on both. Export covers contacts, relationships, notes, reminders, activities, custom fields, and other supported account data with attachments, and the pricing FAQ states it plainly as a right rather than a premium feature, so it works on every plan and costs nothing. The same page confirms you can export from hosted Monica and import into a compatible self-hosted installation. Contacts also support per-contact vCard download. Verify the import path against your self-hosted version before cancelling the hosted account, since the two code lines differ."
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
    "reviewBody": "Monica is a personal CRM done honestly: relationships, reminders and notes, priced at one flat plan. It is not a sales pipeline tool, and it does not pretend to be.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/monica/#app",
      "name": "Monica",
      "url": "https://martechsignal.com/tools/monica/"
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
