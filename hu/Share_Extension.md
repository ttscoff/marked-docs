<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked tartalmaz egy macOS **Megosztás-bővítményt**, amely a rendszer Megosztás menüjében jelenik meg. Ezzel fájlokat vagy kijelölt szöveget küldhet a Markednek anélkül, hogy alkalmazást váltana vagy URL-eket másolna kézzel.

A Megosztás-bővítmény **a Marked 3-mal együtt érkezik**. Nem külön letölthető vagy telepíthető. A Direct, Mac App Store, Marked Pro és Setapp buildben is benne van.

## Működés [how-it-works]

Ha a Megosztás menüben a **Marked** lehetőséget választja, a Marked azonnal megnyílik. Nincs köztes szerkesztőablak.

### Fájl megosztása [share-a-file]

A **Finderből** (vagy más, fájlokat megosztó alkalmazásból) válassza a **Megosztás → Marked** menüpontot.

A Marked megkapja a fájl elérési útját, és ugyanazzal az `x-marked-3://open` URL-kezelővel nyitja meg, mint máshol. A fájl úgy nyílik meg a Markedben, mintha a Dock ikonra húzná, vagy az {% appmenu File, Open... ({{cmd}}O) %} menüvel választaná ki.

Támogatott bemenetek: fájl URL-ek, helyi fájlok és web URL-ek, ha a küldő alkalmazás biztosítja őket.

### Kijelölt szöveg megosztása [share-selected-text]

Jelöljön ki szöveget egy olyan alkalmazásban, mint a **TextEdit**, a **Safari** vagy a **Mail**, majd válassza a **Megosztás → Marked** menüpontot.

A Marked a vágólapra helyezi a szöveget, és **átmeneti előnézetet** nyit az `x-marked-3://paste` kezelővel. Ez ugyanaz a nem mentett előnézet, mint az {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Később mentheti az {% appmenu File, Save Transient Preview %} menüvel.

Támogatott a sima szöveg, HTML, RTF és Markdown, ha a forrásalkalmazás biztosítja.

A mögöttes parancsok részletei: [URL Handler](URL_Handler.html).

## A Megosztás menü használata [using-the-share-menu]

### Finderből [from-finder]

1. Kattintson jobb gombbal egy Markdown- vagy szövegfájlra (vagy jelölje ki, és kattintson a Finder eszköztár **Megosztás** gombjára).
2. Válassza a **Marked** lehetőséget a Megosztás menüből.

Ha a **Marked** nem látható, lásd [A Megosztás-bővítmény engedélyezése](#enable-the-share-extension) alább.

### Szövegkijelölésből [from-a-text-selection]

1. Jelölje ki az előnézni kívánt szöveget.
2. Nyissa meg az alkalmazás **Megosztás** menüjét (menüsor, eszköztár gomb vagy helyi menü).
3. Válassza a **Marked** lehetőséget.

A Marked elindul (vagy az előtérbe kerül) a megosztott tartalom előnézetével.

## A Megosztás-bővítmény engedélyezése [enable-the-share-extension]

A Markednek telepítve kell lennie az `/Applications` mappában (vagy a szokásos Alkalmazások mappában), és legalább egyszer el kell indítani, mielőtt a macOS felsorolná a Megosztás-bővítményt.

### Marked bekapcsolása a Rendszerbeállításokban [turn-on-marked-in-system-settings]

1. Nyissa meg a **Rendszerbeállítások** appot.
2. Lépjen a **Általános → Bejelentkezési elemek és bővítmények** menüpontra (egyes macOS verziókon: **Adatvédelem és biztonság → Bővítmények**).
3. Kattintson a **Bővítmények** elemre (vagy a **ⓘ** gombra a Bővítmények mellett).
4. Válassza a **Megosztás** (vagy **Sharing**) kategóriát.
5. Kapcsolja be a **Marked** elemet.

### Marked hozzáadása egy app Megosztás menüjéhez [add-marked-to-an-apps-share-menu]

Még ha a bővítmény rendszerszinten engedélyezve van, minden app külön választja ki, mely Megosztás célok jelenjenek meg:

1. Nyisson meg egy Megosztást támogató appot (a Finder és a TextEdit jó tesztlehetőség).
2. Nyissa meg a **Megosztás** menüt.
3. Válassza a **Bővítmények szerkesztése…** menüpontot (régebbi macOS-en: **Továbbiak…** vagy **Bővítmény-beállítások…**).
4. A **Megosztás** alatt jelölje be a **Marked** elemet.
5. Opcionálisan húzza feljebb a **Marked** elemet a listában a gyorsabb eléréshez.

A változások a legtöbb appban azonnal érvénybe lépnek.

## Ha a Marked nem jelenik meg a Megosztás menüben [if-marked-does-not-appear-in-share]

W> A Megosztás-bővítmény a Marked 3.1.9 verziótól érhető el. Győződjön meg róla, hogy legalább erre a verzióra frissített.

Próbálja ezeket a lépéseket sorrendben:

1. **Indítsa el a Markedet egyszer** telepítés vagy frissítés után. Frissítés után lépjen ki, majd nyissa meg újra a Markedet.
2. **Ellenőrizze, hogy a bővítmény engedélyezve van-e** a Rendszerbeállításokban, ahogy fentebb leírtuk.
3. **Szabja testre a Megosztás menüt** abban az appban, amelyből megoszt. A macOS elrejti a ritkán használt célokat, amíg be nem kapcsolja őket.
4. **Több Marked másolat:** ha egyszerre van Direct és Mac App Store build, csak a futó példány regisztrálja a bővítményt. Távolítsa el vagy nevezze át a másikat, majd indítsa a kívánt példányt.
5. **Indítsa újra a Macet**, ha frissítés után továbbra sem jelenik meg a bővítmény. A macOS gyorsítótárazza a Megosztás-bővítmény regisztrációt.
6. **Telepítse újra a Markedet** az `/Applications` mappába, ha Xcode-ból vagy lemezképből másolt buildet tesztel. A Megosztás-bővítménynek a `Marked.app/Contents/PlugIns/` mappában kell lennie.

## Tippek [tips]

- A Megosztás-bővítmény ideális gyors előnézetekhez webes részletekből, e-mail bekezdésekből vagy jegyzetekből fájl létrehozása nélkül.
- Teljes oldalakhoz vagy összetett böngészőkijelölésekhez a [böngészőbővítmények](Using_the_Browser_Extensions.html) több lehetőséget adnak (szakaszkiválasztás, Markdownify URL stb.).
- A megosztott fájlok normál Marked-dokumentumként nyílnak meg fájlfigyeléssel. A megosztott szöveg átmeneti előnézetként nyílik meg, amíg el nem menti.
