// Ranking helpers for the two-signal graph model (evidence + sources).
export const evRank: Record<string, number> = { A: 4, B: 3, C: 2, D: 1 };

// Evidence badge style — a SINGLE-HUE green fill ramp (like a signal-strength meter),
// because sage (#8B9D83) is a desaturated green that turns greyish at low opacity, so
// mixing green and grey mid-scale made adjacent grades muddy. Now A→C are the SAME
// green at clearly-stepped fills (~2x apart each), and D drops OFF the green scale to a
// hollow dashed grey ("not on the evidence ladder"). Monotonic by construction.
//   A strong green > B medium green > C faint green > D hollow dashed grey.
export const evidenceClass: Record<string, string> = {
  A: 'bg-sage/75 text-sage-dark border border-transparent',
  B: 'bg-sage/45 text-sage-dark border border-transparent',
  C: 'bg-sage/22 text-sage-dark border border-transparent',
  D: 'text-charcoal-light/75 border border-dashed border-charcoal/35',
};
// No direct studies behind this grade (mechanism/experience estimate) → a dashed,
// hollow grey chip. The dashed outline reads as "provisional, not literature-checked";
// the letter still shows so you can see what the estimate is.
export const evidenceMutedClass = 'text-charcoal-light/65 border border-dashed border-charcoal/25';
export const gradeOrder = ['A', 'B', 'C', 'D'] as const;

// Evidence dominates the sort; the count of independent sources breaks ties.
export function edgeScore(evidence: string, sources = 0): number {
  return (evRank[evidence] ?? 0) * 100 + Math.min(sources, 99);
}

// ── SOURCES SIGNAL ────────────────────────────────────────────────────────────
// Replaces the old, unmeasurable "community" guess. Counts the distinct independent
// voices backing a method: distinct authors, with author-less items falling back to
// their title so two different articles still count as two. Derived straight from
// resources[], so it is verifiable — not an LLM estimate.
type ResourceLike = { author?: string; title?: string; url?: string };
export function sourceCount(resources?: ResourceLike[]): number {
  const seen = new Set<string>();
  for (const r of resources ?? []) {
    const key = (r.author || r.title || r.url || '').trim().toLowerCase();
    if (key) seen.add(key);
  }
  return seen.size;
}

// "1 źródło" · "2–4 źródła" · "5+ źródeł" (Polish plural) / "N source(s)".
export function sourcesLabel(n: number, lang: 'pl' | 'en'): string {
  if (lang === 'en') return `${n} ${n === 1 ? 'source' : 'sources'}`;
  const mod10 = n % 10;
  const mod100 = n % 100;
  let word = 'źródeł';
  if (n === 1) word = 'źródło';
  else if (mod10 >= 2 && mod10 <= 4 && !(mod100 >= 12 && mod100 <= 14)) word = 'źródła';
  return `${n} ${word}`;
}

// Colour weight: more independent voices = stronger.
export function sourceTier(n: number): 'high' | 'mid' | 'low' {
  if (n >= 4) return 'high';
  if (n >= 2) return 'mid';
  return 'low';
}

export const conditionLabel: Record<string, string> = {
  adhd: 'ADHD',
  autism: 'Autism',
  audhd: 'AuDHD',
};
export const conditionIcon: Record<string, string> = {
  adhd: 'mdi:lightning-bolt',
  autism: 'mdi:infinity',
  audhd: 'mdi:yin-yang',
};
// Colour language: ADHD = terracotta, autism = sage, AuDHD = a violet blend of the two.
export const conditionColor: Record<string, string> = {
  adhd: '#A8624A',
  autism: '#6E8268',
  audhd: '#7E6BA8',
};

// Primary profile accent for a card, as a SUBTLE left-border so the type colours
// (terracotta=symptom, sage=method) stay intact while the profile leaning is legible
// at a glance. Matches the active-filter chip colours in AudhdLayout (the legend).
//
// The `audhd` tag is near-universal in this base (almost everything applies to AuDHD),
// so it carries no signal — keying off it paints everything violet. The real signal is
// the ADHD-vs-autism leaning: both present → violet blend; only one → that hue; only the
// bare audhd tag → blend.
export function profileAccent(conditions: string[]): string {
  const s = new Set(conditions);
  const adhd = s.has('adhd');
  const autism = s.has('autism');
  if (adhd && autism) return conditionColor.audhd;
  if (adhd) return conditionColor.adhd;
  if (autism) return conditionColor.autism;
  return conditionColor.audhd;
}
