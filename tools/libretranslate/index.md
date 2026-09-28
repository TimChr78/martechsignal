# LibreTranslate review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Free self-hosted; the hosted API is billed per character on libretranslate.com, stated plainly (Sep 2026) (the vendor pricing page). |
| Feature depth | 4/10 | Neural translation, language detection and a translation API cover localization narrowly (vendor documentation). |
| Integrations | 4/10 | Mastodon, Argos Translate and OpenAPI/Swagger documented (vendor documentation). |
| AI capability | 5/10 | Argos Translate neural models with automatic language detection are the machine core (vendor documentation). |
| Openness | 9/10 | AGPL-3.0 with 16.8k GitHub stars and vendor-lock-in-free self-hosting (the source repository). |
| Operational maturity | 5/10 | 16.8k stars with a hosted per-character service as the commercial arm (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; AGPL-3.0 licence with free self-hosting | &#10007; Translation quality sits below the large commercial engines, especially in uncommon language pairs |
| &#10003; AI capabilities: neural machine translation via Argos Translate models | &#10007; The hosted API publishes no extractable price page, so per-character costs are unknown until quoted |
| &#10003; Established community (16,830 GitHub stars) | &#10007; Self-hosting demands GPU or CPU capacity that scales with volume, and translation is resource-heavy |
| &#10003; Free to self-host under AGPL-3.0, including commercial use, with no per-character billing |  |
| &#10003; Runs offline once models are downloaded, which settles data handling questions outright |  |
| &#10003; The Swagger-documented REST API makes it a drop-in translation backend for other software |  |

**What is LibreTranslate?**
Open-source machine translation API for content localization, self-hostable and free of vendor lock-in. It ships with neural machine translation via Argos Translate models, 16,830 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does LibreTranslate cost?**
LibreTranslate is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 16,830 stars; native integrations cover Mastodon, Argos Translate, OpenAPI/Swagger. You pay in server time and maintenance, not licences.

**Is LibreTranslate a good self-hosted AI Content &amp; Copywriting tool in 2026?**
The translation API to run yourself when cost control and data handling matter more than peak quality. Good for drafts and internal content; keep human review for customer-facing copy.

**Is LibreTranslate free?**
Yes to self-host, including for commercial use. The hosted API on libretranslate.com bills per character behind an API key, but the site had no extractable public price page in September 2026.

**How good is its translation quality?**
Solid for drafts, internal communication, and understanding content in other languages. It trails Google Translate and DeepL on polish, so customer-facing copy still passes a human editor.

**Can LibreTranslate run offline?**
Yes. Once the language models are on disk, the server works with no internet connection, which is the main reason teams pick it for sensitive content.

**What connects to LibreTranslate?**
Anything that can call a REST API. Mastodon is the best-known example, where admins point the post translation backend at a LibreTranslate instance, and the Swagger docs cover the rest.

- **Pricing:** Open Source
- **Category:** [AI Content &amp; Copywriting](/categories/content-ai/)
- **GitHub:** ★ 16830
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** LibreTranslate is a tool in AI Content &amp; Copywriting with free and open source. The catalog documents 3 AI features, 3 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Strapi

Open-source headless CMS with AI-powered content management and API-first design

Predis.ai

AI-powered social media content generator for posts, videos, and ad creatives

Chatwoot

Open-source customer engagement suite with Captain AI and full self-hosting

ContentBot

AI content automation platform with workflows for blogs, ads, and social posts

[More AI Content &amp; Copywriting Tools →](/categories/content-ai/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [AI Content &amp; Copywriting](/categories/content-ai/)
- LibreTranslate
## LibreTranslate review (2026): pricing, AI features, verdict

Open-source machine translation API for content localization, self-hostable and free of vendor lock-in

AI Content &amp; Copywriting · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit LibreTranslate &#8594;](https://libretranslate.com)

[How we review](/methodology/) · No affiliate links

[Visit LibreTranslate &#8594;](https://libretranslate.com)

## MartechSignal Score: 35/60

LibreTranslate is the translation API you can own: AGPL, 16.8k stars, billed per character only if you use their hosting. For localization at volume, self-hosting is the whole argument.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

LibreTranslate is an open-source machine translation API, licensed AGPL-3.0 with 16,830 GitHub stars. It runs neural translation models through Argos Translate and serves them over a REST interface with automatic language detection, so it fits content localization pipelines that need translation as a service rather than as a website. You can self-host it with Docker or pip and run it offline, which keeps text away from third-party translation vendors and their retention policies. Self-hosting is free. The hosted instance at libretranslate.com charges per character through an API key, but the site publishes no price page we could extract in September 2026, so hosted costs need confirming before anyone budgets for them. The API surface is documented with Swagger, and other software can point its translation backend at a LibreTranslate server; Mastodon is the common example, and public instances such as Disroot run on it. Quality is the honest trade-off. The models are smaller than the commercial engines from Google or DeepL, so output fits gisting, internal drafts, and support content better than publish-ready marketing copy in every language pair. Teams that want machine translation under their own control, with an API their code can call, get a working system at no licence cost and can layer human review on top for anything customer-facing.

## AI Capabilities

- Neural machine translation via Argos Translate models
- Automatic language detection
- Self-hosted translation API
## Key Integrations

- Mastodon
- Argos Translate
- OpenAPI/Swagger
## Pricing

LibreTranslate is free to self-host under the AGPL-3.0 licence.

Free self-hosted; hosted API billed per character on libretranslate.com (Sep 2026)

## Best for

Teams building localization pipelines that want a free, self-hosted translation API with no per-character metering and no text leaving their infrastructure.

## Not for

Teams publishing translated marketing copy straight to customers in many languages. The models trail the commercial engines, and the hosted instance has no public price list.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Hands-on (2026-09-28): we installed the Argos Translate 1.11.0 engine behind LibreTranslate, downloaded the English-to-Swedish model (about 100 MB) and translated a marketing sentence fully locally. The output was idiomatic Swedish, sentence splitting ran through Stanza, and no text left the machine. Model downloads and language coverage are the constraints to plan for.

## Verdict

The translation API to run yourself when cost control and data handling matter more than peak quality. Good for drafts and internal content; keep human review for customer-facing copy.

## Pros and cons

## Related concepts

- [AI content](/glossary/ai-content-generation/)
- [Agentic Marketing](/glossary/agentic-marketing/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source machine translation API for content localization, self-hostable and free of vendor lock-in. It ships with neural machine translation via Argos Translate models, 16,830 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

LibreTranslate is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 16,830 stars; native integrations cover Mastodon, Argos Translate, OpenAPI/Swagger. You pay in server time and maintenance, not licences.

The translation API to run yourself when cost control and data handling matter more than peak quality. Good for drafts and internal content; keep human review for customer-facing copy.

Yes to self-host, including for commercial use. The hosted API on libretranslate.com bills per character behind an API key, but the site had no extractable public price page in September 2026.

Solid for drafts, internal communication, and understanding content in other languages. It trails Google Translate and DeepL on polish, so customer-facing copy still passes a human editor.

Yes. Once the language models are on disk, the server works with no internet connection, which is the main reason teams pick it for sensitive content.

Anything that can call a REST API. Mastodon is the best-known example, where admins point the post translation backend at a LibreTranslate instance, and the Swagger docs cover the rest.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [AI visibility advice, audited against 775 logged citations](/blog/geo-experiments-vs-ai-visibility-playbook/)
- [MCP Rewrites the Integration Economics of Your Marketing Stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/libretranslate/#app",
    "name": "LibreTranslate",
    "description": "Open-source machine translation API for content localization, self-hostable and free of vendor lock-in",
    "image": "https://martechsignal.com/og/tools/libretranslate.png",
    "url": "https://martechsignal.com/tools/libretranslate/",
    "sameAs": [
      "https://libretranslate.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/libretranslate/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-25",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://libretranslate.com",
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
        "name": "AI Content & Copywriting",
        "item": "https://martechsignal.com/categories/content-ai/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "LibreTranslate",
        "item": "https://martechsignal.com/tools/libretranslate/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is LibreTranslate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source machine translation API for content localization, self-hostable and free of vendor lock-in. It ships with neural machine translation via Argos Translate models, 16,830 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does LibreTranslate cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "LibreTranslate is open source - AGPL-3.0 licensed and free to self-host; the public repository carries 16,830 stars; native integrations cover Mastodon, Argos Translate, OpenAPI/Swagger. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is LibreTranslate a good self-hosted AI Content & Copywriting tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The translation API to run yourself when cost control and data handling matter more than peak quality. Good for drafts and internal content; keep human review for customer-facing copy."
        }
      },
      {
        "@type": "Question",
        "name": "Is LibreTranslate free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes to self-host, including for commercial use. The hosted API on libretranslate.com bills per character behind an API key, but the site had no extractable public price page in September 2026."
        }
      },
      {
        "@type": "Question",
        "name": "How good is its translation quality?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Solid for drafts, internal communication, and understanding content in other languages. It trails Google Translate and DeepL on polish, so customer-facing copy still passes a human editor."
        }
      },
      {
        "@type": "Question",
        "name": "Can LibreTranslate run offline?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Once the language models are on disk, the server works with no internet connection, which is the main reason teams pick it for sensitive content."
        }
      },
      {
        "@type": "Question",
        "name": "What connects to LibreTranslate?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Anything that can call a REST API. Mastodon is the best-known example, where admins point the post translation backend at a LibreTranslate instance, and the Swagger docs cover the rest."
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
    "reviewBody": "LibreTranslate is the translation API you can own: AGPL, 16.8k stars, billed per character only if you use their hosting. For localization at volume, self-hosting is the whole argument.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/libretranslate/#app",
      "name": "LibreTranslate",
      "url": "https://martechsignal.com/tools/libretranslate/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 35,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
