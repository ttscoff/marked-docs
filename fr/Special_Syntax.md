# <%= @title %>

## Callouts

## Bear/Obsidian ##

Marked prend en charge les callouts avec la syntaxe utilisée par Obsidian et Bear, qui est une citation en bloc au format spécial :

	> [!NOTE] Titre de la note
	> Texte additionnel

Le « NOTE » dans `[!NOTE]` n'est pas sensible à la casse. Il peut s'agir de l'un des mots-clés suivants :

- NOTE
- ABSTRACT, SUMMARY, TLDR
- INFO
- TODO
- TIP, HINT, IMPORTANT
- SUCCESS, CHECK, DONE
- QUESTION, HELP, FAQ
- WARNING, CAUTION, ATTENTION
- FAILURE, FAIL, MISSING
- DANGER, ERROR
- BUG
- EXAMPLE
- QUOTE, CITE

Ces mots-clés créent des blocs au style spécifique.

Vous pouvez utiliser un `+` ou un `-` pour rendre le callout repliable. Un signe plus (`+`) signifie que le callout est repliable mais ouvert par défaut. Un signe moins (`-`) signifie que le callout est repliable mais fermé par défaut.

  ![Callouts dans Marked][callouts]

[callouts]: images/callouts-800.jpg @2x width=800

### Xcode Playground ###

Lors de la prévisualisation de fichiers Xcode Playground, Marked prend en charge la syntaxe native des callouts Xcode Playground :

	- Attention: Titre facultatif
	Le contenu du callout se place ici.

Le type de callout (par exemple, « Attention ») n'est pas sensible à la casse et peut être l'un des types de callout Xcode Playground suivants :

- **Attention** - Stylé comme un callout d'information
- **Author** - Callout de métadonnées
- **Authors** - Callout de métadonnées
- **Bug** - Callout d'erreur/de danger
- **Complexity** - Callout de type note
- **Copyright** - Callout de métadonnées
- **Custom Callout** - Callout de type exemple
- **Date** - Callout de métadonnées
- **Example** - Callout d'exemple
- **Experiment** - Callout de type astuce
- **Important** - Callout de type information
- **Invariant** - Callout de type note
- **Note** - Callout de note
- **Precondition** - Callout de type note
- **Postcondition** - Callout de type note
- **Remark** - Callout de type note
- **Requires** - Callout de type note
- **See Also** - Callout de type information
- **Since** - Callout de métadonnées
- **Version** - Callout de métadonnées
- **Warning** - Callout d'avertissement

Le titre facultatif après les deux-points sera utilisé comme titre du callout. Si aucun titre n'est fourni, le nom du type de callout sera utilisé comme titre.

Le contenu du callout suit immédiatement à la ligne suivante (aucune ligne vide n'est requise). Le contenu se poursuit jusqu'à une ligne vide, le callout suivant, un bloc de code délimité, ou la fin du document.

Exemple :

````markdown
- Important: Performance Note
This algorithm has O(n log n) complexity.

- Example: Quick Sort
Here's how to implement it:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

Vous pouvez également omettre complètement le titre :

	- Warning
	This is a warning without a custom title.

Ces callouts sont automatiquement convertis au format de callout de Marked et stylés en conséquence. Le type de callout d'origine est conservé dans l'attribut `data-callout`, ce qui permet d'appliquer un style CSS personnalisé si vous le souhaitez.

> Cette fonctionnalité ne fonctionne que lors de la prévisualisation de fichiers Xcode Playground (`.playground`). Les fichiers Markdown classiques ne traiteront pas cette syntaxe.


## Table des matières

Vous pouvez spécifier l'endroit du document où la table des matières doit apparaître à l'aide de `<!--TOC-->`. Si ce marqueur est défini, il remplace l'option des Préférences et s'affichera toujours dans la fenêtre d'aperçu, ainsi que lors de l'enregistrement et de l'impression. La table des matières ne s'affichera qu'une seule fois, même si plusieurs marqueurs `<!--TOC-->` sont présents dans le contenu.

Si vous ajoutez `max#` à la balise ci-dessus (où # est un chiffre de 1 à 5), cela contrôlera la profondeur de la table des matières affichée. Par exemple, `<!--TOC max2-->` n'affichera dans la liste que les titres de niveau 1 et 2. Vous pouvez également spécifier un niveau de titre minimum avec `<!--TOC min2-->`. Les maximums et minimums sont basés sur les niveaux de titre réels, et non sur les niveaux d'imbrication. Le maximum et le minimum peuvent être utilisés ensemble.

Marked reconnaît également la syntaxe `{{TOC}}` de style MultiMarkdown, ainsi que `{{TOC:2-6}}` de style Pandoc, où `2-6` correspond à la plage des niveaux de titre minimum et maximum à inclure.

Par défaut, la table des matières s'imprimera sur la première page du document si l'option « Imprimer la table des matières » est activée dans {% prefspane Export %}. Si un marqueur existe dans le document, elle sera placée à cet endroit à la place.

I> Vous pouvez définir le type de numérotation ou de lettrage de chaque niveau d'une hiérarchie de table des matières imbriquée dans {% prefspane Export %}.

## Sauts de page

Vous pouvez forcer un saut de page pour la sortie impression/PDF à l'aide de la syntaxe suivante :

```html
<!--BREAK-->
```

Placez ce jeton seul sur une ligne, et il générera un balisage forçant une nouvelle page à cet endroit. Marked comprend également le format Leanpub :

	{::pagebreak /}

## Pauses de défilement automatique [pauses]

Marked peut fonctionner comme un télésouffleur grâce à la fonctionnalité [Défilement automatique](Autoscroll.html) (pensez à ajouter le [style Teleprompter](https://markedapp.com/styles/preview?style=teleprompter)). Dans ce cas, il peut être utile d'inclure des pauses dans le document. Pour cela, utilisez :

```html
<!--PAUSE:X-->
```

Où `X` est le nombre de secondes pendant lesquelles Marked doit marquer une pause. Ainsi, insérer `<!--PAUSE:15-->` produira une pause de 15 secondes lorsque ce point du document atteindra le milieu de l'écran.

## Inclusions de fichiers

Le contenu de fichiers supplémentaires peut être inséré à l'aide de la syntaxe suivante :

	<<[folder/filename]

Le chemin du fichier peut être relatif au fichier d'index ou absolu. Les inclusions peuvent être imbriquées ; vous pouvez utiliser cette même syntaxe à l'intérieur d'un fichier inclus. Si vous utilisez des chemins relatifs, les inclusions dans les fichiers imbriqués doivent être relatives à ce fichier. ***Cependant,*** MultiMarkdown traitera tout en se basant sur l'emplacement du premier fichier ouvert : tous les chemins d'images ou autres éléments intégrés doivent donc être relatifs au premier fichier parent, même s'ils se trouvent dans des documents enfants.

Les métadonnées MultiMarkdown et les en-têtes YAML sont automatiquement retirés des fichiers inclus avant le rendu. Cela évite que ces en-têtes n'apparaissent dans le document, mais gardez à l'esprit que des métadonnées telles que le « niveau de titre de base » seront ignorées dans les documents inclus.

T> Notez que lors de la consultation de documents contenant des fichiers inclus, vous pouvez taper « I » (majuscule-i) pour voir quel fichier inclus se trouve dans la zone visible.

Voir [« Documents multi-fichiers »][ext] pour plus d'informations.

[ext]: Multi-File_Documents.html

## Inclusion de code

Marked peut inclure des fichiers externes en tant que code à l'aide d'une syntaxe similaire aux inclusions de fichiers ci-dessus :

	<<(folder/filename)

Notez les parenthèses au lieu des crochets. Pour des raisons de compatibilité avec la syntaxe Leanpub, Marked reconnaît également un ensemble de crochets précédents contenant un titre, bien que celui-ci ne soit actuellement pas exploité par Marked :

	<<[Code title](folder/filename)

Le contenu du fichier spécifié sera inséré dans un bloc pre>code de votre document et pourra bénéficier de la coloration syntaxique automatique si elle est activée. Les blocs de code ne peuvent pas être imbriqués et ne seront pas traités par MultiMarkdown. Les processeurs personnalisés continueront cependant de s'exécuter sur le bloc pre>code créé.

## Inclusion de texte ou HTML non traité

E> **Remarque :** Cette fonctionnalité est destinée aux utilisateurs avancés.

Si vous souhaitez inclure du HTML brut ou un autre texte qui ne doit pas être traité par MultiMarkdown (ou votre processeur personnalisé), vous pouvez utiliser des accolades (`{}`) pour inclure un fichier *après* le traitement du reste du document :

	<<{folder/raw_file.html}

Aucune syntaxe d'inclusion ne sera reconnue à l'intérieur de ces fichiers (pas d'imbrication), et le contenu **brut** du fichier sera inséré tel quel dans le résultat HTML final. Cela est idéal pour insérer du HTML sans surcharger le processeur de texte, ou pour éviter la conversion/l'échappement de certains éléments lorsque vous ne le souhaitez pas ; mais soyez prudent, car peu de garde-fous garantissent que la mise en forme du document sera préservée autour de ce que vous insérez.
