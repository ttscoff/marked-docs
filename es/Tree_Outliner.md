# <%= @title %>

Arrastre un documento de [Tree Outliner][tree] (`.treeoutline`) a Marked para verlo como títulos y listas, o como un diagrama Mermaid.

## Títulos y listas [headings-and-lists]

Este es el valor predeterminado. Marked compila el esquema como Markdown:

- El título del documento es un título de nivel 1.
- Las filas del esquema siguen como títulos hasta el nivel que fija **Headings through level** en {% prefspane Apps %}, en el grupo *Tree Outliner*. El valor predeterminado es **2**, de modo que la primera fila del esquema es un título de nivel 2 y las filas más profundas pasan a ser una lista anidada.
- Las notas de una fila pasan a ser párrafos bajo ese título o elemento de lista.

## Diagrama Mermaid [mermaid-diagram]

En {% prefspane Apps %}, en *Mind Maps and Outlines*, active **Tree Outliner outlines** para ver el archivo como un diagrama Mermaid. El título del documento es el nodo raíz. El mismo interruptor se aplica al abrir un archivo `.treeoutline` y al [incluirlo](Embedding_Mind_Maps_and_Outlines.html) en otro documento.

**Headings through level** solo se usa cuando ese interruptor está desactivado.

Los diagramas Mermaid necesitan MultiMarkdown, CommonMark (GFM) o Kramdown. No se muestran con el procesador Discount.

[tree]: https://noteifyapp.com/tree-outliner/
