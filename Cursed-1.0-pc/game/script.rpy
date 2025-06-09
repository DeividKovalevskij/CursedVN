init python:
    renpy.music.register_channel("bgs", "sfx", loop=True)
#To dla muzyki na Background, np szum rozmowy, dzwięk wiatra, drzewa itd.
define left = Position(xalign=0.2, yalign=1.0)
define right = Position(xalign=0.8, yalign=1.0)
#To dla pozycjy umieszczenia
#To jest rejestrowanie postaci, nadanie imieni i koloru.
define j = Character("Jack" , color="#008000")
define l = Character("Lucian", color="#ff0000")
define n = Character("Narrator", color="#808080")
define w = Character("???", color="#A020F0")
define a = Character("Annro", color="#000080")
define s = Character("Stróż", color="#A020F0")
define g = Character("Widmo", color="#FFFFFF")
define d = Character("Dzezebet", color="#FFFFFF")
define b = Character("Barman", color="#FFA500")
define t = Character("Jack i Lucian", color="#008000")

#Background scenes.
image bar1 = "bg/bar1.png"
image bar2 = "bg/bar2.png"
image bar3 = "bg/bar3.png"
image biuro1 = "bg/biuro1.png"
image biuro2 = "bg/biuro2.png"
image dom1 = "bg/dom1.png"
image dom2 = "bg/dom2.png"
image droga1 = "bg/droga1.png"
image droga2 = "bg/droga2.png"
image ulica1 = "bg/ulica1.png"
image black = "bg/Black.png"
image cmentarz1 = "bg/Cmentarz1.png"
image cmentarz2 = "bg/Cmentarz2.png"
image florida = "bg/Florida.png"
image florida2 = "bg/Florida2.png"
image nadgrobek = "bg/Nadgrobek.png"
image park = "bg/Park.png"
image pole = "bg/Pole.png"
image szpital = "bg/Szpital.png"

#Character scenes.
image Lucian1 = "Lucian/Lucian1.png"
image Lucian2 = "Lucian/Lucian2.png"
image Lucian3 = "Lucian/Lucian3.png"
image Lucian4 = "Lucian/Lucian4.png"
image Lucian5 = "Lucian/Lucian5.png"
image Lucian6 = "Lucian/Lucian6.png"
image Luciancsv = "Lucian/Luciancsv.png"
image LucianCombatMode = "Lucian/LucianCombatMode.png"
image LucianKonfliktBar = "Lucian/LucianKonfliktBar.png"
image Luciansad1 = "Lucian/LucianSad1.png"
image LucianMad = "Lucian/LucianMad.png"
image LucianShock = "Lucian/LucianShock.png"
image Lucianemote1 = "Lucian/Lucianemote1.png"
image Barman1 = "Barman/barman1.png"
image Barman2 = "Barman/barman2.png"
image Annro1 = "Annro/Annro1.png"
image Annro2 = "Annro/Annro2.png"
image Widmo1 = "Widmo/Dzez.png"
image Widmo2 = "Widmo/Dzez2.png"
image Struz = "Struz/Struz.png"
image Telefon = "Telefon/Telefon.png"

#Gra rozpoczyna się tutaj.
label start:

$ score = 0

#Rozdział 1: Biuro detektywa

scene biuro1
j "Nareszcie wieczór… W końcu wolne. Można odpocząć."
play music "music/Music-1.mp3" fadein (0.7)
n "Nagle z końca pokoju rozlega się dźwięk"
w "Jack, Jack… My tyle lat pracujemy razem… Ile to już? Dziesięć? Dwadzieścia? Jesteśmy prawie jak mąż i żona. Albo jak Sherlock i Watson."
n "Postać uśmiecha się, podchodzi do biurka Jacka"
show Lucian3
w " No i co? Jakie plany na wolne, co? Patrzy na Jacka z zaciekawieniem."
j "Odpocząć od ciebie, Lucianie. Ale próbuję tego od lat i bez rezultatu… Jak widzę, masz jakąś propozycję, mam rację?"
j "(w myślach) Jak ja go w ogóle wytrzymuję? Pracujemy razem od lat, a on nadal zachowuje się jak dziecko… Ech, mimo wszystko, to dobry towarzysz."
hide Lucian3
show Lucian5
l "Ha ha dobry żart. A co do propozycji ooo, spodoba ci się! Bo…"
n "Nagle Jack przerywa mu bez emocji."
j "Albo spodoba się tylko tobie. Jak zawsze."
hide Lucian5
show Luciansad1
j "(w myślach) Zawsze kiedy on ma jakąś  propozycję to nic dobrego i kończy się awanturą albo kłopotami, choć czasem na wesoło"
hide Luciansad1
show Lucian1
l "Nie gadaj głupstw! To nie moja wina, że tamtym razem…"
j "I nie przypominaj mi o tamtym razie"

hide Lucian1
show Lucian6
l "Tak, to ciekawe, co za propozycję mam mm...?"

menu:
    "Nie.":
        pass
    "No dobra, dawaj, mistrzu awantur. Co tym razem wymyśliłeś?":
        $ score += 2
    "Jak chcesz. Obojętne mi to.":
        $ score += 1

if score == 0:
    hide Lucian6
    n "Odpowiada sucho, bez emocji."
    show Luciansad1
    l "Naprawdę?"
    j "Daj spokój…"
    n "Jack bierze głęboki oddech, patrzy na Luciana, a potem mówi."
    j "I tak nie dasz mi spokoju, jeśli nie wysłucham, prawda?"
    n "Lucian uśmiecha się szeroko."
    l "Oczywiście, że nie!"
    j "Ech… Skoro nie mam wyboru, to mów."
    hide Luciansad1
    show Luciancsv
    l "Pamiętasz ten bar, gdzie czasami, khm… graliśmy w pokera?"
    j "I? Mów szybciej."
    l " Oj, oj, jaki dziś zły… Dobra, w skrócie: dostałem kupon na zniżkę i bilety VIP."
    j "I oczywiście nie chcesz tam iść sam."
    l "Noo… chciałem tylko zaproponować…"
    hide Luciancsv
    jump kolejna_scena

if score == 2:
    hide Lucian6
    show Lucian3
    l "Nic wielkiego, zwyczajna sprawa… Pamiętasz ten bar, gdzie czasami, khm… graliśmy w pokera?"
    j "Ha! Jak mógłbym zapomnieć? Zwłaszcza jak wkurzyłeś mafię, bo oszukiwałeś ich bez przerwy. Nawet kiedy ci mówiłem, żebyś przestał, dalej szulerowałeś, aż zrobiło się… wesoło. Choć niebezpiecznie."
    j "FBI długo jeszcze było na ciebie wściekłe."
    j "(w myślach): I komu to opowiesz, nikt nie uwierzy, że przypadkiem wywołaliśmy obławę FBI na mafię i jednocześnie wykonaliśmy ich robotę. Ech, dziwne jest to życie…"
    hide Lucian3
    show LucianShock
    l "No skąd miałem wiedzieć, że nasze zadanie było powiązane z interesami FBI? I że przez dziwne zbiegi okoliczności dwie mafijne rodziny po prostu… znikną? Najważniejsze, że my nie mieliśmy z tym nic wspólnego."
    n "Lucian robi krótką pauzę, uśmiecha się"
    hide LucianShock
    show Lucian1
    l "No, prawie nic."
    j "Więc… co z tym barem?"
    l "Mam kupon na zniżkę i bilety VIP."
    j "Nawet nie chcę wiedzieć, jak je zdobyłeś…"
    l "Aj, amigo, wszystko legalnie!"
    j "Znam twoje „legalnie”. Dla was, diabłów, „legalne metody” to zupełnie inna bajka…"
    hide Lucian1
    jump kolejna_scena

if score == 1:
    hide Lucian6
    show Lucian4
    l "Czemu taki bez humoru? Nieważne… Pamiętasz ten bar, gdzie czasami, khm… graliśmy w pokera?"
    j "Ha! Jak mógłbym zapomnieć? Zwłaszcza jak wkurzyłeś mafię, bo oszukiwałeś ich bez przerwy. Nawet kiedy ci mówiłem, żebyś przestał, dalej szulerowałeś, aż zrobiło się… wesoło. Choć niebezpiecznie."
    j "FBI długo jeszcze było na ciebie wściekłe."
    j "(w myślach): I komu to opowiesz, nikt nie uwierzy, że przypadkiem wywołaliśmy obławę FBI na mafię i jednocześnie wykonaliśmy ich robotę. Ech, dziwne jest to życie…"
    hide Lucian4
    show LucianShock
    l "No skąd miałem wiedzieć, że nasze zadanie było powiązane z interesami FBI? I że przez dziwne zbiegi okoliczności dwie mafijne rodziny po prostu… znikną? Najważniejsze, że my nie mieliśmy z tym nic wspólnego."
    n "Lucian robi krótką pauzę, uśmiecha się"
    hide LucianShock
    show Lucian1
    l "No, prawie nic."
    j "Więc… co z tym barem?"
    l "Mam kupon na zniżkę i bilety VIP."
    j "Nawet nie chcę wiedzieć, jak je zdobyłeś…"
    l "Aj, amigo, wszystko legalnie!"
    j "Znam twoje „legalnie”. Dla was, diabłów, „legalne metody” to zupełnie inna bajka…"
    hide Lucian1
    jump kolejna_scena

label kolejna_scena:

    show Lucian1
    l "No i co, partner? Jedziemy?"
    j "Dobrze, ale tym razem bez rozrabiania. I zachowuj się jak człowiek, a nie jak diabeł na wolności."
    j "(w myślach): Jak to się mogło stać, że moim partnerem jest diabeł, a ja muszę go tresować, żeby zachowywał się jak dorosły… Jak małe dziecko."
    hide Lucian1
    show Luciancsv
    l "(spoglądając na Jacka, mruczy pod nosem): – Sam jesteś dziecko… A ja jestem starszy od ciebie i doskonale wiem, jak się prowadzić."
    hide Luciancsv
    show Lucian1
    j "(zakładając płaszcz, odwraca się do Luciana): – Coś mówiłeś, Luci? – Pyta specjalnie, żeby go podrażnić."
    l "(udając niewiniątko): – Nie, nic."
    n "Po krótkiej chwili, gdy obaj są już ubrani i gotowi do wyjścia z biura, Lucian spogląda na Jacka i mówi:)"
    l "Hmm… Więc to już dzisiaj? Mija dokładnie 20 lat naszej współpracy, a zaczyna się 21. rok…"
    j "Rzeczywiście. Tyle razem przeżyliśmy, tyle spraw rozwiązaliśmy…"
    l "(szeroko się uśmiechając): – Świetna okazja, żeby to uczcić!"
    j "Aż się prosi, żebyś znowu narobił kłopotów… Żadnych awantur, chociaż dzisiaj, rozumiesz?"
    l "Dobra, dobra, szefie, jak sobie życzysz. Ale pamiętaj, żeby zgasić światło i zamknąć drzwi."
    j "(żartobliwie): – Co ja bym bez ciebie zrobił…"
    play sound "sounds/phone.mp3"
    n "(Jack sięga do włącznika, gasi światło i już prawie zamyka drzwi, gdy nagle zauważa, że na biurku dzwoni telefon.)"
    stop sound
    l "Lucian (zdziwionym tonem): – Ktoś tu nagle potrzebuje naszych usług? Jeśli odbierzesz, od razu powiedz, że po 21:00 naliczamy dodatkową opłatę."
    hide Lucian1
    play sound "sounds/phonepickup.mp3"
    show Telefon
    j "(spogląda na Luciana, wzdycha i mówi): – Tym razem nie mogę się z tobą nie zgodzić… Ale rozumiesz, muszę odebrać."
    n "(Lucian kiwa głową na znak zgody, a Jack podchodzi do telefonu i podnosi słuchawkę.)"
    j "Halo, detektywistyczne biuro „Cursed”, słucham."
    w "Jack Lancaster?"
    j "A kto pyta?"

label pytania:

    $ zadano_a = False
    $ zadano_b = False
    $ zadano_c = False

    label menu_pytan:

    menu:
        w "Człowiek, który ma dla pana propozycję… taką, której nie będzie pan mógł odrzucić."

        "Co za dzieło?" if not zadano_a:
            $ zadano_a = True
            j "I cóż to za zlecenie, że nie mam możliwości odmówić?"
            w "Och, to coś wyjątkowego. Powiem tylko tyle – po tej sprawie będzie pan mógł przejść na emeryturę… i dostać odpowiedzi na kilka dręczących pana pytań. Jeśli, oczywiście, pana to interesuje. Ale nie przez telefon…"
            jump menu_pytan

        "Zapytać o imię" if not zadano_b:
            $ zadano_b = True
            j "Pan już zna moje imię, ale ja nie znam pańskiego. Nie chce się pan przedstawić?"
            w "Moje prawdziwe imię nie jest istotne, ale… może pan nazywać mnie Annro."
            j "Miło poznać."
            a "Również miło, panie Lancaster."
            jump menu_pytan

        "Powiedzieć, że za połączenia po 21:00 naliczana jest dodatkowa opłata." if not zadano_c:
            $ zadano_c = True
            j "Bardzo mi miło, ale muszę pana poinformować, że rozmowy po 21:00 kosztują dodatkowo. A moje usługi nie należą do tanich."
            a "(śmiejąc się) – Ha ha, panie Jacku, dobry żart. Ciekawe, jak często słucha pan swojego partnera, Luciana?"
            j "Tylko kiedy ma rację."
            jump menu_pytan

        "Gdzie i kiedy?" if zadano_a and zadano_b and zadano_c:
            j "Dobrze, gdzie i kiedy możemy się spotkać?"
            a "Bar „Crossroads”, jutro o 13:13. Zna pan adres?"
            j "Tak, znam. Mógłby pan powtórzyć swoje imię?"
            a "Annro. Będę na pana czekać. Do widzenia i życzę miłego wieczoru. (Rozłącza się.)"
            n "(Jack odkłada słuchawkę. W biurze zapada chwila ciszy.)"
            jump kontynuacja_fabuły

label kontynuacja_fabuły:
    play sound "sounds/phonepickup.mp3"
    hide Telefon
    stop sound
    show Lucian5
    l "Myślisz, że on coś wie?"
    j "Możliwe. Tak czy inaczej, musimy to sprawdzić."
    l "A ciebie nie zdziwiło, jak zapytał o mnie?"
    j "Zdziwiło… Zwłaszcza że milczałeś przez całą rozmowę."
    l "Nie podoba mi się to. Mam złe przeczucia."
    j "Cokolwiek nas czeka, poradzimy sobie. Jak zawsze."
    l "A co z barem?"
    j "Innym razem. Nie mam siły nawet na bar."
    hide Lucian5
    show Lucian1
    l "Eh, no dobrze, innym razem to innym razem. Więc jutro o 13:00 w „Crossroads”?"
    j "Tak. Nie martw się. Jak skończymy tę sprawę, ja stawiam w barze."
    n "(Lucian spogląda na Jacka z chłodnym, przenikliwym wzrokiem.)"
    l "A ty… naprawdę tego potrzebujesz? Po co ci to?"
    j "(z niechęcią, unikając spojrzenia): – Nie zaczynaj… Wiesz, dlaczego. Nie mam innego wyboru."
    l "Więc… do jutra?"
    j "Do jutra."
    stop music fadeout (1.5)


#Rozdział 2: Bar „Crossroads”
    scene bar1
    hide Lucian1

    play sound "sounds/doors.mp3"
    n "Jack i Lucian wchodzą powoli do baru. Lucian idzie z tyłu, bez emocji, z niedowierzaniem rozgląda się dookoła. Jack spogląda przed siebie, chcąc coś powiedzieć – szybko jednak zauważa, że w lokalu nie ma ani żywej duszy."
    play music "music/Music-2.mp3" fadein (0.5)
    j "Coś tutaj cicho, a nie jednej duszy i w takim miejscu. Co o tym myślisz Lucian?"
    show Lucian1 at left
    with dissolve
    l "Zacznijmy od tego, że po pierwsze – jest dopiero 13:10. Ludzie zbierają się w takich barach wieczorami."
    l "Po drugie – nie podoba mi się to miejsce."
    l "A po trzecie… skoro widzisz, że nikogo tu nie ma, to znaczy, że możemy stąd wyjść. Albo..."
    j "Po pierwsze: nie wyjdziemy stąd, dopóki nie dostaniemy odpowiedzi."
    j "Po drugie: żadnych twoich awantur, jasne?"
    l "A skąd ta pewność? Może ktoś nas robi w konia."
    l "Może to pułapka. Może wszystko to nie ma choćby grama sensu."

    stop music fadeout (2.0)

    l "I powiedz mi, serio… aż tak bardzo ci na tym zależy?"

    menu:
        "Nie sprawdzimy, nie dowiemy się. I koniec. Masz coś jeszcze do dodania?":
            pass
        "Może masz rację, Lucian… ale musimy przynajmniej sprawdzić tę informację.":
            $ score += 2


if score == 0:
    l "(robi głęboki oddech, po czym uśmiecha się z lekką rezygnacją): – Ech… Czy ja ci kiedyś mówiłem, że czasami jesteś uparty jak baran? Nie? No to pozdrawiam – teraz już wiesz."
    j "Sam dobrze wiesz, na co się pisałeś."
    l "(sucho, spoglądając w stronę baru):– Wiem. Dobrze wiem."
    l "(kierując się powoli w bok w stronę baru) – A jak już dostaniesz wszystkie odpowiedzi… wiesz, gdzie mnie szukać."
    jump kolejna_scena_1

if score == 2:
    l "(prycha, robi krótką pauzę) Sprawdzimy i co dalej? Od razu pobiegniesz tam, gdzie cię wyśle?"
    l "Tylko proszę – nie daj się oszukać, dobra? A ja... poszukam, czy tu w ogóle można coś wypić."
    j "Spokojnie, nie trzeba się tak denerwować. Ale dzięki – to miłe z twojej strony."
    j "Zachowuj się tak częściej, to może w końcu przestaniesz być diabełkiem."
    l "(zamiast odpowiedzi tylko prycha z rozbawieniem)"
    jump kolejna_scena_1

label kolejna_scena_1:
    n "Podczas gdy Jack i Lucian omawiali, kto czym się zajmie, do ich stolika podszedł wysoki, masywny mężczyzna"
    n "Duży mężczyzna (głosem basowym, z wyraźnym sygnałem, że żarty nie są mile widziane)"
    hide Lucian1
    show Struz
    w "Boss czeka na detektywa. I tylko na niego."
    n "Lucian, mierząc wzrokiem olbrzyma, w milczeniu oceniał jego możliwości. Na wypadek, gdyby coś poszło nie tak."
    n "Po krótkiej chwili szepnął pod nosem, ledwo słyszalnie"
    hide Struz
    show LucianKonfliktBar
    l "Daj mi tylko siedem sekund… i poskładam cię tak, że zapomnisz, jak się mówi."
    n "Jack, zauważając minę Luciana i słysząc, co powiedział, szturchnął go mocno łokciem, szepcząc z irytacją"
    j "Uspokój się… albo sam ci „pomogę”."
    hide LucianKonfliktBar
    show Struz
    s "(marszcząc brwi, coraz bardziej zirytowany): – Długo jeszcze będziecie szeptać te głupoty?"
    j "(próbując rozładować napięcie, z wymuszonym uśmiechem): – Lucian, o, spójrz… chyba widzę twoją ulubioną whisky za ladą. (a do mężczyzny) – A co do pana, z miłą chęcią pójdę. Prowadź."
    n "Stróż bez słowa skinął głową i odwrócił się, dając znak Jackowi. Ten ruszył ostrożnie za nim. Przeszli przez ciemny, cichy korytarz i zatrzymali się przy małym stoliku w oddzielnym pomieszczeniu."
    scene bar2
    n "Przy stole siedział człowiek – na pozór zwyczajny, niemal nudny. Ale Jack czuł, że coś jest nie tak. W powietrzu unosiło się coś… nieuchwytnego."
    n "Jakby cień, który nie rzucał się na ścianę, ale wnikał do środka. Mistyczna aura, jakiej Jack nie czuł od bardzo dawna."
    hide Struz
    show Annro2
    a "(z chłodnym uśmiechem) – Panie Lancaster, miło pana widzieć. Jak nastrój?"
    n "Jack przyglądał się Annro uważnie. W jego oczach było coś… trudnego do rozczytania. Jack czuł, że musi uważać – za każdym słowem mogła kryć się pułapka."
    j "Dzień dobry. Nie najgorzej. Co pan chciał mi zaproponować? Co to za praca, która – jak pan twierdzi – jest związana z moją przyszłością?"
    n "(Po tych słowach Jack wbił spojrzenie w twarz rozmówcy, gotów wyłapać najmniejsze drgnięcie, grymas, cokolwiek.)"
    n "Annro skinął głową i gestem zaprosił Jacka do zajęcia miejsca naprzeciw siebie. Splecione dłonie ułożył na stole – wyglądał, jakby miał zaraz zacząć targi."
    a "Zanim przejdziemy do konkretów, chciałbym zapytać… Jak to jest – żyć i pracować z diabłem?"
    j "(siada powoli) – Hm… bywa trudno. Prowadzi jak dziecko – trzeba mieć na niego oko, żeby nie narobił szkód. Lubi działać impulsywnie. Ale mimo to… jest dobrym towarzyszem."
    j "Można powiedzieć, że jesteśmy jak Dante i Wergiliusz."
    n "Annro słuchał nie pokazując żadnych emocji, ale w oczach tliła się ciekawość."
    j "(nie tracąc kontaktu wzrokowego) – A ja mam pytanie…"
    a "(przerywając z lekkim uśmiechem) – Skąd wiem to wszystko i co mam z tego? Niestety… nie wszystko mogę powiedzieć. A jeśli chodzi o korzyści – żadnych. Po prostu chcę pomóc."
    j "(marszcząc brwi) – Po prostu pomoc? Nie przypominam sobie, żebym o nią prosił. Jak niby ma pan mi pomóc? I dlaczego chciał pan, żebym przyszedł bez Luciana?"

    a " (pochyla się lekko do przodu) – Ot, zwykła pomoc. Kiedyś uratował mi pan życie – teraz chciałbym spłacić dług. A co do prośby o pomoc… czasem nie trzeba jej wypowiadać na głos."
    a "Czasem nawet nie wiemy, że jej potrzebujemy. (krótkie zawahanie) – Co do waszego… diabełka – nie podoba mi się jego poczucie humoru. A znając jego wybuchowy charakter, mogłoby to zepsuć mój… obiad."

    menu:
        "Zgodzić się z Annro":
            pass
        "Bronić Luciana":
            $ score += 2


if score == 0:
    j "Trudno się z tym nie zgodzić. Czasem mam wrażenie, że on robi wszystko, żeby coś zepsuć... specjalnie."
    a "(rozbawiony, niemal z ulgą) – Spokojnie, jego tutaj nie ma, więc przynajmniej niczego nie narobi. To już coś."
    j "(z lekkim uśmiechem) – Krótkie chwile spokoju od niego… Ale wracając do celu naszej rozmowy."
    jump kolejna_scena_2

if score == 2:
    j "Nie trzeba tak surowo oceniać Luciana. Może nie jest idealny, ale naprawdę stara się być lepszą wersją siebie."
    a "(z lekkim uniesieniem brwi) – A pan sam w to wierzy? Że ktoś taki jak Lucian może się zmienić?"
    j "(stanowczo) – Tak. Wierzę, że każdy zasługuje na drugą szansę. I nie siedzę tutaj po to, żeby obgadywać swojego partnera."
    a "(po chwili milczenia skinął głową z uznaniem) – Rozumiem."
    jump kolejna_scena_2

label kolejna_scena_2:

    a "(sięga po cienką, ciemną teczkę i podaje ją Jackowi)"
    a "Tutaj jest wszystko, co powinien pan wiedzieć."
    n "Jack bierze teczkę, podnosi się z krzesła i przygotowuje do wyjścia. Wtedy Annro jeszcze raz się odzywa."
    a "Panie Lancaster… broń nie będzie potrzebna. Nic niebezpiecznego pana nie czeka."
    j "(z lekkim uniesieniem brwi)– Oby. Dziękuję, ale muszę już iść."
    a "(ze spokojem) - Powodzenia… i do widzenia."
    hide Annro2
    j "Do widzenia."
    n "Jack ruszył w stronę wyjścia z baru. Po drodze rozejrzał się za znajomą sylwetką. Gdy tylko zobaczył Luciana, zawołał go."
    j "Lucian! Chodź, muszę ci coś opowiedzieć…"
    n "Puki Jack i Lucian szli, Jack opowiedział wszystko co dowiedział się."


#Rozdział 3: Droga do Miasta „Good Hope”

    scene biuro2
    n "Jack i Lucian postanowili wrócić do biura, by tam przeanalizować dokumenty otrzymane od Annro. W trakcie jazdy Jack opowiedział wszystko, czego się dowiedział."
    play music "music/Music-3.mp3" fadein (0.9)
    j "No i tak to wygląda. Co o tym myślisz?"
    show Luciancsv
    l "(długo milczał, aż w końcu westchnął i odezwał się spokojnym, lecz poważnym tonem) To nie nasze pierwsze dziwne zlecenie."
    l "Gdybyśmy wcześniej nie mieli do czynienia z podobnymi sprawami... albo gdybym nie znał ciebie – twojej upartości i pragmatyzmu – to powiedziałbym: „Odmów i zapomnij”."
    hide Luciancsv
    show Luciansad1
    l "Ale jedna rzecz mnie szczególnie niepokoi... „Broń będzie niepotrzebna”? To brzmi bardzo… podejrzanie."
    n "W biurze zapadła cisza. Grobowa, ciężka jak kurz osiadły na starych aktach. Lucian jednak szybko ją przerwał."
    l "Im dalej w to idziemy, tym bardziej to wygląda jak wpadanie w króliczą norę. Kto wie, co tam na nas czeka?"
    j "(nie odrywając wzroku od dokumentów, rzuca z przymrużeniem oka) – Aha, a jeszcze ogry, smoki i szalony Kapelusznik..."
    l "(leniwo przewracając oczami)– Ha, ha, dobry żart. W takim razie nie zapomnij zabrać herbatki i ciasteczek. A co z papierami? Znalazłeś coś konkretnego?"
    j "(surowo, bez emocji)– Prawdopodobnie tak."
    l "(zainteresowany, pochyla się lekko)– I?"
    j "Na pewno pamiętasz miasto Good Hope... W dokumentach jest napisane, że tam znajdę odpowiedzi. I nie tylko."
    l "(przerywając gwałtownie)– „I nie tylko”? Co to ma znaczyć?"
    j "To może oznaczać, że... spotkam się z własną przeszłością. Z tym, gdzie i jak otrzymałem to przeklęstwo. Tam, gdzie moje życie rozpadło się na „przed” i „po”."
    l "(ciszej, jakby ostrożnie)– Nie chcę rozdrapywać starych ran, ale... to też może oznaczać, że wrócimy do przyczyn, dla których to miasto porzuciłeś."
    j "(ze smutkiem, ledwo słyszalnie)– Masz rację."
    l "(z wahaniem, co nie pasuje do jego zwykle pewnego siebie tonu)– Wiem, że zabrzmię jak paranoik – co zupełnie do mnie niepodobne – ale… może jeszcze nie jest za późno, by się wycofać?"
    j "(stanowczo)– Nie tym razem. Jeśli nie chcesz, nie musisz mi pomagać. Poradzę sobie sam."
    l "(z nutą szczerości, jakiej rzadko u niego słychać)– A jak mógłbym cię zostawić? Ktoś musi cię chronić… i pomagać. Mimo że jesteś detektywem, nie mogę pozwolić, żeby twoje życie tonęło w szarości."
    hide Luciansad1
    show Lucian4
    n "(chwila ciszy, potem uśmiecha się lekko)"

    stop music fadeout (1.5)
    l "Poza tym... to nasze ostatnie dzieło. Musimy dojść do końca razem. A potem… niech się dzieje, co chce."

    menu:
        "I co ja bym robił bez ciebie i twoich tekstów...":
            pass
        "Dzięki za dobre słowa. Razem nic nas nie powstrzyma. A jeśli chodzi o kolory... ty naprawdę potrafisz rozjaśnić nawet najciemniejsze.":
            $ score += 2


if score == 0:
    l " No nie wiem, może już by cię tu nie było."
    j "Może…"
    l "Wiem, jak bardzo ci na tym zależy, ale nie możesz tracić głowy, Jack."
    jump kolejna_scena_3

if score == 2:
    l "(z uśmiechem)– Zawsze do usług. Właśnie po to są partnerzy."
    j "Ja bym powiedział – przyjaciele."
    a "Tak, to brzmi jeszcze lepiej."
    jump kolejna_scena_3

label kolejna_scena_3:

    scene droga1
    j "No dobra… to jedziemy?"
    l "Oczewiście."
    hide Lucian4
    play music "music/Music-35.mp3" fadein (0.5)

#Rozdział 4: Miasto „Good Hope”

    scene black
    n "Jack i Lucian jechali przez kilka godzin w stronę miasta o nazwie „Good Hope”. Za kierownicą siedział Lucian, który – co było łatwo zauważyć – nie palił się do tego powrotu."
    n "Tymczasem Jack, siedząc obok, zagłębiał się w dokumentach, które otrzymał od Annro, analizując każdą stronę z coraz większym zdziwieniem."
    n "Z dokumentów wynikało, jakby ktoś spisał jego własną biografię – z detalami, których sam nie był pewien, że pamięta."
    n "Opis przeklętego wydarzenia, dziwne diagnozy lekarzy, zaskakujące informacje o Lucianie, jego pochodzeniu i związku z losem Jacka… A także konkretne instrukcje – dokąd iść, co zobaczyć, gdzie szukać odpowiedzi."
    n "Gdy dotarli do Good Hope, Jack podzielił się wszystkim z Lucianem. Ten tylko od czasu do czasu mruczał coś pod nosem, rzucając sarkastyczne uwagi, jakby próbował rozładować napięcie."

    #[Przyjazd do miasta – scena bezpośrednio po wyjściu z samochodu]
    stop music fadeout (1.5)
    scene droga2
    show Lucian4
    play music "music/Music-4.mp3" fadein (0.5)
    l "(robiąc głęboki wdech): – No to wróciliśmy… Do miejsca, z którego uciekaliśmy z nadzieją, że nigdy nie będziemy musieli tu wracać."
    l "Jak to się mówi… Dom, słodki dom. Tylko że w naszym przypadku to raczej Dom, przeklęty dom. (Uśmiecha się kąśliwie i patrzy na Jacka.)"
    j "(z gorzkim półuśmiechem): – I znowu jesteśmy tam, gdzie wszystko się zaczęło... Myślałem, że zostawiłem to za sobą. Ale masz rację – nic dobrego nas tu nie czeka."
    l "Ironia – miasto nazywa się Good Hope, a my tu jesteśmy z najgorszymi wspomnieniami."
    j "(suchy, lekko ironiczny uśmiech) – Heh, faktycznie… ta nazwa chyba była pomyłką."
    l "No to co, szefie? Od czego zaczynamy?"
    n "Jack przez chwilę milczał. Rozejrzał się wokół, jakby szukał śladów dawnego życia. Wzrok zatrzymał się na starym znaku, zardzewiałym płocie, znajomym kształcie drzewa. Jak duchy dzieciństwa, powracające z mgły wspomnień."
    l "(zniecierpliwiony, ale wciąż z uśmiechem): – Halo? Jack? Zasnąłeś czy może znowu odpłynąłeś w przeszłość? Pytam: od czego zaczynamy?"
    j "(tonem bez emocji) – Od domu. Tego, w którym kiedyś mieszkałem."
    hide Lucian4
    stop music fadeout (1.5)

#Rozdział 5: Stary dom Jacka

    scene ulica1
    n "Jack i Lucian szli cicho przez ulice Good Hope, kierując się do dawnego domu Jacka. Ulice, które kiedyś tętniły dziecięcym śmiechem i spokojem, teraz wydawały się puste i starsze niż powinny."
    n "Jack co krok łapał nostalgiczne obrazy z przeszłości – jak grał w klasy z sąsiadami, jak matka wołała go na kolację, jak słońce o zachodzie zalewało ulice złotem…"
    j "Tyle lat minęło… A czuję się, jakby to wszystko było sto lat temu."
    show Luciansad1
    l "(nie przepuszczając okazji do sarkazmu) - Aha, trawa była bardziej zielona, niebo niebieskie, a słońce świeciło jak z reklamy margaryny."
    j "(z uśmiechem)– Znowu próbujesz mnie drażnić?"
    l "Może tak, może nie… Po prostu… od dawna nie słyszałem, żebyś tak mówił. Jak…"
    j "(unosząc brwi)– Jak kto?"
    l "(uśmiechając się półgębkiem)– Jak stary dziad. Ale nie w zły sposób. Miło posłuchać kogoś, kto potrafi mówić o domu z sentymentem."
    j "I to mówi mi gość, który uważa, że wspomnienia to strata czasu… Ten dzień zapowiada się naprawdę dziwnie."
    l "Ty masz co wspominać."
    j "A ty?"
    l "(chłodno i bez emocji)– Nie."
    j "(po chwili milczenia)– Tak krótko?"
    l "Wiesz, skąd jestem. I wiesz, że tam nie było nic wartego wspomnienia."
    j "Okej… przepraszam."
    l "(z lekkim wzruszeniem ramion)– Nic się nie stało. A tak w ogóle… daleko jeszcze?"
    hide Luciansad1
    j "(rozglądając się)– Już prawie jesteśmy."
    show dom1
    n "W końcu stanęli przed dużym, starym domem. Cegły zbladły, okna zakurzone, ale budynek wciąż wyglądał solidnie. Jakby nie chciał się poddać upływowi czasu."
    j "To tutaj."
    show Lucian1
    l "(przyglądając się domowi z podziwem)– Wow… Ty tu naprawdę mieszkałeś?"
    j "Tak."
    l "Nieźle. Dom wygląda jak z horroru klasy B… ale ma klimat. Ktoś tu jeszcze mieszka?"
    j "Nie sądzę."
    l "A masz klucz?"
    j "(z lekkim zdziwieniem sam do siebie)– Nie wiem jak… ale tak, mam."
    l "(z uśmiechem)– No to na co czekamy?"
    j "Idziemy."
    hide Lucian1
    scene dom2
    play music "music/Music-5.mp3" fadein (0.5)
    n "Po przekroczeniu progu starego domu Jacka, światło jakby przygasło. Mimo że za oknami był słoneczny dzień, w środku czuć było chłód – nie zwykły przeciąg, ale zimno mistyczne, jakby cała przestrzeń nasyciła się echem czegoś dawno zapomnianego."
    n "Chłód, który owijał się wokół karku i skrzypiał pod butami, choć nikt się nie poruszał."
    n "Jack i Lucian wymienili spojrzenia. Oboje wiedzieli, co to oznaczało. Nie byli w tym domu sami."
    t "Ależ !@#%%*&"
    show LucianMad
    l "(w nerwowym szale, niemal z histerią)– „Broń nie będzie potrzebna”, mówili! „Nic wam nie grozi”, mówili! I my co? Posłuchaliśmy tego gościa z twarzą pokerzysty i duszą urzędnika!"
    j "(zaciskając zęby, wkurzony)– Jeżeli z tego wyjdziemy cali, to proponuję złożyć bardzo... intensywną wizytę u Annro."
    l "Nie mogę się nie zgodzić! Ty mu powiesz, co myślisz – w tym jesteś zawodowiec!"
    j "(przez zęby)– A my mamy jakiś wybór?! Ty lepiej opracuj plan B – ty jesteś od tego."
    hide LucianMad
    show LucianKonfliktBar
    l "(rozglądając się i szeptem) – I w ogóle... skąd się tu wzięło widmo? Nie może być, żebym czegoś nie wiedział o tobie. Jack, serio… nie masz jakiejś... klątwy bonusowej, o której zapomniałeś wspomnieć?"
    j "Skąd mam wiedzieć?! Ale jedno wiem – bądź gotów. Czuję, że to coś już jest blisko."
    n "Stanęli tyłem do siebie, instynktownie przyjmując pozycje obronne. Pomimo że broń miała być -niepotrzebna-, obaj czuli ciężar realnego zagrożenia."
    n "Chłód gęstniał, powietrze stawało się cięższe, a wśród ciszy dało się słyszeć coś… subtelnego, jakby odległe szeptanie – albo zgrzyt pazurów po drewnie."
    l "(półgłosem, jakby nie chcąc obudzić czegoś, co już się budzi)– Jeśli to będzie duch twojej przeszłości, to błagam, niech przynajmniej wygląda mniej jak potwór z koszmarów i bardziej jak smutna zjawa z melodramatu."
    j "(niewzruszony)– Tylko pamiętaj – najpierw my pytamy."
    hide LucianKonfliktBar
    show Widmo2 at right
    with dissolve
    show LucianCombatMode at left
    with dissolve
    n "Widmo pojawiłaś przednimi, wyglądała jak młoda kobieta patrzyła na Jacka i Luciana chłodnym i prawie bez emocji ale w oczach jej był smutek."
    n "Chłodnym głosem zaczęła mówić, jej głos nie był groźny choć i wywoływał nie pokój."
    g "(głos rozbrzmiewa jak echem po ścianach): – Komu zachciało się wejść nagle do tego domu? Kto odważył się zakłócić jego ciszę?"
    j "(ostrożnie, spokojnym tonem, by nie prowokować): – Nie szukamy kłopotów. Nazywam się Jack Lancaster, to mój partner Lucian. Ten dom... kiedyś należał do mnie. A ty kim jesteś i jak się tu znalazłaś?"
    g "Jack Lancaster… Znajome imię… Dawno niesłyszane… Ja? Jestem Dzezebet. Nie pamiętam, jak się tu znalazłam. Nie wiem, ile lat już tu jestem…"
    l "(szepcząc do Jacka):– Dobrze idzie. Może obejdzie się bez dramatów..."
    j "Dzezebet… Powiedziałaś, że znasz moje imię. Co to znaczy? (w myślach)– Skądś ją znam. To uczucie… jakby sen, którego nie mogę sobie przypomnieć…"
    d "(jej głos łagodnieje, pojawia się nuta smutku):– Ty… nie pamiętasz? (patrzy na Jacka z czymś w rodzaju zrozumienia)– Jasne…"
    j "Znamy się? Nie opuszcza mnie wrażenie, że już cię widziałem, gdzieś… kiedyś…"
    hide LucianCombatMode
    show Lucian5
    l "Jack… to chyba…(nie zdążył dokończyć, gdy Dzezebet mu przerwała)"
    hide Lucian5
    hide Widmo2
    show Widmo1
    d "Jesteś tu po odpowiedzi, tak?"
    j "Tak."
    d "Tutaj ich nie znajdziesz. Tu są tylko podpowiedzi…"
    j "Ech, a kiedy było inaczej…"
    d "Jeśli chcesz poznać prawdę… musisz przejść przez miejsca, które odcisnęły piętno na twoim życiu. Tam są odpowiedzi."
    j "Jakie to miejsca?"
    d "Park… i cmentarz…Na twoim miejscu nie zostawałabym tu długo."
    n "(Po tych słowach jej sylwetka rozmywa się jak mgła rozproszona porannym słońcem.)"
    hide Widmo1
    show Lucian1
    l "Hmm. Nie wiem kim była… ale znała cię dobrze. I chyba nie tylko z opowieści. Robi się coraz ciekawiej."
    j "Tak… Mam wrażenie, że ją znałem. Ale nie wiem jak. I czemu nie mogę sobie przypomnieć…"
    l "Tak czy siak – wiemy już, gdzie iść."
    j "(sucho, zamyślony)– Idziemy."
    hide Lucian1
    stop music fadeout (1.5)
    scene black
    n " Jack i Lucian opuścili dom w ciszy. Kierowali się w stronę parku – pierwszego z miejsc, które miały rzucić światło na mroczne zakamarki przeszłości Jacka."
    n "W powietrzu wisiała tajemnica, ale i coś więcej – jakby samo miasto oddychało wspomnieniami, które właśnie zaczęły się budzić."

#Rozdział 6: Park
    scene park
    play music "music/Music-6.mp3" fadein (0.5)
    n "Zbliżając się do miejscowego parku, Lucian próbował ułożyć sobie w głowie, jak dom, park i cmentarz są ze sobą powiązane."
    n "Jack również pogrążył się w myślach, próbując rozwikłać sens powrotu do tego miasta i wszystkiego, co się w nim działo."
    j "Co o tym wszystkim sądzisz? Co się tu właściwie dzieje?"
    show Lucian1
    l "Nie wiem. Trudno coś komentować. Cienie przeszłości snują się wszędzie…"

    l "To widmo – Dzezebet – nie była zwykłym duchem. Znała cię. Znalazła się w twoim domu. Ale ty jej nie pamiętasz. To... dziwne."

    menu:
        "Szczerze? Po prostu chcę znać prawdę. Dowiedzieć się i zamknąć ten rozdział.":
            pass
        "Może to miejsce… miasto… próbuje pomóc mi coś sobie przypomnieć. Coś ważnego?":
            $ score += 2


if score == 0:
    l "Rozumiem. Ale… może nie warto?"
    j "Już sam nie wiem, co jest warte, a co nie."
    l "W takim razie… chodźmy dalej. Może odpowiedź sama nas znajdzie."
    j "Tak. Idziemy."
    jump kolejna_scena_4

if score == 2:
    l "Nawet jeśli. Co potem? Co zrobisz z tym wspomnieniem?"
    j " Będę żył dalej… z tym, co odkryję."
    l "A może zapomniałeś o tym wszystkim nie bez powodu? Może były ku temu poważne przyczyny."
    j "Możliwe… bardzo możliwe."
    jump kolejna_scena_4

label kolejna_scena_4:

    l "A tak w ogóle… czego my tu szukamy? Kamienia? Drzewa? Cienia duszy?"
    j "Jakiegoś konkretnego miejsca. Czegoś, co przypomni mi przeszłość."
    l "A co dokładnie to ma być?"
    j "Nie wiem… ale wiem, że to jest tutaj. W parku."
    l "Park jest duży. Daj mi chociaż cień konkretu…"
    j "(przerywa mu stanowczo)– Cisza."
    l "(zaskoczony Jackiem)– Hmm?"
    j "(spoglądając na stare, porośnięte alejki)– To miejsce… tu właśnie spotkałem Dzezebet. Tutaj spędzaliśmy czas razem…"
    l "Czyli już sobie przypomniałeś, kim ona była?"
    j "Nie jestem pewien… ale chyba tak."
    l "I kim ona była?"
    j "(cicho, niepewnie)– Chyba… moją ukochaną."
    l "(cicho, jakby współczując)– Oh…"
    j "Tu się poznaliśmy."
    l "To trudne. Sam wiesz."
    j "Tak… Zrozumieć to wszystko w tym momencie… to niełatwe."
    l "Może na cmentarzu dowiemy się więcej. Wiem, że to wszystko cię szokuje."
    j "Ale musimy. Wiem jedno – nie można już zawrócić."
    stop music fadeout (1.5)
    hide Lucian1

#Rozdział 7: Cmentarz
    scene black
    play music "music/Music-7.mp3" fadein (0.5)
    n "Po opuszczeniu parku, Jack i Lucian ruszyli w stronę ostatniego kluczowego miejsca – cmentarza. Miejsca, gdzie mieli otrzymać odpowiedzi."
    n "Po drodze rozmawiali z miejscowymi, próbując zdobyć jakiekolwiek informacje. Ale to, co słyszeli, było chaotyczne – każdy mówił coś innego, każdy miał własną wersję historii."
    n "Część ludzi całkowicie unikała Jacka, omijała go szerokim łukiem, jakby był... cieniem. Z Lucianem rozmawiali częściej, ale i tak z niechęcią."
    n "W końcu dotarli na cmentarz. Tam znaleźli pomnik. Kamienny. Milczący. Ale krzyczący prawdą, której nie byli gotowi usłyszeć."
    scene cmentarz1
    show Lucian1
    l "Szkoda mi cię, kolego..."
    j "(głosem bez wyrazu)– Wszystko w porządku…"
    l "Nie musisz tłumić emocji. Możesz… możesz zareagować. Jak człowiek."
    j "Lucian… powiedz mi szczerze… ty sam rozumiesz, co się tutaj dzieje?"
    l "Nie. Nie rozumiem wszystkiego. Nie wiem, jak… jak to w ogóle możliwe."
    n "Jack nie odpowiedział. Milczał. Łzy spływały mu po policzkach cicho, bez dźwięku. Lucian kontynuował, nie widząc tego."
    l "Ci ludzie… unikali cię, jakby widzieli ducha. Mówili brednie. Opowiadali historie, których nikt nie potwierdzi. A przecież ty… ty tu stoisz. Jesteś żywy. Prawda?"
    scene nadgrobek
    n "Lucian wreszcie spojrzał w stronę pomnika. Zamarł. Powoli przeczytał wyryty napis"
    n "Dzezebet Lancaster   ur. 1990 – zm. 2015"
    n "Jack Lancaster       ur. 1988 – zm. 2015"
    n "Zginęli tragicznie w wypadku samochodowym. Spoczywają razem."
    l "(ciszej, jakby nie wierzył w to, co widzi) - Hej… to chyba jakiś żart. Ty przecież… stoisz tutaj. A nie leżysz tam…"
    j "Lucianie..."
    l "(milknie, kiwając lekko głową, że słucha)"
    j "To moja wina. Przez mnie… przez mnie Dzezebet nie żyje."
    l "Prawie cały rysunek już masz…"
    j "Jaki rysunek?! LUCIAN!"
    l "(wzdycha, spuszczając głowę)– Ja cię trochę oszukałem, Jack. Wiedziałem, co się stało. Wiedziałem, co zapomniałeś."
    l "Bo sam tego chciałeś. Prosiłeś mnie. Błagałeś, żebym ci pomógł zapomnieć. I zrobiłem to. Pomogłem ci. Ale… nie wszystko rozumiem do końca."
    scene cmentarz2
    j "(pełen gniewu i bólu)– Jak dawno mnie oszukiwałeś?! Jak długo to trwało?! I co sam ty nie rozumiesz?!"

    l "Na przykład… dlaczego ludzie tutaj widzą cię jak ducha. Dlaczego jesteś zapisany jako zmarły, a jednak żyjesz. W raportach… byłeś ranny, ale przeżyłeś. A tutaj, na kamieniu… śmierć. Zakończenie. Wpisane w kamień."

    menu:
        "Lucianie… zrób proszę jedną rzecz. Zniknij mi z oczu.":
            pass
        "Lucian… co ja mam teraz robić?":
            $ score += 2


if score == 0:
    l "No, ale... (nie zdążył dokończyć, Jack przerwał gwałtownie)"
    j "Zostaw mnie. Samego.(Głos Jacka był twardy, lecz drżał. Jakby walczył z samym sobą.)"
    l "Dobrze, okej… jakby co, znajdziesz mnie w barze."
    n "Lucian odwrócił się… ale nie odszedł. Nie miał serca zostawić Jacka. Został – w milczeniu, w cieniu, nie przeszkadzając."
    n "Jack usiadł przed pomnikiem. Łzy spadały na kamień, jakby chciały zmyć napisy."
    j "(półszeptem, do siebie)– Jak ja mogłem… Jak mogłem do tego dopuścić. Tyle lat żyłem jak we śnie...– Dzez… mam nadzieję, że nie masz mi tego za złe."
    j "cisza)– Może Lucian… zrobił to z dobrego serca. Może chciał ochronić mnie przed samym sobą.– Przepraszam. Za wszystko."
    n "Lucian usłyszał przeprosiny. Wiedział, że nie były do niego – i właśnie dlatego milczał. Nie chciał przerwać chwili, która musiała się wydarzyć."
    l "(cicho)– Ja nie trzymam złości na ciebie, Jack. Zrobiłem to, bo uważałem, że tak trzeba. Sam przecież mówiłem – niektórych rzeczy lepiej nie wiedzieć."
    j "Miałeś rację. Ale zrozum mnie... Po tamtym dniu zostawiłem tu wszystko. Żyłem, jakby nie w swoim ciele."
    hide Lucian1
    n "Jack jeszcze długo siedział przy grobie Dzezebet. Godziny mijały, a wspomnienia nawiedzały go jak sen. W końcu wstał."
    n "Z ciężkim sercem ruszył w stronę baru, gdzie czekał Lucian — czas porozmawiać o tym, co dalej."
    jump kolejna_scena_5

if score == 2:
    l "Otrzymałeś odpowiedzi, Jack. Choć nie wiem, czy naprawdę było warto…"
    j "Raczej nie."
    l "Możemy jeszcze tu zostać. Posiedzieć. Powspominać dobre dni z Dzezebet… Opowiedzieć to, co dobre. Co było prawdziwe."
    n "Jack nie odpowiedział, ale jego milczenie mówiło wszystko. Usiadł przy grobie, dłonią przesunął po wyrytym imieniu."
    n "Przez kilka godzin, bez słów, siedzieli tam razem. Jack zamknięty w przeszłości, Lucian — w teraźniejszości, czekający."
    j "Lucian…"
    l "Tak?"
    j "Idziemy do baru. Podsumujemy wszystko, co mamy. A potem… będziemy decydować, co dalej."
    l "Okej, bracie."
    hide Lucian1
    stop music fadeout (1.5)
    n "Jack i Lucian wstali razem. Z grobu nie da się zabrać odpowiedzi, ale można zabrać siłę. Ruszyli w stronę baru — gdzie czekała piwo i decyzje."
    jump kolejna_scena_5

label kolejna_scena_5:

#Rozdział 8: Miejscowy bar, pominki i plany na przyszłość
    n "Po cmentarzu Jack i Lucian weszli do jedynego czynnego baru w mieście. Lokal był pusty, cichy jak kościół po pogrzebie. Gdzieś w tle sączył się blues."
    n "Za ladą stał barman, przetarł szklanki z miną człowieka, który widział wszystko i jeszcze więcej. Gdy Jack i Lucian weszli, barman od razu ich zauważył."
    play music "music/Music-8.mp3" fadein (0.5)
    scene bar3
    show barman1 at right
    b "Co się stało, dżentelmeni? Wyglądacie, jakbyście wrócili z tamtego świata… i tam nic nie było. (Próbował rzucić żartem, ale uśmiech wyszedł krzywo.)"
    j "Coś w tym rodzaju..."
    hide barman1
    show Lucian1 at left
    l "Wyobraź sobie, że zapomniałeś, kim byłeś w swoich złotych czasach… a potem wracasz, tylko po to, by wspomnienia cię dopadły. Jak diabły z kotła."
    hide Lucian1
    show barman1
    b "(mruknął ze zrozumieniem)– Mieliście ciężki dzień. Może chcecie coś na rozluźnienie?"
    j "Piwo."
    l "Dla mnie też."
    n "Barman powoli nalał dwa kufle. Nie spieszył się — jakby wiedział, że czas dziś płynie inaczej."
    hide barman1
    show barman2 at left
    b "Proszę panowie. Zapraszam."
    t "Dzięki.(siadają przy barze, przez chwilę tylko cisza i blues z radia)"
    hide barman2
    show Lucian3
    l "I co? Co chciałeś podsumować?"
    j "(zamyślony, z ręką na kuflu)– Teraz już wiem. Wiem, dlaczego odszedłem, dlaczego chciałem zapomnieć."
    j "Dostałem wszystkie odpowiedzi... Odwiedziłem pomnik Dzezebet. Ludzie tu... opowiadają różne historie. Niektóre prawdziwe, większość to tylko szept i cień."
    l "No i co dalej?"
    j "Jest jeszcze jedno miejsce. To, gdzie dostałem to… przekleństwo. Trzeba tam wrócić. I zakończyć wszystko."
    l "Proponujesz tam pójść i… zamknąć ten rozdział?"
    j "Tak. I zostawić to wszystko za sobą."
    l "A potem?"
    j "(uśmiechnął się półgębkiem)– Pojadę na Florydę. Zacznę nowe życie. Kupię psa. Dzezebet zawsze marzyła o Florydzie. Mówiła, że tam zawsze świeci słońce."
    l "(kiwając głową z uznaniem)– Dobry plan."
    j "A ty? Co planujesz?"
    l "Może dokończę nasze dzieło… albo zmienię ścieżkę. Zacznę pomagać ludziom. Tak prawdziwie."
    j "Niezły plan."
    n "Zapanowała cisza. Nie taka niezręczna — raczej pełna ciężaru, pełna rzeczy, których nie da się już wypowiedzieć."
    n "Ich myśli dryfowały między wspomnieniami a niewiadomym, które dopiero nadchodziło. Piwo powoli znikało z kufli."
    n "Jack uniósł swój kieliszek – gest prosty, ale pełen znaczenia."
    j "Za Dzezebet."
    l "(z szacunkiem uniósł swój kufel)– Za Dzezebet."
    n "Wypili w milczeniu. Wieczór jeszcze młody i oni już wiedzieli, że coś się jeszcze będzie dział. Ostatni łyk, ostatni toast za miłość, za pamięć, za przebaczenie."
    j "Dopijamy i idziemy."
    l "Okej. Za nią… i za nas."
    stop music fadeout (1.5)
    hide Lucian3

#Rozdział 9: Tajemniczne drzwi
    scene black
    n ":Po opuszczeniu baru, Jack i Lucian ruszyli w stronę miejsca, gdzie wszystko się zaczęło. Tam, gdzie Jack jako dziecko otrzymał przeklęstwo — dar, który na zawsze zmienił jego życie."
    scene pole
    play music "music/Music-9.mp3" fadein (0.5)
    n "Szli długo, lecz ich kroki były pewne. Po kilkudziesięciu minutach dotarli. Przed nimi rozciągało się pole kwiatów — kojące, ciche, nierealne w swojej prostocie."
    n "A pośrodku tego pola… stały drzwi. Samotne. Bez ścian. Bez dachu. Bez ram."
    show Lucian1
    l "To chyba wyglądało inaczej, gdy pierwszy raz tu byłeś… prawda?"
    j "(patrzy na drzwi z dziwnym spokojem)– Tak. W dzieciństwie to miejsce miało inny kształt."
    l "Jak je zapamiętałeś?"
    j "Spacerowałem. Nie zauważyłem jamy. Wpadłem. Spędziłem tam całą noc."
    j "W środku był szkielet, ale nie zwykły… wyglądał jak nekromanta z jakiejś powieści fantasy. To było przerażające… a jednak wtedy poczułem coś, jakby… wezwanie."
    l "(ciszej)– Nie umiem sobie nawet wyobrazić… dziecko zamknięte w ciemności z takim widokiem."
    j "A teraz? Wszystko zniknęło. Nie ma jamy. Nie ma szkieletu. Zostały tylko te drzwi."
    l "Drzwi… pośrodku niczego. Bez ścian. Bez celu?"
    j "Ostatnie mistyczne zjawisko. Ostatnia próba. I koniec z tym wszystkim."
    l "(krok do przodu)– Zaczekaj."
    j "(odwraca głowę)– Co?"
    l "Nie wiemy, co jest za nimi."
    j "(z determinacją)– Już mnie to nie obchodzi. Cokolwiek tam jest – nie powstrzyma mnie."
    l "Ale... czego się tam spodziewasz?"
    j "(ciszej, niemal do siebie)– Może możliwości oddania tego przeklętego daru. Może zwykłego życia, w którym nie ma potworów, sztuki cienia i krzyczących duchów."
    j "A może niczego. Może to tylko symbol. Ale muszę przez nie przejść."

    stop music fadeout (1.5)
    l "Zanim to zrobisz… odpowiedz sobie szczerze: Czy naprawdę chcesz tam wejść, nawet jeśli nie będzie już powrotu?"
    hide Lucian1
    n "(cisza. wiatr porusza kwiatami. drzwi lekko skrzypią pod jego podmuchem"
#Rozdział 10: Koniec

if score >= 9:
    play music "music/Music-10.mp3" fadein (0.5)
    j "(w myślach): Co by tam nie czekało... najważniejsze to znaleźć sposób, by wrócić. Cofnąć się do tamtego dnia. Zmienić wszystko. Naprawić swoje błędy."
    n "Z tymi myślami Jack przekroczył drzwi."
    scene black
    "..."
    scene florida2
    n "Obudził się. Ten sam dzień. Ten, w którym stracił Dzezebet. Ale tym razem... coś było inaczej."
    n "Jack zdołał zmienić bieg wydarzeń. Nie pozwolił na wypadek. Ocalił ją. Po kilku latach on i Dzezebet wyjechali na Florydę, gdzie żyli długo i szczęśliwie — w miejscu, które zawsze było jej marzeniem."
    stop music fadeout (1.5)
    return

if score >= 6:
    play music "music/Music-9.mp3" fadein (0.5)
    n "Jack stał przed drzwiami i wciąż nie był pewien."
    n "A może... wcale nie musi przez nie przechodzić?"
    n "Może prawdziwym wyborem jest odpuścić. Nie szukać odpowiedzi. Nie próbować zmieniać przeszłości. Tylko zaakceptować."
    show Lucian1
    n "Po dłuższej chwili ciszy Jack odwrócił się i spojrzał na Luciana."
    j "Chodźmy. Czas zacząć od nowa."
    hide Lucian1
    scene black
    "..."
    scene florida
    n "Kilka miesięcy później Jack zamieszkał na Florydzie. Kupił mały domek, wziął psa ze schroniska i żył prosto. Bez mistyki. Bez duchów. Z wolną duszą — wreszcie."
    n "Lucian natomiast postanowił zakończyć karierę w detektywistyce nadprzyrodzonej. Został policjantem. Pomagał ludziom... tak jak Jack pomógł sobie."
    stop music fadeout (1.5)
    return

else:
    play music "music/Music-11.mp3" fadein (0.5)
    n "Jack wiedział jedno: chce poznać prawdę. Całą. Bez filtrów, bez złudzeń. Chce widzieć rzeczywistość taką, jaka jest."
    n "Gdy przekraczał drzwi, usłyszał za sobą słowa Luciana:"
    show Lucian1
    l "Czasami… tajemnice powinny pozostać tajemnicami. Dla dobra duszy."
    hide Lucian1
    n "Jack otworzył oczy."
    scene szpital
    n "Był w pokoju bez okien. Bielone ściany. Głosy zza drzwi. Zimne światło jarzeniówek."
    n "Szpital psychiatryczny."
    n "Wszystko, co przeżył — Dzezebet, śledztwa, przeklęte moce — było tylko wytworem jego umysłu."
    n "W rzeczywistości… już dawno nie był detektywem. Od lat przebywał w zamknięciu, próbując uciec od traumy, której nigdy nie zdołał pokonać."
    n "I być może... zostanie tam już do końca życia."
    stop music fadeout (1.5)
    return

return
