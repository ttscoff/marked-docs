# <%= @title %>

Transformer votre Markdown en un document fini.

## Exporter après aperçu [export-after-preview]

L'aperçu de Marked est la base de l'exportation : ce que vous voyez dans la fenêtre d'aperçu est ce que vous obtenez au format PDF, DOCX, EPUB et d'autres formats (paramètres spécifiques à l'exportation modulo tels que les marges, les en-têtes et la pagination). Configurez votre style et relisez d'abord l'aperçu, puis exportez lorsque le document est prêt. Voir [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html) pour le flux de travail d'aperçu complet.

## Le panneau d'exportation [drawer]

![Panneau d'exportation][export-panel]

Le **Panneau d'exportation** est un panneau de type projecteur piloté par clavier qui offre un accès rapide à toutes les options d'exportation. Ouvrez-le en cliquant sur l'icône d'exportation dans la barre d'état ou en appuyant sur {% kbd shift cmd e %}.

![Bouton Exporter][expbut]

Le panneau d'exportation vous permet d'enregistrer votre document au format HTML, PDF d'une seule page, PDF paginé, package RTF ou fichier Microsoft Word DOC ou DOCX. Vous pouvez également enregistrer dans un nouveau fichier Markdown (les fonctionnalités spécifiques à Markdown seront rendues et leurs résultats inclus), un document ouvert (ODT) ou au format OPML pour une utilisation dans d'autres applications.

## Copier le HTML [copyhtml]

Utilisez la fonction Copier HTML pour placer le code source HTML de votre aperçu dans votre presse-papiers sans aucun problème. Vous pouvez le sélectionner dans le menu Action ou simplement appuyer sur {% kbd shift cmd C %}. Le code HTML copié sera un extrait prêt à être inséré dans un blog, un forum ou un document HTML.

Vous n'avez pas besoin d'être dans la vue source pour copier. Avec l'aperçu concentré (cliquez dessus), tapez simplement {% kbd shift cmd C %} et vous verrez un message contextuel vous informant que la source est dans votre presse-papiers.

## Enregistrer le code HTML [save-html]

![][exporthtmlaccessory]

La commande Enregistrer HTML (accessible depuis le menu Action ou en tapant simplement **{% kbd cmd S %}**) vous permettra d'enregistrer un document complet prêt à être partagé ou publié.

Vous pouvez éventuellement inclure n'importe lequel des styles de Marked (ou l'un de vos [styles personnalisés][custom]) dans votre exportation, vous donnant ainsi un document prêt à l'emploi avec le formatage nécessaire déjà intégré.

De plus, vous pouvez choisir d'incorporer toutes les images locales incluses dans le document dans le code HTML exporté, ce qui vous permet d'avoir un document autonome qui peut être hébergé n'importe où sans avoir besoin de déplacer les images avec lui. Cela ne fonctionne qu'avec les images référencées sur votre disque local avec des chemins relatifs ou absolus. Évitez d'utiliser les chemins `file:///` si vous souhaitez utiliser cette fonctionnalité.

## Exporter Markdown au format PDF sur Mac [export-markdown-to-pdf-on-mac]

Imprimer/Aperçu PDF ({% kbd cmd P %}) fera apparaître une boîte de dialogue d'impression standard. Chaque style d'aperçu dans Marked est accompagné de ses propres styles d'impression qui suppriment les arrière-plans, modifient la taille des caractères et fournissent des bordures. L'aperçu s'imprimera en fonction du style actuellement sélectionné.

Les boutons PDF et Aperçu sont bien visibles dans la boîte de dialogue d'impression. PDF vous offrira une variété d'options d'exportation au format PDF (en fonction de vos applications disponibles) et Preview exportera une version PDF directement vers Preview.app où vous pourrez l'enregistrer ou l'envoyer par courrier électronique.

L'impression au format PDF à l'aide de cette méthode inclura la pagination. Lors de l'impression sur papier ou PDF, les sauts de page peuvent être insérés manuellement en utilisant la [syntaxe `<!--BREAK-->`][break] ou en définissant les options dans le {% prefspane Export %} pour utiliser les en-têtes de niveau un et/ou de niveau deux comme séparateurs de section.

Il existe également une préférence pour transformer les règles horizontales (`<hr>`) en sauts de page lors de l'impression. Cela remplacera la ligne créée par la balise par un saut de page, la supprimant ainsi de la sortie finale. L'aperçu n'est pas affecté par ce paramètre.

![Marges d'impression][printmargins]

Les marges de page peuvent être définies dans le {% prefspane Export %} et affecteront la sortie PDF imprimée et paginée.

Vous pouvez remplacer les paramètres de marge par document à l'aide de la clé de métadonnées `Margins:`. Les valeurs sont interprétées comme des points ; les suffixes d'unité tels que `px`, `pt` et `em` sont ignorés. Utilisez deux chiffres pour les marges verticales et horizontales (`10 20`), ou quatre chiffres pour le haut, la droite, le bas et la gauche (`10, 20, 10, 20` ou `10 20 10 20`). Les marges des métadonnées remplacent les paramètres {% prefspane Export %}.

### En-têtes et pieds de page [headers-and-footers]

Les en-têtes et pieds de page définis dans le {% prefspane Export %} apparaîtront en haut et en bas de toute page imprimée ou enregistrée au format PDF paginé et lors de l'exportation DOCX. Vous pouvez placer n'importe quel texte en haut à gauche, en haut au centre, en haut à droite, en bas à gauche, en bas au centre et en bas à droite. Le texte central est aligné au centre de la page. Les variables suivantes seront remplacées dans les chaînes si elles sont utilisées :

    %title = Titre du document
    %date = Date actuelle
    %time = Heure actuelle
    %page = Numéro de page actuel
    %total = Nombre total de pages
    %path = Chemin du système de fichiers vers le document
    %filename = Juste le nom de fichier du document
    %basename = Le nom du fichier sans extension
    %logo/%image = Un logo défini dans le champ d'image dans les préférences En-tête/Pied de page
    %%(text) = Texte à imprimer uniquement sur la première page
    %h1/h2/h3/h4/h5/h6 = Titres de section basés sur les en-têtes Markdown
    %sep(X) = Texte à placer entre les titres de section si une sous-section existe

**Le PDF imprimé et paginé** résout `%h1`--`%h6` en utilisant la pagination de Marked, de sorte que chaque page affiche la hiérarchie des titres visible sur cette page. Les variables de métadonnées `%sep(X)` et `%md_*` sont également prises en charge dans la sortie impression/PDF.

**L'exportation DOCX** intègre `%logo`/`%image` dans l'en-tête ou le pied de page de Word (à l'échelle d'environ 50 px de haut, correspondant à l'aperçu avant impression). Les espaces réservés de titre deviennent des champs Word **STYLEREF** qui font référence aux styles `Heading 1`--`Heading 6` exportés. Word met à jour ces champs lorsque le document est ouvert, en fonction de la mise en page et des sauts de page de Word, et non de la pagination d'aperçu de Marked. `%md_*` Les variables de métadonnées sont remplacées une fois au moment de l'exportation, comme pour l'impression/PDF. `%sep(X)` n'est pas converti dans les en-têtes/pieds de page DOCX.

`%title` utilisera n'importe quelle information « Title: » définie dans les en-têtes de métadonnées MultiMarkdown, sinon elle reviendra au nom de fichier sans l'extension de fichier. Pour définir un titre à l'aide des métadonnées MMD, placez ce qui suit sur la première ligne du document :

    Title: Le titre de votre document

Suivez la ligne avec une ligne vide (ou toute autre métadonnée que vous souhaitez définir, suivie d'une ligne vide).

Vous pouvez également utiliser n'importe quelle clé de métadonnées MMD comme variable en la préfixant par `%md_` et en combinant les mots de la clé sous forme de chaîne minuscule. Par exemple, si votre document comporte une clé de métadonnées en haut telle que :

    Funky Monkey: Le singe le plus funky

Ensuite, utiliser `%md_funkymonkey` dans un champ d'en-tête placerait « Le singe le plus funky » dans le document exporté à l'emplacement de cet en-tête. Les documents qui ne contiennent pas cette clé particulière laisseront le champ vide, vous permettant d'ajouter de manière sélective des en-têtes basés sur les métadonnées.

Voir [Formats de date et d'heure](Exporting.html#dateandtimeformats) pour les codes de format `%date` et `%time`.

Le paramètre « Décalage de numérotation des pages » peut être utilisé pour ajuster le numéro à partir duquel les numéros de page commencent. Par exemple, si vous avez une table des matières sur la première page et que vous souhaitez que la numérotation commence sur la deuxième page en tant que page 1, définissez le décalage sur -1. La page 2 sera désormais la page 1 dans l'en-tête/pied de page (`%page`) et le nombre total de pages (`%total`) sera ajusté en conséquence.

Vous pouvez également spécifier une police d'en-tête/pied de page pour un document spécifique en utilisant les métadonnées MMD en haut du fichier :

    Header Font: Mensch

Notez que si vous utilisez un nom de famille de polices, une police par défaut sera sélectionnée. Vous pouvez spécifier une variante en utilisant le nom système de la police. Par exemple, dans le cas d'Helvetica Neue Ultralight, vous utiliserez « Header Font: HelveticaNeueUltralight ».

De plus, vous pouvez spécifier une taille de police d'en-tête/pied de page par document avec les métadonnées :

    Header Font Size: 10

### Formats de date et d'heure [dateandtimeformats]

Les champs **Format de date** et **Format d'heure** dans le {% prefspane Export %} contrôlent la manière dont `%date` et `%time` sont rendus dans les en-têtes et les pieds de page. Les deux champs utilisent des codes de format de style strftime : un `%` suivi d'une lettre. Le texte littéral (tel que `-`, `:` ou espaces) est copié tel quel.

**Exemples**

    %m-%d-%Y → 20/06/2026 (format de date par défaut de Marked)
    %I:%M %p → 15h45 (format d'heure par défaut de Marked)
    %Y-%m-%d → 2026-06-20
    %B %d, %Y → 20 juin 2026
    %a %H:%M → vendredi 15h45

**Codes de format courants**

| Codes | Exemple | Description |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Année à quatre chiffres |
| `%y` | 26 | Année à deux chiffres |
| `%m` | 06 | Mois (01--12) |
| `%B` | juin | Nom complet du mois |
| `%b` | juin | Nom du mois abrégé |
| `%d` | 20 | Jour du mois (01--31) |
| `%e` | 20 | Jour du mois (espaces remplis) |
| `%A` | Vendredi | Nom complet du jour de la semaine |
| `%a` | Ven | Nom abrégé du jour de la semaine |
| `%H` | 15 | Heure, 24 heures (00--23) |
| `%I` | 03 | Heure, 12 heures (01--12) |
| `%M` | 45 | Minutes (00--59) |
| `%S` | 07 | Deuxième (00--59) |
| `%p` | PM | AM ou PM |
| `%x` | (paramètres régionaux) | Date préférée de la région |
| `%X` | (paramètres régionaux) | Heure préférée de la région |
| `%c` | (paramètres régionaux) | Date et heure préférées des paramètres régionaux |

**Les PDF imprimés et paginés** prennent en charge le style strftime complet défini ci-dessus, ainsi que des codes supplémentaires tels que `%j` (jour de l'année), `%U`/`%W` (numéro de la semaine), `%z` (décalage du fuseau horaire) et `%Z` (nom du fuseau horaire). Voir la [Spécification strftime Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) pour une référence complète.

**L'exportation DOCX** prend en charge les codes répertoriés dans le tableau ci-dessus. Les codes moins courants peuvent être ignorés ou transmis sans modification.

Utilisez **Restaurer les formats par défaut** dans {% prefspane Export %} pour réinitialiser à `%m-%d-%Y` et `%I:%M %p`.

### En-têtes et pieds de page par document [per-document-headers-and-footers]

Vous pouvez spécifier des en-têtes et des pieds de page pour chaque document à l'aide des métadonnées MultiMarkdown tout en haut du document :

    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date
    Print Footer Right: %page/%total

Ceux-ci remplaceront tous les paramètres des préférences. Notez que si vous utilisez un processeur autre que MultiMarkdown et que vous ne souhaitez pas que vos en-têtes apparaissent dans le document lui-même, vous pouvez utiliser des commentaires HTML, en veillant à laisser une ligne vide avant la fermeture du commentaire :

    <!--
    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date

    -->

## Enregistrer le PDF [save-pdf]

Cette option enregistre votre aperçu directement dans un fichier PDF sur votre lecteur. Votre document sera rendu dans son intégralité, sans sauts de page. Pour inclure la pagination dans votre sortie, utilisez les options Imprimer/PDF dans le [Panneau d'exportation](#drawer).

## Options d'exportation RTF [rtfexportoptions]

Marked peut exporter des données RTF (Rich Text Format) directement dans votre presse-papiers. Choisissez simplement la commande Copier le texte enrichi dans le menu Action.

Marked peut également enregistrer votre fichier en tant que fichier **RTFD** (Rich Text Format). Le format RTFD est un format groupé qui comprend un fichier RTF et toutes les images intégrées dans le document.

## Exportation DOCX [docx-export]

L'exportation au format DOCX créera un document Microsoft Word valide, avec des éléments tels que des titres, des en-têtes/pieds de page, des accents, des listes, etc., tous mappés à des styles Word valides. Cela signifie que vous pouvez facilement appliquer votre propre thème dans Word.

Voir [Travailler avec DOCX][DOCX] pour plus de détails sur l'importation et l'exportation de Word.

## Exporter Markdown vers EPUB [export-markdown-to-epub]

Marked peut exporter des documents EPUB 100 % valides et 100 % accessibles. Sélectionnez le type d'exportation EPUB, spécifiez les métadonnées telles que le titre, l'auteur et la date, et ajoutez éventuellement une photo de couverture. Le fichier enregistré sera lisible dans n'importe quelle visionneuse EPUB.

Les métadonnées nécessaires à l'exportation EPUB peuvent être incluses dans le fichier lui-même, qu'il s'agisse d'un document Markdown, d'un fichier Scrivener (inclure une page `metadata`) ou d'un autre format de livre. Les clés à utiliser sont :

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

La clé Image de couverture peut inclure un chemin relatif au document de base ou un chemin absolu. Les fichiers PNG ou JPG sont acceptables.

Si le titre n'est pas défini, il sera par défaut le nom de fichier du document original, et si l'auteur n'est pas défini, il sera par défaut le nom complet de votre utilisateur macOS.

La date sera toujours définie sur la date actuelle et ne peut actuellement pas être modifiée avec des métadonnées. Il peut cependant être modifié au moment de la sauvegarde, à condition que le formatage (ISO) reste intact.

### Publication sur Amazon Kindle (KDP) [publishing-to-amazon-kindle-kdp]

EPUB est un format ouvert utilisé par de nombreuses applications et magasins de lecture (Apple Books, Kobo et autres), pas seulement Kindle. Si vous publiez via [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), exportez EPUB depuis Marked et téléchargez ce fichier sur KDP. Amazon le convertit dans son propre format de livraison Kindle (KFX) pour les lecteurs.

KDP accepte plusieurs formats de manuscrits, notamment EPUB et DOCX (que Marked peut également exporter). Consultez les [formats de livres électroniques pris en charge](https://kdp.amazon.com/en_US/help/topic/G200634390) et le [guide de formatage des manuscrits de livres électroniques](https://kdp.amazon.com/en_US/help/topic/G200645680) d'Amazon pour connaître les exigences.

**MOBI n'est pas requis.** KDP n'accepte plus les téléchargements MOBI pour les nouveaux titres (y compris les livres à mise en page fixe, à compter de mars 2025). Marked n'exporte pas MOBI et vous n'avez pas besoin d'un fichier « Kindle » ou Mobipocket distinct pour KDP. Si vous préférez les outils de mise en page d'Amazon, vous pouvez également préparer un livre avec [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), qui produit des fichiers KPF.

Avant de télécharger, vous souhaiterez peut-être vérifier à quoi ressemblera votre EPUB sur les appareils Kindle à l'aide du [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) gratuit d'Amazon. Il s'agit d'un logiciel tiers facultatif d'Amazon, qui ne fait pas partie de Marked.

## Exporter les profils [export-profiles]

Les profils d'exportation vous permettent d'enregistrer et de basculer rapidement entre différents ensembles de préférences d'exportation. Ceci est particulièrement utile si vous exportez régulièrement des documents à des fins différentes : par exemple, un profil pour les PDF prêts à imprimer avec des marges et des en-têtes spécifiques, et un autre pour le HTML prêt pour le Web avec des styles intégrés.

### Utilisation des profils d'exportation [using-export-profiles]

Lorsque vous lancez Marked pour la première fois, un profil « Par défaut » est automatiquement créé avec vos paramètres d'exportation actuels. Vous pouvez voir et sélectionner des profils dans les boîtes de dialogue d'exportation (Exportation PDF, Enregistrer HTML, etc.) à l'aide du menu contextuel du profil en haut de la boîte de dialogue.

**Création d'un nouveau profil :**

1. Ajustez vos paramètres d'exportation dans le {% prefspane Export %} ou dans n'importe quelle boîte de dialogue d'exportation
2. Dans la boîte de dialogue d'exportation, cliquez sur le menu contextuel du profil et choisissez « Ajouter un profil… »
3. Saisissez un nom pour votre profil (par exemple, « Qualité d'impression » ou « Exportation Web »)
4. Les paramètres actuels sont enregistrés en tant que profil

**Chargement d'un profil :**

- Sélectionnez un profil dans le menu contextuel de n'importe quelle boîte de dialogue d'exportation
- Tous les paramètres d'exportation seront immédiatement mis à jour pour correspondre aux valeurs enregistrées de ce profil

**Enregistrement des modifications apportées à un profil :**

- Après avoir modifié les paramètres d'exportation, un bouton « Enregistrer » apparaît à côté de la fenêtre contextuelle du profil.
- Cliquez sur « Enregistrer » pour mettre à jour le profil actuel avec vos modifications
- Le bouton n'est activé que lorsqu'il y a des modifications non enregistrées

**Gestion des profils :**

- Choisissez « Gérer les profils… » dans le menu contextuel du profil pour ouvrir la fenêtre de gestion des profils
- De là, vous pouvez :
  - **Renommer** les profils en double-cliquant sur le nom
  - **Dupliquer** un profil pour en créer un nouveau basé sur celui-ci
  - **Supprimer** les profils (le profil « Par défaut » ne peut pas être supprimé)
  - Afficher tous les profils disponibles dans une liste

### Ce que capturent les profils d'exportation [what-export-profiles-capture]

Les profils d'exportation enregistrent toutes les préférences liées à l'exportation, notamment :

- **Paramètres PDF** : taille de page, marges, en-têtes/pieds de page, polices, sauts de page, table des matières
- **Exportation HTML** : intégration de styles, intégration d'images, coloration syntaxique, rendu mathématique
- **Traitement Markdown** : habillage du texte, formatage des liens, règles du processeur
- **CriticMarkup** : type d'exportation et options de traitement
- **Mise en évidence de la syntaxe** : préférences de détection et de mise en évidence de la langue
- **Rendu mathématique** : intégration MathJax/KaTeX et numérotation des équations
- **Gestion des images** : options d'intégration, comportement de copie, paramètres de chemin
- **Typographie** : Césure, veuves/orphelins, tailles de police
- **Comportement d'exportation** : préférences de dénomination des fichiers, résolution des conflits

Les profils fonctionnent sur tous les types d'exportation : Markdown, HTML, PDF continu, PDF paginé, EPUB, DOCX, ODT, TextBundle, RTF et OPML.

### Stockage de profil [profile-storage]

Les profils sont stockés dans votre dossier Application Support à l'adresse :

    ~/Library/Application Support/Marked/ExportProfiles.plist

Cela signifie que vos profils persistent même si vous réinitialisez les préférences de l'application et qu'ils survivent aux mises à jour de l'application. Vous pouvez sauvegarder ce fichier pour conserver vos profils à travers les installations.

### Conseils pour l'utilisation des profils d'exportation [tips-for-using-export-profiles]

- **Créez des profils pour les flux de travail courants** : si vous exportez régulièrement pour l'impression ou le Web, créez des profils distincts pour chacun.
- **Utilisez des noms descriptifs** : les noms de profil tels que « Impression - Lettre » ou « Web - Styles intégrés » indiquent clairement à quoi sert chaque profil.
- **Enregistrez fréquemment** : le bouton « Enregistrer » apparaît chaque fois que vous avez apporté des modifications. Cliquez dessus pour conserver vos ajustements.
- **Démarrer à partir de profils existants** : utilisez « Dupliquer » dans la fenêtre de gestion pour créer des variantes de profils existants plutôt que de repartir de zéro.

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_With_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center
