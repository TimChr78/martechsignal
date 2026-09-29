# Seonaut review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Self-hosted free (MIT); cloud Lite free for 1 project/500 URLs, Growth $9/mo for 5 projects/10K URLs published (the vendor pricing page: [pricing page](https://seonaut.org/), verified 2026-09-07). |
| Feature depth | 4/10 | Technical SEO crawling with recurring audits cover the audit job (vendor documentation: [vendor site](https://seonaut.org), verified 2026-09-28). |
| Integrations | 2/10 | No named integrations in the catalog and no API (vendor documentation: [vendor site](https://seonaut.org), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://seonaut.org), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 782 GitHub stars in readable Go (the source repository: [repository](https://github.com/StJudeWasHere/seonaut), verified 2026-09-28). |
| Operational maturity | 4/10 | Founded 2022 at 782 stars with priced cloud tiers above the free plan (vendor documentation: [vendor site](https://seonaut.org), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Paid plans start at $9/mo once past the free tier |
| ✓ Actively developed - latest release No tagged releases; ships as the :latest container image |  |

**What is Seonaut?**
Seonaut: Open-source SEO crawler in Go for technical audits, self-hosted or cloud. The public repository carries 782 stars.

**How much does Seonaut cost?**
Seonaut has a free tier; paid plans start at $9/mo. MIT-licensed self-hosted free; cloud Lite free for 1 project and 500 URLs per project, Growth $9/mo for 5 projects and 10,000 URLs with recurring audits. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

**Is Seonaut a good self-hosted SEO & Search tool in 2026?**
A lean, honest, self-hosted technical crawler with 79 documented issue checks; no JS rendering, no API, and a slow-but-alive commit pace.

**Does SEOnaut render JavaScript?**
No. The codebase has no headless browser dependency, and JavaScript rendering appears nowhere in the feature list; the crawler fetches HTML directly. Sites built as client-rendered single-page apps will show empty content, missing links, and phantom issues, because the crawler sees what curl sees. Server-rendered sites, static sites, and sites using pre-rendering audit fine. If your audit targets a React or Vue application without SSR, you need a JS-rendering crawler, and this is not one.

**Is SEOnaut free, and what do the cloud plans cost?**
The self-hosted Community edition is MIT-licensed and free, including commercial use per the support page. The hosted service at app.seonaut.org has two tiers: Lite is free with one project and up to 500 URLs per project, and Growth is $9 per month for five projects, 10,000 URLs per project, and recurring audits, billed through Stripe with one month free on annual plans. The practical difference beyond limits is scheduling: recurring audits are a Growth feature, while self-hosted users set up their own cron-triggered crawls.

**Does SEOnaut compare to Screaming Frog?**
On core technical auditing, more than you might expect: broken links, redirect chains and loops, missing and duplicate metas, heading structure, hreflang, canonical tags, alt text, orphan and dead-end pages, and response-time checks, with 79 issue types in code and ECharts dashboards. The gaps are the commercial tool's strengths: no JavaScript rendering, no API, no team features, no integrated keyword or log-file analysis, and no tagged releases. The project itself makes no comparison claims; it positions as created by SEOs for everyone rather than as a Screaming Frog competitor. For a no-cost, self-hosted crawl of server-rendered sites, it covers the technical layer; for client-facing audits of JS-heavy sites, a rendering crawler remains the safer choice.

- **Pricing:** Open Source
- **Category:** [SEO & Search](/categories/seo/)
- **GitHub:** ★ 782
- **Founded:** 2022
- **HQ:** Open source
- **API:** No
- **Last verified:** 2026-09-07

**Verdict:** Seonaut is a tool in SEO & Search with free and open source. The catalog documents a self-hosting path. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

OpenSEO

Open source alternative to Ahrefs and Semrush

Scrunch

The AI Customer Experience Platform: monitor, optimize and serve your site to AI agents

React Email Editor

Drag-n-Drop Email Editor Component for React.js

Salesforce Marketing Cloud

Enterprise marketing automation on Salesforce with Agentforce AI across email, SMS, and web

MarketMuse

AI-powered content strategy and optimization platform for SEO content teams

[More SEO & Search Tools →](/categories/seo/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [SEO & Search](/categories/seo/)
- Seonaut
Re-check pending: pricing last verified 2026-09-07 (22 days ago).

## Seonaut review (2026): pricing, AI features, verdict

Open-source SEO crawler in Go for technical audits, self-hosted or cloud

SEO & Search · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-26

[Visit Seonaut →](https://seonaut.org)

[How we review](/methodology/) · No affiliate links

[Visit Seonaut →](https://seonaut.org)

## MartechSignal Score: 30/60

Seonaut is a Go crawler for technical SEO audits with a real free cloud tier: one project, 500 URLs. MIT-licensed at 782 stars; small, legible and honest about scope.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

SEOnaut is an MIT-licensed SEO crawler written in Go, self-hosted with Docker and MySQL, and also offered as a hosted service with a free Lite tier (one project, 500 URLs per project) and a $9-per-month Growth plan (five projects, 10,000 URLs, recurring audits), billed through Stripe with one month free on annual plans; the site claims more than 3,000 professionals use it. The code defines 79 issue types across page-level and site-wide checks: broken links and redirects including loops, missing or duplicate meta tags, heading order, hreflang problems, image and alt-text audits for accessibility, content quality, canonical tags, orphan and dead-end pages, HTTPS checks, and TTFB and timeout detection. Documented crawl options include bypassing robots.txt, following nofollow links, crawling from sitemaps or subdomains, checking external links, basic-auth crawls, and WACZ archive creation. Results land in Apache ECharts dashboards with CSV, sitemap, and WACZ exports, and the crawler identifies itself as SEOnautBot/1.0. The honest limits shape who should adopt it: there is no JavaScript rendering, since no headless browser exists in the codebase, so client-rendered pages will audit badly; there is no API, because all routes are session-based web UI; there is no team or role model, with single-user projects in the schema; and no AI features appear anywhere in the product or its site. Maintenance is active but unhurried: 900-plus commits since 2022, the most recent in May 2026, and no tagged releases, so installs track the :latest container image. Source builds need Go 1.25 and the compose file runs MySQL 8.4, serving plain HTTP on port 9000 with signup rather than a default account. Against Screaming Frog the trade is direct: no license cost and repeatable self-hosted audits, in exchange for JS rendering and a commercial feature set.

Seonaut homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## Pricing

Seonaut is free to self-host under the MIT licence, paid plans start at $9/mo as of 2026-09.

MIT-licensed self-hosted free; cloud Lite free for 1 project and 500 URLs per project, Growth $9/mo for 5 projects and 10,000 URLs with recurring audits

Current plans and limits live on the [Seonaut pricing page](https://seonaut.org/).

## How to install

- Docker path from the README: git clone https://github.com/stjudewashere/seonaut.git, cd seonaut, then docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build, and open http://localhost:9000.
- Image-only install: docker pull ghcr.io/stjudewashere/seonaut:latest. From source without Docker: make run per docs/INSTALL.md.
- There is no default account: you register through the /signup route on first run. The compose database credentials (MYSQL_ROOT_PASSWORD=root, database, user, and password all seonaut) are sample values to change before exposing anything.
- Configuration lives in a config file at the repo root, overridable with SEONAUT_* environment variables; the crawler user agent is Mozilla/5.0 (compatible; SEOnautBot/1.0; +https://seonaut.org/bot), so exclude it with robots.txt if you audit sites you do not own.
- The app serves plain HTTP on port 9000; the install docs describe fronting it with Nginx or Apache plus certbot for HTTPS.
## Requirements

Docker and Git for the container path; Go 1.25 and Make to build from source, with MySQL 8.4 as the database in the compose file. A hosted option at app.seonaut.org removes the infrastructure work entirely.

## Best for

Developers and consultants who want a repeatable, self-hosted technical crawler with no per-crawl or license cost, and whose target sites are server-rendered: agencies auditing client HTML, and site owners tracking broken links, redirects, metas, hreflang, and alt text on a schedule they control.

## Not for

Auditing JavaScript-rendered applications (no headless browser in the codebase), teams wanting shared projects or roles (the schema is single-user), and anyone needing programmatic access (there is no API; exports are CSV, sitemap, and WACZ files from the UI).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from the GitHub repository (including the issue-reporter source and route table), seonaut.org, and docs/INSTALL.md. Not a hands-on review. The code defines 79 issue types registered as 57 page-level and 15 site-wide reporters, which is the concrete answer to how much audit coverage the project ships.

Two corrections against our earlier record: the tool has no API (we previously marked api_available true, but every route is session-cookie web UI with no /api endpoints), and the widely repeated claim of 150-plus issue types does not appear in any primary source; the count in code is 79. We also listed integrations that do not exist; the only exports are CSV, sitemap, and WACZ.

Maintenance cadence is the honest risk flag: 534 commits in 2022, then roughly 110 to 130 per year, 33 in the trailing twelve months, and the most recent commit in May 2026. There are no tagged releases, so pinning is not part of the project's model and upgrades mean pulling the latest image. MIT licensing and commercial use are explicitly permitted per the support page.

The hosted tiers change the evaluation: Lite is free with one project and 500 URLs per project, Growth is $9 per month with five projects, 10,000 URLs, and recurring audits, which is the only place scheduled crawling is documented. Self-hosted, you bring your own scheduler via cron.

## Verdict

A lean, honest, self-hosted technical crawler with 79 documented issue checks; no JS rendering, no API, and a slow-but-alive commit pace.

## Pros and cons

## Related concepts

- [SEO](/glossary/seo/)
- [AEO](/glossary/aeo/)
- [AI Visibility](/glossary/ai-search-visibility/)
- [UTM parameters](/glossary/utm-parameters/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Seonaut: Open-source SEO crawler in Go for technical audits, self-hosted or cloud. The public repository carries 782 stars.

Seonaut has a free tier; paid plans start at $9/mo. MIT-licensed self-hosted free; cloud Lite free for 1 project and 500 URLs per project, Growth $9/mo for 5 projects and 10,000 URLs with recurring audits. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers.

A lean, honest, self-hosted technical crawler with 79 documented issue checks; no JS rendering, no API, and a slow-but-alive commit pace.

No. The codebase has no headless browser dependency, and JavaScript rendering appears nowhere in the feature list; the crawler fetches HTML directly. Sites built as client-rendered single-page apps will show empty content, missing links, and phantom issues, because the crawler sees what curl sees. Server-rendered sites, static sites, and sites using pre-rendering audit fine. If your audit targets a React or Vue application without SSR, you need a JS-rendering crawler, and this is not one.

The self-hosted Community edition is MIT-licensed and free, including commercial use per the support page. The hosted service at app.seonaut.org has two tiers: Lite is free with one project and up to 500 URLs per project, and Growth is $9 per month for five projects, 10,000 URLs per project, and recurring audits, billed through Stripe with one month free on annual plans. The practical difference beyond limits is scheduling: recurring audits are a Growth feature, while self-hosted users set up their own cron-triggered crawls.

On core technical auditing, more than you might expect: broken links, redirect chains and loops, missing and duplicate metas, heading structure, hreflang, canonical tags, alt text, orphan and dead-end pages, and response-time checks, with 79 issue types in code and ECharts dashboards. The gaps are the commercial tool's strengths: no JavaScript rendering, no API, no team features, no integrated keyword or log-file analysis, and no tagged releases. The project itself makes no comparison claims; it positions as created by SEOs for everyone rather than as a Screaming Frog competitor. For a no-cost, self-hosted crawl of server-rendered sites, it covers the technical layer; for client-facing audits of JS-heavy sites, a rendering crawler remains the safer choice.

## Similar Tools

## Related reading

- [Claude SEO vs Seonaut: which free SEO checker should you run](/blog/claude-seo-vs-seonaut/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/seonaut/#app",
    "name": "Seonaut",
    "description": "Open-source SEO crawler in Go for technical audits, self-hosted or cloud",
    "image": "https://martechsignal.com/og/tools/seonaut.png",
    "url": "https://martechsignal.com/tools/seonaut/",
    "sameAs": [
      "https://seonaut.org"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/seonaut/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 9,
      "priceCurrency": "USD",
      "url": "https://seonaut.org/",
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
        "name": "SEO & Search",
        "item": "https://martechsignal.com/categories/seo/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Seonaut",
        "item": "https://martechsignal.com/tools/seonaut/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Seonaut?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Seonaut: Open-source SEO crawler in Go for technical audits, self-hosted or cloud. The public repository carries 782 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Seonaut cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Seonaut has a free tier; paid plans start at $9/mo. MIT-licensed self-hosted free; cloud Lite free for 1 project and 500 URLs per project, Growth $9/mo for 5 projects and 10,000 URLs with recurring audits. We last checked both ends of that split on 2026-09-07. The pricing section above shows what the free tier actually covers."
        }
      },
      {
        "@type": "Question",
        "name": "Is Seonaut a good self-hosted SEO & Search tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A lean, honest, self-hosted technical crawler with 79 documented issue checks; no JS rendering, no API, and a slow-but-alive commit pace."
        }
      },
      {
        "@type": "Question",
        "name": "Does SEOnaut render JavaScript?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. The codebase has no headless browser dependency, and JavaScript rendering appears nowhere in the feature list; the crawler fetches HTML directly. Sites built as client-rendered single-page apps will show empty content, missing links, and phantom issues, because the crawler sees what curl sees. Server-rendered sites, static sites, and sites using pre-rendering audit fine. If your audit targets a React or Vue application without SSR, you need a JS-rendering crawler, and this is not one."
        }
      },
      {
        "@type": "Question",
        "name": "Is SEOnaut free, and what do the cloud plans cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The self-hosted Community edition is MIT-licensed and free, including commercial use per the support page. The hosted service at app.seonaut.org has two tiers: Lite is free with one project and up to 500 URLs per project, and Growth is $9 per month for five projects, 10,000 URLs per project, and recurring audits, billed through Stripe with one month free on annual plans. The practical difference beyond limits is scheduling: recurring audits are a Growth feature, while self-hosted users set up their own cron-triggered crawls."
        }
      },
      {
        "@type": "Question",
        "name": "Does SEOnaut compare to Screaming Frog?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "On core technical auditing, more than you might expect: broken links, redirect chains and loops, missing and duplicate metas, heading structure, hreflang, canonical tags, alt text, orphan and dead-end pages, and response-time checks, with 79 issue types in code and ECharts dashboards. The gaps are the commercial tool's strengths: no JavaScript rendering, no API, no team features, no integrated keyword or log-file analysis, and no tagged releases. The project itself makes no comparison claims; it positions as created by SEOs for everyone rather than as a Screaming Frog competitor. For a no-cost, self-hosted crawl of server-rendered sites, it covers the technical layer; for client-facing audits of JS-heavy sites, a rendering crawler remains the safer choice."
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
    "reviewBody": "Seonaut is a Go crawler for technical SEO audits with a real free cloud tier: one project, 500 URLs. MIT-licensed at 782 stars; small, legible and honest about scope.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/seonaut/#app",
      "name": "Seonaut",
      "url": "https://martechsignal.com/tools/seonaut/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 30,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
