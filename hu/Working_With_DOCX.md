<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A Marked kiterjedt támogatást nyújt a Microsoft Word fájlokkal való munkavégzéshez. A tipikus munkafolyamat az **előzetes előnézet, majd a DOCX exportálása**: nyissa meg vagy nézze meg a Markdown-t a Marked alkalmazásban, finomítsa a stílusokat és a lektorálást az élő előnézetben, majd exportálja a Wordbe, amikor a dokumentum elkészült.

## DOCX fájlok megnyitása [opening-docx-files]

A Marked képes olvasni egy DOCX-fájlt, és átkonvertálni tisztavá
Markdown. Az érvényes stíluselemek, például a címsorok és a listák
át kell alakítani a Markdown megfelelőjükre.

A változáskövetés és a megjegyzések konvertálásra kerülnek
CriticMarkup. A kiemelések `<mark>` címkévé lesznek konvertálva,
adott esetben színekkel.

## DOCX-fájlok exportálása [exporting-docx-files]

Használja az Exportálás palettát DOCX fájl létrehozásához
Markdown. A mentési párbeszédpanelen megadhat egy beépített
stílusok --- ez a stílus egyszerűen megváltoztatható a Wordben
a témaválasztó megnyitása és egy új téma kiválasztása.

### Fejlécek és láblécek [headers-and-footers]

Ha a {% prefspane Export %}-ben konfigurálja a fejléceket és lábléceket, akkor azok szerepelnek az exportált DOCX-ben. A szabványos helyőrzőket, például a `%title`, `%date`, `%page` és `%total` helyettesíti az exportáláskor. `%logo` és `%image` beágyazza a logót a Fejléc/lábléc beállításokból. A `%md_*` metaadatváltozók a dokumentum MultiMarkdown metaadataiból oldódnak fel. `%h1`--`%h6` Word **STYLEREF** mezőkké válnak, amelyek az exportált címsorstílusokhoz vannak kötve; A Word kitölti őket a dokumentum megnyitásakor. Lásd: [Exportálás](Exporting.html#headers-and-footers) a teljes változólistáért, valamint a DOCX és a nyomtatási/PDF viselkedés közötti különbségekért.

## Nyomon követés módosítása [change-tracking]

A Markdown dokumentumban lévő CriticMarkup szintaxis konvertálva lesz
a Word Change Tracking-re DOCX-be exportálva. Megjegyzések
a következő beillesztések, törlések és helyettesítések
változáskövetéskor a Word jobb oldali oszlopában jelennek meg
engedélyezve van.

Amikor DOCX-fájlt importál a Marked alkalmazásba, módosítja a nyomkövetést
konvertálható CriticMarkup és `<mark>` címkékké mint
megfelelő.

## Matek [math]

A dokumentumban megjelenített MathJax és Katex egyenletek MathML formátumba lesznek konvertálva a Wordben való megjelenítéshez. Ez az átalakítás nem tökéletes, de a legtöbb esetben érvényes matematikai blokkot jelenít meg a Word dokumentumban. Ez csak az exportálásra vonatkozik --- a Word dokumentumokban lévő matematikai blokkok nem konvertálódnak importáláskor.

## Egyéni exportálási stílusok hozzáadása [adding-custom-export-styles]

Felveheti saját exportálási stílusait egy sablon és egy styles.xml fájl hozzáadásával a `~/Library/Application Support/Marked/Custom Word Styles/` helyen. Ezek létrehozásához:

1. Nyisson meg egy Marked-generált DOCX-fájlt a Wordben
2. Szerkessze a stílusokat a Stílusszerkesztőben minden elemhez, és mindegyiknél válassza a "Hozzáadás a sablonhoz" lehetőséget.
3. Mentse el a DOCX fájlt.
4. Hozzon létre egy sablont a felső sáv **Tervezés** részében, és a bal oldali *Sablon* legördülő menüben kattintson a **Jelenlegi sablon mentése** lehetőségre. Nevezze el úgy, ahogyan szeretné, hogy megjelenjen a Megjelölt stílus menüben, és mentse a `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx` helyre, ahol a `STYLENAME` a stílus neve.
5. Nyissa meg a Finder alkalmazást, és keresse meg a Wordből mentett DOCX-fájlt. Másolja le és nevezze át a másolatot a következőre: `FILENAME.zip`, majd kattintson duplán a kicsomagoláshoz.
6. A kicsomagolt dokumentumban egy styles.xml fájlt tartalmazó "word" mappa fog megjelenni. Másolja a styles.xml fájlt ugyanabba a mappába, mint fent, és nevezze el `STYLENAME.xml` (ahol `STYLENAME` a stílus neve). A `.thmx` és `.xml` fájloknak azonos alapnévvel kell rendelkezniük (csak eltérő kiterjesztéssel).

Amikor legközelebb DOCX-et exportál a Marked alkalmazásból, az új stílust a Mentés párbeszédpanel Stílus menüjében fogja látni.