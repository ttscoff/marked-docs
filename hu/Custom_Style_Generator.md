<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Custom Style Generator egy webalapú eszköz, amely lehetővé teszi egyéni stílusok létrehozását a Marked számára anélkül, hogy kézzel írna CSS-t. Vizuális felületet biztosít a tipográfia, a színek, a térköz és egyebek vezérlőivel, élő előnézettel, amely a változtatások során frissül.

## Hozzáférés a generátorhoz [accessing-the-generator]

A Stílusgenerátor a következő címen érhető el: [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). Használhatja közvetlenül a webböngészőjében – nincs szükség telepítésre.

![Style Generator][img-style-generator]

  [img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Első lépések [getting-started]

Amikor először nyitja meg a generátort, a következőket fogja látni:

- **Előnézeti ablaktábla** (balra): Stílusának élő előnézete a mintaleértékelési tartalomra
- **Vezérlőpanel** (jobbra): Az összes stílusvezérlő szakaszokba rendezve
- **Eszköztár** (fent): Stíluscím, alaptéma-választó és CSS-importálási lehetőség

### Alaptéma kiválasztása [choosing-a-base-theme]

Kezdje azzal, hogy a legördülő menüből válassza ki az **Alaptémát**. Ez alapot ad a stílusodhoz – ezután személyre szabhatod annak minden aspektusát. A népszerű lehetőségek közé tartozik az Üres (a nulláról kezdéshez), az Alapértelmezett és a különböző beépített témák.

### Meglévő CSS importálása [importing-existing-css]

Ha rendelkezik egy meglévő CSS-fájllal, amelyet kiindulási pontként szeretne használni, kattintson a **CSS importálása** lehetőségre, és válassza ki a fájlt. A generátor betölti ezeket a stílusokat, majd a vezérlők segítségével módosíthatja őket.

## Stílusvezérlők [style-controls]

A generátor logikai szakaszokba rendezi a vezérlőket:

### Alap tipográfia [base-typography]

Az alapvető tipográfiai beállítások vezérlése:

- **Ritmus használata**: Ha engedélyezve van, matematikai tipográfiai skálát használ a következetes címsorméretek és térközök érdekében
- **Alapbetűméret**: A gyökér betűméret (általában 16 képpont)
- **Sormagasság**: A szövegsorok közötti térköz
- **Scale Ratio**: A tipográfiai léptékhez használt arány (a címsorméretekre vonatkozik)

### Elrendezés [layout]

A távolság és a behúzás beállítása:

- **Wapper Padding**: Tér a tartalomterület körül
- **Bekezdés behúzása**: Az első sor behúzása a bekezdésekhez
- **Lista behúzás**: Behúzás a listákhoz
- **Blockquote Behúzás**: Bal margó az idézőjelekhez

### Betűtípusok [fonts]

Betűtípus-családok és súlyok beállítása:

- **Fejléc betűtípusok**: A címsorok betűtípusainak vesszővel elválasztott listája (pl. "Georgia, serif")
- **Body Fonts**: A törzsszöveg betűtípusainak vesszővel elválasztott listája
- **Fejléc súlya**: A címsorok betűmérete (100–900)
- **Body Weight**: Betűtömeg a törzsszövegnél
- **Bold Weight**: Betűsúly a félkövér szöveghez
- **Betűköz**: Karaktertávolság a fejlécekhez és a törzsszöveghez

### Google Fonts [google-fonts]

Adja hozzá stílusához a Google betűtípusokat:

1. Írjon be egy betűtípusnevet a keresőmezőbe (az automatikus kiegészítésre vonatkozó javaslatok jelennek meg)
2. Opcionálisan adjon meg stílusokat (pl. "400,400i,700" normál, dőlt, félkövér)
3. Kattintson a **Hozzáadás** gombra a felvételhez
4. A **Tallózás a Google betűtípusok között** segítségével tekintse meg a teljes katalógust előnézetekkel

A hozzáadott betűtípusok a vezérlőelemek alatti listában jelennek meg – kattintson a × gombra az eltávolításukhoz.

### Színek [colors]

Állítsa be a színeket a különböző elemekhez:

- **Háttér**: Az oldal háttérszíne
- **Alapszöveg**: Alapértelmezett szövegszín
- **Fejléc színe**: Minden címsor színe (címsorszintenként felülbírálható)
- **Body Color**: Törzsszöveg színe
- **Link színe**: A hivatkozások színe
- **Kiemelési szín**: A hangsúlyos szöveg színe (`<em>`)
- **Erős szín**: Szín erős szöveghez (`<strong>`)
- **Háttér megjelölése**: A kiemelt szöveg háttérszíne (`<mark>`)

Az egyes fejlécszínek (H1–H6) külön beállíthatók – a **Reset** segítségével törölheti a felülírást, és visszatérhet a fejlécszínhez.

### Sötét mód [dark-mode]

Kapcsolja be a **Sötét mód** lehetőséget a sötét mód színeinek előnézetéhez és konfigurálásához. Ha engedélyezve van, külön színvezérlők jelennek meg a sötét mód változataihoz. A sötét mód stílusai akkor érvényesek, ha a `.inverted` be van állítva a törzselemen a Megjelölve.

A **Színek létrehozása** használatával automatikusan létrehozhat egy sötét mód palettát a világos mód színei alapján.

### Képek [images]

Kép megjelenésének szabályozása:

- **Maximális szélesség**: A képek maximális szélessége (pl. "100%", "800 képpont")
- **Határ sugara**: Lekerekített sarkok (pl. "8px", "0")
- **Igazítás**: Dokumentum alapértelmezett, Balra, Középre vagy Jobbra

### Idézetblokk [blockquotes]

Stílus blokk idézetek:

- **Bal szegély szélessége**: A bal szegély vastagsága
- **Bal szegély színe**: A bal szegély színe
- **Háttérszín**: Háttérszín az idézőjelekhez
- **Betűstílus**: Normál vagy Dőlt
- **Bal margó**: Térköz a bal széltől
- **Beágyazott bal margó**: Szóköz a beágyazott idézőjelekhez (lehet "örökölni")

Külön vezérlők állnak rendelkezésre a sötét módú blokk idézőjelekhez.

### Listák [lists]

A lista megjelenésének konfigurálása:

- **Listastílus pozíció**: belül vagy kívül (ahol a felsorolásjelek/számok jelennek meg)
- **Bal margó**: Térköz a bal széltől
- **Beágyazott bal margó**: A beágyazott listák szóközei (lehet "örökölni")

### Definíciós listák [definition-lists]

Stílusdefiníciós listák (`<dl>`, `<dt>`, `<dd>`):

- **DL behúzás**: Teljes behúzás
- **DT** (kifejezés) beállítások: Betűméret, súly és stílus
- **DD** (definíció) beállítások: Betűméret, súly, stílus és behúzás

### Táblázatok [tables]

Átfogó asztalstílus:

- **Háttérszín**: Asztali háttér
- **Szegély színe**: A cellák szegélyének színe
- **Táblázatszöveg színe**: Alapértelmezett szövegszín a táblázatokban
- **Változó sorok/oszlopok**: Engedélyezze a zebracsíkozást egyéni színekkel
- **Szegély**: A táblázat körvonalának megjelenítése/elrejtése
- **Rács**: Belső rácsvonalak megjelenítése/elrejtése
- **Igazítás**: Balra vagy Középre
- **Határsugár**: Lekerekített sarkok
- **Maximális szélesség**: Maximális asztalszélesség
- **Cellakitöltés**: Belső térköz
- **Fejléc** beállítások: Betűsúly, méret és stílus
- **Feliratok** beállításai: Betűsúly, méret, stílus és szövegszín

Külön vezérlők állnak rendelkezésre a sötét módú táblázatokhoz.

### Kódblokkok [code-blocks]

Stíluskód blokkok és soron belüli kód:

- **Kód betűtípuscsalád**: Monospace betűkészlet
- **Háttér**: Háttérszín
- **Border Color**: Szegély színe
- **Határsugár**: Lekerekített sarkok
- **Csomagolási mód**: nincs becsomagolás (elő), Preserve + wrap (előcsomagolás) vagy Normál (csomagolás)
- **Kód kitöltése**: Belső térköz

A sötét mód kódblokkjaihoz külön vezérlők állnak rendelkezésre.

### Lábjegyzetek [footnotes]

Stílus lábjegyzetek:

- **Jelölő színe**: A lábjegyzetjelzők színe
- **Szöveg színe**: A lábjegyzet szövegének színe
- **Szöveg betűtípusa**: Normál vagy Dőlt

A sötét mód lábjegyzeteihez külön vezérlők állnak rendelkezésre.

### Vető árnyék [drop-shadow]

Vethető árnyékok hozzáadása az elemekhez:

1. Válassza az árnyék **Erőssége** lehetőséget: Lágy, Közepes vagy Erős
2. Válassza ki, mely elemekre kíván árnyékot alkalmazni:
   - Képek
   - Kódblokkok
   - Blokkidézetek
   - Asztalok

## Egyéni CSS [custom-css]

A rendelkezésre álló vezérlőkön túlmutató speciális testreszabáshoz használja az **Egyéni CSS** gombot a kódszerkesztő megnyitásához. Az itt hozzáadott minden CSS hozzá lesz fűzve a generált stílushoz, és automatikusan a Marked dokumentumstruktúrájában működik.

A szerkesztő tartalmazza a szintaxis kiemelését és érvényesítését – az érvénytelen CSS-t hibaüzenetekkel jelzi.

## Élő előnézet [live-preview]

Az előnézeti panelen látható a mintaleértékelési tartalomra alkalmazott stílus, beleértve:

- Címsorok (H1–H6)
- Bekezdések különféle szövegközi formázással
- Asztalok
- Kódblokkok
- Képek
- Listák (rendezett és nem rendezett)
- Blokkidézetek
- Definíciós listák
- Lábjegyzetek
- Feladatlisták

A változások valós időben frissülnek, ahogy módosítja a vezérlőket.

## Mentés és megosztás [saving-and-sharing]

Ha elégedett a stílusával, több lehetőség közül választhat:

### CSS megtekintése [view-css]

Kattintson a **CSS megtekintése** lehetőségre a teljes generált CSS megtekintéséhez egy előugró ablakban. Mentés előtt átmásolhatja a vágólapra, vagy átnézheti.

### CSS mentése [save-css]

Kattintson a **CSS mentése** lehetőségre stílusának CSS-fájlként való letöltéséhez. A letöltés előtt meg kell adnia a metaadatokat (cím, szerző, leírás).

### Hozzáadás a megjelöltekhez [add-to-marked]

Kattintson a **Hozzáadás a megjelölthez** lehetőségre, hogy közvetlenül hozzáadja a stílust a Megjelölt telepítéshez. Ehhez a Markednek futnia kell, és megnyílik egy párbeszédpanel a stílusnév és a szerzői adatok megerősítéséhez.

### Stílus megosztása [share-style]

Kattintson a **Stílus megosztása** lehetőségre, hogy közzétegye stílusát a [Marked Style Gallery](https://markedapp.com/styles) oldalon, hogy mások is használhatják. A következőket kell megadnia:

- Stílus címe
- A neved
- Szerző URL (nem kötelező)
- Leírás
- Megjegyzés (opcionális)

A stílus előnézete megjelenik a megosztási párbeszédpanelen a közzététel előtt.

## Metaadatok [metadata]

Használja a metaadatok szakaszt (a stílus címe melletti nyílgombbal bővíthető) a következők beállításához:

- **Szerző**: Az Ön neve (a munkamenetek során is megmarad)
- **Szerző URL**: Webhelyének vagy profiljának URL-je
- **Leírás**: A stílus leírása
- **Megjegyzés**: További megjegyzések (nem szerepelnek a megosztott stílusokban)

Ezeket a metaadatokat a CSS-fájl fejléce tartalmazza, és stílusok megosztásához használják.

## Tippek [tips]

- Kezdje a kívánthoz közeli alaptémával, majd szabja személyre
- Használja az **Üres** témát, ha teljes irányítást szeretne a semmiből
- Engedélyezze a **Rhythm** funkciót a matematikailag következetes tipográfia érdekében
- Tesztelje stílusát a **Sötét mód** kapcsolóval, ha támogatni kívánja
- Használja takarékosan az **Egyéni CSS-t** – a legtöbb igény kielégíthető a beépített vezérlőkkel
- Megosztás előtt tekintse meg stílusát különféle tartalomtípusokkal

## Böngésző kompatibilitás [browser-compatibility]

A Style Generator a modern böngészőkben (Chrome, Firefox, Safari, Edge) működik a legjobban. A JavaScript engedélyezése szükséges.