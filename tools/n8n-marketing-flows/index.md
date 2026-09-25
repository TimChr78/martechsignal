# n8n Marketing Flows | MartechSignal review

79 free, one-click import n8n workflows for social posting, monitoring, ads, and SEO

- Page: https://martechsignal.com/tools/n8n-marketing-flows/
- Category: Workflow Automation
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-31

n8n Marketing Flows is a library of 79 one-click import workflows for n8n that covers the standard marketing automation jobs: scheduling social posts, monitoring sentiment on forums, digesting AI news, managing ads, and generating images and video. Each template ships as a JSON file you import into n8n, connect your own API keys, change the example parameters, and activate. The templates are in Traditional Chinese with English documentation, and every one lists which credentials it needs before you import.

The AI parts are real but replaceable. Draft workflows call an LLM node for post copy and hashtags, and a local version of every flow swaps the LLM call for Ollama, so the generation and analysis parts run free on your own machine. Only the platform nodes, publishing to Meta, reading YouTube data, writing to Sheets, need paid API keys. The ad management templates include an auto-pause flow for underperforming Meta ads.

Setup assumes you already run n8n or can spin one up with a one-line Docker command. If you have never touched n8n, the templates still work but you will learn the interface first. The docs are Chinese-first, which narrows the audience, though the workflow files themselves are language-neutral.

The directory already has an n8n entry for the platform itself. This is a template pack on top of it, and the honest comparison is that you could build these flows yourself in a weekend. What you pay for is the structure and the verified credential mapping. It is the cheapest way to stand up a working marketing automation stack, and it fits n8n users who want proven flows without rebuilding them, especially teams running Ollama locally who want AI features with no per-call cost.
