# <%= @title %>

## Sélection du processeur

[MultiMarkdown](http://fletcherpenney.net/multimarkdown/ "MultiMarkdown") (par Fletcher Penney) est une extension de [Markdown](http://daringfireball.net/projects/markdown/ "Daring Fireball: Markdown") (par John Gruber). Tout le formatage Markdown standard est respecté, et MultiMarkdown fournit des syntaxes supplémentaires pour des éléments tels que les tableaux et les notes de bas de page.

## Syntaxe

Il existe un guide de syntaxe Markdown dans le menu d'aide, ou vous pouvez consulter la [documentation originale de John Gruber](http://daringfireball.net/projects/markdown/syntax).

Les extensions MultiMarkdown sont documentées par Fletcher Penney dans [ce document](https://github.com/fletcher/MultiMarkdown/blob/master/Documentation/MultiMarkdown%20User%27s%20Guide.md).

## Rendu alternatif

Vous pouvez choisir entre MultiMarkdown, Kramdown, CommonMark et Discount dans le {% prefspane Processor %}. Chacun offre des fonctionnalités supplémentaires avec une syntaxe légèrement différente (voir {% appmenu Help, Markdown Reference %} pour plus de détails). Dans la plupart des cas, MultiMarkdown est préféré, mais si vous avez des fichiers utilisant déjà une syntaxe spécifique à un processeur, ou si vous rencontrez des problèmes pour restituer un fichier Markdown avec MultiMarkdown, sélectionnez CommonMark comme processeur par défaut.
