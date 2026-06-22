# Neuro Toolkit — TODO / status

Status tego, co zostało do zrobienia w bazie `/nt/`. Model + konwencje: [CLAUDE.md](CLAUDE.md)
i [docs/neuro-toolkit/](docs/neuro-toolkit/). Aktualizuj ten plik przy każdej większej zmianie.

Stan: **20 objawów · 22 mechanizmy · 87 metod**, bilingualnie. Deploy: push na `main` → GitHub Pages (cielecki.com).

---

## 🔜 Do zrobienia

### 1. Pełny przemiał ocen + badań  ✅ `87 / 87 metod`
Kalibracja każdej oceny A–D względem literatury + realne cytowania (sekcja „Co mówią badania").
- [x] Przemielono **wszystkie 87 metod** (14 partii po ~6, batche 1–14), każde cytowanie zweryfikowane
      tytułem przez NCBI eutils. Rozkład krawędzi: **A=4, B=45, C=121, D=11**. Wyłapano i usunięto
      kilka zhalucynowanych PMID-ów (m.in. badanie kwetiapiny i pracę fizyczną DESY podszyte pod „badania").
- [x] Fact-check **wszystkich 22 mechanizmów** (runy A–C, `factcheck-workflow.js`): zweryfikowano twierdzenia
      neuro/faktualne, złagodzono przesadzone (m.in. boom-and-bust „endorfiny"→dopamina; revenge-bedtime
      „autonomia" = popnauka, nie konsensus; RSD jako konstrukt Dodsona z cienkim zapleczem; DLMO 45/90 wg
      wieku; supernormalny-bodziec — liczby dopaminy i status „uzależnienia" oznaczone jako sporne).
- **Jak:** skill `neuro-toolkit-embed` → `prep_grades.py` → `gradecheck-workflow.js` (Workflow) → `apply_grades.py`
  (downgrade auto, upgrade po przeglądzie: `--upgrade-slugs`). Recepta na 529: małe runy, batch 2, retry.
- **Narzędzie weryfikacji:** `/tmp/verify_batch.py` (auto-sprawdza wszystkie PubMed/PMC przez eutils:
  tytuł+rok, flaguje mismatch/halucynacje). ZAWSZE uruchamiaj przed `apply_grades`.

### 2. Wyszukiwarka (po wszystkim) ✅
- [x] Pełnotekstowe wyszukiwanie po objawach / mechanizmach / metodach / treści — **Pagefind**, ikona lupy
      w nagłówku → modal, skrót `/`, indeks per-język (pl/en), zakres = `data-pagefind-body` na `<main>` (pomija landing).
      Build: `astro build && pagefind --site dist`. Działa po publikacji (potrzebuje `/pagefind/` z builda).

### 3. Stopka + mapa strony (sitemap) ✅
- [x] Footer (`NtFooter.astro`) na dole każdej strony `/nt/` z **mapą bazy**: 20 objawów pogrupowanych
      wg TEMATÓW + about + disclaimer + przełącznik języka + link do cielecki.com
- [x] `sitemap.xml` — `@astrojs/sitemap` (261 URL-i, sitemap-index)
- [ ] (opcjonalnie później) link do grupy założycieli w footerze — patrz pkt 5

### 4. Kuracja (jakość treści)
- [x] Przejść 87 metod pod kątem near-duplikatów → **brak realnych duplikatów** (analiza podobieństwa
      tytuł+summary: najwyższe pary sim ≤0.36 to komplementarne metody, nie duplikaty — np. światło rano vs
      melatonina wieczór). Korpus już odkurzony dyscypliną „wzbogacaj zamiast duplikować".
- [ ] **Dorobić głębię 3 cienkim objawom** (trawersja tranzytywna): `trauma-przeszlosc` (1 metoda),
      `szukam-pomocy` (1), `rodzicielstwo-bliscy` (2). ⛔ Wymaga NOWEGO materiału źródłowego (harvest filmów) —
      metod się nie zmyśla, więc to czeka na źródła + run harvestu, nie na samo przeliczenie.
- [x] **Audyt szerokości krawędzi metoda→mechanizm** (1. przejście). Przejrzano 37 metod / 55
      tranzytywnych linków. Usunięto 6 jednoznacznie za szerokich krawędzi do mechanizmów (niskoocenowe
      C/D rozsmarowujące wąską metodę na niepowiązany objaw, przy zachowanych trafnych krawędziach
      bezpośrednich): dwa-konta, limit-czasu-na-swipe, polka-pomyslow (→ deficyt-dopaminy); planuj-intymnosc
      (→ deficyt-funkcji-wykonawczych); randka-aktywna, sensoryczne-kotwiczenie-w-seksie (→ sensoryczne-zaklocenia).
      Resztę (RSD→emocje/lęk, pętla paraliżu→chaos/energia, pamięć robocza, maskowanie→wypalenie) zostawiono
      jako trafny rozrzut. Narzędzie: `/tmp/edge_audit.py` (raport zasięgu) — przy kolejnym przemiale przejrzeć borderline'y.

### 5. Polish wizualny / launch
- [x] Color-coding ADHD / autyzm / AuDHD — **ODRZUCONE** (wdrożone i cofnięte 2026-06-22). Per-karta
      „to ADHD czy autyzm" jest dla użytkownika bez znaczenia (po wybraniu profilu już go to nie obchodzi),
      a wizualnie psuło karty. Nie wracać do tego.
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
- **Przemiał ocen wszystkich 87 metod** (batche 1–14): każda ocena A–D skalibrowana z literaturą,
  realne cytowania w „Co mówią badania", każdy PubMed/PMC zweryfikowany tytułem przez NCBI eutils
- **Wyszukiwarka (Pagefind)** — nagłówek + skrót `/` + modal, indeks per-język, zakres `/nt/`
- **Footer z mapą bazy + `sitemap.xml`** (@astrojs/sitemap, 261 URL-i)
- **Audyt szerokości krawędzi** (1. przejście) — usunięto 6 za szerokich krawędzi metoda→mechanizm
