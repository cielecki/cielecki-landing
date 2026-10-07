# cielecki-landing

Astro static site, deployed to **cielecki.com via GitHub Pages** (`.github/workflows/deploy.yml`
builds on push to `main`). NOT Vercel (the `@astrojs/vercel` dep is unused). Tailwind, strict TS.
Build: `npm run build` (must pass before commit).

Currently this is just **Maciej's personal landing page** (`src/pages/index.astro` on
`src/layouts/BaseLayout.astro`, styles in `src/styles/main.css`, JS in `src/scripts/main.js`).

## Neuro Toolkit — MOVED OUT (2026-06)

The ADHD/autism/AuDHD **Neuro Toolkit** knowledge base used to live here at `/nt/[lang]/`
(bilingual graph: symptoms → mechanisms → protocols, Tailwind UI, an embed pipeline skill).
It was **migrated to dopadone.app/neuro-toolkit/** — English-only, vanilla CSS, dark theme —
and fully removed from this repo. The content, pages, components, `src/content*`, `src/lib`,
`src/i18n`, the `AudhdLayout`, `docs/neuro-toolkit/`, and the `neuro-toolkit-embed` skill now
live in **`apps/dopadone/`** (`apps/website/` + repo-root `.claude/skills/`). Edit the toolkit
there, not here.

What remains here for it:
- **Redirects** in `astro.config.mjs`: `/nt`, `/nt/pl|en`, `/neuro-toolkit*`, `/audhd*` →
  `https://dopadone.app/neuro-toolkit/`.
- **`src/pages/404.astro`** — catch-all: any old deep toolkit URL (slugs changed pl→en, so no
  1:1 map) is JS-redirected to the toolkit home; everything else is a normal 404.

## Conventions
- Commit to `main` (deploys via GitHub Pages).
