// r7 M12 (2026-09-28): Markdown content negotiation.
// Accept: text/markdown on a page URL serves that page's .md mirror with
// content-type text/markdown; HTML responses carry Vary: Accept. Everything
// else is plain static asset serving.
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    // r16 M-8 (2026-09-29): repeated-slash path variants (//about/,
    // /tools//) were served at 200 with byte-identical bodies, leaving
    // consolidation to canonicals alone. Collapse to a single slash at
    // the edge with a 301 before anything else touches the request.
    const fixed = url.pathname.replace(/\/{2,}/g, "/");
    if (fixed !== url.pathname) {
      url.pathname = fixed;
      return Response.redirect(url.toString(), 301);
    }
    // r16 L-5 (2026-09-29): documents answered DYNAMIC (origin round-trip
    // every view) because the worker rebuilds each HTML response. Cache
    // GET 200s in the edge cache keyed on the markdown-negotiation branch
    // (an .md variant must never poison the HTML slot or vice versa).
    // Stored responses carry s-maxage=300, which bounds staleness.
    const accept = (request.headers.get("accept") || "").toLowerCase();
    const mdBranch = request.method === "GET" && accept.includes("text/markdown")
        && !url.pathname.endsWith(".md");
    let cacheKey = null;
    if (request.method === "GET" && (url.pathname.endsWith("/") || !url.pathname.split("/").pop().includes("."))) {
      cacheKey = new Request(url.toString() + (mdBranch ? "#md" : "#html"), request);
      try {
        const hit = await caches.default.match(cacheKey);
        if (hit) return hit;
      } catch (e) { /* cache unavailable: serve live */ }
    }
    if (request.method === "GET" && accept.includes("text/markdown")
        && !url.pathname.endsWith(".md")) {
      const last = url.pathname.split("/").pop();
      let cand = null;
      if (url.pathname.endsWith("/")) cand = url.pathname + "index.md";
      else if (!last.includes(".")) cand = url.pathname + "/index.md";
      if (cand) {
        const md = await env.ASSETS.fetch(new URL(cand, url).toString(), request);
        if (md.status === 200) {
          const h = new Headers(md.headers);
          h.set("content-type", "text/markdown; charset=utf-8");
          h.set("vary", "Accept");
          // r18 M-7 (2026-09-30): the fetched mirror carries X-Robots-Tag:
          // noindex from the /*.md _headers rule. That tag is correct on the
          // mirror route but must not ride along onto the canonical URL's
          // negotiated branch - strip it here, keep it there.
          h.delete("x-robots-tag");
          return this._store(cacheKey, ctx, new Response(md.body, { status: 200, headers: h }));
        }
      }
    }
    const res = await env.ASSETS.fetch(request);
    const ct = res.headers.get("content-type") || "";
    if (ct.includes("text/html")) {
      const h = new Headers(res.headers);
      h.set("vary", "Accept");
      // r16 L-13 (2026-09-29): edge answers `access-control-allow-origin: *`
      // on documents though nothing needs it there. Scope the wildcard to
      // the machine-readable data endpoints by stripping it from pages.
      h.delete("access-control-allow-origin");
      return this._store(cacheKey, ctx, new Response(res.body, { status: res.status, headers: h }));
    }
    return res;
  },
  // Cache-API store helper: only page-URL GET 200s, cloned before return.
  async _store(cacheKey, ctx, res) {
    if (cacheKey && ctx && ctx.waitUntil && res.status === 200) {
      try {
        ctx.waitUntil(caches.default.put(cacheKey, res.clone()));
      } catch (e) { /* cache unavailable: serve live */ }
    }
    return res;
  }
};
