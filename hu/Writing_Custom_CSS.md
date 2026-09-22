# <%= @title %>

A Markednek van egy beépített stílusszerkesztője, és egyéni CSS-fájlokat is tud alkalmazni.

A szerkesztő segítségével gyönyörű stílusokat hozhatsz létre, vagy ha éppen annyira ismered a CSS-t, hogy az már veszélyes, a Markedet tetszés szerint testre szabhatod.

## Első lépések [getting-started]

A fejlesztő és a felhasználók által készített Egyéni stílusokból galéria érhető el a [markedapp.com/styles](https://markedapp.com/styles/) oldalon. A galéria lehetővé teszi, hogy a stílusokat közvetlenül a Markedben nézd meg előnézetben, és telepítsd őket. Bármelyik telepített stílus megjeleníthető a Finderben vizsgálat és módosítás céljából. A galéria megnyitható egy belső nézegetővel {% appmenu Style, Generate a Custom Style %} paranccsal, vagy kattints a ceruza (szerkesztés) ikonra bármelyik szerkeszthető stílus mellett a Stíluskezelőben. Ha egy beépített stílust szeretnél szerkeszteni, először duplikálnod kell azt a kezelőben.

Van egy [tárhely az Egyéni stílusoknak](https://github.com/ttscoff/MarkedCustomStyles) is a GitHubon, példákkal. Nyugodtan böngészd, használd, és járulj hozzá te is. Ha az alapstílusok egyikére épülő témát terjesztesz, szívesen látjuk, ha közreműködőként feltünteted magad a köszönetnyilvánításban.

A Marked azon képességével, hogy egyéni CSS-fájlokat használjon, az Előnézet testre szabásának szinte nincs határa. Minden CSS3-lehetőség, ami a Safariban működik, a Markedben is működni fog. Az alapértelmezett Markdown-fájlokkal a Markedben csak néhány HTML-elemet kell kezelned; a teljes tartalom egy "wrapper" azonosítójú div-ben van, minden más a dokumentum jelölésétől függ.

Ha saját használatra tervezel, nincsenek szabályok. Kapcsold be a CSS-követést az egyéni CSS-választó alatti jelölőnégyzettel, és amikor szerkeszted és mented az egyéni CSS-t, az frissíti az előnézetet.

**Egy [alapsablon-téma elérhető](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) a kezdéshez.**

Ha a CSS-alkotásodat meg szeretnéd osztani, van néhány pont, amit érdemes lefedned. Először is, vannak bizonyos body-osztályok, amelyeket stílusokkal kell ellátni:

## Body-osztályok [body-classes]

A következő stílusokat minden megosztásra szánt Marked CSS-nek tartalmaznia kell. A body-osztályok lehetővé teszik, hogy különböző beállítási opciók alatt célozz meg és módosíts bármely szelektort.

### Invertált [inverted]

Amikor a felhasználó a {% appmenu Preview, Dark Mode %} opciót választja, egy "inverted" osztály kerül a body tagre. Ezzel célozhatod meg a magas kontrasztú, sötét alapon világos stílusokat.

Az invertált stílusokat csak az előnézetre szeretnéd alkalmazni, nyomtatásra nem, ezért használj media query-t (@media screen) a korlátozáshoz. Az alábbi kód meglehetősen univerzális, és a legtöbb esetben egyszerűen beillesztheted a stíluslapodba a kompatibilitás érdekében, de nyugodtan alakítsd át.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Vers (Poetry) [poetry]

A felhasználó kiválaszthatja, hogy a tabulátorral behúzott szöveg versként vagy kódként jelenjen-e meg. Az egyetlen különbség, hogy a pre/code blokkok stílusa "költőibb", ha a vers mód van kiválasztva. A "poetry" osztály kerül a body tagre.

Legyél annyira kreatív a formázással, amennyire csak szeretnél, de itt egy alapszintű részlet:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Speciális esetek [special-cases]

A táblázatokat, a Figure/Figcaption elemeket, valamint a `a.footnote` és `div.footnotes>a` speciális esetét is figyelembe kell venni. Nincsenek rögzített szabályok arra, hogyan kezeld ezeket, de nézd meg az alapértelmezett stílusokat, hogy képet kapj arról, milyen CSS-szabályokra van szüksége a Markednek.

Az alapértelmezett stílusok mindegyikében a szabványos táblázatstílus áttetszőséget alkalmaz a váltakozó sorokon, hogy lágyan illeszkedjen bármilyen háttérhez. Átveheted ezeket a stílusokat, vagy mehetsz saját utadon, csak ügyelj rá, hogy mindenképp stílusozd őket! Ugyanez érvényes a figure és figcaption elemekre is; adj egy képet alt szöveggel egy dokumentumhoz, hogy lásd, hogyan alakul ki a jelölés, és stílusozd megfelelően.

A dokumentumban szereplő lábjegyzetek egy hivatkozást jelenítenek meg a tartalmon belül (a.footnote), és egy div-et a végén a hivatkozott szöveggel (div.footnotes). Ismét, nézd meg az alapértelmezett stílusokat referenciaként. Hogy elkerüld a sortávolság megváltozását azokon a sorokon, amelyek lábjegyzet-hivatkozási számot tartalmaznak, mindenképp illessz be valami ilyesmit:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Ahhoz, hogy a visszatérő nyíl ugyanabban a sorban maradjon, illeszd be a következőt:

```css
.footnotes p {display:inline}
```

Az is jó ötlet, ha egy általános szabályt adsz meg minden képre, hogy azok az oldal szélességén belül maradjanak. Valami ilyesmi:

```css
#wrapper img { max-width: 100% }
```

Ha a témádnak extra belső margója vagy fix szélessége van, módosítsd a max-width értéket ennek megfelelően.

## Nyomtatási stílusok [printstyles]

Mindenképp adj meg nyomtatási stílusokat, amelyek eltávolítanak minden háttérszínt, fix görgetést és csak az előnézetre vonatkozó felületi elemeket. A Marked két módot kínál a nyomtatás és a PDF-kimenet megcélzására.

### `@media print` [media-print]

A szabványos CSS nyomtatási szabályok érvényesek, amikor a Markedből nyomtatsz, vagy amikor a PDF-exportálás nyomtatási médiát használ:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### A `.mkprinting` osztály [the-mkprinting-class]

Amikor a Marked egy dokumentumot **PDF-exportáláshoz** vagy **Nyomtatási/PDF-előnézethez** ({% kbd cmd P %}) készít elő, hozzáadja a `mkprinting` osztályt a `<body>` taghez (az olyan exportálási osztályok mellett, mint a `bandw`, `breakAfterTOC`, valamint a stílusod `mkstyle--*` osztálya). A Marked beépített témái ezt az osztályt használják a legtöbb nyomtatásspecifikus szabályhoz, ahelyett hogy kizárólag a `@media print`-re támaszkodnának.

A PDF-exportálás gyakran **screen** médiával tölti be a rejtett renderelő WebView-t (különösen egyéni stílusok és [Fountain](Fountain_for_Screenwriters.html) dokumentumok esetén), így a stíluslapodban lévő `@media print` blokkok **nem feltétlenül** vonatkoznak a PDF-kimenetre. A `.mkprinting` előtaggal ellátott szabályok mindig érvényesülnek exportáláskor, mivel ezek egyszerű osztályszelektorok, nem media query-k.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Azokhoz a stílusokhoz, amelyeknek **mind** a böngészős nyomtatásban, **mind** a Marked PDF-exportálásban működniük kell, duplikáld a kritikus szabályokat, vagy kombináld a szelektorokat:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Egyéni stílus vs. Kiegészítő CSS.** Egy Egyéni stílus stíluslapon belül írd a `.mkprinting #wrapper …` kódot a fent bemutatott módon. A **Kiegészítő CSS** mezőben a Marked átírja a szelektorokat a beillesztés előtt --- ehelyett a body-val minősített formát használd:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Lásd a [Kiegészítő CSS beállításai](#additional-css-settings) részt, hogy megértsd, hogyan működik az átírás, és miért nem illeszkedik ott önmagában a `.mkprinting #wrapper …`.

Amikor egyéni nyomtatási CSS-t hibakeresel, nyisd meg a Nyomtatási/PDF-előnézetet, vagy exportálj PDF-be, majd használd a [Safari Web Inspectorát](#webkitinspector) a dokumentum vizsgálatához --- a `<body>` elemen a `mkprinting` osztály lesz jelen, amíg a nyomtatási elrendezés aktív.

A hivatkozások elrejtése nyomtatáskor a fő témán kívül van kezelve, így a felhasználók választhatják, hogy a hivatkozáskiemelések és aláhúzások rejtve legyenek-e a kinyomtatott dokumentumban. Amíg a szöveghez be van állítva egy alapstílus, ezzel nem kell foglalkoznod.

Szóval, láss neki. Alakítsd át a blogtémádat, alkoss egy ütős nyomtatási stílust a PDF-dokumentumokhoz, vagy készítsd el a tökéletes előnézetet az általad írt tartalomtípushoz. Ha valami remeket alkotsz, [oszd meg a közösséggel](https://markedapp.com/styleshare/).

## Kiegészítő CSS beállításai [additional-css-settings]

A {% prefspane Style %} területen szerkesztheted a **Kiegészítő CSS**-t. Ezek a szabályok **hozzáфűződnek bármelyik betöltött témához**. Ezek egy szándékosan részleges átfedő réteget alkotnak, nem egy teljes témát. Ha egy teljes stíluslapot illesztesz be ebbe a mezőbe --- vagy ugyanazt a részleges lapot a [Stíluskezelőn](Custom_Styles.html) keresztül importálod, mintha az egy téma lenne ---, akkor minden, amit a lap nem fed le, stílus nélkül marad.

### Szelektorok átírása [additional-css-selector-rewriting]

A Marked a beillesztés előtt átírja a Kiegészítő CSS szelektorait (mint `body.mk-has-additional-css …`), hogy a szabályok az előnézetre korlátozódjanak:

- Az a szelektorrész, amely már `body` vagy `#wrapper` kezdetű, megkapja a `body.mk-has-additional-css` előtagot, a body-osztályok pedig összevonásra, nem beágyazásra kerülnek.
- Bármely más szelektorrész a `body.mk-has-additional-css #wrapper …` alá kerül korlátozásra.
- A Marked által a `<body>`-en beállított kezdő body-osztályokat --- beleértve a `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` és `.mkstyle--*` osztályokat --- a rendszer úgy kezeli, mint a `body`-et, és a body-szelektorra vonja össze, ahelyett hogy a `#wrapper` alá ágyazná be őket.

| A Kiegészítő CSS-be beírva | Eredmény |
| :-- | :-- |
| `#wrapper h2` | Illeszkedik (megfelelően korlátozva) |
| `body.mkprinting #wrapper p` | Illeszkedik nyomtatás/PDF közben |
| `.mkprinting #wrapper p` | **Nem** illeszkedik (beágyazott `#wrapper`-t igényelne) |
| `:root { --x: 1; }` | **Nem** illeszkedik (egyéni tulajdonságokhoz inkább a `body` vagy `#wrapper` ajánlott) |

Az ebben a mezőben lévő nyomtatási szabályokhoz inkább a `body.mkprinting #wrapper …` ajánlott. Ugyanaz a vizuális szándék egy Egyéni stílus fájlban megtarthatja a rövidebb `.mkprinting #wrapper …` formát.

A Kiegészítő CSS-nek **nincs méretkorlátja, és nem történik CSS-érvényességi ellenőrzés sem**. A Marked tárolja és beilleszti, amit megadsz; az érvénytelen CSS egyszerűen nem fejt ki hatást az előnézetben.

### HTML és egyéb exportálások [additional-css-exports]

A Kiegészítő CSS érvényesül az élő előnézetben, a Nyomtatási/PDF-előnézetben, a PDF-exportálásban, valamint a **HTML-exportálásban** is, amikor a stílusok bele vannak foglalva --- az exportált `<body>` megkapja a `mk-has-additional-css` osztályt, hogy az átírt szelektorok illeszkedjenek. A DOCX, ODT és EPUB saját stílusozási útvonalakat használ, és nem alkalmazza a Kiegészítő CSS-t ugyanúgy.

[Magas specifitás](#overridingspecificity) használatával, `@media` lekérdezésekkel nyomtatáshoz és képernyőhöz, valamint `body.mkprinting` szelektorokkal (ebben a mezőben) vagy `.mkprinting` szelektorokkal (Egyéni stílusokban), némi CSS-tudással szinte minden stílusbeli szempontot irányítás alatt tarthatsz.

## WebKit Inspector [webkitinspector]

A Safari Web Inspectora a legegyszerűbb módja annak, hogy pontosan lásd, milyen HTML-t és CSS-t generál a Marked, és hogy élőben kísérletezz az Egyéni stílusokkal.

### A Fejlesztés menü engedélyezése a Safariban [enabling-the-develop-menu-in-safari]

1. Nyisd meg a Safarit, és válaszd a {% appmenu Safari, Settings… %} parancsot.
2. Válaszd a **Speciális** fület.
3. Engedélyezd a **Webfejlesztői funkciók megjelenítése** opciót (régebbi macOS-verziókon **Fejlesztés menü megjelenítése a menüsávban**).

Az engedélyezés után egy **Fejlesztés** menü jelenik meg a Safari menüsávjában.

![Safari Fejlesztés menü, amely a Marked dokumentumokat mutatja][develop-menu]

### Egy Marked-dokumentum vizsgálata [inspecting-a-marked-document]

1. Nyisd meg egy előnézeti ablakot a Markedben, majd válts át a Safarira.
2. A menüsávból válaszd a **Fejlesztés → _\<a Mac neved\>_ → Marked → _\<dokumentum címe\>_** parancsot.
3. A Safari megnyit egy Web Inspector-ablakot, amely a kiválasztott Marked-előnézethez kapcsolódik.

Innen a következőket teheted:

- Az **Elemek** fülön megvizsgálhatod a DOM-ot a `#wrapper` div-en belül, és láthatod, mely CSS-szabályok érvényesülnek.
- Az elemek fölé húzva a DOM-fában kiemelheted őket a Marked ablakában.
- A **Stílusok** oldalsávval élőben módosíthatod a szabályokat, majd a működő részleteket visszamásolhatod egy Egyéni stílusba vagy a **Kiegészítő CSS**-be.
    - Miután az Elemek fülön szerkesztetted a CSS-t, a Módosítások fülön összefoglalót kaphatsz a szerkesztéseidről

	![Módosítások][css-changes]
- A **Konzol** fülön JavaScriptet futtathatsz az élő előnézeten. A teljes [Marked JavaScript API](https://markedapp.com/help/jsapi/) elérhető ebben a konzolban.
- Fedezz fel más füleket is, például a **Hálózat** fület, amikor a dokumentumod által betöltött erőforrásokat vizsgálod.

![Egy Marked-előnézet vizsgálata a Safari Web Inspectorával][inspecting]

## Egyéni CSS megosztása [sharing-custom-css]

Használd a {% appmenu Style, Share a Custom Style %} parancsot, hogy megnyisd a megosztó alkalmazást a webböngésződben. Húzd a CSS-fájlodat a leejtési területre (vagy kattints a lemezről történő kiválasztáshoz), és töltsd fel az Egyéni stílusodhoz tartozó CSS-t.

A megosztott stílusokat a fejlesztőnek jóvá kell hagynia, mielőtt megjelennének a galériában, ezért ne számíts azonnali eredményre.

## Egyéb tippek [other-tips]

### A specifitás felülbírálása [overridingspecificity]

A Marked előnézeten belül egy, az aktuális stílus fájlnevén alapuló body-osztály kerül hozzáadásra. Ha az előnézet "Swiss" stílusra van állítva, akkor a `<body>` tagen lesz egy `mkstyle--swiss` nevű osztály. Ha az egyéni CSS-ed neve MyCustom.css, akkor a body-osztály `mkstyle--mycustom` lesz. Ezt felhasználhatod arra, hogy az alapstílusokban meghatározott szabályok elé helyezd, és így felülbíráld őket. Ahhoz, hogy egy szabályban abszolút specifitást érj el, használd a konténer div #wrapper azonosítóját is:

	.mkstyle--mycustom #wrapper p+p { ... }

### A tartalomjegyzék stílusozása [table-of-contents-styling]

Ha a `<!--toc-->` tokent használod [tartalomjegyzék beszúrásához](Special_Syntax.html#tableofcontents), az Egyéni stílusban felülbírálhatod a tartalomjegyzék szintjelzőinek beállításait a "#wrapper" használatával a specifitás növeléséhez:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Ez azt eredményezné, hogy a Tartalomjegyzék összes listaeleme négyzet alakú felsorolásjelet használ ahelyett, amit a Beállításokban megadtál, amikor az Egyéni stílusod aktív.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
