# <%= @title %>

Marked fournit des valeurs par défaut pour améliorer la typographie et la mise en page d'exportation, ainsi qu'offrir un contrôle limité sur les options si vous avez besoin de plus de personnalisation.

## Typographie

### Césure et veuves

L'option _Césure automatique dans les paragraphes_ permet à Marked de déterminer où une ligne serait mieux coupée pour améliorer l'aspect du bord irrégulier d'un paragraphe. Ceci est particulièrement utile lorsque vous utilisez un style avec un alignement justifié, mais peut également améliorer le flux de lecture dans les paragraphes plus longs.

L'option _Empêcher les veuves dans les titres et les paragraphes_, si elle est activée, forcera les sauts dans les titres et les paragraphes pour empêcher des mots simples et courts de se retrouver seuls sur une ligne.

Marked connecte automatiquement les titres à l'élément suivant, pour éviter les titres orphelins lors de l'exportation vers un format paginé (PDF, impression).

### Signes de ponctuation

Si votre processeur est réglé sur MultiMarkdown, vous aurez la possibilité d'activer ou de désactiver la « ponctuation intelligente » à l'aide de l'option _Générer des guillemets et une ponctuation typographiquement corrects_. Si cette option est activée, les guillemets doubles et simples appariés seront transformés en guillemets « bouclés », les apostrophes seront remplacées par des symboles typographiquement corrects et d'autres ajustements automatiques seront effectués.

### Marqueurs de notes de bas de page

Dans la section Mise en page et typographie du {% prefspane Style %}, _Entourer les marqueurs de note de bas de page avec des crochets_ est activé par défaut lors de l'utilisation du processeur MultiMarkdown et crée des marqueurs de note de bas de page dans le document qui sont entourés de crochets (par exemple "[1]"). Pour désactiver la création des crochets, décochez cette option.

## Mode Plan

Le mode Plan affichera tout fichier contenant une série hiérarchique d'en-têtes sous forme d'APA ou de plan décimal. La valeur par défaut est le style APA, mais cela peut être désactivé.

Dans le {% prefspane Style %} sous « Mise en page et typographie », vous pouvez ajouter des extensions de nom de fichier pour lesquelles le mode Plan est automatiquement activé. Ceci est particulièrement utile pour OPML et les fichiers de cartes mentales pris en charge (tels que iThoughtsX et MindNode). L'extension doit être uniquement la partie alphanumérique du nom de fichier apparaissant après le dernier point.

Basculez vers le mode de plan par défaut avec la case à cocher _Utiliser le style APA_. Cela peut être activé temporairement à partir du menu Action d'une fenêtre de document.


## Poésie

L'option _Style verbatim blocs de code en poésie_ dans le {% prefspane Style %} entraînera l'affichage des blocs indentés de 4 espaces ou plus en utilisant le style « poésie » du thème. Il s'agit généralement d'une section en italique et sans syntaxe.

Les sauts de ligne sont conservés par défaut dans ces blocs, ce qui constitue un moyen simple d'incorporer de la poésie et des sections lyriques dans un document qui n'a pas besoin d'autres blocs de code.

> Ce paramètre ajoute une classe de corps « poésie » qui peut être utilisée dans des thèmes personnalisés pour styliser les blocs de code et d'autres éléments lorsque le « mode poésie » est activé.

## Emballage du bloc de code

L'option _Autoriser les thèmes à envelopper le texte dans des blocs de code_ permet au style d'aperçu de déterminer comment formater les blocs de code. La désactivation de cette option force tous les blocs de code à faire défiler le débordement horizontal plutôt que de l'envelopper, quel que soit le style d'aperçu actuel.

## Utilisation en plein écran

Lorsque vous utilisez Marked en mode plein écran (Contrôle-Commande-F), vous souhaiterez peut-être limiter la largeur du texte affiché pour créer une colonne centrée de contenu lisible. La case à cocher _Limiter la largeur du texte dans l'aperçu_ activera un curseur avec lequel vous pourrez définir la largeur maximale du contenu affiché. Cela affecte également l'affichage non plein écran.
