# Neuro Toolkit — model grafu (spec + pilotaż „sen")

Data: 2026-06-04 · status: pilotaż w budowie

## Po co

Dotychczasowy model strony jest płaski i dwuwarstwowy: `challenge → method`. Taksonomia
14 wyzwań została wymyślona z góry („ekspert, który już wie": *maskowanie*, *układ nerwowy*…).
To nie jest język osoby, która szuka pomocy — ona wie tylko, że *„z czymś diluje"* (nie śpi,
spóźnia się, zobowiązuje się i nie robi). Chcemy model, w którym:

1. Wejście jest w języku laika i od razu pokazuje rozwiązanie (bez ściany teorii).
2. Drążenie „dlaczego tak jest" jest opcjonalne, dla ciekawych.
3. Taksonomia wyłania się z **realnych źródeł** (Todoist + WhatsApp + badania), nie z głowy.

## Model: graf trójwarstwowy

Trzy typy węzłów, każdy = osobny plik `.md` (single source of truth, bilingual `pl/`+`en/`):

1. **Symptom** — punkt wejścia, język laika. *„Rozregulowany sen"*, *„Spóźniam się wszędzie"*.
2. **Mechanizm** — *dlaczego* tak jest. Jeden symptom ma wiele mechanizmów.
3. **Metoda / protokół** — co z tym zrobić.

**Krawędzie są wiele-do-wielu i kierunkowe.** Wyrażone jako referencje w frontmatterze
(rozwiązywane przy buildzie — Astro content collections):

- `mechanism.symptoms: [<symptom-slug>...]` — pod jakie symptomy podpina się mechanizm.
- `method.addresses: [{ target, kind: 'mechanism'|'symptom', evidence, community, note }]`
  — metoda może leczyć kilka mechanizmów *i* działać wprost na symptom.

**Dwa osobne sygnały na każdej krawędzi metoda→cel:**

- `evidence`: `A`–`D` — siła dowodu naukowego (A = meta-analiza/RCT … D = anegdota/teoria).
- `community`: `wysoki`|`średni`|`niski`|`brak` — czy ludzie (grupa, własne doświadczenie)
  mówią, że to działa.

Pokazywane **osobno** — czytelnik widzi „mocne w badaniach" vs „ludzie mówią że działa"
i sam waży. Nie udajemy, że anegdota to RCT, ani że brak RCT = bezużyteczne.

**Każdy węzeł** (symptom, mechanizm, metoda) niesie `conditions: [adhd|autism|audhd]` —
filtr profilu działa na całym grafie, nie tylko na metodach. To ortogonalna warstwa tagów
(istniejący segmented control w nagłówku zostaje).

## Drill-down (jak się to czyta)

- **Wejście:** lista symptomów → klik „Rozregulowany sen".
- **Strona symptomu:** OD RAZU top metody (sort: sygnał) — rozwiązanie bez teorii.
  Pod spodem zwijane „Dlaczego tak jest" → mechanizmy.
- **Strona mechanizmu:** krótkie tło (naukowe) + metody ocenione *pod ten mechanizm*.
- **Strona metody:** jak to zrobić + oba sygnały + linki (artykuły/filmy/produkty/naukowe)
  + „Co jeszcze ten protokół rusza" (krawędzie grafu = drill dalej).

## Pilotaż: „Rozregulowany sen" (z realnych źródeł)

Walidujemy model na JEDNYM temacie end-to-end, zanim skalujemy na ~500 źródeł.

**Mechanizmy** (wstępnie, do potwierdzenia w destylacji):
- Hiperfokus / revenge bedtime procrastination (zapominam/odmawiam pójść spać).
- Opóźniona faza dobowa (DSPS) — przesunięty zegar biologiczny.
- Rozregulowany układ nerwowy (hyperarousal, brak „zejścia" wieczorem).
- Nadwrażliwość sensoryczna (hałas, światło) blokująca zaśnięcie.

**Metody + skąd pochodzą:**
- Zatyczki woskowe/piankowe (3M) + ANC — *WhatsApp grupa, community: wysoki*.
- Alarm „kładę się" na HomePodzie / kotwica pory snu — *WhatsApp/system, community: średni*.
- Tonizacja UN / nerw błędny / polyvagal — *Todoist (Porges, „Regulate ADHD Nervous System"), evidence: B/C*.
- Timing światła rano + melatonina wieczorem — *deep research naukowy, evidence: A/B*.
- Wind-down / digital sunset — *research + community*.

**Dostarcza:**
- Nowy schemat (`symptoms`/`mechanisms`/`methods` z krawędziami + dwoma sygnałami + `conditions`).
- Temat „sen" wypełniony prawdziwymi źródłami (nie zmyślone linki).
- Strony renderujące drill-down.
- Wzorzec schematu dla skalowania (podprojekt #2+).

Stary płaski model (`challenges`/`methods`, 14+15 plików) zostaje obok do migracji w kolejnym
kroku — pilota stawiam równolegle, nie burzę istniejącego.

## Poza pilotażem (kolejne podprojekty)

2. Schemat + model danych — zamrożenie grafu na bazie pilota.
3. Migracja całej strony na nowy model + color coding + atrakcyjność dla mózgów neuroatypowych.
4. Pipeline iteracyjny — skill Claude Code + `CLAUDE.md`, żeby dorzucanie nowych źródeł
   (też podsyłanych przez ludzi z grupy) było sprytne i powtarzalne.
