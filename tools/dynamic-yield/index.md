# Dynamic Yield | MartechSignal review

AI-powered personalization platform for web, mobile, and email experiences

- Page: https://martechsignal.com/tools/dynamic-yield/
- Category: Personalization & CDP
- Pricing: Enterprise
- Open source: no
- Last verified: 2026-09-06

Dynamic Yield by Mastercard is an enterprise personalization platform built around Experience OS, a decisioning layer that picks the content, products, and offers to serve each visitor across web, mobile apps, email, and triggered messages. Mastercard acquired the company in 2022, and documentation lives in two places: a support knowledge base and the technical documentation at dy.dev, which is unusually deep for a marketing product, covering script internals, CSP configuration, a cookie inventory, and the Parquet Daily Activity Stream.

Implementation follows a documented six-step path: create sections, sync a product feed, implement on every page, track events, set cookies from the backend, and install the Chrome extension used for debugging and visual editing. Two routes exist and the docs recommend both: client-side scripts (api_static.js or api_dynamic.js, served from adm.dynamicyield.com or adm.dynamicyield.eu) or server-side calls to the Experience API's Choose endpoint, with Kotlin, Swift, and React Native SDKs for apps.

The capability surface is broad and app names have shifted. Experience Web handles on-site campaigns and split testing, Recommendations and Algorithm Studio cover merchandising, Experience Email and Reconnect handle campaign and triggered messaging (Reconnect gained a native email delivery channel in September 2025), Audience Hub manages segmentation, and Rollout adds gradual feature release with rollback. AI features are named: Experience OS Agents is a multi-agent system with five defined roles (Personalization Expert, Designer, Developer, Copywriter, Analyst), Shopping Muse is the generative conversational commerce product now exposed as a server-side API, Predictive Targeting automates audience selection, and NextML, AffinityML, and VisualML handle ranking, affinity, and visual similarity.

Pricing is not published: the pricing URL redirects to a Mastercard product page and every path ends at contact sales or a demo request. The vendor claims eight consecutive Gartner Magic Quadrant leader placements, 80 million personalized sessions daily, and MACH Alliance certification. Documented integrations include Shopify, Shopify Hydrogen 2, Salesforce Commerce Cloud, commercetools, Magento 2, SAP Hybris, mParticle, and several email service providers.
