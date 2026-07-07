# <%= @title %>

Marked offre une prise en charge étendue du travail avec les fichiers Microsoft Word. Le flux de travail habituel consiste à **prévisualiser d'abord, exporter en DOCX ensuite** : ouvrez ou surveillez votre Markdown dans Marked, affinez les styles et la relecture dans l'aperçu en direct, puis exportez vers Word lorsque le document est prêt.

## Ouvrir des fichiers DOCX

Marked peut lire un fichier DOCX et le convertir en Markdown propre. Les éléments de style valides, comme les titres et les listes, seront convertis vers leur équivalent Markdown.

Le suivi des modifications et les commentaires seront convertis en CriticMarkup. Les surlignages seront convertis en balises `<mark>`, avec les couleurs appropriées le cas échéant.

## Exporter des fichiers DOCX

Utilisez la palette d'export pour générer un fichier DOCX à partir de votre Markdown. Dans la boîte de dialogue d'enregistrement, vous pouvez spécifier un style intégré : ce style peut ensuite être facilement modifié dans Word, simplement en ouvrant le sélecteur de thèmes et en choisissant un nouveau thème.

### En-têtes et pieds de page

Si vous configurez des en-têtes et pieds de page dans {% prefspane Export %}, ils sont inclus dans le DOCX exporté. Les espaces réservés standards tels que `%title`, `%date`, `%page` et `%total` sont substitués au moment de l'export. `%logo` et `%image` intègrent le logo défini dans les préférences d'en-tête/pied de page. Les variables de métadonnées `%md_*` sont résolues à partir des métadonnées MultiMarkdown du document. `%h1`–`%h6` deviennent des champs Word **STYLEREF** liés aux styles de titre exportés ; Word les remplit automatiquement à l'ouverture du document. Voir [Exportation](Exporting.html#headers-and-footers) pour la liste complète des variables et les différences de comportement entre le DOCX et l'impression/PDF.

## Suivi des modifications

La syntaxe CriticMarkup d'un document Markdown sera convertie en suivi des modifications Word lors de l'export en DOCX. Les commentaires accompagnant les insertions, suppressions et substitutions apparaîtront dans la colonne de droite dans Word, lorsque le suivi des modifications est activé.

Lors de l'importation d'un fichier DOCX dans Marked, le suivi des modifications sera converti en CriticMarkup et en balises `<mark>` selon le cas.

## Mathématiques

Les équations MathJax et KaTeX affichées dans le document seront converties en MathML pour l'affichage dans Word. Cette conversion n'est pas parfaite, mais génère dans la plupart des cas un bloc mathématique valide dans le document Word. Cela ne s'applique qu'à l'export : les blocs mathématiques présents dans les documents Word ne seront pas convertis lors de l'importation.

## Ajouter des styles d'export personnalisés

Vous pouvez ajouter vos propres styles d'export en incluant un modèle et un fichier styles.xml dans `~/Library/Application Support/Marked/Custom Word Styles/`. Pour cela :

1. Ouvrez un fichier DOCX généré par Marked dans Word.
2. Modifiez-y les styles dans l'éditeur de style pour chaque élément, en sélectionnant « Ajouter au modèle » pour chacun d'eux.
3. Enregistrez le fichier DOCX.
4. Générez un modèle en accédant à **Création** dans la barre supérieure, puis, dans le menu déroulant *Modèle* à gauche, cliquez sur **Enregistrer le modèle actuel**. Nommez-le comme vous souhaitez qu'il apparaisse dans le menu Style de Marked, et enregistrez-le sous `~/Library/Application Support/Marked/Custom Word Styles/NOMDUSTYLE.thmx`, où `NOMDUSTYLE` est le nom de votre style.
5. Allez dans le Finder et repérez le fichier DOCX que vous avez enregistré depuis Word. Dupliquez-le, renommez la copie en `NOMDUFICHIER.zip`, puis double-cliquez dessus pour le décompresser.
6. Dans le document décompressé, vous verrez un dossier « word » contenant un fichier styles.xml. Copiez ce fichier styles.xml dans le même dossier que ci-dessus, et nommez-le `NOMDUSTYLE.xml` (où `NOMDUSTYLE` est le nom de votre style). Les fichiers `.thmx` et `.xml` doivent porter le même nom de base (seule l'extension diffère).

La prochaine fois que vous exporterez un DOCX depuis Marked, votre nouveau style apparaîtra dans le menu Style de la boîte de dialogue d'enregistrement.
