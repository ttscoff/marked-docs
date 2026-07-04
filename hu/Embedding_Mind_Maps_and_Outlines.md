<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Gondolattérképek és körvonalak beágyazhatók a Markdown előnézetébe a [Markeds include syntax][include] vagy az [IA Writer block syntax][ia] használatával. A viselkedés a fájlformátumtól és a „Térképek beágyazása sellődiagramokként” beállítástól függ a {% prefspane Apps %} alatt a *Mind Maps/Outlines* alatt.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Támogatott formátumok

### iThoughts X (.itmz)

Az iThoughts gondolattérkép-fájlok zip-archívumok, amelyek térképadatokat és opcionális előnézeti képet tartalmaznak.

### MindManager (.mmap)

A MindManager fájlok zip-archívumok, amelyek a következőt tartalmazzák: `Document.xml`. A kicsomagolt MindManager-csomagok (a `Document.xml`-t tartalmazó mappa) és a `Document.xml`-hez vezető közvetlen elérési út szintén támogatott.

### FreeMind (.mm)

A FreeMind gondolattérkép-fájlok az `.mm` kiterjesztést használják, és XML-ként tárolják az adatokat. A Marked úgy érzékeli a FreeMind formátumot, hogy ellenőrzi, hogy a fájl tartalma `<map`-vel kezdődik-e; ha nem (pl. kódrészlet), akkor a fájl egyszerű szövegként szerepel. A FreeMind fájlokat a Mermaid gondolattérkép beágyazása támogatja.

### OPML (.opml)

Az OPML (Outline Processor Markup Language) egy XML-formátum hierarchikus körvonalakhoz, amelyet széles körben használnak a körvonalazók és a hírfolyam-olvasók. Az iThoughts és más alkalmazások exportálhatnak OPML-be. A megjelölt konvertálások OPML-fájlokat tartalmaztak Mermaid gondolattérkép-diagramokká.

### Kerékpár (.bike)

A Bike.app körvonalait a rendszer védett HTML-fájlokként tárolja (`.bike`). A `.bike` fájlt közvetlenül a Marked alkalmazásban nyithatja meg: a dokumentum Markdownként jelenik meg, a fájlnévvel (mínusz kiterjesztéssel) a fő fejlécként (H1), a legfelső szintű címsorelemeket H2ként, a beágyazott címsorokat félkövér listaelemként, a feladatokat pedig GitHub-stílusú jelölőnégyzetként. Ha egy `.bike` fájl szerepel az include szintaxison keresztül, a Bike „Beágyazás sellődiagramként” beállítása (az Alkalmazások → Mind Maps/Outlines részben) szabályozza, hogy Mermaid gondolattérkép legyen (a fájlnév gyökércsomópontként) vagy beágyazott Markdown lista (nincs H1).

## Térképek beágyazása sellődiagramként

Ha **engedélyezve** (alapértelmezett), a megjelölt konvertálások gondolattérképeket és körvonalakat tartalmaztak [Hableány](https://mermaid.js.org/) diagramokká:

**iThoughts, MindManager, FreeMind, OPML & Bike** – Mermaid gondolattérkép-diagramok formájában renderelt fa elrendezéssel. Az iThoughts és a MindManager esetében az alakinformációk (lekerekített, téglalap, hatszög stb.) megőrződnek, ahol rendelkezésre állnak. A FreeMind (`.mm`) és az OPML ugyanazt a gondolattérkép-formátumot használja. A kerékpáros (`.bike`) körvonalai a mellékelt fájlnevet (mínusz kiterjesztést) használják gondolattérkép gyökércsomópontként. A csomópontcímkék egyszerű szövegesek (a hivatkozások hivatkozásszöveggé válnak; a feladatok ☐ / ☑ előtagként jelennek meg). A Mermaid alapértelmezés szerint minden Markdown előnézetben szerepel.

**Korlátozás:** A gondolattérkép-beágyazás (Hableány diagramok) nem működik a Discount elemzővel. Használja a MultiMarkdown-t, a CommonMark-ot (GFM) vagy a Kramdownt a gondolattérkép-előnézetekhez.

Ha **letiltva**:

- **iThoughts** — Az .itmz fájl beépített előnézeti képe (`preview.png`) base64 képként van beágyazva. A kép alternatív szövege a fájlnevet használja.
- **MindManager** — A vázlat beágyazott Markdown listaként van beágyazva.
- **FreeMind** — A vázlat beágyazott jelölőlistaként van beágyazva.
- **OPML** — A körvonal beágyazott Markdown listaként van beágyazva (nincs gondolattérkép).
- **Kerékpár** — A körvonal beágyazott Markdown listaként van beágyazva (nincs H1); A legfelső szintű címsorelemek H2-vé, a beágyazott címsorok félkövérek, a feladatok pedig GitHub-jelölőnégyzetekké válnak.

## Tartalmazza a szintaxist

Használja ugyanazt a szintaxist, mint a többi fájl esetében:

	<<[path/to/map.itmz]
	<<[útvonal/map.mmap]
	<<[útvonal/térkép.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]

Vagy iA Writer blokk szintaxissal:

	/path/to/map.itmz

Az elérési utak lehetnek a fő dokumentumhoz képest relatívak vagy abszolútak (`/` vagy `~` karakterekkel kezdve). A részletekért lásd: [Többfájlos dokumentumok](Multi-File_Documents.html).

## OPML konverzió

Az OPML-fájlok beágyazott `<outline>` elemeket használnak `text` attribútummal. Ha a „Beágyazás sellődiagramként” engedélyezve van (lásd: [Beállítások: Alkalmazások](Settings_Apps.html)), az átalakítás egy Mermaid gondolattérképet hoz létre, amely ugyanazt a formátumot használja, mint az iThoughts és a MindManager:

- A `<body>` gyermek körvonalai a legfelső szintté válnak (vagy az „Outline” gyökér gyermekei, ha több legfelső szintű elem is van)
- A beágyazott körvonalak határozzák meg a hierarchiát
- A hiányzó vagy üres `text` a következőként jelenik meg: `(unnamed)`
- A szöveg fertőtlenített; különleges karaktereket szöknek meg a Mermaid számára

## Bike átalakítás

A kerékpáros `.bike` fájlok HTML formátumúak, `<ul>` és `<li>` elemekkel. Az elemeken lehet `data-type="heading"` (legfelső szint → H2 megnyitott vagy lista módban; beágyazott → félkövér) vagy `data-type="task"` (GitHub jelölőnégyzetek; kitöltve, ha a `data-done` időbélyeggel rendelkezik, vagy a `data-checked` / `data-completed` igaz). A szövegközi formázás és a csomópontszövegben lévő hivatkozások Markdown formátumba konvertálódnak. Mermaid gondolattérképként történő beágyazáskor a fájlnév (mínusz kiterjesztés) egyetlen gyökércsomópontként használatos, a címkék pedig egyszerű szöveges formázásúak a Mermaid gondolattérkép szintaxisához.