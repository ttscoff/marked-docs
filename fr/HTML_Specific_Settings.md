# <%= @title %>

## Désactiver les identifiants d'en-tête automatiques [disable-automatic-header-ids]

Marked inclut une option pour désactiver la génération automatique d'ID d'en-tête. Vous pouvez trouver cette option dans le {% prefspane Processor %}.

## ID de note de bas de page aléatoires [random-footnote-ids]

Dans le volet **Processeur**, vous pouvez cocher la case « Utiliser des ID de note de bas de page aléatoires » pour générer des identifiants de note de bas de page aléatoires, ce qui permet d'éviter les conflits lorsque plusieurs documents sont affichés sur une même page Web. Cette option n'est disponible que lors de l'utilisation du processeur MultiMarkdown.

## Traitement du Markdown à l'intérieur du HTML [process-markdown-inside-of-html]

Par défaut, la syntaxe Markdown à l'intérieur des balises de bloc HTML est généralement ignorée par les processeurs Markdown. Cette option force Marked à poursuivre le traitement dans les éléments de bloc. Notez que certains balisages peuvent causer des problèmes.
