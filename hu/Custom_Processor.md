<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>


A Marked teljes irányítást biztosít az egyéni szabályokkal, szöveggel
átalakítja, és képes futtatni saját parancsait vagy futtatni
különböző processzorok a megfelelő fájltulajdonságok alapján.


## Egyéni előfeldolgozók/processzorok használata

Egyéni processzorok hozzáadásához lépjen a {% prefspane Processor %}
és kattintson az **Egyéni szabályok** lehetőségre.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


A Szabályszerkesztőben (más néven "Conductor") egyéni beállításokat adhat hozzá
szabályok, amelyeknek kritériumai vannak a fájlok fájlnév alapján történő egyeztetésére,
elérési utat, egyezéseket a tartalomban, metaadatokat és még azt is
más fájlok is léteznek ugyanabban a fában, mint a dokumentum
kinyitotta. Ha egy szabály egyezik, a műveletek meghatározott
szabály fut az adott fájlon.

> A Processzor mező alatt jelölje be az „Új
> a dokumentumok egyéni használatot használnak:" határozza meg, hogy a szabályok tesztelve vannak-e
> egyáltalán az Előfeldolgozó és Processzor fázisokra. általában
> hagyja bejelölve ezeket, de ha teljesen felül akarja írni
> bármilyen egyéni processzor, állítsa be itt.

![Szabályszerkesztő][2]

  [2]: images/CustomRules-800.jpg @2x width=800

Új szabály létrehozásához használja a `+`
gombot a bal oldali szabálylista alján. Adja meg a
szabály egy nevet, és állítsa be előfeldolgozóként vagy processzorként.

A szabály melletti három pont az előfeldolgozót, a processzort és az engedélyezettet jelzi. A Preprocessor vagy Processor közül csak az egyik jelölhető ki, és a pontokra kattintva módosíthatja a szabály állapotát.

Előfeldolgozó
: A fájl kezdeti feldolgozása után fut, amikor a Marked hozzáadja a benne foglalt fájlokat, kezeli a stílusbeállításokat, például a GitHub újsorait stb., de a feldolgozási fázis előtt. A dokumentum jelenleg még nyers Markdown, és módosíthatja a tartalmat, hogy átadja a processzornak. Ha egyetlen egyéni processzor sem egyezik, vagy nem fut a Futtatás a processzorban egy megfelelő egyéni processzoron, akkor az alapértelmezett processzor fut.

Processzor
: Egyedi processzor váltja fel az {% prefspane Processor %}-ben meghatározott beépített processzort. Minden olyan műveletet képes kezelni, amelyet az előfeldolgozó tud, és hozzáadja a Futtatási parancsot és a Processzor futtatása műveleteket. Ez lehetővé teszi egyéni parancs futtatását, pl. Pandoc, vagy futtasson egy másik beépített processzort a feltételeknek megfelelő fájlokon.

Az Egyéni szabályok szerkesztőjében lévő összes táblázat átrendezhető
húzással, így befolyásolhatja a sorrendet
szabályok futnak, a kritériumok sorrendje az állítmányban
szerkesztőt, és a sorban végrehajtandó műveletek sorrendjét.

### Predikátumszerkesztő

![Predikátumszerkesztő][predikátum]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

A szabály hozzáadása után használja a predikátumszerkesztőt a meghatározásához
kritériumok, amelyek meghatározzák, hogy a szabály fut-e a
adott fájl. A bal oldali legördülő menüből válassza ki a
feltételt, majd használja a komparátor és az érték mezőket az összeállításhoz
az állítmány.

- A _Fájlnév_ csak a fájl fájlnevének felel meg
- A _Extension_ csak a fájl kiterjesztésének felel meg
- A _Path_ megegyezik a fájl teljes POSIX (Unix) elérési útjával
- A _Tree_ megkeresi a fájlnév egyezéseit bárhol a fájlban
  a fájl könyvtárfája
- A _Szöveg_ megegyezik a fájl szöveges tartalmával. Használja előre
  perjel a szövegérték körül, hogy szabályos legyen
  kifejezés keresés.
- A _Fájl tartalmazza_ azt teszteli, hogy a fájl tartalmazza-e a benne foglaltakat
  fájlok (a [Marked's include
  szintaxisok](Multi-File_Documents.html)).
- A _Metadata type_ teszteli, hogy a fájl tartalmaz-e YAML-t,
  MultiMarkdown vagy Pandoc metaadatok
- _Metadata:_ mezők (például _Metaadatok: Szerző_,
  _Metaadatok: Dátum_, _Metaadatok: Cím_) teszt az adott
  metaadat kulcsok. Bármely metaadat-kulcs a legördülő listában, mint
  _Metadata:_, majd a mező neve.
- A _Manuálisan engedélyezett_ akkor egyezik, ha a szabályt megfordították
  be az aktuális előnézeti ablakhoz (lásd: [Kézi engedélyezés
  szabályok](#manuallyenabled) lent). Kombináld mással
  feltételek egy Mind (ÉS) csoportban, így a szabály csak akkor fut le, ha
  feliratkozik, és a fájl megfelel az egyéb feltételeknek.

Az összes fájl illeszkedéséhez (azaz egy egyéni processzorhoz, amely mindig
fut), állítsa a _Fájlnév_ értéket `contains` `*` értékre. A csillag lesz
helyettesítő karakterként működik, és minden fájlnak megfelel.

[Add a predikátum][addpredicate]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Új predikátum hozzáadásához kattintson a pluszjelre (+) az állítmánysorban. Tartsa lenyomva az Option gombot, miközben a + jelre kattint, hogy hozzáadjon egy logikai csoportot, amely beállítható Mind (ÉS) vagy Bármely (VAGY) értékre.

### Manuálisan engedélyezett szabályok [manuallyenabled]

Egyes szabályok nem futhatnak minden fájlon, amely megfelel a sajátjuknak
kritériumok. Ha akarja, adjon hozzá egy **Manuálisan engedélyezett** feltételt
egy szabály, amely csak azután fut, hogy bekapcsolta az áramot
előnézet.

Használja a **Kézi engedélyezése hozzáadása** gombot az állítmány alatt
szerkesztőt, hogy beillessze ezt a feltételt. Mindegyik szabály tartalmazhatja
csak egyszer. Ha jelen van, a szabály megjelenik az előnézet {% appmenu
Preview, Enable Custom Rule %} almenüjében
ablakot.

**Példa felhasználási eset:** Ön fenntart egy szabályt, amely beadja
nyomtat CSS-t, eltávolítja a megjegyzéseket, és eltolja a fejlécszinteket
PDF exportálás. Nem akarod ezt az átalakulást mindenkinél
mentse a rajzolás közben, de igény szerint szeretné. Adja meg a
szabály normál fájlegyezési feltételek plusz **Manuálisan engedélyezve**,
majd kapcsolja be az Előnézet menüből (vagy egy trigger parancsikonból)
ha készen áll a nyomtatási elrendezés ellenőrzésére.

#### Indító parancsikon

Ha egy kiválasztott szabályban szerepel a **Kézi engedélyezés** lehetőség, a
Az **Indítási parancsikon** mező jelenik meg a **Kézi hozzáadása mellett
Engedélyezve**. Kattintson a felvevőre, majd nyomja meg a gombot
kívánt kombinációt. Ez a parancsikon átkapcsolja a szabályt a
legelső Megjelölt előnézet (engedélyezés, ha ki, tiltás, ha be). A
parancsikont a szabállyal együtt tárolja, és az indítások során is megmarad.
Törölje a mezőt a parancsikon eltávolításához.

![Trigger parancsikon-rögzítő a karmesterben][kézi parancsikon]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Előnézetenkénti felülbírálások az Előnézet menüben

Két Előnézet menü almenü vezérlése felülírja az aktív
csak előnézet. A beállítások mentése [view](#multiview) szerint történik, amikor
több ablak ugyanazt a fájlt mutatja.

**Egyéni szabály engedélyezése**
: Felsorol minden engedélyezett szabályt, amely tartalmaz egy **Manuálisan
  engedélyezett** feltétel. Ellenőrizzen egy szabályt, amellyel bekapcsolhatja ezt
  előnézet; törölje a jelölést a kikapcsoláshoz. Az előnézet frissül
  azonnal.

**Egyéni szabály felülírása**
: Felsorolja a folyamatfázis-szabályokat. Válasszon egyet a *rögzítéshez*: közben
  a Folyamat fázisban csak az a szabály kerül kiértékelésre (egyéb
  A folyamatszabályok kimaradnak). Válassza a **Nincs (automatikus)** lehetőséget
  visszatér a normál szabályillesztéshez. Ez akkor hasznos, ha
  egy adott processzorfolyamatot szeretne rákényszeríteni az egyikre
  előnézetet a globális egyéni szabályok megváltoztatása nélkül.

#### Felülírás gomb az előnézeti eszköztáron

Ha egy előnézethez legalább egy manuálisan engedélyezett szabály tartozik, vagy a
rögzítve Folyamat felülbírálása, egy ág ikon jelenik meg alul
eszköztár (az exportálás és a fiókvezérlőktől balra).
A kitöltött, hangsúlyos színű ikon azt jelenti, hogy a felülírások aktívak;
a körvonal ikon azt jelenti, hogy a felülírások felfüggesztve vannak.

![Egyéni szabály felülírása gomb az előnézeti eszköztáron][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Kattintson a gombra a felülbírálások felfüggesztéséhez vagy újbóli engedélyezéséhez
előnézetet anélkül, hogy törölné a kézi szabály pipáját, vagy
rögzített Folyamatszabály. A felfüggesztett felülírások visszaállnak, amikor
ismét kattintasz. Ez gyorsabb, mint a szabályok bejelölésének törlése a
menüt, ha össze szeretné hasonlítani a normál előnézetet a sajátjával
csővezeték felülírása.

### Műveletek

A *+ Művelet* gombbal műveleteket adhat hozzá a szabályhoz.

![Művelet hozzáadása][kiegészítés]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

A rendelkezésre álló műveletek a következők:

Állítsa be a stílust
: Állítsa be az előnézet stílusát. Bármelyik hozzáadott beépített stílus vagy egyéni stílus elérhető.

Futtassa a Parancsot
: Ez egy parancssori parancsot vesz igénybe, beleértve az argumentumokat, és átadja a fájl tartalmát az STDIN-en. A parancsnak vissza kell adnia a kapott kimenetet az STDOUT-on.

> **Mac App Store Sandboxing**: A Marked Mac App Store (MAS) verziója olyan sandbox környezetben fut, amely korlátozza a külső binárisok végrehajtását. Ha olyan külső processzorokat kell használnia, mint a Pandoc a MAS verzióban, akkor a bináris fájlt át kell másolnia az alkalmazáscsomagba. Ehhez tegye a következőket:
>
> 1. Kattintson jobb gombbal a Marked.app → Csomag tartalmának megjelenítése elemre
> 2. Keresse meg a Tartalom/Források/
> 3. Hozzon létre egy `bin` mappát, ha nem létezik
> 4. Másolja a bináris fájlt (pl. `pandoc`) ebbe
> `bin` mappát
> 5. Tegye végrehajthatóvá: `chmod +x` a bináris
> 6. A Parancs futtatása műveletben hivatkozzon rá:
>
> `YOUR_BINARY_NAME [arguments]`
> Vagy használja a teljes elérési utat:
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **Megjegyzés**: A külső shebang-ot tartalmazó szkriptek (például a `/opt/homebrew/bin/python`-ra mutató Python-szkriptek) automatikusan végrehajtásra kerülnek a rendszer értelmezőin keresztül, amikor a csomagba másolják őket. A MAS-verziónak továbbra is gondjai lehetnek a bináris fájlok helyett valójában Python- vagy Ruby-szkriptek végrehajtásával.
> Minden alkalmazásfrissítés után újra át kell másolnia a bináris fájlokat, mivel a frissítések felváltják a teljes csomagot. Alternatív megoldásként használja a **Súgó->Crossgrade** lehetőséget a nem homokozós verzióhoz, amelyre nincsenek ilyen korlátozások.

Futtassa a beágyazott szkriptet
: Szerkesszen teljes szkriptet a beépített kódszerkesztőben. A Futtatási parancshoz hasonlóan ennek is STDIN-en kell bemenetet fogadnia, és STDOUT-on kell visszaadnia a kimenetet.

Metaadatok beállítása
: Metaadatok hozzáadása vagy beállítása. Adjon meg egy kulcsot és egy értéket. Ha a kulcs létezik, akkor az értéke frissül, ha nincs, akkor hozzáadódik. A felhasznált metaadatok típusát a fájl tartalma (vagy egy metaadat-konverziós művelet eredménye) automatikusan meghatározza.
: Ha nem található meglévő metaadat, akkor a metaadatok MultiMarkdown formátumban kerülnek hozzáadásra egy HTML megjegyzésbe. A Megjelölt képes elolvasni ezeket a metaadatokat, de nem jelennek meg az előnézetben, függetlenül attól, hogy milyen processzort használnak.

Metaadatok törlése
: Metaadatok törlése a kulcsa alapján.

Metaadatok csíkozása
: Az összes metaadat törlése. A YAML, MultiMarkdown és Pandoc metaadatokat érinti.

A YAML Meta konvertálása MMD-re
: A fájl tetején lévő YAML metaadatblokkot MultiMarkdown stílusú metaadatokká alakítja.

Az MMD Meta konvertálása YAML-re
: MultiMarkdown metaadatblokkot konvertál YAML-re.

Keresés és csere
: Végezzen keresést és cserélje le a fájl tartalmát.
: Ha a keresési karakterláncot perjelek veszik körül (pl. `/Project \w+/`), akkor a rendszer reguláris kifejezésként kezeli. A `$1`, `$2` stb. használatával egyezési csoportokat is beilleszthet a helyettesítő karakterláncba.
: A cseremező néhány escape szekvenciát támogat (a fordított perjel után): `\n` újsort szúr be, `\t` tabulátor karaktert, `\\` szó szerinti fordított perjelet, `\$` literális dollárjelet szúr be (egyezési csoport helyett)
: Minden más `\X` sorozat csak `X`ként lesz kezelve (a fordított perjel el lesz távolítva), így a `\e` `e` lesz. Az utána karakter nélküli \ jelet a rendszer szó szerinti fordított perjelként megőrzi.
: Használja a `[%key]` karakterláncot a dokumentum metaadataiból, környezeti változóiból vagy kontextusból származó érték beszúrásához (pl. `[%title]`, `[%MARKED_PATH]`). Elérhetők az ugyanazon szabály korábbi műveletei által vagy egy korábbi szabály által beállított kulcsok. A páratlan kulcsok helyére üres karakterlánc kerül.

H1 cím beszúrása
: H1-et szúr be a dokumentumba. Ez lekérhető a metaadatokból vagy a fájlnévből.

Shift fejlécek
: Állítsa be a fejlécszinteket -5--+5 között. Például, ha ezt -1-re állítja, akkor minden H1-ből H2, H2-ből H3 lesz stb. Állítsa be pozitív számra, hogy ezzel az összeggel megemelje a fejlécszinteket.

Fejlécek normalizálása
: Ez a művelet biztosítja, ha lehetséges, hogy csak egy H1 legyen a dokumentumban, és beállítja az összes fejlécszintet úgy, hogy azok szemantikai sorrendben legyenek, és ne ugorjanak ki szinteket, pl. H2-ről H4-re. Ha az eredeti dokumentum egyáltalán szemantikailag kezdetben rendezett, ez jól finomítja a hierarchiát.

TOC beszúrása
: Tartalomjegyzék beszúrása. A TOC mehet az első H1, az első H2 után vagy a fájl tetejére (a metaadat után kerül beillesztésre).

Fájl beszúrása
: Beszúr egy kiválasztott szövegfájlt a dokumentum egy adott pontjára. Ez lehet az első H1, az első H2, felül, lent vagy egy szövegegyezés után (reguláris kifejezés kereséséhez használja a `/pattern/`-t).

Szöveg beszúrása
: Előugró ablakszerkesztőt biztosít, amellyel közvetlenül beágyazhat szöveget a műveletbe. A pozicionálási beállítások ugyanazok, mint a _Fájl beszúrása_.
: A beszúrt szövegben bárhol használhatja a `[%key]` billentyűt, ha értékeket szeretne lekérni a dokumentum metaadataiból, környezeti változóiból vagy megjelölt kontextusból (pl. `[%author]`, `[%MARKED_PATH]`). Ez attól függetlenül működik, hogy melyik processzort használja, így nincs szüksége MultiMarkdownra a metaadatok helyettesítéséhez. Az ugyanabban a szabályban szereplő korábbi műveletekből származó értékek (például **Metaadatok beállítása**) vagy egy előző szabályból származó értékek szerepelnek. A páratlan kulcsok helyére üres karakterlánc kerül.

CSS fájl beszúrása
: A kiválasztott CSS-fájlt beszúrja a dokumentumba. Ez minden stíluskiválasztás után betöltődik, és a meglévő stílusok felülbírálására vagy újak hozzáadására használható.

CSS beszúrása
: Előugró CSS-szerkesztőt kínál, ahol közvetlenül hozzáadhatja saját CSS-jét a művelethez. Ezt a CSS-t a rendszer a dokumentum tetejére szúrja be, a meglévő stílusok után. A beszúrt stílusok sorrendje megegyezik a szabályban szereplő műveletek sorrendjével.

JavaScript fájl beszúrása
: Beszúr egy kiválasztott JavaScript fájlt a dokumentum végére. Vegye figyelembe, hogy egy *Insert JavaScript* műveletet kell használnia egy [frissítési horog](#updatehook) mellett, ha azt szeretné, hogy a szkript minden frissítéssel újratöltődjön.

JavaScript beillesztése az URL-ből
: Használja ezt egy `<script>` címke beszúrásához, amely egy CDN-hez vagy más távoli URL-hez kapcsolódik a dokumentum végére. Vegye figyelembe, hogy egy *Insert JavaScript* műveletet kell használnia egy [frissítési horog](#updatehook) mellett, ha azt szeretné, hogy a szkript minden frissítéssel újratöltődjön.

JavaScript beillesztése
: Előugró JavaScript-szerkesztőt biztosít, amellyel egyéni JavaScript-kódot közvetlenül beágyazhat a műveletbe. Ez a dokumentum végén lesz beszúrva, és a szabály által futtatott JavaScript sorrendjét a műveletek sorrendje határozza meg, az utolsó művelettel pedig utoljára.
: Ne feledje, hogy [update hook] (#updatehook) használatára van szükség, ha azt szeretné, hogy a szkriptek minden frissítéssel fussanak.

Önlinkelő URL-ek
: Konvertálja a csupasz URL-eket `<url>`-ra, ami hiperhivatkozást generál bármely processzorban.

Futtassa a parancsikont
: Futtasson egy Apple parancsikont. Bármely parancsikon futásnak át kell vennie az STDIN bemenetet, és a végén vissza kell adnia a kimenetet (Stop és Return Output). Ha olyan műveleteket szeretne végrehajtani, amelyek nem módosítják a szöveget, állítsa be a bevitelt egy változóra, futtassa a műveleteket, majd a végén adja ki az eredeti szövegváltozót.

Futtassa a Rendszerszolgáltatást
: Futtasson bármely rendszerszolgáltatást itt: `~/Library/Services`. A szolgáltatásnak fogadnia kell a bemeneti és a visszatérési kimenetet.

Futtassa az Automator munkafolyamatot
: Futtassa bármelyik Automator `.workflow` fájlt. A bemenetet a rendszer STDIN-en adja át, a kimenetet pedig az STDOUT-on.

Szabály futtatása
: Egy másik egyéni szabály műveleteinek futtatása az aktuális szabályból.
  Válassza ki a célszabályt a felugró ablakból. A hivatkozott szabály
  ugyanabban a fázisban fut (Preprocessor vagy Process) anélkül
  predikátumának újraértékelése, ami hasznossá teszi a számára
  újrafelhasználható "összetevő" szabályok.

  **Példa a használati esetre:** Határozzon meg egy kis szabályt, melynek neve „Strip
  HTML megjegyzések" egy Keresés és csere művelettel, és adja meg
  ez egy **Manuálisan engedélyezett** feltétel, így soha nem fut le
  automatikusan. A fő könyvfeldolgozási szabályhoz adja hozzá
  **Futtassa a szabály** műveleteket egymás után: először „A fejlécek normalizálása”,
  majd a "HTML megjegyzések kivágása", majd a Futtatás parancs, amely meghívja
  Pandoc. Minden lépést karbantarthat duplikáció nélkül
  szabályokon átívelő cselekvések.

  **Beágyazás:** A **Run Rule** által meghívott szabály nem hívható meg
  másik szabály. Ha a célszabály tartalmaz egy **Futtatási szabályt**
  művelet, a művelet kimarad; minden egyéb művelet a
  a célszabály továbbra is fut. Több **Futtatási szabályt** is hozzáadhat
  műveleteket egyetlen szabály szerint hajtják végre, és sorrendben hajtják végre.

  A szabály nem tudja meghívni magát, és a Marked érzékeli a ciklusokat
  (például az A szabály meghívja a B szabályt, amely meghívja az A szabályt)
  és kihagyja a beágyazott hívást. Lásd az [Egyéni szabályokat
  Napló](#customprocessorlog) az üzenetek kihagyásához.

Folytatás
: Alapértelmezés szerint a szabály egyeztetése után a feldolgozás leáll (külön az előfeldolgozókhoz és a processzorokhoz, így egy előfeldolgozó és egy processzor egyezhet). Ez a művelet kényszeríti a szabályegyeztetés folytatását, miután a szabály végrehajtja a műveleteit.

### Hook frissítése

A Marked nem végez teljes frissítést minden frissítésnél, így ha
olyan szkriptjei vannak, amelyek a DOM egyes részeit jelenítik meg, amire szükségük van
hogy a Marked's Hook API használatával futtassák renderelési funkciójukat.

Az alábbi példa a Mermaidet használja, amit valójában soha
meg kell tennie, mivel a Mermaid már alapértelmezés szerint benne van. De
itt van, hogyan csinálná, ha manuálisan venné fel.

Adjon hozzá egy **JavaScript beillesztése** műveletet, és a „JS szerkesztése”
ablakban inicializálja a szkriptet, és adja hozzá a horgot:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Ez azt eredményezi, hogy a `mermaid.run()` minden alkalommal végrehajtódik
A Megjelölt részleges frissítést hajt végre.

### Tesztszabályok

A Szabályok listája alatti _Test Rules_ gomb megnyílik a
párbeszédablak, ahol kiválaszthat bármilyen Markdown fájlt, és az lesz
minden Szabálya szerint tesztelve. Szabályok, amelyek megfelelnek
bal oldalon zöld füllel kiemelve. Párosításkor
egy fájl ellen, egy X gomb jelenik meg, amely használható
törölje a tesztet, és szüntesse meg a sorok kiemelését.

## Fogd és vidd

A Conductor ablak támogatja a továbbfejlesztett drag and drop funkciót
képességek, amelyek intelligensen felismerik a fájltípusokat és
megfelelő műveleteket biztosít a húzott fájl alapján. A
A megvalósítás tartalmaz egy osztott átfedő rendszert a szöveghez
fájlokat, amelyek lehetővé teszik a felhasználók számára, hogy válasszanak a fájl tesztelése között
szabályok ellen, vagy cselekvésként történő hozzáadásával.

![Drag and Drop in Custom Rules][drag]

[drag]: images/draganddropconductor.jpg @2x width=800

### Fájltípus észlelése

A rendszer automatikusan felismeri a különböző fájltípusokat és
megfelelő fedvényüzeneteket jelenít meg:

- **CSS-fájlok** (`.css`): "CSS-fájl beszúrása" fedvény megjelenítése
- **JavaScript fájlok** (`.js`, `.javascript`): A „Beszúrás”
  JS File" fedvény
- **Szkriptfájlok** (bármilyen végrehajtható fájl)): A „Run
  Command" fedvény
- **Szövegfájlok**: Megosztott fedvényt jelenít meg
- **Végrehajtható fájlok**: Megjeleníti a „Futtatási parancs” fedvényt
- **Ismeretlen kiterjesztések**: Alapértelmezés szerint "szöveg" típusú, és megjelenik
  osztott fedvény

## Egyéni processzornapló [customprocessorlog]

Ha furcsa eredményeket kap, és meg szeretné tekinteni, mi történik, az egyéni szabályok naplója megmutatja, hogy milyen szabályok és milyen sorrendben futnak. A **Súgó->Egyéni szabályok naplójának megjelenítése** segítségével nyissa meg. A meghívott **Run Rule** műveletek és a kihagyott beágyazott hívások is itt kerülnek naplózásra.

![Egyéni szabályok naplója][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Több parancs végrehajtása

Egy szabályhoz több parancs is tartozhat egymás után. A kimenete
minden parancs átkerül a következőre. Ha szeretnél
egy parancs a Marked parancsával egy időben ad ki valamit
megtekintheti a frissítéseket, ügyeljen arra, hogy visszaadja az eredeti tartalmat
STDOUT-ra a következő parancs vagy beépített parancs feldolgozásához
processzor.

Például, ha egy parancsot szeretne frissíteni egy PDF-fájlt
dokumentumot a Pandoc használatával, csak adja meg az eredeti fájl elérési útját
(környezeti változóktól) a Pandoc-hoz megfelelővel
parancssori beállításokat, majd visszhangozza vissza az STDIN tartalmat
ki STDOUT-ra.

## Az egyéni processzorok dinamikus megkerülése

Ha egy egyéni processzor a „NOCUSTOM” értéket adja vissza az STDOUT-on, megjelölve
leállítja az egyéni processzort, és visszatér a
alapértelmezett belső processzor. Ez lehetővé teszi, hogy létrehozza a
egyedi processzor, amely el tudja dönteni, hogy szükség van-e rá
futtassa a [környezeti változókkal] (#environmentvariables)
alább a dokumentum fájlneve vagy kiterjesztése, a tartalomegyeztetés
vagy más logika.

Ha a `NOCUSTOM` helyett egyéni processzor tér vissza
`MULTIMARKDOWN` vagy `DISCOUNT` (vagy `GFM`), `KRAMDOWN` vagy
`COMMONMARK`, akkor ezt a belső processzort használja a rendszer
csak az a dokumentum. Ez a módosítás nem érinti az alapértelmezettet
processzor beállítása a Beállításokban.

## Környezeti változók

A Parancs futtatása műveletnek van egy környezetszerkesztője, ahol Ön
beállíthatja saját környezeti változóit, amelyek lesznek
elérhető a parancs vagy a szkript számára. Ezeken kívül
egyéni változókat, a Marked tartalmaz néhány saját változót is.

A Marked saját héjában futtatja az egyéni processzort, azaz
a szabványos környezeti változók nem kerülnek átadásra automatikusan.
A Marked környezeti változóival bővítheti saját magát
a saját forgatókönyveiben. A Marked a következő változókat hozza létre
használható a shell szkriptekben:

**MARKED_ORIGIN**
: Az elsődleges munkafájl helye (alapkönyvtár) (a munkaszöveg mappája, a Scrivener vagy az indexfájl).

**PATH**
: Megjelölve beállít egy elérési utat, amely tartalmazza az alapértelmezett végrehajtható mappákat, és hozzáfűzi a fenti `MARKED_ORIGIN` könyvtárat. Az alapértelmezett értékek: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Hozzáadhatja sajátját a PATH változó szükség szerinti beállításával, és a Marked elérési útjának hozzáfűzésével vagy felülírásával (pl. `PATH=/usr/local/yourfolder:$PATH`).

**OTTHON**
: A bejelentkezett felhasználó saját könyvtára. A Python és más szkriptek, amelyek a beállított HOME változóra támaszkodnak, automatikusan felveszik ezt, de a szkriptekben más célokra is elérhető.

**MARKED_EXT**
: A feldolgozás alatt álló elsődleges fájl kiterjesztése. Ez a változó lehetővé teszi, hogy a megtekintett fájl típusától függően különböző folyamatokat írjon le. Például, ha `$MARKED_EXT == "md"` futtassa az előnyben részesített Markdown processzort, de ha `$MARKED_EXT == "textile"` egy Textil processzort.

**MARKED_PATH**
: Ez a teljes UNIX elérési útja annak a fő fájlnak, amely a betöltéskor megnyílik a Megjelölt mappában.

**MARKED_INCLUDES**
: A megjelölt fájl idézőjeles, vesszővel elválasztott listája, amelyet az átadott szövegbe foglaltak a különböző [include syntaxes](Special_Syntax.html#pagebreaks) használatával.

**MARKED_PHASE**
: Ez vagy "PROCESS" vagy "PREPPROCESS" lesz beállítva, ami lehetővé teszi, hogy egyetlen szkriptet használjon mindkét fázis kezelésére e változó alapján.

**MARKED_CSS_PATH**
: Az aktuális stíluslap teljes elérési útja

### Metaadatkörnyezeti változók

Amikor a Parancs futtatása művelet végrehajtásra kerül a Markedben
Konduktor rendszer, a dokumentum metaadatai automatikusan
kinyerjük és környezeti változóként elérhetővé teszik a
parancsot.

#### Hogyan működik

1. **Metaadat-kinyerés**: A rendszer a metaadatokat a meglévő `extractMetaDataFromString:` módszerrel kinyeri a dokumentumból, amely támogatja:
   - YAML elülső anyag (`---` blokk)
   - MultiMarkdown metaadatok (kulcs: értéksorok)
   - Pandoc metaadatok (`%` címblokkok)
   - HTML megjegyzés metaadatok (`<!-- key: value -->`)

2. **Kulcsok normalizálása**: A metaadatkulcsok normalizálva vannak környezeti változóként való használatra:
   - Kisbetűssé alakítva
   - Minden nem alfanumerikus karakter eltávolításra kerül
   - A szóközök és a speciális karakterek megvonásra kerülnek

3. **Környezeti változó formátuma**: Minden metaadatkulcs környezeti változóvá válik `MD_` előtaggal:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Példa

Adott egy dokumentum a következő metaadatokkal:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

A következő környezeti változók állnak rendelkezésre
parancsok:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Használat a parancsokban

Most már használhatja ezeket a környezeti változókat a Futtatásban
Parancs műveletek:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Támogatott műveletek

Ez a metaadat-környezetre változó funkció
elérhető:

- **Parancs futtatása** műveletek
- **Futtassa az Embedded Script** műveleteket

A metaadatok automatikusan kivonásra kerülnek a dokumentumból
tartalmat, és elérhetővé kell tenni minden olyan parancs vagy szkript számára
végigfut ezeken a műveleteken.

## Engedélyezés és letiltás

Az egyedi processzorok be- és kikapcsolhatók
egyedi dokumentumokat a {% kbd opt cmd C %} használatával. Te
Előfeldolgozót vagy processzort is bekapcsolhat egy dokumentumhoz
automatikusan [metaadatok használatával](#perdocument) a tetején
a dokumentumot.

Az egyes dokumentumok feldolgozóinak aktuális állapota:
jelzőfényként jelenik meg (csak akkor látható, ha egy processzor
engedélyezve van) az eszköztár elemeitől balra alul
az Előnézet jobb oldali eszköztárában.

### Előfeldolgozó

Ha beállítja az előfeldolgozó szabályokat, azok a Marked után futnak le
kezel minden Megjelölt-specifikus feladatot, például a külsőt is
dokumentumokat és kódot, de mielőtt lefutná a processzort
(belső vagy egyedi). Ez lehetőséget ad a renderelésre
egyéni sablonváltozók, helyettesítések kezelése vagy injektálás
a saját tartalmat bármilyen más módon.

A Marked beállít egy környezeti változót a munkavégzéshez
könyvtárból (`MARKED_ORIGIN`) a szülőkönyvtárba
fájl előnézete folyamatban van. Ezzel megváltoztathatja a működést
egy szkript könyvtárába, és tartalmazzon fájlokat relatív elérési úttal
az eredeti dokumentumhoz. Például Rubyban megteheti
használd:

	Dir.chdir(ENV['MARKED_ORIGIN'])

Ha engedélyezve van, az egyéni előfeldolgozó bekapcsolható és
kikapcsolva az egyes dokumentumok használatához
{% kbd ctrl opt cmd C %}.

#### Dokumentumfeldolgozó/előfeldolgozó [dokumentum]

Az egyéni processzorok dokumentumonként is beállíthatók
a metaadat formátum használatával a [Dokumentumonként
beállítások](Per-Document_Settings.html).

Megadhatja, hogy használjon-e egyéni processzorbeállításokat és
felülírja a dokumentum alapértelmezett értékét a [Dokumentumonkénti
beállítások](Per-Document_Settings.html) (`Custom Processor:`
és `Custom Preprocessor:`). Bármilyen beállítás, amely nem "igaz"
vagy az "igen" letiltja az egyéni elő-/feldolgozót.

Használati példa:

    Egyedi processzor: igaz
    Egyéni előfeldolgozó: false

Amint azt a [Dokumentum
Beállítások](Per-Document_Settings.html#hidingmeta) oldal, te
körülveheti ezeket a metaadatokat HTML megjegyzésjelölőkkel az elrejtéshez
a GitHubból és más processzorokból, amelyek nem távolítják el
a kimenetből:

    <!--
    Egyedi processzor: igaz
    Egyéni előfeldolgozó: igaz
    -->

## Alternatív Markdown processzor használata

Bármilyen Markdown íz, amelyet a parancssorból megjeleníthet
használható a Marked. Képesnek kell lennie befogadni a bemenetet
STDIN, ami ugyanaz, mint a Markdown rárakása
parancssor, azaz `cat myfile.md | myprocessor`. Szükség van rá
hogy visszaadja a kapott HTML-t az STDOUT-on, amely minden
A processzor, amellyel valaha is dolgoztam, alapértelmezés szerint működik.

Használja a `which YOUR_PROCESSOR`-t a Terminálban az elérési út meghatározásához
a végrehajtható fájlba, majd illessze be a Run Command elérési útjába
mezőbe, vagy egyszerűen húzza a végrehajtható fájlt az Egyéni szabályok ablakba
azzal a szabállyal, amelyhez hozzá szeretné adni a kiválasztott műveletet.

Ha a processzor argumentumokat igényel a parancssorban,
ezeket is be kell írnia a mezőbe. Néhány
a processzoroknak kötőjelekre van szükségük ahhoz, hogy STDIN és/vagy STDOUT rendszeren működjenek,
pl. `-o - -` gyakran jelzi a bemenetet az STDIN-ről, a kimenetet a következőre
STDOUT. A részletekért lásd a processzor dokumentációját.

Kipróbáltam az egyéni processzor funkciót a Pandoc segítségével,
Kramdown, jelzett (kedvezmény), MultiMarkdown 6, Maruku és
különféle egyéb ízek.

### Megjegyzés a Pandoc-ról és a Sandboxingról

A Pandoc (és néhány más parancssori eszköz) nem fut be
a Marked Mac App Store (sandboxos) verziója.
Ha szüksége van a Pandoc futtatására, használja a **Súgó->Crossgrade** parancsot, hogy a
ingyenes licenc a közvetlen (Paddle) verzióhoz. Ez igaz
minden olyan processzorról, amely sandbox problémákba ütközik: ha meg van jelölve
nem tudja végrehajtani a MAS engedélyekkel kapcsolatos problémák miatt, akkor fog
ajánlja fel a crossgrade lépéseit. Ha problémákat tapasztal
és ez nem történik meg, kérem, vegye fel velem a kapcsolatot a
[támogatási webhely](https://support.markedapp.com/questions/add).

### Pandoc, mint a svájci hadsereg leértékelési processzora

A [Pandoc](https://pandoc.org/) messze a legrugalmasabb
univerzális eszköz a jelölési formátumok tömbjének kezelésére. által
`-f` argumentum hozzáadásával a következők egyikével, Pandoc képes
legyen az Ön egyéni feldolgozója a következők bármelyikéhez:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

És még egy csomó más. Lásd a [Pandoc
dokumentáció](https://pandoc.org/MANUAL.html) további információért
info. Ha ezek közül valamelyiket beviteli formátumként szeretné használni, egyszerűen adja hozzá a
a következőt a Futtatási parancs mezőben:

    /usr/local/bin/pandoc -f INPUT_FORMAT

A Pandoc tökéletes olyan szkript írásához, amely a
`$MARKED_EXT` környezeti változó a formátum meghatározásához
átfutni a Pandocon, vagy egy sor szabályt használni
kiterjesztés egyezik. Ha a kiterjesztés `md`, használja
`pandoc -f gfm` vagy `pandoc -f markdown_mmd` (vagy csak vissza
`NOCUSTOM` az STDOUT-on az alapértelmezett processzor használatához). De ha az
`textile`, futtassa a `pandoc -f textile` parancsot a szkripten belül. És ha
ez `wiki`, használd valamelyik wiki jelölőprocesszort. Megkapod
az ötlet.

A Pandoc rajongói tudni fogják, hogy a Pandoc is képes kezelni
kiterjedt bibliográfia és LaTeX forgatókönyvek. A legtöbb funkció
a parancssoron keresztül érheti el csak
átadási argumentumok használatával a Markedben.

## Textil használata

Néhányan megkérdezték, hogyan lehet a Textile-t munkába állni
Megjelölve. Rendelkezésre kell állnia egy textil átalakítónak
a parancssort. Van néhány lehetőség, köztük a Pandoc
(lásd fent), de ha még nincs telepítve a Pandoc,
két másik lehetőség a RedCloth a Ruby és a Textile a Perl számára
(A Fejlesztői eszközök telepítése szükséges). Telepítés
egyik vagy másik:

1. Telepítse Textile innen
   <https://github.com/bradchoate/text-textile> **VAGY**
   `sudo gem install RedCloth` a terminálban
2. A `which textile` vagy `which redcloth` segítségével határozza meg a
   használandó elérési út az Egyéni processzor elérési út beállításaiban

A Now Marked egy textil-előzetes az Ön számára!

## Az AsciiDoc használata

1. Telepítse az [AsciiDoctor]-t (http://asciidoctor.org/).
2. Engedélyezzen egy egyéni szabályt az {% prefspane Processor %}-ben, hogy illeszkedjen az AsciiDoc fájlokhoz.
3. Állítsa be a szabályt Processzor értékre, és adjon hozzá egy Futtatási parancsot
    1. Határozza meg a `asciidoc` elérési útját, amely lesz
       valami ilyesmi: `/usr/bin/asciidoc` vagy
       `/opt/local/bin/asciidoc`. Ha bizonytalan, használja
       `which asciidoc` megtalálásához
    2. Írja be: `[PATH To asciidoc] --backend html5 -o - -` as
       a parancs (a végén lévő - a kimenetet mint
       STDOUT)

Ez elküldi az aktuális dokumentumot az STDIN-nek, és megjeleníti a
STDOUT néven generált HTML-t.

Lásd [ezt a lényeget](https://gist.github.com/mojavelinux/6324279)
from [Dan Allen](https://gist.github.com/mojavelinux) for
további információ.