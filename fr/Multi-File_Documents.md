# <%= @title %>

Marked autorise plusieurs syntaxes différentes pour inclure un fichier dans un autre.

## Syntaxe de Marked [marked-syntax]

Vous pouvez inclure des fichiers externes dans un seul document d'aperçu en utilisant la syntaxe spéciale `<<[path/file]` au début d'une ligne. La ligne doit avoir des lignes vides au-dessus et en dessous, et le chemin est supposé être relatif au document principal à moins qu'il ne commence par une barre oblique (`/`) ou un tilde (`~`). Slash (répertoire racine) et tilde (répertoire personnel) peuvent être utilisés pour définir des chemins absolus vers les fichiers. Aucun chemin n'est nécessaire si les fichiers externes se trouvent dans le même dossier que le document principal, il suffit de mettre le nom du fichier (sensible à la casse et incluant l'extension) entre crochets.

Vous pouvez utiliser les en-têtes de métadonnées "Include Base" ou "Transclude Base" pour modifier l'emplacement de base des fichiers inclus, par exemple :

    Transclude Base: ~/Desktop

*Notez que lors de la visualisation de documents contenant des fichiers inclus, vous pouvez taper « I » (shift-i) pour voir quel fichier inclus se trouve dans la zone visible. Appuyer sur Entrée pendant que le chemin du fichier inclus est affiché ouvrira le fichier inclus dans l'éditeur par défaut.*

Grâce à cette fonctionnalité, vous pouvez créer des documents/livres volumineux en utilisant plusieurs fichiers (par exemple un fichier pour chaque chapitre), puis spécifier l'ordre des documents dans un seul fichier d'index. Peu importe le nom des fichiers ou la manière dont les dossiers sont organisés ; le fichier que vous ouvrez dans Marked sera considéré comme l'index et les fichiers répertoriés à l'intérieur seront inclus. Un exemple de fichier d'index pour un document en trois parties :

Structure des dossiers :

![][1]

[1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Index.md :

	# Titre du document

	## Section 1

	<<[sections/section1.md]

	## Section 2

	<<[sections/section2.md]

	## Section 3

	<<[sections/section3.md]

L'ouverture d'Index.md dans Marked affichera son contenu avec les trois fichiers inclus développés à l'intérieur. Tous les fichiers inclus seront surveillés pour détecter les modifications. Contrairement au document ouvert dans Marked, le suivi des fichiers inclus dépend de Spotlight pour obtenir les mises à jour et doit exister dans un dossier indexé Spotlight sur votre disque.

Vous pouvez également inclure des extraits de code et du HTML ou du texte brut en utilisant [variations de cette syntaxe](Special_Syntax.html#includingcode).

L'exportation HTML finale d'un document contenant des inclusions aura des commentaires HTML contenant le chemin relatif du fichier inclus au début et à la fin du texte importé.

**Remarque :** plus un document contient de fichiers, plus le temps de compilation global de l'aperçu sera lent. Marked essaie d'optimiser et de mettre en cache le processus, mais attendez-vous à des retards de rendu à mesure que la taille de votre document augmente.

## Syntaxe de transclusion MultiMarkdown [multimarkdown-transclude-syntax]

Vous pouvez également utiliser la syntaxe `{{filename}}` basée sur la nouvelle spécification MultiMarkdown. Marked reconnaîtra `Transclude Base: path` dans les métadonnées MMD et l'utilisera comme base pour la transclusion de fichiers.

Transclude Base ne sera reconnu que dans le document parent, pas dans les documents supplémentaires inclus. Toutes les inclusions imbriquées doivent avoir des chemins basés sur la base Transclude initiale ou à partir de l'emplacement du document parent.

La syntaxe de code clôturée fournie par MultiMarkdown pour inclure des fichiers sans traitement ne fonctionnera pas dans Marked. Pour ce faire, veuillez utiliser la syntaxe `<<(file)` (bloc de code) ou `<<{file}` (brut).

## Syntaxe du bloc iA Writer [ia-writer-block-syntax]

Marked 2.5.11+ prend en charge la syntaxe iA Writer [Content Block][ia]. Il s'agit d'une référence commençant par une barre oblique (`/`) sur sa propre ligne. Il peut s'agir d'un exemple de code, d'une image, d'un fichier markdown ou d'un fichier CSV. Tout sera traité de manière appropriée en fonction de l'extension du fichier inclus, et les CSV seront [convertis en tableaux Markdown][csv] si possible.

Dans iA Writer, les fichiers inclus sont importés dans le conteneur iCloud et ne nécessitent pas toujours de chemins « réels ». Dans Marked, à moins que les fichiers inclus n'existent déjà dans le même dossier que le fichier en cours de prévisualisation, cette syntaxe doit être utilisée avec un chemin, absolu ou relatif. La première barre oblique sera ignorée, donc s'il s'agit d'un chemin absolu, commencez par deux barres obliques.

Un extrait de code dans le même dossier que le document en cours de prévisualisation :

    /snippet.h

Chemin relatif vers un sous-répertoire appelé "images" :

    /images/image.png "titre facultatif"

Chemin absolu vers le dossier Documents :

    //Users/username/Documents/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Comment les plans, les cartes mentales et les inclusions CSV sont convertis [how-outline-mind-map-and-csv-includes-are-converted]

Lorsque vous incluez certains types de fichiers avec la syntaxe de bloc `<<[path]` ou iA Writer, Marked les convertit au lieu d'insérer le contenu brut du fichier. Le comportement des plans et des cartes mentales dépend de l'extension du fichier et de vos préférences [Paramètres : Applications → Cartes mentales/Contours][mindmaps]. Les fichiers CSV/TSV sont toujours convertis en tableaux Markdown (voir [Création de tableaux à l'aide de fichiers CSV][csv]).

| Format | Extension | Lorsque « Intégrer en tant que Mermaid » est **activé** | Quand **éteint** |
|--------|------------|-------------------------|--------------|
| **iThoughtsX** | .itmz | Diagramme de carte mentale Mermaid (arbre rangé) | Image d'aperçu du fichier .itmz |
| **MindManager** | .mmap | Diagramme de carte mentale Mermaid | Liste Markdown imbriquée |
| **FreeMind** | .mm | Diagramme de carte mentale Mermaid | Liste Markdown imbriquée |
| **OPML** | .opml | Diagramme de carte mentale Mermaid | Liste Markdown imbriquée |
| **OmniOutliner** | .ooutline | Diagramme de carte mentale Mermaid | Liste Markdown imbriquée |
| **Bike** | .bike | Carte mentale Mermaid (nom de fichier en tant que nœud racine) | Liste Markdown imbriquée (pas de titre du document) |
| **CSV/TSV** | .csv, .tsv | Tableau Markdown ||
| **RTF/RTFD** | .rtf, .rtfd | Markdown via la conversion RTF (voir [Support RTF et RTFD](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown via la conversion PDF lors de l'ouverture en tant que document principal (voir [Support PDF](PDF_Support.html)) ||

Chaque format de plan/carte mentale a sa propre case à cocher sous *Mind Maps/Outlines* (cartes mentales, fichiers OPML, contours Bike, contours OmniOutliner). La désactivation d'un format utilise le comportement "off" pour ce type uniquement. Voir [Intégration de cartes mentales et de plans](Embedding_Mind_Maps_and_Outlines.html) pour les détails du format et [Paramètres : applications][mindmaps] pour modifier ces options. Pour plus de détails sur la conversion CSV, voir [Création de tables à l'aide de fichiers CSV][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Formats de livres [book-formats]

Marked prend également en charge les fichiers d'index dans des formats tels que [Leanpub][lp], [GitBook][gb] et mmd\_merge (MultiMarkdown). Les fichiers inclus dans les index au format livre seront surveillés pour détecter les modifications et le résultat sera un aperçu complet de votre document compilé, tout comme l'exemple "Index.md" ci-dessus.

### Leanpub [leanpub]

Si vous activez l'option dans le {% prefspane Apps %} sous Prise en charge Leanpub/GitBook, les fichiers nommés « Book.txt » seront automatiquement traités comme des fichiers d'index Leanpub. L'ancien format « frontmatter: » est également reconnu.

[Documentation Leanpub.][lpdocs]

Exemple de fichier Leanpub Book.txt :

    frontmatter:
    Remerciements.txt
    Préface.txt
    Introduction.txt
    mainmatter:
    Markdown.txt
    Exemples de livres.txt
    Insertion d'images.txt


### mmd_merge [mmdmerge]

Pour mmd\_merge, Marked nécessite que la première ligne soit "#merge" (un déclencheur Marked spécial pour mmd\_merge, traité comme un commentaire et ignoré par les autres processeurs).

[Documentation mmd_merge.][mmdm]

Exemple mmd_merge :

    #merge
    métadonnées.txt
    Chapitre-1.md
        sous-chapitre-1-1.md
        sous-chapitre-1-2.md
    Chapitre-2.md
        sous-chapitre-2-1.md
        sous-chapitre-2-2.md
    FAQ.md
    Remerciements.md

### GitBook [gitbook]

Le formatage GitBook utilise une liste Markdown pour créer la structure et la table des matières. Si le support GitBook est activé dans le {% prefspane Apps %} sous Leanpub/GitBook support, un fichier nommé SUMMARY.md sera lu et automatiquement converti au format mmd_merge, permettant un aperçu complet de votre document GitBook.

[Documentation GitBook.][gbdocs]

Exemple GitBook SUMMARY.md :

    # Résumé

    * [Partie I](part1/README.md)
        * [Écrire, c'est bien](part1/writing.md)
        * [GitBook est sympa](part1/gitbook.md)
    * [Partie II](part2/README.md)
        * [Nous aimons les commentaires](part2/feedback_please.md)
        * [De meilleurs outils pour les auteurs](part2/better_tools.md)

GitBook permet d'utiliser des ancres dans la table des matières SUMMARY.md, mais Marked les ignorera et n'inclura le document de base qu'une seule fois.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Fonctionnalités d'aperçu de documents multi-fichiers [multi-file-document-preview-features]

![Limites de fichiers incluses][2]

[2]: images/includeboundaries.png @2x width=859px height=239px class=center

Lorsque vous affichez un document contenant des fichiers inclus, vous pouvez utiliser deux fonctionnalités pour vous aider à déterminer quel fichier vous consultez.

* **Clavier :** Appuyer sur {% kbd shift I %} affichera brièvement une fenêtre contextuelle affichant le titre du fichier actuellement visible à la position de défilement de l'aperçu.
    * Appuyer sur {% kbd Return %} après {% kbd I %} modifiera le fichier affiché avec votre éditeur externe.
* **Souris :** La sélection de « Afficher les limites des fichiers inclus » dans le menu Action ({% kbd ctrl cmd B %}) ajoutera une barre colorée sur le côté gauche de l'aperçu, segmentée pour afficher le début et la fin des fichiers inclus. Il affiche également les inclusions imbriquées. Passer la souris sur une section de cette barre affichera le nom du fichier qu'elle représente, et cliquer dessus ouvrira ce fichier dans l'éditeur de votre choix.
