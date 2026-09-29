# Attribution models

Attribution

AI-powered marketing attribution platform connecting ad spend to revenue

Amplitude

AI-powered digital analytics platform for product and marketing teams

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

[Browse all tools →](/tools/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Attribution Models (First-Touch, Last-Touch, Multi-Touch)

GLOSSARY

## Definition

An attribution model is the rule that decides which marketing touchpoint gets credit for a conversion. First-touch credits the first interaction. Last-touch credits the final one before purchase. Linear splits credit equally. Time-decay gives more weight to recent touches. Position-based (U-shaped) gives 40% to first and last, 20% to everything in between.

## Why it matters

Every model is wrong, but some are useful for specific questions. First-touch tells you which channels generate awareness. Last-touch tells you which channels close. Multi-touch tells you the whole story but requires data most companies don't have. The practical advice: pick one model, use it consistently, and compare trends over time rather than treating any single number as truth.

## How it works

Attribution models decide how credit for a conversion is split across the touchpoints that preceded it. Last-touch gives everything to the final click. First-touch rewards the channel that introduced the customer. Multi-touch models spread credit with set weights or data-driven attribution. Each model tells a different story of the same journey, and the choice shapes budget decisions, team bonuses, and channel strategy. The model is a policy, not a fact. You start by deciding which touches are eligible for credit and over what lookback window. Then the model's weights run over every converted path and split credit by its rules. What most teams miss is that changing the eligibility rules, whether view-through conversions count, whether email opens are touches, changes the output as much as changing the model itself.

## Practical uses

Attribution data drives channel budget allocation, campaign reporting, and performance comparisons. Teams pick a model that matches their funnel: long B2B cycles need multi-touch because last-touch will always credit the final demo. The mature approach is to run a couple of models side by side and treat the gap between them as the uncertainty to discuss. The model that rewards the behavior you want is the one to run.

## How to choose

Match model complexity to data quality. If conversion data is incomplete, the fanciest data-driven model just overfits the noise; a simple first- or last-touch model is more honest. Tools range from platform-native (Google Analytics) to dedicated suites like Rockerbox that fold in offline and walled-garden data. Before buying, ask what the tool does with the data it cannot see, because every attribution tool hides a guess there.

## The numbers

What changes in practice: moving from last-touch to data-driven attribution typically shifts credit toward mid-funnel touchpoints by 10-30% of converted revenue, which reorders your channel leaderboard without changing a single ad. The number that matters more is return on ad spend stability - models that swing more than about 20% month to month are telling you the sample is too thin, not that performance changed. Attribution tooling is priced per event volume or per monthly tracked users, and enterprise suites bundle it into an analytics contract, so pricing varies by vendor. The cheaper experiment is free: run one model's rules in a spreadsheet over a quarter of converted paths before you buy anything. If two models give you the same channel ranking, the tool will not change your decisions, only your vocabulary.

## Common mistakes

The recurring failure is treating model output as revenue truth and making irreversible budget cuts on a single model's word. The second is switching models mid-year, destroying comparability and turning reviews into methodology debates. The third is rewarding the channel that visits last rather than the one that builds demand. Attribution is a compass, not a receipt. Attribution models get confused with incrementality. A model reallocates credit inside observed journeys; incrementality testing measures what would have happened without the spend. Only the second tells you whether a channel caused revenue. Teams also confuse data-driven attribution with ground truth. It is still a model, trained on your conversion data, and it will favor the channels your tracking can see. If a channel disappears from the model when you change tracking, it was never proven, just measured.

## What changed with AI

AI search and agentic media buying broke click-based attribution further. When ChatGPT answers without a click and agents buy without referrers, the standard model sees nothing. Measurement is shifting from clicks to clean outcome events: signups, revenue, retention. The tools that survive are the ones that ingest warehouse-level outcome data rather than just ad-platform clicks. Attribution's future is outcome measurement, not click arithmetic.

## Tools in this space

## Related terms

[CRO](/glossary/cro/) · [CDP](/glossary/cdp/) · [Customer journey](/glossary/customer-journey/) · [DMP](/glossary/dmp/) · [First-party data](/glossary/first-party-data/)

Sources: [Attribution](https://www.attributionapp.com) · [Amplitude](https://amplitude.com) · [Mixpanel](https://mixpanel.com)

### Categories

[Analytics & Attribution](/categories/analytics/) [Best Analytics & Attribution tools](/best/marketing-analytics-tools/)

## See also

- [First-party data](/glossary/first-party-data/)
© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "DefinedTerm",
    "name": "Attribution Models (First-Touch, Last-Touch, Multi-Touch)",
    "description": "An attribution model is the rule that decides which marketing touchpoint gets credit for a conversion. First-touch credits the first interaction. Last-touch credits the final one before purchase. Linear splits credit equally. Time-decay gives more weight to recent touches. Position-based (U-shaped) gives 40% to first and last, 20% to everything in between.",
    "dateModified": "2026-09-28",
    "inDefinedTermSet": {
      "@type": "DefinedTermSet",
      "name": "Martech Glossary",
      "url": "https://martechsignal.com/glossary/"
    },
    "url": "https://martechsignal.com/glossary/marketing-attribution-models/"
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
        "name": "Glossary",
        "item": "https://martechsignal.com/glossary/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Attribution models",
        "item": "https://martechsignal.com/glossary/marketing-attribution-models/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
