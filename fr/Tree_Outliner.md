# <%= @title %>

Faites glisser un document [Tree Outliner][tree] (`.treeoutline`) sur Marked pour l'afficher comme des titres et des listes, ou comme un diagramme Mermaid.

## Titres et listes [headings-and-lists]

C'est le réglage par défaut. Marked compile le plan en Markdown :

- Le titre du document est un titre de niveau 1.
- Les lignes du plan restent des titres jusqu'au niveau fixé par **Headings through level** dans {% prefspane Apps %}, sous *Tree Outliner*. La valeur par défaut est **2** : la première ligne du plan est un titre de niveau 2, et les lignes plus profondes deviennent une liste imbriquée.
- Les notes d'une ligne deviennent des paragraphes sous ce titre ou cet élément de liste.

## Diagramme Mermaid [mermaid-diagram]

Dans {% prefspane Apps %}, sous *Mind Maps and Outlines*, activez **Tree Outliner outlines** pour afficher le fichier comme un diagramme Mermaid. Le titre du document est le nœud racine. Le même réglage s'applique lorsque vous ouvrez un fichier `.treeoutline` et lorsque vous en [incluez](Embedding_Mind_Maps_and_Outlines.html) un dans un autre document.

**Headings through level** n'est utilisé que lorsque ce réglage est désactivé.

Les diagrammes Mermaid exigent MultiMarkdown, CommonMark (GFM) ou Kramdown. Ils ne s'affichent pas avec le processeur Discount.

[tree]: https://noteifyapp.com/tree-outliner/
