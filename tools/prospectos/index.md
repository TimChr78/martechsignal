# ProspectOS | MartechSignal review

Open-source lead prospecting CRM with Google Maps and Instagram scraping

- Page: https://martechsignal.com/tools/prospectos/
- Category: CRM
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-08-31

ProspectOS is a local lead-prospecting tool for agencies and freelancers who sell websites or digital services to small businesses. It scans Google Maps by niche and city (or by pin and radius), checks each company's website to separate no-site from slow-or-insecure-site, scores the results, and generates an AI-written outreach message plus a PDF diagnosis per lead, all tracked in a visual kanban CRM. The stack is Flask, React 19, TypeScript, and SQLite, runs locally on Windows, and the repo shows 230 passing tests. The honest catch is in the project's own warnings: it is a scraping tool, Google Maps and Instagram scraping can violate those platforms' terms, and the Instagram module logs in with a personal account via instagrapi, which carries a real risk of checkpoint or ban. The README recommends a secondary account and moderate use. MIT-licensed with 206 stars, it is a working codebase for learning and prospecting at small scale, sold to nobody and hosted by you, with the compliance question deliberately left in your hands.
