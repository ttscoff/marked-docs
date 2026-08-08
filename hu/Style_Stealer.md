<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Bármely webhelyről stílusokat nyerhet ki és lophat el.

## Mi az a Style Stealer? [what-is-the-style-stealer]

A Style Stealer egy olyan eszköz, amely lehetővé teszi CSS-stílusok kinyerését bármely webhelyről, és [Custom Styles](Custom_Styles.html)-ként alkalmazza azokat Markdown-dokumentumaira. Tökéletes a következőkhöz:

- **Bloggerek**, akik szeretnének megfelelni kedvenc webhelyeik stílusának
- **Írók**, akiknek olyan dokumentumokat kell létrehozniuk, amelyek megfelelnek egy adott márkának vagy kiadványnak
- **Fejlesztők**, akik gyorsan szeretnének prototípust készíteni a meglévő tervezőrendszerekkel
- **Bárki**, aki meg akarja ragadni bármely jól megtervezett webhely megjelenését és hangulatát

> A Style Stealer attól függ, hogy egy webhely viszonylag jól kidolgozott, világos jelölési felosztásokkal. Nem működik minden webhelyen, de a legtöbben jó munkát kell végeznie.

> A legjobb eredmény érdekében olyan oldalt adjon meg, amely a lehető legtöbb szöveges tartalmat tartalmazza. Ha például stílusokat szeretne kivonni egy blogból, nyissa meg közvetlenül egy cikkhez vagy bejegyzéshez, ne pedig a fő indexoldalhoz.

## A Style Stealer használata [how-to-use-the-style-stealer]

### 1. lépés: Nyissa meg a Style Stealer alkalmazást [step-1-open-the-style-stealer]

A Style Stealer eléréséhez a **Súgó** → **Stíluslopó** menüpontot használja.

### 2. lépés: Írjon be egy URL-t [step-2-enter-a-url]

Az URL mezőbe írja be annak a webhelynek a címét, amelyről stílusokat szeretne kinyerni. A Style Stealer bármely nyilvánosan elérhető weboldallal működik. Ha a webhely fizetőfal mögött található, előfordulhat, hogy be kell jelentkeznie a tartalom kinyeréséhez.

![Style Stealer előnézet][előnézet]

  [előnézet]: images/style-stealer-preview.jpg @2x width=800

### 3. lépés: Betöltés és navigáció [step-3-load-and-navigate]

Kattintson a **Kivonat** gombra, vagy nyomja meg a {% kbd return  %} gombot a webhely betöltéséhez. A betöltés után a következőket teheti:

- **Navigáció** a webhelyen a Command+Click on links billentyűkombinációval
- **Vigye az egérmutatót** a tartalomterületek fölé, hogy kiemelve láthassa őket
- **Kattintson** arra a fő tartalomterületre, amelyből stílusokat szeretne kinyerni

A kiválasztott fő tartalomterület csak címsorokat, bekezdéseket, listákat stb. tartalmazhat. Ne válasszon olyan tartalomterületet, amely menüket, oldalsávokat vagy egyéb idegen tartalmat tartalmaz. A címsor gyakran a szokásos bekezdéstartalomtól különálló tárolóban található. Ilyen esetekben először próbálja meg kiválasztani a legkisebb tárolót, amely mindkettőt tartalmazza. Ha az eredmények rosszak, kattintson ismét a **Kivonat** lehetőségre, és válassza ki újra csak azt a tárolót, amely a bekezdéseket tartalmazza.

### 4. lépés: Stílusok kibontása [step-4-extract-styles]

Ha rákattint a tartalomterületre, az adott területre vonatkozó stílusok kibontásra kerülnek. Az előnézet újra betöltődik egy általános oldallal, amely bemutatja az összes gyakori HTML-elemet, és azt, hogy a kibontott stílusok hogyan vonatkoznak rájuk.

Ezt az egyéni stílust elmentheti egyéni CSS mappájába, hogy bármilyen dokumentumban felhasználhassa. Kattintson a **Mentés** gombra, vagy nyomja meg az {% kbd cmd S %} gombot a mentéshez. A stílus elnevezése a megadott URL domainje alapján történik.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## Amit kivonnak [what-gets-extracted]

A Style Stealer stílusok átfogó készletét rögzíti, beleértve:

### Tipográfia [typography]

- **Betűcsaládok** és méretek minden címsorszinthez (H1-H6)
- **Bekezdés** stílus, beleértve a sormagasságot és a térközt
- **Szövegszínek** és háttérszínek
- **Betűsúlyok** és stílusok (félkövér, dőlt stb.)

### Elrendezés és térköz [layout-and-spacing]

- **Margók és párnázás** minden elemhez
- **Border** stílusok és színek
- **Háttérszínek**, beleértve a test hátterét a sötét témákhoz

### Interaktív elemek [interactive-elements]

- **Linkstílusok**, beleértve a lebegtetést és a meglátogatott állapotokat
- **Gomb** és formaelem-stílus
- **Lista** stílus (jelek, számok, behúzás)

### Különleges szolgáltatások [special-features]

- **Első bekezdés** stílus
- **Blockquote** formázás
- **Kód** és előre formázott szövegstílus
- **Asztal** stílus
- **Egyedi betűtípusok** és webes betűtípusok

## Speciális funkciók [advanced-features]

### Médiablokkolás [media-blocking]

A Style Stealer automatikusan blokkolja a médiatartalmakat (videókat, képeket, hangot), hogy megelőzze az összeomlásokat, és a szövegstílusra összpontosítson. Ez biztosítja a zökkenőmentes kivonási folyamatot még a médiaigényes webhelyeken is.

### Álválasztó támogatás [pseudo-selector-support]

Az eszköz rögzíti a CSS pszeudoválasztókat, például:

- `:hover` állapotok a hivatkozásokhoz és gombokhoz
- `:visited` link állapotok
- `:first-child` bekezdésstílus
- `::first-letter` cseppsapkákhoz

### Intelligens szűrés [smart-filtering]

A Style Stealer intelligensen kiszűri:

- Alapértelmezett böngészőstílusok
- Felesleges szállítói előtagok
- Ellentmondó vagy redundáns szabályok
- Stílusok, amelyek olvashatatlanná teszik a szöveget

### Hibakeresési mód [debug-mode]

A kivonatolási folyamat részletes naplózásához engedélyezze a hibakeresési módot a Style Stealerben. Ez hasznos a hibaelhárításhoz vagy a rögzítésre kerülő stílusok megértéséhez.

## Tippek a legjobb eredményekhez [tips-for-best-results]

### Válassza ki a megfelelő tartalomterületet [choose-the-right-content-area]

- Kattintson az oldal **főtartalmi területére**, ne a fejlécekre, oldalsávokra vagy láblécekre
- Keresse meg azt a területet, amely a cikk szövegét, a blogbejegyzést vagy a fő tartalmat tartalmazza
- Kerülje az erős JavaScript- vagy dinamikus tartalommal rendelkező területeket

### Sötét témák kezelése [handle-dark-themes]

A Style Stealer automatikusan rögzíti a test háttérszíneit, így tökéletes a sötét témastílusok kiemelésére. Az előnézet megmutatja, hogyan néz ki a tartalom a kivont sötét stílussal.

### Betűtípus-megfontolások [font-considerations]

- A **Web betűtípusok** rögzítésre kerülnek, és belekerülnek a kibontott stílusokba
  - A távoli URL-ről (pl. Google Fonts) betöltött betűtípusok megtartják ezt az URL-t. Az adat-URL-ekből betöltött betűtípusok megkettőződnek a generált stíluslapon.
- A **Rendszer-betűkészletek** kecsesen visszaállnak a különböző rendszerekre
- **A betűtípus betöltése** eltarthat egy ideig az előnézetben

### Stílusaid tesztelése [testing-your-styles]

A kibontott stílusok mentése után:

1. Alkalmazza őket egy tesztdokumentumra
2. Ellenőrizze, hogyan néznek ki a tényleges tartalommal
3. Végezze el a beállításokat a következők szerint:
   1. Nyissa meg a {% prefspane Style %}
   2. Válassza ki az új stílust az Egyéni stílusok táblázatban
   3. Kattintson a Felfedés gombra a fájl Finderben való megjelenítéséhez
   4. Nyissa meg a fájlt bármely egyszerű szövegszerkesztőben (a TextEdit egyszerű szöveges módban működik), és végezze el a szükséges módosításokat

## Hibaelhárítás [troubleshooting]

### A webhely nem töltődik be [website-wont-load]

- Ellenőrizze, hogy az URL helyes-e és nyilvánosan elérhető-e
- Egyes webhelyek blokkolhatják az automatikus hozzáférést
- Próbáljon meg egy másik oldalt ugyanazon a webhelyen

### A stílusok másképp néznek ki [styles-look-different]

- A kinyert stílusok az Ön által kiválasztott konkrét tartalomon alapulnak
- Egyes webhelyek összetett CSS-t használnak, amely nem feltétlenül fordítható tökéletesen
- Használjon További CSS-t, vagy szerkessze a stíluslapot a finombeállításokhoz

### Hiányzó stílusok [missing-styles]

- Győződjön meg arról, hogy a fő tartalomterületet választotta, nem pedig az oldalsávot vagy a fejlécet
- Egyes stílusok JavaScripten keresztül alkalmazhatók, és nem kerülnek rögzítésre
- Nézze meg a hibakereső konzolt a részletes kibontási információkért

## Billentyűparancsok [keyboard-shortcuts]

- {% kbd return  %} - URL betöltése kinyeréshez
- {% kbd cmd S %} - Mentse el a kibontott stílust egyéni stílusú CSS-fájlba
- {% kbd cmd  %}-Kattintson - Navigáljon a hivatkozásokon előnézet közben

## Integráció egyéni stílusokkal [integration-with-custom-styles]

A kibontott stílusokat a rendszer az Egyéni CSS mappába menti, és ezek lehetnek:

- **Alkalmazva** bármely dokumentumra a Stílus menün keresztül
- **Módosítva** bármilyen szövegszerkesztővel
- **Megosztva** másokkal a CSS-fájl másolásával
- **Kombinált** más egyedi stílusokkal

A Style Stealer megkönnyíti a gyönyörű stílusok könyvtárának felépítését, amelyet az internet legjobban megtervezett webhelyei ihlettek.