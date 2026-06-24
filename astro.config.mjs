// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://cielecki.com',
  integrations: [tailwind(), sitemap()],
  // The Neuro Toolkit moved to dopadone.app/neuro-toolkit/ (2026-06). These redirect the
  // old entry points; deep old URLs (slugs changed pl→en) are caught by src/pages/404.astro.
  redirects: {
    '/nt': 'https://dopadone.app/neuro-toolkit/',
    '/nt/pl': 'https://dopadone.app/neuro-toolkit/',
    '/nt/en': 'https://dopadone.app/neuro-toolkit/',
    '/neuro-toolkit': 'https://dopadone.app/neuro-toolkit/',
    '/neuro-toolkit/pl': 'https://dopadone.app/neuro-toolkit/',
    '/neuro-toolkit/en': 'https://dopadone.app/neuro-toolkit/',
    '/audhd': 'https://dopadone.app/neuro-toolkit/',
    '/audhd/pl': 'https://dopadone.app/neuro-toolkit/',
    '/audhd/en': 'https://dopadone.app/neuro-toolkit/'
  },
  build: {
    inlineStylesheets: 'auto'
  }
});
