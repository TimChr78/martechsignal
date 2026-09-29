# ProspectOS review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free under MIT self-hosted with scraping API costs called out as the run expense (the vendor pricing page: [pricing page](https://github.com/nando0x/ProspectOS), verified 2026-08-31). |
| Feature depth | 4/10 | Lead discovery and contact enrichment cover the prospecting loop (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Integrations | 3/10 | Google Maps and Instagram documented as data sources plus an API (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| AI capability | 3/10 | Lead discovery and enrichment run as data automation more than model work (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 214 GitHub stars and full self-hosting (the source repository: [repository](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |
| Operational maturity | 2/10 | Founded 2026 at 214 stars as an early project (vendor documentation: [vendor site](https://github.com/nando0x/ProspectOS), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (226 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: lead discovery | ✗ Short native integration list - plan for API work |
| ✓ Native integrations include Google Maps, Instagram (2 listed) |  |

**What is ProspectOS?**
ProspectOS: Open-source lead prospecting CRM with Google Maps and Instagram scraping. ProspectOS ships with lead discovery. The public repository carries 226 stars.

**How much does ProspectOS cost?**
ProspectOS is open source - MIT licensed and free to self-host; the public repository carries 226 stars. You pay in server time and maintenance, not licences.

**Is ProspectOS a good self-hosted CRM tool in 2026?**
A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS.

- **Pricing:** Open Source
- **Category:** [CRM](/categories/crm/)
- **GitHub:** ★ 226
- **Founded:** 2026
- **HQ:** Open source
- **API:** Yes
- **Last verified:** 2026-08-31

**Verdict:** ProspectOS is a tool in CRM with free and open source. The catalog documents 2 AI features, 2 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-08-31. This is a desk review, not a hands-on test. Desk-reviewed

Chatfuel

AI chatbot platform for automating customer conversations on messaging channels

Line Harness

Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control

Cordys CRM

Open-source AI CRM with built-in agents, conversational analytics, and private deployment

HubSpot CRM

Free AI-powered CRM platform with sales, service, and marketing tools unified

[More CRM Tools →](/categories/crm/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [CRM](/categories/crm/)
- ProspectOS
Re-check pending: pricing last verified 2026-08-31 (29 days ago).

## ProspectOS review (2026): pricing, AI features, verdict

Open-source lead prospecting CRM with Google Maps and Instagram scraping

CRM · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit ProspectOS →](https://github.com/nando0x/ProspectOS)

[How we review](/methodology/) · No affiliate links

[Visit ProspectOS →](https://github.com/nando0x/ProspectOS)

## MartechSignal Score: 29/60

ProspectOS is MIT lead prospecting with Google Maps and Instagram scraping built in. At 214 stars it is early, and the scraping APIs carry their own costs and risks.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

ProspectOS is a local lead-prospecting tool for agencies and freelancers who sell websites or digital services to small businesses. It scans Google Maps by niche and city (or by pin and radius), checks each company's website to separate no-site from slow-or-insecure-site, scores the results, and generates an AI-written outreach message plus a PDF diagnosis per lead, all tracked in a visual kanban CRM. The stack is Flask, React 19, TypeScript, and SQLite, runs locally on Windows, and the repo shows 230 passing tests. The honest catch is in the project's own warnings: it is a scraping tool, Google Maps and Instagram scraping can violate those platforms' terms, and the Instagram module logs in with a personal account via instagrapi, which carries a real risk of checkpoint or ban. The README recommends a secondary account and moderate use. MIT-licensed with 206 stars, it is a working codebase for learning and prospecting at small scale, sold to nobody and hosted by you, with the compliance question deliberately left in your hands.

ProspectOS homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Lead discovery
- Contact enrichment
## Key Integrations

- Google Maps
- Instagram
## Pricing

ProspectOS is free to self-host under the MIT licence.

Free and open source (MIT). Self-hosted; scraping APIs may have their own costs.

Current plans and limits live on the [ProspectOS pricing page](https://github.com/nando0x/ProspectOS).

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

The README is unusually candid: a dedicated 'before you use' section spells out that the tool scrapes Google Maps and Instagram, that Instagram access uses your personal account through instagrapi with a documented risk of security checkpoints or bans, and that the WhatsApp cockpit only passively reads a chat window you open yourself. That transparency makes evaluation easier, since the operational risks are the product's most important features. All claims here come from the repository documentation.

The scope is deliberately narrow and local: businesses without websites or with poor ones, approached via WhatsApp with an AI-drafted message and a PDF diagnosis. For a web-design freelancer that is a genuine end-to-end workflow. The Instagram module is optional but account-risk-bearing, and the tool runs on your machine by design, so there is no SaaS convenience layer or team features.

## Verdict

A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS.

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

ProspectOS: Open-source lead prospecting CRM with Google Maps and Instagram scraping. ProspectOS ships with lead discovery. The public repository carries 226 stars.

ProspectOS is open source - MIT licensed and free to self-host; the public repository carries 226 stars. You pay in server time and maintenance, not licences.

A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS.

## Similar Tools

## Related reading

- [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
- [Your Dashboard Can't See AI Search, Here's the 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/prospectos/#app",
    "name": "ProspectOS",
    "description": "Open-source lead prospecting CRM with Google Maps and Instagram scraping",
    "image": "https://martechsignal.com/og/tools/prospectos.png",
    "url": "https://martechsignal.com/tools/prospectos/",
    "sameAs": [
      "https://github.com/nando0x/ProspectOS"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/prospectos/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-08-29",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://github.com/nando0x/ProspectOS",
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
        "name": "ProspectOS",
        "item": "https://martechsignal.com/tools/prospectos/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is ProspectOS?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "ProspectOS: Open-source lead prospecting CRM with Google Maps and Instagram scraping. ProspectOS ships with lead discovery. The public repository carries 226 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does ProspectOS cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "ProspectOS is open source - MIT licensed and free to self-host; the public repository carries 226 stars. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is ProspectOS a good self-hosted CRM tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A working, well-tested local prospecting tool with unusually honest documentation about its scraping risks. Suitable for individual freelancers who accept the terms-of-service exposure; not a team tool, and not compliant-by-design with Google or Instagram ToS."
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
    "reviewBody": "ProspectOS is MIT lead prospecting with Google Maps and Instagram scraping built in. At 214 stars it is early, and the scraping APIs carry their own costs and risks.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/prospectos/#app",
      "name": "ProspectOS",
      "url": "https://martechsignal.com/tools/prospectos/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 29,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
