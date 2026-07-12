# <%= @title %>

Marked utilise beaucoup de JavaScript pour proposer les fonctionnalités qu'il offre dans l'aperçu. Pour cette raison, un certain nombre de complications peuvent survenir lorsque des scripts sont inclus dans le corps du document.

## Scripts externes

Vous pouvez inclure certains scripts externes à l'aide d'une ligne de métadonnées « CSS Header: » en haut de votre document. Ces scripts ne seront toutefois pas insérés dans l'en-tête, mais dans le pied de page, après le chargement de jQuery et des scripts de Marked. C'est la solution idéale dans la plupart des cas. Vous pourriez tout de même rencontrer un comportement inattendu, car Marked ne peut pas compenser tous les conflits de script possibles. Les modifications du DOM peuvent être particulièrement problématiques.

    CSS Header: <script src="file.js"></script>

## Inclusions en ligne

Il existe de nombreux usages pour faire apparaître du JavaScript dans le corps d'un document, comme des générateurs de graphiques ou d'autres outils Canvas. Selon les réglages de configuration et le processeur utilisé, ce contenu est souvent altéré. La solution consiste à placer votre script et les éléments DOM supplémentaires dans un fichier externe, et à utiliser la syntaxe de Marked pour les [fichiers inclus « bruts »][syntax]. Ces fichiers ne sont traités d'aucune façon : leur contenu est ajouté au fichier une fois le reste du traitement terminé.

    Markdown text.

    <<{file.html}

    More Markdown text...

Pour expérimenter et déboguer le JavaScript qui s'exécute dans l'aperçu de Marked, vous pouvez rattacher l'Inspecteur web de Safari à la fenêtre d'aperçu en suivant les étapes décrites dans [Inspecteur WebKit](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml
