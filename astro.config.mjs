// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://cielecki.com',
  outDir: './dist',
  build: {
    inlineStylesheets: 'auto'
  }
});
