export const languages = ['pl', 'en'] as const;
export type Lang = (typeof languages)[number];
export const defaultLang: Lang = 'pl';

export const languageNames: Record<Lang, string> = {
  pl: 'Polski',
  en: 'English',
};

export const ui = {
  pl: {
    'site.title': 'Neuro Toolkit',
    'site.tagline': 'Narzędziownik dla mózgu z ADHD, autyzmem lub oboma — sprawdzone sposoby na codzienne wyzwania.',
    'site.description':
      'Neuro Toolkit — narzędziownik dla mózgu z ADHD, autyzmem lub oboma (AuDHD): od wyzwania do konkretnych sposobów radzenia sobie, lifehacków i materiałów.',
    'nav.challenges': 'Wyzwania',
    'nav.allChallenges': 'Wszystkie wyzwania',
    'home.intro':
      'Wybierz wyzwanie, z którym się mierzysz. Pod spodem znajdziesz metody radzenia sobie, a przy każdej — artykuły, filmy i linki.',
    'challenge.methods': 'Metody radzenia sobie',
    'challenge.empty': 'Wkrótce — metody w opracowaniu.',
    'challenge.methodCount': 'metod',
    'method.resources': 'Materiały i linki',
    'method.noResources': 'Brak linków — wkrótce.',
    'method.linkSoon': 'link wkrótce',
    'method.lenses': 'Jak to wygląda zależnie od profilu',
    'nt.pilot': 'pilotaż',
    'nt.intro': 'Zacznij od tego, z czym realnie się mierzysz. Klikasz — i od razu masz sposoby. Jeśli chcesz zrozumieć dlaczego, drążysz głębiej: do mechanizmów i badań.',
    'nt.topMethods': 'Sposoby, które pomagają',
    'nt.topics': 'Tematy',
    'nt.browseTopics': 'Przeglądaj tematy',
    'nt.why': 'Dlaczego tak się dzieje',
    'nt.background': 'Tło',
    'nt.methodsHere': 'Sposoby na ten mechanizm',
    'nt.alsoTouches': 'Co jeszcze ten sposób rusza',
    'nt.evidence': 'Dowód naukowy',
    'nt.community': 'Ludzie mówią',
    'nt.appliesTo': 'Dotyczy',
    'nt.helpsWith': 'Pomaga na',
    'nt.howProven': 'Na ile to potwierdzone',
    'type.symptom': 'Objaw',
    'type.mechanism': 'Mechanizm',
    'type.method': 'Sposób',
    'ev.A': 'A · mocny (RCT / meta-analiza)',
    'ev.B': 'B · dobry',
    'ev.C': 'C · słaby / wstępny',
    'ev.D': 'D · brak / teoria',
    'comm.wysoki': 'wysoki',
    'comm.średni': 'średni',
    'comm.niski': 'niski',
    'comm.brak': 'brak',
    'filter.label': 'Dla kogo:',
    'filter.all': 'Wszystko',
    'filter.adhd': 'ADHD',
    'filter.autism': 'Autyzm',
    'filter.audhd': 'AuDHD',
    'filter.hidden': 'ukrytych dla tego profilu',
    'filter.showAll': 'pokaż wszystko',
    'profile.adhd': 'ADHD',
    'profile.autism': 'Autyzm',
    'profile.audhd': 'AuDHD',
    'breadcrumb.home': 'Neuro Toolkit',
    'footer.disclaimer':
      'To nie jest porada medyczna. Baza tworzona przez społeczność osób z ADHD/autyzmem — zawsze konsultuj się ze specjalistą.',
    'resource.video': 'Film',
    'resource.article': 'Artykuł',
    'resource.book': 'Książka',
    'resource.podcast': 'Podcast',
    'resource.app': 'Aplikacja',
    'resource.product': 'Produkt',
    'resource.tool': 'Narzędzie',
    'resource.specialist': 'Specjalista',
  },
  en: {
    'site.title': 'Neuro Toolkit',
    'site.tagline': 'A toolkit for brains with ADHD, autism, or both — field-tested ways for everyday challenges.',
    'site.description':
      'Neuro Toolkit — for brains with ADHD, autism, or both (AuDHD): from a challenge to concrete coping methods, lifehacks and resources.',
    'nav.challenges': 'Challenges',
    'nav.allChallenges': 'All challenges',
    'home.intro':
      'Pick the challenge you are facing. Underneath you will find coping methods, and for each one — articles, videos and links.',
    'challenge.methods': 'Coping methods',
    'challenge.empty': 'Coming soon — methods in the works.',
    'challenge.methodCount': 'methods',
    'method.resources': 'Resources & links',
    'method.noResources': 'No links yet — coming soon.',
    'method.linkSoon': 'link soon',
    'method.lenses': 'How this differs by profile',
    'nt.pilot': 'pilot',
    'nt.intro': 'Start from what you are actually dealing with. Click — and you get methods straight away. If you want to understand why, drill deeper: into mechanisms and the research.',
    'nt.topMethods': 'Methods that help',
    'nt.topics': 'Topics',
    'nt.browseTopics': 'Browse topics',
    'nt.why': 'Why this happens',
    'nt.background': 'Background',
    'nt.methodsHere': 'Methods for this mechanism',
    'nt.alsoTouches': 'What else this method touches',
    'nt.evidence': 'Scientific evidence',
    'nt.community': 'People say',
    'nt.appliesTo': 'Applies to',
    'nt.helpsWith': 'Helps with',
    'nt.howProven': 'How proven this is',
    'type.symptom': 'Symptom',
    'type.mechanism': 'Mechanism',
    'type.method': 'Method',
    'ev.A': 'A · strong (RCT / meta-analysis)',
    'ev.B': 'B · good',
    'ev.C': 'C · weak / preliminary',
    'ev.D': 'D · none / theory',
    'comm.wysoki': 'high',
    'comm.średni': 'medium',
    'comm.niski': 'low',
    'comm.brak': 'none',
    'filter.label': 'For whom:',
    'filter.all': 'Everything',
    'filter.adhd': 'ADHD',
    'filter.autism': 'Autism',
    'filter.audhd': 'AuDHD',
    'filter.hidden': 'hidden for this profile',
    'filter.showAll': 'show all',
    'profile.adhd': 'ADHD',
    'profile.autism': 'Autism',
    'profile.audhd': 'AuDHD',
    'breadcrumb.home': 'Neuro Toolkit',
    'footer.disclaimer':
      'This is not medical advice. Built by a community of people with ADHD/autism — always consult a professional.',
    'resource.video': 'Video',
    'resource.article': 'Article',
    'resource.book': 'Book',
    'resource.podcast': 'Podcast',
    'resource.app': 'App',
    'resource.product': 'Product',
    'resource.tool': 'Tool',
    'resource.specialist': 'Specialist',
  },
} as const;

export type UIKey = keyof (typeof ui)['pl'];

export function useTranslations(lang: Lang) {
  return function t(key: UIKey): string {
    return ui[lang][key] ?? ui[defaultLang][key];
  };
}

export function otherLang(lang: Lang): Lang {
  return lang === 'pl' ? 'en' : 'pl';
}
