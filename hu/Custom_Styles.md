# <%= @title %>

Tekintse meg dokumentumait *az Ön* stílusában.

## Egyéni stílusok használata [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Az egyéni stílusok felfedezésének legegyszerűbb módja az
[Egyéni stílusgaléria][2]. Itt böngészhet az elérhető stílusok
között működés közben, egyetlen kattintással telepítheti őket,
sőt akár [beküldheti saját alkotásait][6] is, hogy bekerüljenek
a gyűjteménybe.

Ahhoz, hogy saját meghajtójáról egyéni stíluslapokat adjon a
Markedhez, használja a {% prefspane Style %}. Az új stílusok bekerülnek a
Window (Ablak) beállítások és az egyes ablakok legördülő
menüibe, és a hozzáadott CSS-fájl alap fájlnevéről kapják a
nevüket. A saját CSS-fájljait tárolja a meghajtó egy biztonságos
helyén. Ha később áthelyezi őket, a Marked eltávolítja azokat
mindaddig, amíg újra hozzá nem adja őket az új helyükről. Érdemes
bezárni a nyitott dokumentumokat, és eltávolítani a stílust a
Beállításokból, mielőtt törölne vagy átnevezne egy Marked által
használt CSS-fájlt. Ha ezt elmulasztja, semmi nem törik el tőle,
de elkerülhető vele némi zavar.

Egyéni stílusokat a Stíluskezelőn keresztül, a Hozzáadás gombbal,
vagy egy vagy több CSS-fájl Beállítások panelre húzásával adhat
hozzá.

## Stílusok kezelése a Stíluskezelővel [managing-styles-with-the-style-manager]

A Stíluskezelő megnyitásával egyetlen helyen gondozhatja az összes
beépített és egyéni témát. Kattintson a **Stílusok kezelése…**
gombra a {% prefspane Style %} panelen, vagy egyszerűen húzzon CSS-fájlokat a
beállítások ablakára — a Marked importálja őket, megnyitja a
Stíluskezelőt, és kijelöli az újonnan hozzáadott sort. A CSS-fájlok
közvetlenül a Stíluskezelő ablakára húzása is működik; ha több
fájlt húz egyszerre, az átfedő felirat "N egyéni stílus hozzáadása"
szövegre változik, hogy egyértelmű legyen: köteges importálás
történik.

![][img-style-manager]

A Stíluskezelőn belül egy rendezhető táblázatot talál, amely a
beépített és az egyéni stílusokat együtt jeleníti meg. Minden sor
a következőket kínálja:

- Egy **Engedélyezve** jelölőnégyzet, amely azonnal hozzáadja vagy
  eltávolítja a stílust a Stílus menüből, az Alapértelmezett stílus
  felugró menüből és a billentyűparancsokból. Ha letiltja az éppen
  aktív stílust, a Marked automatikusan a következő elérhető
  bejegyzésre vált.
- Egy **Név** oszlop, amelyet a helyszínen szerkeszthet; a
  változtatások megmaradnak, és minden menüben érvényesülnek.
  Kattintson a stílus nevére a helyszíni szerkesztéshez.
- Egy **Forrás** oszlop, amely megjelöli, hogy a stílus Beépített,
  Egyéni vagy Duplikált.
- Egy **Műveletek** gombcsoport a **Szerkesztés** (megnyitja a
  CSS-fájlt a szerkesztőjében), a **Duplikálás** (másolatot és új
  CSS-fájlt hoz létre a lemezen), a **Megjelenítés** (megmutatja a
  fájlt a Finderben) és a **Törlés** (a hivatkozás eltávolításának
  vagy a CSS-fájl Kukába helyezésének lehetőségével) gombokkal.

A sorok fogd és vidd módszerrel átrendezhetők, és a sorrend
határozza meg a Stílus menüt, valamint a `⌘/#` billentyűparancs-
hozzárendeléseket is, így a stílusokat szó szerint a kívánt
helyekre húzhatja. Külső CSS-fájlokat is húzhat konkrét pozíciókba;
az ejtési jelző mutatja, hova kerül majd az új stílus.

### Élő előnézet [live-preview]

A jobb oldali panel egy előnézetet tartalmaz, amely a kiválasztott
stílust egy teljes HTML-dokumentumban jeleníti meg, benne a
címsorok, listák, táblázatok, kódblokkok stb. átfogó gyűjteményével.
Az előnézet a lemezen lévő tényleges CSS-t használja, így a külső
szerkesztőjében végzett módosítások azonnal megjelennek. Egy
jelölőnégyzettel be- és kikapcsolható a Sötét mód előnézete.

További stílusokat találhat (vagy mintaként használhatja saját
stílusai elkészítéséhez) a [GitHubon][1] (lásd a [példákat][2] egy
gyors betekintésért). Részletekért és tippekért lásd az
[Egyéni CSS létrehozása][3] című részt.

## További CSS [additional-css]

A {% prefspane Style %} alatt talál egy További CSS nevű beállítást, "CSS
szerkesztése" feliratú gombbal. A gombra kattintva egy ablak
nyílik meg, ahol univerzális CSS-szabályokat adhat hozzá, amelyek
minden stílusra alkalmazásra kerülnek. Vegye figyelembe, hogy a
szabályok specificitása fontos lehet, amikor a Marked
alapértelmezett stílusainak egy részét felülírja. A dokumentum
törzse egy "#wrapper" azonosítójú div-be van csomagolva. Ha egy
szelektor elé ezt teszi, könnyebben felülírhatja a stílusokat,
például:

    #wrapper img { width: 100%; height: auto; }

Az ebben a mezőben lévő CSS **hozzáfűződik az aktív témához**. Ez
nem helyettesíti a teljes egyéni stílust: a kizárólag ehhez a
mezőhöz írt stíluslap szándékosan hiányos, és ha témaként töltené
be a Stíluskezelőn keresztül, minden, amit nem fed le, formázatlan
maradna.

A Marked **átírja** a További CSS szelektorait beillesztés előtt.
A vezető body-osztályok, mint például a `.mkprinting`, a `body`-ra
kerülnek egyesítésre, nem pedig a `#wrapper` alá ágyazva, ezért az
ebben a mezőben lévő nyomtatási szabályoknak a `body.mkprinting #wrapper …` formát kell
használniuk (a teljes átírási szabályokért lásd az [Egyéni CSS
létrehozása](Writing_Custom_CSS.html#additional-css-settings)
című részt). A mezőnek nincs mérethatára vagy érvényességi
ellenőrzése — az érvénytelen CSS egyszerűen nem fejt ki hatást.

Az ebben a mezőben lévő CSS minden dokumentumra alkalmazásra
kerül, függetlenül attól, hogy melyik stílust használja — beleértve
a HTML-exportot is, ha a stílusok be vannak vonva. Ha feltételekhez
kötött CSS-t szeretne alkalmazni, használja a Stílus beállítása,
CSS-fájl beszúrása vagy CSS beszúrása műveleteket a {% prefspane Processor %}
Egyéni szabályokban.

## Nyomtatás és PDF-exportálás [print-and-pdf-export]

A Marked minden előnézetbe beilleszt egy beépített `@media print`
blokkot (`mkprintstyles`). Ez olyan alapértelmezéseket állít be, mint a
**10pt** alapméret a `html`, `body` és `#wrapper` elemeken (vagy az
**Egyéni betűméret exportáláshoz/nyomtatáshoz** beállításban
megadott méretet, a {% prefspane Export %} panelen, ha ez az opció engedélyezve
van), és a `p { font-size: 1em; }` és `li p { font-size: 1em; }` segítségével normalizálja a
bekezdésszöveget, hogy a csak képernyőn érvényes szabályok, mint a
`p { font-size: 1.1429em; }`, ne növeljék meg a törzsszöveget a PDF-ekben és a
nyomtatott kimenetben.

A PDF-exportálás a generáláshoz használt rejtett WebView-n
**print** vagy **screen** médiatípust használhat. A beépített
témák jellemzően a print médiát használják; az **egyéni stílusok**
és a [Fountain](Fountain_for_Screenwriters.html) dokumentumok
gyakran a screen médiát használják, hogy az elrendezés megegyezzen
az előnézettel. Ez azt jelenti, hogy a `@media print { ... }` szabályok nem
mindig érvényesülnek PDF-exportálás közben.

A megbízható PDF- és Nyomtatás/PDF-előnézet stílusához lássa el a
szelektorokat a `mkprinting` osztállyal, amelyet a Marked exportáláskor
ad hozzá a `<body>`-hoz (lásd az [Egyéni CSS
létrehozása](Writing_Custom_CSS.html#printstyles) című részt a
részletekért és példákért). Egy **egyéni stílus** fájlban
önmagában is használhatja a `.mkprinting`-ot. A **További CSS**
mezőben a body-minősítésű `body.mkprinting #wrapper …` formát használja, mivel ez a
mező átírja a szelektorokat. A két formát kombinálhatja is a
`@media print`-val, ha mindkét útvonalat le kell fednie.

Ha a Marked nyomtatási alapértelmezéseitől eltérő méreteket
szeretne beállítani, adjon hozzá kifejezett szabályokat a saját
CSS-éhez (vagy a További CSS mezőhöz). Használja a `!important`-t,
amikor felül kell írnia a Marked által beillesztett nyomtatási
stílusokat — például:

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

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

A `!important` nélküli szabályok alulmaradhatnak a `mkprintstyles`-ben lévő
későbbi szabályokkal szemben, vagy a stíluslapban lévő más,
minősítés nélküli szelektorokkal szemben, amelyek nyomtatáskor is
érvényesülnek. Ha a csak nyomtatásra vonatkozó finomhangolásokat
a `@media print`-ba és/vagy `.mkprinting` / `body.mkprinting` szabályokba teszi
(nem csak a screen szabályokba), az előnézet és az exportálás
viselkedése könnyebben átlátható marad.

## CSS-változások figyelése [watching-css-changes]

A {% prefspane Style %} Egyéni stílusok részében bejelölhet egy jelölőnégyzetet,
hogy a Marked figyelje az aktív CSS-fájlt a szerkesztett
Markdown-fájl mellett. Amikor bármelyik fájlon változást észlel, az
előnézet frissül. Ez hasznos egyéni stílusok szerkesztéséhez
anélkül, hogy folyamatosan frissítenie kellene, és egyszerű
webfejlesztési feladatokhoz is használható.

Ez néhány alapvető webdesign-munkához és CSS-kísérletezéshez
(például egyéni stílusok készítéséhez) is hasznos. Töltsön be egy
Markdown-fájlt, amely tartalmazza az összes formázást, amelyre
stílust szeretne készíteni, hozzon létre egy egyéni stílust, és
figyelje az előnézetet, ahogy élőben változik szerkesztés közben.

## Egyéni CSS írása [writing-custom-css]

Ha jártas a CSS-ben, saját stíluslapokat is készíthet a Markedhez
való használatra. Részletekért lásd az [Egyéni CSS írása][3] című
részt. Amikor valami újat hoz létre, fontolja meg, hogy [beküldi][6]
a [galériába][2], hogy megoszthassa más felhasználókkal. Ügyeljen
arra, hogy lefedje az útmutatóban felsorolt alapokat, és illessze
be a metaadat-megjegyzést a tetejére.

### Automatikus egyéni stílusok a StyleStealerrel [automatic-custom-styles-with-stylestealer]

Akár automatikusan is generálhat stílust egy létező weboldal
alapján a [Style Stealer][4] segítségével. Ez lehetővé teszi, hogy
betöltsön egy weboldalt, és lekérje a Markdownban előforduló összes
fontosabb elem kiszámított stílusát, majd elmentse egyéni
stílusként.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Az egyéni stílusok kezelése (átnevezés, átrendezés, duplikálás és
törlés) a [Stíluskezelőben](Style_Manager.html) történik.

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
