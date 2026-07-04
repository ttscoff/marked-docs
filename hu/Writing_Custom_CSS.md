<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked beépített stílusszerkesztővel rendelkezik, és egyéni CSS-fájlokat is tud alkalmazni.

A szerkesztővel gyönyörű stílusokat hozhat létre, vagy ha éppen elég CSS-t ismer ahhoz, hogy veszélyes legyen, a Megjelölt megjelenést tetszés szerint alakíthatja.

## Első lépések

A [markedapp.com/styles] (https://markedapp.com/styles/) oldalon található a fejlesztő és a felhasználók által létrehozott egyéni stílusok galériája. A galéria lehetővé teszi a stílusok előnézetét és telepítését közvetlenül a Marked alkalmazásban. Bármely telepített stílus megjeleníthető a Finderben vizsgálat és módosítás céljából. A galéria megnyitható belső megjelenítővel a ⟧, vagy kattintson a következő ikonra ⟧, vagy kattintson a következő ikonra. a Stíluskezelő Ha szerkeszteni szeretne egy beépített stílust, először meg kell másolnia azt a kezelőben.

A GitHubon egy [egyéni stílusok tárháza](https://github.com/ttscoff/MarkedCustomStyles) is található példákkal. Nyugodtan böngészhet, használhat, és hozzájárulhat ott. Ha a témáját az egyik alaptéma alapján terjeszti, kérjük, bátran adja hozzá magát a kreditekhez közreműködőként.

Mivel a Marked képes egyéni CSS-fájlok használatára, az előnézet testreszabásakor az ég szab határt. A Safariban működő összes CSS3-beállítás a Megjelölt módban is működik. A Marked alapértelmezett Markdown fájljaival csak néhány HTML-elemet kell kezelnie; az összes tartalom egy divben van, "wrapper" azonosítóval, minden mást a dokumentum jelölése határoz meg.

Ha személyes használatra tervez, nincsenek szabályok. Kapcsolja be a CSS-követést az egyéni CSS-választó alatti jelölőnégyzet segítségével, és amikor szerkeszti és menti az egyéni CSS-t, az frissíti az előnézetet.

**Egy [csontváz téma áll rendelkezésre](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) a kezdéshez.**

Ha azt tervezi, hogy megosztja CSS-alkotását, néhány pontra ki kell térnie. Először is, van néhány testosztály, amelyekhez stílusokat kell alkalmazni:

## Testórák

A következő stílusoknak szerepelniük kell minden megjelölt CSS-ben a megosztáshoz. A törzsosztályok lehetővé teszik bármely választó megcélzását és módosítását különböző preferencia-beállítások mellett.

### Megfordítva

 Amikor a felhasználó kiválasztja az {% appmenu Preview, Dark Mode %} értéket, egy "fordított" osztály kerül hozzáadásra a törzscímkéhez. Ezzel megcélozhatja a nagy kontrasztú, világos és sötét stílusokat.

Csak azt szeretné, hogy a fordított stílusok az előnézetre vonatkozzanak, a nyomtatásra nem, ezért használjon médialekérdezést (@media screen) a korlátozásához. Az alábbi kód meglehetősen univerzális, és a legtöbb esetben a kompatibilitás érdekében egyszerűen bedobhatja a stíluslapjába, de nyugodtan módosíthatja.

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

### Költészet

A felhasználó kiválaszthatja, hogy a tabulátorral behúzott szöveg vers vagy kód legyen. Az egyetlen különbség az, hogy a pre/code blokkok stílusosabbak, hm, költőibbek, ha a költői módot választjuk. A "költészet" osztályt alkalmazzák a törzscímkére.

Legyen olyan kreatív a formázással, amennyit csak akar, de itt van egy alaprészlet:

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

## Különleges esetek

A táblázatokat, az ábrákat/ábrafeliratokat, valamint a `a.footnote` és `div.footnotes>a` speciális esetét is figyelembe kell venni. Nincsenek meghatározott szabályok a kezelésükre, de vessen egy pillantást az alapértelmezett stílusokra, hogy megtudja, milyen CSS-szabályokra van szüksége a Markednek.

A szabványos táblázatstílus az összes alapértelmezett stílusban átlátszóságot használ a váltakozó sorokon, hogy lágyan illeszkedjen bármilyen háttérhez. Másolhatja ezeket a stílusokat, vagy a saját útját járhatja, csak győződjön meg arról, hogy stílust alakított ki! Ugyanez az ábra és a képfelirat esetében; adjon hozzá egy képet a dokumentumhoz alternatív szöveggel, hogy megtudja, hogyan fog kijönni a jelölés és a megfelelő stílus.

A dokumentumban található lábjegyzetek hivatkozást jelenítenek meg a tartalomban (a.footnote), a végén pedig egy div-t a hivatkozott szöveggel (div.footnotes). Ismét lásd az alapértelmezett stílusokat referenciaként. A lábjegyzet hivatkozási számot tartalmazó sorok sormagasságának megváltoztatásának elkerülése érdekében feltétlenül szerepeltessen valami ilyesmit:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Ha a visszatérő nyilat ugyanabban a sorban szeretné tartani, tegye a következőket:

```css
.footnotes p {display:inline}
```

Az is jó ötlet, hogy minden képre általános szabályt írjon be, hogy az oldal szélességén belül maradjon. Valami ilyesmi:

```css
#wrapper img { max-width: 100% }
```

Ha a témája további kitöltést vagy rögzített szélességet tartalmaz, módosítsa a maximális szélességet, hogy illeszkedjen.

## Nyomtatási stílusok

Ügyeljen arra, hogy olyan nyomtatási stílusokat adjon meg, amelyek eltávolítják a háttérszíneket, a rögzített görgetést és a csak előnézeti felhasználói felületet. A Marked két módot kínál a nyomtatási és a PDF kimenet célzására.

### `@media print`

A szabványos CSS-nyomtatási szabályok érvényesek, ha Markedből nyomtat, vagy ha a PDF-exportálás nyomtatott médiát használ:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### A `.mkprinting` osztály

Amikor a Marked előkészít egy dokumentumot **PDF-exportáláshoz** vagy **Nyomtatás/PDF-előnézethez** ({% kbd cmd P %}), hozzáadja a `mkprinting` osztályt a `<body>` címkéhez (az exportosztályok, például a `bandw`, `breakAfterTOC` és az Ön stílusának `mkstyle--*` osztálya mellett). A Marked beépített témái ezt az osztályt használják a legtöbb nyomtatásspecifikus szabályhoz, ahelyett, hogy egyedül a `@media print`-re hagyatkoznának.

A PDF-exportálás gyakran betölti a rejtett renderelő WebView-t **képernyő** adathordozóval (különösen az egyéni stílusok és a [Fountain](Fountain_for_Screenwriters.html) dokumentumok esetében), így előfordulhat, hogy a stíluslap `@media print` blokkjai **nem** vonatkoznak a PDF kimenetre. A `.mkprinting` előtaggal ellátott szabályok mindig érvényesek az exportálás során, mivel ezek közönséges osztályválasztók, nem médialekérdezések.

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

Azon stílusok esetében, amelyeknek működniük kell **mind** böngészőnyomtatásban és megjelölt PDF-exportálásban, duplikálja meg a kritikus szabályokat, vagy kombinálja a kijelölőket:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

Egyedi nyomtatási CSS hibakereséskor nyissa meg a Nyomtatás/PDF előnézetet, vagy exportálja PDF-be, majd használja a [Safari Web Inspector] (#webkitinspector) alkalmazást a dokumentum ellenőrzéséhez --- a `<body>` `mkprinting` osztályú lesz, amíg a nyomtatási elrendezés aktív.

A nyomtatási hivatkozások elrejtését a fő témán kívül kezelik, így a felhasználók választhatják, hogy a hivatkozások kiemelése és aláhúzása legyen elrejtve a nyomtatásban. Mindaddig, amíg be van állítva egy alapstílus a szöveghez, nem kell aggódnia emiatt.

Szóval, csináld. Alakítsa át blogtémáját, hozzon létre lenyűgöző nyomtatási stílust a PDF-dokumentumokhoz, vagy készítsen tökéletes előnézetet az írási stílushoz. Ha valami fantasztikusat készítesz, tudasd velem, és közzéteszem az egész Megjelölt közösség számára.

## További CSS-beállítások

A {% prefspane Style %} részben további CSS-eket szerkeszthet. Ezek a stílusok minden betöltött témához hozzá lesznek fűzve, és használhatók az összes téma univerzális módosítására.

A [nagy specifikusság] (#overridingspecificity), a `@media` nyomtatási és képernyős lekérdezések, valamint a `.mkprinting` PDF-exportálási választókkal szinte minden stílust vezérelhet egy kis CSS-ismerettel.

## WebKit Inspector

A Safari Web Inspector segítségével láthatja a legegyszerűbben, hogy pontosan mit hoz létre a HTML és CSS Marked, és élőben kísérletezhet az egyéni stílusokkal.

### A Fejlesztés menü engedélyezése a Safariban

1. Nyissa meg a Safarit, és válassza a {% appmenu Safari, Settings… %} lehetőséget.
2. Válassza a **Speciális** lapot.
3. Engedélyezze a **Funkciók megjelenítése webfejlesztőknek** (vagy **Régebbi macOS-verziók esetén a **Fejlesztés menü megjelenítése a menüsorban**) beállítást.

Ha engedélyezve van, egy **Fejlesztés** menü jelenik meg a Safari menüsorában.

![Safari Develop menü a megjelölt dokumentumokat megjelenítve][fejlesztési menü]

### Megjelölt dokumentum vizsgálata

1. A Megjelölt alkalmazásban megnyílt előnézeti ablakban váltson át Safarira.
2. A menüsorban válassza a **Fejlesztés → _\<az Ön Mac-nevének\>_ → Megjelölve → _\<dokumentum címe\>_** lehetőséget.
3. A Safari megnyit egy Web Inspector ablakot a kiválasztott Megjelölt előnézethez csatolva.

Innen a következőket teheti:

- Az **Elements** lapon ellenőrizze a `#wrapper` div-ben lévő DOM-ot, és nézze meg, hogy mely CSS-szabályok vannak alkalmazva.
- Mutasson rá az elemekre a DOM-fában, hogy kiemelje őket a Megjelölt ablakban.
- Használja a **Stílusok** oldalsávot a szabályok éles módosításához, majd másolja vissza a működő kódrészleteket egyéni stílusba vagy **További CSS-be**.
    - Miután szerkesztette a CSS-t az Elemek lapon, a Módosítások lap kiválasztásával összefoglalót kaphat a módosításokról

	![Változások][css-módosítások]
- Használja a **Konzol** lapot a JavaScript futtatásához az élő előnézetben. A teljes [Marked JavaScript API](https://markedapp.com/help/jsapi/) elérhető ezen a konzolon.
- Fedezzen fel más lapokat, például a **Hálózat** lehetőséget a dokumentum által betöltött erőforrások hibakeresése során.

![Megjelölt előnézet ellenőrzése a Safari Web Inspector segítségével][ellenőrzés]

## Egyéni CSS megosztása

Az {% appmenu Style, Share a Custom Style %} gombbal nyissa meg a megosztó alkalmazást a webböngészőben. Húzza a CSS-t az ejtőzónába (vagy kattintson a lemezről való kiválasztásához), és töltse fel a CSS-t az egyéni stílusához.

A megosztott stílusokat a fejlesztőnek jóvá kell hagynia ahhoz, hogy megjelenjenek a galériában, így nem fog azonnali eredményeket látni.

## Egyéb tippek

### A sajátosság felülbírálása

A Megjelölt előnézetben az aktuális stílus fájlnevén alapuló törzsosztály kerül hozzáadásra. Ha az előnézet beállítása „Svájci”, akkor a `<body>` címkén lesz egy `mkstyle--swiss` nevű osztály. Ha egyéni CSS-je MyCustom.css, akkor a törzsosztály `mkstyle--mycustom` lesz. Használhatja ezt az alapstílusokban meghatározott szabályok előtt, hogy felülbírálja azokat. A szabály abszolút pontosságának eléréséhez használja a #wrapper azonosítót is a tároló div részéből:

	.mkstyle--egyéni #wrapper p+p { ... }

### Tartalomjegyzék stílus

Ha a `<!--toc-->` tokent használja a [tartalomjegyzék beszúrásához](Special_Syntax.html#tableofcontents), felülírhatja a tartalomjegyzék szintjelzőinek beállításait egyéni stílusban a „#wrapper” használatával a pontosság növelése érdekében:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Ez azt eredményezi, hogy a tartalomjegyzékben szereplő összes listaelem négyzet alakú felsorolásjelet használna a Beállításokban meghatározottak helyett, amikor az egyéni stílus aktív.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px