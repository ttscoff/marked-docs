# <%= @title %>

Marked vous donne des options.

## Workflow de prévisualisation en direct

1. Faites glisser un fichier Markdown sur Marked (ou utilisez {% appmenu File, Open... ({{cmd}}O) %}).
2. Modifiez le fichier dans votre éditeur préféré.
3. Enregistrer : Marked met automatiquement à jour l'aperçu.

Voir [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html) pour la visualisation du coffre-fort, l'aperçu en streaming et les guides spécifiques à l'éditeur.

## Faites glisser vers l'icône du Dock

Le moyen le plus simple d'utiliser Marked sur un fichier que vous êtes déjà en train de modifier est de faire glisser l'icône du document depuis la barre d'outils de votre éditeur ou du Finder vers l'icône Marked dans votre Dock. Marked commencera immédiatement à suivre tout fichier Markdown (ou fichier texte) déposé dessus. Vous pouvez également faire glisser des fichiers directement depuis le Finder.

## Utilisation du menu

![][2]

[2]: images/file_open.jpg @2x width=300px height=118px class=center

Vous pouvez bien sûr ouvrir les fichiers Markdown directement en utilisant l'option de menu {% appmenu File, Open... ({{cmd}}O) %}. Marked fonctionne également très bien _sans_ un éditeur de texte. Vous pouvez prévisualiser et convertir votre Markdown en un seul clic.

Marked peut également ouvrir directement les fichiers **`.rtf` et `.rtfd`** (par exemple les exportations depuis Pages ou TextEdit). Ils sont convertis en Markdown pour aperçu et mise à jour lorsque vous enregistrez dans l'application d'origine. Voir [Support RTF et RTFD](RTF_Support.html) pour plus de détails, y compris les images et les limitations.

Marked peut ouvrir les fichiers **`.pdf`** de la même manière : la conversion s'exécute en arrière-plan, puis l'aperçu est mis à jour une fois terminé. Cela fonctionne mieux pour les PDF plus courts et basés sur du texte ; les manuels volumineux et les documents numérisés sont plus lents et moins précis. Voir [Support PDF](PDF_Support.html) pour plus de détails et les limitations.

## Depuis le Presse-papiers

Si vous avez du texte compatible (par exemple Markdown) dans votre presse-papiers, vous pouvez ouvrir un aperçu instantané en sélectionnant {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. Si vous avez copié une sélection à partir d'un navigateur Web ou d'une autre application qui mettait du HTML ou du RTF dans le presse-papiers, Marked la convertit en Markdown pour un aperçu. Lorsque vous collez du RTF à partir d'une application telle que TextEdit ou Pages, les tailles de police plus grandes sont grossièrement converties en niveaux de titre (par exemple, un texte très volumineux devient un titre de niveau 1, un texte plus petit devient un niveau 2, et ainsi de suite). Vous pouvez ouvrir plusieurs aperçus du presse-papiers à la fois et les enregistrer dans un nouveau fichier en choisissant {% appmenu File, Save Transient Preview %}.

## Création d'un nouveau document

Marked vous permet de créer un nouveau fichier texte vide avec la commande {% appmenu File, New ({{cmd}}N) %}. Il vous demandera immédiatement un emplacement pour enregistrer le fichier et vous pourrez activer l'option "Modifier automatiquement les nouveaux fichiers" dans le {% prefspane Apps %}, à côté du bouton Éditeur de texte pour ouvrir automatiquement le fichier nouvellement créé dans votre éditeur par défaut.

## Ouvrir récent

![][3]

[3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked garde également une trace des documents récents. L'option de menu {% appmenu File, Open Recent %} vous montrera les fichiers que vous avez ouverts et vous permettra d'y revenir. Vous pouvez rapidement rouvrir le dernier fichier que vous visualisiez avec {% kbd shift cmd R %}. Utilisez {% kbd shift cmd P %} ou [Actions rapides](Quick_Actions.html) pour exécuter le menu et prévisualiser les commandes à partir du clavier. Il existe également de nombreux autres raccourcis clavier. Si vous souhaitez les apprendre, vous pouvez trouver un tableau sous [Raccourcis clavier](Keyboard_Shortcuts.html).

## Ouverture rapide ##

Vous pouvez rapidement basculer entre les documents ouverts, ouvrir des documents récents ou ouvrir la boîte de dialogue Fichier->Ouvrir avec le [Panneau d'ouverture rapide](Quick_Open.html) ({% kbd cmd shift o %}).
