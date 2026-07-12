# <%= @title %>

Options du panneau de préférences {% prefspane Processor %} :

![Paramètres : Processeur][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Traiter le Markdown avec

Processeur Markdown par défaut. Le processeur CommonMark est préférable pour les utilisateurs de GitHub, MultiMarkdown est idéal pour les rédacteurs, et Discount et Kramdown ont des usages spécialisés. Marked compense certaines différences de syntaxe entre eux. Voir __Aide->Référence Markdown__ pour plus d'informations.

Règles personnalisées
: Cliquez sur le bouton Règles personnalisées pour ouvrir l'éditeur de règles, où vous pouvez définir différents processeurs et transformations de document à exécuter selon des critères de correspondance. Voir [Processeur personnalisé](Custom_Processor.html) pour plus de détails.

Les nouveaux documents utilisent les règles personnalisées
: Lorsque cette option est cochée, les nouveaux documents utilisent automatiquement le **préprocesseur** et/ou le **processeur** enregistrés dans les règles personnalisées, sans configuration à refaire pour chaque document.

Accès complet au disque
: Cliquez sur **Autoriser** pour accorder à Marked la permission de lire des fichiers en dehors de son bac à sable lors de l'utilisation de processeurs personnalisés ou d'autres fonctionnalités nécessitant un accès étendu aux fichiers.

Pour explorer les différences entre les processeurs, consultez le [Markdown Dingus](Markdown_Dingus.html).

### HTML

Générer des ID sur les titres
: Génère des ID d'en-tête à partir du contenu des balises h1 à h6.

Utiliser des ID de notes de bas de page aléatoires
: Génère des ID de notes de bas de page aléatoires pour éviter les conflits lorsque plusieurs documents sont affichés sur une même page.

Traiter le Markdown à l'intérieur du HTML
: Par défaut, le Markdown à l'intérieur de balises HTML est généralement ignoré. Cette option force Marked à continuer de le traiter au sein des éléments de bloc. Notez que certaines balises peuvent poser problème.

### Rendu

Conserver les sauts de ligne dans les paragraphes
: Respecte les sauts de ligne dans le texte des paragraphes, en les remplaçant par des sauts forcés plutôt qu'en les concaténant à la ligne précédente.

Rendre les cases à cocher GitHub
: Rend `- [ ]` et `- [x]` pour créer des cases à cocher dans les listes. Les cases à cocher sont affichées dans l'aperçu mais ne sont pas fonctionnelles dans Marked.

Rendre les émojis GitHub :emoji:
: Rend les codes courts `:nom:` sous forme d'émojis façon GitHub dans l'aperçu.

\#Le texte est une balise
: Permet d'interpréter les hashtags (un `#` immédiatement suivi de texte, sans espace) comme des balises plutôt que comme des titres. Cette fonctionnalité est activée par défaut pour les utilisateurs de Bear.

Balises de style
: Lorsque **#Le texte est une balise** est activé, affiche les balises reconnues avec un style en capsule. Les balises peuvent être affichées ou masquées depuis {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Le texte est une balise activé][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Rendre `==surlignage==` et `~~suppression~~`
: Si cette option est activée, le texte `==surlignage==` sera rendu avec une balise HTML `<mark>`, qui apparaîtra en surbrillance jaune sauf modification par un style. De plus, la syntaxe `~~suppression~~` sera rendue avec une balise `<del>`.

: Si __Rendre en CriticMarkup__ est activé, la syntaxe `==surlignage==` et `~~suppression~~` sera convertie en CriticMarkup, qui peut alors être affichée dans les vues originale, balisée et éditée.

Rendre `~texte~` comme du texte souligné
: Si cette option est activée, `~texte~` entouré de tildes simples sera affiché souligné. Cela entre en conflit avec la syntaxe MultiMarkdown pour l'indice, et est désactivé par défaut.
