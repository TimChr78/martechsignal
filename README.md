# martechsignal.com

Source for [martechsignal.com](https://martechsignal.com) — independent reviews of AI marketing automation tools, pricing research, comparisons and benchmarks.

## Structure

- `index.html` — landing page (single-file, no build step)
- `deploy.sh` — deploy to Cloudflare Pages via Direct Upload API

## Deploy

```bash
./deploy.sh
```

Requires `CLOUDFLARE_API_KEY` env var (CF API token with Pages:Edit permission).

## Notes

- Hosted on Cloudflare Pages (project: `martechsignal`)
- Kit newsletter embed via Kit CDN
