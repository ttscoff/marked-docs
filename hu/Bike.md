# <%= @title %>

Húzzon egy [Bike][bike]-vázlatot a Markedre, hogy beágyazott Markdown-listaként jelenjen meg, a címsorokkal félkövéren és a feladatokkal jelölőnégyzetként. Egy önálló vázlat `.bike` fájl. A Bike 2 `.biked` csomagot ment, ha a vázlat beágyazott képeket tartalmaz.

## Bike-vázlat megnyitása [opening-a-bike-outline]

A Marked a fájl megnyitásakor alakítja át a vázlatot:

- A címsorként jelölt sorok **félkövér** listaelemek lesznek.
- A feladatok GitHub-stílusú jelölőnégyzetek lesznek. A feladat be van jelölve, ha a Bike befejezési időt tárol, vagy késznek jelöli.
- A sor szövegében lévő hivatkozások és formázás Markdown marad.

A `.bike` fájl megnyitása mindig ezt a listát használja. A vázlat nem lesz Mermaid-diagram. A `.biked` csomag a lentebb leírt **Bike outlines** beállítást követi.

## Bike-vázlat beillesztése [including-a-bike-outline]

Egy `.bike` fájl egy másik Markdown-dokumentumba is beilleszthető. Lásd: [Gondolattérképek és vázlatok beágyazása](Embedding_Mind_Maps_and_Outlines.html).

A {% prefspane Apps %} *Mind Maps and Outlines* csoportjában a **Bike outlines** a beillesztett fájlokra vonatkozik:

- **Be** (alapértelmezés) — Mermaid-diagram. A fájlnév `.bike` nélkül a gyökércsomópont.
- **Ki** — ugyanaz a beágyazott Markdown-lista, mint a fájl megnyitásakor, dokumentumcím nélkül.

## Vázlatok képekkel [outlines-with-images]

A Bike 2 `.biked` csomagot ment, ha a vázlat beágyazott képeket tartalmaz. A csomag TextBundle: `text.bike` és egy `assets` mappa. Magát a `.biked` fájlt nyissa meg. A Marked a benne lévő vázlatot olvassa, az ablak címe pedig a csomag neve.

Kapcsolja ki a **Bike outlines** beállítást, ha a csomagot beágyazott listaként, a képekkel együtt szeretné látni. A **Be** állás Mermaid-diagramot készít.

[bike]: https://www.hogbaysoftware.com/bike/
