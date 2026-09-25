# advertools | MartechSignal review

Python toolkit for SEO and advertising analysis in pandas DataFrames

- Page: https://martechsignal.com/tools/advertools/
- Category: Advertising & Paid Media
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-25

advertools is a Python package by Elias Dabbas for online marketing analysis. Each function does one job, and the results land in pandas DataFrames. On the advertising side, kw_generate builds keyword lists from product and attribute combinations, and ad_from_string splits a long text into headline and description slots so ad copy can be assembled and checked at scale. urlytics breaks large URL sets into components for reporting, and the *_to_df helpers convert log files, XML sitemaps, robots.txt files and URL lists into DataFrames.

The SEO side is just as concrete. spider is a generic SEO crawler built on Scrapy, with full access to Scrapy settings for headers, user agents and crawl limits. robotstxt_to_df downloads robots.txt into a DataFrame, and the sitemap functions download and parse XML sitemaps. serp_goog and serp_yt import search results pages from Google and YouTube, with the search parameters needed for country and language splits. There are also modules for the Twitter and YouTube data APIs, a 3,000-plus emoji database, and extract_ functions that pull hashtags, mentions and emoji out of social text.

Version 0.18.0 added a Claude SERP analytics module, which points part of the toolkit at LLM answer data. The package installs from PyPI with pip install advertools, needs no account, and is MIT licensed. Docs live on Read the Docs, with notebooks on Kaggle for practice data. For marketers who work in notebooks rather than dashboards, it covers SERP, keyword, ad text and URL analysis without SaaS pricing.
