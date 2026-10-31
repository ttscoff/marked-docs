# <%= @title %>

Húzzon egy [Bike][bike]-vázlatot (`.bike`) a Markedre, hogy beágyazott Markdown-listaként jelenjen meg, a címsorokkal félkövéren és a feladatokkal jelölőnégyzetként.

## Bike-vázlat megnyitása [opening-a-bike-outline]

A Marked a fájl megnyitásakor alakítja át a vázlatot:

- A címsorként jelölt sorok **félkövér** listaelemek lesznek.
- A feladatok GitHub-stílusú jelölőnégyzetek lesznek. A feladat be van jelölve, ha a Bike befejezési időt tárol, vagy késznek jelöli.
- A sor szövegében lévő hivatkozások és formázás Markdown marad.

A `.bike` fájl megnyitása mindig ezt a listát használja. A vázlat nem lesz Mermaid-diagram.

## Bike-vázlat beillesztése [including-a-bike-outline]

Egy `.bike` fájl egy másik Markdown-dokumentumba is beilleszthető. Lásd: [Gondolattérképek és vázlatok beágyazása](Embedding_Mind_Maps_and_Outlines.html).

A {% prefspane Apps %} *Mind Maps and Outlines* csoportjában a **Bike outlines** a beillesztett fájlokra vonatkozik:

- **Be** (alapértelmezés) — Mermaid-diagram. A fájlnév `.bike` nélkül a gyökércsomópont.
- **Ki** — ugyanaz a beágyazott Markdown-lista, mint a fájl megnyitásakor, dokumentumcím nélkül.

A Mermaid-diagramokhoz MultiMarkdown, CommonMark (GFM) vagy Kramdown kell. A Discount processzorral nem jelennek meg.

[bike]: https://www.hogbaysoftware.com/bike/
