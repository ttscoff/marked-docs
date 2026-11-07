# <%= @title %>

Les cartes mentales et les plans peuvent être intégrés dans votre aperçu Markdown à l'aide de la [syntaxe d'inclusion de Marked][include] ou de la [syntaxe de bloc iA Writer][ia]. Le comportement dépend du format de fichier et du paramètre « Intégrer les cartes en tant que diagrammes Mermaid » dans {% prefspane Apps %} sous *Mind Maps/Outlines*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Formats pris en charge [supported-formats]

### iThoughtsX (.itmz) [ithoughts-x-itmz]

Les fichiers de cartes mentales iThoughts sont des archives zip contenant des données cartographiques et une image d'aperçu facultative.

### MindManager (.mmap) [mindmanager-mmap]

Les fichiers MindManager sont des archives zip contenant `Document.xml`. Les packages MindManager décompressés (un dossier contenant `Document.xml`) et les chemins directs vers `Document.xml` sont également pris en charge.

### FreeMind (.mm) [freemind-mm]

Les fichiers de cartes mentales FreeMind utilisent l'extension `.mm` et stockent les données au format XML. Marked détecte le format FreeMind en vérifiant que le contenu du fichier commence par `<map` ; sinon (par exemple, un extrait de code), le fichier est inclus sous forme de texte brut. Les fichiers FreeMind sont pris en charge pour l'intégration de la carte mentale Mermaid.

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) est un format XML pour les plans hiérarchiques, largement utilisé par les planificateurs et les lecteurs de flux. iThoughts et d'autres applications peuvent exporter vers OPML. Marked convertit les fichiers OPML en diagrammes de carte mentale Mermaid.

### Bike (.bike) [bike-bike]

Voir [Bike](Bike.html) pour ouvrir un fichier `.bike`. Les plans Bike inclus suivent la case **Bike outlines** : activée, une carte mentale Mermaid (le nom du fichier, sans `.bike`, est le nœud racine) ; désactivée, une liste Markdown imbriquée sans titre de document.

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

Voir [Tree Outliner](Tree_Outliner.html). La case **Tree Outliner outlines** régit l'ouverture d'un fichier `.treeoutline` et son inclusion. Activée, elle dessine une carte mentale Mermaid dont la racine est le titre du document. Désactivée, elle compile des titres et des listes ; **Headings through level** dans le groupe *Tree Outliner* fixe la profondeur des titres.

## Intégrer des cartes sous forme de diagrammes Mermaid [embed-maps-as-mermaid-diagrams]

Lorsqu'il est **activé** (valeur par défaut), Marked convertit les cartes mentales et les contours inclus en diagrammes [Mermaid](https://mermaid.js.org/) :

**iThoughts, MindManager, FreeMind, OPML & Bike** : Rendus sous forme de diagrammes mindmap Mermaid avec la disposition en arbre bien rangé. Pour iThoughts et MindManager, les informations de forme (arrondi, rectangle, hexagone, etc.) sont conservées lorsqu'elles sont disponibles. FreeMind (`.mm`) et OPML utilisent le même format de carte mentale. Les contours Bike (`.bike`) utilisent le nom de fichier inclus (moins l'extension) comme nœud racine de la carte mentale. Les étiquettes de nœud sont en texte brut (les liens deviennent du texte de lien ; les tâches s'affichent sous la forme de préfixes ☐/☑). Mermaid est incluse par défaut dans chaque aperçu Markdown.

**Limitation :** L'intégration de cartes mentales (diagrammes Mermaid) ne fonctionne pas avec l'analyseur Discount. Utilisez MultiMarkdown, CommonMark (GFM) ou Kramdown pour les aperçus de cartes mentales.

Lorsque **désactivé** :

- **iThoughts** : L'image d'aperçu intégrée (`preview.png`) du fichier .itmz est intégrée en tant qu'image base64. Le texte alternatif de l'image utilise le nom du fichier.
- **MindManager** : Le plan est intégré sous forme de liste Markdown imbriquée.
- **FreeMind** : Le plan est intégré sous forme de liste Markdown imbriquée.
- **OPML** : Le plan est intégré sous forme de liste Markdown imbriquée (pas de carte mentale).
- **Bike** : Le plan est intégré sous forme de liste Markdown imbriquée (pas de H1) ; les éléments de titre de niveau supérieur deviennent H2, les titres imbriqués sont en gras et les tâches deviennent des cases à cocher GitHub.

## Inclure la syntaxe [include-syntax]

Utilisez la même syntaxe que pour les autres fichiers inclus :

	<<[path/to/map.itmz]
	<<[path/to/map.mmap]
	<<[path/to/outline.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]
	<<[path/to/outline.treeoutline]

Ou avec la syntaxe de bloc iA Writer :

	/path/to/map.itmz

Les chemins peuvent être relatifs au document principal ou absolus (commençant par `/` ou `~`). Voir [Documents multi-fichiers](Multi-File_Documents.html) pour plus de détails.

## Conversion OPML [opml-conversion]

Les fichiers OPML utilisent des éléments `<outline>` imbriqués avec un attribut `text`. Lorsque « Intégrer les cartes en tant que diagrammes Mermaid » est activé (voir [Paramètres : Applications](Settings_Apps.html)), la conversion produit une carte mentale Mermaid utilisant le même format que iThoughts et MindManager :

- Les contours enfants de `<body>` deviennent le niveau supérieur (ou les enfants d'une racine "Outline" s'il y a plusieurs éléments de niveau supérieur)
- Les contours imbriqués définissent la hiérarchie
- Le `text` manquant ou vide est affiché comme `(unnamed)`
- Le texte est aseptisé ; les caractères spéciaux sont échappés pour Mermaid

## Conversion de Bike [bike-conversion]

Les fichiers Bike `.bike` sont du HTML avec une `<ul>` racine et des éléments `<li>`. En mode liste, chaque ligne est un élément de liste : les lignes `data-type="heading"` sont en gras, et les lignes `data-type="task"` sont des cases GitHub (cochées lorsque `data-done` a un horodatage, ou lorsque `data-checked` / `data-completed` est vrai). La mise en forme et les liens dans le texte du nœud sont convertis en Markdown. Ouvrir un fichier `.bike` utilise toujours cette liste. Lorsqu'un fichier inclus est intégré comme carte mentale Mermaid, le nom du fichier (sans l'extension) est l'unique nœud racine et les étiquettes sont du texte brut pour la syntaxe mindmap de Mermaid.
