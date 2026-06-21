// Ranking helpers for the two-signal graph model (evidence + sources).
export const evRank: Record<string, number> = { A: 4, B: 3, C: 2, D: 1 };

// Evidence badge colour — MONOTONIC: stronger evidence is more saturated, weaker
// fades to neutral grey. (Was inverted: C in warm sand stood out more than B.)
// One hue (sage/green) for A–B so "backed" reads instantly; C–D go grey.
export const evidenceClass: Record<string, string> = {
  A: 'bg-sage/40 text-sage-dark ring-1 ring-sage/30',
  B: 'bg-sage/20 text-sage-dark',
  C: 'bg-charcoal/12 text-charcoal-light',
  D: 'bg-charcoal/8 text-charcoal-light/90',
};
// When a grade has no direct studies behind it (just a mechanism/experience estimate),
// it renders greyed regardless of letter — the letter still shows, the colour says "unverified".
export const evidenceMutedClass = 'bg-charcoal/6 text-charcoal-light/55';
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
