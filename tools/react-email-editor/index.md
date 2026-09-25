# React Email Editor | MartechSignal review

Drag-n-Drop Email Editor Component for React.js

- Page: https://martechsignal.com/tools/react-email-editor/
- Category: Email Marketing
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-06

React Email Editor is Unlayer's official React component for embedding a drag-and-drop email builder inside your own application, and it pays to be precise about what the MIT license covers. The npm package is a thin wrapper whose single runtime dependency is a types package; the editor itself is a hosted service loaded from editor.unlayer.com into an iframe and unlocked with a projectId from Unlayer's developer console. Install is npm install react-email-editor, then mount the component with an onReady callback and call loadDesign, saveDesign, or exportHtml on the ref. Version 2.0.0 (July 2026) modernized the build, requires React 16.8 or newer, and fixed a long-standing unmount leak; 2.1.2 in August 2026 fixed an SSR hydration bug that could leave a blank editor under the Next.js App Router.

The hosted engine is a real builder, not a demo. It ships 15 built-in content blocks, custom tools and blocks, merge tags that accept any templating syntax, display conditions, device previews, undo and redo, and inbox previews across real email clients on the top plan. Pricing is public: a free tier, Launch at $250 per month for white-labeling, custom tools, and the Cloud API, Scale at $750 for custom blocks, collaboration, and smart merge tags, and Optimize at $2,000 for custom CSS, AMP, and inbox previews.

AI features are real and metered. An AI Assistant on paid plans streams edits into the design from chat prompts, routes to OpenAI or Anthropic, and draws on a workspace credit balance; AI image generation reached Launch plans in August 2026. There is also a hosted MCP server in beta with 14 documented tools plus agent skills for Claude Code, Codex, and Cursor, unusual for an embedded editor and handy if your users work with AI assistants.

The trade is control. Exports return HTML and a design JSON, there is no MJML output, AMP requires the top plan, and self-hosting is Enterprise-only.
