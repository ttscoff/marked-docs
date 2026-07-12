# <%= @title %>

Options du panneau {% prefspane Advanced %} :

![Paramètres : Avancé][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

Métadonnées YAML et Pandoc
: - __Ignorer :__ Les laisse exactement telles qu'elles existent dans le document, utile si votre processeur ou préprocesseur utilise réellement le YAML.
: - __Supprimer avant le rendu :__ Le bloc YAML est retiré.
: - __Traiter comme métadonnées MMD :__ Convertit le bloc de métadonnées YAML ou Pandoc au format MultiMarkdown.

Supprimer les en-têtes de métadonnées MultiMarkdown
: Si cette option est activée, les métadonnées MultiMarkdown situées en haut du document seront supprimées avant le rendu.
: Cela peut être utile si vous utilisez un processeur autre que MultiMarkdown qui afficherait sinon les métadonnées dans le document rendu. Les métadonnées sont tout de même lues avant leur suppression, la syntaxe propre à Marked continuera donc d'être reconnue.

Mettre en cache les images hébergées
: Par défaut, Marked ne met pas en cache les images dans l'aperçu, car il surveille ces images pour détecter leurs modifications et les met à jour instantanément. Si vous utilisez des images référencées via une URL web, vous pouvez activer la mise en cache de ces images pour accélérer le rendu sur les connexions plus lentes.

Analyser les statistiques de lisibilité
: Si vous préférez ne pas faire calculer les [statistiques](Document_Statistics.html), cette option désactive ce traitement. Cela peut apporter des gains de performance sur les documents très volumineux. Le comptage des caractères, des mots et des phrases continuera de fonctionner.

Utiliser le presse-papiers de recherche du système
: Cette option permet à Marked de reprendre le dernier terme de recherche utilisé dans une autre application d'édition, et toute recherche effectuée dans Marked deviendra également la recherche dans les autres applications. La désactiver permet à la fonction de recherche de Marked de fonctionner de manière indépendante.

Utiliser {% kbd cmd E %} pour « Rechercher avec la sélection »
: Par défaut, {% kbd cmd E %} ouvre l'éditeur par défaut. Si cette option est activée, {% kbd cmd E %} fonctionnera comme dans la plupart des applications d'édition de texte, en utilisant le texte sélectionné pour la recherche ; l'ouverture dans l'éditeur peut alors être déclenchée avec {% kbd opt cmd E %}.

Mode débogage
: Active la journalisation de débogage. Utilisez cette option pour vos propres dépannages, ainsi que lors du signalement d'un problème. Sélectionnez __Aide -> Ouvrir le journal de débogage__ pour consulter l'activité.
: Le réglage sur _Tout_ affichera les messages d'information, les avertissements et les messages d'erreur. Vous pouvez également le régler pour n'afficher que les erreurs, ou les erreurs et les avertissements.

Sauvegarde des paramètres
: Vous pouvez sauvegarder vos réglages dans un fichier JSON pouvant être utilisé pour les restaurer ou les transférer vers une nouvelle machine.
