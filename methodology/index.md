# Methodology


| Pillar | What it measures | Anchor points |
| --- | --- | --- |
| Pricing transparency | Whether buyers can see real numbers before talking to sales. | 0: no public pricing · 3: quote-only pricing page · 5: entry price published · 7: full tier table with limits · 10: public tiers, limits, and documented free tier |
| Feature depth | Coverage against what the category baseline requires. | 3: core capability only · 5: baseline covered · 8: baseline plus real differentiators · 10: category-defining breadth |
| Integrations | Documented connection surface: API, native integrations, marketplace. | 0: none documented · 3: API or a few natives · 5: API plus 10-30 natives · 7: broad catalog and marketplace · 10: marketplace, open API, and iPaaS coverage |
| AI capability | Shipped AI features, not AI marketing copy. | 0: none · 3: mentioned but thin · 5: one real shipped feature · 7: several shipped features · 10: AI-native surface (agents, MCP, protocol-level) |
| Openness | Exit rights: source access, self-hosting, data portability. | 0: closed, no export · 3: data export exists · 5: full export and open API · 7: source-available or open-core · 10: open-source licence and self-hostable |
| Operational maturity | Whether the product is maintained like a product. | 0: unknown or abandoned · 3: young or single maintainer · 5: steady cadence · 7: multiple releases a year, real docs, real company · 10: enterprise cadence, SLAs, ecosystem |

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Methodology

By [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-26

Everything on MartechSignal follows one evidence standard and one scoring rubric. Both are published here so you can check our work.

## How we evaluate

Every assessment is researched from public documentation, the source repository when the product is open, and vendor materials including pricing pages. Running the tools is not our default and we do not claim it. Where a page does report hands-on work, that page says exactly what was run and discloses any relationship to the product on its face. Where a page depends on a specific fact (a price, an integration count, a release cadence), the fact is stated with its source and its verification date.

What that standard gives us: prices only as the vendor publishes them, statistics only from the named source, and no synthetic performance data. What it costs us: we cannot tell you how a tool feels to use day to day. Where a question only hands-on testing can answer, the page says so.

Corrections are public. When a published claim is wrong, the fix ships with an entry on the [corrections page](/corrections/) in the same change.

## The MartechSignal Score

Each evaluated tool receives a 0-10 score on six pillars. The total is the sum of the six, reported out of 60. Every pillar score on a tool page carries a one-line evidence statement naming its source. A score without evidence is a defect.

The score is an editorial assessment against published anchors. It is not a lab benchmark, not a verified-buyer rating, and not influenced by vendors: we take no vendor money, run no affiliate links, and accept no payment for placement or scoring. Tools we cover include products we built ourselves; those pages say so on their face.

The pilot covered the 20 most-searched tools on the site. The rollout now covers 160 of 163 active tool pages with the same six-pillar MartechSignal Score out of 60. The three exceptions, each named rather than generalized: [Zoho CRM](/tools/zoho-crm/), [AI Marketing Claude](/tools/ai-marketing-claude/), and [Digital Marketing Pro](/tools/digital-marketing-pro/) are not yet scored against the rubric. Verification dates and price sources sit on each tool page; the rubric below is the same one they were all judged against.

## Data artifacts

When a post cites a number we computed, the underlying artifact is published with its window and source so the query can be rerun.

**gsc-query-distribution-2026-05-29_2026-08-26.csv.** Source: Google Search Console API (searchAnalytics.query), property sc-domain:martechsignal.com, webmasters scope, service-account auth. Window: 2026-05-29 through 2026-08-26 (90 days). Dimensions: query-level rows, no filters, up to 1,000 rows (417 returned; the API omits ultra-low-impression queries). Headline numbers cited on the site: 417 queries, 1,737 total impressions, 0 clicks site-wide in the window; 1,492 impressions (85.9%) at average position 51+. Caveat: average position is Google's mean over impressions in the window; day-by-day rank volatility is not visible in the export. Any GSC performance export filtered to the same dates produces the same shape.

## OSS Momentum Tracker

The [momentum dataset](/oss-momentum.json) covers every catalog entry that names a public GitHub repository. Two real sources back it: fresh GitHub repository totals and release dates, and the measurement series from the git history of our public catalog (every committed snapshot of the tools file, dated by its commit). GitHub's star-timestamp endpoints are not accessible to this project, so each growth figure states its own snapshot-bounded window and snapshots are never interpolated. Entries without a recorded repository URL are listed as out of scope, never estimated.

## Source claims

A claim ships on a page only when a source is attached to it at write time. If the source cannot be named, the claim does not ship. This covers feature lists, pricing statements, customer counts, star counts, and rankings alike, and it applies to every page in the directory including this one. A claim without a source is removed, not softened.

## Corrections

Published errors get public entries. See the [corrections page](/corrections/) for the running log.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
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
        "name": "Methodology",
        "item": "https://martechsignal.com/methodology/"
      }
    ]
  },
  {
    "@type": "WebPage",
    "@id": "https://martechsignal.com/methodology/#webpage",
    "name": "How we evaluate",
    "description": "How MartechSignal researches tools, verifies prices and dates, and scores the six pillars: the rubric, the review policy, and the corrections process.",
    "url": "https://martechsignal.com/methodology/",
    "dateModified": "2026-09-28"
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
