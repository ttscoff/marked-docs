# <%= @title %>

Options du panneau de préférences {% prefspane Style %} :

![Paramètres : Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Mise en page et typographie [layout-and-typography]

Limiter la largeur du texte dans l'aperçu
: Définissez une largeur maximale pour le corps de l'aperçu à l'aide du curseur (en pixels).

Césure automatique dans les paragraphes
: Autorise la coupure automatique des mots par césure.

Empêcher les veuves dans les titres et paragraphes
: Force une espace insécable entre les deux derniers mots des titres et des paragraphes, afin d'éviter qu'un mot isolé ne passe seul à la ligne suivante.

Générer des guillemets et une ponctuation typographiquement corrects
: Utilise SmartyPants pour les guillemets typographiques, la conversion des points de suspension et d'autres fonctionnalités typographiques (MultiMarkdown).

Entourer les repères de notes de bas de page de crochets
: Si cette option est cochée, utilise le formatage MultiMarkdown par défaut pour les repères de notes de bas de page ([1]). Décochez pour retirer les crochets.

Activer le mode Plan pour les extensions
: Active automatiquement le mode Plan pour les fichiers dont l'extension est listée.

Utiliser le style APA
: Utilise une structure de plan au style APA plutôt que le format décimal par défaut.

Styliser les blocs de code verbatim comme de la poésie
: Si cette option est cochée, le code indenté par tabulation, délimité ou inclus est affiché comme de la poésie plutôt que comme un bloc de code (pas de coloration syntaxique, avec un style particulier selon le thème).

Autoriser les thèmes à faire retourner le texte à la ligne dans les blocs de code
: Si cette option est cochée, les thèmes sont autorisés à provoquer un retour à la ligne à l'intérieur des blocs `pre>code`. Si elle est décochée, le débordement horizontal donnera toujours lieu à un défilement.

Toujours retourner le code à la ligne
: Force le retour à la ligne dans les blocs de code, quel que soit le réglage du thème (remplace le comportement de retour à la ligne défini par le thème).

Détecter et styliser le texte RTL
: Détecte la langue de chaque élément du document et applique le style droite à gauche en conséquence.

### Thème [theme]

Gérer les styles
: Ouvre la fenêtre du [Gestionnaire de styles](Style_Manager.html). Ajoutez des fichiers CSS depuis votre disque pour qu'ils apparaissent dans les menus du sélecteur de style. Utilisez le bouton `Ajouter un nouveau style` ou glissez des fichiers CSS dans cette fenêtre. Glissez pour réorganiser, et utilisez les cases à cocher pour activer ou désactiver les styles.

Plus de thèmes
: Ouvre la galerie de thèmes en ligne pour parcourir et installer des styles supplémentaires.

Style par défaut
: Le style sélectionné ici sera chargé pour toutes les nouvelles fenêtres, sauf si [un style spécifique au document est indiqué dans les métadonnées](Per-Document_Settings.html) (par exemple, « Marked Style: Grump »).

Suivre les modifications du CSS
: Lorsque cette option est activée, Marked surveille le style actuel pour détecter les modifications sur le disque, ce qui facilite l'édition de styles personnalisés et le développement web.

CSS supplémentaire
: Le CSS ajouté ici sera inclus après la feuille de style normale, avec tous les thèmes. Vous pouvez notamment vous en servir pour remplacer des réglages de façon globale sans modifier les styles internes.
: Ceci s'applique à tous les documents et à tous les styles. Si vous souhaitez appliquer du CSS personnalisé à des documents selon certaines conditions, utilisez les Règles personnalisées dans {% prefspane Processor %}.

### Inclure des scripts [include-scripts]

Coloration syntaxique
: Active la [coloration syntaxique](Syntax_Highlighting.html) highlight.js pour les blocs de code. Sélectionnez un thème dans le menu déroulant.
: Si **Uniquement si le langage est spécifié** est coché, la coloration syntaxique ne s'appliquera qu'aux blocs de code délimités pour lesquels un langage est spécifié.

Activer MathJax
: Charge [MathJax](MathJax.html) pour l'affichage des équations MathML. Choisissez **Local** (intégré) ou **CDN** dans le menu déroulant.
: **Paquets supplémentaires** ouvre une feuille permettant d'inclure des paquets MathJax additionnels (par exemple Physique et Chimie).
: **Configuration avancée** ouvre une feuille pour une configuration MathJax personnalisée.

Activer KaTeX
: Charge [KaTeX](MathJax.html#katex) comme alternative à MathJax. Un seul des deux peut être sélectionné à la fois.

Numéroter les équations
: Le cas échéant, Marked ajoutera des numéros de figure aux équations rendues. Choisissez **Côté gauche** ou **Côté droit** pour la numérotation. Avec MathJax, vous pouvez choisir **AMS uniquement** pour ne numéroter que les équations AMS.

Mermaid
: Charge [mermaid.js](https://mermaid.js) depuis un CDN pour permettre la création de diagrammes au format Markdown. Le hook nécessaire pour rendre les diagrammes Mermaid à chaque mise à jour du document est inclus automatiquement.

Diagrammes en panoramique et zoom
: Lorsque des diagrammes Mermaid sont présents, activez le zoom avec {% kbd cmd %}-défilement et le panoramique en cliquant-glissant.
