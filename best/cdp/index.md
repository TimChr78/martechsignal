# Best CDP platforms (2026): 6 compared


| Tool | Pricing | Open source | Best for |
| --- | --- | --- | --- |
| [RudderStack](/tools/rudderstack/) | Free tier | Source-available (fair-code) | Best Segment-compatible router for warehouse-first stacks on a budget. |
| [Hightouch](/tools/hightouch/) | Freemium | No | Best activation layer when the warehouse is already the source of truth. |
| [Jitsu](/tools/jitsu/) | Freemium | Yes (MIT) | Best fully open-source event collection for self-hosting the pipeline. |
| [Apache Unomi](/tools/apache-unomi/) | Open Source | Yes (Apache-2.0) | Best when data-residency rules and European-consent governance drive the architecture. |
| [Twilio Segment](/tools/segment/) | Freemium | No | Best documented default when budget is not the deciding axis. |
| [Tealium](/tools/tealium/) | Enterprise | No | Best enterprise governance and consent orchestration at large scale. |

[Open-Source Tools](/categories/open-source/)[Personalization & CDP](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Best Customer Data Platforms (2026): composable to self-hosted

RudderStack fits warehouse-first teams that want a self-hostable event router with a free 250K events/mo tier. Hightouch activates data already in the warehouse with no event collection of its own. Jitsu is the fully open-source option. Apache Unomi suits consent- and residency-governed European stacks. Segment is the documented default at a price, Tealium the enterprise governance play.

**Our top pick: [RudderStack](#rudderstack)** — Best Segment-compatible router for warehouse-first stacks on a budget. [Try RudderStack](https://www.rudderstack.com/)

Last verified 2026-10-01.

## How we picked

A customer data platform solves one problem: events arrive from an app, and a coherent profile has to come out where the campaigns run. The 2026 market splits cleanly along one axis - does the tool store the profile itself (classic CDPs like Segment and Tealium), or does it only route warehouse data and leave storage to Snowflake or BigQuery (composable CDPs like Hightouch, and event routers like RudderStack or Jitsu)?

This list draws only from tools already in the catalog, each with verified pricing on its own page and, where open source, a live GitHub snapshot. It is desk research against vendor documentation and receipts, not a hands-on bake-off. Pricing figures are the catalog's last verified numbers, dated on each tool page.

Cuts to start from: cheapest Segment-compatible router is RudderStack (free 250K events/mo, self-hostable data plane). Activation-only over an existing warehouse is Hightouch (free for 2 active syncs). Fully self-hosted and open-source routes are Jitsu (event router) and Apache Unomi (rules-based profile store). The documented classic profile CDP is Segment. Enterprise tag-and-hub governance is Tealium.

## What we checked and when

Pricing checked 2026-09-28 against each vendor's own pricing page · API availability confirmed from public documentation · Integrations read from vendor listings and source repositories. Not installed and not benchmarked: this is desk research with dates on it.

What we could not verify is called out under each tool below.

## Browse the hubs behind these picks

## Open-source momentum, with receipts

Star counts we snapshot ourselves every morning - check any of them against GitHub in one click.

- Jitsu - 5,094 stars, +3 in the 6-snapshot window to 2026-10-01 5,091→5,094 [verify on GitHub](https://github.com/jitsucom/jitsu)
- Apache Unomi - 375 stars, +0 in the 6-snapshot window to 2026-10-01 375→375 [verify on GitHub](https://github.com/apache/unomi)
[All movers on the trending page](/trending/).

## [RudderStack](/tools/rudderstack/)

RudderStack routes events from SDKs into warehouses and 200+ cloud destinations with reverse ETL closing the loop. The self-hostable Go data plane (rudder-server, needs only PostgreSQL) plus a free 250K events/mo cloud tier make it the cheapest Segment-shaped start; Growth at $265/mo adds unlimited team members and 30-minute warehouse syncs.

**Verdict:** Best Segment-compatible router for warehouse-first stacks on a budget.

Vendor: [Official site](https://www.rudderstack.com/) · [Pricing](https://www.rudderstack.com/pricing/) · [GitHub](https://github.com/rudderlabs/rudder-server)

**Skip it if you want a managed profile store with identity resolution out of the box - the OSS data plane leaves that to your warehouse.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Hightouch](/tools/hightouch/)

Hightouch does not collect events at all: it queries the warehouse you already run and syncs audiences and traits into Salesforce, Braze, Klaviyo, Meta Ads, and Google Ads. Identity resolution and AI Decisioning extend it beyond batch reverse ETL. Free plan covers 2 active syncs monthly; self-serve covers 10; business tier quotes on usage.

**Verdict:** Best activation layer when the warehouse is already the source of truth.

Vendor: [Official site](https://hightouch.com/) · [Pricing](https://hightouch.com/pricing)

**Skip it if the company has no modern data warehouse - there is nothing for it to sync from.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Jitsu](/tools/jitsu/)

Jitsu is the fully open-source (MIT) event router in this list: self-host the Go data plane, keep data in your Postgres cluster, and mirror the Segment API so existing SDK code keeps working. Cloud adds a managed control plane; the free tier covers modest event counts.

**Verdict:** Best fully open-source event collection for self-hosting the pipeline.

Vendor: [Official site](https://jitsu.com) · [Pricing](https://jitsu.com/pricing) · [GitHub](https://github.com/jitsucom/jitsu)

**Skip it if managed identity graphs and a large destination catalog are day-one requirements.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Apache Unomi](/tools/apache-unomi/)

Apache Unomi is the rules-based profile store of the ASF: Java war deployable, OSGi extension points, consent and privacy management contextually aware. Active community but a much smaller one (375 GitHub stars) and heavier operational lift than the routers.

**Verdict:** Best when data-residency rules and European-consent governance drive the architecture.

Vendor: [Official site](https://unomi.apache.org) · [GitHub](https://github.com/apache/unomi)

**Skip it if you need a modern UI, SDK breadth, or quick time-to-value - Unomi is plumbing, not product.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Twilio Segment](/tools/segment/)

Twilio Segment remains the reference CDP: the widest SDK and destination catalog, the cleanest docs, and a protocol every router here copies. Pricing is the catch - free to 1,000 monthly tracked users, Team from $120/mo for 10,000 MTUs with per-event overages.

**Verdict:** Best documented default when budget is not the deciding axis.

Vendor: [Official site](https://segment.com) · [Pricing](https://www.twilio.com/en-us/pricing/customer-data)

**Skip it if event volume pricing at scale outruns the budget; warehouse-first or open-source stacks start cheaper.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Tealium](/tools/tealium/)

Tealium sells governance and enterprise control: tag management plus the Customer Data Hub with consent orchestration, regional deployment, and audit trails. No published pricing - annual enterprise contracts only.

**Verdict:** Best enterprise governance and consent orchestration at large scale.

Vendor: [Official site](https://tealium.com) · [Pricing](https://tealium.com/pricing/)

**Skip it if procurement cannot fund an unquoted annual contract or the team is below enterprise scale.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

Every price quoted here comes from the vendor's own pricing page as catalogued on the tool page. Browse [all 166 tools](/tools/) or read [how we evaluate](/methodology/), or download the [machine-readable catalog](/catalog-tools.json).

## What is the difference between a classic and a composable CDP?

A classic CDP (Segment, Tealium) collects events itself and owns the profile store. A composable CDP (Hightouch) leaves collection and storage to the warehouse you already have and only routes data out to tools. RudderStack straddles both: it can collect events and push them to your warehouse.

## Which one can we self-host completely?

Jitsu (MIT, event routing plus light profiles) and Apache Unomi (ASF, rules-based profile store). RudderStack self-hosts the data plane while the control plane runs in the cloud.

## Which one is cheapest to start?

RudderStack's 250K-events free tier and Hightouch's 2-sync free plan are both $0. Segment's free tier stops at 1,000 monthly tracked users, then Team pricing starts at $120/mo.

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Best Customer Data Platforms (2026): composable to self-hosted",
    "datePublished": "2026-10-01",
    "dateModified": "2026-10-01",
    "author": {
      "@type": "Person",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/"
    },
    "publisher": {
      "@id": "https://martechsignal.com/#organization"
    },
    "isPartOf": {
      "@id": "https://martechsignal.com/#website"
    },
    "numberOfItems": 6,
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "RudderStack",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/rudderstack/#app",
          "url": "https://martechsignal.com/tools/rudderstack/",
          "name": "RudderStack"
        }
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Hightouch",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/hightouch/#app",
          "url": "https://martechsignal.com/tools/hightouch/",
          "name": "Hightouch"
        }
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Jitsu",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/jitsu/#app",
          "url": "https://martechsignal.com/tools/jitsu/",
          "name": "Jitsu"
        }
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Apache Unomi",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/apache-unomi/#app",
          "url": "https://martechsignal.com/tools/apache-unomi/",
          "name": "Apache Unomi"
        }
      },
      {
        "@type": "ListItem",
        "position": 5,
        "name": "Twilio Segment",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/segment/#app",
          "url": "https://martechsignal.com/tools/segment/",
          "name": "Twilio Segment"
        }
      },
      {
        "@type": "ListItem",
        "position": 6,
        "name": "Tealium",
        "item": {
          "@type": "SoftwareApplication",
          "@id": "https://martechsignal.com/tools/tealium/#app",
          "url": "https://martechsignal.com/tools/tealium/",
          "name": "Tealium"
        }
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
        "name": "Best-of lists",
        "item": "https://martechsignal.com/best/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Best Customer Data Platforms (2026): composable to self-hosted",
        "item": "https://martechsignal.com/best/cdp/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/best/cdp/", "breadcrumb": {"@id": "https://martechsignal.com/best/cdp/#breadcrumb"}, "dateModified": "2026-10-01"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
