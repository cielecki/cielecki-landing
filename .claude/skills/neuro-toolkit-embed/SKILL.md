---
name: neuro-toolkit-embed
description: >-
  Embed a source (YouTube video / whole channel / a pasted summarize-anything summary)
  into the Neuro Toolkit graph knowledge base at src/content (symptoms → mechanisms →
  protocols, two-signal evidence+community, timestamped nuggets). Use when adding ADHD/
  autism/AuDHD material to the /nt/ knowledge base, when someone shares a video/link to
  fold in, when deriving the symptom taxonomy from the harvested corpus, or when running
  the harvest / extraction / fact-check pipeline. Triggers: "embed this video", "dodaj to
  źródło do bazy", "wciągnij ten film do neuro toolkit", "zbierz kanał X", "wyprowadź
  taksonomię z korpusu", "pogłęb temat <symptom>".
---

# Neuro Toolkit — embed a source

Repeatable pipeline that turns ADHD/autism/AuDHD content into graph entries. The data
model + private/public split live in the repo `CLAUDE.md`; read it first. Bilingual: every
node gets a `pl/` and `en/` file with the same slug.

## Public / private split (do not break)
- **Public** (this repo, committed, deployed): the graph content under `src/content/{symptoms,mechanisms,protocols}/` and these tools.
- **Private** (`~/Documents/Projects/personal/AuDHD/`, NEVER committed/published): raw transcripts in `zrodla/transcripts/`, diagnostic data in `diagnoza/`. Harvested transcripts land there.

## Three entry paths

### A. A pasted summarize-anything summary (already has timestamped links)
Fastest. The summary already carries `&t=Ns` links. Structure it straight into the graph:
read it, map nuggets to symptoms/mechanisms/methods (reuse existing slugs; create new only
for genuinely new entry-points), then write a one-shot generator like the committed
`scripts/embed_*.py` pattern (JSON frontmatter + bilingual bodies). **Watch the Polish
curly-quote trap**: never close a `„` with an ASCII `"` inside a Python string — use `”`
(U+201D) or the `fix_quotes` one-liner. Evidence is usually C (single source); bump
established frameworks (DBT/ACT/GTD/CBT) to B.

### B. One video / a few videos
1. Harvest: `python3 scripts/harvest_channel.py <url> --limit N` → timestamped `.vtt` in the private transcripts dir.
2. Clean: `python3 scripts/vtt_to_text.py <file.vtt> --link=<videoId>` (use `--link=` with the `=` — video ids can start with `-`).
3. Extract + synthesize: run the **Workflow** tool with `scripts/extract-workflow.js` (edit its EXISTING-taxonomy list first), args = JSON array of `{id,title,path,url}` for the cleaned `.txt` files.
4. Apply: `python3 scripts/apply_synth.py <workflow-output.json> --symptom <slug>` (creates new nodes, never clobbers; appends enrichment resources).

### C. A whole channel / the corpus (bulk)
- `scripts/harvest_batch.sh` harvests the dedicated channels (full) + general channels (title-filtered) + the hand-picked seed. Resumable (`--no-overwrites`). **Runs long — the harness kills multi-hundred-video background tasks; chunk per channel** (set the channel list small per run) so each finishes.
- Then the same extract→synthesize→apply as B, fanned over the corpus. This is how the **symptom taxonomy is derived bottom-up** — let the synthesis propose symptoms, then curate with Maciej (the decision gate).

## Verify evidence grades against the literature (gradecheck)

The A–D `evidence` grade starts as the synth's GUESS. This process recalibrates it against real
science and attaches citations, which render as the **"Co mówią badania"** section on the method page.

1. **Prep**: `python3 scripts/prep_grades.py /tmp/grades.json [--slugs a,b,c | --cap N]` → JSON of methods + current grades + resolved target names.
2. **Verify**: run the **Workflow** tool with `scripts/gradecheck-workflow.js`, args = that JSON. Each agent literature-searches the method→target efficacy, assigns a defensible grade, returns REAL citations. Small batches (`BATCH=2`) + retry (529 defense). Keep a run ≤ ~6 methods.
3. **Apply**: `python3 scripts/apply_grades.py <workflow-output.json>` — auto-applies **downgrades**, reports **upgrades** for review (rerun with `--apply-upgrades` to accept), writes `studies[]`. `--dry-run` first.
4. `npm run build`, spot-check the "Co mówią badania" section, **fetch 1–2 of the returned citations to confirm they are real** (the agent can hallucinate URLs — this is the top risk), commit.

Grade taxonomy — **keep identical** in the workflow prompt AND on the page:
- **A** meta-analysis / systematic review / multiple RCTs
- **B** ≥1 RCT or consistent controlled studies; or strong mechanism w/ supporting trials
- **C** small/uncontrolled/indirect; strong mechanism, little direct test; clinical consensus only
- **D** no empirical test — theory / single voice / lived experience

Hard rules: conservative (downgrade on doubt); cite only sources actually found — **NEVER invent a PMID/DOI**; no study found → C/D + `no_direct_evidence`, say so plainly. `nt-factcheck` (prose-claim truth) and `nt-gradecheck` (grade calibration) are SEPARATE workflows — run both.

## Conventions (enforce on every embed)
- **Two signals**: `evidence` A–D (scientific strength, per-edge) and the **source count** (how many INDEPENDENT sources back the method — computed from `resources[]`, NOT authored). Be HONEST on evidence — a bare YouTube claim is C; A/B needs a study or strong mechanism. The old `community` enum is retired (it was an unmeasurable guess); you no longer set it. The way to make a method's source signal stronger is to attach MORE genuine resources from DIFFERENT authors — never inflate.
- **Every resource nugget links to the exact second**: url `…&t=Ns`, plus a `note` (the nugget itself = the quote shown on the page), `author` (drives the independent-source count — distinct authors count as distinct sources), `type`. Two nuggets from the same interview = ONE source.
- **Fact-check before trusting synth claims.** The synth guesses evidence and can misquote studies (it once wrote "30 min" for a study that used ~1 h). For any specific study/number a node asserts, verify via web search and add the real link (inline markdown in the body) or correct it. This is health content — unverified claims are the top risk.
- **Reuse slugs; prefer enriching an existing method over a near-duplicate.** Curate overlaps (e.g. phone-out-of-bedroom ⊂ digital-sunset).
- **Bilingual**: pl + en, same slug. Bodies 2–4 short concrete paragraphs.
- Mechanisms have no `resources` field — put study links as inline markdown in the body.

## After writing
`npm run build` (must pass), spot-check the rendered page(s), commit to `main` with a
descriptive message (push deploys via GitHub Pages). Raw transcripts stay private — never
`git add` anything under `personal/AuDHD/`.

## Schema (authoritative: `src/content.config.ts`)
- **symptom**: title, summary, icon, order, lang, conditions[]
- **mechanism**: + `symptoms[]` (slugs it underlies)
- **protocol (method)**: + `addresses[]` (edges: target, kind mechanism|symptom, evidence A–D, note; `community` is deprecated/optional, not displayed), `resources[]` (title, url, type, author, note), `studies[]` (title, url, year, type, finding — written by gradecheck, renders as "Co mówią badania")
