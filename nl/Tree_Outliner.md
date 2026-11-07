# <%= @title %>

Sleep een [Tree Outliner][tree]-document (`.treeoutline`) naar Marked om het als koppen en lijsten te bekijken, of als een Mermaid-diagram.

## Koppen en lijsten [headings-and-lists]

Dit is de standaard. Marked stelt het overzicht samen als Markdown:

- De documenttitel is een kop van niveau 1.
- Overzichtsregels blijven koppen tot het niveau dat **Headings through level** instelt in {% prefspane Apps %}, in de groep *Tree Outliner*. De standaard is **2**, zodat de eerste regel van het overzicht een kop van niveau 2 is en diepere regels een geneste lijst worden.
- Notities bij een regel worden alinea's onder die kop of dat lijstonderdeel.

## Mermaid-diagram [mermaid-diagram]

Zet in {% prefspane Apps %}, onder *Mind Maps and Outlines*, **Tree Outliner outlines** aan om het bestand als Mermaid-diagram te bekijken. De documenttitel is de hoofdknoop. Dezelfde schakelaar geldt wanneer u een `.treeoutline`-bestand opent en wanneer u er een [invoegt](Embedding_Mind_Maps_and_Outlines.html) in een ander document.

**Headings through level** wordt alleen gebruikt wanneer die schakelaar uit staat.

Mermaid-diagrammen hebben MultiMarkdown, CommonMark (GFM) of Kramdown nodig. Ze worden niet getekend met de Discount-processor.

[tree]: https://noteifyapp.com/tree-outliner/
