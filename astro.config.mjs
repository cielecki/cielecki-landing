// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://cielecki.com',
  integrations: [tailwind()],
  redirects: {
    '/audhd': '/audhd/pl/'
  },
  build: {
    inlineStylesheets: 'auto'
  }
});
