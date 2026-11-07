# <%= @title %>

Trascina un documento [Tree Outliner][tree] (`.treeoutline`) su Marked per vederlo come titoli ed elenchi, oppure come un diagramma Mermaid.

## Titoli ed elenchi [headings-and-lists]

È l'impostazione predefinita. Marked compila la struttura come Markdown:

- Il titolo del documento è un titolo di livello 1.
- Le righe della struttura restano titoli fino al livello impostato da **Headings through level** in {% prefspane Apps %}, nel gruppo *Tree Outliner*. Il valore predefinito è **2**, quindi la prima riga della struttura è un titolo di livello 2 e le righe più profonde diventano un elenco annidato.
- Le note di una riga diventano paragrafi sotto quel titolo o elemento di elenco.

## Diagramma Mermaid [mermaid-diagram]

In {% prefspane Apps %}, sotto *Mind Maps and Outlines*, attiva **Tree Outliner outlines** per vedere il file come un diagramma Mermaid. Il titolo del documento è il nodo radice. Lo stesso interruttore vale quando apri un file `.treeoutline` e quando ne [includi](Embedding_Mind_Maps_and_Outlines.html) uno in un altro documento.

**Headings through level** si usa solo quando quell'interruttore è disattivo.

I diagrammi Mermaid richiedono MultiMarkdown, CommonMark (GFM) o Kramdown. Non vengono disegnati con il processore Discount.

[tree]: https://noteifyapp.com/tree-outliner/
