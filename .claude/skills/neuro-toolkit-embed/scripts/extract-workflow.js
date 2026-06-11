// Neuro Toolkit extraction workflow — TEMPLATE.
// Invoke via the Workflow tool with args = JSON array of
//   { id, title, path, url }  (one per cleaned transcript .txt)
// Phase 1 (Extract): one agent per transcript -> structured nuggets.
// Phase 2 (Synthesize): one agent clusters all nuggets -> new_mechanisms /
//   new_methods / enrichments, aligned to content.config.ts so apply_synth.py
//   can write them directly. Returns { synth }.
//
// NOTE: args may arrive as a JSON string — the `sources` line below handles both.
// Edit the EXISTING-taxonomy list in the synth prompt before each run so it
// reuses current slugs and never duplicates them.
export const meta = {
  name: 'nt-extract',
  description: 'Extract nuggets from cleaned transcripts and synthesize graph additions',
  phases: [{ title: 'Extract' }, { title: 'Synthesize' }],
}

const ev = { type: 'string', enum: ['A', 'B', 'C', 'D'] }
const comm = { type: 'string', enum: ['wysoki', 'średni', 'niski', 'brak'] }
const cond = { type: 'array', items: { type: 'string', enum: ['adhd', 'autism', 'audhd'] } }
const NUGGET_SCHEMA = { type: 'object', additionalProperties: false, properties: { nuggets: { type: 'array', items: {
  type: 'object', additionalProperties: false, properties: {
    claim_pl: { type: 'string' }, claim_en: { type: 'string' }, timestamp_s: { type: 'number' },
    kind: { type: 'string', enum: ['method-tip', 'mechanism-evidence', 'symptom-description', 'framing'] },
    mechanism_hint: { type: 'string' }, method_hint: { type: 'string' }, evidence_hint: ev, verbatim: { type: 'string' },
  }, required: ['claim_pl', 'claim_en', 'timestamp_s', 'kind', 'evidence_hint'],
} } }, required: ['nuggets'] }
const edge = { type: 'object', additionalProperties: false, properties: {
  target: { type: 'string' }, kind: { type: 'string', enum: ['mechanism', 'symptom'] }, evidence: ev, community: comm,
  note_pl: { type: 'string' }, note_en: { type: 'string' } }, required: ['target', 'kind', 'evidence', 'community'] }
const resource = { type: 'object', additionalProperties: false, properties: {
  title_pl: { type: 'string' }, title_en: { type: 'string' }, url: { type: 'string' },
  type: { type: 'string', enum: ['video', 'article', 'book', 'podcast', 'app', 'product', 'tool', 'specialist'] },
  author: { type: 'string' }, note_pl: { type: 'string' }, note_en: { type: 'string' } }, required: ['title_pl', 'title_en', 'type'] }
const mech = { type: 'object', additionalProperties: false, properties: {
  slug: { type: 'string' }, title_pl: { type: 'string' }, title_en: { type: 'string' }, summary_pl: { type: 'string' },
  summary_en: { type: 'string' }, body_pl: { type: 'string' }, body_en: { type: 'string' }, conditions: cond,
  symptoms: { type: 'array', items: { type: 'string' } } },
  required: ['slug', 'title_pl', 'title_en', 'summary_pl', 'summary_en', 'body_pl', 'body_en', 'conditions'] }
const method = { type: 'object', additionalProperties: false, properties: {
  slug: { type: 'string' }, title_pl: { type: 'string' }, title_en: { type: 'string' }, summary_pl: { type: 'string' },
  summary_en: { type: 'string' }, body_pl: { type: 'string' }, body_en: { type: 'string' }, conditions: cond,
  addresses: { type: 'array', items: edge }, resources: { type: 'array', items: resource } },
  required: ['slug', 'title_pl', 'title_en', 'summary_pl', 'summary_en', 'body_pl', 'body_en', 'conditions', 'addresses'] }
const enrichment = { type: 'object', additionalProperties: false, properties: {
  method_slug: { type: 'string' }, resource }, required: ['method_slug', 'resource'] }
const SYNTH_SCHEMA = { type: 'object', additionalProperties: false, properties: {
  new_mechanisms: { type: 'array', items: mech }, new_methods: { type: 'array', items: method },
  enrichments: { type: 'array', items: enrichment } }, required: ['new_mechanisms', 'new_methods', 'enrichments'] }

phase('Extract')
const sources = typeof args === 'string' ? JSON.parse(args) : args
const perTx = await parallel(sources.map((s) => () =>
  agent(
    `You are mining a transcript for a knowledge base helping neurodivergent people (ADHD / autism / AuDHD).\n` +
    `Read the file at: ${s.path}\nVideo: "${s.title}"   base url: ${s.url}\n` +
    `Lines: [H:MM:SS | <url>&t=Ns] spoken text.\n` +
    `Extract up to 12 CONCRETE, actionable or genuinely-instructive nuggets. Skip filler/sponsor/intro. ` +
    `Per nugget: claim_pl + claim_en, timestamp_s (line start second), kind, evidence_hint (A best..D; be conservative — a bare claim is usually C), ` +
    `mechanism_hint, method_hint, verbatim. Return few/zero if little relevant content — don't pad.`,
    { label: `extract:${s.id}`, phase: 'Extract', schema: NUGGET_SCHEMA }
  ).then((r) => ({ source: s, nuggets: (r && r.nuggets) || [] })).catch(() => ({ source: s, nuggets: [] }))
))
const allNuggets = []
for (const b of perTx.filter(Boolean))
  for (const n of b.nuggets)
    allNuggets.push({ claim_pl: n.claim_pl, claim_en: n.claim_en, kind: n.kind, evidence_hint: n.evidence_hint,
      mechanism_hint: n.mechanism_hint || '', method_hint: n.method_hint || '', verbatim: n.verbatim || '',
      source_title: b.source.title, url: `${b.source.url}&t=${Math.round(n.timestamp_s)}s` })
log(`extracted ${allNuggets.length} nuggets`)

phase('Synthesize')
const synth = await agent(
  `Design graph ADDITIONS for a neurodivergent knowledge base. Polish first, mirror in English.\n` +
  `EXISTING taxonomy — REUSE these slugs, never duplicate (EDIT THIS LIST before each run):\n` +
  `- symptoms: sen, zaczynanie, lek-unikanie, emocje-czarnobiale, pamiec-mysli, energia-wypalenie, szukam-pomocy\n` +
  `- mechanisms: revenge-bedtime, opozniona-faza, pobudzony-uklad, sensoryczne-zaklocenia, nocny-zryw, chroniczna-czujnosc, dlug-snu-presja, rsd, slaba-pamiec-robocza\n` +
  `Nuggets (each carries a timestamped url):\n${JSON.stringify(allNuggets)}\n\n` +
  `Return: new_mechanisms (only if a cluster justifies a NEW cause; set symptoms[]), new_methods (full how-to body pl+en, conditions, addresses[] edges with honest evidence + community + note, resources[] = the nuggets with their timestamped url, type video, author), ` +
  `enrichments (resources to attach to EXISTING methods). Evidence honest: a bare claim is C; B/A only with study/mechanism. Slugs lowercase-hyphen ASCII. Prefer enriching over near-duplicates.`,
  { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA }
)
return { nuggetCount: allNuggets.length, newMechanisms: synth.new_mechanisms.length, newMethods: synth.new_methods.length, enrichments: synth.enrichments.length, synth }
