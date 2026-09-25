# Promptfoo | MartechSignal review

Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming

- Page: https://martechsignal.com/tools/promptfoo/
- Category: GEO & LLM Optimization
- Pricing: Freemium
- Open source: yes (MIT)
- Last verified: 2026-09-25

Promptfoo is an open source LLM evaluation toolkit, used by developers to test prompts and models and by marketing teams to track brand answers in AI search. The core is a CLI and a TypeScript library, both MIT licensed. You define prompt sets, providers and grading rules in YAML, run everything in one command, and get a comparison of how each model answered each prompt. Outputs are scored with assertions: exact match, contains, regex, similarity, and model-graded checks where one model grades another's answer. Results open in a local web viewer.

For generative engine optimization, Promptfoo is not a dedicated GEO dashboard and does not pretend to be one. What teams do is write a fixed set of buyer questions, run that set across ChatGPT, Perplexity and other models on a schedule, and grade whether their brand appears in each answer and what the answer claims. That yields prompt-level brand-answer tracking with developer tooling: versioned, repeatable and diffable between runs. There is no share-of-voice index or rank chart out of the box; tracking is only as good as the prompt set and grading rules you write.

The second major mode is red teaming. The CLI generates attack probes against an application and reports findings. Guardrails, an MCP proxy, model security and code scanning are separate products on the cloud side, and the hosted red team product shows a 10k probes per month limit. Everything so far runs locally at no cost. Promptfoo's cloud adds team and enterprise features, and as of September 2026 the pricing page lists no public price numbers.
