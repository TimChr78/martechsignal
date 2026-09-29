// M8 (r9, 2026-09-28): collapse malformed path variants (double slashes,
// dot segments, repeated trailing slashes) to the canonical path with a 308.
// LIVE NOTE (r11 L-4, 2026-09-29): this file ships in deploy-out/functions/
// but the edge still serves 200 on // variants (verified live). Canonicals on
// those URLs are correct, so impact is crawl-budget noise only — accepted
// risk, not re-fixed. Revisit only if GSC shows variant URLs indexed.
// Fixed-point safe: the redirect target always equals its own normalization,
// so the rule can never loop (cf. the 2026-09-09 _redirects loop incident —
// path-prefix redirect rules are banned for this; this middleware compares
// first and only redirects when the path actually changes, otherwise passes
// through to the static asset via context.next()).
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const raw = url.pathname;
  const trailing = raw.endsWith("/");
  const norm =
    "/" +
    raw
      .split("/")
      .filter((seg) => seg !== "" && seg !== ".")
      .join("/") +
    (trailing ? "/" : "");
  const fixed = norm === "/" || norm === "" ? "/" : norm;
  if (fixed !== raw) {
    url.pathname = fixed;
    return Response.redirect(url.toString(), 308);
  }
  return context.next();
}
