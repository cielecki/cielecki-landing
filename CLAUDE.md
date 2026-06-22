# cielecki-landing

Astro static site, deployed to **cielecki.com via GitHub Pages** (`.github/workflows/deploy.yml`
builds on push to `main`). NOT Vercel (the `@astrojs/vercel` dep is unused). Tailwind,
strict TS, bilingual (pl/en) via `src/i18n/ui.ts`. Build: `npm run build` (must pass before commit).

## Neuro Toolkit — the knowledge base (the main ongoing project here)

A navigable ADHD / autism / AuDHD knowledge base: **CHALLENGE/SYMPTOM → coping METHODS →
articles + timestamped links**, filterable per profile (ADHD / autism / AuDHD). Plan + model:
`docs/neuro-toolkit/2026-06-04-graph-model-pilot.md`.

**One structure: the graph model at `/nt/[lang]/`.** Three layers: `symptoms` → `mechanisms`
→ `protocols` (collections in `src/content/`), many-to-many directed edges. Each method shows
**two independent signals**: `evidence` (A–D scientific, per-edge) + **sources** (count of
INDEPENDENT sources backing it, computed from `resources[]` via `lib/signals.ts` → `sourceCount`).
The old per-edge `community` enum was retired 2026-06-21 (unmeasurable LLM guess → now a real
count; the field is kept optional in the schema for back-compat but is not displayed). Defined in
`src/content.config.ts`. Currently ~20 symptoms / ~22 mechanisms / ~87 methods, bilingual.

The OLD flat pilot (`challenges` + `methods` collections, `/neuro-toolkit/*`) was retired
2026-06-20: its unique methods were ported into the graph, the collections + pages deleted,
and `/neuro-toolkit*` + `/audhd*` now redirect to `/nt/`.

**Traversal consistency (load-bearing) — DIRECT-ONLY:** a method is listed under a symptom iff
it addresses that symptom **directly** (a `kind:'symptom'` edge). We do NOT flatten in the symptoms
behind a method's mechanisms. Transitive routing (method→mechanism→symptom) was tried 2026-06-21
and removed 2026-06-22: because every method on a multi-symptom mechanism inherited ALL its symptoms,
it produced nonsense placements (a note-taking method under "can't start" because both touch working
memory) that grew with the base and couldn't be fixed by edge-trimming. The **mechanisms are the
bridge** instead: symptom page shows direct methods + a "Dlaczego tak się dzieje" mechanisms section;
click a mechanism → mechanism page lists the methods that address THAT mechanism directly. Symmetry
holds on direct edges: method→symptom shows on both the symptom page and the method page's "Pomaga na";
method→mechanism shows on both the method page and the mechanism page. A `mechanism.symptoms[]` entry
means "this mechanism underlies this symptom" (drives the symptom's "why" section + breadcrumbs), NOT
"route every method here onto that symptom". Keep symptom/mechanism/method pages on this direct rule —
do not re-add transitive method routing.

Schema is authoritative in `src/content.config.ts`. Every node is bilingual (same slug in
`pl/` and `en/`) and tagged `conditions: [adhd|autism|audhd]` so the header profile filter
(see `src/layouts/AudhdLayout.astro`) works graph-wide.

### Building / extending the base → use the skill
`.claude/skills/neuro-toolkit-embed/` encodes the full repeatable pipeline (harvest →
clean → extraction Workflow → synthesize → apply → fact-check). Use it whenever embedding a
source. Key rules it enforces: two signals stay separate and HONEST, every nugget links to
the exact video second, **fact-check any specific study/number before trusting the synthesis**
(it has misquoted studies), reuse slugs, prefer enriching over near-duplicates.

### Public / private split (hard rule)
- **Public** (this repo): the graph content + the embed tooling. Safe to commit/deploy.
- **Private** (`~/Documents/Projects/personal/AuDHD/`, NEVER committed or published): raw
  harvested transcripts (`zrodla/`), Maciej's diagnostic data (`diagnoza/` — F84, screening
  scores, meds). Do not `git add` anything from there, and never publish its contents.

### Roadmap to v1 (see docs/ for detail)
1. Finish corpus (chunked harvest + WhatsApp founders group). 2. Derive symptom taxonomy
bottom-up from the whole corpus — **decision gate: Maciej approves the symptom list**.
3. (done) pipeline as this skill + CLAUDE.md. 4. Fill + fact-check each symptom. 5. Retire the
old flat model + color-coding/product polish + link the ADHD founders group. 6. Launch:
link from homepage. "Done" = 8–12 data-derived symptoms, each ≥3 methods with timestamped
sources + honest evidence, one structure, one-command source-embedding, linked from homepage.

## Conventions
- Commit to `main` (deploys). Keep raw transcripts and diagnostic data out of git.
- Polish curly-quote trap when generating content via Python: never close `„` with an ASCII `"`
  inside a string literal — use `”` (U+201D). Build frontmatter via `json.dumps`, not f-strings.
