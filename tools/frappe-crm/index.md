# Frappe CRM | MartechSignal review

Fully featured, open source CRM

- Page: https://martechsignal.com/tools/frappe-crm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-06

Frappe CRM is an open-source sales CRM built on the Frappe framework, the Python and MariaDB stack behind ERPNext, and it ships under AGPL-3.0, a license worth reading before you plan to offer it as a hosted service. The README pitches a simple, affordable CRM for modern sales teams with unlimited users, and pricing supports the affordability half of that: self-hosting is free, Frappe Cloud hosting starts at $5 per month per site, dedicated servers run $20 to $60 per month, and no tier charges per user.

Development moves quickly. The project released roughly 130 times across 2025 and 2026, reaching v1.83.0 in September 2026, adding Sales Hierarchy in June 2026, an editable dashboard in July 2025, and assignment rules. Every lead, deal, contact, and organization is a Frappe document, so custom fields, custom statuses, list actions, and Python server scripts extend the CRM the same way ERPNext gets extended. The interface is a Vue 3 single-page app with a drag-and-drop kanban board for leads and deals, saved, public, and pinned views, web forms for lead capture, and a mobile experience delivered as a progressive web app rather than a native app.

Integrations are narrow and documented. Telephony covers Twilio and Exotel, with click-to-call from lead, deal, and contact pages, call pop-ups, recording, and notes. WhatsApp arrives through a separate third-party app, Frappe WhatsApp by Shridhar, sending from templates over the WhatsApp Business Cloud API. Email works from lead and deal records with multiple accounts and templates. Facebook and Instagram lead sync is documented as beta. ERPNext sync creates customers and quotations from won deals, though most of it needs both apps on the same site.

Two things to check first: no AI features appear in the README, marketing site, or release notes, and the repository's default branch is develop, which tracks the unreleased Frappe v17, so pin to main for a stable install.
