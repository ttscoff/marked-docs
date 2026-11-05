<!-- MT draft for hu — Reading Mode help. Review before publishing. -->
# <%= @title %>

Az olvasási mód megtartja a helyét a hosszú dokumentumokban, fókuszálja az aktuális blokkot, és lehetővé teszi a tartós kiemelések mentését.

## Belépés az olvasási módba [entering-reading-mode]

Válassza a {% appmenu Preview, Reading Mode %} lehetőséget, vagy nyomja meg a {% kbd ctrl opt r %} gombot. Ha a Speed ​​Read funkció fut, a Marked leállítja azt az olvasási módba lépés előtt.

Az aktuális bekezdés, címsor, listaelem, kép, kódblokk, táblázat vagy más olvasási egység bal jelölőt kap. A billentyűzet navigációja zökkenőmentesen mozog a blokkok között, és az aktuális egységet az előnézet felső harmadához közel tartja. A manuális görgetés újracélozza a fókuszt, anélkül, hogy az oldalt elkapná.

## Navigáció és önéletrajz [navigation-and-resume]

Ha az olvasási mód aktív:

- {% kbd j %} vagy {% kbd down %}: Ugrás a következő olvasási egységre.
- {% kbd k %} vagy {% kbd up %}: Ugrás az előző olvasási egységre.
- {% kbd h %}: A kijelölés kiemelése, vagy az aktuális egység kiemelésének váltása, ha nincs szöveg kijelölve.

A Marked elmenti az aktuális olvasási pozíciót minden egyes dokumentumhoz. Ha egy mentett pozíció eltér az aktuális nézettől, az olvasási módba való belépés két lehetőséget kínál:

- A **Folytatás** visszatér a mentett olvasási pozícióba.
- A **Indítás innen** az előnézetben jelenleg látható olvasási egységet használja.

## Fókuszmód [focus-mode]

Kattintson a Fókusz mód eszközre az előnézet tetején az összes blokk elsötétítéséhez, kivéve az aktuális olvasási egységet. A fókusz mód követi az aktuális egységet a navigáció során. Kattintson ismét az eszközre a többi blokk visszaállításához, vagy lépjen ki az Olvasási módból a Fókusz mód automatikus törléséhez.

## Kiemelések létrehozása és szerkesztése [creating-and-editing-highlights]

Jelölje ki a szöveget, és nyomja meg a {% kbd h %} gombot a soron belüli marker kiemeléséhez. Kiválasztás nélkül nyomja meg a {% kbd h %} gombot a teljes aktuális leolvasási egység kijelöléséhez, vagy nyomja meg újra az egység kiemelésének eltávolításához. Az első kiemelés egy aláírást kér, amelyet Marked használ a CriticMarkup létrehozásakor. Az aláírást a {% prefspane Preview %}-ben módosíthatja.

### Kiválasztás előugró ablak

Jelölje ki a szöveget a kiválasztási előugró ablak megjelenítéséhez a sor közepén lévő ikongombokkal:

- A **Highlighter** soron belüli kiemelést hoz létre (vagy **X** eltávolítja az utolsó automatikus kiemelést, ha az automatikus kiemelés be van kapcsolva).
- A **Megjegyzés** párbeszédpanelt nyit meg a kiemelés jegyzetének hozzáadásához vagy szerkesztéséhez. Ha a kijelölés még nincs kiemelve, a Marked először azt emeli ki.

A felugró ablak a kiválasztási szavak számát is mutatja, ha a **Szószám megjelenítése a kijelölésnél** engedélyezve van.

### Megjegyzések kiemelése [highlight-comments]

A megjegyzések elkülönülnek az aláírásoktól. Egy aláírás tulajdonítja a kiemelést; egy megjegyzés az Ön megjegyzése róla.

Megjegyzés hozzáadása vagy szerkesztése a kijelölő felugró megjegyzés ikonról, vagy a Ctrl billentyűt lenyomva tartva kattintson egy kiemelésre, és válassza a **Megjegyzés hozzáadása…** vagy a **Megjegyzés szerkesztése…** lehetőséget. Válassza a **Megjegyzés törlése** lehetőséget a jegyzet eltávolításához a kiemelés törlése nélkül.

A megjegyzésekkel ellátott kiemelések egy kis jelzőpontot mutatnak. Ha látható a Megjegyzések oldalsáv (**Előnézet > Megjegyzések megjelenítése**), az olvasási mód kiemelt megjegyzései ott jelennek meg a szülőkiemeléshez vezető összekötő vonallal, a CriticMarkup és más dokumentum-megjegyzések mellett.

### Automatikus kiemelések

Kattintson a kiemelő eszközre az előnézet tetején, hogy automatikusan kiemelje a szöveget a kijelöléskor. Kattintson a kiemelőre a kiválasztási előugró ablakban az utolsó automatikus kiemelés visszavonásához, vagy kattintson ismét a felső kiemelő eszközre az automatikus kiemelés kikapcsolásához.

Soron belül kiemeli a kezdő és záró fogantyúkat, amikor rámutat vagy kiválasztja őket. Húzza el a fogantyút a kiemelt tartomány kiterjesztéséhez vagy szűkítéséhez. A módosítások automatikusan mentésre kerülnek, és a dokumentum frissítésekor vagy újranyitásakor visszaállnak.

Kattintson egy kiemelésre a fókuszáláshoz, majd nyomja meg a Delete vagy a Backspace gombot az eltávolításhoz. A Ctrl billentyűt lenyomva tartva kattintson egy kiemelésre, és válassza a **Megosztás...** lehetőséget a macOS megosztási lap megnyitásához a dokumentum címével és a kiemelt szöveggel, a **Megjegyzés hozzáadása…** / **Megjegyzés szerkesztése…** jegyzet csatolásához, vagy a **Megjegyzés törlése** elemre a jegyzet törléséhez.

A **Kiemelések megjelenítése, ha az olvasási mód ki van kapcsolva** beállítás szabályozza, hogy a mentett kiemelések láthatóak maradjanak-e az üzemmód elhagyása után.

## Fénypontok exportálása [exporting-highlights]

Válassza az **Előnézet > Fénypontok exportálása…** lehetőséget, vagy kattintson a Kiemelt elemek exportálása eszközre az Olvasási mód eszköztárában. Formátumok: Markdown, HTML (jelenlegi előnézeti stílus), egyszerű szöveg, CSV (Readwise-kompatibilis, megjegyzésekkel a **Megjegyzés** oszlopban és aláírásokkal az **Aláírás** alatt) és JSON (minden kiemelésnél egy `comment` mezőt tartalmaz).

A HTML exportáló fészkek a megjegyzéseket idézőjelként emelik ki az egyes kiemelt szakaszok alatt.

A JSON formátum a Marked cserefájlja. Mentse el egy Markdown dokumentum mellé `Document.markedhighlights.json` néven, vagy adja hozzá automatikusan a TextBundle exportálásakor.

## Kiemelések importálása [importing-highlights]

Válassza az **Előnézet > Kiemelések importálása…** lehetőséget, és válasszon ki egy Marked kiemelések JSON-fájlt. A kiemelések azonosító szerint egyesülnek: új azonosítók kerülnek hozzáadásra, a megfelelő azonosítók frissülnek, és a fájlban nem szereplő meglévő kiemelések megmaradnak.

Amikor megnyit egy TextBundle kifejezést, amely tartalmazza a `highlights.json` karaktert, a Marked automatikusan egyesíti ezeket a kiemeléseket. Amíg a TextBundle nyitva van, a Marked a kiemelések és megjegyzések módosításait is visszamenti a `highlights.json`-re a csomagban (a `text.md` módosítása nélkül).

## TextBundle kiemeli [textbundle-highlights]

A **Save TextBundle** lehetőségnél engedélyezze a **Kiemelések belefoglalása** beállítást a `highlights.json` csomagba (vagy TextPack) beágyazásához. Oszd meg a csomagot, hogy az együttműködők a Marked kifejezéssel megnyithassák, és megtarthassák a kombinált kiemelési készletet.

## CriticMarkup műveleteket [criticmarkup-actions]

A kiemelések exportálásától és importálásától függetlenül az Előnézet menü két CriticMarkup műveletet biztosít a mentett kiemelésekhez:

- **Kiemelések másolása CriticMarkup**ként minden kiemelést CriticMarkup formátumban másol a forrásfájl megváltoztatása nélkül.
- **Kiemelések beszúrása a dokumentumba...** megerősítést kér, majd az egyértelműen illeszkedő forrásszöveget a CriticMarkup kifejezésbe csomagolja. Marked kihagyja a hiányzó, ismétlődő vagy átfedő egyezéseket, és jelentést készít az eredményről.

Aláírással és megjegyzéssel a generált jelölés a <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code> értéket használja. Csak megjegyzés esetén a Marked a <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>-t használja. Csak egy aláírással a <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>-t használja. Egyik nélkül a Marked csak a <code>{=<span>=</span>highlighted text==}</code> jelölőt hozza létre.

## Nyomtatás kiemeli [printing-highlights]

Alapértelmezés szerint az olvasási mód kiemelései megjelennek a nyomtatáskor vagy a PDF néven történő mentéskor. Használja a **Olvasási mód kiemeléseit** a nyomtatási lapon az aktuális kimenethez való módosításához. A {% prefspane Export %} megfelelő beállítása szabályozza a jövőbeli nyomtatási és PDF feladatok alapértelmezett értékét.
