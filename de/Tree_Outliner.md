# <%= @title %>

Ziehen Sie ein [Tree Outliner][tree]-Dokument (`.treeoutline`) auf Marked, um es als Überschriften und Listen oder als Mermaid-Diagramm zu sehen.

## Überschriften und Listen [headings-and-lists]

Das ist die Vorgabe. Marked kompiliert die Gliederung als Markdown:

- Der Dokumenttitel ist eine Überschrift der Ebene 1.
- Gliederungszeilen bleiben Überschriften bis zu der Ebene, die **Headings through level** unter {% prefspane Apps %} in der Gruppe *Tree Outliner* festlegt. Die Vorgabe ist **2**, sodass die erste Zeile der Gliederung eine Überschrift der Ebene 2 ist und tiefere Zeilen eine verschachtelte Liste werden.
- Notizen an einer Zeile werden Absätze unter dieser Überschrift oder diesem Listeneintrag.

## Mermaid-Diagramm [mermaid-diagram]

Schalten Sie unter {% prefspane Apps %}, bei *Mindmaps/Gliederungen*, **Tree Outliner outlines** ein, um die Datei als Mermaid-Diagramm zu sehen. Der Dokumenttitel ist der Stammknoten. Derselbe Schalter gilt, wenn Sie eine `.treeoutline`-Datei öffnen und wenn Sie eine in ein anderes Dokument [einbinden](Embedding_Mind_Maps_and_Outlines.html).

**Headings through level** gilt nur, wenn dieser Schalter aus ist.

Mermaid-Diagramme brauchen MultiMarkdown, CommonMark (GFM) oder Kramdown. Mit dem Discount-Prozessor werden sie nicht gerendert.

[tree]: https://noteifyapp.com/tree-outliner/
