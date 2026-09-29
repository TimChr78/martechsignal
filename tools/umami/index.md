# Umami review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 10/10 | umami.is/pricing documents every self-serve tier with limits: Hobby free to 100,000 events per month, Pro at 20 USD for 1 million events, Business at 200 USD for 10 million, per-event overage terms, plus free self-hosting under MIT (the vendor pricing page: [pricing page](https://umami.is/pricing), verified 2026-09-26). |
| Feature depth | 7/10 | Core analytics plus session replay (v3.1), heatmaps (v3.2), funnels, retention, revenue, journey, attribution and UTM reports cover the analytics baseline with cookieless tracking as the differentiator, though it stays lighter than Matomo on configuration (vendor documentation: [vendor site](https://umami.is), verified 2026-09-26). |
| Integrations | 5/10 | An API plus community plugins for ten platforms and API clients for Laravel, Python and Go make up the catalog, with no native marketing integrations documented (vendor documentation: [vendor site](https://umami.is), verified 2026-09-26). |
| AI capability | 0/10 | A search of the full documentation set, the README and every release from v3.0.3 to v3.3.1 found no AI feature of any kind, and the directory removed earlier AI claims as incorrect (vendor documentation: [vendor site](https://umami.is), verified 2026-09-26). |
| Openness | 10/10 | MIT-licensed and self-hostable via a two-service Docker compose file, with data retained indefinitely and full ownership of the database (the source repository: [repository](https://github.com/umami-software/umami), verified 2026-09-26). |
| Operational maturity | 8/10 | Created in 2020 with a steady v3.x release cadence through v3.3.1 on August 20, 2026 (vendor documentation: [vendor site](https://umami.is), verified 2026-09-26). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Paid plans start at $20/mo once past the free tier |
| ✓ Active public repository (39,072 GitHub stars counted at last check) |  |
| ✓ Native integrations include WordPress (community plugin), Next.js, Vercel (5 listed) |  |

**What is Umami?**
Umami: Open-source, cookieless web analytics with real-time dashboards, session replay, and heatmaps. The public repository carries 39,072 stars. Umami offers a public API for custom integrations.

**How much does Umami cost?**
Umami has a free tier; paid plans start at $20/mo. Self-hosted free (MIT). Cloud: Hobby free to 100K events/mo; Pro $20/mo for 1M events; Business $200/mo for 10M events; Enterprise custom. 14-day trial. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."

**Is Umami a good self-hosted Analytics & Attribution tool in 2026?**
Light, honest, cookieless analytics you can own outright; the AI-free tracking script is the point, not a gap. Self-host for unlimited sites, or pay $20 a month for 1 million cloud events.

**How do I stop ad blockers from blocking Umami?**
The docs describe three methods: reverse-proxy the tracking script at the server level (Nginx, Apache, or an Express endpoint serving it), self-host the tracker file and point the snippet at it with data-host-url, or on self-hosted installs rename the tracker with TRACKER_SCRIPT_NAME and the collection endpoint with COLLECT_API_ENDPOINT. The docs concede the point plainly: even though Umami is privacy-focused, it may still get blocked by certain ad blockers.

**Does Umami track UTM campaign parameters?**
Yes, natively since v2.11.0. All five standard parameters (utm_source, utm_medium, utm_campaign, utm_term, utm_content) are collected automatically with no extra configuration, and there is a dedicated UTM report. The v2.18.0 attribution report builds on that with first-click and last-click models across referrers, paid ads, and UTM parameters, so campaign credit can be viewed under either model.

**What happened to MySQL support in Umami v3?**
It was removed. The v3 upgrade guide announces that Umami is standardizing on PostgreSQL, and the FAQ states PostgreSQL 12.14 or newer is the only supported database. Existing MySQL users migrate by upgrading to v2.19.0 first, exporting with mysqldump or CSV, and importing with a tool such as pgloader or pg_chameleon; the docs walk the full path. MariaDB, which v2 tolerated as a MySQL variant, goes with it.

- **Pricing:** Open Source
- **Category:** [Analytics & Attribution](/categories/analytics/)
- **GitHub:** ★ 39072
- **Founded:** 2020
- **API:** Yes
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-07

**Verdict:** Umami is a tool in Analytics & Attribution with free and open source. The catalog documents 5 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

PostHog

Open-source product analytics platform with session replay, feature flags, experiments, and surveys

Heap

AI-powered product analytics with autocapture and digital experience insights

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

Amplitude

AI-powered digital analytics platform for product and marketing teams

[More Analytics & Attribution Tools →](/categories/analytics/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Analytics & Attribution](/categories/analytics/)
- Umami
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Umami review (2026): pricing, AI features, verdict

Open-source, cookieless web analytics with real-time dashboards, session replay, and heatmaps

Analytics & Attribution · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit Umami →](https://umami.is)

[How we review](/methodology/) · No affiliate links

[Visit Umami →](https://umami.is)

## MartechSignal Score: 40/60

Light, cookieless analytics with fully public pricing and an MIT license, where the absence of AI is a deliberate design point rather than a gap. Session replay, heatmaps and the streaming API live on paid Cloud tiers, and the integration surface is small.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Umami is an open-source, cookieless web analytics platform you can self-host under the MIT license or run on the vendor's cloud, created in 2020 by Mike Cao and now at v3 with roughly 39,072 GitHub stars. It tracks pageviews, sessions, referrers, countries, devices, UTM parameters, and custom events without cookies and without collecting personal data, which is why sites use it to drop consent banners entirely. The v3 line has grown well past simple dashboards: session replay (v3.1, rrweb-based, off by default, replays kept 30 days), click and scroll heatmaps (v3.2), an attribution report with first-click and last-click models, funnels, retention, revenue, journey, and UTM reports, custom Boards dashboards, and TOTP two-factor auth, plus short links and tracking pixels on the cloud platform. Deployment is a Node.js app (18.18+) on PostgreSQL (12.14 minimum); v3 removed MySQL and MariaDB, and the docs publish a migration path through v2.19 for anyone still on MySQL. Install is docker compose up -d with a two-service file (app plus postgres:15-alpine) or pnpm install and pnpm run build from source; the build creates an admin/umami login you replace on first sign-in. Self-hosted instances keep an admin-only API, retain data indefinitely, and can turn off the app's anonymous telemetry with one environment variable. Cloud pricing is usage-based per event rather than per seat: Hobby is free to 100,000 events a month, Pro is $20 for 1 million, Business is $200 for 10 million with session replay, heatmaps, and the streaming API included, and Enterprise is custom. Self-hosted installs get the core analytics but not email reports or the streaming API. Compared with Google Analytics, Umami trades ad-ecosystem integrations and behavioral depth for a script the vendor puts under 2KB, no sampling, and full data ownership; compared with Matomo, it is lighter and less configurable. Best for developers and privacy-conscious marketing teams that want campaign and conversion numbers without surveillance overhead.

Umami homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Key Integrations

- WordPress (community plugin)
- Next.js
- Vercel
- Node.js (@umami/node)
- Community API clients (Laravel, Python, Go)
## Pricing

Umami is free to self-host under the MIT licence, paid plans start at $20/mo as of 2026-09.

Self-hosted free (MIT). Cloud: Hobby free to 100K events/mo; Pro $20/mo for 1M events; Business $200/mo for 10M events; Enterprise custom. 14-day trial.

Current plans and limits live on the [Umami pricing page](https://umami.is/pricing).

## How to install

- Docker path: docker pull docker.umami.is/umami-software/umami:latest, or clone the repo and run docker compose up -d with the shipped file, which starts the app on port 3000 plus postgres:15-alpine, each with a health check and a persistent umami-db-data volume.
- Source path: git clone https://github.com/umami-software/umami.git && cd umami && pnpm install, set DATABASE_URL (postgresql://username:mypassword@localhost:5432/mydb, the only required variable), then pnpm run build and pnpm run start. Node.js 18.18+ and PostgreSQL 12.14+ are required.
- The build creates a default admin/umami login; change it on first sign-in. Two-factor auth needs TWO_FACTOR_ENCRYPTION_KEY set (generate with openssl rand -hex 32), required since v3.3.
- Updates: git pull && pnpm install && pnpm build from source, or docker compose pull && docker compose up --force-recreate -d for Docker deployments.
- Get data flowing: add the tracking script to your site (Next.js via the next/script component; a WordPress community plugin exists), then watch events land in the dashboard. Server-side events post to /api/send or /api/batch as JSON and require a valid User-Agent header; requests without one are rejected.
## Requirements

Node.js 18.18+ and PostgreSQL 12.14+; v3 dropped MySQL and MariaDB, and the docs document a v2.19 stepping-stone migration for anyone moving off MySQL. DATABASE_URL is the only required variable; APP_SECRET, TRACKER_SCRIPT_NAME (renames script.js), COLLECT_API_ENDPOINT (renames /api/send), IGNORE_IP, and DISABLE_TELEMETRY=1 cover most configuration. Self-hosted data is retained indefinitely unless you delete it. The docs list three ways around ad blockers: reverse-proxy the script, self-host the tracker file with data-host-url, or rename the tracker and collect endpoint.

## Best for

Developers and privacy-conscious marketing teams that want campaign and conversion reporting without cookies or consent banners: UTM and attribution reports, funnels, retention, revenue, and shareable dashboards, with unlimited websites when self-hosted and an API-first design for custom pipelines.

## Not for

Buyers who want zero infrastructure: self-hosters are responsible for the security of their own deployment, and session replay, heatmaps, email reports, and the streaming API sit behind paid Cloud tiers (Business and up for replay and heatmaps). Also not for teams that need certified compliance attestations, since the security page states Umami claims no certifications it has not completed, and not for MySQL shops, which v3 no longer supports.

## Review notes

Assessed from umami.is, docs.umami.is (about 120 pages, fetched through its published llms.txt), the GitHub repo, and the release log in September 2026; we have not deployed an instance. The docs cover v3 only, with v2 split off at v2.umami.is, and the release cadence is healthy: v3.3.1 (August 20, 2026), v3.3.0 (August 12), v3.2.0 (June 24), v3.1.0 (April 16), with a push to master the day before we checked.

The correction that matters: our earlier record listed AI-powered insights, AI anomaly detection, and AI event tracking. None exist. A search across the full documentation set, the README, and every release from v3.0.3 to v3.3.1 finds no AI feature of any kind; Insights in Umami is a menu of deterministic reports (compare, breakdown, funnel, retention, UTM, goals, journey, revenue, attribution). We have removed the AI claims.

Second correction: our cloud pricing was wrong. Hobby is free to 100,000 events a month, not $20; Pro is $20 for 1 million events; Business is $200 for 10 million; Enterprise is custom, with overage billed per event and no interruption to collection. The old claim that Umami lacks session recordings and heatmaps is also out of date: replay shipped in v3.1 and heatmaps in v3.2, both off by default and both Cloud Business tier and above on the hosted side.

Two more stale facts: v3 removed MySQL and MariaDB in favor of PostgreSQL-only, and the integration list was padded. Zapier, Slack, and Google Search Console appear nowhere in the docs; WordPress is a community plugin, Next.js and Vercel are documented guides rather than integrations, and the official integrations page lists community plugins for ten platforms plus API clients.

## Verdict

Light, honest, cookieless analytics you can own outright; the AI-free tracking script is the point, not a gap. Self-host for unlimited sites, or pay $20 a month for 1 million cloud events.

## Pros and cons

## Related concepts

- [Attribution models](/glossary/marketing-attribution-models/)
- [First-party data](/glossary/first-party-data/)
- [DMP](/glossary/dmp/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Umami: Open-source, cookieless web analytics with real-time dashboards, session replay, and heatmaps. The public repository carries 39,072 stars. Umami offers a public API for custom integrations.

Umami has a free tier; paid plans start at $20/mo. Self-hosted free (MIT). Cloud: Hobby free to 100K events/mo; Pro $20/mo for 1M events; Business $200/mo for 10M events; Enterprise custom. 14-day trial. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."

Light, honest, cookieless analytics you can own outright; the AI-free tracking script is the point, not a gap. Self-host for unlimited sites, or pay $20 a month for 1 million cloud events.

The docs describe three methods: reverse-proxy the tracking script at the server level (Nginx, Apache, or an Express endpoint serving it), self-host the tracker file and point the snippet at it with data-host-url, or on self-hosted installs rename the tracker with TRACKER_SCRIPT_NAME and the collection endpoint with COLLECT_API_ENDPOINT. The docs concede the point plainly: even though Umami is privacy-focused, it may still get blocked by certain ad blockers.

Yes, natively since v2.11.0. All five standard parameters (utm_source, utm_medium, utm_campaign, utm_term, utm_content) are collected automatically with no extra configuration, and there is a dedicated UTM report. The v2.18.0 attribution report builds on that with first-click and last-click models across referrers, paid ads, and UTM parameters, so campaign credit can be viewed under either model.

It was removed. The v3 upgrade guide announces that Umami is standardizing on PostgreSQL, and the FAQ states PostgreSQL 12.14 or newer is the only supported database. Existing MySQL users migrate by upgrading to v2.19.0 first, exporting with mysqldump or CSV, and importing with a tool such as pgloader or pg_chameleon; the docs walk the full path. MariaDB, which v2 tolerated as a MySQL variant, goes with it.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Multi-Touch Attribution Was Always a Fiction](/blog/multi-touch-attribution-was-always-a-fiction/)
- [What a free SEO audit replaces in your Semrush stack, and what it does not](/blog/what-free-seo-audit-replaces/)
## Also featured in

- [Best Marketing Analytics & Attribution tools (2026): 8 compared](/best/marketing-analytics-tools/) — Best for analytics & attribution teams that want the job covered in one platform and can host it themselves, with a free starting tier.
### Quick Facts

Related guides: [Umami in Matomo alternatives](/alternatives/matomo/) · [Marketing Analytics Tools](/best/marketing-analytics-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/umami/#app",
    "name": "Umami",
    "description": "Open-source, cookieless web analytics with real-time dashboards, session replay, and heatmaps",
    "image": "https://martechsignal.com/og/tools/umami.png",
    "url": "https://martechsignal.com/tools/umami/",
    "sameAs": [
      "https://umami.is"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/umami/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-07-27",
    "offers": [
      {
        "@type": "Offer",
        "price": 0,
        "priceCurrency": "USD",
        "url": "https://umami.is/pricing",
        "priceValidUntil": "2026-12-31"
      },
      {
        "@type": "Offer",
        "price": 20,
        "priceCurrency": "USD",
        "url": "https://umami.is/pricing",
        "priceValidUntil": "2026-12-31"
      }
    ]
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
        "name": "Umami",
        "item": "https://martechsignal.com/tools/umami/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Umami?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Umami: Open-source, cookieless web analytics with real-time dashboards, session replay, and heatmaps. The public repository carries 39,072 stars. Umami offers a public API for custom integrations."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Umami cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Umami has a free tier; paid plans start at $20/mo. Self-hosted free (MIT). Cloud: Hobby free to 100K events/mo; Pro $20/mo for 1M events; Business $200/mo for 10M events; Enterprise custom. 14-day trial. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.\""
        }
      },
      {
        "@type": "Question",
        "name": "Is Umami a good self-hosted Analytics & Attribution tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Light, honest, cookieless analytics you can own outright; the AI-free tracking script is the point, not a gap. Self-host for unlimited sites, or pay $20 a month for 1 million cloud events."
        }
      },
      {
        "@type": "Question",
        "name": "How do I stop ad blockers from blocking Umami?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The docs describe three methods: reverse-proxy the tracking script at the server level (Nginx, Apache, or an Express endpoint serving it), self-host the tracker file and point the snippet at it with data-host-url, or on self-hosted installs rename the tracker with TRACKER_SCRIPT_NAME and the collection endpoint with COLLECT_API_ENDPOINT. The docs concede the point plainly: even though Umami is privacy-focused, it may still get blocked by certain ad blockers."
        }
      },
      {
        "@type": "Question",
        "name": "Does Umami track UTM campaign parameters?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, natively since v2.11.0. All five standard parameters (utm_source, utm_medium, utm_campaign, utm_term, utm_content) are collected automatically with no extra configuration, and there is a dedicated UTM report. The v2.18.0 attribution report builds on that with first-click and last-click models across referrers, paid ads, and UTM parameters, so campaign credit can be viewed under either model."
        }
      },
      {
        "@type": "Question",
        "name": "What happened to MySQL support in Umami v3?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It was removed. The v3 upgrade guide announces that Umami is standardizing on PostgreSQL, and the FAQ states PostgreSQL 12.14 or newer is the only supported database. Existing MySQL users migrate by upgrading to v2.19.0 first, exporting with mysqldump or CSV, and importing with a tool such as pgloader or pg_chameleon; the docs walk the full path. MariaDB, which v2 tolerated as a MySQL variant, goes with it."
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
    "reviewBody": "Light, cookieless analytics with fully public pricing and an MIT license, where the absence of AI is a deliberate design point rather than a gap. Session replay, heatmaps and the streaming API live on paid Cloud tiers, and the integration surface is small.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/umami/#app",
      "name": "Umami",
      "url": "https://martechsignal.com/tools/umami/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 40,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
