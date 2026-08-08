# <%= @title %>

### Mode débogage [debug-mode]

Vous pouvez activer la journalisation de débogage en ouvrant {% prefspane Advanced %} et en cochant la case **Mode débogage** en bas du panneau. Cela affichera un menu déroulant permettant de définir le niveau de journalisation souhaité :

- **Erreurs uniquement** : Seules les erreurs sévères seront journalisées
- **Erreurs et avertissements** : Affiche également les avertissements moins urgents
- **Tout** : Affiche les erreurs, les avertissements et les messages de débogage de niveau info. C'est le réglage recommandé pour le dépannage.

{% note %}
TODO: Does this still work?
You can also access these options by holding the {% kbd opt  %} key when opening {% appmenu Help %} in the menu bar.
{% endnote %}

### Consulter le journal [viewing-the-log]

Une fois le **Mode débogage** activé, vous pouvez ouvrir le menu {% appmenu Help %} et sélectionner Ouvrir le journal de débogage. Cela ouvrira le journal de Marked dans Console.app, qui sera mis à jour en direct à mesure que des messages sont ajoutés pendant l'utilisation de Marked.

### Dépannage des règles personnalisées [troubleshooting-custom-rules]

[Les préprocesseurs et processeurs personnalisés](Custom_Processor.html) disposent de leur propre interface de journalisation. Sélectionnez {% appmenu Help, Show Custom Rules Log %} pour ouvrir la fenêtre. Cette fenêtre affiche un journal en couleur indiquant quelles règles ont correspondu et quelles commandes elles exécutent.

### Signaler un problème [reporting-an-issue]

Utilisez {% appmenu Help, Report an Issue %} pour ouvrir une fenêtre affichant vos réglages pour les paramètres les plus courants, ainsi qu'un modèle de rapport de bogue. Utilisez le bouton « Copier dans le presse-papiers » pour copier le contenu de la fenêtre, puis cliquez sur « Ouvrir le site d'assistance » pour ouvrir [le formulaire de nouvelle question](https://support.markedapp.com/questions/add), où vous pourrez coller votre rapport. Je m'efforce de répondre aux signalements sous 48 heures.
