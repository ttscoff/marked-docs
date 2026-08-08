# <%= @title %>

[Bear][bear] peut envoyer un aperçu en direct vers Marked.

## Envoi depuis Bear [sending-from-bear]

Dans Bear, choisissez **Aperçu dans Marked** dans le menu **Affichage** (le libellé peut varier légèrement selon la version de Bear). Marked reçoit un TextBundle, donc les images et ressources intégrées sont généralement transmises avec le texte.

Les images référencées avec des chemins absolus ou des URL `https` sont également résolues, tant que Marked peut y accéder.

## Remarque sur le Mac App Store [mac-app-store-note]

Si vous utilisez la version **Mac App Store** de Marked et que macOS continue de demander l'autorisation d'ouvrir des répertoires lors d'un aperçu depuis Bear, [contactez le support Marked](http://support.markedapp.com) pour un cross-grade gratuit vers l'édition en téléchargement direct, ce qui évite ce frottement particulier lié au bac à sable.

## Balises [tags]

Les balises de style Bear peuvent être affichées comme telles en activant **#Le texte est une balise** et **Balises de style** dans {% prefspane Processor %}.

W> Ce réglage peut perturber Marked si vous écrivez des titres classiques sans espace après le `#`.

## Noms de fichiers et export [filenames-and-export]

Si vous activez **Utiliser le premier H1 comme titre par défault** dans {% prefspane Export %}, ce titre peut déterminer le nom de fichier et l'espace réservé `%title` lors de l'impression ou de l'export PDF depuis Marked.

I> Un style d'aperçu qui se rapproche de l'apparence propre à Bear [est disponible sur markedapp.com/styles](https://markedapp.com/styles/preview?style=bear).

L'aperçu en streaming depuis Bear est détaillé sur la page [Aperçu en streaming](Streaming_Preview.html) et dans [Prise en charge d'applications supplémentaires](Additional_Application_Support.html).

[bear]: https://bear.app/
