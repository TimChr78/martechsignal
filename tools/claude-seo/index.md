# Claude SEO | MartechSignal review

Open-source SEO skill for Claude Code with 25 sub-skills and 18 parallel agents

- Page: https://martechsignal.com/tools/claude-seo/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-28

Claude SEO turns Claude Code into an SEO audit machine. You type /seo audit and it spawns up to 15 specialist agents in parallel, each covering a different discipline: technical SEO, content quality, E-E-A-T signals, Schema.org markup, Core Web Vitals, local SEO, ecommerce SEO, international SEO, and AI search optimization (what Google calls GEO). A full-site audit that would take a consultant a full day finishes in minutes. The output is a prioritized action plan where every recommendation carries the observation it rests on, its dependencies, and an explicit "how would we know this failed?" check. That last part matters. Most SEO tools tell you what's wrong. Claude SEO tells you what's wrong, why it matters, and how you'd verify the fix worked.

The AI-search angle is what separates this from a Screaming Frog crawl. Claude SEO scores your content for citability by AI answer engines: whether your pages have self-contained 134-167 word answer blocks, question-based heading hierarchy, and the structured data that makes LLMs cite you instead of your competitor. It checks for IPTC TrainedAlgorithmicMedia metadata on AI-generated images, llms.txt files, and agent-friendly page structure per web.dev guidance. If you're optimizing for a world where Google's AI Overviews and ChatGPT answers replace traditional blue links, this is the audit tool built for that reality.

It's free and MIT-licensed. The catch is you need Claude Code (Anthropic's paid CLI/IDE product) to run it, so you're paying for API tokens. A full audit on a 200-page site burns through a meaningful chunk of tokens. There's also a private community mirror on Skool (AI Marketing Hub Pro) that gets early features, but the public repo is fully functional. Version 2.2.5 ships 439 passing tests, which is unusual rigor for a skill pack.

Compared to doing this manually with Screaming Frog, Ahrefs, and a spreadsheet, Claude SEO collapses the workflow into one command. Compared to SaaS audit tools like Sitebulb or Lumar, it's more flexible and cheaper, but you lose the polished dashboards and historical tracking. It's best for SEO agencies running 5+ client sites who want weekly automated audits instead of quarterly manual ones, and for in-house SEO leads who want a second pair of eyes before executive reviews. If you don't use Claude Code, look at Codex SEO, the same author's port for OpenAI's Codex.
