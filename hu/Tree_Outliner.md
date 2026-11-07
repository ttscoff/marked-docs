# <%= @title %>

Húzzon egy [Tree Outliner][tree]-dokumentumot (`.treeoutline`) a Markedre, hogy címsorokként és listákként, vagy Mermaid-diagramként jelenjen meg.

## Címsorok és listák [headings-and-lists]

Ez az alapértelmezés. A Marked Markdownként állítja össze a vázlatot:

- A dokumentum címe 1. szintű címsor.
- A vázlat sorai címsorok maradnak addig a szintig, amelyet a **Headings through level** állít be a {% prefspane Apps %} *Tree Outliner* csoportjában. Az alapértelmezés **2**, így a vázlat első sora 2. szintű címsor, a mélyebb sorok pedig beágyazott listává válnak.
- Egy sor jegyzetei bekezdések lesznek az adott címsor vagy listaelem alatt.

## Mermaid-diagram [mermaid-diagram]

A {% prefspane Apps %} *Mind Maps and Outlines* csoportjában kapcsolja be a **Tree Outliner outlines** lehetőséget, hogy a fájl Mermaid-diagramként jelenjen meg. A dokumentum címe a gyökércsomópont. Ugyanez a kapcsoló érvényes, amikor megnyit egy `.treeoutline` fájlt, és amikor [beilleszt](Embedding_Mind_Maps_and_Outlines.html) egyet egy másik dokumentumba.

A **Headings through level** csak akkor érvényes, ha ez a kapcsoló ki van kapcsolva.

A Mermaid-diagramokhoz MultiMarkdown, CommonMark (GFM) vagy Kramdown kell. A Discount processzorral nem jelennek meg.

[tree]: https://noteifyapp.com/tree-outliner/
