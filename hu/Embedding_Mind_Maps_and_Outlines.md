<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Gondolattérképek és körvonalak beágyazhatók a Markdown előnézetébe a [Markeds include syntax][include] vagy az [IA Writer block syntax][ia] használatával. A viselkedés a fájlformátumtól és a „Térképek beágyazása sellődiagramokként” beállítástól függ a {% prefspane Apps %} alatt a *Mind Maps/Outlines* alatt.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Támogatott formátumok [supported-formats]

### iThoughts X (.itmz) [ithoughts-x-itmz]

Az iThoughts gondolattérkép-fájlok zip-archívumok, amelyek térképadatokat és opcionális előnézeti képet tartalmaznak.

### MindManager (.mmap) [mindmanager-mmap]

A MindManager fájlok zip-archívumok, amelyek a következőt tartalmazzák: `Document.xml`. A kicsomagolt MindManager-csomagok (a `Document.xml`-t tartalmazó mappa) és a `Document.xml`-hez vezető közvetlen elérési út szintén támogatott.

### FreeMind (.mm) [freemind-mm]

A FreeMind gondolattérkép-fájlok az `.mm` kiterjesztést használják, és XML-ként tárolják az adatokat. A Marked úgy érzékeli a FreeMind formátumot, hogy ellenőrzi, hogy a fájl tartalma `<map`-vel kezdődik-e; ha nem (pl. kódrészlet), akkor a fájl egyszerű szövegként szerepel. A FreeMind fájlokat a Mermaid gondolattérkép beágyazása támogatja.

### OPML (.opml) [opml-opml]

Az OPML (Outline Processor Markup Language) egy XML-formátum hierarchikus körvonalakhoz, amelyet széles körben használnak a körvonalazók és a hírfolyam-olvasók. Az iThoughts és más alkalmazások exportálhatnak OPML-be. A megjelölt konvertálások OPML-fájlokat tartalmaztak Mermaid gondolattérkép-diagramokká.

### Kerékpár (.bike) [bike-bike]

`.bike` fájl megnyitása: [Bike](Bike.html). A beillesztett Bike-vázlatok a **Bike outlines** jelölőnégyzetet követik. Be: Mermaid-gondolattérkép (a fájlnév `.bike` nélkül a gyökér). Ki: beágyazott Markdown-lista dokumentumcím nélkül.

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

Lásd: [Tree Outliner](Tree_Outliner.html). A **Tree Outliner outlines** jelölőnégyzet a `.treeoutline` fájl megnyitását és beillesztését is vezérli. Be: Mermaid-gondolattérkép, a dokumentum címével mint gyökérrel. Ki: címsorok és listák; a *Tree Outliner* csoport **Headings through level** beállítása szabja meg, meddig tartanak a címsorok.

## Térképek beágyazása sellődiagramként [embed-maps-as-mermaid-diagrams]

Ha **engedélyezve** (alapértelmezett), a megjelölt konvertálások gondolattérképeket és körvonalakat tartalmaztak [Hableány](https://mermaid.js.org/) diagramokká:

**iThoughts, MindManager, FreeMind, OPML & Bike** – Mermaid gondolattérkép-diagramok formájában renderelt fa elrendezéssel. Az iThoughts és a MindManager esetében az alakinformációk (lekerekített, téglalap, hatszög stb.) megőrződnek, ahol rendelkezésre állnak. A FreeMind (`.mm`) és az OPML ugyanazt a gondolattérkép-formátumot használja. A kerékpáros (`.bike`) körvonalai a mellékelt fájlnevet (mínusz kiterjesztést) használják gondolattérkép gyökércsomópontként. A csomópontcímkék egyszerű szövegesek (a hivatkozások hivatkozásszöveggé válnak; a feladatok ☐ / ☑ előtagként jelennek meg). A Mermaid alapértelmezés szerint minden Markdown előnézetben szerepel.

**Korlátozás:** A gondolattérkép-beágyazás (Hableány diagramok) nem működik a Discount elemzővel. Használja a MultiMarkdown-t, a CommonMark-ot (GFM) vagy a Kramdownt a gondolattérkép-előnézetekhez.

Ha **letiltva**:

- **iThoughts** — Az .itmz fájl beépített előnézeti képe (`preview.png`) base64 képként van beágyazva. A kép alternatív szövege a fájlnevet használja.
- **MindManager** — A vázlat beágyazott Markdown listaként van beágyazva.
- **FreeMind** — A vázlat beágyazott jelölőlistaként van beágyazva.
- **OPML** — A körvonal beágyazott Markdown listaként van beágyazva (nincs gondolattérkép).
- **Kerékpár** — A körvonal beágyazott Markdown listaként van beágyazva (nincs H1); A legfelső szintű címsorelemek H2-vé, a beágyazott címsorok félkövérek, a feladatok pedig GitHub-jelölőnégyzetekké válnak.

## Tartalmazza a szintaxist [include-syntax]

Használja ugyanazt a szintaxist, mint a többi fájl esetében:

	<<[path/to/map.itmz]
	<<[útvonal/map.mmap]
	<<[útvonal/térkép.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]
	<<[path/to/outline.treeoutline]

Vagy iA Writer blokk szintaxissal:

	/path/to/map.itmz

Az elérési utak lehetnek a fő dokumentumhoz képest relatívak vagy abszolútak (`/` vagy `~` karakterekkel kezdve). A részletekért lásd: [Többfájlos dokumentumok](Multi-File_Documents.html).

## OPML konverzió [opml-conversion]

Az OPML-fájlok beágyazott `<outline>` elemeket használnak `text` attribútummal. Ha a „Beágyazás sellődiagramként” engedélyezve van (lásd: [Beállítások: Alkalmazások](Settings_Apps.html)), az átalakítás egy Mermaid gondolattérképet hoz létre, amely ugyanazt a formátumot használja, mint az iThoughts és a MindManager:

- A `<body>` gyermek körvonalai a legfelső szintté válnak (vagy az „Outline” gyökér gyermekei, ha több legfelső szintű elem is van)
- A beágyazott körvonalak határozzák meg a hierarchiát
- A hiányzó vagy üres `text` a következőként jelenik meg: `(unnamed)`
- A szöveg fertőtlenített; különleges karaktereket szöknek meg a Mermaid számára

## Bike átalakítás [bike-conversion]

A Bike `.bike` fájljai HTML-ek, gyökér-`<ul>` elemmel és `<li>` elemekkel. Lista módban minden sor listaelem: a `data-type="heading"` sorok félkövérek, a `data-type="task"` sorok GitHub-jelölőnégyzetek (kész, ha a `data-done` időbélyeget tartalmaz, vagy a `data-checked` / `data-completed` igaz). A csomópont szövegének formázása és hivatkozásai Markdownná alakulnak. Egy `.bike` fájl megnyitása mindig ezt a listát használja. Ha egy beillesztett fájl Mermaid-gondolattérképként ágyazódik be, a fájlnév (kiterjesztés nélkül) az egyetlen gyökércsomópont, a címkék pedig egyszerű szöveg a Mermaid mindmap szintaxisához.
