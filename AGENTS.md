# cielecki-landing

Astro static site, deployed to **cielecki.com via GitHub Pages** (`.github/workflows/deploy.yml`
builds on push to `main`). NOT Vercel (the `@astrojs/vercel` dep is unused). Tailwind, strict TS.
Build: `npm run build` (must pass before commit).

Currently this is just **Maciej's personal landing page** (`src/pages/index.astro` on
`src/layouts/BaseLayout.astro`, styles in `src/styles/main.css`, JS in `src/scripts/main.js`).

## Neuro Toolkit — MOVED OUT

The ADHD/autism/AuDHD **Neuro Toolkit** knowledge base (symptoms → mechanisms → methods) used to
live here at `/nt/[lang]/`. In 2026-06 it moved to dopadone.app/neuro-toolkit/; on 2026-11-01,
when DopaDone was retired, it moved again into its own repo **`cielecki/neuro-toolkit`**
(`~/workspace/projects/neuro-toolkit`), live at **https://neuro.cielecki.com**. Its content,
pages, the `neuro-toolkit-embed` skill and its issues all live there. Edit the toolkit there,
not here.

What remains here for it:
- **Redirects** in `astro.config.mjs`: `/nt`, `/nt/pl|en`, `/neuro-toolkit*`, `/audhd*` →
  `https://neuro.cielecki.com/`.
- **`src/pages/404.astro`** — catch-all: any old deep toolkit URL (slugs changed pl→en, so no
  1:1 map) is JS-redirected to the toolkit home; everything else is a normal 404.

## Conventions
- Commit to `main` (deploys via GitHub Pages).
