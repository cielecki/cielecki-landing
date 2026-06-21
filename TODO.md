# Neuro Toolkit — TODO / status

Status tego, co zostało do zrobienia w bazie `/nt/`. Model + konwencje: [CLAUDE.md](CLAUDE.md)
i [docs/neuro-toolkit/](docs/neuro-toolkit/). Aktualizuj ten plik przy każdej większej zmianie.

Stan: **20 objawów · 22 mechanizmy · 87 metod**, bilingualnie. Deploy: push na `main` → GitHub Pages (cielecki.com).

---

## 🔜 Do zrobienia

### 1. Pełny przemiał ocen + badań  ⏳ `4 / 87 metod`
Kalibracja każdej oceny A–D względem literatury + realne cytowania (sekcja „Co mówią badania").
- [ ] Przemielić pozostałe **83 metody** — małymi partiami (5–6 naraz), z ręczną weryfikacją każdego cytowania
- [ ] Fact-check pozostałych **~16 mechanizmów** (treść + cytowania w „Tło")
- **Jak:** skill `neuro-toolkit-embed` → `prep_grades.py` → `gradecheck-workflow.js` (Workflow) → `apply_grades.py`
  (downgrade auto, upgrade po przeglądzie: `--upgrade-slugs`). Recepta na 529: małe runy, batch 2, retry.
- **Zasada:** ZAWSZE sprawdź, czy URL cytowania się rozwiązuje i tytuł się zgadza, zanim zaufasz syntezie.

### 2. Wyszukiwarka (po wszystkim)
- [ ] Pełnotekstowe wyszukiwanie po objawach / mechanizmach / metodach / treści / źródłach
- **Rekomendacja:** [Pagefind](https://pagefind.app) — indeksuje zbudowany statyczny HTML, zero-config,
  działa bez backendu (idealne pod GitHub Pages). Dodać do nagłówka (ikona lupy → modal) + skrót `/`.
- Alternatywa: prebuilt JSON index + Fuse.js (więcej roboty, mniej „za darmo").

### 3. Stopka + mapa strony (sitemap)
- [ ] Porządny footer na dole każdej strony z **mapą bazy**: wszystkie objawy pogrupowane wg kategorii
      (TEMATY), + linki: O projekcie / Disclaimer medyczny / przełącznik języka / (docelowo) grupa założycieli
- [ ] `sitemap.xml` dla SEO — `@astrojs/sitemap` (osobne od footera; maszynowe)

### 4. Kuracja (jakość treści)
- [ ] Przejść 87 metod pod kątem near-duplikatów / przegenerowania → scalić / przyciąć
- [ ] Dorobić głębię cienkim objawom (część ma 1–2 metody) — kolejne małe runy harvestu
- [ ] **Audyt szerokości krawędzi metoda→mechanizm.** Trawersja jest tranzytywna (metoda celująca
      w mechanizm pokazuje się pod wszystkimi objawami tego mechanizmu — i odwrotnie). Skutek: luźne
      skojarzenia, np. „Dwa konta + znajomy na impuls" pokazuje się pod „Nie mogę zacząć" (wspólny
      mechanizm Deficyt dopaminy). Przejrzeć, czy takie krawędzie metoda→mechanizm nie są za szerokie;
      jeśli tak — zawęzić do bezpośredniej krawędzi metoda→objaw albo usunąć krawędź do mechanizmu.

### 5. Polish wizualny / launch
- [ ] Color-coding ADHD / autyzm / AuDHD (rozważyć — czy nie zaszumi)
- [ ] **Launch: link z homepage** — DOPIERO po skończeniu bazy + Twoim wizualnym QA + Twoim „tak"
- [ ] Link do grupy WhatsApp założycieli ADHD/autyzm

---

## ✅ Zrobione

- Model grafowy (objaw → mechanizm → metoda), jedna struktura `/nt/[lang]/`; stary płaski model zwinięty + redirecty
- Dwa niezależne sygnały: **dowód A–D** (per-krawędź) + **liczba źródeł** (z `resources[]`); legenda A–D + tooltipy
- Linki do **konkretnej sekundy** filmu (fragment od MM:SS)
- Filtr profilu (ADHD / autyzm / AuDHD) + notka „nie dla profilu" przy wejściu bezpośrednim
- Powtarzalny pipeline jako skill `neuro-toolkit-embed` (harvest → clean → Workflow → apply → fact-check)
- Spójny układ stron: „Dotyczy" na dole, źródła w nagłówku „Materiały", ocena per-cel w „Pomaga na" (wszystkie 3 typy)
- testy-przesiewowe → A (zweryfikowane: walidacje ASRS/AQ)
