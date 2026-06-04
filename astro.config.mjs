// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://cielecki.com',
  integrations: [tailwind()],
  redirects: {
    '/neuro-toolkit': '/neuro-toolkit/pl/',
    '/nt': '/nt/pl/',
    '/audhd': '/neuro-toolkit/pl/',
    '/audhd/pl': '/neuro-toolkit/pl/',
    '/audhd/en': '/neuro-toolkit/en/'
  },
  build: {
    inlineStylesheets: 'auto'
  }
});
