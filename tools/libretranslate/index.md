# LibreTranslate | MartechSignal review

Open-source machine translation API for content localization, self-hostable and free of vendor lock-in

- Page: https://martechsignal.com/tools/libretranslate/
- Category: AI Content & Copywriting
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-25

LibreTranslate is an open-source machine translation API, licensed AGPL-3.0 with 16,830 GitHub stars. It runs neural translation models through Argos Translate and serves them over a REST interface with automatic language detection, so it fits content localization pipelines that need translation as a service rather than as a website. You can self-host it with Docker or pip and run it offline, which keeps text away from third-party translation vendors and their retention policies.

Self-hosting is free. The hosted instance at libretranslate.com charges per character through an API key, but the site publishes no price page we could extract in September 2026, so hosted costs need confirming before anyone budgets for them. The API surface is documented with Swagger, and other software can point its translation backend at a LibreTranslate server; Mastodon is the common example, and public instances such as Disroot run on it.

Quality is the honest trade-off. The models are smaller than the commercial engines from Google or DeepL, so output fits gisting, internal drafts, and support content better than publish-ready marketing copy in every language pair. Teams that want machine translation under their own control, with an API their code can call, get a working system at no licence cost and can layer human review on top for anything customer-facing.
