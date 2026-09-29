# Lead Scoring

HubSpot CRM

Free AI-powered CRM platform with sales, service, and marketing tools unified

Salesforce CRM

Enterprise CRM platform with Einstein AI for sales, service, and marketing teams

ActiveCampaign

AI-powered marketing automation and CRM for small to mid-size businesses

[Browse all tools →](/tools/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Lead Scoring

GLOSSARY

## Definition

Lead scoring assigns a numerical value to each prospect based on their likelihood to buy. Points accumulate for demographic fit (job title, company size) and behavioral signals (page visits, email opens, content downloads). Sales prioritizes the highest scores.

## Why it matters

Traditional lead scoring was a rules engine: +10 for visiting the pricing page, +5 for opening an email, -20 for unsubscribing. AI-based scoring replaced the hand-tuned rules with models trained on historical conversion data. The improvement is real but modest. The bigger issue is that most scoring models are trained on whatever data the CRM has, which is usually incomplete and biased toward the leads sales already liked.

## How it works

Lead scoring assigns a number to each lead based on behaviors and attributes. A score might add points for visiting the pricing page, more for requesting a demo, and subtract for bouncing from the last three emails. Attribute points handle fit: job title, company size, and industry match the ideal customer profile. When the score crosses a threshold, the lead becomes sales-ready and gets routed. The score is only as good as the model behind it. You run two scores in parallel. Fit scores grade the person and company against your ideal customer profile. Engagement scores track recency and frequency of meaningful actions, weighted so that a pricing-page visit outranks a newsletter open. Keep the two numbers visible separately, because a high-engagement bad-fit lead is a research project, not a sales opportunity.

## Practical uses

Scoring decides who sales calls and who stays in nurture. Without it, reps cherry-pick the loudest leads and marketing cannot prove its contribution. With it, the routing is automatic and the pipeline forecast has a basis. Teams typically calibrate the threshold against history: which scored leads booked meetings. The output is a handoff rule both teams can defend, which removes most of the friction in the MQL debate.

## How to choose

Start with explicit rules, not a machine-learned model. A transparent scorecard with ten weighted signals can be tuned by the team that owns it. Move to predictive scoring only after the rule-based version has data to learn from, and the model's decisions can still be explained. The tooling spans the CRM's built-in scorer, marketing automation platforms, and dedicated scoring products. Pick the one where the score is visible, because invisible scores get mistrusted.

## The numbers

Calibration check: in a healthy scoring model, roughly 25-40% of marketing-qualified leads convert to sales opportunities within 90 days. Below 20% means the threshold is too loose; above 50% usually means sales is quietly ignoring scores and cherry-picking. Track that one conversion rate quarterly instead of debating individual score weights - it catches drift faster than any model review. Scoring itself is rarely priced alone. It ships inside marketing automation platforms priced per contact or per seat, and standalone AI scoring tools price per record scored or per seat. All of it varies by vendor. The bigger number is the one sales and marketing must agree on: what score threshold converts a lead into a sales-accepted one, and how fast it must be worked.

## Common mistakes

The recurring failure is scoring activity without scoring fit, so marketing passes eager but irrelevant leads to sales. The second is never reviewing the model, letting the threshold drift from the market as seasons change. The third is scoring everything, including the bottom of the funnel, where a demo request should route instantly regardless of score. Scoring should make routing faster, not add a bureaucratic gate on ready buyers. Lead scoring gets confused with intent data. Intent data is third-party signal about what a company researches across the web; your score is built from what people do on your properties. One is a hint, the other is a record. Teams also confuse scoring with routing. A score decides priority; routing decides owner. If a demo request waits for a nightly score batch instead of routing instantly, the model is in the way.

## What changed with AI

Predictive scoring finds patterns humans miss: a lead that reads three specific pages in one session may behave like a closer even if the attribute score is low. AI can also re-score in real time as new signals arrive, which rules cannot do cheaply. The risk is opaque decisions. Model scores that cannot be explained produce sales teams that ignore them. Whatever the model, someone has to be able to say why a lead became a priority.

## Tools in this space

## Related terms

[ABM](/glossary/abm/) · [Agentic Marketing](/glossary/agentic-marketing/) · [AI Agent](/glossary/ai-agent/) · [Customer journey](/glossary/customer-journey/) · [CRM](/glossary/crm/)

## Seen in the wild

[Your Dashboard Can&#x27;t See AI Search: 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/) · [n8n + AI: The Open-Source Automation Engine](/blog/n8n-ai-open-source-automation/) · [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)

Sources: [HubSpot CRM](https://www.hubspot.com/products/crm) · [Salesforce CRM](https://www.salesforce.com/crm/) · [ActiveCampaign](https://www.activecampaign.com)

### Categories

[CRM](/categories/crm/) [Best CRM tools](/best/ai-crm-tools/) [Marketing Automation](/categories/marketing-automation/) [Best Marketing Automation tools](/best/ai-marketing-automation-tools/) [Automation strategy](/guides/workflow-automation-strategy/)

## See also

- [MQL / SQL](/glossary/mql-sql/)
© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "DefinedTerm",
    "name": "Lead Scoring",
    "description": "Lead scoring assigns a numerical value to each prospect based on their likelihood to buy. Points accumulate for demographic fit (job title, company size) and behavioral signals (page visits, email opens, content downloads). Sales prioritizes the highest scores.",
    "dateModified": "2026-09-28",
    "inDefinedTermSet": {
      "@type": "DefinedTermSet",
      "name": "Martech Glossary",
      "url": "https://martechsignal.com/glossary/"
    },
    "url": "https://martechsignal.com/glossary/lead-scoring/"
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
        "name": "Lead scoring",
        "item": "https://martechsignal.com/glossary/lead-scoring/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}]}
```
