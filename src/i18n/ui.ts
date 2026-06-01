export const languages = ['pl', 'en'] as const;
export type Lang = (typeof languages)[number];
export const defaultLang: Lang = 'pl';

export const languageNames: Record<Lang, string> = {
  pl: 'Polski',
  en: 'English',
};

export const ui = {
  pl: {
    'site.title': 'Baza wiedzy AuDHD',
    'site.tagline': 'Wyzwania ADHD i spektrum autyzmu → sprawdzone metody radzenia sobie.',
    'site.description':
      'Otwarta baza wiedzy o ADHD i autyzmie (AuDHD): zaczynasz od wyzwania, schodzisz do konkretnych metod radzenia sobie i materiałów.',
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
    'breadcrumb.home': 'AuDHD',
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
    'site.title': 'AuDHD knowledge base',
    'site.tagline': 'ADHD & autism-spectrum challenges → field-tested coping methods.',
    'site.description':
      'An open knowledge base on ADHD and autism (AuDHD): start from a challenge, drill down into concrete coping methods and resources.',
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
    'breadcrumb.home': 'AuDHD',
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
