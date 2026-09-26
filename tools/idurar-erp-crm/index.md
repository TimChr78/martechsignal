# IDURAR ERP & CRM | MartechSignal review

Free Open Source ERP CRM Software Accounting Invoicing | Node.Js React

- Page: https://martechsignal.com/tools/idurar-erp-crm/
- Category: CRM
- Pricing: Open Source
- Open source: yes (AGPL-3.0)
- Last verified: 2026-09-07

IDURAR is an open-source ERP and CRM on the MERN stack - Node.js and Express with MongoDB behind an Ant Design React frontend - and it is smaller than its 8,700-plus GitHub stars suggest. The license file is verbatim AGPL-3.0 with no custom clauses, and the README answers the commercial question directly: free for personal or commercial use. The same README also calls the project fair-code in one line and open source in another, and the backend package.json still says Fair-code License, so the licensing story is untidy even though the license itself is standard AGPL. The feature set needs the most correction before you commit: the README claims exactly four modules - invoice, payment, quote, and customer management - and the code backs that up. Quotes are not a separate entity but an invoice with a quote type, converted through a dedicated endpoint, and recurring invoices are a field on the invoice model rather than a billing engine. There are no expense, lead, product, or inventory models in the open-source code, and the role model ships with a single owner role, so this is a one-admin invoicing core rather than a departmental suite. The paid tiers on the vendor site make the same point by omission: a Professional lifetime license at $5,000 and an Enterprise license at $10,000, which add multi-company, multi-currency, multiple languages, a headless API, and support windows. Every entity gets auto-generated REST routes (create, read, update, delete, search, filter, summary) but there is no Swagger spec and the docs subdomain does not resolve, so plan to read the source. Installation is two npm terminals rather than a container; there is no Dockerfile in the repository. This assessment is from the repository, the license file, and the vendor site.
