# <%= @title %>

Arraste um documento do [Tree Outliner][tree] (`.treeoutline`) para o Marked para vê-lo como títulos e listas, ou como um diagrama Mermaid.

## Títulos e listas [headings-and-lists]

Este é o padrão. O Marked compila o esboço como Markdown:

- O título do documento é um título de nível 1.
- As linhas do esboço continuam como títulos até o nível definido por **Headings through level** em {% prefspane Apps %}, no grupo *Tree Outliner*. O padrão é **2**, então a primeira linha do esboço é um título de nível 2 e as linhas mais profundas viram uma lista aninhada.
- Notas em uma linha viram parágrafos sob esse título ou item de lista.

## Diagrama Mermaid [mermaid-diagram]

Em {% prefspane Apps %}, em *Mind Maps and Outlines*, ative **Tree Outliner outlines** para ver o arquivo como um diagrama Mermaid. O título do documento é o nó raiz. O mesmo interruptor vale ao abrir um arquivo `.treeoutline` e ao [incluí-lo](Embedding_Mind_Maps_and_Outlines.html) em outro documento.

**Headings through level** só é usado quando esse interruptor está desativado.

Diagramas Mermaid precisam de MultiMarkdown, CommonMark (GFM) ou Kramdown. Eles não são desenhados com o processador Discount.

[tree]: https://noteifyapp.com/tree-outliner/
