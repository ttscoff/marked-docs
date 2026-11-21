# <%= @title %>

Les cartes FerventMind (`.fvmd`) s'ouvrent dans Marked. Marked décompresse le paquet. Si un `text.md` s'y trouve, ce fichier est l'aperçu. Sinon, Marked construit un plan à partir de `map.xml`.

## Plan tiré de la carte [outline-from-the-map]

Le texte de chaque sujet devient des titres jusqu'au niveau fixé par **Headings through level** (2 par défaut). Les sujets plus profonds deviennent des puces imbriquées, de sorte que les tâches de ces niveaux gardent une case de liste. Les notes deviennent le corps de la section. Une tâche terminée devient une case cochée, et une tâche partielle affiche son pourcentage. Les images sont les fichiers sous `assets/`, sans légende portant le nom du fichier.

## N'afficher que les sujets visibles [display-only-visible-topics]

**Display only visible topics**, dans {% prefspane Apps %} sous *FerventMind*, ignore les sujets situés dans une branche repliée lorsque Marked construit ce plan. Il ne modifie pas un `text.md` déjà enregistré par l'application.

## Inclure une carte [including-a-map]

Inclure un `.fvmd` utilise **FerventMind files** sous **Embed as Mermaid mind maps :** dans {% prefspane Apps %}. Activé, cela produit un diagramme Mermaid de l'arbre visible ou complet, selon la case ci-dessus. Désactivé, cela intègre le `preview.png` de la carte. Voir [Intégration de cartes mentales et de plans](Embedding_Mind_Maps_and_Outlines.html).

## Ouvrir dans l'éditeur [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) lance FerventMind.
