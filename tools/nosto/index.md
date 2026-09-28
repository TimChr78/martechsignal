# Nosto review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 3/10 | Quote-based: a platform fee plus a GMV and traffic-based fee scaled by modules, with no public numbers (the vendor pricing page, verified 2026-09-28). |
| Feature depth | 7/10 | Recommendations, semantic search, visual AI tagging and category merchandising cover the commerce experience loop (vendor documentation). |
| Integrations | 7/10 | Seven named commerce platforms from Shopify Plus to PrestaShop plus Klaviyo and Attentive (vendor documentation). |
| AI capability | 7/10 | Vector-embedding search and predictive recommendations are core, with visual tagging on top (vendor documentation). |
| Openness | 2/10 | Closed enterprise SaaS (the source repository). |
| Operational maturity | 7/10 | Founded 2013 with a decade of commerce personalization deployments (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; AI capabilities: predictive product recommendations | &#10007; Closed source - no self-hosting option |
| &#10003; Native integrations include Shopify, Shopify Plus, Adobe Commerce (Magento) (11 listed) | &#10007; Enterprise pricing is quote-based - no public numbers |
| &#10003; API access for custom integrations |  |

**What is Nosto?**
AI-powered ecommerce personalization with product recommendations and merchandising. It ships with predictive product recommendations, 11 listed integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Nosto cost?**
Nosto uses enterprise pricing, so the number depends on your volume and contract. Quote-based: a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled by modules and support level. No published numbers anywhere on the site. Our last verified read of the pricing model was 2026-09-07; the vendor&#x27;s pricing page carries the current quote criteria.

**Is Nosto a good Personalization &amp; CDP tool in 2026?**
A genuinely documented enterprise personalization platform with an unusual seam between its core search and the acquired Findologic line. Strong fit for large multilingual catalogs; no self-serve way to find out if it fits yours.

**How does Nosto pricing scale with GMV?**
The pricing FAQ describes a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled further by the modules selected and the support level required. No numbers are published. Attribution matters to the bill: products are grouped so that when a visitor interacts with two products in one group, only the sale from the most recently interacted product counts toward the fee. Pop-ups and onsite recommendations form one group, Facebook and Instagram Ads another, and triggered emails and email widgets a third, and test orders can be billed.

**What are Nosto&#x27;s API rate limits?**
They are costed in points per second rather than requests. Search GraphQL allows 40,000 points per second standard and 200,000 with the Peak Performance package; recommendations allow 10,000 (80,000 advanced) and the main GraphQL API 10,000 (50,000). A search, category, or autocomplete request costs 600 points and a typical recommendation request 100-200. Over-limit calls return HTTP 429 with a Retry-After header (the docs suggest 1 second backoff), current status is exposed in the X-Nosto-Ratelimit-Status header, and nosto-cost-debug returns a per-section cost breakdown.

**How do visitors opt out of Nosto tracking?**
Nosto documents a consent-conditional pattern: wrap the tracking script (connect.nosto.com/include/$accountID) in a check of your consent cookie so it is injected only after a visitor accepts, which the help center says disables the initialization of Nosto entirely for that user. A data processing agreement is published at nosto.com/legal/terms-conditions-dpa. For implementation, that means opt-out lives in your storefront template rather than in a Nosto settings toggle.

- **Pricing:** Enterprise
- **Category:** [Personalization &amp; CDP](/categories/personalization/)
- **Founded:** 2013
- **HQ:** Helsinki, Finland
- **API:** Yes
- **Last verified:** 2026-09-07

**Verdict:** Nosto is a tool in Personalization &amp; CDP with custom pricing. The catalog documents 5 AI features, 11 integrations and a public API. We reviewed it from vendor documentation on 2026-09-07. This is a desk review, not a hands-on test. Desk-reviewed

Clerk.io

AI-powered ecommerce personalization with search, recommendations, and email

Bloomreach

AI-powered commerce experience platform with search, personalization, and CDP

Dynamic Yield

AI-powered personalization platform for web, mobile, and email experiences

Hypotenuse AI

AI content generation platform for ecommerce product descriptions and articles

GrowthBook

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting

[More Personalization &amp; CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Personalization &amp; CDP](/categories/personalization/)
- Nosto
## Nosto review (2026): pricing, AI features, verdict

AI-powered ecommerce personalization with product recommendations and merchandising

Personalization &amp; CDP · Enterprise Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-07

[Visit Nosto &#8594;](https://www.nosto.com)

[How we review](/methodology/) · No affiliate links

[Visit Nosto &#8594;](https://www.nosto.com)

## MartechSignal Score: 33/60

Nosto is commerce personalization with real merchandising controls: recommendations, semantic search and visual tagging. GMV-based pricing means success and cost move together.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Nosto is a commerce experience platform for online stores, built around a shared AI layer the company brands experience.AI: one engine that collects shopper behavior and feeds every module, so what a shopper clicks in search informs the recommendations and category sort orders they see next. It is sold as two modular suites. Product Experience Cloud covers personalized search, category merchandising, product recommendations, post-purchase upsell, dynamic bundles, and personalized emails; an AI Search product is labeled coming soon on the pricing page. Content Experience Cloud covers A/B testing and optimization, onsite content personalization, pop-ups, and shoppable UGC. The search module documents semantic search with vector embeddings, AI-suggested synonyms, merchandising rules keyed to margin, stock, and seasonality, and 27 languages out of the box; content and vector search carry alpha labels. Implementation is documented in detail: Nosto replicates the store catalog (one account per domain and language), a script tag plus page tagging feeds behavioral profiles, and published search go-live estimates run from 1-3 weeks (templates) to 4-8 weeks (API). GraphQL is the documented path into the intelligence engine; REST is legacy, used to push orders, products, and exchange rates, and stays mandatory for product updates in SPA builds. Rate limits are published in points, with a search request costing 600. Pricing is quote-based: a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled by the modules and support level, with AI bundled into every module and an optional Product Scalability Package carrying a 99.99% uptime SLA. There is no self-serve trial; qualified merchants get a proof of concept on their own store data. Founded in 2013 with eight offices including Helsinki, London, and New York, Nosto reports more than 1,500 brand customers and a 4.6/5 G2 rating. Its search line now includes the Austrian vendor Findologic, whose typo-tolerance docs sit in Nosto&#x27;s help center beside its own.

Nosto homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Predictive product recommendations
- Semantic search with vector embeddings
- Visual AI product tagging
- AI content personalization
- Category merchandising with global rules
## Key Integrations

- Shopify
- Shopify Plus
- Adobe Commerce (Magento)
- BigCommerce
- Salesforce Commerce Cloud
- Shopware
- PrestaShop
- Klaviyo
- Attentive
- Yotpo
- Google Analytics
## Pricing

Nosto is sold on quote-based enterprise contracts.

Quote-based: a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled by modules and support level. No published numbers anywhere on the site.

Current plans and limits live on the [Nosto pricing page](https://www.nosto.com/pricing/).

## How to install

- No self-serve signup and no published pricing: the entry point is the 30-minute demo form at nosto.com/book-a-demo. The pricing FAQ states it directly: &quot;While we do not offer a standard self-service free trial, we provide a structured Proof of Concept (PoC) for qualified merchants.&quot;
- Qualified merchants install the Nosto app from their platform&#x27;s app store (Shopify, Adobe Commerce, BigCommerce, Shopware) with a Nosto representative attached to the account, then preview AI Search and merchandising against their own live catalog data.
- Module activation is vendor-gated, not self-serve. For search the docs say: &quot;Your search engine will be ready after the Nosto representative enables the Search module for your account.&quot;
- Technical onboarding is script tag plus catalog replication: the tracking script (connect.nosto.com/include/$accountID) and page tagging build behavioral profiles, and Nosto replicates the product catalog, one account per domain and language.
- Headless and SPA builds use the Session API with GraphQL for reads; the docs keep REST mandatory for product updates in SPA/PWA storefronts and warn that proxying GraphQL through a backend hides the end user&#x27;s IP, breaking geolocation.
## Requirements

A storefront on Shopify/Shopify Plus, Adobe Commerce, BigCommerce, Salesforce Commerce Cloud, Shopware, PrestaShop, or a custom build you can tag and replicate. Search requests are metered in points, not calls: a search, category, or autocomplete request costs 600 points against a 40,000 points-per-second standard allowance (200,000 with the paid Peak Performance package), and recommendation requests typically cost 100-200 points. API integrations need GraphQL capability; the legacy REST API is for pushing orders, products, and exchange rates. Higher support tiers (priority support, dedicated CSM) are attached to the Professional and Enterprise packages.

## Best for

Mid-market and enterprise retailers on Shopify Plus, Adobe Commerce, BigCommerce, or Shopware who want search, merchandising, and recommendations driven by one shared engine, especially multilingual and long-tail catalogs (27 languages out of the box, vector search built for queries without explicit keywords) and merchandising teams that work in the UI without depending on IT.

## Not for

Small catalogs and small teams: pricing is quote-based GMV-plus-traffic with a base platform fee, module activation needs a representative, and there is no self-serve trial to evaluate against. Also not for teams that need AI Search today (labeled coming soon, with content and vector search in alpha), SPA teams hoping to use in-browser search templates (the docs steer them to the JS library or API), or headless builds that need geo-targeting behind a proxied GraphQL connection.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from nosto.com, docs.nosto.com, help.nosto.com, and the pricing page (September 2026). Not a hands-on review. The public surface is unusually deep for a quote-based vendor: a full technical docs site with published rate limits and implementation timelines, a help center, and a pricing page that explains structure while publishing no numbers. Evaluation without a sales conversation stops at the documentation.

The correction that matters: our earlier description described a three-module platform (recommendations, search and discovery, category merchandising) and said merchants pay &quot;a fixed percentage of revenue.&quot; Both are outdated. The current structure is two suites (Product Experience Cloud, Content Experience Cloud) on the experience.AI layer, and the pricing FAQ words the volume component as &quot;a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic),&quot; not a percentage.

A second correction: our earlier text credited &quot;two dedicated search acquisitions.&quot; Only one is verifiable on live pages. Findologic (Salzburg) is confirmed as part of Nosto, with a 55-article FAQ collection in Nosto&#x27;s help center; Fredhopper is branded &quot;A rezolve solution&quot; under Crownpeak and is not a Nosto property. The split is visible in the product: typo tolerance and Smart Did-You-Mean live in the Findologic collection, while the core search docs cover semantic and vector search, and the help center keeps two separate category merchandising collections (Platform v1 and Universal).

What the docs do well: published points-based rate limits with cost per request type, four search implementation routes with honest timelines (1-3 weeks for templates up to 4-8 weeks for the API), a documented consent pattern that disables Nosto entirely for visitors who opt out, a published DPA, and a hard telemetry-style detail most vendors omit, the attribution rule that bills only the most recently interacted product when a visitor touches two products in a group.

## Verdict

A genuinely documented enterprise personalization platform with an unusual seam between its core search and the acquired Findologic line. Strong fit for large multilingual catalogs; no self-serve way to find out if it fits yours.

## Pros and cons

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

AI-powered ecommerce personalization with product recommendations and merchandising. It ships with predictive product recommendations, 11 listed integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Nosto uses enterprise pricing, so the number depends on your volume and contract. Quote-based: a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled by modules and support level. No published numbers anywhere on the site. Our last verified read of the pricing model was 2026-09-07; the vendor&#x27;s pricing page carries the current quote criteria.

A genuinely documented enterprise personalization platform with an unusual seam between its core search and the acquired Findologic line. Strong fit for large multilingual catalogs; no self-serve way to find out if it fits yours.

The pricing FAQ describes a base platform fee plus a fixed fee calculated on your store&#x27;s volume (GMV turnover and traffic), scaled further by the modules selected and the support level required. No numbers are published. Attribution matters to the bill: products are grouped so that when a visitor interacts with two products in one group, only the sale from the most recently interacted product counts toward the fee. Pop-ups and onsite recommendations form one group, Facebook and Instagram Ads another, and triggered emails and email widgets a third, and test orders can be billed.

They are costed in points per second rather than requests. Search GraphQL allows 40,000 points per second standard and 200,000 with the Peak Performance package; recommendations allow 10,000 (80,000 advanced) and the main GraphQL API 10,000 (50,000). A search, category, or autocomplete request costs 600 points and a typical recommendation request 100-200. Over-limit calls return HTTP 429 with a Retry-After header (the docs suggest 1 second backoff), current status is exposed in the X-Nosto-Ratelimit-Status header, and nosto-cost-debug returns a per-section cost breakdown.

Nosto documents a consent-conditional pattern: wrap the tracking script (connect.nosto.com/include/$accountID) in a check of your consent cookie so it is injected only after a visitor accepts, which the help center says disables the initialization of Nosto entirely for that user. A data processing agreement is published at nosto.com/legal/terms-conditions-dpa. For implementation, that means opt-out lives in your storefront template rather than in a Nosto settings toggle.

## Similar Tools

## Related reading

- [The AI-search funnel map GA4 won't give you](/blog/ai-search-funnel-map-ga4-wont-give-you/)
- [Google Doesn't Need Your Site Anymore. You Taught It Everything It Knows.](/blog/google-doesnt-need-your-site-anymore-you-taught-it-everything-it-knows/)
- [Your Dashboard Can't See AI Search, Here's the 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/)
### Quick Facts

Related guides: [Ai Personalization Tools](/best/ai-personalization-tools)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/nosto/#app",
    "name": "Nosto",
    "description": "AI-powered ecommerce personalization with product recommendations and merchandising",
    "image": "https://martechsignal.com/og/tools/nosto.png",
    "url": "https://martechsignal.com/tools/nosto/",
    "sameAs": [
      "https://www.nosto.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/nosto/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-07",
    "datePublished": "2026-07-27"
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
        "name": "Personalization & CDP",
        "item": "https://martechsignal.com/categories/personalization/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Nosto",
        "item": "https://martechsignal.com/tools/nosto/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Nosto?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI-powered ecommerce personalization with product recommendations and merchandising. It ships with predictive product recommendations, 11 listed integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Nosto cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nosto uses enterprise pricing, so the number depends on your volume and contract. Quote-based: a base platform fee plus a fixed fee calculated on your store's volume (GMV turnover and traffic), scaled by modules and support level. No published numbers anywhere on the site. Our last verified read of the pricing model was 2026-09-07; the vendor's pricing page carries the current quote criteria."
        }
      },
      {
        "@type": "Question",
        "name": "Is Nosto a good Personalization & CDP tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A genuinely documented enterprise personalization platform with an unusual seam between its core search and the acquired Findologic line. Strong fit for large multilingual catalogs; no self-serve way to find out if it fits yours."
        }
      },
      {
        "@type": "Question",
        "name": "How does Nosto pricing scale with GMV?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The pricing FAQ describes a base platform fee plus a fixed fee calculated on your store's volume (GMV turnover and traffic), scaled further by the modules selected and the support level required. No numbers are published. Attribution matters to the bill: products are grouped so that when a visitor interacts with two products in one group, only the sale from the most recently interacted product counts toward the fee. Pop-ups and onsite recommendations form one group, Facebook and Instagram Ads another, and triggered emails and email widgets a third, and test orders can be billed."
        }
      },
      {
        "@type": "Question",
        "name": "What are Nosto's API rate limits?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "They are costed in points per second rather than requests. Search GraphQL allows 40,000 points per second standard and 200,000 with the Peak Performance package; recommendations allow 10,000 (80,000 advanced) and the main GraphQL API 10,000 (50,000). A search, category, or autocomplete request costs 600 points and a typical recommendation request 100-200. Over-limit calls return HTTP 429 with a Retry-After header (the docs suggest 1 second backoff), current status is exposed in the X-Nosto-Ratelimit-Status header, and nosto-cost-debug returns a per-section cost breakdown."
        }
      },
      {
        "@type": "Question",
        "name": "How do visitors opt out of Nosto tracking?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nosto documents a consent-conditional pattern: wrap the tracking script (connect.nosto.com/include/$accountID) in a check of your consent cookie so it is injected only after a visitor accepts, which the help center says disables the initialization of Nosto entirely for that user. A data processing agreement is published at nosto.com/legal/terms-conditions-dpa. For implementation, that means opt-out lives in your storefront template rather than in a Nosto settings toggle."
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
    "reviewBody": "Nosto is commerce personalization with real merchandising controls: recommendations, semantic search and visual tagging. GMV-based pricing means success and cost move together.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/nosto/#app",
      "name": "Nosto",
      "url": "https://martechsignal.com/tools/nosto/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 33,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
