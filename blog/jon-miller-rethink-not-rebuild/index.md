# Rethink, not rebuild: the replatform-for-AI trap


|  | Replatform "for AI" | Rethink in place |
| --- | --- | --- |
| **Trigger** | A launch made you feel behind | Contract is up and the platform can't run what you need |
| **Cost center** | A software swap that becomes a data plumbing project | No migration; budget stays on programs |
| **Data risk** | Buying groups, intent, and history get copied out | Stays where it is |
| **What AI arrives as** | A platform you must repopulate | A layer: MCP tool surfaces, vendor-shipped reasoning |

TC **[Tim Christensen](/authors/tim-christensen/)**

Verdict: the replatform pitch is a trap

MARKETING AUTOMATION · AI AGENTS · 6 MIN

## Rethink, not rebuild: Jon Miller and the replatform-for-AI trap

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Rethink, not rebuild: Jon Miller and the replatform-for-AI trap

OCT 01, 2026

Filed under [Marketing Automation](/categories/marketing-automation/)

Jon Miller co-founded Marketo, then founded Engagio, the account-based marketing platform Demandbase bought in 2020 ([Demandbase press release](https://www.demandbase.com/press-release/demandbase-acquires-engagio/)). This week he came back to the category he helped create. Phave, his new platform, launched September 23, 2026 after two years in stealth, and it already powers marketing operations at 10 companies, Miller told [MarTech](https://martech.org/marketo-co-founder-jon-miller-rethinks-b2b-marketing-automation-for-the-ai-age/).

His diagnosis of legacy marketing automation is dead on. The cure on offer is another story.

## What Phave actually changes

Most of the launch coverage describes an AI product. The MarTech interview describes an architecture.

Phave treats individual contacts, target accounts, and multi-person buying groups as first-class objects, each with its own intent scores and tailored buyer journeys. It replaces static triggers with AI reasoning. Campaigns become "playlists": the tactics are the songs, and the platform picks the optimal order and timing for each person rather than running a flowchart someone drew. It acts as a traffic controller so two teams cannot email the same account on the same day. And it exposes 319 tools through the Model Context Protocol, so agents can drive it directly instead of somebody clicking through dashboards.

<!- BREAK ->

## Miller's argument is with rules, not with your MAP

Miller told MarTech:

> I like to say rules are good at what must be true, but they can't handle ambiguity, and they can't provide judgment about what is best. And the reality is B2B buying is ambiguous and complex, and doesn't lend itself very well to rules.

The frustration is real, and it is not confined to Marketo. A campaign analyst at a major Australian bank posted in r/MarketingAutomation [last week](https://www.reddit.com/r/MarketingAutomation/comments/1wm8q1c/switching_from_unica_should_i_upskill_in/): their stack is "mainly SQL + Unica," they call Unica "pretty outdated at this point," and they are weighing Salesforce Marketing Cloud, Adobe Campaign, and Pega for their next role. When someone who runs campaigns on a legacy platform for a living describes it that bluntly, the rules problem has outlived the platform.

**Rules were never the enemy. Rules were the constraint of the era.** Map a rigid buyer journey once and let the machine execute it, because a human cannot send a million individually-timed messages by hand. A rules engine was the best available encoding of judgment. LLMs changed the economics of that encoding. That is the real story in Phave: reasoning finally got cheap enough to replace rules, and the field is racing to rebuild products around that fact.

## Why "replatform for AI" is the trap

You will read this launch as a to-do item. That reading is the trap.

Salesforce spent its Dreamforce 2026 health keynote making the same argument from the other side. Their advice for teams under pressure to modernize ([Salesforce blog](https://www.salesforce.com/blog/3-must-haves-for-scaling-agentic-ai-in-health/)): "For years, the answer to every new problem has been another system, another login, or another workflow." Trust, context, and action are properties of how well the platform you already own is used, not line items on a purchase order. Their own numbers say the same. UCLA Health ran 75,000+ patient interactions in six months through an Agentforce-powered front door with a 4.6/5 rating, answers in under 60 seconds, and 40% of conversations directly supporting faster access to care. Those figures are Salesforce's own reporting, so treat them accordingly. The instructive part is the shape, not the decimals: agent wins reported on the old pattern of platform adoption, not on net-new purchases.

That is the contrarian reading of this launch. Vendors need the AI era to require new software, because they sell software. Buyers do not. Three lines of evidence say the replatform pitch deserves your skepticism:

1. The cost center is your data, not the platform. Migrations are billed as software swaps and costed as data plumbing projects. The CDP wave taught this lesson expensively, and the warehouse-native stack is the correction ([our CDP reckoning post](/blog/cdp-reckoning-warehouse-native/), [our Fivetran post](/blog/you-dont-need-new-data-stack-fivetran/)). Buying groups, intent, and history: that is where the switching cost lives, and every vendor wants to take a copy of it. 2. Agents attack the reason replatforms were scary. The replatform-for-AI pitch relies on integration risk staying high, because that is what a migration budget is priced against. The same MCP pattern that lets agents drive Phave lets them drive the platform you already own. Phave itself is the proof: 319 MCP tools means agents operate it, and other platforms are racing to match that ([why your stack doesn't need another AI tool](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/)). 3. Reasoning-over-rules is coming to your current platform anyway. If Miller is right that rules fail at ambiguity, incumbents have to respond, and fast. Salesforce is already doing it. Adobe is pushing AJO and Real-Time CDP as a Campaign successor. The AI reasoning layer is arriving as a layer, not only as a platform swap.

Miller's diagnosis is right and his cure is optional. If your MAP runs your programs and the complaints are the rules layer's rigidity, the reasoning layer is likely to arrive where you already are, through MCP tool surfaces and vendor-shipped reasoning, and the data you would risk in a migration is the asset every vendor actually wants.

## If you do replatform, do it for one reason

None of this makes Phave wrong. Its architectural ideas are genuinely good, and someone has to build the reasoning-native MAP. Phave's own site says it replaces Marketo, Pardot, Eloqua, and HubSpot, a bold scope claim from a 10-customer company, and there is no public pricing. Miller said early adopters report building campaigns two to three times faster, which is a vendor claim from a two-year stealth period, so hold it lightly.

If your contract is up and your platform cannot run the campaigns you actually need, replatform on the merits. Compare the candidates on their own pages: [Adobe Marketo Engage](/tools/adobe-marketo/), [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/), [HubSpot Marketing Hub](/tools/hubspot-marketing-hub/), [Adobe Campaign](https://business.adobe.com/products/campaign.html), [Adobe Journey Optimizer](https://business.adobe.com/products/journey-optimizer.html), [Pega](https://www.pega.com), and the new entrant, [Phave](https://phave.com). Replatform because the economics and the capability fit, the way the Sydney analyst is doing it: deliberately, comparing [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) and Adobe's stack against real requirements.

But do not replatform *for* AI. If the stack you have runs your programs, the AI you are being sold arrives as a layer on top of it. Miller spent his career proving that a new platform can reshape a category. The Sydney analyst's blunt Unica post shows the old ones still run the programs. Both are true, and the honest middle between them is where most teams should stay.

*Tools linked in this post: [Adobe Marketo Engage](/tools/adobe-marketo/) | [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) | [HubSpot Marketing Hub](/tools/hubspot-marketing-hub/) | [HubSpot CRM](/tools/hubspot-crm/)*

## Related reading

- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Salesforce putting Claude inside Commerce Cloud is the quiet admission Agentforce isn't enough](/blog/salesforce-claude-commerce-cloud-agentforce/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
## Related tools

- [Bloomreach](/tools/bloomreach/) - AI-powered commerce experience platform with search, personalization, and CDP
- [Braze](/tools/braze/) - Customer engagement platform with AI-powered real-time messaging across channels
- [Laudspeaker](/tools/laudspeaker/) - Open-source customer engagement and product onboarding platform, alternative to Braze
## Comparison guides

- [Best AI Marketing Automation tools (2026): 8 compared](/best/ai-marketing-automation-tools/)
- [Best Zapier alternatives (2026)](/alternatives/zapier/)
## Glossary terms

- [DSP](/glossary/dsp/)
- [CDP](/glossary/cdp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [OpenOutreach](/tools/openoutreach/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)


```json
{
  "@context": "https://schema.org",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelectors": [
      "h1",
      "article h2"
    ]
  },
  "@type": "BlogPosting",
  "headline": "Rethink, not rebuild: Jon Miller and the replatform-for-AI trap",
  "description": "Jon Miller co-founded Marketo, then founded Engagio, the account-based marketing platform Demandbase bought in 2020 (Demandbase press release). This week.",
  "author": {
    "@type": "Person",
    "@id": "https://martechsignal.com/authors/tim-christensen/#person",
    "name": "Tim Christensen",
    "url": "https://martechsignal.com/authors/tim-christensen/"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://martechsignal.com/#organization",
    "name": "MartechSignal",
    "url": "https://martechsignal.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://martechsignal.com/logo.png"
    }
  },
  "datePublished": "2026-10-01",
  "dateModified": "2026-10-02",
  "mainEntityOfPage": "https://martechsignal.com/blog/jon-miller-rethink-not-rebuild/",
  "image": {
    "@type": "ImageObject",
    "url": "https://martechsignal.com/og/jon-miller-rethink-not-rebuild.png",
    "width": 1200,
    "height": 630
  },
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 1272,
  "articleSection": "marketing-automation"
}
```

```json
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
      "name": "Blog",
      "item": "https://martechsignal.com/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Rethink, not rebuild: Jon Miller and the replatform-for-AI trap",
      "item": "https://martechsignal.com/blog/jon-miller-rethink-not-rebuild/"
    }
  ]
}
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/blog/jon-miller-rethink-not-rebuild/", "breadcrumb": {"@id": "https://martechsignal.com/blog/jon-miller-rethink-not-rebuild/#breadcrumb"}, "dateModified": "2026-10-02"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
