# <%= @title %>

Options du panneau de préférences {% prefspane Proofing %} :

![Paramètres : Relecture][1]

[1]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane-scroll

Toujours ouvrir les nouveaux documents en mode relecture
: Les nouveaux documents afficheront par défaut la mise en évidence des mots-clés.

Activer automatiquement CriticMarkup
: Active automatiquement le traitement [CriticMarkup](CriticMarkup.html) lorsqu'une syntaxe appropriée est détectée.

Mettre en évidence les erreurs de syntaxe Markdown
: Met en évidence les liens Markdown incorrects et les autres balisages qui pourraient avoir été mal convertis.

Afficher la barre latérale des commentaires par défaut
: Ouvre la barre latérale des commentaires lorsqu'un document contenant des commentaires ou des annotations est chargé.

Inclure les notes de bas de page dans la barre latérale des commentaires
: Lorsque la barre latérale des commentaires est ouverte, inclut les notes de bas de page en plus des commentaires. Si cette option est désactivée, seuls les commentaires (CriticMarkup, Fountain, Word et similaires) apparaissent dans la barre latérale.

Vitesse de lecture (mpm)
: Ce nombre (mots par minute) est utilisé pour calculer le temps de lecture affiché dans les statistiques du texte. La vitesse de lecture moyenne d'un adulte se situe entre 200 et 300 mots par minute.

### Mots-clés

[Définissez des listes de mots-clés à mettre en évidence](Keyword_Highlighting.html). Utilisez les onglets pour modifier chaque liste :

Éviter
: Mots et expressions (un par ligne) à signaler comme surutilisés ou à revoir. La correspondance ne tient pas compte de la casse et doit porter sur des mots ou expressions complets.

Utiliser une alternative
: Suggère une formulation alternative pour les expressions listées.

Mettre en évidence
: Met en évidence des mots ou expressions arbitraires pour les faire ressortir pendant la relecture.

Ignorer les répétitions
: Mots à exclure de l'analyse **Visualiser les répétitions de mots** (un par ligne).

Restaurer les expressions par défaut
: Réinitialise la liste de mots-clés actuelle aux valeurs par défaut de Marked (par exemple, la liste à éviter de la [Plain English Campaign](http://www.plainenglish.co.uk)).
