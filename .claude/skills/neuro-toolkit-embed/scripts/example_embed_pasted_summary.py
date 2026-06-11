#!/usr/bin/env python3
"""Embed the 'Living with ADHD: Courage Over Fear' interview (Magdalena Daniłoś)
into the Neuro Toolkit graph: 6 new symptoms, 2 mechanisms, ~13 methods — each
nugget linked to the exact second of the source video."""
import json, pathlib
BASE = pathlib.Path("/Users/maciel/Documents/Projects/apps/cielecki-landing/src/content")
VID = "https://www.youtube.com/watch?v=8yilaGkSOlo"
AUTHOR = "Magdalena Daniłoś"

def L(sec): return f"{VID}&t={sec}s"
def write(coll, lang, slug, fm, body):
    d = BASE / coll / lang; d.mkdir(parents=True, exist_ok=True)
    fm = dict(fm); fm["lang"] = lang
    (d / f"{slug}.md").write_text("---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---\n\n" + body.strip() + "\n", encoding="utf-8")

# ── SYMPTOMS ───────────────────────────────────────────────────────────────
SYM = [
 ("zaczynanie","mdi:rocket-launch-outline",2,["adhd","autism","audhd"],
  "Nie mogę zacząć (nudne zadania)","Wiesz, że trzeba — papiery, formularz, telefon — a mózg po prostu nie rusza, bo nie ma w tym nowości ani nagrody.",
  "Can't get started (boring tasks)","You know you must — paperwork, a form, a call — but the brain just won't start, because there's no novelty or reward in it.",
  "Mózg z ADHD potrzebuje nowości albo frajdy, żeby ciągnąć nudne zadanie — sama presja działa krótko i długofalowo szkodzi. Niżej masz sposoby, które obniżają próg wejścia: dzielenie na absurdalnie małe kawałki i dokładanie bodźca/nagrody.",
  "An ADHD brain needs novelty or fun to sustain a boring task — pressure alone works short-term and harms long-term. Below are ways to lower the activation threshold: breaking work into absurdly small pieces and adding stimulation/reward."),
 ("lek-unikanie","mdi:weather-lightning",3,["adhd","autism","audhd"],
  "Lęk i unikanie","Odkładasz, omijasz, racjonalizujesz — żeby nie poczuć dyskomfortu. Im bardziej walczysz z lękiem, tym bardziej rośnie.",
  "Fear and avoidance","You delay, dodge, rationalise — anything to not feel the discomfort. The more you fight the fear, the bigger it grows.",
  "Odwaga to nie brak lęku, tylko działanie razem z nim. Celem nie jest usunąć dyskomfort, lecz nauczyć się przy nim być. Niżej: akceptacja lęku zamiast walki, gotowy zestaw uspokajający i trenowanie odwagi na drobiazgach.",
  "Courage isn't the absence of fear — it's acting alongside it. The goal isn't to remove discomfort but to learn to sit with it. Below: accepting fear instead of fighting it, a ready calming kit, and training courage on small things."),
 ("emocje-czarnobiale","mdi:emoticon-sad-outline",4,["adhd","autism","audhd"],
  "Emocje i czarno-białe myślenie","„Albo świetnie, albo beznadziejnie”, „jestem do niczego” — skrajne stany, które wzmacniają cierpienie.",
  "Emotions and black-and-white thinking","'Either great or hopeless', 'I'm useless' — extreme states that amplify suffering.",
  "Mózg ADHD ciągnie do myślenia zero-jedynkowego (fajne/niefajne, skuteczny/leniwy), co pogłębia cierpienie. Niżej: myślenie dialektyczne („i” zamiast „albo”) oraz ciekawość zamiast oceny wobec własnych zachowań.",
  "The ADHD brain leans toward zero-one thinking (fun/not-fun, effective/lazy), which deepens suffering. Below: dialectical thinking ('and' instead of 'either/or') and curiosity instead of judgment toward your own behaviour."),
 ("pamiec-mysli","mdi:thought-bubble-outline",5,["adhd","audhd"],
  "Gubię myśli / przerywam innym","Boisz się, że zapomnisz, więc wpadasz innym w słowo; pomysł nieskapturowany „zjada” pamięć roboczą na cały tydzień.",
  "Losing thoughts / interrupting","You're afraid you'll forget, so you cut others off; an uncaptured thought 'eats' your working memory for a week.",
  "Za przerywaniem i rozproszeniem często stoi słabsza pamięć robocza — lęk przed utratą myśli. Rozwiązaniem nie jest „bardziej się starać”, tylko wyrzucić myśl na zewnątrz: zapisać, zamiast trzymać w głowie.",
  "Behind interrupting and distraction often sits weaker working memory — the fear of losing a thought. The fix isn't 'try harder' but to externalise: write it down instead of holding it in your head."),
 ("energia-wypalenie","mdi:battery-low",6,["adhd","autism","audhd"],
  "Energia i wypalenie","Głowa zapisuje cię na więcej, niż ciało udźwignie; nawet ulubiona praca w hiperfokusie potrafi skończyć się wypaleniem.",
  "Energy and burnout","Your head signs you up for more than the body can carry; even beloved work in hyperfocus can end in burnout.",
  "Zarządzanie energią to fundament życia z ADHD — ważniejsze niż „więcej dyscypliny”. Niżej: audyt energii (must-vs-want, parking, „jutro nowa gra”), aktywny odpoczynek i mówienie wprost, jak działa twój mózg.",
  "Energy management is the foundation of ADHD life — more than 'more discipline'. Below: an energy audit (must-vs-want, a parking lot, 'tomorrow is a new game'), active rest, and saying out loud how your brain works."),
 ("szukam-pomocy","mdi:account-heart-outline",7,["adhd","autism","audhd"],
  "Szukam terapii dopasowanej do mózgu","Próbowałeś terapii i „nie zadziałała”? Modalność ma ogromne znaczenie dla mózgu neuroatypowego — nie każda pasuje.",
  "Looking for therapy that fits the brain","Tried therapy and it 'didn't work'? The modality matters enormously for a neurodivergent brain — not every kind fits.",
  "„Terapia nie działa” często znaczy „ta terapia nie pasowała do tego mózgu”. Niżej: jak dobierać modalność — co bywa trudnym dopasowaniem, a co ma wsparcie badawcze w ADHD.",
  "'Therapy doesn't work' often means 'that therapy didn't fit this brain'. Below: how to choose a modality — what tends to be a hard fit, and what has research support in ADHD."),
]
for slug,icon,order,cond,tp,sp,te,se,bp,be in SYM:
    write("symptoms","pl",slug,{"title":tp,"summary":sp,"icon":icon,"order":order,"conditions":cond},bp)
    write("symptoms","en",slug,{"title":te,"summary":se,"icon":icon,"order":order,"conditions":cond},be)

# ── MECHANISMS ─────────────────────────────────────────────────────────────
MECH = [
 ("rsd","mdi:heart-broken-outline",1,["adhd","audhd"],["emocje-czarnobiale","lek-unikanie"],
  "RSD: nadwrażliwość na odrzucenie","Lata nieafirmujących komunikatów („słomiany zapał”, „leniwa”) osadzają intensywny ból na punkcie odrzucenia i krytyki.",
  "RSD: rejection-sensitive dysphoria","Years of un-affirming messages ('a flash in the pan', 'lazy') lay down an intense pain around rejection and criticism.",
  "RSD (Rejection Sensitive Dysphoria) nie jest oficjalnym kryterium diagnostycznym, ale coraz częściej omawianym zjawiskiem w ADHD. Narasta z lat słyszenia, że jest się „nie w porządku” — aż człowiek sam zaczyna pytać „czy na pewno wszystko ze mną OK?”. Skutek: skrajne reakcje na (czasem wyobrażone) odrzucenie i unikanie sytuacji, które grożą krytyką.",
  "RSD (Rejection Sensitive Dysphoria) is not an official diagnostic criterion but is increasingly discussed in ADHD. It grows from years of hearing you're 'not okay' — until you start asking 'is everything actually right with me?'. The result: extreme reactions to (sometimes imagined) rejection and avoidance of situations that risk criticism."),
 ("slaba-pamiec-robocza","mdi:memory",2,["adhd","audhd"],["pamiec-mysli","zaczynanie"],
  "Słaba pamięć robocza","Myśl, której nie zapiszesz, znika — i mózg „pilnuje” jej kosztem uwagi, napędzając przerywanie i rozproszenie.",
  "Weak working memory","A thought you don't write down vanishes — and the brain 'guards' it at the cost of attention, driving interrupting and distraction.",
  "Słabsza pamięć robocza to jeden z rdzeniowych mechanizmów ADHD. Strach przed zapomnieniem myśli sprawia, że wpadasz innym w słowo albo nie możesz skupić się na rozmowie. Nieskapturowane „zrobię to później” krąży w głowie i zżera zasoby uwagi. Dlatego systemy zewnętrznego zapisu (kartka, notatnik, jeden inbox) działają u ADHD lepiej niż „zapamiętam”.",
  "Weaker working memory is one of ADHD's core mechanisms. Fear of forgetting a thought makes you cut people off or lose focus in conversation. An uncaptured 'I'll do it later' circles in your head and eats attention. That's why external-capture systems (a card, a notebook, a single inbox) work better for ADHD than 'I'll remember'."),
]
for slug,icon,order,cond,syms,tp,sp,te,se,bp,be in MECH:
    write("mechanisms","pl",slug,{"title":tp,"summary":sp,"icon":icon,"order":order,"conditions":cond,"symptoms":syms},bp)
    write("mechanisms","en",slug,{"title":te,"summary":se,"icon":icon,"order":order,"conditions":cond,"symptoms":syms},be)

# ── METHODS ────────────────────────────────────────────────────────────────
def edge(t,k,ev,c,npl=None,nen=None):
    e={"target":t,"kind":k,"evidence":ev,"community":c}
    return (e,npl,nen)
def res(tp,te,sec,npl,nen):
    return {"title_pl":tp,"title_en":te,"url":L(sec),"sec":sec,"npl":npl,"nen":nen}

M = [
 ("male-kawalki","mdi:scatter-plot-outline",8,["adhd","autism","audhd"],
  "Absurdalnie małe kawałki","Pokrój zadanie na śmiesznie małe części (20 min); po pierwszej „torturze” reszta wydaje się łatwa.",
  "Absurdly small chunks","Slice the task into ridiculously small pieces (20 min); after the first '20-minute torture' the rest feels easy.",
  "Ludzie oczekują skoku od „posłuchałem podcastu” do działania o trudności 9, lekceważąc mikro-kroki — a to one są najważniejszą częścią roboty w ADHD. Syn Magdaleny ogarnia 10-godzinny audiobook, tnąc go na „miliard” 20-minutowych kawałków.\n\nUstaw absurdalnie niski próg: nie „napisz raport”, tylko „otwórz dokument i napisz tytuł”. Po przekroczeniu pierwszej bariery rozpęd zwykle niesie dalej.",
  "People expect to jump from 'I listened to a podcast' to a difficulty-9 action, dismissing the micro-steps — yet those are the most important part of the work in ADHD. Magdalena's son tackles a 10-hour audiobook by splitting it into 'a gazillion' 20-minute chunks.\n\nSet an absurdly low bar: not 'write the report' but 'open the doc and type the title'. Once you cross the first barrier, momentum usually carries you.",
  [edge("zaczynanie","symptom","C","średni","Po pierwszym 20-min kawałku reszta wydaje się łatwa.","After the first 20-min chunk the rest feels easy.")],
  [res("Magdalena Daniłoś: tnij na „miliard” 20-minutowych kawałków","Magdalena Daniłoś: split into a 'gazillion' 20-minute chunks",3660,
       "10-godzinny audiobook → wiele 20-minutowych kawałków; po pierwszej „torturze” reszta jest łatwa.",
       "A 10-hour audiobook → many 20-minute chunks; after the first 'torture' the rest is easy.")]),
 ("wstrzyknij-frajde","mdi:party-popper",9,["adhd","autism","audhd"],
  "Wstrzyknij frajdę w nudne zadanie","Dołóż bodziec, którego brakuje: dobra kawa, energetyczna muzyka, świeca, 10 pompek co 15 min, praca w kawiarni.",
  "Inject fun into a boring task","Add the stimulation that's missing: good coffee, energising music, a candle, 10 push-ups every 15 min, working from a café.",
  "W dorosłości oduczamy się szukać frajdy — a mózg ADHD jej potrzebuje, żeby w ogóle ruszyć nudne zadanie. Zamiast zaciskać zęby, dołóż bodziec: dobra kawa przed otwarciem laptopa, energetyczna playlista, zapach świecy, 10 pompek co 15 minut, kawiarnia pełna szumu.\n\nTo nie fanaberia, tylko paliwo: nowość i drobna przyjemność obniżają opór wejścia w zadanie, którego mózg inaczej unika.",
  "In adulthood we unlearn seeking fun — but the ADHD brain needs it to start a boring task at all. Instead of gritting your teeth, add stimulation: good coffee before opening the laptop, an energising playlist, a scented candle, 10 push-ups every 15 minutes, a café full of buzz.\n\nIt's not a whim but fuel: novelty and a small pleasure lower the resistance to a task the brain otherwise avoids.",
  [edge("zaczynanie","symptom","C","niski","Nowość/przyjemność obniża próg wejścia w nudne zadanie.","Novelty/pleasure lowers the threshold to start a boring task.")],
  [res("Magdalena Daniłoś: dołóż bodziec do nudnego zadania","Magdalena Daniłoś: add stimulation to a boring task",3513,
       "Kawa, muzyka, świeca, 10 pompek co 15 min, kawiarnia — frajda jako paliwo, nie nagroda.",
       "Coffee, music, candle, 10 push-ups every 15 min, a café — fun as fuel, not reward.")]),
 ("trudne-potem-nagroda","mdi:trophy-outline",10,["adhd","audhd"],
  "Najpierw trudne, potem nagroda","Zbuduj system punktów/nagród i zasadę „zrób trudne, a potem czeka coś fajnego” — to adresuje odroczoną gratyfikację.",
  "Hard thing first, then a reward","Build a points/reward system and the rule 'do the hard thing, then something fun waits' — addressing delayed gratification.",
  "Presja działa krótkoterminowo, ale jako jedyny motor jest długofalowo groźna. Zamiast niej buduj systemy nagrody: „zrób trudne, potem czeka coś fajnego”. Trzymaj nagrody małe i najlepiej neutralne/zdrowe, żeby nie wzmacniać dobrego nawyku złym.\n\nTo bezpośrednio adresuje problem odroczonej gratyfikacji, z którym mózg ADHD ma trudność.",
  "Pressure works short-term but is dangerous long-term as the sole motor. Build reward systems instead: 'do the hard thing, then something fun waits'. Keep rewards small and ideally neutral/healthy, so you don't reinforce a good habit with a bad one.\n\nThis directly addresses the delayed-gratification problem the ADHD brain struggles with.",
  [edge("zaczynanie","symptom","C","niski","System nagród zamiast presji jako długofalowy motor.","A reward system instead of pressure as the long-term motor.")],
  [res("Magdalena Daniłoś: trudne najpierw, nagroda po","Magdalena Daniłoś: hard thing first, reward after",3564,
       "Punkty/nagrody + „najpierw trudne”; nagrody małe i zdrowe, by nie wzmacniać nawyku złym.",
       "Points/rewards + 'hard thing first'; keep rewards small and healthy so you don't reinforce a habit with a bad one.")]),
 ("boj-sie-i-rob","mdi:airplane",11,["adhd","autism","audhd"],
  "Bój się i rób (akceptacja lęku)","Nie walcz z lękiem (to go powiększa) i nie uciekaj — wsiądź razem z nim, oczekując go. Posadź lęk na fotelu obok.",
  "Feel the fear and do it (acceptance)","Don't fight the fear (that grows it) and don't flee — board with it, expecting it. Sit the fear in the seat beside you.",
  "Po latach lęku przed lataniem Magdalena nie wybrała ani „nie wsiadam”, ani „wsiadam i walczę” (co przez prawo akcji-reakcji tylko podbija lęk). Wybrała trzecią drogę: wsiąść RAZEM z lękiem, z góry zakładając „będzie strasznie, będę się bać — siadam z tym lękiem”. Dosłownie wyobraziła sobie lęk na fotelu obok. To akceptacja w rozumieniu ACT.\n\nTen sam ruch poprzedził utratę 36 kg: najpierw musiała nazwać sytuację (przestać mówić „jestem puszysta”, spojrzeć na fakt otyłości II stopnia), zanim w ogóle zaczęła szukać rozwiązań. „Trudne jest drogą” — omijanie trudności to omijanie dobra po jej drugiej stronie.",
  "After years of fearing flying, Magdalena chose neither 'I won't board' nor 'board and fight' (which, by action-reaction, only inflates the fear). She chose a third path: board WITH the fear, expecting it — 'this will be terrible, I'll be scared — I sit down with this fear'. She literally pictured the fear in the seat beside her. That's acceptance in ACT terms.\n\nThe same move preceded losing 36 kg: she first had to name the situation (stop saying 'I'm just plump', face the Stage-II obesity fact) before she could even look for solutions. 'Hard is the way' — avoiding difficulty means avoiding the good on its far side.",
  [edge("lek-unikanie","symptom","B","średni","Akceptacja (ACT): wsiądź z lękiem zamiast z nim walczyć — walka go powiększa.","Acceptance (ACT): board with the fear instead of fighting it — fighting grows it."),
   edge("emocje-czarnobiale","mechanism","C","niski",None,None)],
  [res("Magdalena Daniłoś: posadź lęk na fotelu obok (historia samolotu)","Magdalena Daniłoś: sit the fear in the seat beside you (the airplane story)",2197,
       "Trzecia droga: nie walcz i nie uciekaj — wsiądź RAZEM z lękiem, oczekując go (akceptacja ACT).",
       "A third path: don't fight, don't flee — board WITH the fear, expecting it (ACT acceptance).")]),
 ("zestaw-na-lek","mdi:bag-personal-outline",12,["adhd","autism","audhd"],
  "Zestaw na lęk w kieszeni","Przygotuj listę narzędzi z wyprzedzeniem. Samo posiadanie ich „w kieszeni” obniża napięcie, nawet jeśli ich nie użyjesz.",
  "A fear kit in your back pocket","Prepare a tool list in advance. Just having them 'in your back pocket' lowers tension — even if you don't use them.",
  "Cel zestawu to nie natychmiastowy spokój, tylko niedopuszczenie, by lęk eskalował do niezdrowego poziomu. Klientka, która nie wyobrażała sobie wejścia do samolotu, poleciała na Cypr w 3 miesiące, budując taki kit — i ledwie z niego skorzystała. Samo posiadanie narzędzi „w kieszeni” rozładowuje wewnętrzne napięcie.\n\nPrzykładowe narzędzia: technika 5-4-3-2-1 (5 rzeczy, które widzisz, 4 które słyszysz, 3 które czujesz…), nagły kwaśny smak (guma/cukierek — przekierowuje uwagę i redukuje lęk), termos ulubionej melisy, umówiony sygnał z bliską osobą (ściśnięcie dłoni = „boję się, potrzebuję wsparcia”), powiedzenie obsłudze/drugiej osobie.",
  "The kit's goal isn't instant calm but keeping fear from escalating to an unhealthy degree. A client who couldn't imagine boarding a plane flew to Cyprus in 3 months by building one — and barely used it. Just having the tools 'in your pocket' discharges the inner tension.\n\nExample tools: the 5-4-3-2-1 technique (5 things you see, 4 you hear, 3 you feel…), a sudden sour taste (gum/sweet — redirects attention and cuts anxiety), a thermos of favourite melissa tea, a pre-agreed signal with a close person (a hand squeeze = 'I'm scared, I need support'), telling the crew/another person.",
  [edge("lek-unikanie","symptom","C","średni","Samo posiadanie narzędzi obniża napięcie — nie musisz ich użyć.","Just having the tools lowers tension — you don't have to use them.")],
  [res("Magdalena Daniłoś: 5-4-3-2-1 i kwaśny smak na lęk","Magdalena Daniłoś: 5-4-3-2-1 and sour taste for anxiety",2726,
       "Uziemienie 5-4-3-2-1 + nagły kwaśny smak przekierowują uwagę i redukują objawy lęku.",
       "5-4-3-2-1 grounding + a sudden sour taste redirect attention and reduce anxiety symptoms."),
   res("Magdalena Daniłoś: umówiony sygnał z bliską osobą","Magdalena Daniłoś: a pre-agreed signal with a close person",2678,
       "Ściśnięcie dłoni partnera = „boję się, potrzebuję wsparcia”, gdy mówienie jest trudne.",
       "Squeezing a partner's hand = 'I'm scared, I need support', when speaking is hard.")]),
 ("mikro-odwaga","mdi:dumbbell",13,["adhd","autism","audhd"],
  "Trenuj odwagę na drobiazgach","Ćwicz mikro-dyskomfort tam, gdzie stawka jest zerowa: „prosiłem o trzy, nie cztery”, odeślij danie w restauracji.",
  "Train courage on small things","Practise micro-discomfort where the stakes are zero: 'I asked for three, not four', send a dish back at a restaurant.",
  "Odwagi nie buduje się od razu na zadaniu o trudności 9. Trenuj ją na rzeczach bez stawki: jeśli warzywniak dorzuci czwartego pomidora, gdy prosiłeś o trzy — po prostu powiedz „nie, prosiłem o trzy”. To samo z odesłaniem dania.\n\nKażdy taki mikro-akt to powtórzenie „czuję dyskomfort i działam”, które buduje mięsień odwagi na większe sytuacje.",
  "Courage isn't built straight on a difficulty-9 task. Train it on no-stakes things: if the greengrocer adds a fourth tomato when you asked for three — just say 'no, I asked for three'. Same with sending a dish back.\n\nEach micro-act is a rep of 'I feel discomfort and I act', building the courage muscle for bigger situations.",
  [edge("lek-unikanie","symptom","C","niski","Mikro-dyskomfort bez stawki buduje mięsień odwagi na większe sytuacje.","No-stakes micro-discomfort builds the courage muscle for bigger situations.")],
  [res("Magdalena Daniłoś: pomidory u warzywniaka jako trening odwagi","Magdalena Daniłoś: the greengrocer's tomatoes as courage training",3169,
       "„Prosiłem o trzy, nie cztery” — mikro-akt dyskomfortu jako trening na większe sytuacje.",
       "'I asked for three, not four' — a micro-act of discomfort as training for bigger situations.")]),
 ("myslenie-dialektyczne","mdi:scale-balance",14,["adhd","autism","audhd"],
  "Myślenie dialektyczne („i” zamiast „albo”)","Trzymaj dwie przeciwne prawdy naraz: „mam trudny poranek I mogę być produktywny”, „czuję się beznadziejnie I nie jestem beznadziejny”.",
  "Dialectical thinking ('and' not 'either/or')","Hold two opposite truths at once: 'I had a rough morning AND I can be productive', 'I feel awful AND I'm not an awful person'.",
  "Z DBT (terapii dialektyczno-behawioralnej) pochodzi umiejętność trzymania dwóch przeciwnych prawd jednocześnie — zamiana „albo/albo” na „i”. Mózg ADHD ciągnie do skrajności (fajne/niefajne, skuteczny/leniwy), które wzmacniają cierpienie.\n\nĆwiczenie: gdy łapiesz się na ocenie „jestem do niczego”, dopisz „…I zrobiłem dziś trzy rzeczy”. Oba zdania mogą być prawdziwe naraz.",
  "From DBT (dialectical behaviour therapy) comes the skill of holding two opposite truths at once — swapping 'either/or' for 'and'. The ADHD brain leans to extremes (fun/not-fun, effective/lazy) that amplify suffering.\n\nExercise: when you catch the judgment 'I'm useless', add '…AND I did three things today'. Both can be true at once.",
  [edge("emocje-czarnobiale","symptom","B","średni","DBT: trzymaj dwie przeciwne prawdy naraz zamiast skrajności zero-jedynkowych.","DBT: hold two opposite truths at once instead of zero-one extremes."),
   edge("rsd","mechanism","C","niski",None,None)],
  [res("Magdalena Daniłoś: „i” zamiast „albo” (DBT)","Magdalena Daniłoś: 'and' instead of 'either/or' (DBT)",2100,
       "„Mam trudny poranek I mogę być produktywny” — dialektyka rozbraja myślenie zero-jedynkowe.",
       "'I had a rough morning AND I can be productive' — dialectics defuses zero-one thinking.")]),
 ("ciekawosc-zamiast-oceny","mdi:camera-outline",15,["adhd","autism","audhd"],
  "Ciekawość zamiast oceny (kamera / góra lodowa)","Obserwuj swoje „dziwne” zachowanie jak kamera bez kontekstu — bez etykiety — i pytaj, czemu ono służy, zanim zaczniesz je zmieniać.",
  "Curiosity over judgment (camera / iceberg)","Observe your 'weird' behaviour like a context-free camera — no label — and ask what function it serves before trying to change it.",
  "Ćwiczenie z Gestalt: wyobraź sobie, że kamera filmuje twój dzień bez kontekstu — co obiektywnie by zobaczyła? Widzimy tylko czubek góry lodowej (zachowania), nie to, co pod spodem (myśli, emocje, funkcja). Inni doklejają interpretację („leniwy”, „niechlujny”), która bywa całkiem fałszywa.\n\nZamiast oceniać własne dziwactwo, podejdź z ciekawością: czemu to robię, jaką pełni rolę? Dopiero rozumiejąc funkcję, da się sensownie coś zmienić.",
  "A Gestalt exercise: imagine a camera filming your day with no context — what would it objectively see? We see only the tip of the iceberg (behaviours), not what's underneath (thoughts, emotions, function). Others layer on interpretation ('lazy', 'careless') that may be entirely false.\n\nInstead of judging your own quirk, get curious: why do I do this, what role does it serve? Only by understanding the function can you meaningfully change it.",
  [edge("emocje-czarnobiale","symptom","C","niski","Najpierw zrozum funkcję zachowania (ciekawość), zanim je ocenisz/zmienisz.","Understand the behaviour's function (curiosity) before judging/changing it.")],
  [res("Magdalena Daniłoś: ćwiczenie kamery / góry lodowej","Magdalena Daniłoś: the camera / iceberg exercise",1302,
       "Obserwuj zachowanie bez kontekstu i etykiety; widać tylko czubek góry lodowej, nie funkcję pod spodem.",
       "Observe behaviour without context or label; you see only the tip of the iceberg, not the function beneath.")]),
 ("zapisuj-zamiast-przerywac","mdi:note-edit-outline",16,["adhd","audhd"],
  "Zapisuj zamiast przerywać","Gdy ktoś mówi do końca, NOTUJ swoje pytania zamiast wpadać w słowo. Połowa pytań i tak okaże się zbędna, bo mówca sam na nie odpowie.",
  "Write it down instead of interrupting","While someone speaks to the end, WRITE DOWN your questions instead of cutting in. Half will turn out moot — the speaker answers them anyway.",
  "Za przerywaniem stoją dwie rzeczy: ekscytacja, żeby dorzucić swoje trzy grosze, oraz (ważniejsze) słabsza pamięć robocza — strach, że zapomnisz myśl. Zasada z grupy Magdaleny (działa też 1:1): dopóki ktoś mówi, każdy zapisuje to, o co chce zapytać. Zabawny efekt — połowa pytań staje się nieistotna, bo mówca już na nie odpowiedział.\n\nMożesz wprost wyjąć telefon: „Sekundę, zanotuję to, żeby nie zapomnieć” — to rozładowuje napięcie po obu stronach.",
  "Interrupting has two roots: excitement to add your two cents, and (more important) weaker working memory — fear you'll forget the thought. A rule from Magdalena's group (works 1-on-1 too): while someone speaks, everyone writes down what they want to ask. The funny payoff — half the questions become moot because the speaker already answered them.\n\nYou can openly pull out your phone: 'One sec, I'm noting this so I don't forget' — it relieves tension on both sides.",
  [edge("pamiec-mysli","symptom","C","średni","Notuj pytania, gdy inni mówią; połowa okaże się zbędna.","Note questions while others speak; half turn out moot."),
   edge("slaba-pamiec-robocza","mechanism","C","niski",None,None)],
  [res("Magdalena Daniłoś: notuj zamiast wpadać w słowo","Magdalena Daniłoś: note it down instead of cutting in",4224,
       "Zapisuj pytania, gdy ktoś mówi do końca; wyjmij telefon i powiedz „notuję, żeby nie zapomnieć”.",
       "Write questions while someone finishes; pull out your phone and say 'noting this so I don't forget'.")]),
 ("gtd-2-min-inbox","mdi:inbox-arrow-down-outline",17,["adhd","audhd"],
  "Reguła 2 minut + jeden inbox","Jeśli zajmie ≤2 min — zrób od razu. Resztę wrzucaj do JEDNEGO miejsca (notatnik/kartka), inaczej myśl „zżera” pamięć roboczą na tydzień.",
  "The 2-minute rule + one inbox","If it takes ≤2 min — do it now. Everything else goes into ONE place (notebook/card), or the thought 'eats' your working memory for a week.",
  "Z metody GTD Davida Allena: jeśli coś zajmie do dwóch minut, zrób od razu — niezarejestrowana myśl inaczej „zżera” pamięć roboczą przez tydzień. Resztę wrzucaj do JEDNEGO inboxa (Magdalena trzyma wszystko w Google Keep, synchronizowanym telefon↔PC; Mateusz: kartka obok podczas głębokiej pracy, potem przepisana na jedną listę-matkę).\n\nPułapka: otwieraj appkę z notatkami WPROST — nie daj się po drodze porwać mailom i komunikatorom. System działa, dopóki wszystko w nim jest, zaglądasz do niego i utrzymujesz porządek.",
  "From David Allen's GTD: if something takes under two minutes, do it now — otherwise an unrecorded thought 'eats' working memory for a week. Everything else goes into ONE inbox (Magdalena keeps it all in Google Keep, synced phone↔PC; Mateusz: a paper card during deep work, later copied to one master list).\n\nThe trap: open the notes app DIRECTLY — don't get hijacked by email and messengers on the way. A system works as long as everything's in it, you look at it, and you keep it tidy.",
  [edge("pamiec-mysli","symptom","B","średni","GTD: ≤2 min → zrób teraz; resztę do jednego inboxa, by nie obciążać pamięci.","GTD: ≤2 min → do it now; the rest into one inbox so it doesn't load memory.")],
  [res("Magdalena Daniłoś / Mateusz Sobieraj: reguła 2 minut (GTD)","Magdalena Daniłoś / Mateusz Sobieraj: the 2-minute rule (GTD)",4434,
       "≤2 min → zrób od razu; nieskapturowana myśl zżera pamięć roboczą na tydzień.",
       "≤2 min → do it now; an uncaptured thought eats working memory for a week."),
   res("Magdalena Daniłoś: jeden inbox (Google Keep)","Magdalena Daniłoś: one inbox (Google Keep)",4500,
       "Wszystko w jednym miejscu; otwieraj appkę wprost, nie daj się porwać mailom po drodze.",
       "Everything in one place; open the app directly, don't get hijacked by email on the way.")]),
 ("audyt-energii","mdi:battery-heart-variant",18,["adhd","autism","audhd"],
  "Audyt energii: must-vs-want, parking, nowa gra","Pytaj, czy CIAŁO udźwignie to, na co zapisała się GŁOWA. Zostaw „parking” na to, czego świadomie nie zrobisz, i zaczynaj każdy dzień od zera.",
  "Energy audit: must-vs-want, parking lot, fresh day","Ask whether the BODY can carry what the HEAD signed up for. Keep a 'parking lot' for what you consciously won't do, and start each day from zero.",
  "Zarządzanie energią to fundament, nie dodatek. Kilka dźwigni z rozmowy:\n\n• „Parking” — lista zadań, które świadomie przyjmujesz, że nie wydarzą się w tym tygodniu; akceptacja tego, czego NIE zrobisz, redukuje poczucie winy i mielenie w głowie.\n• „Głowa myśli, że ciało może więcej, niż może” — pytaj, czy ciało realnie udźwignie to, na co właśnie się zapisałeś.\n• „Muszę, bo muszę” vs „muszę, bo chcę” — zadania-chcę dają energię na te trudne; wytnij je, a motywacja, żeby wstać jutro, się sypie. Balans jest konieczny.\n• „Jutro nowa gra” — nie przewalaj niezrobionych zadań w stertę poczucia winy; wyczyść tablicę i zaprojektuj kolejny dzień od zera.",
  "Energy management is the foundation, not an add-on. A few levers from the talk:\n\n• 'Parking lot' — a list of tasks you consciously accept won't happen this week; accepting what you WON'T do reduces guilt and mental churn.\n• 'Your head thinks the body can do more than it can' — ask whether the body will actually carry what you just signed up for.\n• 'Must because I must' vs 'must because I want' — want-tasks fuel energy for the hard ones; strip them away and the motivation to get up tomorrow collapses. Balance is essential.\n• 'Tomorrow is a new game' — don't roll undone tasks into a guilt pile; wipe the board and design the next day from zero.",
  [edge("energia-wypalenie","symptom","C","niski","Parking + must-vs-want + „jutro nowa gra” chronią energię i tną poczucie winy.","Parking lot + must-vs-want + 'fresh day' protect energy and cut guilt.")],
  [res("Magdalena Daniłoś: parking, must-vs-want, „jutro nowa gra”","Magdalena Daniłoś: parking lot, must-vs-want, 'fresh day'",4651,
       "Akceptuj, czego nie zrobisz; pytaj czy ciało udźwignie plan głowy; zaczynaj dzień od zera.",
       "Accept what you won't do; ask if the body can carry the head's plan; start the day from zero.")]),
 ("aktywny-odpoczynek","mdi:horse-variant",19,["adhd","autism","audhd"],
  "Aktywny odpoczynek (ruch angażujący głowę)","Bierny odpoczynek nie działa w ADHD. Odpoczynek to „robienie odwrotności tego, co męczy” — najlepiej ruch, który WYMAGA pełnej uwagi i wyłącza myślenie.",
  "Active rest (movement that engages the mind)","Passive rest doesn't work in ADHD. Rest is 'doing the opposite of what tires you' — ideally movement that DEMANDS full attention and switches thinking off.",
  "W ADHD bierne nicnierobienie nie regeneruje — głowa dalej miele problemy. Nudny trening zostawia umysł wolny do przeżuwania pracy; aktywność, która wymaga pełnej uwagi (np. jazda konna, gdzie nieuwaga grozi kontuzją), dopiero wyłącza myślenie.\n\nNawet zwykły trening można robić uważnie albo bezmyślnie. Cel: dobrać odpoczynek, który jest odwrotnością tego, co cię męczy — i naprawdę angażuje, zamiast zostawiać głowę na biegu jałowym.",
  "In ADHD, passive doing-nothing doesn't restore — the head keeps churning. Boring exercise leaves the mind free to chew on work; an activity that demands full attention (e.g. horse riding, where inattention risks injury) finally switches thinking off.\n\nEven a normal workout can be done mindfully or mindlessly. The aim: pick rest that's the opposite of what tires you — and genuinely engages, instead of leaving your head idling.",
  [edge("energia-wypalenie","symptom","C","niski","Odpoczynek = odwrotność tego, co męczy; ruch angażujący uwagę wyłącza myślenie.","Rest = the opposite of what tires you; attention-demanding movement switches thinking off.")],
  [res("Magdalena Daniłoś / Mateusz Sobieraj: aktywny odpoczynek","Magdalena Daniłoś / Mateusz Sobieraj: active rest",864,
       "Ruch wymagający pełnej uwagi (np. jazda konna) wyłącza myślenie; nudny trening zostawia głowę na biegu jałowym.",
       "Movement demanding full attention (e.g. horse riding) switches thinking off; boring exercise leaves the head idling.")]),
 ("powiedz-jak-dzialasz","mdi:account-voice",20,["adhd","autism","audhd"],
  "Powiedz, jak działa twój mózg","Mów wprost: „to zajmie mi 13× więcej energii niż Kasi — poszukajmy innego sposobu”. To strategia zarządzania energią, nie wymówka.",
  "Tell people how your brain works","Say it plainly: 'this'll take me 13× more energy than it would Kasia — let's find another way'. It's an energy strategy, not an excuse.",
  "Zakładamy „skoro ja tak mam, to inni też” — i większość trudności bierze się z NIEmówienia. Magdalena mówi wprost współpracownikom: „to zajmie mi 13× więcej energii i czasu niż Kasi czy Marcinowi — znajdźmy inne rozwiązanie”. Korzyści: nazwanie trudności uruchamia szukanie lepszego podejścia zamiast brnięcia na siłę; ludzie przestają oczekiwać tego, czego nie dasz; „czysta gra”.\n\nWażne: to NIE „nie umiem, bo mam ADHD” jako wymówka — nie musisz nawet wspominać o ADHD. Wystarczy „mój mózg tego nie ogarnia, potrzebuję tego prościej / na piśmie / narysowane”, w parze ze wskazaniem, co zrobisz znakomicie. Odwaga mówienia i o słabościach, i o mocnych stronach.",
  "We assume 'if I'm like this, others are too' — and most difficulty comes from NOT telling. Magdalena says it plainly to collaborators: 'this'll take me 13× more energy and time than Kasia or Marcin — let's find another solution'. Benefits: naming a difficulty triggers a search for a better approach instead of grinding through; people stop expecting what you won't give; a 'clean game'.\n\nImportant: this is NOT 'I can't, I have ADHD' as a blanket excuse — you needn't even mention ADHD. Just 'my brain doesn't handle this, I need it simpler / written / drawn', paired with pointing to what you'll do excellently. The courage to speak of both weaknesses and strengths.",
  [edge("energia-wypalenie","symptom","C","niski","Nazwanie trudności wprost uruchamia lepsze podejście — to oszczędza energię.","Naming the difficulty plainly triggers a better approach — it saves energy.")],
  [res("Magdalena Daniłoś: powiedz wprost, jak działa twój mózg","Magdalena Daniłoś: say plainly how your brain works",4915,
       "„To zajmie mi 13× więcej energii — poszukajmy innego sposobu”; nie wymówka, lecz strategia energii.",
       "'This'll take me 13× more energy — let's find another way'; not an excuse but an energy strategy.")]),
 ("terapia-pod-mozg","mdi:sofa-outline",21,["adhd","autism","audhd"],
  "Dobierz terapię do mózgu","„Terapia nie zadziałała” często znaczy „ta modalność nie pasowała”. Trzecia fala CBT (DBT, ACT) i Gestalt bywają trafniejsze dla mózgu ADHD niż np. psychodynamiczna.",
  "Match the therapy to the brain","'Therapy didn't work' often means 'that modality didn't fit'. Third-wave CBT (DBT, ACT) and Gestalt can fit the ADHD brain better than e.g. psychodynamic.",
  "Modalność terapii ma ogromne znaczenie dla mózgu neuroatypowego. Z doświadczenia Magdaleny: terapia psychodynamiczna była brutalnym dopasowaniem (brak wody/kawy, cisza, „przez godzinę powiedzieliśmy może trzy zdania”). Gestalt dał jej najwięcej — ponowne połączenie z ciałem (wiele osób z ADHD czuje, że „ciało to tylko statyw pod głowę”). CBT i jej trzecia fala (DBT, ACT) są mocno przebadane i skuteczne; ich wspólny rdzeń to nauka, że „jesteś czymś więcej niż twoje myśli” i jak „być w dyskomforcie”.\n\nWniosek: jeśli jedna terapia „nie działa”, to nie wyrok na terapię w ogóle — szukaj modalności pasującej do twojego mózgu. (Uwaga: dopasowanie psychodynamicznej jako „złej” to jej osobiste doświadczenie, nie reguła; skuteczność CBT/DBT/ACT w ADHD ma wsparcie badawcze.)",
  "Therapy modality matters enormously for a neurodivergent brain. From Magdalena's experience: psychodynamic therapy was a brutal fit (no water/coffee, silence, 'in an hour we said maybe three sentences'). Gestalt gave her the most — reconnecting with the body (many ADHD people feel 'the body is just a tripod for the head'). CBT and its third wave (DBT, ACT) are heavily researched and effective; their shared core is learning that 'you are more than your thoughts' and how 'to be in discomfort'.\n\nTakeaway: if one therapy 'doesn't work', it's not a verdict on therapy itself — look for a modality that fits your brain. (Note: rating psychodynamic as a 'bad' fit is her personal experience, not a rule; CBT/DBT/ACT efficacy in ADHD has research support.)",
  [edge("szukam-pomocy","symptom","B","średni","Trzecia fala CBT (DBT/ACT) i Gestalt bywają trafniejsze dla ADHD niż psychodynamiczna.","Third-wave CBT (DBT/ACT) and Gestalt can fit ADHD better than psychodynamic.")],
  [res("Magdalena Daniłoś: która terapia pasuje do mózgu ADHD","Magdalena Daniłoś: which therapy fits the ADHD brain",604,
       "Psychodynamiczna — trudne dopasowanie; Gestalt (ciało) i trzecia fala CBT (DBT/ACT) — realne przełomy.",
       "Psychodynamic — a hard fit; Gestalt (body) and third-wave CBT (DBT/ACT) — the real breakthroughs.")]),
]

for slug,icon,order,cond,tp,sp,te,se,bp,be,edges,reslist in M:
    for lang in ("pl","en"):
        en=(lang=="en")
        addrs=[]
        for e,npl,nen in edges:
            a=dict(e); n=nen if en else npl
            if n: a["note"]=n
            addrs.append(a)
        resources=[{"title":(r["title_en"] if en else r["title_pl"]),"url":r["url"],"type":"video","author":AUTHOR,
                    "note":(r["nen"] if en else r["npl"])} for r in reslist]
        write("protocols",lang,slug,{"title":(te if en else tp),"summary":(se if en else sp),
              "icon":icon,"order":order,"conditions":cond,"addresses":addrs,"resources":resources},
              be if en else bp)

print("symptoms:", [s[0] for s in SYM])
print("mechanisms:", [m[0] for m in MECH])
print("methods:", [m[0] for m in M])
