// Navigation taxonomy for the Neuro Toolkit graph. Mirrors the FROZEN canonical
// symptom grouping in docs/neuro-toolkit/taxonomy.md (6 themes + caregiver mode).
// Used by the index directory and the persistent topic sidebar so the 20 entry
// points are browsable by theme instead of one long flat list.
import type { Lang } from '../i18n/ui';

export interface NavGroup {
  id: string;
  label: Record<Lang, string>;
  symptoms: string[]; // slugs, in display order
}

export const NAV_GROUPS: NavGroup[] = [
  {
    id: 'codziennosc',
    label: { pl: 'Codzienność i ciało', en: 'Everyday & body' },
    symptoms: ['zaczynanie', 'chaos-czas-organizacja', 'sen', 'energia-wypalenie'],
  },
  {
    id: 'glowa-emocje',
    label: { pl: 'Głowa i emocje', en: 'Mind & emotions' },
    symptoms: [
      'emocje-rozregulowane',
      'pamiec-mysli',
      'lek-unikanie',
      'odrzucenie-rsd',
      'samoocena-wstyd',
      'depresja-sens',
    ],
  },
  {
    id: 'ja-tozsamosc',
    label: { pl: 'Ja i tożsamość', en: 'Self & identity' },
    symptoms: ['diagnoza', 'maskowanie-tozsamosc'],
  },
  {
    id: 'ludzie-relacje',
    label: { pl: 'Ludzie i relacje', en: 'People & relationships' },
    symptoms: ['relacje-spoleczne', 'randki-zwiazki', 'seks-porno-wstyd'],
  },
  {
    id: 'kontrola-kierunek',
    label: { pl: 'Kontrola i kierunek', en: 'Control & direction' },
    symptoms: ['uzaleznienia', 'praca-kariera', 'trauma-przeszlosc', 'szukam-pomocy'],
  },
  {
    id: 'opiekun',
    label: { pl: 'Tryb opiekuna', en: 'Caregiver mode' },
    symptoms: ['rodzicielstwo-bliscy'],
  },
];

export interface NavItem {
  slug: string;
  title: string;
  icon: string;
  conditions: string[]; // which profiles this topic applies to (for the filter)
}
export interface ResolvedGroup {
  id: string;
  label: string;
  items: NavItem[];
  conditions: string[]; // UNION of member conditions — lets the whole group hide when empty
}

const ALL_CONDITIONS = ['adhd', 'autism', 'audhd'];
type SymptomEntry = { id: string; data: { title: string; icon: string; conditions?: string[] } };

// Resolve the frozen group structure against the symptoms that actually exist
// in this language, so unpublished topics never render as dead links.
export function buildNav(entries: SymptomEntry[], lang: Lang): ResolvedGroup[] {
  const map = new Map(entries.map((e) => [e.id.split('/').pop()!, e]));
  const groups: ResolvedGroup[] = [];
  for (const g of NAV_GROUPS) {
    const items: NavItem[] = [];
    for (const slug of g.symptoms) {
      const e = map.get(slug);
      if (e) items.push({ slug, title: e.data.title, icon: e.data.icon, conditions: e.data.conditions ?? ALL_CONDITIONS });
    }
    if (items.length) {
      const conditions = [...new Set(items.flatMap((it) => it.conditions))];
      groups.push({ id: g.id, label: g.label[lang], items, conditions });
    }
  }
  return groups;
}
