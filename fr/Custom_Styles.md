# <%= @title %>

Visualisez vos documents *à votre* manière.

## Utiliser des styles personnalisés

![][img1]

[img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

La manière la plus simple d'explorer les styles personnalisés consiste à utiliser la [Galerie de styles personnalisés][2]. De là, vous pouvez parcourir les styles disponibles en action, les installer en un clic de bouton, et même [soumettre vos propres créations][6] pour inclusion.

Pour ajouter des feuilles de style personnalisées de votre disque local à Marked, utilisez le {% prefspane Style %}. De nouveaux styles seront ajoutés aux menus déroulants dans les paramètres de la fenêtre et sur chaque fenêtre, et seront nommés en fonction du nom de fichier de base du fichier CSS ajouté. Stockez vos fichiers CSS personnalisés dans un endroit sûr sur votre disque. S'ils se déplacent sur votre disque, ils seront supprimés de Marked jusqu'à ce que vous les ajoutiez à nouveau à partir du nouvel emplacement. C'est une bonne idée de fermer les documents ouverts et de supprimer le style à partir des paramètres avant de supprimer ou de renommer un fichier CSS utilisé par Marked. Cela ne cassera rien si vous ne le faites pas, mais cela évite une certaine confusion.

Ajoutez des styles personnalisés à l'aide du gestionnaire de styles avec le bouton Ajouter, ou en faisant glisser un ou plusieurs fichiers CSS sur le volet des paramètres.

## Gérer les styles avec le Style Manager

Le lancement du Style Manager vous offre un emplacement unique pour organiser tous les thèmes intégrés et personnalisés. Cliquez sur le bouton **Gérer les styles…** dans le volet {% prefspane Style %}, ou déposez simplement les fichiers CSS dans la fenêtre des préférences, Marked les importera, ouvrira le gestionnaire de styles et sélectionnera la ligne nouvellement ajoutée pour vous. Faire glisser des fichiers CSS directement dans la fenêtre Style Manager fonctionne également ; quand plusieurs fichiers sont déplacés, vous verrez la superposition se mettre à jour vers « Ajouter N styles personnalisés » pour qu'il soit clair que vous importez un lot.

![][img-style-manager]

Dans le gestionnaire de styles, vous trouverez un tableau triable qui mélange les éléments intégrés et personnalisés. Chaque ligne propose :

- Une case à cocher **Activé** qui ajoute/supprime immédiatement le style du menu Style, de la fenêtre contextuelle Style par défaut et des raccourcis clavier. Désactiver le style actif passe automatiquement à l'entrée disponible suivante.
- Une colonne **Nom** que vous pouvez modifier en ligne ; les changements persistent et se propagent à tous les menus. Cliquez sur le nom du style pour le modifier sur place.
- Une colonne **Source** qui indique Intégré, Personnalisé ou Dupliqué.
- Une pile **Actions** avec des boutons pour **Modifier** (ouvre le fichier CSS dans votre éditeur), **Dupliquer** (crée une copie et un nouveau fichier CSS sur le disque), **Révéler** (affiche le fichier dans le Finder) et **Supprimer** (avec des options pour supprimer la référence ou déplacer le fichier CSS vers la corbeille).

Les lignes sont réorganisées par glisser-déposer, et l'ordre déterminera le menu Style ainsi que les attributions de raccourcis `⌘/#`, afin que vous puissiez littéralement faire glisser les styles dans les emplacements que vous voulez. Vous pouvez également faire glisser des fichiers CSS externes vers des positions spécifiques ; l'indicateur de dépôt détermine où le nouveau style est inséré.

### Aperçu en direct

Le volet de droite contient un aperçu qui restitue le style sélectionné dans un document HTML complet avec un ensemble complet de titres, de listes, de tableaux, de blocs de code, etc. L'aperçu utilise le CSS réel sur le disque, de sorte que les modifications que vous effectuez dans votre éditeur externe sont mises à jour instantanément. Une case à cocher active l'aperçu du mode sombre.

Vous pouvez trouver des styles supplémentaires à utiliser (ou comme exemples pour créer le vôtre) [sur GitHub][1] (voir les [exemples][2] pour un rapide coup d'œil à ce qu'il y a). Voir [Écrire du CSS personnalisé][3] pour plus de détails et de conseils.

## CSS supplémentaire

Sous le {% prefspane Style %}, vous trouverez une option intitulée CSS supplémentaire avec un bouton intitulé « Modifier le CSS ». Cliquer sur ce bouton ouvre une fenêtre dans laquelle vous pouvez ajouter des règles CSS universelles qui seront appliquées à tous les styles. Notez que la spécificité des règles peut être importante lorsque vous remplacez certains styles par défaut de Marked. Le corps principal du document est enveloppé dans un div avec l'identifiant `#wrapper`. Préfixer un sélecteur avec ceci peut permettre des remplacements plus faciles, par exemple :

    #wrapper img { width: 100%; height: auto; }

Le CSS dans ce champ sera appliqué à chaque document, quel que soit le style qu'il utilise. Si vous souhaitez appliquer du CSS basé sur des correspondances conditionnelles, utilisez les actions Définir le style, Insérer un fichier CSS ou Insérer du CSS dans {% prefspane Processor %} Règles personnalisées.

## Impression et export PDF

Marked injecte un bloc `@media print` intégré (`mkprintstyles`) sur chaque aperçu. Il définit des valeurs par défaut telles qu'une base **10pt** sur `html`, `body` et `#wrapper` (ou la taille de **Taille de police personnalisée pour l'exportation/impression** dans {% prefspane Export %} lorsque cette option est activée), et normalise le texte des paragraphes avec `p { font-size: 1em; }` et `li p { font-size: 1em; }` afin que les règles affichées uniquement à l'écran comme `p { font-size: 1.1429em; }` ne gonflent pas le corps du texte dans les PDF et les sorties imprimées.

L'exportation PDF peut utiliser un support **impression** ou **écran** sur la WebView masquée utilisée pour la génération. Les thèmes intégrés utilisent généralement des supports imprimés ; les **styles personnalisés** et les documents [Fountain](Fountain_for_Screenwriters.html) utilisent souvent des supports d'écran, afin que la mise en page corresponde à l'aperçu. Cela signifie que les règles `@media print { ... }` ne sont pas toujours appliquées lors de l'exportation PDF.

Pour un style fiable en PDF et en aperçu avant impression, préfixez les sélecteurs avec la classe `mkprinting` que Marked ajoute à `<body>` lors de l'exportation (voir [Écrire du CSS personnalisé](Writing_Custom_CSS.html#printstyles) pour plus de détails et d'exemples). Vous pouvez utiliser `.mkprinting` seul, ou le combiner avec `@media print` lorsque vous avez besoin des deux chemins couverts.

Pour définir des tailles différentes des valeurs d'impression par défaut de Marked, ajoutez des règles explicites dans votre CSS personnalisé (ou en CSS supplémentaire). Utilisez `!important` lorsque vous avez besoin de remplacer les styles d'impression injectés par Marked, par exemple :

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}
```

Les règles sans `!important` peuvent perdre face aux règles ultérieures en `mkprintstyles` ou à d'autres sélecteurs non qualifiés dans votre feuille qui s'appliquent toujours en version imprimée. Mettre les ajustements d'impression uniquement dans les règles `@media print` et/ou `.mkprinting` (plutôt que uniquement dans les règles d'écran) rend le comportement de prévisualisation et d'exportation plus facile à comprendre.

## Surveiller les modifications CSS

Vous pouvez cocher une case dans la section Styles personnalisés du {% prefspane Style %} pour que Marked surveille le fichier CSS actif en plus du fichier Markdown que vous modifiez. Quand des modifications sont détectées sur l'un ou l'autre fichier, l'aperçu sera mis à jour. Ceci est utile pour modifier des styles personnalisés sans avoir à actualiser constamment, et peut également être utilisé pour des tâches simples de développement web.

Ceci est également utile pour certains travaux de conception web de base et d'expérimentation CSS (comme la création de styles personnalisés). Chargez un fichier Markdown contenant toutes les balises que vous souhaitez styliser, créez un style personnalisé, et observez l'aperçu en direct se modifier au fur et à mesure que vous le modifiez.

## Écrire du CSS personnalisé

Si vous êtes familier avec CSS, vous pouvez créer vos propres feuilles de style à utiliser dans Marked. Voir [Écrire du CSS personnalisé][3] pour plus de détails. Chaque fois que vous créez quelque chose de nouveau, pensez à [le soumettre][6] à la [galerie][2] pour le partager avec d'autres utilisateurs. Assurez-vous de couvrir les bases répertoriées dans le guide, et incluez le commentaire sur les métadonnées en haut.

### Styles personnalisés automatiques avec StyleStealer

Vous pouvez même générer automatiquement un style basé sur un site Web existant utilisant le [Style Stealer][4]. Cela vous permet de charger une page Web et de récupérer les styles calculés pour tous les principaux éléments trouvés dans Markdown, puis de l'enregistrer dans un style personnalisé.

![Style Stealer][stylestealer]

[stylestealer]: images/style-stealer-800.jpg @2x width=800


Gérez les styles personnalisés (renommer, réorganiser, dupliquer et supprimer) à partir du [Gestionnaire de styles](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
