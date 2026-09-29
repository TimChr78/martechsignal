// r7 M12 (2026-09-28): Markdown content negotiation.
// Accept: text/markdown on a page URL serves that page's .md mirror with
// content-type text/markdown; HTML responses carry Vary: Accept. Everything
// else is plain static asset serving.
export default {
  async fetch(request, env) {
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
    const accept = (request.headers.get("accept") || "").toLowerCase();
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
          return new Response(md.body, { status: 200, headers: h });
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
      return new Response(res.body, { status: res.status, headers: h });
    }
    return res;
  }
};
