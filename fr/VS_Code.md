# <%= @title %>

[Visual Studio Code][vscode] n'inclut pas Marked de base, mais vous pouvez utiliser une extension communautaire pour un **aperçu Markdown en direct** dans Marked : aperçu, export et relecture pendant que vous continuez à écrire dans VS Code.

## Démarrage rapide [quick-start]

1. Installez une extension VS Code **Open in Marked** (voir [l'extension Open in Marked][ext] ci-dessous).
2. Ouvrez votre fichier Markdown dans VS Code.
3. Envoyez le fichier vers Marked : l'aperçu se met à jour à chaque enregistrement.

## Extension Open in Marked [open-in-marked-extension]

L'[extension Open in Marked][ext] (Visual Studio Marketplace) ajoute une action **Open in Marked** : bouton dans le titre de l'éditeur, **{% kbd shift cmd m %}**, menus contextuels dans l'éditeur et l'explorateur de fichiers, **ouverture de dossier** facultative pour le navigateur de fichiers de Marked, un indicateur dans la barre d'état, et un enregistrement automatique facultatif avant l'ouverture. Les réglages permettent de définir le chemin de l'application Marked si elle ne se trouve pas à l'emplacement par défaut.

I> Cette extension a été publiée à l'origine pour Marked 2. Marked 3 utilise le même type de transmission de fichier et d'URL, cette intégration continue donc de fonctionner ; en cas de changement, consultez la [page de l'extension][ext] ou le dépôt de son auteur pour les mises à jour.

## Prérequis [requirements]

Marked fonctionne uniquement sous macOS. Installez [Marked 3][marked] ainsi que l'extension, puis définissez le **chemin de l'application** vers votre copie de Marked si nécessaire.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/
