<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Tekintse meg a dokumentumokat *a maga* módján.

## Egyéni stílusok használata

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Az egyéni stílusok felfedezésének legegyszerűbb módja a
[Egyedi stílusú galéria][2]. Innen böngészhet a
elérhető stílusok működés közben, telepítse őket a kattintással
gombot, és még [küldje be saját alkotásait][6]
befogadás.

Egyéni stíluslapok hozzáadásához a helyi meghajtóról a Markedhez,
használja a {% prefspane Style %}-t. Új stílusok kerülnek hozzáadásra
a legördülő menük az Ablakbeállításokban és az egyes ablakokban,
és a CSS-fájl alapfájlneve alapján lesz elnevezve
tette hozzá. Tárolja egyéni CSS-fájljait biztonságos helyen
meghajtó. Ha a meghajtón mozognak, eltávolítják őket
Megjelölve, amíg újból hozzá nem adja őket az új helyről. ez van
jó ötlet a megnyitott dokumentumok bezárása és a stílus eltávolítása
által használt CSS-fájl törlése vagy átnevezése előtt a Beállítások menüből
Megjelölve. Nem tör el semmit, ha nem, de megment
némi zavartság.

Adjon hozzá egyéni stílusokat a Stíluskezelővel a Hozzáadás gombbal, vagy húzzon egy vagy több CSS-fájlt a Beállításokba
ablaktáblát.

## Stílusok kezelése a Stíluskezelővel

A Stíluskezelő elindítása egyetlen helyen kínál minden beépített elemet
és egyéni téma. Kattintson a **Stílusok kezelése…** gombra az {% prefspane Style %}
ablaktábla,
vagy egyszerűen dobja be a CSS fájlokat a beállítások ablakba --- A Megjelölve importálja őket,
nyissa meg a Stíluskezelőt, és válassza ki az újonnan hozzáadott sort. CSS húzása
fájlok közvetlenül a Stíluskezelő ablakban is működnek; amikor több fájl
elhúzva látni fogja a fedvényfrissítést az „N egyéni stílus hozzáadása” értékre, így egyértelmű
tételt importál.

![][img-style-manager]

A Stíluskezelőben talál egy rendezhető táblázatot, amely keveri a beépített és a
egyedi stílusok. Minden sor a következőket kínálja:

- Egy **Engedélyezve** jelölőnégyzet, amely azonnal hozzáadja/eltávolítja a stílust a Stílusból
  menüt, az Alapértelmezett stílus előugró ablakot és a billentyűparancsokat. Az aktuális letiltása
  aktív stílus automatikusan átvált a következő elérhető bejegyzésre.
- Egy **Név** oszlop, amelyet soron belül szerkeszthet; a változások továbbra is fennállnak, és mindenkire kiterjednek
  menüt. Kattintson a stílus nevére a helyén való szerkesztéshez.
- Egy **Forrás** oszlop, amely a Beépített, Egyéni vagy Duplikált elemeket hívja meg.
- Egy **Műveletek** verem a **Szerkesztés** gombokkal (megnyitja a CSS-fájlt a
  szerkesztő), **Duplikálás** (másolat és új CSS-fájl létrehozása a lemezen), **Reveal**
  (megjeleníti a fájlt a Finderben), és a **Törlés** (a hivatkozás eltávolításának lehetőségeivel vagy
  helyezze át a CSS-fájlt a kukába).

A sorok húzással átrendeződnek, és a sorrend a Stílus menüt is irányítja
a `⌘/#` parancsikon-hozzárendeléseket, így szó szerint áthúzhatja a stílusokat a helyekre
akarod. A külső CSS-fájlokat adott pozíciókba is húzhatja; a csepp
indikátor határozza meg, hogy hova kerül az új stílus.

### Élő előnézet

A jobb oldali ablaktábla egy előnézetet tartalmaz, amely megjeleníti a kiválasztott stílust
egy teljes HTML-dokumentum belsejében címsorok, listák, táblázatok, kódblokkok stb. átfogó készletével.
Az előnézet a tényleges CSS-t használja a lemezen, így a külső szerkesztőben végzett szerkesztések azonnal frissülnek. Egy jelölőnégyzet váltja a Sötét mód előnézetét.

További használati stílusokat találhat (vagy példákat a
saját létrehozása) [a GitHubon][1] (lásd a [példák][2] részt
egy gyors pillantás, mi van ott). Lásd: [Egyéni CSS létrehozása][3]
részletekért és tippekért.

## További CSS

A {% prefspane Style %} alatt talál egy lehetőséget
További CSS címmel a "CSS szerkesztése" gombbal.
Erre a gombra kattintva megnyílik egy ablak, ahol hozzáadhat
univerzális CSS-szabályok, amelyek minden stílusra vonatkoznak. Megjegyzés
hogy a szabályok sajátossága akkor lehet fontos
felülírja a Marked néhány alapértelmezett stílusát. A fő test
A dokumentum „#wrapper” azonosítójú div-be van csomagolva.
A választó előtagja ezzel könnyebbé teheti
felülírja, pl.:

    #wrapper img { szélesség: 100%; magasság: auto; }

Ebben a mezőben a CSS minden dokumentumra érvényes lesz, nem
mindegy, hogy milyen stílust használ. Ha egyéni stílust szeretne alkalmazni
Feltételes egyezéseken alapuló CSS, használja a Stílus beállítása, Beszúrás parancsot
CSS-fájl vagy CSS-műveletek beszúrása a {% prefspane Processor %}-ban
Egyéni szabályok.

## Nyomtatás és PDF exportálás

A megjelölt beépített `@media print` blokkot (`mkprintstyles`) szúr be minden
előnézet. Alapértelmezéseket állít be, például **10pt** alapot a `html`, `body` és
`#wrapper` (vagy a méret az **Egyéni betűméret exportáláshoz/nyomtatáshoz** in
{% prefspane Export %}, ha ez az opció engedélyezve van), és normalizálja a bekezdést
szöveget `p { font-size: 1em; }` és `li p { font-size: 1em; }` karakterekkel, tehát
A csak képernyőre vonatkozó szabályok, mint például a `p { font-size: 1.1429em; }`, nem növelik fel a szövegtörzset
PDF-ben és nyomtatott formában.

A PDF-exportálás **nyomtatási** vagy **képernyős** médiát használhat a rejtett WebView-n
generáció. A beépített témák általában nyomtatott médiát használnak; **egyedi stílusok** és
[Fountain](Fountain_for_Screenwriters.html) dokumentumok gyakran használnak képernyős médiát, így
elrendezése megegyezik az előnézettel. Ez azt jelenti, hogy a `@media print { ... }` szabályok nem
mindig alkalmazva a PDF-exportálás során.

A megbízható PDF és Print/PDF Preview stílus érdekében az előtagválasztókat a
A `mkprinting` osztály megjelölve hozzáadja a `<body>` elemet az exportálás során (lásd [Egyéni írás
CSS](Writing_Custom_CSS.html#printstyles) részletekért és példákért). Használhatod
`.mkprinting` egyedül, vagy kombinálja a `@media print`-al, ha mindkét útra van szüksége
fedett.

A Marked nyomtatási alapértelmezéseitől eltérő méretek beállításához adjon hozzá explicit szabályokat
egyéni CSS-jét (vagy a További CSS-ben). Használja a `!important`-t, amikor szükséges
felülírja Marked beszúrt nyomtatási stílusait --- például:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}
```

A `!important` nélküli szabályok elveszhetnek a `mkprintstyles` későbbi szabályaival szemben, vagy
egyéb minősíthetetlen válogatók a lapon, amelyek továbbra is érvényesek a nyomtatásban. Elhelyezés
csak nyomtatásra vonatkozó módosítások a `@media print` és/vagy a `.mkprinting` szabályokban (ahelyett
csak a képernyőszabályokban) megkönnyíti az előnézeti és exportálási viselkedést
kb.

## CSS-változások figyelése

Bejelölhet egy négyzetet az {% prefspane Style %} Egyéni stílusok szakaszában.
hogy a Megjelölt figyelje az aktív CSS-fájlt
a szerkesztett Markdown fájlon kívül. Mikor
bármelyik fájlban változást észlel, az előnézet megtörténik
frissítés. Ez hasznos egyéni stílusok szerkesztéséhez anélkül
folyamatosan frissül, és egyszerű webre is használható
fejlesztési feladatokat.

Ez bizonyos alapvető webtervezési munkákhoz és CSS-hez is hasznos
kísérletezés (például egyéni stílusok létrehozása). Töltés a
Markdown fájl, amely tartalmazza az összes stílusozni kívánt jelölést
hozzon létre egyéni stílust, és nézze meg az előnézetet élőben
szerkesztés közben változik.

## Egyéni CSS írása

Ha ismeri a CSS-t, létrehozhatja saját stílusát
lapok használatához Marked. Lásd: [Egyéni CSS írása][3]
részleteket. Bármikor, amikor valami újat alkot, fontolja meg
[beküldése][6] a [galériába][2], hogy megosszák másokkal
felhasználókat. Feltétlenül ismerje meg az útmutatóban felsorolt alapokat, és
tartalmazza a metaadat megjegyzést a tetején.

### Automatikus egyéni stílusok a StyleStealer segítségével

Akár automatikusan is generálhat stílust egy alapján
meglévő webhely a [Style Stealer][4] segítségével. Ez lehetővé teszi, hogy betöltsön egy weboldalt, és megragadja a számított stílusokat a Markdownban található összes fő elemhez, majd elmentse egy egyéni stílusba.

![Stíluslopó][stíluslopó]

[stylestealer]: images/style-stealer-800.jpg @2x width=800


Egyéni stílusok kezelése (átnevezés, átrendezés, másolás és törlés) a [Stíluskezelő](Style_Manager.html) segítségével.

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center