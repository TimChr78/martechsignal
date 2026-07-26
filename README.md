# martechsignal.com

Source for [martechsignal.com](https://martechsignal.com) — *The AI in Marketing Automation* newsletter landing page + blog.

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
- Zone: `3ebb3af1888d56dac8732ddf6158c6d2`
- Kit newsletter embed UID: `9c9d44c5b7`
