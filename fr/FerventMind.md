# <%= @title %>

Les cartes FerventMind (`.fvmd`) s'ouvrent dans Marked. Marked décompresse le paquet et affiche le `text.md` enregistré par FerventMind.

## Markdown dans la carte [markdown-in-the-map]

La façon d'écrire ce Markdown se règle dans FerventMind, sous **Settings > Files And Export**, dans le groupe **Markdown**. Marked affiche le fichier tel qu'il a été enregistré.

![FerventMind Files And Export][fm-export]

**Headings** fixe le nombre de niveaux qui restent des titres. **Visible topics only** ignore les sujets situés dans une branche repliée. **Notes** et **Task checkboxes** décident si les notes et les tâches sont écrites dans ce Markdown. Ces choix s'appliquent à l'exportation Markdown, à Copy As et à la copie Markdown enregistrée dans chaque carte pour des applications telles que Marked. Une carte peut les remplacer sous **Definitions • MAP**.

Si une ancienne carte n'a pas de `text.md`, Marked construit un plan à partir de `map.xml` : le titre est le titre 1, le niveau suivant est le titre 2, et les sujets plus profonds deviennent des puces imbriquées. Les notes deviennent le corps de la section. Une tâche terminée devient une case cochée, et une tâche partielle affiche son pourcentage. Les images sont les fichiers sous `assets/`, sans légende portant le nom du fichier.

## Inclure une carte [including-a-map]

Inclure un `.fvmd` utilise **FerventMind files** sous **Embed as Mermaid mind maps :** dans {% prefspane Apps %}. Activé, cela produit un diagramme Mermaid à partir de la carte. Désactivé, cela intègre le `preview.png` de la carte. Voir [Intégration de cartes mentales et de plans](Embedding_Mind_Maps_and_Outlines.html).

## Ouvrir dans l'éditeur [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) lance FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
