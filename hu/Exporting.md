<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Markdown kész dokumentummá alakítása.

## Exportálás az előnézet után

A Marked előnézete az exportálás alapja --- amit az előnézeti ablakban lát, azt PDF, DOCX, EPUB és más formátumokban kapja meg (modulo export-specifikus beállítások, például margók, fejlécek és oldalszámozás). Először állítsa be a stílust és a lektorálást az előnézetben, majd exportálja, amikor a dokumentum készen áll. A teljes előnézeti munkafolyamatért lásd: [Élő Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html).

## Az exportálási panel [fiók]

![Exportálási panel][exportálási panel]

Az **Export Panel** egy billentyűzet-vezérelt, reflektorfényű panel, amely gyors hozzáférést biztosít az összes exportálási lehetőséghez. Nyissa meg az exportálás ikonra kattintva az állapotsorban vagy a {% kbd shift cmd e %} megnyomásával.

![Export Button][expbut]

Az Exportálás panelen a dokumentumot HTML, egyoldalas PDF, oldalszámozott PDF, RTF-csomagként vagy Microsoft Word DOC- vagy DOCX-fájlként mentheti el. Menthet egy új Markdown-fájlba (a megjelölt-specifikus funkciók megjelennek, és azok eredményei is megjelennek), nyílt dokumentumba (ODT), vagy OPML-ként más alkalmazásokban való használatra.

## HTML másolása

A HTML másolása funkcióval gond nélkül elhelyezheti az előnézet HTML-forráskódját a vágólapra. Kiválaszthatja a fogaskerék menüből, vagy egyszerűen nyomja meg az {% kbd shift cmd C %} gombot. A másolt HTML egy részlet lesz, amely készen áll a blogba, fórumba vagy HTML dokumentumba való beillesztésre.

A másoláshoz nem kell a forrás nézetben lennie. Az előnézetre fókuszálva (kattintson rá), csak írja be a {% kbd shift cmd C %} parancsot, és megjelenik egy felugró üzenet, amely tájékoztatja, hogy a forrás a vágólapon van.

## HTML mentése

![][exporthtmltartozék]



A HTML mentése paranccsal – amely elérhető a fogaskerék menüből vagy egyszerűen a **{% kbd cmd S %}** beírásával – lehetővé teszi a teljes dokumentum mentését megosztásra vagy közzétételre készen.

Opcionálisan felveheti a Marked bármelyik stílusát (vagy az [egyéni stílusok][egyéni] egyikét) az exportálásba, így egy használatra kész dokumentumot kaphat, amely már be van ágyazva a szükséges formázással.

Ezenkívül beágyazhatja a dokumentumban szereplő helyi képeket az exportált HTML-kódba, így önálló dokumentumot készíthet, amelyet bárhol tárolhat anélkül, hogy át kellene vele mozgatnia a képeket. Ez csak a helyi meghajtón relatív vagy abszolút elérési úttal hivatkozott képekkel működik. Kerülje a `file:///` elérési utak használatát, ha használni szeretné ezt a funkciót.

## A Markdown exportálása PDF-be Mac rendszeren

Nyomtatás/PDF előnézet ({% kbd cmd P %}) egy szabványos nyomtatási párbeszédpanelt jelenít meg. A Marked minden előnézeti stílusához saját kísérő nyomtatási stílusok tartoznak, amelyek eltávolítják a hátteret, módosítják a betűméreteket és szegélyeket biztosítanak. Az előnézet az aktuálisan kiválasztott stílus alapján kerül kinyomtatásra.

A nyomtatási párbeszédpanelen jól láthatóak a PDF és az Előnézet gombok. A PDF számos lehetőséget kínál a PDF-be való exportáláshoz (az elérhető alkalmazások alapján), a Preview pedig közvetlenül exportálja a PDF-verziót a Preview.appba, ahol elmentheti vagy elküldheti e-mailben.

Az ezzel a módszerrel végzett PDF formátumba történő nyomtatás során az oldalszámozás is benne lesz. Ha papírra vagy PDF-re nyomtat, az oldaltöréseket manuálisan is beillesztheti a [`<!--BREAK-->` szintaxis][törés] használatával vagy az {% prefspane Export %} opciók beállításával, hogy első és/vagy második szintű fejlécet használjon szakaszelválasztóként.

Előnyben részesítik azt is, hogy a vízszintes szabályokat (`<hr>`) nyomtatáskor oldaltörésekké alakítsák. Ezzel a címke által létrehozott sort oldaltörésre cseréli, és eltávolítja azt a végső kimenetből. Ez a beállítás nincs hatással az előnézetre.

![Nyomtatási margók][margónyomtatás]

Az oldalmargók a {% prefspane Export %}-ban állíthatók be, és hatással vannak a nyomtatási és oldalszámozott PDF kimenetre.

A `Margins:` metaadatkulcs segítségével felülbírálhatja dokumentumonkénti margóbeállításokat. Az értékeket pontként értelmezzük; az egységutótagokat, például a `px`, `pt` és `em` figyelmen kívül hagyja. Használjon két számot a függőleges és vízszintes margókhoz (`10 20`), vagy négy számot a felső, jobb, alsó és bal oldali margókhoz (`10, 20, 10, 20` vagy `10 20 10 20`). A metaadat-margók felülbírálják a {% prefspane Export %} beállításokat.

### Fejlécek és láblécek

A {% prefspane Export %}-ben meghatározott fejlécek és láblécek minden nyomtatott vagy oldalszámozott PDF-be mentett oldal tetején és alján, valamint a DOCX-exportálás során megjelennek. Bármilyen szöveget elhelyezhet a bal felső, felső középső, jobb felső, bal alsó, alsó középső és jobb alsó sarokban. A középső szöveg középre igazítva van az oldalon. A következő változók lecserélődnek a karakterláncokban, ha használják őket:

    %title = Dokumentum címe
    %date = Aktuális dátum
    %time = Jelenlegi idő
    %page = Aktuális oldalszám
    %total = Teljes oldalszám
    %path = Fájlrendszer elérési útja a dokumentumhoz
    %filename = Csak a dokumentum fájlneve
    %basename = Kiterjesztés nélküli fájlnév
    %logo/%image = A Fejléc/lábléc beállításainál a képen beállított logó
    %%(text) = Csak az első oldalon nyomtatandó szöveg
    %h1/h2/h3/h4/h5/h6 = szakaszcímek Markdown fejlécek alapján
    %sep(X) = A szakaszcímek közé elhelyezendő szöveg, ha létezik alszakasz

**Nyomtatott és oldalszámozott PDF** a `%h1`--`%h6` a Marked oldalszámozásával oldja fel, így minden oldal az adott oldalon látható fejléc-hierarchiát mutatja. A `%sep(X)` és a `%md_*` metaadat-változók nyomtatási/PDF-kimenetben is támogatottak.

A **DOCX export** beágyazza a `%logo`/`%image` jelet a Word fejlécébe vagy láblécébe (körülbelül 50 képpont magasra méretezve, a nyomtatási előnézetnek megfelelő). A címsor helyőrzői Word **STYLEREF** mezőkké válnak, amelyek az exportált `Heading 1`--`Heading 6` stílusokra hivatkoznak. A Word frissíti ezeket a mezőket a dokumentum megnyitásakor, a Word saját elrendezése és oldaltörései alapján --- nem a Marked előnézeti oldalszámozása alapján. A `%md_*` metaadat-változók exportáláskor egyszer kerülnek helyettesítésre, ugyanúgy, mint a nyomtatott/PDF-ben. A `%sep(X)` nem konvertálódik DOCX fejlécekbe/láblécekké.

A `%title` a MultiMarkdown Metadata fejlécekben meghatározott "Title:" információkat fog használni, ellenkező esetben a fájlnévre esik vissza a fájl kiterjesztése nélkül. Ha címet szeretne megadni az MMD metaadatok használatával, tegye a következőket a dokumentum első sorába:

    Cím: A dokumentum címe

Kövesse a sort egy üres sorral (vagy bármely más definiálni kívánt metaadattal, amelyet egy üres sor követ).

Bármely MMD-metaadat-kulcsot is használhatja változóként, ha előtagként `%md_`-t tesz, és a kulcs szavait kisbetűs karakterláncként kombinálja. Például, ha a dokumentum tetején metaadatkulcs található, például:

    Funky Monkey: A legfinomabb majom

Ha a `%md_funkymonkey` karaktert használja a fejlécmezőben, a „Legfinomabb majom” bekerül az exportált dokumentumba a fejléc helyére. Az adott kulcsot nem tartalmazó dokumentumok üresen hagyják a mezőt, így a metaadatok alapján szelektíven adhat hozzá fejlécet.

A `%date` és `%time` formátumkódokról lásd a [Dátum- és időformátumok](Exporting.html#dateandtimeformats) részt.

Az „Oldalszámozás eltolása” beállítással beállítható, hogy az oldalszámok melyik számmal kezdõdjenek. Például, ha van egy tartalomjegyzéke az első oldalon, és azt szeretné, hogy a számozás a második oldalon 1. oldalként kezdődjön, állítsa az eltolást -1-re. A 2. oldal mostantól az 1. oldal lesz a fejlécben/láblécben (`%page`), és a teljes oldalszám (`%total`) ennek megfelelően módosul.

A fájl tetején található MMD metaadatok használatával fejléc/lábléc betűtípust is megadhat egy adott dokumentumhoz:

    Fejléc betűtípusa: Mensch

Vegye figyelembe, hogy ha betűtípus-családnevet használ, akkor az alapértelmezett betűtípus kerül kiválasztásra. A betűtípus rendszernevének használatával megadhat egy változatot. Például a Helvetica Neue Ultralight esetében a „Fejléc betűtípusa: HelveticaNeueUltralight” értéket kell használnia.

Ezenkívül megadhat egy dokumentumonkénti fejléc/lábléc betűméretet a metaadatokkal:

    Fejléc betűmérete: 10

### Dátum és idő formátumok

A {% prefspane Export %} **Dátumformátum** és **Időformátum** mezői szabályozzák, hogy a `%date` és a `%time` hogyan jelenjenek meg a fejlécekben és a láblécekben. Mindkét mező strftime stílusú formátumkódokat használ: egy `%`, amelyet egy betű követ. A szó szerinti szöveget (például `-`, `:` vagy szóközöket) a rendszer úgy másolja, ahogy van.

**Példák**

    %m-%d-%Y → 2026-06-20 (A megjelölt alapértelmezett dátumformátuma)
    %I:%M %p → 15:45 (a megjelölt alapértelmezett időformátuma)
    %Y-%m-%d → 2026-06-20
    %B %d, %Y → 2026. június 20
    %a %H:%M → P 15:45

**Általános formátumkódok**

| Kód | Példa | Leírás |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Négy számjegyű év |
| `%y` | 26 | Kétszámjegyű év |
| `%m` | 06 | Hónap (01--12) |
| `%B` | június | A hónap teljes neve |
| `%b` | jún | A hónap rövidített neve |
| `%d` | 20 | A hónap napja (01--31) |
| `%e` | 20 | A hónap napja (szóközzel kitöltve) |
| `%A` | péntek | A hétköznapok teljes neve |
| `%a` | P | A hétköznapok rövidített neve |
| `%H` | 15 | Óra, 24 órás (00--23) |
| `%I` | 03 | Óra, 12 órás (01--12) |
| `%M` | 45 | Perc (00--59) |
| `%S` | 07 | Második (00--59) |
| `%p` | PM | AM vagy PM |
| `%x` | (helyszín) | A nyelv által preferált dátum |
| `%X` | (helyszín) | A nyelv által preferált idő |
| `%c` | (helyszín) | A nyelv által preferált dátum és idő |

A **nyomtatott és oldalszámozott PDF** támogatja a fenti teljes strftime stílust, valamint további kódokat, például `%j` (az év napja), `%U`/`%W` (hétszám), `%z` (időzóna eltolás) és `%Z` (időzóna neve). A teljes referenciaért lásd az [Open Group strftime specifikációt](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html).

A **DOCX export** támogatja a fenti táblázatban felsorolt ​​kódokat. A kevésbé gyakori kódokat figyelmen kívül lehet hagyni, vagy változatlan formában át lehet adni.

A {% prefspane Export %} **Alapértelmezett formátumok visszaállítása** használatával állítsa vissza a `%m-%d-%Y` és `%I:%M %p` értékre.

### Dokumentumonkénti fejlécek és láblécek

A fejléceket és lábléceket dokumentumonként határozhatja meg a dokumentum legtetején található MultiMarkdown metaadatok használatával:

    Fejléc nyomtatása balra: %title
    Nyomtatási fejléc központ: %basename
    Fejléc nyomtatása jobbra: %date
    Lábléc nyomtatása jobbra: %page/%total

Ezek felülírnak minden beállítást a beállításokban. Vegye figyelembe, hogy ha a MultiMarkdowntól eltérő processzort használ, és nem szeretné, hogy a fejlécek megjelenjenek magában a dokumentumban, használhat HTML megjegyzéseket, ügyelve arra, hogy a megjegyzés bezárása előtt hagyjon üres sort:

    <!--
    Fejléc nyomtatása balra: %title
    Nyomtatási fejléc központ: %basename
    Fejléc nyomtatása jobbra: %date

    -->

## PDF mentése

Ezzel a lehetőséggel az előnézetet közvetlenül egy PDF-fájlba menti a meghajtón. A dokumentum teljes egészében, oldaltörések nélkül jelenik meg. Ha lapozást szeretne tartalmazni a kimenetben, használja az [Exportálási panel] (#drawer) Nyomtatás/PDF beállításait.

## RTF exportálási lehetőségek

A Megjelölt RTF (Rich Text Format) adatokat közvetlenül a vágólapra exportálhat. Csak válassza ki a Rich Text másolása parancsot a fogaskerék menüből.

A Megjelölt **RTFD** (Rich Text Format) fájlként is mentheti a fájlt. Az RTFD formátum egy csomagformátum, amely egy RTF fájlt és a dokumentumba ágyazott képeket tartalmaz.

## DOCX export

A DOCX formátumban történő exportálás egy érvényes Microsoft Word dokumentumot hoz létre, amelynek elemei, például címsorok, fejlécek/láblécek, kiemelések, listák stb. érvényes Word-stílusokra vannak leképezve. Ez azt jelenti, hogy könnyedén alkalmazhatja saját témáját a Wordben.

A Word importálásával és exportálásával kapcsolatos további részletekért lásd a [DOCX-feldolgozás][DOCX] részt.

## A Markdown exportálása EPUB-ba

A megjelölt 100%-ban érvényes, 100%-ban hozzáférhető EPUB dokumentumokat exportálhat. Válassza ki az EPUB-exportálás típusát, adja meg a metaadatokat, például a címet, a szerzőt és a dátumot, és opcionálisan adjon hozzá egy borítóképet. A mentett fájl bármely EPUB-nézegetőben olvasható lesz.

Az EPUB-exportáláshoz szükséges metaadatokat magában a fájlban lehet foglalni, legyen szó Markdown-dokumentumról, Scrivener-fájlról (`metadata` oldal) vagy más könyvformátumról. A használható kulcsok a következők:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

A borítókép kulcs tartalmazhat egy, az alapdokumentumhoz viszonyított elérési utat vagy egy abszolút elérési utat. PNG vagy JPG fájlok elfogadhatók.

Ha a cím nincs beállítva, akkor alapértelmezés szerint az eredeti dokumentum fájlneve lesz, ha pedig a szerző nincs beállítva, akkor a macOS-felhasználó teljes neve lesz.

A dátum mindig az aktuális dátumra lesz állítva, és jelenleg nem módosítható metaadatokkal. Mentéskor azonban módosítható, ha a formázás (ISO) érintetlen marad.

### Közzététel az Amazon Kindle-ben (KDP)

Az EPUB egy nyílt formátum, amelyet számos olvasóalkalmazás és üzlet (Apple Books, Kobo és mások) használ, nem csak a Kindle. Ha a [Kindle Direct Publishing (KDP)] (https://kdp.amazon.com/) segítségével tesz közzé közzétételt, exportálja az EPUB-t a Markedből, és töltse fel a fájlt a KDP-be. Az Amazon a saját Kindle kézbesítési formátumára (KFX) alakítja át az olvasók számára.

A KDP számos kéziratformátumot fogad el, beleértve az EPUB-t és a DOCX-et (amelyeket a Marked exportálhat is). A követelményekért lásd az Amazon [támogatott e-könyv-formátumait] (https://kdp.amazon.com/en_US/help/topic/G200634390) és az [e-könyv kézirat-formázási útmutatóját] (https://kdp.amazon.com/en_US/help/topic/G200645680).

**MOBI nem szükséges.** A KDP már nem fogadja el a MOBI-feltöltéseket új címekhez (2025 márciusától kezdve a rögzített elrendezésű könyveket is). A Marked nem exportálja a MOBI-t, és nem kell külön "Kindle" vagy Mobipocket fájl a KDP-hez. Ha az Amazon elrendezési eszközeit részesíti előnyben, a [Kindle Create] (https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT) segítségével is készíthet könyvet, amely KPF-fájlokat állít elő.

Feltöltés előtt érdemes ellenőrizni, hogyan fog kinézni az EPUB a Kindle eszközökön az Amazon ingyenes [Kindle Previewer] (https://kdp.amazon.com/help/topic/G202131170) segítségével. Ez az Amazon opcionális, harmadik féltől származó szoftvere, nem a Marked része.

## Profilok exportálása

Az exportálási profilok lehetővé teszik az exportálási beállítások mentését és gyors váltását. Ez különösen akkor hasznos, ha rendszeresen exportál dokumentumokat különböző célokra – például egy profilt a nyomtatásra kész PDF-ekhez meghatározott margókkal és fejlécekkel, egy másikat pedig a beágyazott stílusokkal rendelkező, webkész HTML-hez.

### Az exportálási profilok használata

A Marked első elindításakor automatikusan létrejön egy „Alapértelmezett” profil az aktuális exportálási beállításokkal. Megtekintheti és kiválaszthatja a profilokat az exportálási párbeszédpaneleken (PDF exportálás, HTML mentés stb.) a párbeszédablak tetején található profil előugró menü segítségével.

**Új profil létrehozása:**

1. Módosítsa az exportálási beállításokat a {% prefspane Export %} vagy bármely exportálási párbeszédpanelen
2. Az exportálási párbeszédpanelen kattintson a profil előugró menüre, és válassza a „Profil hozzáadása…” lehetőséget.
3. Adja meg a profil nevét (pl. "Nyomtatási minőség" vagy "Webes export")
4. Az aktuális beállítások a profilként kerülnek mentésre

**Profil betöltése:**

- Válasszon ki egy profilt a felugró menüből bármely exportálási párbeszédpanelen
- Az összes exportálási beállítás azonnal frissül, hogy megfeleljen a profil mentett értékeinek

**Profil módosításainak mentése:**

- Az exportálási beállítások módosítása után a profil felugró ablak mellett megjelenik a „Mentés” gomb
- Kattintson a "Mentés" gombra, hogy frissítse az aktuális profilt a módosításokkal
- A gomb csak akkor engedélyezett, ha nem mentett módosítások vannak

**Profilok kezelése:**

- Válassza a „Profilok kezelése…” lehetőséget a profil felugró menüből a profilkezelési ablak megnyitásához
- Innen a következőket teheti:
  - **Profilok átnevezése** a névre való dupla kattintással
  - **Másoljon** egy profilt, hogy az alapján újat hozzon létre
  - **Profilok** törlése (az "Alapértelmezett" profil nem törölhető)
  - Az összes elérhető profil megtekintése egy listában

### Mit rögzítenek az exportprofilok

Az exportprofilok mentik az összes exporttal kapcsolatos beállítást, beleértve:

- **PDF beállítások**: Oldalméret, margók, fejlécek/láblécek, betűtípusok, oldaltörések, tartalomjegyzék
- **HTML-exportálás**: stílusbeágyazás, képbeágyazás, szintaktikai kiemelés, matematikai megjelenítés
- **Markdown Processing**: Szöveg tördelése, link formázása, processzorszabályok
- **CriticMarkup**: Exportálási típus és feldolgozási lehetőségek
- **Syntax Highlighting**: Nyelvfelismerési és kiemelési beállítások
- **Math Rendering**: MathJax/KaTeX integráció és egyenletszámozás
- **Képkezelés**: Beágyazási lehetőségek, másolási viselkedés, elérési út beállítások
- **Tipográfia**: Elválasztás, özvegyek/árvák, betűméretek
- **Exportálási viselkedés**: Fájlnév-beállítások, konfliktusfeloldás

A profilok minden exportálási típusban működnek: Markdown, HTML, folyamatos PDF, oldalszámozott PDF, EPUB, DOCX, ODT, TextBundle, RTF és OPML.

### Profil tárolása

A profilokat az Alkalmazástámogatás mappája tárolja a következő címen:

    ~/Library/Application Support/Marked/ExportProfiles.plist

Ez azt jelenti, hogy profiljai akkor is megmaradnak, ha visszaállítja az alkalmazásbeállításokat, és túlélik az alkalmazásfrissítéseket. A fájlról biztonsági másolatot készíthet, hogy megőrizze profiljait a telepítések során.

### Tippek az exportprofilok használatához

- **Hozzon létre profilokat a gyakori munkafolyamatokhoz**: Ha rendszeresen exportál nyomtatott vagy webes célra, hozzon létre külön profilt mindegyikhez.
- **Használjon leíró neveket**: A profilnevek, például „Nyomtatás – Levél” vagy „Web – Beágyazott stílusok” egyértelművé teszik, hogy az egyes profilok mire valók
- **Gyakori mentés**: A "Mentés" gomb mindig megjelenik, amikor változtatásokat hajt végre – kattintson rá a módosítások megőrzéséhez.
- **Kezdje a meglévő profilokból**: Használja a "Duplikálás" lehetőséget a kezelőablakban meglévő profilok változatainak létrehozásához, ahelyett, hogy a nulláról kezdené.

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_with_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center