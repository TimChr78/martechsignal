# Macro | MartechSignal review

Open source workspace with a self-updating, agent-driven CRM and shared AI team memory

- Page: https://martechsignal.com/tools/macro/
- Category: CRM
- Pricing: Freemium
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-07

Macro is an open-source workspace that folds email, chat, docs, tasks, calls, and a CRM into one app, built in Rust and SolidJS with the speed obsession to show for it. The premise is that AI agents are only as good as the context they can see, and team context is scattered across a dozen SaaS tools. The whole product sits in the repo: the README says fully open source, not open core, under AGPL-3.0, a switch from the Business Source License made on May 31, 2026, so the license is only months old. The CRM is the part marketing teams will ask about first, and the docs are precise about what it is. Contact and company records build themselves from your team's email: a contact appears when a teammate messages an external person, and companies roll up by email domain. There is no separate deal entity. Pipeline stages from Lead through Customer and Churned live on company records with Stage, Owner, Revenue, and Last Interaction properties, and the docs state plainly that while records create themselves, stages are all manual. Around the CRM sit Signal and Noise email triage, drafting in your voice that sends only on approval, team memory rebuilt nightly from the day's activity, agents that take a task and report back, calls recorded and transcribed into that memory, and an MCP server outside agents reach with a one-line connection command. Pricing is free for personal use and $40 per seat per month for the first five seats, then $80 per seat, with no free team plan; team-level agent memory and auto-shared email and CRM are paid features. The security posture is unusually strong for a project this young: SOC 2 Type II, ISO 27001, HIPAA with a BAA, GDPR, and US plus EU data regions. This assessment is from the repository, the docs, and the site.
