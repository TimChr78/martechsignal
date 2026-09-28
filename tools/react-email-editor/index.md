# React Email Editor pricing


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | The live Unlayer pricing page (fetched Sep 2026) publishes Free at $0 forever, Launch at $250 per month, Scale at $750, and Optimize at $2,000 with a full comparison table of per-tier limits and published credit pack rates such as 50,000 AI credits per $50 per month, leaving only Enterprise custom. |
| Feature depth | 7/10 | The React Email Editor tool page documents 15 built-in content blocks, custom tools and blocks, merge tags, display conditions, device previews, and HTML plus design JSON export, which covers the embedded editor baseline with real differentiators. |
| Integrations | 4/10 | tools.json lists React, Angular, Vue, vanilla JavaScript, a Cloud API, OpenAI, and Anthropic as the named connections with no marketplace documented, which sits between the few natives and broad catalog anchors. |
| AI capability | 8/10 | The React Email Editor tool page documents a shipped AI Assistant with chat-driven edits, AI image generation, and an AI Template Importer plus a beta MCP server with 14 documented tools and agent skills for Claude Code, Codex, and Cursor. |
| Openness | 5/10 | The React Email Editor tool page states exports return HTML and design JSON and the live Unlayer pricing page documents a Cloud API, but the MIT license covers only a thin wrapper around a hosted closed editor and self-hosting is Enterprise-only. |
| Operational maturity | 8/10 | The React Email Editor tool page reports wrapper versions 2.0.0 in July 2026 and 2.1.2 in August 2026 with real docs, and the live Unlayer pricing page adds SOC 2 Type II, a 99.9 percent uptime SLA, and Y Combinator backing. |


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; Paid plans start at $250/mo once past the free tier |
| &#10003; AI capabilities: AI Assistant chat editing |  |
| &#10003; Established community (5,219 GitHub stars) |  |
| &#10003; Native integrations include React, Angular, Vue (7 listed) |  |

**What is React Email Editor?**
Drag-n-Drop Email Editor Component for React.js. It ships with AI Assistant chat editing, 5,219 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does React Email Editor cost?**
React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers.

**Is React Email Editor a good self-hosted Email Marketing tool in 2026?**
The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor.

**Is React Email Editor really open source?**
The npm package is, under MIT, with about 5,200 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer&#x27;s CDN into an iframe and is governed by Unlayer&#x27;s plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier.

**What are Unlayer&#x27;s paid plans?**
Free at $0, Launch at $250 per month, Scale at $750 per month, and Optimize at $2,000 per month, with custom Enterprise pricing. Annual billing saves 10 percent across the paid tiers, every paid plan includes a 14-day trial, and add-on credit packs for AI, exports, inbox previews, and bandwidth start at $50 per month and top out at $2,000.

**Does React Email Editor support AMP emails?**
Yes, but only on the Optimize plan. You enable it with amp: true in the options, preview the AMP version inside the editor, and export AMP alongside standard HTML. The carousel block requires AMP in email designs, which is why it is a top-tier feature.

**Should I build my own editor on GrapesJS or MJML instead?**
If you need a fully open pipeline with no third-party dependency, yes, and you should budget for it: email client compatibility, a design schema, undo history, and preview tooling are the hard parts, and they are what the $250 to $2,000 per month buys. Unlayer has no MJML export, so a strict MJML workflow means rolling your own. Teams that can absorb that engineering cost should; product teams that cannot will ship faster with the wrapper.

- **Pricing:** Open Source
- **Category:** [Email Marketing](/categories/email-marketing/)
- **GitHub:** ★ 5219
- **API:** No
- **Last verified:** 2026-09-06

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

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Email Marketing](/categories/email-marketing/)
- React Email Editor
Re-check pending: pricing last verified 2026-09-06 (22 days ago).

## React Email Editor review (2026): pricing, AI features, verdict

Drag-n-Drop Email Editor Component for React.js

Email Marketing · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-06

[How we review](/methodology/) · No affiliate links

[Visit React Email Editor &#8594;](https://unlayer.com/)

## MartechSignal Score: 41/60

React Email Editor is a mature embedded builder with unusually clear pricing, per-tier limits, and published credit pack rates. The MIT license covers only a thin wrapper around a hosted editor, so teams that need a self-hosted builder should look elsewhere.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

React Email Editor is Unlayer&#x27;s official React component for embedding a drag-and-drop email builder inside your own application, and it pays to be precise about what the MIT license covers. The npm package is a thin wrapper whose single runtime dependency is a types package; the editor itself is a hosted service loaded from editor.unlayer.com into an iframe and unlocked with a projectId from Unlayer&#x27;s developer console. Install is npm install react-email-editor, then mount the component with an onReady callback and call loadDesign, saveDesign, or exportHtml on the ref. Version 2.0.0 (July 2026) modernized the build, requires React 16.8 or newer, and fixed a long-standing unmount leak; 2.1.2 in August 2026 fixed an SSR hydration bug that could leave a blank editor under the Next.js App Router. The hosted engine is a real builder, not a demo. It ships 15 built-in content blocks, custom tools and blocks, merge tags that accept any templating syntax, display conditions, device previews, undo and redo, and inbox previews across real email clients on the top plan. Pricing is public: a free tier, Launch at $250 per month for white-labeling, custom tools, and the Cloud API, Scale at $750 for custom blocks, collaboration, and smart merge tags, and Optimize at $2,000 for custom CSS, AMP, and inbox previews. AI features are real and metered. An AI Assistant on paid plans streams edits into the design from chat prompts, routes to OpenAI or Anthropic, and draws on a workspace credit balance; AI image generation reached Launch plans in August 2026. There is also a hosted MCP server in beta with 14 documented tools plus agent skills for Claude Code, Codex, and Cursor, unusual for an embedded editor and handy if your users work with AI assistants. The trade is control. Exports return HTML and a design JSON, there is no MJML output, AMP requires the top plan, and self-hosting is Enterprise-only.

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
- Import EmailEditor, hold a ref with useRef, and render &lt;EmailEditor ref={emailEditorRef} onReady={onReady} /&gt;. The published bundle carries a &#x27;use client&#x27; directive, so it runs in the Next.js App Router, and 2.1.2 fixed the SSR hydration mismatch that produced a silently blank editor there.
- Create a project in the Unlayer Developer Console. The component loads editor.unlayer.com/embed.js and needs a projectId to initialize, and the docs tell you to add your production domains under Project &gt; Settings &gt; Deployment so the builder only runs where you allow.
- Drive the editor through the three documented methods on the ref: loadDesign(object) to load saved JSON, saveDesign(callback) to get it back, and exportHtml(callback) to receive both the design JSON and the HTML.
- Enable AI with features: { ai: { enabled: true, assistant: true } } in the options prop plus a user id. The docs state that without the user id the assistant stays hidden and AI requests are rejected server-side.
- Angular and Vue teams do not need this package: Unlayer publishes separate open-source Angular Email Editor and Vue Email Editor components, plus a vanilla JS path through unlayer.init().
## Requirements

React 16.8 or newer and Node 18 or newer for the build, a Unlayer project with a projectId, and network access to editor.unlayer.com at runtime, because the editor renders in an iframe served from Unlayer&#x27;s CDN. Custom tools and blocks are configured through that hosted options model rather than in your bundle.

## Best for

SaaS teams that need a white-label drag-and-drop email builder inside their product and would rather buy the editor than spend months building and maintaining one. The React, Angular, and Vue components cover mixed stacks.

## Not for

Teams that need the editing engine on their own infrastructure, since on-premise deployment is Enterprise-only. The free tier omits white-labeling, and custom tools, custom blocks, custom CSS, collaboration, AMP, and inbox previews each sit behind a specific paid plan, so map the features you need to a tier before you commit.

## Review notes

Assessed from the GitHub repository, Unlayer&#x27;s docs, and the pricing page rather than an integration. The architecture is the first thing to understand: the npm package is a thin MIT-licensed wrapper whose single runtime dependency is a types package, while the editor is a hosted service loaded from editor.unlayer.com into an iframe and unlocked with a projectId.

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

Drag-n-Drop Email Editor Component for React.js. It ships with AI Assistant chat editing, 5,219 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers.

The fastest route to a real email builder inside a React app, and an honest one as long as you read the MIT license as covering the wrapper rather than the editor.

The npm package is, under MIT, with about 5,200 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer&#x27;s CDN into an iframe and is governed by Unlayer&#x27;s plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier.

Free at $0, Launch at $250 per month, Scale at $750 per month, and Optimize at $2,000 per month, with custom Enterprise pricing. Annual billing saves 10 percent across the paid tiers, every paid plan includes a 14-day trial, and add-on credit packs for AI, exports, inbox previews, and bandwidth start at $50 per month and top out at $2,000.

Yes, but only on the Optimize plan. You enable it with amp: true in the options, preview the AMP version inside the editor, and export AMP alongside standard HTML. The carousel block requires AMP in email designs, which is why it is a top-tier feature.

If you need a fully open pipeline with no third-party dependency, yes, and you should budget for it: email client compatibility, a design schema, undo history, and preview tooling are the hard parts, and they are what the $250 to $2,000 per month buys. Unlayer has no MJML export, so a strict MJML workflow means rolling your own. Teams that can absorb that engineering cost should; product teams that cannot will ship faster with the wrapper.

## Similar Tools

## Related reading

- [Claude SEO vs Codex SEO: same audit, pick the agent you already pay for](/blog/claude-seo-vs-codex-seo/)
- [Claude SEO vs Seonaut: which free SEO checker should you run](/blog/claude-seo-vs-seonaut/)
- [Deliverability in the AI-spam Era Is a Content Problem, Not an IT Problem](/blog/deliverability-ai-spam-content-problem/)
### Quick Facts

Related guides: [Ai Email Marketing Tools](/best/ai-email-marketing-tools) · [Open Source Marketing Tools](/best/open-source-marketing-tools)

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
    "dateModified": "2026-09-06",
    "datePublished": "2026-08-25",
    "offers": {
      "@type": "Offer",
      "price": 250,
      "priceCurrency": "USD",
      "url": "https://unlayer.com/pricing",
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
          "text": "Drag-n-Drop Email Editor Component for React.js. It ships with AI Assistant chat editing, 5,219 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does React Email Editor cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "React Email Editor has a free tier; paid plans start at $250/mo. Free tier for the builder. Launch $250/mo, Scale $750/mo, Optimize $2,000/mo, Enterprise custom. Annual billing saves 10% and paid plans include a 14-day trial. AI, export, inbox preview, and bandwidth credit packs run $50 to $2,000/mo. We last checked both ends of that split on 2026-09-06. The pricing section above shows what the free tier actually covers."
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
          "text": "The npm package is, under MIT, with about 5,200 GitHub stars. It is a thin React wrapper with one runtime dependency. The editor engine loads from Unlayer's CDN into an iframe and is governed by Unlayer's plans, so you can fork the wrapper but not the editor: on-premise deployment appears only in the Enterprise tier."
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
    "reviewBody": "React Email Editor is a mature embedded builder with unusually clear pricing, per-tier limits, and published credit pack rates. The MIT license covers only a thin wrapper around a hosted editor, so teams that need a self-hosted builder should look elsewhere.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/react-email-editor/#app",
      "name": "React Email Editor",
      "url": "https://martechsignal.com/tools/react-email-editor/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 41,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
