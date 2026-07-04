<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Markdown Dingus egy speciális tesztelőeszköz, amely segít
megérti, hogy a különböző Markdown processzorok hogyan kezelik
tartalmat. Három paneles felületet biztosít, ahol lehet
Szerkessze a Markdown elemet, tekintse meg a generált HTML-forrást, és tekintse meg a
egyidejűleg készült előnézet.

A Dingus alacsony szintű kezelhetőséget mutat Markeddel
előnézet, például az elkerített kódblokkok speciális kezelése.
__nem__ fut [Egyéni szabályok](Custom_Processor.html)
(Karmester). A legtöbb alapértelmezett beállítást használja, figyelmen kívül hagyva a beállításokat
mint a „GitHub újsorok” és „GitHub jelölőnégyzetek”, így a
az eredmény eltérhet attól, amit egy normál Megjelöltnél lát
előnézet.

## Az egyéni szabályok nem érvényesek

A Dingus egy __processzoros sandbox__: a Markdown megy
egyenesen a választott beépített processzorhoz (MultiMarkdown,
CommonMark (GFM), Discount vagy Kramdown). [Egyéni szabályok](Custom_Processor.html)
soha ne futtasson ott – nincsenek előfeldolgozási műveletek, szabályok keresése/csere,
shell-parancsok, Szöveg/fájl beszúrása vagy más Vezérlő lépések.

Normál előnézetben az egyéni szabályok módosíthatják a leértékelést
renderelés előtt állítson be stílusokat, szúrjon be CSS-t vagy JavaScriptet, és
több. A Dingusban szerkesztve ez nem történik meg.
Egyéni szabályok módosítása, miközben a Dingus nyitva van, nem
frissítse az előnézetét.

A Dingus __használhatja__ ugyanazokat az [előzetes CSS-stílusokat](Custom_Styles.html)
főablakként (a kimeneti panel stílusmenüjén keresztül).
Ez csak a látszat; ez nem ugyanaz, mint a Custom futtatása
Szabályok.

__Megnyitás a Dingusban__ előnézetből betölti a dokumentumot
aktuális Markdown puffer. Ha az egyéni szabályok már lefutottak, amikor
a fájlt a Marked alkalmazásban nyitották meg, akkor láthatja a hatásukat
a szöveget (például szabály által beszúrt szöveget), de a
A Dingus nem alkalmazza újra a szabályokat gépelés közben. Egyéni teszteléshez
Szabályok, használjon szabványos megjelölt előnézetet, vagy mentse el a Dingusból
és nyissa meg a fájlt a __Open in Marked__ paranccsal.

## Mi az a "Dingus"?

A „dingus” a webfejlesztésből kölcsönzött kifejezés
egy egyszerű tesztelőeszközre vagy sandbox környezetre utal. A
A Markdown Dingus segítségével kísérletezhet a Markdown szintaxissal és
azonnal látni, hogyan értelmezik a különböző processzorok.

## Hozzáférés a Dingushoz

A Markdown Dingus innen érhető el
[{% appmenu Help, Open Markdown Dingus %}][2]. Ez különösen
hasznos, ha:

* Új Markdown szintaxis elsajátítása
* Renderelési problémák hibaelhárítása
* Választás a különböző processzorok között
* Dokumentáció írása, amelynek több helyen kell működnie
  rendszerek

## Három paneles elrendezés

![][1]

A Dingus ablak három szinkronizált ablaktáblára oszlik:

### 1. Markdown bevitel (bal oldali ablaktábla)

* __Syntax Highlighting__: A Markdown a következővel van kiemelve
  színek a szerkezet egyértelművé tételéhez
* __Élő szerkesztés__: Gépeljen be, és azonnal látja a változásokat
  a többi ablaktáblában
* __Nagy betűtípus__: 21pt Menlo betűtípus a kényelmes szerkesztés érdekében

__Opciók legördülő menü__ (a bal oldali ablaktábla jobb felső sarkában): A
Az **Opciók** menüben a következőket válthatja:

* __Sorszámok megjelenítése__: Egy ereszcsatornát jelenít meg a bal oldalon
  bekezdésenként egy sorszám (a tördelt sorok egynek számítanak
  sor).
* __Láthatatlanok megjelenítése__: A szóközöket középpontként (·), a tabulátorokat pedig mint
  egy jobbra mutató nyíl (→), és az újsorok kocsivissza
  szimbólum (↵) világosszürkével, hogy észrevegye a kóbort
  szóköz.
* __Gremlins kiemelése__: Világos vörös hátteret helyez el
  nem ASCII karakterek (pl. göndör idézőjelek, hangulatjelek) és egy sötét
  piros háttér a problémás láthatatlan karaktereken (pl.
  nulla szélességű szóközök). Normál tabulátor és újsor karakterek
  nincs kiemelve.

A választások mentésre kerülnek, és a következő megnyitáskor visszaállnak
a Dingus.

__Keresősáv__: Nyomja meg a **⌘F** billentyűt a keresősáv megjelenítéséhez
"Markdown Input" címke. Kereshet és cserélhet a
szerkesztő, használja a **⌘G** gombot a Következő kereséshez és a **⇧⌘G** gombot a Kereséshez
Előző, és cserélje ki egy vagy az összes találatot. Nyomja meg a bezárást
gombot vagy a **⌘F** gombot ismét a keresősáv elrejtéséhez.

### 2. HTML-forrás (középső ablaktábla)

* __Létrehozott HTML__: Tekintse meg, hogy pontosan melyik HTML-t választotta ki
  processzor hozza létre
* __Szintaxis kiemelve__: A HTML színkóddal van ellátva az egyszerűség kedvéért
  olvasás

### 3. Renderelt előnézet (jobb oldali ablaktábla)

* __Élő előnézet__: Tekintse meg, hogy mikor fog kinézni a Markdown
  renderelt
* __Emoji támogatás__: GitHub-stílusú hangulatjelek, például `:zzz:`
  képekké konvertálva
* __Automatikus görgetés__: Automatikus görgetés, hogy megjelenítse a
  aktuális szerkesztési pozíció

## Szerkesztés a Dingusban

A Markdown Input panel intelligens szerkesztési funkciókat tartalmaz
gyorsabbá és természetesebbé teheti a Markdown írását.

### Intelligens újsor (Return Key)

A Return megnyomása alkalmazkodik az aktuális sorhoz:

* __Lists__: egy listasorban (`-`, `*`, `+` vagy `1.`),
  beszúr egy új listaelemet a megfelelő jelölővel. Számozott
  a listák a következő számmal folytatódnak.
* __Blockquotes__: A `>` karakterrel kezdődő sorban beszúr egy
  új idézőjelsor.
* __Kódkerítések__: Három vagy több backticket tartalmazó vonalon
  (pl. ` ``` `), üres sort szúr be a nyílás közé
  és a kerítések lezárása.
* __Egyéb sorok__: normál újsort szúr be.

### Karakterpárosítás

Amikor beír egy nyitó karaktert, a szerkesztő automatikusan
beszúrja a záró karaktert és a kurzort közé helyezi
őket. Támogatott párok: `"` `'` `(` `[` `` ` `` `<` .

* __Kijelöléssel__: A kiválasztott szöveget párba csomagolja.
* __Kiválasztás nélkül__: A pár beszúrása a kurzorral
  közöttük.
* __Type-over__: Ha a következő karakter már a
  Ha bezárja a határolót, ismét beírja a kurzort mögé
  duplikáció beszúrása helyett.
- __Szóköz üres párban__: Ha a kurzor egy üres pár között van (pl. `(|)`), a szóköz beírása a záró karaktert szóközzel helyettesíti.

### Gyorsbillentyűk

| Parancsikon | Akció |
|:------------------------|:------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------|
| **⌘F** | A keresősáv megjelenítése vagy elrejtése a Markdown beviteli ablaktáblában |
| **⌘G** | Következő keresése (ha a keresősáv látható) |
| **⇧⌘G** | Előző keresése (amikor a keresősáv látható) |
| **⌘B** | Félkövér: a kijelölés tördelése `**` karakterrel vagy `**\|**` beszúrása a kurzorral a |
| **⌘I** | Dőlt: a kijelölés tördelése `_` karakterrel vagy `_\|_` beszúrása a kurzorral a |
| **⇧⌘L** | Cikluslista jelölő (rendezetlen ↔ rendezett) |
| **Tab** | Sor vagy listaelem behúzása |
| **Shift+Tab** | Sor vagy listaelem kihúzása |
| **⌃⌘→** | Sor vagy listaelem behúzása (ugyanaz, mint a Tab) |
| **⌃⌘←** | Sor vagy listaelem kihúzása (ugyanaz, mint a Shift+Tab) |
| **⌃⌘↑** | Bekezdés mozgatása felfelé (bekezdés kivágása újsorral, beillesztés egy sorral feljebb) |
| **⌃⌘↓** | Bekezdés lefelé mozgatása (bekezdés kivágása újsorral együtt, beillesztés egy sorral lejjebb) |
| **⌘K** | Markdown hivatkozás beszúrása vagy tördelése: a kijelölés tördelése `[text]()`-ként és a kurzor elhelyezése az URL-ben, vagy a `[]()` karakter beszúrása a kurzorral a zárójelek közé, ha nincs kijelölés |
| **⌘U** | Kimeneti ablaktábla váltása (Forrás/Előnézet) |
| **⌥⌘↑** | Kijelölés bővítése: szó → belső/külső határolók → mondat → bekezdés → összefüggő blokk (például táblázat vagy kódblokk) → befoglaló lista/blokkidézet/kódblokk → dokumentum |
| **⌥⌘↓** | A szerződés kiválasztása ugyanazokon a szinteken keresztül, vissza az eredeti pozícióba |

Tab/Shift+Tab (és ⌃⌘←/⌃⌘→) tiszteletben tartja a lista szerkezetét és
idézőjelek: behúzzák/kihúzzák a listaelemeket, és hozzáadnak vagy
távolítsa el a `>`-t az idézőjelsorokból. Bekezdés mozgatása fel/le
kijelöli a teljes bekezdést a kurzor alatt (beleértve a
záró újsor), kivágja, és beilleszti a fölé vagy alá
szomszédos bekezdést, így a bekezdések nem olvadnak össze.

### Intelligens URL beillesztése

Beillesztéskor a vágólap az űrlap URL-jét tartalmazza
`protocol://...` szóközök nélkül:

* __Kijelöléssel__: a kijelölés a
  Lejelölő link: `[selected text](url)` .
* __Kijelölés nélkül__: az URL beillesztése a
  saját link: `<url>` .

Ez megkönnyíti a másolt URL-ek hivatkozásokká alakítását anélkül
kézi gépelés.

### Intelligens kiválasztás (⌥⌘↑ / ⌥⌘↓)

A Dingus szerkesztő támogatja a __szemantikus kijelölés kiterjesztését__:

* __⌥⌘↑__ a pontnál kezdődik, és kibővíti a választékot
  keresztül:
	- az aktuális szó
	- belső és külső határolt tartalom (idézőjel, zárójel,
   zárójelek és elkerített kódblokkok)
	- az aktuális mondat
	- az aktuális bekezdés
	- az összefüggő, nem üres sorblokk (például a
   egész táblázat vagy többsoros kódblokk üres sorok nélkül)
	- a mellékelt listaelemet, idézőjelet vagy kódblokkot
	- a teljes dokumentumot
* __⌥⌘↓__ visszasétál ugyanazokon a szinteken, amíg meg nem történik
  visszaáll az eredeti cart pozícióba.

Minden gombnyomás mindig szigorúan nagyobbra vagy kisebbre lép
kiválasztás, így soha nem fog "no-op" billentyűt lenyomni közben
bővül vagy összehúzódik.

## A Dingus használata szerkesztőként

A Dingus nem helyettesíti a teljes értékű szöveget
szerkesztő, de nagyon hasznos lehet __gyors szerkesztéseknél a
élő előnézet__, különösen akkor, ha pontosan szeretné látni, hogyan
a változások megjelennek. Az összes szövegszerkesztési viselkedés
A [Szerkesztés a Dingusban][3] részben leírtak itt érvényesek.

### Fájl megnyitása/új fájl létrehozása

* __Új fájl létrehozása a Dingusban__
	- Válassza a __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Amikor a rendszer kéri, válassza a __Dingus__ lehetőséget egy új, nem mentett új elindításához
   Dingus dokumentum.
	- Megnyílik az új Dingus dokumentumok a kiválasztott mintatartalommal;
   csak kezdje el gépelni, hogy lecserélje.
* __Meglévő fájl megnyitása a Dingusban__
	- Használja a __{% appmenu File, Open in Dingus... %}__ (⌥⌘O), vagy a következőt
   ha a Dingus ablak aktív, kattintson az állapot __Megnyitás…__ elemére
   bár. A parancs szükség esetén megnyitja a Dingus ablakot
   a Megnyitás panelt mutatja.
	- Válasszon ki egy támogatott egyszerű szöveges / Markdown fájlt; annak
   tartalma felváltja a jelenlegi Dingus puffert.
* __Megjelölt előnézeti dokumentum megnyitása a Dingusban__
	- Egy normál előnézeti ablakban használja a __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E) parancsot.
	- Az aktuális dokumentum Markdown-ja betöltődik a Dingusba
   így kísérletezhet anélkül, hogy megérintené az eredeti fájlt
   amíg nem választja a mentést. Az egyéni szabályok nem kerülnek alkalmazásra
   a Dingusok; lásd: [Az egyéni szabályok nem vonatkoznak](#custom-rules-do-not-apply).

### Fájl mentése

* __Változtatások mentése az aktuális fájlba__
	- A Dingus ablakban kattintson a __Mentés__ gombra az állapotsorban,
   vagy használja
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Ha a Dingus dokumentumot még nem mentette el, akkor fog
   helyet és fájlnevet kér; ezt követően ⌘S
   ugyanazt a fájlt frissíti.
* __Mentés másként / másolás új fájlba__
	- A __{% appmenu File, Save Dingus As... %}__ (⌥⌘S) használata.
	- Ez mindig megnyit egy __Mentés másként__ párbeszédablakot, és kiírja a
   az aktuális Dingus tartalmat egy új fájlba felülírás nélkül
   az eredeti.

### Előnézet a Megjelöltben

* __Nyissa meg a Dingus dokumentumot teljes megjelölt előnézetként__
	- Kattintson a __Megnyitás megjelölve__ lehetőségre a Dingus állapotsorában, vagy használja

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Ha a Dingus dokumentum nincs mentve, vagy nem mentett módosításokat tartalmaz,
   először menteni kell; majd a Marked megnyitja a
   a fájl szabványos előnézete.

Ezekkel a parancsokkal kezelheti a Dingust a
könnyű szerkesztő a gyors javításokhoz és kísérletekhez
ugorjon a teljes Megjelölt előnézethez vagy a szokásos szerkesztőhöz, amikor
készen áll a bővebb szerkesztésre.

## Processzor kiválasztása

A felül található legördülő menü segítségével válthat a különböző lehetőségek között
Markdown processzorok:

* __MultiMarkdown__: Teljes funkcionalitású processzor táblázatokkal,
  lábjegyzetek és matematikai támogatás
* __CommonMark (GFM)__: Szabványos, gyors processzor követi a
  CommonMark specifikáció
* __Kedvezmény__: GitHub ízesítésű leértékelés feladattal
  listák és táblázatok
* __Kramdown__: Fejlett processzor további funkciókkal
  mint az IAL-ok és a tipográfia

## Miért használja a Dingust?

### A processzorok közötti különbségek megértése

A különböző Markdown processzorok eltérően kezelik a szintaxist. A
A Dingus segít:

* __Kimenet összehasonlítása__: Pontosan megtekintheti, hogyan jelennek meg az egyes processzorok
  ugyanaz a Markdown
* __Debug Issues__: Határozza meg, hogy bizonyos szintaxis miért nem
  az elvárásoknak megfelelően működik
* __Szintaxistanulás__: Értse meg a finom különbségeket
  processzor implementációk között

### Teszt írás előtt

Mielőtt elkötelezné magát egy adott Markdown stílus mellett
dokumentumok:

* __Szintaxis érvényesítése__: Győződjön meg arról, hogy a Markdown megjelenik
  helyesen
* __Processzorok kiválasztása__: Döntse el, melyik processzor működik a legjobban
  a tartalmadért
* __Kísérletezzen biztonságosan__: Próbáljon ki új szintaxist anélkül, hogy befolyásolná
  az Ön tényleges dokumentumait

## Általános használati esetek

### Táblázat szintaxisbeli különbségek

Egyes processzorok eltérően kezelik a táblázat szintaxisát. A Dingus
lehetővé teszi, hogy megnézze, melyik processzor támogatja a legjobban a táblázatot
formázási igények.

### Lábjegyzet támogatás

Nem minden processzor támogatja a lábjegyzeteket. Használja a Dingust
ellenőrizze, hogy a lábjegyzet szintaxisa működik-e a választott processzorral.

### Matek és speciális karakterek

Tesztelje, hogy a különböző processzorok hogyan kezelik a matematikát
kifejezések és speciális tipográfiai karakterek.

## Tippek a hatékony használathoz

1. __Egyszerű indítás__: Kezdje az alapvető Markdown-szal, és fokozatosan
   bonyolultabbá teszi
2. __Test Edge Cases__: Próbáljon ki szokatlan szintaktikai kombinációkat
   megérteni a processzor korlátait
3. __Összehasonlítás__: Váltás a processzorok között
   tisztán látni a különbségeket
4. __Valódi tartalom használata__: Másolja át a tényleges tartalmat a saját
   dokumentumokat a valós forgatókönyvek teszteléséhez

A Dingus egy hatékony eszköz mindenkinek, aki akar
megértse a különböző Markdown implementációk árnyalatait
és biztosítsák, hogy tartalmuk helyesen jelenjen meg a különböző területeken
platformok és processzorok.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus