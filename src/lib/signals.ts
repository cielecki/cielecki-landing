// Ranking helpers for the two-signal graph model (evidence + community).
export const evRank: Record<string, number> = { A: 4, B: 3, C: 2, D: 1 };
export const commRank: Record<string, number> = { wysoki: 3, 'średni': 2, niski: 1, brak: 0 };

// Evidence dominates the sort; community breaks ties.
export function edgeScore(evidence: string, community: string): number {
  return (evRank[evidence] ?? 0) * 10 + (commRank[community] ?? 0);
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
