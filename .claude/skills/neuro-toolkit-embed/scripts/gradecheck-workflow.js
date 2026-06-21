// Neuro Toolkit EVIDENCE-GRADE verification workflow.
// args = JSON array from prep_grades.py: [{slug,title,summary,body,conditions,targets,sources}].
// For each method, a skeptical-scientist agent searches the SCIENTIFIC LITERATURE for
// the efficacy of that method for its targets, assigns a defensible A-D grade per the
// taxonomy below, and returns REAL citations. Conservative: downgrade on uncertainty,
// never invent a study. Apply with apply_grades.py (auto-downgrade, flag upgrades).
//
// Grade taxonomy (must match what the site shows):
//   A meta-analysis / systematic review / multiple RCTs
//   B >=1 RCT or consistent controlled studies; or strong mechanism w/ supporting trials
//   C small/uncontrolled/indirect studies; strong mechanism, little direct test; clinical consensus
//   D no empirical test — theory / single voice / lived experience
export const meta = {
  name: 'nt-gradecheck',
  description: 'Verify Neuro Toolkit evidence grades (A-D) against the scientific literature',
  phases: [{ title: 'Literature' }],
}

const STUDY = {
  type: 'object', additionalProperties: false,
  properties: {
    title: { type: 'string' },
    url: { type: 'string', description: 'real URL actually found — prefer PubMed/DOI/Cochrane' },
    year: { type: 'integer' },
    type: { type: 'string', enum: ['meta-analysis', 'rct', 'cohort', 'review', 'guideline', 'other'] },
    finding_pl: { type: 'string' },
    finding_en: { type: 'string' },
  },
  required: ['title', 'type', 'finding_en'],
}
const PER_TARGET = {
  type: 'object', additionalProperties: false,
  properties: {
    target: { type: 'string' },
    grade: { type: 'string', enum: ['A', 'B', 'C', 'D'] },
  },
  required: ['target', 'grade'],
}
const RESULT = {
  type: 'object', additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    recommended_grade: { type: 'string', enum: ['A', 'B', 'C', 'D'] },
    confidence: { type: 'string', enum: ['high', 'med', 'low'] },
    no_direct_evidence: { type: 'boolean', description: 'true if no study directly tests this method->target' },
    studies: { type: 'array', items: STUDY },
    per_target: { type: 'array', items: PER_TARGET, description: 'only where a target differs from recommended_grade' },
    rationale_pl: { type: 'string' },
    rationale_en: { type: 'string' },
  },
  required: ['slug', 'recommended_grade', 'confidence', 'no_direct_evidence', 'studies', 'rationale_en'],
}
const SCHEMA = { type: 'object', additionalProperties: false, properties: { result: RESULT }, required: ['result'] }

phase('Literature')
const items = typeof args === 'string' ? JSON.parse(args) : args
const BATCH = 2 // web-search agents are heavy; keep concurrency low (529 defense)

const gradeOne = (m) => {
  const targets = (m.targets || []).map((t) => `"${t.name}" [slug: ${t.target}, kind: ${t.kind}] (obecna ocena: ${t.evidence})`).join('; ')
  return agent(
    `You are a skeptical evidence-based-medicine researcher grading an ADHD/autism/AuDHD coping method ` +
    `against the SCIENTIFIC LITERATURE. Output is data, not prose.\n\n` +
    `METHOD: ${m.title}\nWHAT IT IS: ${m.summary}\nBODY:\n${m.body}\n\n` +
    `IT CLAIMS TO HELP: ${targets}\n\n` +
    `TASK:\n` +
    `1) State the core efficacy claim ("${m.title} improves [target] for people with ADHD/autism").\n` +
    `2) Run 2-4 literature searches (PubMed, Cochrane, systematic reviews, Google Scholar). Phrase real queries.\n` +
    `3) Find the BEST available evidence specifically for this method→target. Source hierarchy:\n` +
    `   meta-analysis/Cochrane > RCT > cohort/observational > narrative review/clinical guideline > anecdote.\n` +
    `4) Assign recommended_grade by this taxonomy:\n` +
    `   A = meta-analysis / systematic review / multiple RCTs.\n` +
    `   B = >=1 RCT or consistent controlled studies; or strong mechanism w/ supporting trials.\n` +
    `   C = small/uncontrolled/indirect studies; strong mechanism but little direct test; clinical consensus only.\n` +
    `   D = no empirical test — theory / single voice / lived experience.\n` +
    `HARD RULES:\n` +
    `- Be conservative: when the evidence is thin or you are unsure, grade DOWN, not up.\n` +
    `- Cite ONLY studies you actually found in your searches. NEVER invent a title, URL, PMID or DOI.\n` +
    `- If you find no study that directly tests this method→target, set no_direct_evidence=true and grade C or D, ` +
    `and say so plainly in rationale (do not pad with loosely-related papers as if they were direct evidence).\n` +
    `- Prefer URLs that resolve (PubMed /pubmed/NNN, doi.org/..., cochranelibrary.com). Include year + type.\n` +
    `- per_target: only list a target if its evidence genuinely differs from recommended_grade. ` +
    `per_target.target MUST be the exact SLUG shown in brackets above (e.g. "deficyt-dopaminy"), NOT the human name.\n` +
    `- slug: echo back exactly "${m.slug}" unchanged.\n` +
    `Return recommended_grade, confidence, no_direct_evidence, studies[] (real), per_target[], rationale_pl + rationale_en.`,
    { label: `grade:${m.slug}`, phase: 'Literature', schema: SCHEMA }
  // Force the input slug — the model tends to invent a title-derived one, which breaks apply.
  ).then((r) => (r && r.result ? { ...r.result, slug: m.slug } : null)).catch(() => null)
}

const results = new Map()
async function runBatches(list, tag) {
  for (let i = 0; i < list.length; i += BATCH) {
    const chunk = list.slice(i, i + BATCH)
    const res = await parallel(chunk.map((m) => () => gradeOne(m)))
    for (let j = 0; j < chunk.length; j++) if (res[j]) results.set(chunk[j].slug, res[j])
    log(`${tag}: ${results.size}/${items.length} graded`)
  }
}
await runBatches(items, 'pass1')
const failed = items.filter((m) => !results.has(m.slug))
if (failed.length) { log(`retrying ${failed.length}`); await runBatches(failed, 'retry') }

// Reconcile against the current grades so the report highlights changes.
const RANK = { A: 4, B: 3, C: 2, D: 1 }
const current = new Map(items.map((m) => [m.slug, m]))
const out = [...results.values()].map((r) => {
  const m = current.get(r.slug)
  const top = (m?.targets || []).reduce((a, t) => Math.max(a, RANK[t.evidence] || 0), 0)
  const rec = RANK[r.recommended_grade] || 0
  return { ...r, change: rec < top ? 'downgrade' : rec > top ? 'upgrade' : 'same' }
})
const downgrades = out.filter((r) => r.change === 'downgrade').map((r) => r.slug)
const upgrades = out.filter((r) => r.change === 'upgrade').map((r) => r.slug)
const noEvidence = out.filter((r) => r.no_direct_evidence).map((r) => r.slug)
return { graded: out.length, of: items.length, downgrades, upgrades, noEvidence, results: out }
