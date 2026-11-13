# <%= @title %>

Faites glisser un plan [Bike][bike] sur Marked pour l'afficher comme une liste Markdown imbriquée, avec les lignes de titre en gras et les tâches comme cases à cocher. Un plan seul est un fichier `.bike`. Bike 2 enregistre un paquet `.biked` lorsque le plan contient des images intégrées.

## Ouvrir un plan Bike [opening-a-bike-outline]

Marked convertit le plan à l'ouverture du fichier :

- Les lignes marquées comme titre deviennent des éléments de liste en **gras**.
- Les tâches deviennent des cases à cocher dans le style GitHub. Une tâche est cochée lorsque Bike enregistre une heure d'achèvement ou la marque comme faite.
- Les liens et la mise en forme dans le texte de la ligne sont conservés en Markdown.

Ouvrir un fichier `.bike` utilise toujours cette liste. Le plan ne devient pas un diagramme Mermaid. Un paquet `.biked` suit le réglage **Bike outlines** décrit plus bas.

## Inclure un plan Bike [including-a-bike-outline]

Un fichier `.bike` peut aussi être inclus dans un autre document Markdown. Voir [Intégrer des cartes mentales et des plans](Embedding_Mind_Maps_and_Outlines.html).

Dans {% prefspane Apps %}, sous *Mind Maps and Outlines*, **Bike outlines** s'applique aux fichiers inclus :

- **Activé** (valeur par défaut) — un diagramme Mermaid. Le nom du fichier, sans `.bike`, est le nœud racine.
- **Désactivé** — la même liste Markdown imbriquée qu'à l'ouverture du fichier, sans titre de document.

## Plans avec images [outlines-with-images]

Bike 2 enregistre un paquet `.biked` lorsque le plan contient des images intégrées. Le paquet est un TextBundle : `text.bike` et un dossier `assets`. Ouvrez le fichier `.biked` lui-même. Marked lit le plan qu'il contient et donne à la fenêtre le nom du paquet.

Désactivez **Bike outlines** pour afficher ce paquet comme la liste imbriquée, qui conserve les images intégrées. **Activé** transforme le plan en diagramme Mermaid.

[bike]: https://www.hogbaysoftware.com/bike/
