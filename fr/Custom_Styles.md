# <%= @title %>

Consultez vos documents à *votre* façon.

## Utilisation des styles personnalisés [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Le moyen le plus simple d'explorer les styles personnalisés est de passer par la
[Galerie de styles personnalisés][2]. Vous pouvez y parcourir les
styles disponibles en action, les installer d'un simple clic,
et même [soumettre vos propres créations][6] pour
qu'elles y figurent.

Pour ajouter des feuilles de style personnalisées depuis votre disque local à Marked,
utilisez {% prefspane Style %}. Les nouveaux styles seront ajoutés aux
menus déroulants dans les paramètres de fenêtre et sur chaque fenêtre,
et seront nommés d'après le nom de base du fichier CSS
ajouté. Conservez vos fichiers CSS personnalisés dans un emplacement sûr sur votre
disque. S'ils sont déplacés, ils seront retirés de
Marked jusqu'à ce que vous les ajoutiez à nouveau depuis leur nouvel emplacement. Il est
conseillé de fermer les documents ouverts et de retirer le style
des Paramètres avant de supprimer ou de renommer un fichier CSS utilisé par
Marked. Cela ne cassera rien si vous ne le faites pas, mais cela évite
toute confusion.

Ajoutez des styles personnalisés à l'aide du Gestionnaire de styles avec le bouton Ajouter, ou en
faisant glisser un ou plusieurs fichiers CSS sur le panneau des Paramètres.

## Gérer les styles avec le Gestionnaire de styles [managing-styles-with-the-style-manager]

Le Gestionnaire de styles vous offre un endroit unique pour organiser tous les
thèmes intégrés et personnalisés. Cliquez sur le bouton **Gérer les styles…** dans le panneau {% prefspane Style %},
ou déposez simplement des fichiers CSS sur la fenêtre des préférences --- Marked les
importera, ouvrira le Gestionnaire de styles et sélectionnera pour vous la nouvelle
ligne ajoutée. Faire glisser des fichiers CSS directement sur la fenêtre du Gestionnaire de styles
fonctionne également ; lorsque plusieurs fichiers
sont glissés, l'overlay affiche « Ajouter N styles personnalisés » afin qu'il soit clair
que vous importez un lot.

![][img-style-manager]

Dans le Gestionnaire de styles, vous trouverez un tableau triable qui mélange styles
intégrés et personnalisés. Chaque ligne propose :

- Une case à cocher **Activé** qui ajoute/retire immédiatement le style du menu
  Style, du menu local Style par défaut et des raccourcis clavier. Désactiver le style
  actuellement actif bascule automatiquement vers l'entrée disponible suivante.
- Une colonne **Nom** modifiable en ligne ; les modifications persistent et se propagent à
  tous les menus. Cliquez sur le nom du style pour le modifier directement.
- Une colonne **Source** qui indique Intégré, Personnalisé ou Dupliqué.
- Une pile **Actions** avec des boutons pour **Modifier** (ouvre le fichier CSS dans votre
  éditeur), **Dupliquer** (crée une copie et un nouveau fichier CSS sur le disque), **Afficher**
  (montre le fichier dans le Finder), et **Supprimer** (avec des options pour retirer la référence ou
  déplacer le fichier CSS vers la Corbeille).

Les lignes se réorganisent par glisser-déposer, et l'ordre détermine le menu Style ainsi que
les attributions de raccourci `⌘/#`, vous pouvez donc littéralement faire glisser les styles vers les
emplacements souhaités. Vous pouvez également glisser des fichiers CSS externes vers des positions
spécifiques ; l'indicateur de dépôt détermine où le nouveau style sera inséré.

### Aperçu en direct [live-preview]

Le panneau de droite contient un aperçu qui affiche le style sélectionné
dans un document HTML complet comportant un ensemble varié de titres, listes, tableaux, blocs de code, etc. L'
aperçu utilise le CSS réel présent sur le disque, de sorte que les modifications que vous apportez dans votre éditeur externe se mettent à jour instantanément. Une case à cocher permet de basculer l'aperçu en Mode sombre.

Vous trouverez des styles supplémentaires à utiliser (ou comme exemples pour
créer les vôtres) [sur GitHub][1] (voir les [exemples][2] pour
un rapide aperçu de ce qui s'y trouve). Consultez [Créer un CSS personnalisé][3]
pour plus de détails et de conseils.

## CSS supplémentaire [additional-css]

Sous {% prefspane Style %}, vous trouverez une option
intitulée CSS supplémentaire avec un bouton nommé « Modifier le CSS ».
En cliquant sur ce bouton, une fenêtre s'ouvre où vous pouvez ajouter
des règles CSS universelles qui seront appliquées à tous les styles. Notez
que la spécificité des règles peut avoir de l'importance lorsqu'il s'agit de
remplacer certains styles par défaut de Marked. Le corps principal
du document est encapsulé dans une div avec l'id « #wrapper ».
Préfixer un sélecteur avec celui-ci peut faciliter les
remplacements, par exemple :

    #wrapper img { width: 100%; height: auto; }

Le CSS dans ce champ est **ajouté au thème actif**. Ce n'est pas un
substitut à un véritable style personnalisé : une feuille de style écrite uniquement pour ce
champ est volontairement partielle, et la charger via le Gestionnaire de styles en tant que
thème laisserait tout ce qu'elle ne couvre pas sans mise en forme.

Marked **réécrit** les sélecteurs du CSS supplémentaire avant l'injection. Les classes
de body en tête, comme `.mkprinting`, sont fusionnées sur `body` plutôt que
imbriquées sous `#wrapper`, les règles d'impression dans ce champ doivent donc utiliser
`body.mkprinting #wrapper …` (voir [Créer un CSS
personnalisé](Writing_Custom_CSS.html#additional-css-settings) pour l'ensemble des règles
de réécriture). Il n'y a aucune limite de taille ni contrôle de validité sur ce champ
--- un CSS invalide n'a simplement aucun effet.

Le CSS de ce champ sera appliqué à chaque document, quel
que soit le style utilisé --- y compris lors de l'export HTML lorsque les styles sont
inclus. Si vous souhaitez appliquer un CSS personnalisé
selon des correspondances conditionnelles, utilisez les actions Définir le style, Insérer
un fichier CSS ou Insérer du CSS dans les {% prefspane Processor %}
Règles personnalisées.

## Export en impression et PDF [print-and-pdf-export]

Marked injecte un bloc `@media print` intégré (`mkprintstyles`) dans chaque
aperçu. Il définit des valeurs par défaut telles qu'une base de **10 pt** sur `html`, `body`, et
`#wrapper` (ou la taille définie par **Taille de police personnalisée pour l'export/impression** dans
{% prefspane Export %} lorsque cette option est activée), et normalise le texte des
paragraphes avec `p { font-size: 1em; }` et `li p { font-size: 1em; }` afin que
des règles réservées à l'écran comme `p { font-size: 1.1429em; }` n'agrandissent pas le corps du texte
dans les PDF et les documents imprimés.

L'export PDF peut utiliser le média **print** ou **screen** sur la WebView masquée utilisée pour
la génération. Les thèmes intégrés utilisent généralement le média print ; les **styles personnalisés** et
les documents [Fountain](Fountain_for_Screenwriters.html) utilisent souvent le média screen afin que la
mise en page corresponde à l'aperçu. Cela signifie que les règles `@media print { ... }` ne sont pas
toujours appliquées lors de l'export PDF.

Pour une mise en forme fiable en PDF et en Aperçu impression/PDF, préfixez les sélecteurs avec la
classe `mkprinting` que Marked ajoute à `<body>` pendant l'export (voir [Créer un CSS
personnalisé](Writing_Custom_CSS.html#printstyles) pour plus de détails et d'exemples). Dans un
fichier de **style personnalisé**, vous pouvez utiliser `.mkprinting` seul. Dans le **CSS
supplémentaire**, utilisez la forme qualifiée par le body `body.mkprinting #wrapper …` car ce champ
réécrit les sélecteurs. Vous pouvez aussi combiner l'une ou l'autre forme avec `@media print` lorsque
vous devez couvrir les deux cas.

Pour définir des tailles différentes des valeurs d'impression par défaut de Marked, ajoutez des règles explicites dans
votre CSS personnalisé (ou dans le CSS supplémentaire). Utilisez `!important` lorsque vous devez
remplacer les styles d'impression injectés par Marked --- par exemple :

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

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Les règles sans `!important` peuvent être supplantées par des règles ultérieures dans `mkprintstyles` ou par
d'autres sélecteurs non qualifiés de votre feuille de style qui s'appliquent encore à l'impression. Placer
les ajustements réservés à l'impression dans `@media print` et/ou dans des règles `.mkprinting` / `body.mkprinting`
(plutôt que uniquement dans des règles réservées à l'écran) facilite la compréhension du
comportement de l'aperçu et de l'export.

## Surveillance des modifications CSS [watching-css-changes]

Vous pouvez cocher une case dans la section Styles personnalisés des {% prefspane Style %}
pour que Marked surveille le fichier CSS actif
en plus du fichier Markdown que vous modifiez. Lorsque des
modifications sont détectées sur l'un ou l'autre fichier, l'aperçu se
met à jour. Ceci est utile pour modifier des styles personnalisés sans
avoir à actualiser constamment, et peut aussi servir pour des tâches simples
de développement web.

Cela est également utile pour certains travaux de base de conception web et
d'expérimentation CSS (comme la création de styles personnalisés). Chargez un
fichier Markdown contenant tout le balisage que vous souhaitez styliser,
créez un style personnalisé, et observez l'aperçu se mettre à jour en direct
pendant que vous le modifiez.

## Créer un CSS personnalisé [writing-custom-css]

Si vous connaissez bien le CSS, vous pouvez créer vos propres feuilles de
style pour Marked. Consultez [Créer un CSS personnalisé][3] pour
plus de détails. Chaque fois que vous créez quelque chose de nouveau, pensez à
[le soumettre][6] à la [galerie][2] pour le partager avec les autres
utilisateurs. Veillez à couvrir les points essentiels indiqués dans le guide, et
à inclure le commentaire de métadonnées en haut du fichier.

### Styles personnalisés automatiques avec StyleStealer [automatic-custom-styles-with-stylestealer]

Vous pouvez même générer automatiquement un style à partir d'un
site web existant grâce au [Style Stealer][4]. Cela vous permet de charger une page web et de récupérer les styles calculés pour tous les éléments principaux présents dans Markdown, puis de les enregistrer sous forme de style personnalisé.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Gérez les styles personnalisés (renommer, réordonner, dupliquer et supprimer) depuis le [Gestionnaire de styles](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
