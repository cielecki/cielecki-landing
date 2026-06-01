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
// Which viewer profiles a piece of content is relevant to. This is a DITA-style
// "profiling attribute": author once, filter per profile. `audhd` marks content
// specific to the ADHD+autism INTERACTION (the push-pull), not just the union.
const condition = z.enum(['adhd', 'autism', 'audhd']);

const challenges = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/challenges' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    icon: z.string().default('mdi:lightbulb-on-outline'),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
    conditions: z.array(condition).default(['adhd', 'autism']),
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
    conditions: z.array(condition).default(['adhd', 'autism']),
    // Inline "lenses": short profile-specific framing shown WITHIN one method,
    // for challenges where the same surface behaviour has an opposite mechanism
    // per profile. Single-source-of-truth — never fork the method into 3 files.
    lenses: z
      .array(z.object({ profile: condition, note: z.string() }))
      .default([]),
    resources: z.array(resource).default([]),
  }),
});

export const collections = { challenges, methods };
