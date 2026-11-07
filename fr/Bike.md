# <%= @title %>

Faites glisser un plan [Bike][bike] (`.bike`) sur Marked pour l'afficher comme une liste Markdown imbriquée, avec les lignes de titre en gras et les tâches comme cases à cocher.

## Ouvrir un plan Bike [opening-a-bike-outline]

Marked convertit le plan à l'ouverture du fichier :

- Les lignes marquées comme titre deviennent des éléments de liste en **gras**.
- Les tâches deviennent des cases à cocher dans le style GitHub. Une tâche est cochée lorsque Bike enregistre une heure d'achèvement ou la marque comme faite.
- Les liens et la mise en forme dans le texte de la ligne sont conservés en Markdown.

Ouvrir un fichier `.bike` utilise toujours cette liste. Le plan ne devient pas un diagramme Mermaid.

## Inclure un plan Bike [including-a-bike-outline]

Un fichier `.bike` peut aussi être inclus dans un autre document Markdown. Voir [Intégrer des cartes mentales et des plans](Embedding_Mind_Maps_and_Outlines.html).

Dans {% prefspane Apps %}, sous *Mind Maps and Outlines*, **Bike outlines** s'applique aux fichiers inclus :

- **Activé** (valeur par défaut) — un diagramme Mermaid. Le nom du fichier, sans `.bike`, est le nœud racine.
- **Désactivé** — la même liste Markdown imbriquée qu'à l'ouverture du fichier, sans titre de document.

Les diagrammes Mermaid exigent MultiMarkdown, CommonMark (GFM) ou Kramdown. Ils ne s'affichent pas avec le processeur Discount.

[bike]: https://www.hogbaysoftware.com/bike/
