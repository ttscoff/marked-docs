# <%= @title %>

Options du {% prefspane Processor %} :

![Paramètres : Processeur][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Traiter le Markdown avec

Processeur Markdown par défaut. Le processeur Discount est préféré par les utilisateurs de GitHub, MultiMarkdown est idéal pour les rédacteurs. Marked compense certaines différences de syntaxe. Voir __Aide → Référence Markdown__ pour plus d'informations.

Règles personnalisées
: Utilisez le bouton Règles personnalisées pour ouvrir l'éditeur de règles personnalisées, qui vous permet de déterminer des options de traitement et des transformations de document en fonction de critères. Voir la [documentation du processeur personnalisé](Custom_Processor.html) pour plus de détails.

Les nouveaux documents utilisent la personnalisation
: Sélectionnez préprocesseur et/ou processeur pour activer automatiquement le traitement des règles sur les nouveaux documents. Si vous utilisez les Règles personnalisées, vous voudrez probablement activer les deux.

### HTML

Générer des ID sur les titres
: Génère des ID d'en-tête basés sur le contenu des balises h1 à h6.

Utiliser des ID de note de bas de page aléatoires
: Génère des ID de note de bas de page aléatoires pour éviter les conflits lorsque plusieurs documents sont affichés sur une même page.

Traiter le Markdown à l'intérieur du HTML
: Par défaut, le Markdown à l'intérieur des balises HTML est généralement ignoré. Cette option force Marked à poursuivre le traitement à l'intérieur des éléments de bloc. Notez que certains balisages peuvent causer des problèmes.


### Rendu

Conserver les sauts de ligne dans les paragraphes
: Respecte les sauts de ligne dans le texte des paragraphes, en les remplaçant par des sauts forcés plutôt que de les fusionner avec la ligne précédente.

Afficher les cases à cocher GitHub
: Affiche `- [ ]` et `- [x]` pour créer des cases à cocher dans les listes. Les cases à cocher sont affichées pour l'aperçu mais ne sont pas fonctionnelles dans Marked.

\#Le texte est une balise
: Permet aux hashtags (`#` immédiatement suivi de texte sans espace) d'être interprétés comme des balises, pas des titres. Cette fonctionnalité est activée par défaut pour les utilisateurs de Bear.
: __Balises de style__ fait en sorte que les balises soient affichées avec un formatage en « capsule » pour les distinguer du texte. Lorsque cette option est activée, les balises peuvent être affichées/masquées via {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Le texte est une balise activé][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Afficher `==surlignage==` et `~~suppression~~`
: Si cette option est activée, alors le texte `==surlignage==` sera rendu sous forme de balise HTML `<mark>`, qui apparaîtra comme un surlignage jaune sauf modification par un Style. De plus, la syntaxe `~~suppression~~` sera rendue avec une balise `<del>`.

: Si __Convertir en CriticMarkup__ est activé, alors la syntaxe `==surlignage==` et `~~suppression~~` sera convertie en CriticMarkup, qui peut ensuite être affichée dans les vues originale, balisage et modifiée.

Afficher `~texte~` en soulignement
: Si cette option est activée, `~texte~` entouré de simples tildes sera affiché en souligné. Cela entre en conflit avec la syntaxe MultiMarkdown pour l'indice inférieur et est désactivé par défaut.
