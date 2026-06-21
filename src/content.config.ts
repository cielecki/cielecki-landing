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
  // The "nugget": the specific claim/insight pulled from this source. For a video,
  // pair this with a timestamped url (…&t=NNNs) so it links to the exact moment.
  note: z.string().optional(),
});

// A CHALLENGE — the top-level navigation unit. Slug is the filename; the same
// slug exists in both the `pl/` and `en/` folders so locale-switching keeps you
// on the equivalent page.
// Which viewer profiles a piece of content is relevant to. This is a DITA-style
// "profiling attribute": author once, filter per profile. `audhd` marks content
// specific to the ADHD+autism INTERACTION (the push-pull), not just the union.
const condition = z.enum(['adhd', 'autism', 'audhd']);

// ── GRAPH MODEL ───────────────────────────────────────────────────────────────
// New three-layer graph that supersedes the flat challenge→method model:
//   SYMPTOM (lay-language entry) → MECHANISM (why) → PROTOCOL (what to do).
// Edges are many-to-many and directional, each carrying TWO independent signals:
//   evidence  — strength of scientific backing (A = meta-analysis/RCT … D = anecdote/theory)
//   sources   — how many INDEPENDENT sources back the method (computed from resources[]
//               at render time, see lib/signals.ts → sourceCount). Replaces the old,
//               unmeasurable LLM "community" guess. Shown SEPARATELY from evidence so the
//               reader weighs "strong in studies" vs "many independent voices recommend it".

const evidence = z.enum(['A', 'B', 'C', 'D']);
// DEPRECATED: kept optional for backward-compat with already-authored data. No longer
// displayed — the second signal is now the computed source count. New synth may omit it.
const community = z.enum(['wysoki', 'średni', 'niski', 'brak']).optional();

// A directed edge from a PROTOCOL to the mechanism (or symptom) it addresses.
const edge = z.object({
  target: z.string(), // slug of the mechanism or symptom (language-agnostic)
  kind: z.enum(['mechanism', 'symptom']),
  evidence,
  community,
  note: z.string().optional(),
});

const symptoms = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/symptoms' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    icon: z.string().default('mdi:help-circle-outline'),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
    conditions: z.array(condition).default(['adhd', 'autism', 'audhd']),
  }),
});

const mechanisms = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/mechanisms' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    icon: z.string().default('mdi:cog-outline'),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
    conditions: z.array(condition).default(['adhd', 'autism', 'audhd']),
    symptoms: z.array(z.string()).default([]), // symptom slugs this mechanism underlies
  }),
});

const protocols = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/protocols' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    icon: z.string().default('mdi:tools'),
    order: z.number().default(99),
    lang: z.enum(['pl', 'en']),
    conditions: z.array(condition).default(['adhd', 'autism', 'audhd']),
    addresses: z.array(edge).default([]),
    resources: z.array(resource).default([]),
  }),
});

export const collections = { symptoms, mechanisms, protocols };
