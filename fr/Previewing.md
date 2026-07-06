# <%= @title %>

I> Cette page couvre l'*apparence* de l'aperçu : styles, zoom, mode sombre et barre d'état. Pour configurer l'aperçu en direct depuis votre éditeur, voir [Aperçu Live Markdown sur Mac](Live_Markdown_Preview_on_Mac.html).

Changer la façon dont vous voyez les choses.

## Choisir un style

![][1]

[1]: images/StylePicker.jpg @2x width=896px height=195px class=center

Vous pouvez définir un style par défaut pour les nouveaux documents dans le {% prefspane Style %}. Si vous avez activé le menu de style dans la barre d'outils via les paramètres de fenêtre, vous pouvez ajuster le style document par document directement depuis la fenêtre d'aperçu. Votre sélection de style sera mémorisée et sera le premier choix pour les options d'exportation et d'impression.

Les styles personnalisés ajoutés dans les paramètres de style seront disponibles dans les deux menus.

Les styles peuvent être sélectionnés à l'aide de raccourcis clavier. Ouvrez le menu de style pour voir le raccourci clavier de chaque style. Les raccourcis clavier sont attribués dans l'ordre des styles : les 9 premiers styles de la liste sont accessibles avec {% kbd cmd 1 %} -- {% kbd cmd 9 %}, les 10 styles suivants avec {% kbd cmd opt 1 %} -- {% kbd cmd opt 0 %}, etc.

## Mode Plan

Si votre document est une liste hiérarchique, comme celle générée par une carte mentale ou une application de plan, vous pouvez activer le Mode Plan depuis le menu Action pour appliquer un formatage spécial selon le style de plan APA ou décimal.

Le mode plan automatique peut être activé pour des extensions de fichier spécifiques dans le {% prefspane Style %}.

## Zoom du texte

![][2]

[2]: images/textzoom.jpg @2x width=800px height=414px class=center

Vous pouvez modifier la taille du texte à l'aide de {% kbd cmd shift + %} et {% kbd cmd shift - %}, ou utiliser le menu Zoom sous Aperçu dans la barre de menus ou dans le menu Action de la fenêtre du document. Marked se souviendra de tous les changements que vous effectuez, pour la prochaine fois (et à chaque fois). Réinitialisez le zoom à 100 % avec {% kbd cmd 0 %} (ou accédez à **Réinitialiser le zoom** depuis le menu Zoom).

## Mode sombre/Contraste élevé

Si vous préférez un texte clair sur fond sombre, Marked répond à ce besoin. Dans le menu __Aperçu__, vous pouvez utiliser {% appmenu Preview, Dark Mode ({{opt}}{{cmd}}I) %} pour inverser les couleurs de n'importe quel schéma par défaut afin d'obtenir un résultat clair sur sombre, et si un thème personnalisé est [construit correctement](Writing_Custom_CSS.html), cela fonctionnera aussi avec lui.

## Afficher/Masquer la barre d'état

La barre d'état en bas de la fenêtre d'aperçu peut être basculée avec l'élément de menu {% appmenu Preview, Show Status Bar ({{ctrl}}/) %}. Lorsqu'elle est masquée, elle peut être visualisée et utilisée en survolant l'espace en bas de l'aperçu.
