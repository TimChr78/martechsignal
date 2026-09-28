# Attribution models

Attribution

AI-powered marketing attribution platform connecting ad spend to revenue

Amplitude

AI-powered digital analytics platform for product and marketing teams

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

[Browse all tools →](/tools/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

## Attribution Models (First-Touch, Last-Touch, Multi-Touch)

GLOSSARY

## Definition

An attribution model is the rule that decides which marketing touchpoint gets credit for a conversion. First-touch credits the first interaction. Last-touch credits the final one before purchase. Linear splits credit equally. Time-decay gives more weight to recent touches. Position-based (U-shaped) gives 40% to first and last, 20% to everything in between.

## Why it matters

Every model is wrong, but some are useful for specific questions. First-touch tells you which channels generate awareness. Last-touch tells you which channels close. Multi-touch tells you the whole story but requires data most companies don&#x27;t have. The practical advice: pick one model, use it consistently, and compare trends over time rather than treating any single number as truth.

## How it works

Attribution models decide how credit for a conversion is split across the touchpoints that preceded it. Last-touch gives everything to the final click. First-touch rewards the channel that introduced the customer. Multi-touch models spread credit with set weights or data-driven attribution. Each model tells a different story of the same journey, and the choice shapes budget decisions, team bonuses, and channel strategy. The model is a policy, not a fact. You start by deciding which touches are eligible for credit and over what lookback window. Then the model&#x27;s weights run over every converted path and split credit by its rules. What most teams miss is that changing the eligibility rules, whether view-through conversions count, whether email opens are touches, changes the output as much as changing the model itself.

## Practical uses

Attribution data drives channel budget allocation, campaign reporting, and performance comparisons. Teams pick a model that matches their funnel: long B2B cycles need multi-touch because last-touch will always credit the final demo. The mature approach is to run a couple of models side by side and treat the gap between them as the uncertainty to discuss. The model that rewards the behavior you want is the one to run.

## How to choose

Match model complexity to data quality. If conversion data is incomplete, the fanciest data-driven model just overfits the noise; a simple first- or last-touch model is more honest. Tools range from platform-native (Google Analytics) to dedicated suites like Rockerbox that fold in offline and walled-garden data. Before buying, ask what the tool does with the data it cannot see, because every attribution tool hides a guess there.

## The numbers

What changes in practice: moving from last-touch to data-driven attribution typically shifts credit toward mid-funnel touchpoints by 10-30% of converted revenue, which reorders your channel leaderboard without changing a single ad. The number that matters more is return on ad spend stability - models that swing more than about 20% month to month are telling you the sample is too thin, not that performance changed. Attribution tooling is priced per event volume or per monthly tracked users, and enterprise suites bundle it into an analytics contract, so pricing varies by vendor. The cheaper experiment is free: run one model&#x27;s rules in a spreadsheet over a quarter of converted paths before you buy anything. If two models give you the same channel ranking, the tool will not change your decisions, only your vocabulary.

## Common mistakes

The recurring failure is treating model output as revenue truth and making irreversible budget cuts on a single model&#x27;s word. The second is switching models mid-year, destroying comparability and turning reviews into methodology debates. The third is rewarding the channel that visits last rather than the one that builds demand. Attribution is a compass, not a receipt. Attribution models get confused with incrementality. A model reallocates credit inside observed journeys; incrementality testing measures what would have happened without the spend. Only the second tells you whether a channel caused revenue. Teams also confuse data-driven attribution with ground truth. It is still a model, trained on your conversion data, and it will favor the channels your tracking can see. If a channel disappears from the model when you change tracking, it was never proven, just measured.

## What changed with AI

AI search and agentic media buying broke click-based attribution further. When ChatGPT answers without a click and agents buy without referrers, the standard model sees nothing. Measurement is shifting from clicks to clean outcome events: signups, revenue, retention. The tools that survive are the ones that ingest warehouse-level outcome data rather than just ad-platform clicks. Attribution&#x27;s future is outcome measurement, not click arithmetic.

## Tools in this space

## Related terms

[CDP](/glossary/cdp/) · [DMP](/glossary/dmp/) · [CRO](/glossary/cro/) · [UTM parameters](/glossary/utm-parameters/) · [Customer journey](/glossary/customer-journey/)

### Categories

[Analytics &amp; Attribution](/categories/analytics/)

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
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/glossary/marketing-attribution-models/#webpage", "dateModified": "2026-09-28"}
```
