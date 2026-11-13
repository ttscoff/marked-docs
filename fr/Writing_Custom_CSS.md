# <%= @title %>

Marked dispose d'un éditeur de style intégré et peut appliquer des fichiers CSS personnalisés.

Vous pouvez utiliser l'éditeur pour créer de superbes styles, ou si vous connaissez juste assez de CSS pour être dangereux, vous pouvez faire en sorte que Marked ressemble exactement à ce que vous voulez.

## Pour commencer [getting-started]

Il existe une galerie de styles personnalisés créés par le développeur et par les utilisateurs sur [markedapp.com/styles](https://markedapp.com/styles/). La galerie vous permet de prévisualiser et d'installer des styles directement dans Marked. Tout style installé peut être révélé dans le Finder pour examen et modification. La galerie peut être ouverte à l'aide d'un visualiseur interne avec {% appmenu Style, Generate a Custom Style %}, ou en cliquant sur l'icône du crayon (modifier) à côté de tout style modifiable dans le Gestionnaire de styles. Si vous souhaitez modifier un style intégré, vous devrez d'abord le dupliquer dans le gestionnaire.

Il existe également un [dépôt de styles personnalisés](https://github.com/ttscoff/MarkedCustomStyles) sur GitHub avec des exemples. N'hésitez pas à le parcourir, à l'utiliser et à y contribuer. Si vous distribuez votre thème basé sur l'un des thèmes de base, n'hésitez pas à vous ajouter aux crédits en tant que contributeur.

Avec la capacité de Marked à utiliser des fichiers CSS personnalisés, le ciel est la limite pour personnaliser votre aperçu. Toutes les options CSS3 qui fonctionnent dans Safari fonctionneront dans Marked. Avec les fichiers Markdown par défaut dans Marked, il n'y a que quelques éléments HTML à gérer ; tout le contenu se trouve dans une div avec l'ID « wrapper », le reste étant déterminé par le balisage de votre document.

Si vous créez un style pour un usage personnel, il n'y a aucune règle. Activez le suivi du CSS avec la case à cocher sous le sélecteur de CSS personnalisé, et lorsque vous modifiez et enregistrez votre CSS personnalisé, l'aperçu se mettra à jour.

**Un [thème squelette est disponible](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) pour bien démarrer.**

Si vous envisagez de partager votre création CSS, il y a quelques points à couvrir. Tout d'abord, certaines classes du body doivent recevoir des styles :

## Classes du body [body-classes]

Les styles suivants doivent être inclus dans tout CSS Marked destiné à être partagé. Les classes du body vous permettent de cibler et de modifier n'importe quel sélecteur selon les différentes options de préférences.

### Inversé [inverted]

Lorsque l'utilisateur sélectionne {% appmenu Preview, Dark Mode %}, une classe « inverted » est ajoutée à la balise body. Vous pouvez l'utiliser pour cibler les styles à fort contraste, clairs sur fond sombre.

Vous ne voulez généralement appliquer les styles inversés qu'à l'aperçu, pas à l'impression, donc utilisez une media query (@media screen) pour le restreindre. Le code ci-dessous est plutôt polyvalent et, dans la plupart des cas, vous pouvez simplement le déposer dans votre feuille de style pour assurer la compatibilité, mais n'hésitez pas à l'ajuster.

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

### Poésie [poetry]

L'utilisateur peut choisir si le texte indenté par tabulation est de la poésie ou du code. La seule différence est que les blocs pre/code sont stylés de façon plus, disons, poétique si le mode poésie est choisi. La classe « poetry » est appliquée à la balise body.

Soyez aussi créatif que vous le souhaitez avec la mise en forme, mais voici un extrait de base :

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

## Cas particuliers [special-cases]

Les tableaux, Figure/Figcaption, et le cas particulier de `a.footnote` et `div.footnotes>a` doivent également être pris en compte. Il n'y a pas de règles fixes sur la façon de les gérer, mais jetez un œil aux styles par défaut pour avoir une idée des règles CSS dont Marked a besoin.

Le style de tableau standard utilisé dans tous les styles par défaut applique de la transparence sur les rangées alternées afin qu'il se fonde doucement avec n'importe quel arrière-plan. Vous pouvez reprendre ces styles, ou suivre votre propre voie, assurez-vous simplement de les avoir stylés ! Il en va de même pour figure et figcaption ; ajoutez une image avec un texte alternatif à un document pour voir comment le balisage se présente et stylez-le en conséquence.

Les notes de bas de page incluses dans un document produiront un lien dans le contenu (a.footnote), et une div à la fin avec le texte référencé (div.footnotes). Là encore, consultez les styles par défaut pour référence. Pour éviter de modifier la hauteur de ligne des lignes contenant un numéro de référence de note de bas de page, veillez à inclure quelque chose comme :

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

Il est également conseillé d'inclure une règle générale pour toutes les images afin de les maintenir dans la largeur de la page. Quelque chose comme :

```css
#wrapper img { max-width: 100% }
```

Si votre thème comporte un remplissage supplémentaire ou une largeur fixe, modifiez le max-width en conséquence.

## Styles d'impression [printstyles]

Veillez à inclure des styles d'impression qui suppriment toute couleur d'arrière-plan, le défilement fixe et l'interface propre à l'aperçu uniquement. Marked vous offre deux façons de cibler l'impression et la sortie PDF.

### `@media print` [media-print]

Les règles CSS d'impression standard s'appliquent lors de l'impression depuis Marked ou lorsque l'export PDF utilise le média print :

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### La classe `.mkprinting` [the-mkprinting-class]

Lorsque Marked prépare un document pour l'**export PDF** ou l'**aperçu Impression/PDF** ({% kbd cmd P %}), il ajoute la classe `mkprinting` à la balise `<body>` (aux côtés de classes d'export telles que `bandw`, `breakAfterTOC`, et la classe `mkstyle--*` de votre style). Les thèmes intégrés de Marked utilisent cette classe pour la plupart des règles spécifiques à l'impression plutôt que de se reposer uniquement sur `@media print`.

L'export PDF charge souvent la WebView de rendu masquée avec le média **screen** (en particulier pour les styles personnalisés et les documents [Fountain](Fountain_for_Screenwriters.html)), donc les blocs `@media print` dans votre feuille de style peuvent **ne pas** s'appliquer à la sortie PDF. Les règles préfixées par `.mkprinting` s'appliquent toujours pendant l'export car ce sont des sélecteurs de classe ordinaires, pas des media queries.

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

Pour les styles qui doivent fonctionner à la fois pour l'impression navigateur **et** l'export PDF de Marked, dupliquez les règles critiques ou combinez les sélecteurs :

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Style personnalisé vs CSS additionnel.** Dans une feuille de style de Style personnalisé, écrivez `.mkprinting #wrapper …` comme indiqué ci-dessus. Dans le champ **CSS additionnel**, Marked réécrit les sélecteurs avant l'injection --- utilisez plutôt la forme qualifiée par le body :

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Consultez [Paramètres CSS additionnel](#additional-css-settings) pour savoir comment fonctionne la réécriture et pourquoi `.mkprinting #wrapper …` seul n'y correspond pas.

Lors du débogage de votre CSS d'impression personnalisé, ouvrez l'aperçu Impression/PDF ou exportez en PDF, puis utilisez [l'Inspecteur Web de Safari](#webkitinspector) pour inspecter le document --- le `<body>` aura la classe `mkprinting` tant que la mise en page d'impression est active.

La dissimulation des liens à l'impression est gérée en dehors du thème principal, ce qui permet aux utilisateurs de choisir de masquer les surlignages et soulignements de liens à l'impression. Tant que vous avez défini un style de base pour le texte, vous n'avez pas à vous en soucier.

Alors, lancez-vous. Convertissez votre thème de blog, créez un style d'impression redoutable pour les documents PDF, ou concevez l'aperçu parfait pour le style d'écriture que vous pratiquez. Si vous créez quelque chose de génial, [partagez-le avec la communauté](https://markedapp.com/styleshare/).

## Paramètres CSS additionnel [additional-css-settings]

Dans le {% prefspane Style %}, vous pouvez modifier le **CSS additionnel**. Ces règles sont **ajoutées à la suite du thème chargé**, quel qu'il soit. Il s'agit d'une superposition partielle délibérée, pas d'un thème complet. Si vous collez une feuille de style complète dans ce champ --- ou si vous importez cette même feuille partielle via le [Gestionnaire de styles](Custom_Styles.html) comme s'il s'agissait d'un thème --- tout ce que la feuille ne couvre pas restera sans style.

### Réécriture des sélecteurs [additional-css-selector-rewriting]

Marked réécrit les sélecteurs du CSS additionnel avant de les injecter (en tant que `body.mk-has-additional-css …`) afin que les règles restent circonscrites à l'aperçu :

- Une partie de sélecteur qui commence déjà par `body` ou `#wrapper` reçoit le préfixe `body.mk-has-additional-css`, les classes du body étant fusionnées plutôt qu'imbriquées.
- Toute autre partie de sélecteur est circonscrite sous `body.mk-has-additional-css #wrapper …`.
- Les classes de body en tête que Marked définit sur `<body>` --- notamment `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` et `.mkstyle--*` --- sont traitées comme `body` et fusionnées sur le sélecteur body plutôt qu'imbriquées sous `#wrapper`.

| Saisi dans CSS additionnel | Résultat |
| :-- | :-- |
| `#wrapper h2` | Correspond (correctement circonscrit) |
| `body.mkprinting #wrapper p` | Correspond pendant l'impression/PDF |
| `.mkprinting #wrapper p` | Ne correspond **pas** (nécessiterait un `#wrapper` imbriqué) |
| `:root { --x: 1; }` | Ne correspond **pas** (préférez `body` ou `#wrapper` pour les propriétés personnalisées) |

Pour les règles d'impression dans ce champ, préférez `body.mkprinting #wrapper …`. La même intention visuelle dans un fichier de Style personnalisé peut conserver la forme plus courte `.mkprinting #wrapper …`.

Il n'y a **aucune limite de taille et aucune vérification de validité CSS** sur le CSS additionnel. Marked stocke et injecte ce que vous saisissez ; un CSS invalide n'a simplement aucun effet dans l'aperçu.

### HTML et autres exports [additional-css-exports]

Le CSS additionnel s'applique dans l'aperçu en direct, l'aperçu Impression/PDF, l'export PDF, et l'**export HTML** lorsque les styles sont inclus --- le `<body>` exporté reçoit la classe `mk-has-additional-css` afin que les sélecteurs réécrits correspondent. DOCX, ODT et EPUB utilisent leurs propres chemins de style et n'appliquent pas le CSS additionnel de la même manière.

En utilisant une [spécificité élevée](#overridingspecificity), des requêtes `@media` pour l'impression et l'écran, et des sélecteurs `body.mkprinting` (dans ce champ) ou `.mkprinting` (dans les Styles personnalisés), vous pouvez contrôler pratiquement tous les aspects du style avec un peu de connaissance en CSS.

## Inspecteur WebKit [webkitinspector]

L'Inspecteur Web de Safari est le moyen le plus simple de voir exactement quel HTML et CSS Marked génère, et d'expérimenter avec les Styles personnalisés en direct.

### Activer le menu Développement dans Safari [enabling-the-develop-menu-in-safari]

1. Ouvrez Safari et choisissez {% appmenu Safari, Settings… %}.
2. Sélectionnez l'onglet **Avancées**.
3. Activez **Afficher les fonctions pour les développeurs Web** (ou **Afficher le menu Développement dans la barre des menus** sur les versions plus anciennes de macOS).

Une fois activé, un menu **Développement** apparaîtra dans la barre des menus de Safari.

![Menu Développement de Safari affichant les documents Marked][develop-menu]

### Inspecter un document Marked [inspecting-a-marked-document]

1. Avec une fenêtre d'aperçu ouverte dans Marked, passez à Safari.
2. Depuis la barre des menus, choisissez **Développement → _\<nom de votre Mac\>_ → Marked → _\<titre du document\>_**.
3. Safari ouvrira une fenêtre d'Inspecteur Web attachée à l'aperçu Marked sélectionné.

À partir de là, vous pouvez :

- Utiliser l'onglet **Éléments** pour inspecter le DOM à l'intérieur de la div `#wrapper` et voir quelles règles CSS sont appliquées.
- Survoler les éléments dans l'arborescence DOM pour les mettre en évidence dans la fenêtre Marked.
- Utiliser la barre latérale **Styles** pour ajuster les règles en direct, puis copier les extraits fonctionnels dans un Style personnalisé ou le **CSS additionnel**.
    - Après avoir modifié le CSS dans l'onglet Éléments, vous pouvez obtenir un résumé de vos modifications en sélectionnant l'onglet Modifications

	![Modifications][css-changes]
- Utiliser l'onglet **Console** pour exécuter du JavaScript sur l'aperçu en direct. L'ensemble de l'[API JavaScript de Marked](https://markedapp.com/help/jsapi/) est disponible dans cette console.
- Explorer d'autres onglets tels que **Réseau** lors du débogage des ressources chargées par votre document.

![Inspection d'un aperçu Marked avec l'Inspecteur Web de Safari][inspecting]

## Partager un CSS personnalisé [sharing-custom-css]

Utilisez {% appmenu Style, Share a Custom Style %} pour ouvrir l'application de partage dans votre navigateur web. Glissez votre CSS dans la zone de dépôt (ou cliquez pour le sélectionner sur le disque) et téléversez le CSS de votre Style personnalisé.

Les styles partagés doivent être approuvés par le développeur avant d'apparaître dans la galerie, vous ne verrez donc pas de résultats immédiats.

## Autres astuces [other-tips]

### Surcharger la spécificité [overridingspecificity]

Dans l'aperçu Marked, une classe de body basée sur le nom de fichier du style actuel est ajoutée. Si l'aperçu est réglé sur « Swiss », alors il y aura une classe sur la balise `<body>` appelée `mkstyle--swiss`. Si votre CSS personnalisé s'appelle MyCustom.css, alors la classe du body sera `mkstyle--mycustom`. Vous pouvez l'utiliser avant les règles définies dans les styles de base pour les surcharger. Pour obtenir une spécificité absolue dans une règle, utilisez également l'ID #wrapper de la div conteneur :

	.mkstyle--mycustom #wrapper p+p { ... }

### Style de la table des matières [table-of-contents-styling]

Si vous utilisez le jeton `<!--toc-->` pour [insérer une table des matières](Special_Syntax.html#tableofcontents), vous pouvez surcharger les paramètres des indicateurs de niveau de la Table des matières dans un Style personnalisé en utilisant « #wrapper » pour augmenter la spécificité :

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Cela ferait en sorte que tous les éléments de liste de la Table des matières utilisent une puce carrée au lieu de celle définie dans les Paramètres, lorsque votre Style personnalisé est actif.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
