# Make vs Zapier (2026): pricing and AI


| Tool | Starts at | Pick it when |
| --- | --- | --- |
| Make | Freemium | You want the most visual scenario builder and a generous free tier to prototype in. |
| Zapier | Freemium | You want the deepest app catalog and the least thinking about edge cases. |


| Dimension | Make | Zapier |
| --- | --- | --- |
| Pricing | Freemium | Freemium |
| Open source | no | no |
| Integrations listed | not listed | 8 listed: Salesforce, HubSpot, Slack, Microsoft Dynamics 365 (+4 more) |
| Public API | yes | yes |


| Scenario | Make | Zapier |
| --- | --- | --- |
| Cost basis | Operations per month (credits) | Successful tasks |
| Free tier | 1,000 credits per month, 2 active scenarios | 100 tasks per month, 2-step Zaps |
| Entry paid | Core $9/mo for 10,000 credits (annual billing) | Professional from $19.99/mo |
| At 10K tasks/mo | Core covers 10K credits at $9/mo with annual billing. Watch the credit multiplier: some modules consume more than one credit per run. | Volume is a slider above the published starting prices, so 10K tasks costs more than the $69/mo Team entry. Get the quote in writing before comparing. |
| Checked | 2026-09-27 | 2026-09-27 |

- **Pick Make if:** Pick Make if you want a hosted platform the vendor runs for you, and ai agents and ai workflow suggestions matters to your team, starting free.
- **Pick Zapier if:** Pick Zapier if you want a hosted platform the vendor runs for you, and ai workflow builder and ai data formatting matters to your team, starting free.

[Workflow Automation](/categories/workflow-automation/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

## Make vs Zapier (2026): pricing, AI features, verdict

Make and Zapier end up on the same shortlist. Make, the platform formerly known as Integromat, sits between Zapier's simplicity and n8n's depth. Zapier is the automation platform most people mean when they say they want to connect two tools without writing code.

Most decisions here come down to price and fit. The figures below are the catalog's last verified numbers, each dated on the tool page. This page is desk research rather than a hands-on test.

Both platforms now sell AI features on top of the same plumbing: triggers, actions, and a scheduler between them. The price gap and the credit-versus-task metering decide more deals than any feature list, so the volume table below is the part to read twice.

The pair pages beside this one (n8n vs Zapier, and the three-way) carry the wider automation-platform picture; here we stay on the two visual builders that fight for the same buyer.

## Make vs Zapier: the quick decision

The pair pages carry the same evidence in depth: [n8n vs Zapier](/vs/n8n-vs-zapier/).

[Make assessment](/tools/make/) · [Zapier assessment](/tools/zapier/)

Make: [Official site](https://www.make.com) · [Pricing](https://www.make.com/en/pricing)

Zapier: [Official site](https://zapier.com) · [Pricing](https://zapier.com/pricing)

Make

Zapier

## Priced at volume

Cost picture at 10K automation tasks per month. All figures checked 2026-09-27 on vendor pricing pages.

## Positioning

**Make:** Make, the platform formerly known as Integromat, sits between Zapier's simplicity and n8n's depth. Founded in Prague in 2012 and acquired by Celonis in 2020, it is where technical marketing teams land when a linear editor stops being enough: scenarios are drawn as a graph, so branching, looping, and error handling are visible rather than buried in configuration. Billing changed in August 2026, when credits replaced operations as the unit of account. It was founded in 2012.

**Zapier:** Zapier is the automation platform most people mean when they say they want to connect two tools without writing code. It lists more than 9,000 app integrations, still the widest catalogue in this directory, and the niche martech tools that lack an n8n node or a Make module usually still have a Zapier integration. It was founded in 2011.

## Pricing

**Make:** It starts free, and free (1,000 credits/mo, 2 active scenarios); Core $9/mo, Pro $16/mo, Teams €29/mo, each for 10,000 credits/mo with a slider up to 8M+; annual billing saves 15% or more; Enterprise custom (verified 2026-09-07).

**Zapier:** It starts free, and free (100 tasks/mo, 2-step Zaps); Professional $19.99/mo (annual); Team $69/mo (annual) (verified 2026-09-07).

## Deployment and self-hosting

**Make:** Hosted only. The vendor runs the infrastructure and bills by seats, tasks, or usage.

**Zapier:** Hosted only. The vendor runs the infrastructure and bills by seats, tasks, or usage.

## AI features

**Make:** 5 documented AI features, including ai agents, ai workflow suggestions, ai data transformation, ai content generation, and ai error handling.

**Zapier:** 5 documented AI features, including ai workflow builder, ai data formatting, ai chatbot builder, and ai agents.

## Integrations

**Make:** 8 listed integrations, including slack, gmail, salesforce, hubspot, and shopify.

**Zapier:** 8 listed integrations, including slack, gmail, salesforce, hubspot, and shopify.

## Lock-in and exit cost

**Make:** Scenarios export as JSON blueprints you can archive. Run history stays with the vendor, so keep your own records if audit trails matter to you.

**Zapier:** Zapier holds the logic and the history. Exports cover documentation at best, so leaving means re-implementing every active Zap wherever you land.

## Decision notes

**Make:** Pick Make if you want a hosted platform the vendor runs for you, and ai agents and ai workflow suggestions matters to your team, starting free.

**Zapier:** Pick Zapier if you want a hosted platform the vendor runs for you, and ai workflow builder and ai data formatting matters to your team, starting free.

## Migration cost

Scenario to Zap translation is mechanical on the simple flows and stubborn on the clever ones. Routers map to Paths, iterators and aggregators often need a rethink, and Make's tolerance for loose JSON means error handling that worked for years can fail on day one in Zapier.

The reverse move has its own tax. Zapier's formatter steps get rebuilt as Make functions, and any code step becomes a Make module or a call to your own endpoint. Exports cover the structure, not the run history, so keep a copy of the old platform until finance has signed off on the numbers.

Switching costs land in the connectors, not the canvas. Triggers and actions map across all three roughly one to one, so a careful export and rebuild of a 20-step workflow takes an afternoon. The expensive parts are the steps that used a vendor-specific helper: JSON construction in n8n, iterators and aggregators in Make, formatter steps in Zapier. Budget a day per workflow that leans on those.

## When neither is the right answer

None of the three is right when your automation work is mostly custom code with a scheduler: a worker service and a queue will cost less and break less than any of them. They are also the wrong tools for one-way data pipelines, where an ETL product fits better than a workflow builder.

## Who should pick which

## When does Make beat Zapier?

When builders outgrow a linear editor. Make offers branching, looping and scenario-level control with AI agents and workflow suggestions, plus cheaper runs at moderate volume for technical marketing teams.

## When does Zapier keep the deal?

When the catalog decides it: the largest app library, the least setup per workflow, and an AI workflow builder for teams that never want to see a branch node. Niche integrations working this week is Zapier's home turf.

## Which one is cheaper at scale?

Make at moderate volume, where its runs price below Zapier tasks. At very high volume both lose to self-hosted n8n, which is exactly the three-way comparison this site carries separately.

Prices and features here come from each vendor's own published materials as catalogued on the tool pages. Read [how we evaluate](/methodology/) or download the [machine-readable catalog](/catalog-tools.json).

Last verified 2026-09-28.

## Browse the hubs behind this comparison

**Guide:** [MCP and agent protocols](/guides/mcp-agent-protocols/) · [automation strategy](/guides/workflow-automation-strategy/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "@id": "https://martechsignal.com/vs/make-vs-zapier/#article",
    "datePublished": "2026-09-27",
    "dateModified": "2026-09-28",
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
    "name": "Make vs Zapier (2026): pricing, AI features, verdict",
    "url": "https://martechsignal.com/vs/make-vs-zapier/",
    "inLanguage": "en",
    "headline": "Make vs Zapier (2026): pricing, AI features, verdict",
    "image": "https://martechsignal.com/og/vs/make-vs-zapier.png",
    "about": [
      {
        "@id": "https://martechsignal.com/tools/make/#app"
      },
      {
        "@id": "https://martechsignal.com/tools/zapier/#app"
      }
    ],
    "mainEntity": {
      "@type": "ItemList",
      "name": "Make vs Zapier",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Make",
          "item": {
            "@type": "SoftwareApplication",
            "@id": "https://martechsignal.com/tools/make/#app",
            "url": "https://martechsignal.com/tools/make/",
            "name": "Make"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Zapier",
          "item": {
            "@type": "SoftwareApplication",
            "@id": "https://martechsignal.com/tools/zapier/#app",
            "url": "https://martechsignal.com/tools/zapier/",
            "name": "Zapier"
          }
        }
      ]
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
        "name": "Head-to-head comparisons",
        "item": "https://martechsignal.com/vs/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Make vs Zapier (2026): pricing, AI features, verdict",
        "item": "https://martechsignal.com/vs/make-vs-zapier/"
      }
    ]
  }
]
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/vs/make-vs-zapier/", "dateModified": "2026-09-29"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
