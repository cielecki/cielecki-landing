import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// A single external (or internal) resource attached to a coping method.
const resource = z.object({
  title: z.string(),
  url: z.string().url().optional(), // optional: some items are referenced by name before a link is confirmed
  type: z.enum([
    'video',
    'article',
    'book',
    'podcast',
    'app',
    'product',
    'tool',
    'specialist',
  ]),
  author: z.string().optional(),
});

// A CHALLENGE — the top-level navigation unit. Slug is the filename; the same
// slug exists in both the `pl/` and `en/` folders so locale-switching keeps you
// on the equivalent page.
const challenges = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/challenges' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    icon: z.string().default('mdi:lightbulb-on-outline'),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
  }),
});

// A METHOD — a concrete way of coping with a given challenge. `challenge` is the
// slug of the parent challenge. Body (markdown) = the how-to. `resources` = links.
const methods = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/methods' }),
  schema: z.object({
    title: z.string(),
    challenge: z.string(),
    summary: z.string(),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
    resources: z.array(resource).default([]),
  }),
});

export const collections = { challenges, methods };
