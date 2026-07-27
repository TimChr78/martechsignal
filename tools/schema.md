# Tool Directory Schema

## Database: `tools/tools.json`

JSON array of tool objects. Chosen over SQLite for simplicity — the build script reads JSON directly, no DB dependency.

## Tool Object

```json
{
  "slug": "hubspot",
  "name": "HubSpot",
  "tagline": "All-in-one CRM, marketing, sales, and service platform",
  "website": "https://www.hubspot.com",
  "category": "marketing-automation",
  "pricing_model": "freemium",
  "pricing_url": "https://www.hubspot.com/pricing",
  "price_from": 0,
  "price_notes": "Free CRM; Marketing Hub from $20/mo per seat",
  "ai_features": ["Content generation", "Predictive lead scoring", "Chatbot builder", "Email subject line AI"],
  "integrations": ["Salesforce", "Zapier", "Shopify", "WordPress", "Slack"],
  "github_repo": null,
  "github_stars": null,
  "last_release": null,
  "g2_rating": 4.4,
  "g2_reviews": 12500,
  "open_source": false,
  "api_available": true,
  "founded": 2006,
  "hq": "Cambridge, MA, USA",
  "status": "active",
  "date_added": "2026-07-27",
  "date_updated": "2026-07-27"
}
```

## Field Reference

| Field | Type | Required | Notes |
|---|---|---|---|
| slug | string | ✅ | URL-safe, lowercase, hyphens. Used in /tools/{slug} |
| name | string | ✅ | Display name |
| tagline | string | ✅ | One-line description (max 120 chars) |
| website | string | ✅ | Official URL |
| category | string | ✅ | Must match categories.json |
| pricing_model | enum | ✅ | free, freemium, paid, enterprise, open-source |
| pricing_url | string | — | Direct link to pricing page |
| price_from | number | — | Lowest monthly price in USD (0 = free tier exists) |
| price_notes | string | — | Human-readable pricing summary |
| ai_features | string[] | — | AI/ML capabilities |
| integrations | string[] | — | Key integrations (max 10) |
| github_repo | string | — | owner/repo format |
| github_stars | number | — | Auto-updated by pipeline |
| last_release | string | — | ISO date, auto-updated |
| g2_rating | number | — | 0-5 scale |
| g2_reviews | number | — | Review count |
| open_source | bool | ✅ | |
| api_available | bool | ✅ | |
| founded | number | — | Year |
| hq | string | — | Location |
| status | enum | ✅ | active, discontinued, acquired |
| date_added | string | ✅ | ISO date |
| date_updated | string | ✅ | ISO date |

## Categories: `tools/categories.json`

```json
[
  {"slug": "marketing-automation", "name": "Marketing Automation", "description": "End-to-end campaign orchestration and workflow automation"},
  {"slug": "email-marketing", "name": "Email Marketing", "description": "Email campaigns, sequences, and deliverability"},
  {"slug": "crm", "name": "CRM", "description": "Customer relationship management and sales pipelines"},
  {"slug": "content-ai", "name": "AI Content & Copywriting", "description": "AI-powered content generation and optimization"},
  {"slug": "analytics", "name": "Analytics & Attribution", "description": "Marketing analytics, attribution, and reporting"},
  {"slug": "social-media", "name": "Social Media", "description": "Social scheduling, listening, and engagement"},
  {"slug": "advertising", "name": "Advertising & Paid Media", "description": "Ad creation, bidding, and campaign management"},
  {"slug": "personalization", "name": "Personalization & CDP", "description": "Customer data platforms and experience personalization"},
  {"slug": "chatbots", "name": "Chatbots & Conversational AI", "description": "AI chatbots, virtual assistants, and conversational marketing"},
  {"slug": "seo", "name": "SEO & Search", "description": "Search optimization, keyword research, and content strategy"},
  {"slug": "workflow-automation", "name": "Workflow Automation", "description": "No-code/low-code automation platforms and iPaaS"},
  {"slug": "open-source", "name": "Open-Source Tools", "description": "Self-hostable open-source marketing and AI tools"}
]
```

## File Structure

```
/opt/data/martechsignal/
├── tools/
│   ├── schema.md          ← this file
│   ├── tools.json         ← tool database
│   ├── categories.json    ← category definitions
│   └── build_tools.py     ← page generator script
├── tools/index.html       ← generated: directory hub
├── tools/{slug}.html      ← generated: tool profiles (in /tools/ subdir)
├── categories/{slug}.html ← generated: category pages
└── ...existing files...
```
