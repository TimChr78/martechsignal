# Potato | MartechSignal review

Free local tool that measures brand mentions and citations in Claude's web-search answers

- Page: https://martechsignal.com/tools/potato-ai-visibility/
- Category: SEO & Search
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-31

Potato measures how visible your brand is inside Claude's web-search answers, which is a specific corner of the AI search optimization (GEO) problem. It asks Claude a fixed set of frozen questions, collects every brand mention and source citation in the answers, and scores them with deterministic rules. No AI judge, no guesswork. Every number in the report carries a confidence interval, and the whole thing runs locally so results are reproducible and auditable.

The output is a single-file offline HTML report covering mention coverage, citation validity, and the split between citations from your own domain versus third-party pages. The report is honest about its limits: it measures one engine, Claude, under one exact configuration, and it says so in the output. It is a proxy measurement, not a ranking truth detector. A free mock preview mode runs with no API key so you can see the report shape before spending anything.

Setup is the friendliest of any tool in this batch. Windows users download a portable zip and double-click a batch file. Developers can pip install the package and run the CLI or the local GUI wizard. Real runs against Claude need your own Anthropic API key, which is also the only cost.

The closest directory entry is Claude SEO, which audits your whole site for citability. Potato is narrower and complementary: it measures what Claude actually says about you today, repeatedly, so you can track whether fixes move the numbers. It fits brands that care specifically about Claude citations, analysts who want reproducible measurement, and teams that refuse to send brand data to a third-party monitoring SaaS. If you need cross-engine coverage of ChatGPT, Gemini, and Perplexity too, the commercial AI visibility platforms in this category are the broader option.
