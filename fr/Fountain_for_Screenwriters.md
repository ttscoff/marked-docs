# <%= @title %>

[Fountain](http://fountain.io/) est un langage de balisage de texte spécialisé conçu pour l'écriture de scénarios. Les scénaristes qui écrivent en utilisant la syntaxe de Fountain peuvent utiliser Marked pour prévisualiser leur travail.

L'ouverture de n'importe quel fichier avec une extension ".fountain" activera automatiquement la prise en charge de Fountain pour la fenêtre. Une feuille de style Fountain par défaut sera appliquée pour l'aperçu et l'exportation.

Vous pouvez forcer le traitement de n'importe quel document en tant que Markdown en ouvrant le menu Action en bas à droite de la fenêtre d'aperçu et en désélectionnant **Traiter comme Fountain**.

Les en-têtes de section et de scène apparaîtront dans la table des matières pour une navigation rapide dans votre scénario.

## Scrippets

Vous pouvez également utiliser des « scripts » dans un document standard pour que des sections individuelles soient traitées et stylisées avec Fountain. Entourez simplement votre balisage Fountain à l'intérieur du document principal avec les balises `[scrippet]` :

    [scrippet]
    Votre texte de scénario...
    [/scrippet]

Vous pouvez également utiliser des balises de style Marked standard :

    <!--SCRIPPET-->
    Votre texte de scénario...
    <!--/SCRIPPET-->
