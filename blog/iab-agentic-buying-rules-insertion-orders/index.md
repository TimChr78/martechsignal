# IAB agentic buying rules land before ad stacks can honor them


|  | What AAMP 3.0 assumes | What your stack runs today |
| --- | --- | --- |
| **Brief issued** | Machine-readable, agent-consumable | Email, doc, deck, or a form in a UI |
| **Proposal discovery** | Agents query standardized ad product feeds | A planner checks publisher sites and rate cards by hand |
| **Comparison and negotiation** | Agent compares proposals against the brief, negotiates terms | Threads of email, redlined PDFs, phone calls |
| **Commitment to buy** | Deal ID flows into existing execution standards | A human signs the insertion order |
| **Measurement terms** | Modular standard contract, adaptable per deal | Every measurement agreement negotiated from scratch |

TC **[Tim Christensen](/authors/tim-christensen/)**

✓ Direction: right. Timeline: not yours.

DIGITAL ADVERTISING · AI AGENTS · 8 MIN

## Your insertion orders were written for humans: the IAB&#x27;s agentic buying rules land before your ad stack can honor them

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Your insertion orders were written for humans: the IAB's agentic buying rules land before your ad stack can honor them

SEP 28, 2026

Filed under [Digital Advertising](/categories/digital-advertising/)

Two announcements landed 24 hours apart this week, and they describe the same workflow from opposite ends. On September 22, IAB Tech Lab shipped AAMP 3.0 with a new specification called OpenProposal, plus a proposed standard contract for measurement services. On September 23, MarTech reported that OpenAI is testing a third-party-style tracking cookie behind ChatGPT ads. One sets rules for machines negotiating media buys. The other shows a platform building measurement faster than the consent language that should govern it. Your stack sits in the middle and, today, supports neither.

## What OpenProposal actually covers

The part of media buying OpenProposal addresses is the part nobody productized. After the brief and before the commitment, proposals get exchanged, compared, negotiated, and approved. That step still runs on people reading documents. Insertion orders exist because a human wrote them for another human to read.

OpenProposal gives sellers a machine-readable format for describing ad products and responding to briefs. A buyer agent can discover available packages, compare proposals against the brief, check availability and fit, negotiate terms, and connect the resulting deal to the standards that already handle execution and reporting. IAB Tech Lab built it on top of AdCOM, OpenDirect, and the Deals API, so nothing in the current programmatic stack gets ripped out. Safeguards cover pricing, orders, agent identity, and duplicate transactions. Both OpenProposal and the Measurement Services Addendum are open for public comment through October 22, 2026.

The quiet claim inside the announcement is worth stating plainly: agents can evaluate proposals from more publishers than a human planner could reasonably review. Wider consideration at the planning stage is the actual promise. Whether your organization can accept it depends on what sits between the brief and the money, and that is where the gap lives.

## The spec versus what you run today

Every row on the right works. It also caps how fast you can buy and how much inventory you can consider. The left column describes machinery that mostly does not exist on the buyer side yet. That is the contrarian read on a standards announcement: the IAB standardized a workflow that most stacks have not digitized at all, so the spec arrives before the systems that could honor it.

## The IAB's own advice cuts against the hype

Anthony Katsur, CEO of IAB Tech Lab, published a column on AdExchanger the day after the announcement, and it is more sober than the agentic-AI framing suggests. His guidance: deterministic software should handle what needs to happen and under which conditions. AI handles interpretation, synthesis, and proposing options where inputs are ambiguous. Booking campaigns, validating prices, and billing belong to deterministic systems. Agent recommendations should pass validation and approval controls before they create a financial commitment.

He also pushes back on agentic sprawl with math. The column cites McKinsey research putting the savings from routing predictable, rules-based tasks to deterministic software at 20% to 30% of AI costs, and links a consultancy estimate that layered architectures combining models with rules-based logic can cut blended token costs by up to 87% versus running a single frontier model for everything. His example target for an agency is concrete: cut the cost of producing an approved campaign plan by 25% within 90 days, or shrink planning from two weeks to two hours. Agent count, he says, is not a measure of success.

**The contradiction is the design.** The same organization that standardized agent-to-agent negotiation is telling you agents should not commit money without approval. OpenProposal negotiates; the approval gate stays human. If a vendor's roadmap promises agents that set budgets autonomously, that vendor now disagrees with the standards body the industry just aligned on. We made the same point about [Google Ads' AI guardrails](/blog/google-ads-ai-guardrails/): the platforms drawing the tightest boundaries around what their agents may touch are the credible ones.

## Measurement ran ahead of the contracts

The other announcement is a measurement story, and it landed one day after the standards story. A researcher who goes by Buchodi found that ChatGPT can place a cookie called `__obi` in a browser, where it persists for up to a year. When that browser later visits a site running OpenAI's advertising pixel, requests back to OpenAI can carry the same identifier along with page and conversion data. The design links ad interactions in ChatGPT to actions on participating advertiser sites, which is functionally a traditional third-party cookie in a new context.

Two qualifications keep this story honest. First, MarTech notes that Buchodi did not observe a final server-side step joining off-site activity to a named ChatGPT account, so the strongest version of the claim is unproven. Second, the consent labeling is messy: OpenAI lists `__obi` as an analytics cookie, and the research reports it could be set when analytics consent was allowed even when a visitor declined marketing cookies. OpenAI had not publicly answered questions about the labeling when the piece was published.

Put the two stories side by side and the sequencing problem appears. The IAB spent this week proposing standard contracts for measurement, verification, attribution, and analytics, so companies stop negotiating every agreement from scratch. Meanwhile a platform with a year-old cookie and an analytics label is already building the measurement the contracts are supposed to govern. We covered the spending half of this in [agents that spend without you](/blog/openai-agent-ads-spending-without-you/) and the checkout half in [ChatGPT as checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/). The measurement half completes the set: transactions inside a chat send no referrer and no click, so platforms build identifiers to close the loop, and consent becomes the fine print.

OpenProposal extends AdCOM, OpenDirect, and the Deals API instead of replacing them, which is the rare standards move that asks nothing to be ripped out. The hybrid guidance matches how reliable automation actually works. The cost of waiting has a date: public comment closes October 22, 2026, and after that the spec hardens with input from whoever showed up. Sellers that publish machine-readable ad products early will be discoverable by buyer agents first. Advertisers that wait will let their vendors decide what agentic readiness costs.

## What to do before October 22

- **Read OpenProposal and the Measurement Services Addendum.** Both are open for public comment through October 22. File where the spec breaks your workflow. This is the one window where the format bends toward the people who read it.
- **Map your brief-to-commitment path and count the human-only steps.** Each hand-off that requires a person reading a document is a step a buyer agent cannot run, and a ceiling on how much inventory you can consider.
- **Sort your own automation the way Katsur sorts it.** Money movement stays deterministic. Execution is already deterministic software, whether that is your DSP or open-source ad serving like [Revive Adserver](/tools/revive-adserver/). Agents belong where inputs are ambiguous: interpreting a brief, synthesizing performance, proposing options.
- **Ask every vendor where their AI sits relative to the financial commitment.** If the answer is upstream of approval controls, workable. If it is autonomous spend, that is now a disagreement with the IAB's published position, and you should price it like a risk.
- **Add consent labeling to measurement due diligence.** If you buy attribution, from [Northbeam](/tools/northbeam/) to an in-house model, the addendum is the contract template your lawyers will start from. The `__obi` story shows what happens when the measurement ships first and the consent language catches up later.
The insertion order was written for humans because only humans could read a proposal. That assumption expired this week, and the industry wrote down what replaces it. Whether your stack can honor the replacement is a question you answer by counting the human-only steps in your own workflow, not by waiting for your vendors to tell you.

**Sources:** [MarTech: IAB sets new standards for agentic buying and measurement (Sep 22, 2026)](https://martech.org/iab-sets-new-standards-for-agentic-buying-and-measurement/) · [MarTech: OpenAI testing third-party-style tracking in ChatGPT ads (Sep 23, 2026)](https://martech.org/openai-testing-third-party-style-tracking-in-chatgpt-ads/) · [AdExchanger: The Hybrid Advantage, by Anthony Katsur, IAB Tech Lab (Sep 23, 2026)](https://www.adexchanger.com/data-driven-thinking/the-hybrid-advantage-getting-value-out-of-agentic-ai-means-knowing-when-not-to-use-it/) · [Buchodi: ChatGPT now knows what you do on other websites via ad collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

**Tools linked in this post:** [Revive Adserver](/tools/revive-adserver/) | [Northbeam](/tools/northbeam/)

## Related reading

- [OpenAI Isn't Building Ads. It's Building Agents That Spend Money Without You.](/blog/openai-agent-ads-spending-without-you/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [Your autonomous stack's loophole is the approval step you deleted](/blog/autonomous-stack-loophole-approval-step/)
## Related tools

- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/) - Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [Paperclip](/tools/paperclip/) - Open-source control plane to manage AI agents like a company, hire, schedule, budget, and audit
- [Profound](/tools/profound/) - Enterprise AI marketing platform: answer-engine visibility plus drafting agents
## Comparison guides

- [Best Zapier alternatives (2026)](/alternatives/zapier/)
- [Best workflow automation tools (2026)](/best/workflow-automation-tools/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
- [AI Visibility](/glossary/ai-search-visibility/)
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
  "headline": "Your insertion orders were written for humans: the IAB's agentic buying rules land before your ad stack can honor them",
  "description": "Two announcements landed 24 hours apart this week, and they describe the same workflow from opposite ends. On September 22, IAB Tech Lab shipped AAMP 3.0.",
  "author": {
    "@type": "Person",
    "name": "Tim Christensen",
    "url": "https://martechsignal.com/authors/tim-christensen/",
    "@id": "https://martechsignal.com/authors/tim-christensen/#person",
    "sameAs": [
      "https://www.linkedin.com/in/tchristensen78",
      "https://github.com/timchr78"
    ]
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
  "datePublished": "2026-09-28",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": "https://martechsignal.com/blog/iab-agentic-buying-rules-insertion-orders/",
  "image": "https://martechsignal.com/og/iab-agentic-buying-rules-insertion-orders.png",
  "citation": [],
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 1540,
  "articleSection": "digital-advertising"
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
      "name": "Your insertion orders were written for humans: the IAB's agentic buying rules land before your ad stack can honor them",
      "item": "https://martechsignal.com/blog/iab-agentic-buying-rules-insertion-orders/"
    }
  ]
}
```
