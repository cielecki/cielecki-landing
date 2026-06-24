// Neuro Toolkit extraction workflow — TEMPLATE (resilient/batched).
// Invoke via the Workflow tool with args = JSON array of { id, title, path, url }.
// Phase 1 (Extract): transcripts processed in SMALL BATCHES (avoids the rate-limit
//   that killed a 22-agent fan-out) -> structured nuggets, failures degrade to [].
// Phase 2 (Synthesize): cluster all nuggets -> new_mechanisms / new_methods /
//   enrichments aligned to content.config.ts. Guarded against a null (rate-limited)
//   synth so the run returns whatever nuggets it got instead of crashing.
// args may arrive as a JSON string — the `sources` line handles both.
// Edit the EXISTING-taxonomy list in the synth prompt before each run.
export const meta = {
  name: 'nt-extract',
  description: 'Extract nuggets from cleaned transcripts and synthesize graph additions (batched, resilient)',
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
const BATCH = 2 // 529 overload defense: minimal concurrency + keep runs SHORT (few transcripts) to avoid long-exposure stalls
const extractOne = (s) => agent(
  `You are mining a transcript for a knowledge base helping neurodivergent people (ADHD / autism / AuDHD).\n` +
  `Read the file at: ${s.path}\nVideo: "${s.title}"   base url: ${s.url}\n` +
  `Lines: [H:MM:SS | <url>&t=Ns] spoken text.\n` +
  `Extract up to 12 CONCRETE, actionable or genuinely-instructive nuggets. Skip filler/sponsor/intro. ` +
  `Per nugget: claim_pl + claim_en, timestamp_s (line start second), kind, evidence_hint (A best..D; be conservative — a bare claim is usually C), ` +
  `mechanism_hint, method_hint, verbatim. Return few/zero if little relevant content — don't pad.`,
  { label: `extract:${s.id}`, phase: 'Extract', schema: NUGGET_SCHEMA }
).then((r) => ({ source: s, nuggets: (r && r.nuggets) || [] })).catch(() => ({ source: s, nuggets: [] }))

const results = new Map() // id -> { source, nuggets }
async function runBatches(list, tag) {
  for (let i = 0; i < list.length; i += BATCH) {
    const chunk = list.slice(i, i + BATCH)
    const res = await parallel(chunk.map((s) => () => extractOne(s)))
    for (const b of res.filter(Boolean)) results.set(b.source.id, b)
    const ok = [...results.values()].filter((x) => x.nuggets.length).length
    log(`${tag} batch ${Math.floor(i / BATCH) + 1}: ${ok}/${sources.length} transcripts ok`)
  }
}
await runBatches(sources, 'pass1')
// retry transcripts the throttle dropped (0 nuggets) — gives full coverage in one slower run
const failed = sources.filter((s) => !(results.get(s.id) && results.get(s.id).nuggets.length))
if (failed.length) { log(`retrying ${failed.length} empty/rate-limited transcripts`); await runBatches(failed, 'retry') }

const allNuggets = []
let okCount = 0
for (const b of results.values()) {
  if (b.nuggets.length) okCount++
  for (const n of b.nuggets)
    allNuggets.push({ claim_pl: n.claim_pl, claim_en: n.claim_en, kind: n.kind, evidence_hint: n.evidence_hint,
      mechanism_hint: n.mechanism_hint || '', method_hint: n.method_hint || '', verbatim: n.verbatim || '',
      source_title: b.source.title, url: `${b.source.url}&t=${Math.round(n.timestamp_s)}s` })
}
log(`extracted ${allNuggets.length} nuggets from ${okCount}/${sources.length} transcripts`)

if (!allNuggets.length) return { error: 'no nuggets extracted (all transcripts failed/rate-limited)', nuggetCount: 0 }

phase('Synthesize')
const synthPrompt =
  `Design graph ADDITIONS for a neurodivergent knowledge base. Polish first, mirror in English.\n` +
  `EXISTING taxonomy — REUSE these slugs, never duplicate (see docs/neuro-toolkit/taxonomy.md):\n` +
  `- symptoms: sen, zaczynanie, chaos-czas-organizacja, energia-wypalenie, emocje-rozregulowane, pamiec-mysli, lek-unikanie, odrzucenie-rsd, samoocena-wstyd, depresja-sens, diagnoza, maskowanie-tozsamosc, relacje-spoleczne, randki-zwiazki, seks-porno-wstyd, uzaleznienia, praca-kariera, trauma-przeszlosc, szukam-pomocy, rodzicielstwo-bliscy\n` +
  `- mechanisms: revenge-bedtime, opozniona-faza, pobudzony-uklad, sensoryczne-zaklocenia, nocny-zryw, chroniczna-czujnosc, dlug-snu-presja, rsd, slaba-pamiec-robocza\n` +
  `Nuggets (each carries a timestamped url):\n${JSON.stringify(allNuggets)}\n\n` +
  `VOICE (critical): write bodies as IMPERSONAL, general knowledge — NOT a recap of one person's video. No named non-experts ("z doświadczenia Magdaleny", "autorka", "klientka"), no first person, no "in this video". A named expert/researcher/clinician may appear only as a LIGHT citation. State the principle generally; the specific anecdote lives in the resource, not the body.\n` +
  `TRAVERSAL: a method shows under a symptom ONLY via a DIRECT edge — so in addresses[] add a kind:'symptom' edge for EVERY symptom the method genuinely helps (do NOT rely on a mechanism to carry it onto symptoms). Add kind:'mechanism' for the underlying cause(s). Mechanisms are the "why" layer, not method routing.\n` +
  `Return: new_mechanisms (only if a cluster justifies a NEW cause; set symptoms[] = ONLY symptoms it directly underlies — keep tight, a broad symptoms[] sprays every method onto unrelated symptoms), new_methods (full how-to body pl+en, conditions, addresses[] edges with honest evidence + note, resources[] = the nuggets with their timestamped url, type video, author = the VIDEO TITLE), ` +
  `enrichments (resources to attach to EXISTING methods). Evidence honest: a bare claim is C; B/A only with study/mechanism. Slugs lowercase-hyphen ASCII (NO Polish letters). Prefer enriching over near-duplicates.`
let synth = await agent(synthPrompt, { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA })
if (!synth) synth = await agent(synthPrompt, { label: 'synthesize-retry', phase: 'Synthesize', schema: SYNTH_SCHEMA })
if (!synth) return { error: 'synthesis failed (rate-limited)', nuggetCount: allNuggets.length, nuggets: allNuggets }

return { nuggetCount: allNuggets.length, transcriptsOk: okCount, newMechanisms: synth.new_mechanisms.length, newMethods: synth.new_methods.length, enrichments: synth.enrichments.length, synth }
