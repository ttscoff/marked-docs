# <%= @title %>

Marked exporte des fichiers EPUB entièrement conformes à partir de votre aperçu Markdown, stylisés avec les mêmes thèmes intégrés et personnalisés que vous utilisez à l'écran et lisibles dans **Apple Books**, **Kobo** et d'autres lecteurs EPUB standard.

Le flux de travail typique est **prévisualiser d'abord, exporter EPUB ensuite** : ouvrez ou compilez votre document dans Marked, choisissez un thème, relisez dans l'aperçu en direct, puis exportez lorsque le livre est prêt.

## Exporter un EPUB [exporting-an-epub]

Ouvrez le [Panneau d'exportation](Exporting.html#drawer) ({% kbd shift cmd e %}) ou utilisez **Enregistrer sous** dans le menu Action et choisissez **EPUB**.

La boîte de dialogue d'enregistrement EPUB vous permet de définir :

* **Titre** : par défaut les métadonnées MultiMarkdown ou le nom du fichier
* **Auteur** : par défaut, votre nom d'utilisateur macOS ; le dernier auteur saisi est mémorisé pour le prochain export
* **Date** : Format ISO ; modifiable au moment de la sauvegarde
* **Image de couverture** : PNG ou JPG facultatif ; Marked génère un aperçu de la couverture par défaut lorsqu'aucun n'est défini

Marked intègre des images locales dans l'EPUB et peut télécharger des images distantes afin que le fichier final soit autonome. Les EPUB exportés sont validés comme XHTML bien formés avant d'être enregistrés, produisant des fichiers conformes aux normes EPUB en matière de distribution et d'accessibilité.

Voir [Exporter les profils](Exporting.html#export-profiles) pour enregistrer les métadonnées EPUB et exporter les paramètres pour une utilisation répétée.

## Style avec des thèmes intégrés [styling-with-built-in-themes]

Le **style d'aperçu** sélectionné pour votre document détermine l'apparence de l'EPUB. Chaque thème Marked intégré (Swiss, GitHub, Manuscript et le reste) peut être appliqué à l'exportation EPUB.

1. Choisissez un style dans le menu Style de la fenêtre d'aperçu (ou définissez un style par défaut dans {% prefspane Style %}).
2. Vérifiez la typographie, les titres, les blocs de code et les images dans l'aperçu en direct.
3. Exporter vers EPUB : Marked regroupe le CSS du thème dans le package EPUB.

Marked applique également du CSS spécifique à l'exportation au-dessus de votre thème d'aperçu afin que les éléments tels que les notes de bas de page, les tableaux et les blocs de code mis en surbrillance par la syntaxe s'affichent correctement dans les liseuses électroniques. Les documents en mode plan utilisent des styles d'exportation optimisés pour les plans ; les index [Leanpub](Multi-File_Documents.html) `Book.txt` utilisent automatiquement le style d'exportation orienté Leanpub.

I> Les lecteurs EPUB ignorent certains CSS réservés au Web (positionnement fixe, astuces de fenêtre d'affichage, etc.). Ce que vous voyez dans l'aperçu de Marked est l'objectif, mais les moteurs de mise en page des liseuses peuvent simplifier l'espacement et les polices. Testez dans Apple Books ou votre lecteur cible avant de publier.

## Stylisme avec des thèmes personnalisés [styling-with-custom-themes]

[Styles personnalisés](Custom_Styles.html) fonctionnent de la même manière pour EPUB que pour l'aperçu et le PDF :

* Ajoutez des fichiers CSS dans {% prefspane Style %} ou dans le [Style Manager](Custom_Styles.html).
* Sélectionnez le thème personnalisé avant d'exporter.
* Marked intègre votre feuille de style dans l'EPUB exporté.

Conseils pour un CSS personnalisé compatible avec EPUB :

* Gardez les mises en page fluides : utilisez des unités relatives et `max-width: 100%` sur les images (`#wrapper img { max-width: 100%; }` est une bonne base de référence).
* Évitez les règles `@media print` pour le style des ebooks ; EPUB utilise les styles de l'écran principal ainsi que la feuille de style d'exportation de Marked.
* [Mode sombre](Previewing.html) : l'inversion dans l'aperçu utilise des requêtes `@media screen` ; la plupart des lecteurs EPUB utilisent la feuille de style claire, sauf si l'application de lecture applique son propre thème sombre.
* Utilisez [CSS supplémentaire](Custom_Styles.html) dans les paramètres de style pour modifier tous les thèmes à la fois (par exemple, une taille de police uniforme dans toutes les exportations).

Pour obtenir des conseils sur la création, voir [Écrire du CSS personnalisé](Writing_Custom_CSS.html).

## Mise en évidence de la syntaxe et mathématiques [syntax-highlighting-and-math]

Si **Inclure la coloration syntaxique dans l'exportation** est activé dans {% prefspane Export %}, les blocs de code s'exportent avec les mêmes couleurs de syntaxe que votre aperçu. Les mathématiques rendues avec [MathJax](MathJax.html) sont incluses dans l'EPUB comme approprié pour la prise en charge des liseuses électroniques.

## Métadonnées dans votre fichier source [metadata-in-your-source-file]

Vous pouvez définir les métadonnées EPUB dans le document au lieu de la boîte de dialogue d'enregistrement. En haut d'un fichier Markdown (ou dans une page de métadonnées Scrivener), utilisez les clés de style MultiMarkdown :

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` accepte un chemin relatif au document ou un chemin absolu. PNG et JPG sont pris en charge. Les valeurs des boîtes de dialogue remplacent ou complètent les métadonnées manquantes au moment de l'exportation.

## Livres multi-fichiers [multi-file-books]

Pour les travaux longs, compilez des chapitres avec [Documents multi-fichiers](Multi-File_Documents.html) : fichiers d'index, exportations Scrivener, Leanpub `Book.txt` ou index de style GitBook. La surveillance de fichiers de Marked inclut les fichiers, prévisualise le livre complet et exporte un EPUB à partir du HTML compilé.

Les titres du document compilé deviennent la [table des matières](Document_Navigation.html) de l'EPUB pour la navigation dans Apple Books et d'autres lecteurs.

## Lecture et publication [reading-and-publishing]

Les EPUB exportés s'ouvrent directement dans **Apple Books** (double-cliquez sur le fichier ou utilisez **Fichier → Ajouter à la bibliothèque**). Ils fonctionnent également dans Kobo, Thorium, Calibre et la plupart des applications compatibles EPUB 3.

### Apple Books [apple-books]

Faites glisser un fichier `.epub` exporté sur l'application Apple Books ou ajoutez-le via **Fichier → Importer**. La typographie personnalisée et la pochette de votre thème Marked sont conservées. Utilisez Apple Books sur Mac, iPad ou iPhone pour vérifier la mise en page avant de partager.

### Publication directe Kindle (KDP) [kindle-direct-publishing-kdp]

EPUB est un format de téléchargement accepté pour [Kindle Direct Publishing](https://kdp.amazon.com/). Exportez depuis Marked et téléchargez le fichier `.epub` ; Amazon le convertit pour la livraison Kindle. KDP accepte également [DOCX](Working_With_DOCX.html). Consultez les [formats de livres électroniques pris en charge](https://kdp.amazon.com/en_US/help/topic/G200634390) d'Amazon pour connaître les exigences actuelles.

**MOBI n'est pas requis** pour les nouveaux titres KDP. Marked n'exporte pas MOBI.

Facultatif : prévisualisez la mise en page du Kindle avec le [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuit d'Amazon avant le téléchargement.

## Connexes [related]

* [Exportation HTML](HTML_Export.html) : HTML autonome avec styles et images intégrés
* [Exportation](Exporting.html) : panneau d'exportation, profils et autres formats
* [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html) : aperçu du flux de travail avant l'exportation
* [Styles personnalisés](Custom_Styles.html) et [Générateur de styles personnalisés](Custom_Style_Generator.html)
* [Documents multi-fichiers](Multi-File_Documents.html) : livres et index de chapitres
* [Exportation AppleScript](AppleScript_Support.html) : automatiser l'exportation EPUB
