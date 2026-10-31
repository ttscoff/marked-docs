<!-- MT draft for fr — Reading Mode help. Review before publishing. -->
# <%= @title %>

Le mode lecture conserve votre place dans les documents longs, concentre le bloc actuel et vous permet d'enregistrer les surlignages persistants.

## Entrer en mode lecture [entering-reading-mode]

Choisissez {% appmenu Preview, Reading Mode %} ou appuyez sur {% kbd ctrl opt r %}. Si Speed ​​Read est en cours d’exécution, Marked l’arrête avant d’entrer en mode lecture.

Le paragraphe, le titre, l'élément de liste, l'image, le bloc de code, le tableau ou toute autre unité de lecture en cours reçoit un marqueur gauche. La navigation au clavier se déplace en douceur entre les blocs et maintient l'unité actuelle près du tiers supérieur de l'aperçu. Le défilement manuel recible le focus sans casser la page.

## Navigation et reprise [navigation-and-resume]

Lorsque le mode lecture est actif :

- {% kbd j %} ou {% kbd down %} : Passer à l'unité de lecture suivante.
- {% kbd k %} ou {% kbd up %} : Passer à l'unité de lecture précédente.
- {% kbd h %} : Mettez en surbrillance la sélection ou activez la surbrillance de l'unité actuelle lorsqu'aucun texte n'est sélectionné.

Marked enregistre la position de lecture actuelle pour chaque document. Lorsqu'une position enregistrée diffère de la vue actuelle, l'accès au mode Lecture offre deux choix :

- **Reprendre** revient à la position de lecture enregistrée.
- **Commencer à partir d'ici** utilise l'unité de lecture actuellement visible dans l'aperçu.

## Mode focus [focus-mode]

Cliquez sur l'outil Mode Focus en haut de l'aperçu pour assombrir chaque bloc à l'exception de l'unité de lecture actuelle. Le mode Focus suit l’unité actuelle pendant que vous naviguez. Cliquez à nouveau sur l'outil pour restaurer les autres blocs, ou quittez le mode lecture pour effacer automatiquement le mode Focus.

## Création et modification des faits saillants [creating-and-editing-highlights]

Sélectionnez le texte et appuyez sur {% kbd h %} pour créer un surlignage de marqueur en ligne. Sans sélection, appuyez sur {% kbd h %} pour mettre en surbrillance toute l'unité de lecture actuelle, ou appuyez à nouveau dessus pour supprimer cette unité en surbrillance. La première surbrillance demande une signature, que Marked utilise lors de la création de CriticMarkup. Vous pouvez modifier la signature dans {% prefspane Preview %}.

### Popup de sélection

Sélectionnez le texte pour afficher la fenêtre contextuelle de sélection avec les boutons d'icônes centrés dans la ligne :

- **Surligneur** crée une surbrillance en ligne (ou **X** supprime la dernière surbrillance automatique lorsque la surbrillance automatique est activée).
- **Commentaire** ouvre une boîte de dialogue pour ajouter ou modifier une note pour la surbrillance. Si la sélection n'est pas encore mise en surbrillance, Marked la met en évidence en premier.

La fenêtre contextuelle affiche également le nombre de mots de sélection lorsque **Afficher le nombre de mots lors de la sélection** est activé.

### Mettre en surbrillance les commentaires [highlight-comments]

Les commentaires sont distincts des signatures. Une signature attribue la mise en valeur ; un commentaire est votre note à ce sujet.

Ajoutez ou modifiez un commentaire à partir de l'icône de commentaire contextuel de sélection, ou faites un Ctrl-clic sur un surlignage et choisissez **Ajouter un commentaire…** ou **Modifier un commentaire…**. Choisissez **Supprimer le commentaire** pour supprimer la note sans supprimer la surbrillance.

Les surlignages avec commentaires affichent un petit point indicateur. Lorsque la barre latérale Commentaires est visible (**Aperçu > Afficher les commentaires**), les commentaires en surbrillance du mode lecture y apparaissent avec une ligne de connexion à la surbrillance parent, aux côtés de CriticMarkup et d'autres commentaires du document.

### Faits saillants automatiques

Cliquez sur l'outil de surligneur en haut de l'aperçu pour mettre automatiquement en surbrillance le texte lorsque vous le sélectionnez. Cliquez sur le surligneur dans la fenêtre contextuelle de sélection pour annuler la dernière surbrillance automatique, ou cliquez à nouveau sur l'outil de surligneur supérieur pour désactiver la surbrillance automatique.

Les surbrillances en ligne affichent les poignées de début et de fin lorsque vous les pointez ou les sélectionnez. Faites glisser l’une des poignées pour étendre ou réduire la plage en surbrillance. Les modifications sont enregistrées automatiquement et restaurées lorsque le document est actualisé ou rouvert.

Cliquez sur un surlignage pour le mettre au point, puis appuyez sur Supprimer ou Retour arrière pour le supprimer. Ctrl-cliquez sur une surbrillance et choisissez **Partager...** pour ouvrir la feuille de partage macOS avec le titre du document et le texte en surbrillance, **Ajouter un commentaire…** / **Modifier le commentaire…** pour joindre une note, ou **Supprimer un commentaire** pour effacer la note.

Le paramètre **Afficher les surbrillances lorsque le mode lecture est désactivé** contrôle si les surbrillances enregistrées restent visibles après que vous ayez quitté le mode.

## Exporter les faits saillants [exporting-highlights]

Choisissez **Aperçu > Exporter les faits saillants…** ou cliquez sur l'outil Exporter les faits saillants dans la barre d'outils du mode lecture. Formats : Markdown, HTML (style d'aperçu actuel), texte brut, CSV (compatible en lecture, avec commentaires dans la colonne **Note** et signatures dans **Signature**) et JSON (comprend un champ `comment` sur chaque surbrillance).

Les nids d'exportation HTML mettent en évidence les commentaires sous forme de guillemets sous chaque passage en surbrillance.

Le format JSON est le fichier d'échange de Marked. Enregistrez-le à côté d'un document Markdown sous le nom `Document.markedhighlights.json`, ou incluez-le automatiquement lors de l'exportation d'un TextBundle.

## Importation des faits saillants [importing-highlights]

Choisissez **Aperçu > Importer les faits saillants…** et sélectionnez un fichier JSON de faits saillants Marked. Les faits saillants sont fusionnés par identifiant : de nouveaux identifiants sont ajoutés, les identifiants correspondants sont mis à jour et vos surlignages existants qui ne sont pas dans le fichier restent.

Lorsque vous ouvrez un TextBundle contenant `highlights.json`, Marked fusionne automatiquement ces surlignages. Pendant qu'un TextBundle est ouvert, Marked enregistre également les modifications de surbrillance et de commentaire dans `highlights.json` dans le bundle (sans modifier `text.md`).

## Points forts de TextBundle [textbundle-highlights]

Sur **Enregistrez TextBundle**, activez **Inclure les faits saillants** pour intégrer `highlights.json` dans l'ensemble (ou TextPack). Partagez l'ensemble afin que les collaborateurs puissent l'ouvrir dans Marked et conservez un ensemble de points forts combinés.

## CriticMarkup actions [criticmarkup-actions]

Outre l'exportation et l'importation des surbrillances, le menu Aperçu propose deux actions CriticMarkup pour les surbrillance enregistrées :

- **Copier les faits saillants au format CriticMarkup** copie chaque surbrillance au format CriticMarkup sans modifier le fichier source.
- **Inject Highlights into Document...** demande une confirmation, puis encapsule le texte source correspondant sans ambiguïté dans CriticMarkup. Marked ignore les correspondances manquantes, en double ou qui se chevauchent et rapporte le résultat.

Avec une signature et un commentaire, le balisage généré utilise <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>. Avec seulement un commentaire, Marked utilise <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>. Avec seulement une signature, il utilise <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>. Sans l'un ou l'autre, Marked crée uniquement le marqueur <code>{=<span>=</span>highlighted text==}</code>.

## Points forts de l'impression [printing-highlights]

Les surlignages du mode de lecture sont inclus lors de l’impression ou de l’enregistrement sous PDF par défaut. Utilisez **Inclure les surbrillances du mode de lecture** dans la feuille d'impression pour la modifier pour la sortie actuelle. Le paramètre correspondant dans {% prefspane Export %} contrôle la valeur par défaut pour les futurs travaux d'impression et PDF.
