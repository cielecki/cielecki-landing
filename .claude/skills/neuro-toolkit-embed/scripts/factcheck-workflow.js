// Neuro Toolkit fact-check workflow.
// args = JSON array of { slug, title, body } (mechanisms or methods to verify).
// Each agent identifies the central FACTUAL/neuroscience claims, web-verifies them
// against reputable sources, and returns a verdict + real citation + a suggested
// fix for anything overstated/contested. Batched (529 defense) + resilient.
// Apply results by hand (judgment): add citations to confirmed claims, soften the rest.
export const meta = {
  name: 'nt-factcheck',
  description: 'Web-verify the factual claims in Neuro Toolkit mechanisms/methods',
  phases: [{ title: 'Verify' }],
}

const FINDING = {
  type: 'object', additionalProperties: false,
  properties: {
    claim: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'overstated', 'contested', 'unsupported'] },
    source_url: { type: 'string' }, source_title: { type: 'string' },
    note_pl: { type: 'string' }, note_en: { type: 'string' },
    fix_pl: { type: 'string' }, fix_en: { type: 'string' },
  },
  required: ['claim', 'verdict', 'note_en'],
}
const RESULT = {
  type: 'object', additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    overall: { type: 'string', enum: ['solid', 'mixed', 'dubious'] },
    findings: { type: 'array', items: FINDING },
  },
  required: ['slug', 'overall', 'findings'],
}
const SCHEMA = { type: 'object', additionalProperties: false, properties: { result: RESULT }, required: ['result'] }

phase('Verify')
const items = typeof args === 'string' ? JSON.parse(args) : args
const BATCH = 3
const verifyOne = (m) => agent(
  `You are fact-checking an ADHD/autism/AuDHD knowledge-base entry. Be a skeptical scientist.\n` +
  `SLUG: ${m.slug}\nTITLE: ${m.title}\nTEXT:\n${m.body}\n\n` +
  `1) Identify the 1-3 central FACTUAL / neuroscience claims (ignore lived-experience framing and advice — only check checkable facts).\n` +
  `2) For each, run 1-3 web searches and judge against REPUTABLE sources (peer-reviewed papers, Barkley, established clinical bodies — NOT random blogs or single influencers).\n` +
  `3) Be especially skeptical of pop-neuroscience: specific dopamine numbers, 'object permanence' as an ADHD mechanism, single-podcaster claims, evolutionary just-so stories.\n` +
  `Return per claim: verdict (confirmed / overstated / contested / unsupported), the best real source_url + source_title, note_en (one line on what the evidence says), and — only if NOT confirmed — fix_pl + fix_en: a short hedge/correction to splice into the body. Set overall = solid / mixed / dubious.`,
  { label: `verify:${m.slug}`, phase: 'Verify', schema: SCHEMA }
).then((r) => (r && r.result) || null).catch(() => null)

const results = new Map()
async function runBatches(list, tag) {
  for (let i = 0; i < list.length; i += BATCH) {
    const chunk = list.slice(i, i + BATCH)
    const res = await parallel(chunk.map((m) => () => verifyOne(m)))
    for (let j = 0; j < chunk.length; j++) if (res[j]) results.set(chunk[j].slug, res[j])
    log(`${tag}: ${results.size}/${items.length} verified`)
  }
}
await runBatches(items, 'pass1')
const failed = items.filter((m) => !results.has(m.slug))
if (failed.length) { log(`retrying ${failed.length}`); await runBatches(failed, 'retry') }

const out = [...results.values()]
const flags = out.filter((r) => r.overall !== 'solid')
return { verified: out.length, of: items.length, dubiousOrMixed: flags.map((r) => r.slug), results: out }
