// r7 M12 (2026-09-28): Markdown content negotiation.
// Accept: text/markdown on a page URL serves that page's .md mirror with
// content-type text/markdown; HTML responses carry Vary: Accept. Everything
// else is plain static asset serving.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
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
      return new Response(res.body, { status: res.status, headers: h });
    }
    return res;
  }
};
