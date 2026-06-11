# Neuro Toolkit — canonical symptom taxonomy (FROZEN 2026-06-11)

Derived bottom-up from 1878 unique video titles across the harvested ADHD/autism/AuDHD
corpus (workflow `nt-taxonomy`: 147 candidate clusters → curated). Approved by Maciej.
This is the canonical entry-point list — the `extract-workflow.js` EXISTING-taxonomy list
must mirror it so synthesis reuses these slugs.

Entry points are first-person lay language ("z czym dilujesz"), grouped for navigation.
Status: ✓ = already populated · ＋ = to create in Faza 4 fill.

## Codzienność i ciało
- ✓ `zaczynanie` — Nie mogę się zebrać / odkładam wszystko [duży]
- ＋ `chaos-czas-organizacja` — Wszystko mi się rozjeżdża: czas, bałagan, organizacja [śred]
- ✓ `sen` — Sen się sypie, wiecznie zmęczony [śred]
- ✓ `energia-wypalenie` — Wypalenie, meltdowny, przeładowanie (wchłania sensorykę) [duży]

## Głowa i emocje
- ✓ `emocje-rozregulowane` — Złość, wstyd, branie do siebie (renamed from `emocje-czarnobiale`) [duży]
- ✓ `pamiec-mysli` — Overthinking, ruminacje, mgła, gubienie myśli [śred]
- ✓ `lek-unikanie` — Lęk, panika, unikanie [duży]
- ＋ `odrzucenie-rsd` — Nadwrażliwość na odrzucenie (RSD) [śred] *(mechanism `rsd` underlies it)*
- ＋ `samoocena-wstyd` — „Jestem zepsuty/bezwartościowy", syndrom oszusta [duży]
- ＋ `depresja-sens` — Pustka, brak sensu [duży] — ⚠️ **SAFETY**: includes suicidal-ideation content. Must lead with crisis resources (PL: **116 123**, **112**, **116 111** for youth) and careful framing; this is signposting + coping, NOT clinical treatment. Disclaimer mandatory.

## Ja i tożsamość
- ＋ `diagnoza` — „Czy ja to mam?" autodiagnoza + diagnoza w dorosłości [duży] ← **largest theme in the corpus**
- ＋ `maskowanie-tozsamosc` — Maskowanie, udawanie, kim jestem [duży]

## Ludzie i relacje
- ＋ `relacje-spoleczne` — Sygnały społeczne, small talk, samotność, przyjaźnie (merges komunikacja + samotność) [duży]
- ＋ `randki-zwiazki` — Randki, związki, granice, męska samotność [duży]
- ＋ `seks-porno-wstyd` — Seks, intymność, wstyd [śred]

## Kontrola i kierunek
- ＋ `uzaleznienia` — Gry, ekrany, scrollowanie, porno-jako-kompulsja, używki [duży]
- ＋ `praca-kariera` — Praca, kariera, „marnuję potencjał" (wchłania pieniądze) [śred]
- ＋ `trauma-przeszlosc` — Trauma, toksyczni rodzice, żałoba [śred]
- ✓ `szukam-pomocy` — Terapia, leki, „co właściwie działa" [śred]

## Tryb opiekuna (osobna grupa — caregiver-facing, NOT first-person)
- ＋ `rodzicielstwo-bliscy` — Wspieram bliskiego z neuroróżnorodnością [śred] — render with a distinct "caregiver lens" treatment so it doesn't read as a personal symptom.

## Fill order (Faza 4) — by corpus volume, highest first
diagnoza · randki-zwiazki · samoocena-wstyd · maskowanie-tozsamosc · uzaleznienia ·
depresja-sens (with safety layer) · relacje-spoleczne · chaos-czas-organizacja ·
odrzucenie-rsd · seks-porno-wstyd · praca-kariera · trauma-przeszlosc · rodzicielstwo-bliscy.
Each symptom: select relevant corpus transcripts → extract-workflow → apply_synth → fact-check → publish (create the symptom entry page TOGETHER with its methods, so no empty topics go live).

## Decisions on record (2026-06-11)
1. Accept the 20-symptom grouped canon. 2. Rename `emocje-czarnobiale` → `emocje-rozregulowane`.
3. `depresja-sens` included WITH crisis lines + careful framing. 4. `rodzicielstwo-bliscy` included as a caregiver-lens entry.
