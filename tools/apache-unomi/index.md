# Apache Unomi | MartechSignal review

Apache's open-source customer data platform and personalization engine

- Page: https://martechsignal.com/tools/apache-unomi/
- Category: Personalization & CDP
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-09-25

Apache Unomi is a Java customer data platform and personalization engine governed by the Apache Software Foundation, licensed Apache-2.0, with 375 stars on the apache/unomi repository. It runs as an OSGi application inside Apache Karaf and speaks HTTP REST with JSON payloads, managing user profiles, the events attached to those profiles, segments, scoring plans, and a rule system that fires actions when matching events arrive. The privacy REST API is the differentiator: integrators can build interfaces that let visitors see what has been collected, withdraw consent, anonymize past and future data, or delete a profile entirely. Unomi is also the reference implementation of the OASIS Context Server (CXS) specification for exchanging profile data between systems.

The documented quick start is a Docker Compose file pairing the apache/unomi image with Elasticsearch 7.10.2 and exposing ports 8181, 9443, and 8102 behind default karaf credentials. The site states plainly that this configuration is for discovery and not for production. The current stable release is 3.0.1, with 3.1.0 in development. Unomi is built to integrate with CMS, CRM, and mobile systems over its REST API, its storage layer works with Elasticsearch or MongoDB, and new conditions and actions are added as Karaf plugins rather than by forking the core.

There is no commercial cloud tier and no vendor selling support. Teams run it themselves and own the operations work. The project carries no licence fee and no paid feature tier, and the trade is a small community and a Java-heavy skill profile for full control over profile data.
