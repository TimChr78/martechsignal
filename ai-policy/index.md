# AI policy

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

## AI policy

MartechSignal publishes for people first and for answer engines second. This page states, in plain terms, what AI systems may and may not do with our content. It was last updated on 2026-09-26.

## The short version

- **Search and indexing: yes.** Building a search index and returning links with short excerpts is fine.
- **Retrieval, grounding, and AI answers: yes, with attribution.** Pulling our content into a live answer (RAG, grounding, agent fetches on a user's request) is fine. Cite the page you took it from.
- **One trade-off to know.** Our robots.txt blocks Google-Extended. That token governs model training, but it also removes us from Gemini API and Vertex AI grounding pipelines. AI Overviews and the Gemini app are unaffected (those follow Googlebot, which we allow). We accept the trade: keeping our content out of model training is worth losing Vertex-based RAG citation. Added 2026-09-26.
- **Training or fine-tuning models: no.** Do not use our content to train or fine-tune a model.
- **Republishing our work as your own: no.** The same rule we publish in our [terms of use](/terms/).
## What the signals mean

We express this policy with the three content signals defined by the Cloudflare Content Signals Policy, and the same wording appears in our [robots.txt](/robots.txt):

- **search** (we say yes): building a search index and providing search results, such as returning hyperlinks and short excerpts. Search does not include providing AI-generated search summaries.
- **ai-input** (we say yes): inputting content into one or more AI models, such as retrieval augmented generation, grounding, or other real-time taking of content for generative AI answers.
- **ai-train** (we say no): training or fine-tuning AI models.
## How this is enforced

Anthropic runs three separately controlled crawlers: ClaudeBot collects training data and stays blocked here; Claude-User and Claude-SearchBot handle retrieval and search and stay open. That split is why the same robots.txt can say yes to AI answers and no to training without contradicting itself.

Our robots.txt declares the signals, and it blocks the well-known training crawlers outright: GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, meta-externalagent, Bytespider, and Amazonbot. Search crawlers and user-triggered fetch agents are left open on purpose. The signals are a stated preference and a reservation of rights, not a technical guarantee. Some tools ignore robots.txt; the policy stands either way.

## Why this line

Retrieval sends readers to the source. Training does not. We publish pricing research, benchmarks, and assessments so buyers can make better decisions, and a model trained on the corpus competes with the site that produced it. Allowing the first use and refusing the second is the honest split.

## Getting permission

Want to train on the corpus, license it, or ask about a use this page does not cover? [Contact us](/contact/). Licensing is available; silence is not consent.

Two non-standard extensions appear in the robots.txt on purpose: Content-Signal declares what each crawler may do with what it fetches, and Agentmap points agents at the machine-readable catalog in /.well-known/ard.json. Parsers that follow RFC 9309 ignore what they do not know, which is the intended behavior.

&copy; 2026 MARTECHSIGNAL &middot; THE AI IN MARKETING AUTOMATION


```json
{"@context": "https://schema.org", "@type": "WebPage", "name": "AI policy | MartechSignal", "url": "https://martechsignal.com/ai-policy/", "publisher": {"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/"}}
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/ai-policy/#webpage", "dateModified": "2026-09-26"}
```
