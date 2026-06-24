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
`src/content.config.ts`. Currently ~20 symptoms / ~25 mechanisms / ~119 methods, bilingual
(all graded A–D against the literature + citation-verified; every symptom has ≥5 methods).

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
3. (done) pipeline as this skill + CLAUDE.md. 4. (done) fill + grade + fact-check every symptom.
5. (mostly done) flat model retired; color-coding tried & **REJECTED** 2026-06-22 (per-card profile
colour is irrelevant once you've picked a profile — do not revisit); founders-group link still needs
a real URL. 6. **Launch: link from homepage — the only real blocker left, gated on Maciej's visual
QA + "tak".** The content "Done" bar (8–12 data-derived symptoms, each ≥3 graded methods with
timestamped sources) is **exceeded** (20 symptoms, each ≥5, graded + verified). Validated next
direction: expose the base as a **skill/MCP** ("problem in → graded methods + citations out") — all
three testers (Ola, Bartek, Radek) said that's the killer form factor, not the website.

## Conventions
- Commit to `main` (deploys). Keep raw transcripts and diagnostic data out of git.
- **Impersonal voice for content.** Method/mechanism bodies are general, impersonal knowledge —
  never a recap of one person's video (no named non-experts, no first person, no "in this video").
  A named expert may appear as a light citation; the specific anecdote lives in the timestamped
  resource. Enforced in the embed skill's synth prompt; a 2026-06 pass depersonalized the base and
  audited it for AI-slop after tester feedback that anecdote-recap + visibly-unreviewed text erodes trust.
- **YouTube resources render as grouped video cards** (method page): one thumbnail per video +
  the video title (`resource.author`) + a chapter list of timestamped moments (`resource.title` per
  moment), de-duplicated by video id. Thumbnail = `img.youtube.com/vi/<id>/hqdefault.jpg`, build-time,
  no API. Non-YouTube resources stay as simple rows. Method/symptom/mechanism method-lists are
  compact single-line rows (layout "variant B"), not the old uneven card grid.
- Polish curly-quote trap when generating content via Python: never close `„` with an ASCII `"`
  inside a string literal — use `”` (U+201D). Build frontmatter via `json.dumps`, not f-strings.
