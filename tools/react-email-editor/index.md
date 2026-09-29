# React Email Editor pricing


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 7/10 | Free builder tier, then Launch $250/mo, Scale $750/mo, Optimize $2,000/mo published with 10% annual saving and 14-day trials (the vendor pricing page: [pricing page](https://unlayer.com/pricing), verified 2026-09-06). |
| Feature depth | 6/10 | Drag-and-drop editing across four frameworks plus template import covers the component job; the AI editing and generation layers sit on the paid plans (vendor documentation: [vendor site](https://unlayer.com/), verified 2026-09-28). |
| Integrations | 5/10 | React, Angular, Vue and vanilla JS embeds, a Cloud API and OpenAI and Anthropic connections are documented (vendor documentation: [vendor site](https://unlayer.com/), verified 2026-09-28). |
| AI capability | 7/10 | AI chat editing, image generation, template import and an Unlayer MCP server with Agent Skills for coding agents (vendor documentation: [vendor site](https://unlayer.com/), verified 2026-09-28). |
| Openness | 8/10 | MIT-licensed core; the hosted AI services are what you pay for (the source repository: [repository](https://github.com/unlayer/react-email-editor), verified 2026-09-28). |
| Operational maturity | 6/10 | A commercial component vendor with priced tiers and trials behind the OSS core (vendor documentation: [vendor site](https://unlayer.com/), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Paid plans start at $250/mo once past the free tier |
| ✓ AI capabilities: AI Assistant chat editing |  |
| ✓ Active public repository (5,231 GitHub stars counted at last check) |  |
| ✓ Native integrations include React, Angular, Vue (7 listed) |  |

**What is React Email Editor?**
React Email Editor: Drag-n-Drop Email Editor Component for React.js. React Email Editor ships with AI Assistant chat editing. The public repository carries 5,231 stars.

**How much does React Email Editor cost?**
React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers."

**Is React Email Editor a good self-hosted Email Marketing tool in 2026?**
The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor.

**Is React Email Editor really open source?**
The npm package is, under MIT, with about 5,231 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer's CDN into an iframe and is governed by Unlayer's plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier.

**What are Unlayer's paid plans?**
Free at $0, Launch at $250 per month, Scale at $750 per month, and Optimize at $2,000 per month, with custom Enterprise pricing. Annual billing saves 10 percent across the paid tiers, every paid plan includes a 14-day trial, and add-on credit packs for AI, exports, inbox previews, and bandwidth start at $50 per month and top out at $2,000.

**Does React Email Editor support AMP emails?**
Yes, but only on the Optimize plan. You enable it with amp: true in the options, preview the AMP version inside the editor, and export AMP alongside standard HTML. The carousel block requires AMP in email designs, which is why it is a top-tier feature.

**Should I build my own editor on GrapesJS or MJML instead?**
If you need a fully open pipeline with no third-party dependency, yes, and you should budget for it: email client compatibility, a design schema, undo history, and preview tooling are the hard parts, and they are what the $250 to $2,000 per month buys. Unlayer has no MJML export, so a strict MJML workflow means rolling your own. Teams that can absorb that engineering cost should; product teams that cannot will ship faster with the wrapper.

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 5231
- **API:** No
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-06

**Verdict:** React Email Editor is a tool in Email Marketing with free and open source. The catalog documents 5 AI features, 7 integrations and a self-hosting path. We reviewed it from vendor documentation on 2026-09-06. This is a desk review, not a hands-on test. Desk-reviewed

Resend

Developer-first email API built around React Email, batch sending, and agent tooling

Customer.io

Data-driven messaging platform for automated email, push, SMS, and in-app messages

Codex SEO

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

Notifuse

Open-source, self-hosted email marketing platform with BYO-ESP and LLM integrations

BillionMail

Open-source mail server, newsletter, and email marketing platform, fully self-hosted and free

[More Email Marketing Tools →](/categories/email-marketing/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- React Email Editor
Re-check pending: pricing last verified 2026-09-06 (23 days ago).

## React Email Editor review (2026): pricing, AI features, verdict

Drag-n-Drop Email Editor Component for React.js

Email Marketing · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-29

[Visit React Email Editor →](https://unlayer.com/)

[How we review](/methodology/) · No affiliate links

[Visit React Email Editor →](https://unlayer.com/)

## MartechSignal Score: 39/60

The builder is free and MIT-licensed, which is the right way to sell a component. The hosted AI features land at $250/mo and up, so the real cost is where you draw the line.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

React Email Editor is Unlayer's official React component for embedding a drag-and-drop email builder inside your own application, and it pays to be precise about what the MIT license covers. The npm package is a thin wrapper whose single runtime dependency is a types package; the editor itself is a hosted service loaded from editor.unlayer.com into an iframe and unlocked with a projectId from Unlayer's developer console. Install is npm install react-email-editor, then mount the component with an onReady callback and call loadDesign, saveDesign, or exportHtml on the ref. Version 2.0.0 (July 2026) modernized the build, requires React 16.8 or newer, and fixed a long-standing unmount leak; 2.1.2 in August 2026 fixed an SSR hydration bug that could leave a blank editor under the Next.js App Router. The hosted engine is a real builder, not a demo. It ships 15 built-in content blocks, custom tools and blocks, merge tags that accept any templating syntax, display conditions, device previews, undo and redo, and inbox previews across real email clients on the top plan. Pricing is public: a free tier, Launch at $250 per month for white-labeling, custom tools, and the Cloud API, Scale at $750 for custom blocks, collaboration, and smart merge tags, and Optimize at $2,000 for custom CSS, AMP, and inbox previews. AI features are real and metered. An AI Assistant on paid plans streams edits into the design from chat prompts, routes to OpenAI or Anthropic, and draws on a workspace credit balance; AI image generation reached Launch plans in August 2026. There is also a hosted MCP server in beta with 14 documented tools plus agent skills for Claude Code, Codex, and Cursor, unusual for an embedded editor and handy if your users work with AI assistants. The trade is control. Exports return HTML and a design JSON, there is no MJML output, AMP requires the top plan, and self-hosting is Enterprise-only.

React Email Editor homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI Assistant chat editing
- AI image generation
- AI Template Importer
- Unlayer MCP server (beta)
- Agent Skills for Claude Code, Codex, and Cursor
## Key Integrations

- React
- Angular
- Vue
- Vanilla JavaScript
- Cloud API
- OpenAI
- Anthropic
## Pricing

React Email Editor is free to self-host under the MIT licence, paid plans start at $250/mo as of 2026-09.

Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo.

Current plans and limits live on the [React Email Editor pricing page](https://unlayer.com/pricing).

## How to install

- Install the wrapper: npm install react-email-editor --save. Version 2.0.0 (July 2026) raised the floor to React 16.8 or newer and Node 18 or newer.
- Import EmailEditor, hold a ref with useRef, and render <EmailEditor ref={emailEditorRef} onReady={onReady} />. The published bundle carries a 'use client' directive, so it runs in the Next.js App Router, and 2.1.2 fixed the SSR hydration mismatch that produced a silently blank editor there.
- Create a project in the Unlayer Developer Console. The component loads editor.unlayer.com/embed.js and needs a projectId to initialize, and the docs tell you to add your production domains under Project > Settings > Deployment so the builder only runs where you allow.
- Drive the editor through the three documented methods on the ref: loadDesign(object) to load saved JSON, saveDesign(callback) to get it back, and exportHtml(callback) to receive both the design JSON and the HTML.
- Enable AI with features: { ai: { enabled: true, assistant: true } } in the options prop plus a user id. The docs state that without the user id the assistant stays hidden and AI requests are rejected server-side.
- Angular and Vue teams do not need this package: Unlayer publishes separate open-source Angular Email Editor and Vue Email Editor components, plus a vanilla JS path through unlayer.init().
## Requirements

React 16.8 or newer and Node 18 or newer for the build, a Unlayer project with a projectId, and network access to editor.unlayer.com at runtime, because the editor renders in an iframe served from Unlayer's CDN. Custom tools and blocks are configured through that hosted options model rather than in your bundle.

## Best for

SaaS teams that need a white-label drag-and-drop email builder inside their product and would rather buy the editor than spend months building and maintaining one. The React, Angular, and Vue components cover mixed stacks.

## Not for

Teams that need the editing engine on their own infrastructure, since on-premise deployment is Enterprise-only. The free tier omits white-labeling, and custom tools, custom blocks, custom CSS, collaboration, AMP, and inbox previews each sit behind a specific paid plan, so map the features you need to a tier before you commit.

## Review notes

Assessed from the GitHub repository, Unlayer's docs, and the pricing page rather than an integration. The architecture is the first thing to understand: the npm package is a thin MIT-licensed wrapper whose single runtime dependency is a types package, while the editor is a hosted service loaded from editor.unlayer.com into an iframe and unlocked with a projectId.

The component API is small and stable. Three documented methods cover the data path: loadDesign, saveDesign, and exportHtml, which returns both the design JSON and the HTML. Version 2.0.0 in July 2026 modernized the build and requires React 16.8 or newer, and 2.1.2 in August 2026 fixed an SSR hydration bug that could render a blank editor in the Next.js App Router.

Plan against the pricing tiers rather than the free tier. White-labeling starts at Launch, custom blocks and collaboration at Scale, and custom CSS, AMP, and inbox previews at Optimize, with AI metered through a workspace credit balance. The docs do not describe how Unlayer branding appears on free-plan exports, so test that path before committing to it.

## Verdict

The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor.

## Pros and cons

## Related concepts

- [Email sequence](/glossary/email-sequence/)
- [Deliverability](/glossary/deliverability/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

React Email Editor: Drag-n-Drop Email Editor Component for React.js. React Email Editor ships with AI Assistant chat editing. The public repository carries 5,231 stars.

React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers."

The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor.

The npm package is, under MIT, with about 5,231 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer's CDN into an iframe and is governed by Unlayer's plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier.

Free at $0, Launch at $250 per month, Scale at $750 per month, and Optimize at $2,000 per month, with custom Enterprise pricing. Annual billing saves 10 percent across the paid tiers, every paid plan includes a 14-day trial, and add-on credit packs for AI, exports, inbox previews, and bandwidth start at $50 per month and top out at $2,000.

Yes, but only on the Optimize plan. You enable it with amp: true in the options, preview the AMP version inside the editor, and export AMP alongside standard HTML. The carousel block requires AMP in email designs, which is why it is a top-tier feature.

If you need a fully open pipeline with no third-party dependency, yes, and you should budget for it: email client compatibility, a design schema, undo history, and preview tooling are the hard parts, and they are what the $250 to $2,000 per month buys. Unlayer has no MJML export, so a strict MJML workflow means rolling your own. Teams that can absorb that engineering cost should; product teams that cannot will ship faster with the wrapper.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Most of your marketing AI agents should be if/then](/blog/determinism-audit/)
- [What a free SEO audit replaces in your Semrush stack, and what it does not](/blog/what-free-seo-audit-replaces/)
## Also featured in

- [Best AI Email Marketing tools (2026): 8 compared](/best/ai-email-marketing-tools/) — Developer teams that want email templates versioned as code
### Quick Facts

Related guides: [Ai Email Marketing Tools](/best/ai-email-marketing-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/react-email-editor/#app",
    "name": "React Email Editor",
    "description": "Drag-n-Drop Email Editor Component for React.js",
    "image": "https://martechsignal.com/og/tools/react-email-editor.png",
    "url": "https://martechsignal.com/tools/react-email-editor/",
    "sameAs": [
      "https://unlayer.com/"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/react-email-editor/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-29",
    "datePublished": "2026-08-25",
    "offers": [
      {
        "@type": "Offer",
        "price": 0,
        "priceCurrency": "USD",
        "url": "https://unlayer.com/pricing",
        "priceValidUntil": "2026-12-31"
      },
      {
        "@type": "Offer",
        "price": 250,
        "priceCurrency": "USD",
        "url": "https://unlayer.com/pricing",
        "priceValidUntil": "2026-12-31"
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
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Email Marketing",
        "item": "https://martechsignal.com/categories/email-marketing/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "React Email Editor",
        "item": "https://martechsignal.com/tools/react-email-editor/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is React Email Editor?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "React Email Editor: Drag-n-Drop Email Editor Component for React.js. React Email Editor ships with AI Assistant chat editing. The public repository carries 5,231 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does React Email Editor cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers.\""
        }
      },
      {
        "@type": "Question",
        "name": "Is React Email Editor a good self-hosted Email Marketing tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor."
        }
      },
      {
        "@type": "Question",
        "name": "Is React Email Editor really open source?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The npm package is, under MIT, with about 5,231 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer's CDN into an iframe and is governed by Unlayer's plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier."
        }
      },
      {
        "@type": "Question",
        "name": "What are Unlayer's paid plans?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Free at $0, Launch at $250 per month, Scale at $750 per month, and Optimize at $2,000 per month, with custom Enterprise pricing. Annual billing saves 10 percent across the paid tiers, every paid plan includes a 14-day trial, and add-on credit packs for AI, exports, inbox previews, and bandwidth start at $50 per month and top out at $2,000."
        }
      },
      {
        "@type": "Question",
        "name": "Does React Email Editor support AMP emails?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, but only on the Optimize plan. You enable it with amp: true in the options, preview the AMP version inside the editor, and export AMP alongside standard HTML. The carousel block requires AMP in email designs, which is why it is a top-tier feature."
        }
      },
      {
        "@type": "Question",
        "name": "Should I build my own editor on GrapesJS or MJML instead?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "If you need a fully open pipeline with no third-party dependency, yes, and you should budget for it: email client compatibility, a design schema, undo history, and preview tooling are the hard parts, and they are what the $250 to $2,000 per month buys. Unlayer has no MJML export, so a strict MJML workflow means rolling your own. Teams that can absorb that engineering cost should; product teams that cannot will ship faster with the wrapper."
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
    "reviewBody": "The builder is free and MIT-licensed, which is the right way to sell a component. The hosted AI features land at $250/mo and up, so the real cost is where you draw the line.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/react-email-editor/#app",
      "name": "React Email Editor",
      "url": "https://martechsignal.com/tools/react-email-editor/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 39,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
