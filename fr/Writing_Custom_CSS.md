# <%= @title %>

Marked dispose d'un éditeur de style intégré et peut appliquer des fichiers CSS personnalisés.

Vous pouvez utiliser l'éditeur pour créer de superbes styles, ou, si vous en savez juste assez en CSS pour être dangereux, faire en sorte que Marked ait exactement l'apparence que vous souhaitez.

## Pour commencer

Il existe une galerie de styles personnalisés créés par le développeur et par les utilisateurs, sur [markedapp.com/styles](https://markedapp.com/styles/). La galerie permet de prévisualiser et d'installer des styles directement dans Marked. Tout style installé peut être affiché dans le Finder pour examen et modification. La galerie peut être ouverte à l'aide d'un visualiseur interne avec {% appmenu Style, Generate a Custom Style %}, ou en cliquant sur l'icône de crayon (modifier) à côté de n'importe quel style modifiable dans le Gestionnaire de styles. Si vous souhaitez modifier un style intégré, vous devrez d'abord le dupliquer dans le gestionnaire.

Il existe également un [dépôt de styles personnalisés](https://github.com/ttscoff/MarkedCustomStyles) sur GitHub, avec des exemples. N'hésitez pas à le parcourir, à l'utiliser et à y contribuer. Si vous diffusez votre thème basé sur l'un des thèmes de base, n'hésitez pas à vous ajouter aux crédits en tant que contributeur.

Grâce à la capacité de Marked à utiliser des fichiers CSS personnalisés, les possibilités de personnalisation de votre aperçu sont quasiment illimitées. Toutes les options CSS3 qui fonctionnent dans Safari fonctionneront dans Marked. Avec les fichiers Markdown par défaut dans Marked, il n'y a que quelques éléments HTML à gérer : tout le contenu se trouve dans une div dont l'id est « wrapper », le reste étant déterminé par le balisage de votre document.

Si vous concevez pour un usage personnel, il n'y a aucune règle. Activez le suivi du CSS avec la case à cocher sous le sélecteur de CSS personnalisé, et lorsque vous modifiez et enregistrez votre CSS personnalisé, l'aperçu se mettra à jour.

**Un [thème squelette est disponible](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) pour vous aider à démarrer.**

Si vous prévoyez de partager votre création CSS, il y a quelques points à couvrir. Premièrement, certaines classes du body doivent recevoir des styles :

## Classes du body

Les styles suivants doivent être inclus dans tout CSS Marked destiné à être partagé. Les classes du body permettent de cibler et de modifier n'importe quel sélecteur selon différentes options de préférence.

### Inverted (mode sombre)

Lorsque l'utilisateur sélectionne {% appmenu Preview, Dark Mode %}, une classe « inverted » est ajoutée à la balise body. Vous pouvez l'utiliser pour cibler les styles à fort contraste, clair sur fond sombre.

Vous ne souhaitez appliquer les styles inversés qu'à l'aperçu, pas à l'impression : utilisez donc une media query (`@media screen`) pour les restreindre. Le code ci-dessous est assez générique, et dans la plupart des cas vous pouvez simplement l'intégrer à votre feuille de style pour assurer la compatibilité, mais n'hésitez pas à l'ajuster.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poetry (poésie)

L'utilisateur peut choisir si un texte indenté par tabulation doit être traité comme de la poésie ou du code. La seule différence est que les blocs pre/code sont stylés de façon plus, disons, poétique lorsque le mode poésie est choisi. La classe « poetry » est appliquée à la balise body.

Laissez libre cours à votre créativité dans la mise en forme, mais voici un extrait de base :

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Cas particuliers

Les tableaux, les balises Figure/Figcaption, ainsi que le cas particulier de `a.footnote` et `div.footnotes>a` doivent également être pris en compte. Il n'existe pas de règles fixes sur la façon de les gérer, mais examinez les styles par défaut pour avoir une idée des règles CSS dont Marked a besoin.

Le style de tableau standard, dans tous les styles par défaut, utilise de la transparence sur les lignes alternées pour se fondre en douceur avec n'importe quel arrière-plan. Vous pouvez reprendre ces styles, ou faire à votre façon : assurez-vous simplement de les avoir stylés ! Il en va de même pour figure et figcaption ; ajoutez une image avec un texte alternatif à un document pour voir à quoi ressemble le balisage généré, et stylez-le en conséquence.

Les notes de bas de page incluses dans un document génèrent un lien dans le contenu (`a.footnote`), ainsi qu'une div en fin de document contenant le texte référencé (`div.footnotes`). Là encore, reportez-vous aux styles par défaut. Pour éviter de modifier la hauteur de ligne des lignes contenant un numéro de référence de note de bas de page, veillez à inclure quelque chose comme :

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Pour garder la flèche de retour sur la même ligne, incluez :

```css
.footnotes p {display:inline}
```

Il est également conseillé d'inclure une règle générale pour toutes les images, afin qu'elles restent dans la largeur de la page. Quelque chose comme :

```css
#wrapper img { max-width: 100% }
```

Si votre thème comporte un espacement supplémentaire ou une largeur fixe, ajustez le max-width en conséquence.

## Styles d'impression

Veillez à inclure des styles d'impression qui suppriment toute couleur d'arrière-plan, tout défilement fixe, et l'interface propre à l'aperçu. Marked offre deux façons de cibler la sortie impression et PDF.

### `@media print`

Les règles CSS d'impression standards s'appliquent lors de l'impression depuis Marked, ou lorsque l'export PDF utilise le media type print :

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### La classe `.mkprinting`

Lorsque Marked prépare un document pour l'**export PDF** ou l'**aperçu Impression/PDF** ({% kbd cmd P %}), il ajoute la classe `mkprinting` à la balise `<body>` (aux côtés de classes d'export telles que `bandw`, `breakAfterTOC`, et de la classe `mkstyle--*` propre à votre style). Les thèmes intégrés de Marked utilisent cette classe pour la plupart des règles spécifiques à l'impression, plutôt que de se fier uniquement à `@media print`.

L'export PDF charge souvent la WebView de rendu masquée avec le media type **screen** (en particulier pour les styles personnalisés et les documents [Fountain](Fountain_for_Screenwriters.html)) : les blocs `@media print` de votre feuille de style peuvent donc **ne pas** s'appliquer à la sortie PDF. Les règles préfixées par `.mkprinting` s'appliquent toujours lors de l'export, car ce sont de simples sélecteurs de classe, et non des media queries.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Pour les styles qui doivent fonctionner à la fois pour l'impression navigateur et l'export PDF de Marked, dupliquez les règles essentielles ou combinez les sélecteurs :

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

Pour déboguer du CSS d'impression personnalisé, ouvrez l'aperçu Impression/PDF ou exportez en PDF, puis utilisez [l'Inspecteur web de Safari](#webkitinspector) pour inspecter le document : la balise `<body>` portera la classe `mkprinting` tant que la mise en page d'impression est active.

Le masquage des liens à l'impression est géré en dehors du thème principal, ce qui permet aux utilisateurs de choisir de masquer les mises en évidence et soulignements de liens à l'impression. Tant que vous avez défini un style de base pour le texte, vous n'avez pas à vous en soucier.

Alors, à vous de jouer. Convertissez le thème de votre blog, créez un style d'impression parfait pour vos documents PDF, ou concevez l'aperçu idéal pour votre style d'écriture. Si vous créez quelque chose de formidable, [partagez-le avec la communauté](https://markedapp.com/styleshare/).

## Réglages CSS supplémentaires

Dans le {% prefspane Style %}, vous pouvez modifier le CSS supplémentaire. Ces styles seront ajoutés après tout thème chargé, et peuvent servir à apporter des modifications universelles à tous les thèmes.

En utilisant une [spécificité élevée](#overridingspecificity), des media queries `@media` pour l'impression et l'écran, ainsi que des sélecteurs `.mkprinting` pour l'export PDF, vous pouvez contrôler pratiquement tous les aspects du style avec un minimum de connaissances en CSS.

## Inspecteur WebKit

L'Inspecteur web de Safari est le moyen le plus simple de voir exactement quel HTML et quel CSS Marked génère, et d'expérimenter en direct avec les styles personnalisés.

### Activer le menu Développement dans Safari

1. Ouvrez Safari et choisissez {% appmenu Safari, Settings… %}.
2. Sélectionnez l'onglet **Avancé**.
3. Activez **Afficher les fonctionnalités pour les développeurs de sites web** (ou **Afficher le menu Développement dans la barre des menus** sur les anciennes versions de macOS).

Une fois cette option activée, un menu **Développement** apparaîtra dans la barre de menus de Safari.

![Menu Développement de Safari montrant les documents Marked][develop-menu]

### Inspecter un document Marked

1. Avec une fenêtre d'aperçu ouverte dans Marked, passez à Safari.
2. Dans la barre de menus, choisissez **Développement → _\<nom de votre Mac\>_ → Marked → _\<titre du document\>_**.
3. Safari ouvrira une fenêtre Inspecteur web rattachée à l'aperçu Marked sélectionné.

À partir de là, vous pouvez :

- Utiliser l'onglet **Éléments** pour inspecter le DOM à l'intérieur de la div `#wrapper` et voir quelles règles CSS sont appliquées.
- Survoler des éléments dans l'arborescence DOM pour les mettre en évidence dans la fenêtre Marked.
- Utiliser le panneau latéral **Styles** pour ajuster les règles en direct, puis recopier les extraits fonctionnels dans un style personnalisé ou dans le **CSS supplémentaire**.
    - Après avoir modifié du CSS dans l'onglet Éléments, vous pouvez obtenir un résumé de vos modifications en sélectionnant l'onglet Modifications

	![Modifications][css-changes]
- Utiliser l'onglet **Console** pour exécuter du JavaScript sur l'aperçu en direct. L'intégralité de l'[API JavaScript de Marked](https://markedapp.com/help/jsapi/) est disponible dans cette console.
- Explorer d'autres onglets, comme **Réseau**, pour déboguer les ressources chargées par votre document.

![Inspection d'un aperçu Marked avec l'Inspecteur web de Safari][inspecting]

## Partager du CSS personnalisé

Utilisez {% appmenu Style, Share a Custom Style %} pour ouvrir l'application de partage dans votre navigateur web. Glissez votre CSS dans la zone de dépôt (ou cliquez pour le sélectionner depuis le disque) et envoyez le CSS de votre style personnalisé.

Les styles partagés doivent être approuvés par le développeur avant d'apparaître dans la galerie : vous ne verrez donc pas de résultat immédiat.

## Autres astuces

### Surcharger la spécificité

Dans l'aperçu de Marked, une classe de body basée sur le nom de fichier du style actuel est ajoutée. Si l'aperçu est réglé sur « Swiss », la balise `<body>` portera une classe nommée `mkstyle--swiss`. Si votre CSS personnalisé s'appelle MyCustom.css, la classe du body sera `mkstyle--mycustom`. Vous pouvez l'utiliser avant les règles définies dans les styles de base pour les surcharger. Pour obtenir une spécificité absolue dans une règle, utilisez également l'ID #wrapper de la div conteneur :

	.mkstyle--mycustom #wrapper p+p { ... }

### Style de la table des matières

Si vous utilisez le jeton `<!--toc-->` pour [insérer une table des matières](Special_Syntax.html#tableofcontents), vous pouvez surcharger les réglages des indicateurs de niveau de la table des matières dans un style personnalisé, en utilisant « #wrapper » pour augmenter la spécificité :

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Cela ferait en sorte que tous les éléments de liste de la table des matières utilisent une puce carrée plutôt que celle définie dans les Paramètres, lorsque votre style personnalisé est actif.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
