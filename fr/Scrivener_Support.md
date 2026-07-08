# <%= @title %>

Utilisez ensemble vos deux outils d'écriture préférés.

> Marked peut toujours lire les fichiers Scrivener 2.0, mais le développement se concentrera sur la version 3 à partir de Marked 2.5.11.

## Notions de base de Scrivener 3.0

Faites glisser un projet Scrivener (.scriv) vers Marked et il sera compilé et prévisualisé. Si vous choisissez l'option d'ouvrir les fichiers .scriv dans Scrivener (ci-dessus), Marked lancera également Scrivener lorsque vous glisserez le fichier vers Marked.

Comme pour les autres documents, les modifications des fichiers Scrivener sont mises à jour en direct à l'enregistrement. De plus, lorsqu'un document Scrivener est au premier plan dans Marked, {% kbd cmd E %} l'ouvrira dans Scrivener pour vous.

## Filtrer les documents du classeur

Lorsque vous ouvrez un projet Scrivener dans Marked, le contenu de l'aperçu est construit uniquement à partir des documents du classeur que vous sélectionnez. Le filtrage est toujours actif pour les fichiers `.scriv` ; le panneau de filtre est simplement un moyen pratique de modifier ce qui est inclus.

Ouvrez le panneau depuis **Relecture > Filtrer les documents Scrivener** ({% kbd opt-cmd-f %}). L'élément de menu affiche une coche tant que le panneau est visible. Fermer le panneau ne désactive pas le filtrage ni ne réinitialise vos sélections.

Le panneau de filtre liste les sections du classeur de votre projet (Manuscrit, Recherche, et les autres classeurs de premier niveau sauf Corbeille). Chaque section est réduite par défaut. Développez une section pour voir ses documents et dossiers sous forme de plan :

- Cochez ou décochez n'importe quel **document texte** pour l'inclure ou l'exclure de l'aperçu.
- Cliquez sur une ligne de **dossier** pour sélectionner ou désélectionner tous ses descendants. Un tiret dans la case à cocher signifie que seule une partie des descendants est sélectionnée.
- Les lignes dont l'option **Inclure dans la compilation** est désactivée dans Scrivener apparaissent grisées, mais vous pouvez toujours les cocher pour les prévisualiser dans Marked.
- Les **images, PDF et autres éléments non textuels** du classeur apparaissent dans la liste mais ne peuvent pas être sélectionnés.
- Les fichiers **RTF manquants** apparaissent quand même ; si vous ajoutez du contenu dans Scrivener pendant que Marked est ouvert, l'aperçu se met à jour à l'enregistrement comme pour toute autre modification Scrivener.

Utilisez **Tout sélectionner** et **Tout désélectionner** en haut du panneau pour l'ensemble du projet. Chaque en-tête de section possède des boutons **Tout** et **Aucun** pour cette section uniquement. **Tout désélectionner** signifie qu'aucun document n'est coché.

Si rien n'est sélectionné, l'aperçu affiche un court message avec un lien pour ouvrir le panneau de filtre (`x-marked://scrivenerfilter`). Vous pouvez utiliser cette URL dans des scripts ou d'autres applications pour faire apparaître le panneau du document Scrivener au premier plan dans Marked.

Vos sélections de cases à cocher sont enregistrées par projet Scrivener (grâce à l'identifiant du projet dans le fichier `.scrivx`) et restaurées la prochaine fois que vous ouvrez ce projet dans Marked. La première fois que vous ouvrez un projet, Marked ne sélectionne que les documents du classeur **Manuscrit** dont l'indicateur **Inclure dans la compilation** est Oui (ou non défini, ce que Scrivener traite comme Oui). Recherche et les autres classeurs démarrent décochés ; les éléments du Manuscrit exclus de la compilation démarrent décochés mais restent sélectionnables dans la liste.

Les projets Scrivener 2 n'affichent que le classeur **Manuscrit** dans le panneau de filtre. Les projets Scrivener 3 incluent tous les classeurs sauf la Corbeille.

Le panneau de filtre peut rester ouvert en parallèle d'autres outils comme **Visualiser la répétition des mots**. Modifier une case à cocher recompile l'aperçu après un court délai ; si un projet volumineux est encore en cours de compilation, Marked annule l'importation en cours et recommence avec votre nouvelle sélection.

## Titres Markdown à partir des titres Scrivener

Marked peut également créer pour vous des titres Markdown hiérarchiques basés sur les pages de votre fichier Scrivener. Pour activer cela, cochez simplement l'option indiquée ci-dessus.

## Métadonnées MultiMarkdown

Si le premier document de votre dossier Manuscrit est nommé « metadata », il sera traité comme des métadonnées MultiMarkdown au début du document d'aperçu. Aucun titre ne sera inséré pour cette section, quel que soit le paramètre « Titres Markdown à partir des titres Scrivener » (décrit ci-dessus), ce qui permet au processeur MultiMarkdown de le lire comme des métadonnées et d'autoriser les remplacements et options d'exportation en conséquence.

Vous pouvez formater ce fichier en YAML si votre processeur est de ceux qui gèrent le YAML.

Si vous n'utilisez pas de document `metadata`, Marked peut également ajouter au début des métadonnées MultiMarkdown à partir des paramètres de compilation de votre projet (`Settings/compile.xml`), en utilisant les mêmes champs **Title** et **Author** que Scrivener exporterait vers MultiMarkdown. Cette option est activée par défaut (clé de préférence `scrivenerCompileMetadata`). Les champs de métadonnées personnalisés ne sont inclus que lorsqu'ils apparaissent dans les paramètres de compilation **MMD Metadata** du projet, pas à partir des champs personnalisés par document.

## Liens

Pour les liens externes (HTTP), vous pouvez utiliser soit la syntaxe Markdown, soit le format de lien de Scrivener. Marked convertira le format Scrivener en Markdown avant le traitement.

## Commentaires

Marked peut traiter les commentaires et notes de bas de page créés en ligne dans le document.

## Tableaux

Marked peut convertir les tableaux Scrivener basiques. Si vous souhaitez inclure un tableau dans votre sortie, il est toutefois préférable de le faire au [format de tableau MultiMarkdown](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (Une application appelée [TableFlip](http://tableflipapp.com/) peut simplifier grandement leur création.)

## Fonctionnalités Scrivener supplémentaires

En plus des fonctionnalités de base de compilation et d'aperçu, Marked prend également en charge certaines conventions propres à Scrivener. Tout d'abord, dans votre document Scrivener, vous pouvez utiliser « Préserver le formatage » en ligne ou sur un bloc de texte autonome, et cela sera converti en blocs de code dans l'aperçu.

Marked lit également les notes de bas de page _en ligne_ de Scrivener. Si vous saisissez une note de bas de page à l'intérieur ou à la fin d'un paragraphe, elle sera convertie en note de bas de page MultiMarkdown dans l'aperçu.

## Utiliser des images dans votre document Scrivener

Les images peuvent être intégrées dans le document Scrivener, ou référencées avec la syntaxe d'image Markdown. La version Markdown d'une balise d'image est `![texte alternatif](chemin/vers/image.ext "titre/description facultatif")`. Le format de référence peut également être utilisé :

    ![texte alternatif][img1]

    [img1]: /chemin/vers/image.ext "description facultative"

Le chemin de base pour la sortie HTML dans l'aperçu sera défini sur le dossier contenant le document Scrivener. Ainsi, placer des images dans le même dossier que le document de travail permettra d'y accéder directement. Si votre document Scrivener se trouve dans `~/Desktop/TestDoc.scriv`, et que vous avez une image appelée « testimage.png » dans `~/Desktop/testimage.png`, vous pouvez ajouter l'image à votre document en utilisant :

    ![Image de test](testimage.png)

Les chemins relatifs basés sur le dossier parent du document fonctionneront, et les chemins absolus permettront d'accéder à des images n'importe où, mais pourraient être moins portables pour la sortie HTML.

## Remarque sur la sécurité

Un dossier de cache sera créé dans ~/Library/Application Support/Marked lorsque vous ouvrirez votre fichier .scriv dans Marked. Ce n'est pas un dossier protégé, donc si votre document original se trouve sur un disque chiffré ou autrement protégé, notez que son contenu sera non chiffré dans le cache. Pour une protection limitée, vous pouvez faire en sorte que ce cache n'apparaisse pas dans Spotlight en ajoutant ~/Library/Application Support/Marked à vos paramètres de confidentialité dans Spotlight.

Voir [Prise en charge d'applications supplémentaires](Additional_Application_Support.html) pour l'aperçu du presse-papiers, les liens wiki, le scripting, et la liste complète des guides par application.
