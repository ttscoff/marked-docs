<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Megjelölve többféle szintaxist tesz lehetővé az egyik fájl másikba való beillesztéséhez.

## Megjelölt szintaxis

Egyetlen előnézeti dokumentumba külső fájlokat is beilleszthet a sor elején található speciális szintaxis `<<[path/file]` használatával. A sorban üres soroknak kell lenniük felette és alatta, és az útvonalat a fő dokumentumhoz viszonyítottnak kell tekinteni, hacsak nem perjellel (`/`) vagy hullámvonallal (`~`) kezdődik. A perjel (gyökérkönyvtár) és a tilde (home könyvtár) használható a fájlok abszolút elérési útjainak meghatározására. Nincs szükség elérési útra, ha a külső fájlok ugyanabban a mappában vannak, mint a fő dokumentum, csak tegye a fájlnevet (a kis- és nagybetűket megkülönböztetve, a kiterjesztést is beleértve) a szögletes zárójelbe.

Használhatja az „Include Base” vagy „Transclude Base” metaadatfejlécet a mellékelt fájlok alaphelyének megváltoztatásához, például:

    Transclude Base: ~/Desktop

*Ne feledje, hogy a mellékelt fájlokat tartalmazó dokumentumok megtekintésekor az „I” (shift-i) beírásával megtekintheti, hogy melyik fájl van a látható területen. Ha megnyomja a visszatérést, miközben a mellékelt fájl elérési útja látható, a mellékelt fájl megnyílik az alapértelmezett szerkesztőben.*

Ezzel a funkcióval nagyméretű dokumentumokat/könyveket hozhat létre több fájlból (pl. minden fejezethez egy fájl), majd egyetlen indexfájlban adhatja meg a dokumentumok sorrendjét. Nem számít, hogy a fájlok hogyan vannak elnevezve, vagy hogyan vannak elrendezve a mappák; a Marked alkalmazásban megnyitott fájl indexnek minősül, és a benne felsorolt ​​fájlok szerepelnek benne. Példa indexfájlra három részből álló dokumentumhoz:

Mappa szerkezete:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Index.md:

	# Dokumentum címe

	## 1. szakasz

	<<[sections/section1.md]

	## 2. szakasz

	<<[sections/section2.md]

	## 3. szakasz

	<<[sections/section3.md]

Az Index.md megnyitása a Marked alkalmazásban megjeleníti annak tartalmát, mindhárom fájl kibontva. A rendszer az összes mellékelt fájlt figyeli a változások miatt. A Marked alkalmazásban lévő megnyitott dokumentumtól eltérően a mellékelt fájlkövetés a Spotlighttól függ a frissítések beszerzéséhez, és a lemezen egy Spotlight-indexelt mappában kell lennie.

Kódrészleteket és nyers html-t vagy szöveget is beilleszthet a [szintaxis változatai](Special_Syntax.html#includingcode) használatával.

Az elemeket tartalmazó dokumentum végső HTML-exportálásakor az importált szöveg elején és végén HTML-megjegyzések találhatók, amelyek a benne lévő fájl relatív elérési útját tartalmazzák.

**Megjegyzés:** minél több fájl van egy dokumentumban, annál lassabb lesz az előnézet teljes fordítási ideje. A Marked megpróbálja optimalizálni és gyorsítótárazni a folyamatot, de a dokumentum méretének növekedésével némi megjelenítési késéssel számol.

## MultiMarkdown Transclude Syntax

Használhatja a `{{filename}}` szintaxist is az újabb MultiMarkdown specifikáció alapján. A Marked felismeri a `Transclude Base: path` jelet az MMD metaadatokban, és ezt használja a fájlátvitel alapjaként.

A Transclude Base csak a szülődokumentumban kerül felismerésre, a további mellékelt dokumentumokban nem. Az összes beágyazott elemnek a kezdeti Transclude Base-n vagy a szülődokumentum helyén alapuló útvonalaknak kell lennie.

Az elkerített kód szintaxisa, amelyet a MultiMarkdown biztosít a fájlok feldolgozás nélküli felvételéhez, nem fog működni a Marked alkalmazásban. Ehhez használja a `<<(file)` (kódblokk) vagy a `<<{file}` (nyers) szintaxist.

## IA Writer Block szintaxis

A megjelölt 2.5.11+ támogatja az IA Writer [Content Block][ia] szintaxisát. Ez egy hivatkozás, amely egy perjellel (`/`) kezdődik a saját sorában. Ez lehet kódminta, kép, leértékelési fájl vagy CSV-fájl. Mindent megfelelően kezelünk a mellékelt fájl kiterjesztésének megfelelően, és a CSV-ket lehetőség szerint [Konvertáljuk Markdown][csv] táblákká.

Az IA-íróban a mellékelt fájlok az iCloud-tárolóba kerülnek, és nem mindig igényelnek „tényleges” elérési utat. Ha a Megjelölt fájlok már nem léteznek ugyanabban a mappában, mint a megtekintett fájl, akkor ezt a szintaxist abszolút vagy relatív elérési úttal kell használni. Az első perjelet figyelmen kívül hagyja, ezért ha ez egy abszolút elérési út, akkor két perjellel kezdje.

Egy kódrészlet ugyanabban a mappában, mint a megtekintett dokumentum:

    /részlet.h

Az "images" nevű alkönyvtár relatív elérési útja:

    /images/image.png "opcionális cím"

A Dokumentumok mappa abszolút elérési útja:

    //Users/username/Documents/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## A vázlatok, gondolattérképek és a CSV tartalmak konvertálása

Ha bizonyos fájltípusokat `<<[path]` vagy IA Writer blokkszintaxissal vesz fel, a Marked konvertálja azokat a nyers fájltartalom beszúrása helyett. A körvonalak és gondolattérképek viselkedése a fájlkiterjesztéstől és a [Beállítások: Alkalmazások → Gondolattérképek/Körvonalak][mindtérképek] beállításaitól függ. A CSV/TSV-fájlok mindig Markdown-táblázatokká konvertálódnak (lásd: [Táblázatok létrehozása CSV-fájlok segítségével][csv]).

| Formátum | Kiterjesztés | Amikor a „Beágyazás sellőként” **be van kapcsolva** | Amikor **ki** |
|--------|------------|----------------------------------------------------|
| **iThoughts X** | .itmz | Mermaid gondolattérkép diagram (tidy-tree) | Előnézeti kép a .itmz | fájlból
| **MindManager** | .mmap | Mermaid gondolattérkép diagram | Beágyazott leértékelési lista |
| **FreeMind** | .mm | Mermaid gondolattérkép diagram | Beágyazott leértékelési lista |
| **OPML** | .opml | Mermaid gondolattérkép diagram | Beágyazott leértékelési lista |
| **OmniOutliner** | .ooutline | Mermaid gondolattérkép diagram | Beágyazott leértékelési lista |
| **Kerékpár** | .bicikli | Mermaid mindmap (fájlnév gyökércsomópontként) | Beágyazott leértékelési lista (nincs dokumentum címe) |
| **CSV / TSV** | .csv, .tsv | Leértékelési táblázat ||
| **RTF / RTFD** | .rtf, .rtfd | Leértékelés RTF-konverzión keresztül (lásd [RTF- és RTFD-támogatás](RTF_Support.html)) ||
| **PDF** | .pdf | Lejelölés PDF-konverzión keresztül, amikor fő dokumentumként van megnyitva (lásd [PDF támogatás](PDF_Support.html)) ||

Minden körvonal-/elmetérkép-formátumnak saját jelölőnégyzete van a *Mind Maps/Outlines* alatt (elmetérképek, OPML-fájlok, kerékpáros körvonalak, OmniOutliner körvonalak). A formátum kikapcsolása csak az adott típusnál használja a „ki” viselkedést. A formátum részleteiért lásd: [Mindtérképek és körvonalak beágyazása](Embedding_Mind_Maps_and_Outlines.html), a beállítások módosításához pedig a [Beállítások: Alkalmazások][gondolattérképek]. A CSV-konverzió részleteiért lásd a [Táblázatok létrehozása CSV-fájlok használatával][csv] című részt.

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Könyvformátumok

A Marked támogatja a [Leanpub][lp], [GitBook][gb] és mmd\_merge (MultiMarkdown) formátumú indexfájlokat is. A könyvformátum-indexekben szereplő fájlokat a rendszer figyeli a változásokra, és az eredmény az összeállított dokumentum teljes előnézete, akárcsak a fenti „Index.md” példa.

### Leanpub

Ha engedélyezi a lehetőséget a {% prefspane Apps %}-ban a Leanpub/GitBook támogatás alatt, a „Book.txt” nevű fájlokat a rendszer automatikusan Leanpub indexfájlként kezeli. A régebbi "frontmatter:" formátumot is felismeri.

[Leanpub dokumentáció.][lpdocs]

Leanpub Book.txt példa:

    frontanyag:
    Acknowledgements.txt
    Előszó.txt
    Bevezetés.txt
    fő dolog:
    Markdown.txt
    Minta Books.txt
    Képek.txt beszúrása


### mmd_merge

Az mmd\_merge esetén a Marked megköveteli, hogy az első sor legyen "#merge" (egy speciális Marked trigger az mmd\_merge számára, megjegyzésként kezelik, és a többi processzor figyelmen kívül hagyja).

[mmd_merge dokumentáció.][mmdm]

mmd_merge példa:

    #egyesítés
    metaadat.txt
    Fejezet-1.md
        alfejezet-1-1.md
        alfejezet-1-2.md
    fejezet-2.md
        alfejezet-2-1.md
        alfejezet-2-2.md
    GYIK.md
    Köszönetnyilvánítás.md

### GitBook

A GitBook formázása Markdown listát használ a szerkezet és a tartalomjegyzék létrehozásához. Ha a GitBook támogatás engedélyezve van a Leanpub/GitBook támogatás {% prefspane Apps %} pontjában, a SUMMARY.md nevű fájl beolvasásra kerül, és automatikusan mmd_merge formátumba konvertálódik, lehetővé téve a GitBook dokumentum teljes előnézetét.

[GitBook dokumentáció.][gbdocs]

GitBook SUMMARY.md példa:

    # Összegzés

    * [I. rész] (1. rész/README.md)
        * [Szép írni] (part1/writing.md)
        * [A GitBook szép] (part1/gitbook.md)
    * [II. rész] (2. rész/README.md)
        * [Szeretjük a visszajelzéseket] (part2/feedback_please.md)
        * [Jobb eszközök szerzőknek] (part2/better_tools.md)

A GitBook lehetővé teszi a horgonyok használatát a SUMMARY.md tartalomjegyzékben, de a Marked figyelmen kívül hagyja ezeket, és csak egyszer tartalmazza az alapdokumentumot.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Többfájlos dokumentum-előnézeti funkciók

![Fájlhatárok] [2]

   [2]: images/includeboundaries.png @2x width=859px height=239px class=center

Ha olyan dokumentumot tekint meg, amely tartalmaz fájlokat, akkor két funkció segítségével megállapíthatja, hogy melyik fájlt nézi.

* **Billentyűzet:** A {% kbd shift I %} gomb megnyomásával rövid időre megjelenik egy felugró ablak, amely az előnézet görgetési helyén jelenleg látható fájl címét mutatja.
    * A {% kbd Return %} megnyomásával a {% kbd I %} után szerkesztheti a megjelenített fájlt a külső szerkesztővel.
* **Egér:** Ha a Fogaskerék menüben ({% kbd ctrl cmd B %}) választja a „Befoglalt fájlok határainak megjelenítése” lehetőséget, az előnézet bal oldalán egy színes sáv jelenik meg, amely szegmentálva mutatja a benne foglalt fájlok elejét és végét. Megjeleníti a beágyazott elemeket is. Ha a sáv egy része fölé viszi az egérmutatót, megjelenik az általa képviselt fájl neve, és rákattintva megnyílik a fájl a kiválasztott szerkesztőben.