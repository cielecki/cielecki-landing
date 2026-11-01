// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://cielecki.com',
  integrations: [tailwind(), sitemap()],
  // The Neuro Toolkit lives at neuro.cielecki.com (moved there 2026-11-01). These redirect the
  // old entry points; deep old URLs (slugs changed pl→en) are caught by src/pages/404.astro.
  redirects: {
    '/nt': 'https://neuro.cielecki.com/',
    '/nt/pl': 'https://neuro.cielecki.com/',
    '/nt/en': 'https://neuro.cielecki.com/',
    '/neuro-toolkit': 'https://neuro.cielecki.com/',
    '/neuro-toolkit/pl': 'https://neuro.cielecki.com/',
    '/neuro-toolkit/en': 'https://neuro.cielecki.com/',
    '/audhd': 'https://neuro.cielecki.com/',
    '/audhd/pl': 'https://neuro.cielecki.com/',
    '/audhd/en': 'https://neuro.cielecki.com/'
  },
  build: {
    inlineStylesheets: 'auto'
  }
});
