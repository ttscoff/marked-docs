Options dans le {% prefspane Style %} :

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Mise en page et typographie [layout-and-typography]

Limiter la largeur du texte dans l'aperçu
: Définit une largeur maximale pour le corps de l'aperçu à l'aide du curseur (en pixels).

Coupure automatique des mots dans les paragraphes
: Autorise la coupure automatique des mots par césure.

Empêcher les veuves dans les titres et les paragraphes
: Force une espace insécable entre les deux derniers mots des titres et des paragraphes pour éviter qu'un mot isolé ne passe seul à la ligne.

Générer des guillemets et une ponctuation typographiquement corrects
: Utilise SmartyPants pour les guillemets typographiques, la conversion des points de suspension et d'autres fonctions typographiques (MultiMarkdown).

Entourer les marqueurs de notes de bas de page de crochets
: Si cette option est cochée, utilise le format MultiMarkdown par défaut pour les marqueurs de notes de bas de page ([1]). Décochez pour retirer les crochets.

Activer le Plan pour les extensions
: Active automatiquement le mode Plan pour les fichiers ayant les extensions listées.

Utiliser le style APA
: Utilise des plans au style APA au lieu du format décimal par défaut.

Styliser les blocs verbatim (code) comme de la poésie
: Si cette option est cochée, le code indenté par tabulation, en bloc ou inclus est affiché comme de la poésie plutôt que comme un bloc de code (pas de coloration syntaxique, avec une mise en forme spéciale selon le thème).

Autoriser les thèmes à faire un retour à la ligne dans les blocs de code
: Si cette option est cochée, les thèmes sont autorisés à provoquer un retour à la ligne dans les blocs `pre>code`. Si elle est décochée, le débordement horizontal donnera toujours lieu à un défilement.

Toujours faire un retour à la ligne dans le code
: Force les blocs de code à revenir à la ligne quels que soient les réglages du thème (remplace le comportement de retour à la ligne défini par le thème).

Détecter et styliser le texte RTL
: Détecte la langue de chaque élément du document et applique le style approprié pour l'écriture de droite à gauche.

### Thème [theme]

Gérer les styles
: Ouvre la fenêtre du [Gestionnaire de styles](Style_Manager.html). Ajoutez des fichiers CSS depuis votre disque pour les faire apparaître dans les menus du sélecteur de style. Utilisez le bouton `Add New Style` ou faites glisser des fichiers CSS vers cette fenêtre. Faites glisser pour réorganiser, et utilisez les cases à cocher pour activer ou désactiver les styles.

Plus de thèmes
: Ouvre la galerie de thèmes en ligne pour parcourir et installer des styles supplémentaires.

Style par défaut
: Le style sélectionné ici sera chargé pour toutes les nouvelles fenêtres, à moins qu'un [style spécifique au document ne soit indiqué dans les métadonnées](Per-Document_Settings.html) (par exemple « Marked Style: Grump »).

Suivre les modifications du CSS
: Lorsque cette option est activée, Marked surveille les modifications sur le disque du style actuel, ce qui facilite l'édition de styles personnalisés et le développement web.

CSS additionnel
: Le CSS ajouté ici est ajouté à la suite de la feuille de style normale pour chaque thème. Il s'agit d'une superposition partielle, pas d'un thème complet de remplacement.
: Marked réécrit les sélecteurs de ce champ (par exemple, les règles d'impression doivent utiliser `body.mkprinting #wrapper …`). Il n'y a aucune limite de taille ni contrôle de validité --- voir [Créer du CSS personnalisé](Writing_Custom_CSS.html#additional-css-settings).
: Cela s'applique à tous les documents et à tous les styles, y compris à l'export HTML lorsque les styles sont inclus. Si vous souhaitez appliquer du CSS personnalisé aux documents selon certaines conditions, utilisez les Règles personnalisées sous {% prefspane Processor %}.

### Inclure des scripts [include-scripts]

Coloration syntaxique
: Active la [coloration syntaxique](Syntax_Highlighting.html) highlight.js pour les blocs de code. Sélectionnez un thème dans le menu déroulant.
: Si **Uniquement si le langage est spécifié** est coché, la coloration syntaxique ne s'appliquera qu'aux blocs de code en clôture avec un langage spécifié.

Activer MathJax
: Charge [MathJax](MathJax.html) pour afficher les équations MathML. Choisissez **Local** (intégré) ou **CDN** dans le menu déroulant.
: **Paquets additionnels** ouvre une feuille pour inclure des paquets MathJax supplémentaires (par exemple Physics et Chemistry).
: **Configuration avancée** ouvre une feuille pour une configuration MathJax personnalisée.

Activer KaTeX
: Charge [KaTeX](MathJax.html#katex) comme alternative à MathJax. Un seul des deux peut être sélectionné à la fois.

Numéroter les équations
: Le cas échéant, Marked ajoute des numéros de figure aux équations affichées. Choisissez **Côté gauche** ou **Côté droit** pour la numérotation. Si vous utilisez MathJax, vous pouvez choisir **AMS uniquement** pour ne numéroter que les équations AMS.

Mermaid
: Charge [mermaid.js](https://mermaid.js) depuis un CDN pour permettre la création de diagrammes au style Markdown. Le hook nécessaire pour afficher les diagrammes Mermaid à chaque mise à jour du document est inclus automatiquement.

Zoomer et déplacer les diagrammes
: Lorsque des diagrammes Mermaid sont présents, active le zoom avec {% kbd cmd %}-défilement et le déplacement en cliquant-glissant.
