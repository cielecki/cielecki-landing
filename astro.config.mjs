// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://cielecki.com',
  integrations: [tailwind(), sitemap()],
  redirects: {
    '/nt': '/nt/pl/',
    '/neuro-toolkit': '/nt/pl/',
    '/neuro-toolkit/pl': '/nt/pl/',
    '/neuro-toolkit/en': '/nt/en/',
    '/audhd': '/nt/pl/',
    '/audhd/pl': '/nt/pl/',
    '/audhd/en': '/nt/en/'
  },
  build: {
    inlineStylesheets: 'auto'
  }
});
