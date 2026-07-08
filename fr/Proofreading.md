# <%= @title %>

Activez le mode de relecture depuis le menu Action. Il s'agit d'une fonctionnalité expérimentale conçue principalement pour les éditeurs qui reçoivent du texte d'autres personnes et doivent faire des commentaires et donner leur avis.

Le mode de relecture fige les mises à jour du document, ce qui évite que les annotations et les notes soient perdues lors de l'actualisation du document. Un indicateur rouge apparaît dans la barre supérieure pour vous rappeler que le mode de relecture est actif.

La navigation au clavier, la mise en favoris et la mise en évidence des mots clés fonctionnent toutes pendant la relecture.

## Annotations

En mode de relecture, sélectionner du texte dans le document fait apparaître une fenêtre contextuelle qui vous permet de choisir parmi plusieurs types de surbrillance. Cliquez sur le type de surbrillance que vous souhaitez ajouter au texte, ou annulez en cliquant sur le bouton « Annuler » ou simplement en cliquant en dehors de la fenêtre contextuelle.

## Notes

![Annotations][1]

[1]: images/Annotating.jpg class=center

Une fois une surbrillance ajoutée, vous pouvez y ajouter de courtes notes en cliquant dessus. La fenêtre contextuelle contiendra alors un champ de texte où vous pouvez saisir toute note pertinente pour le texte en surbrillance. Les notes peuvent être supprimées et modifiées en cliquant sur une surbrillance qui possède déjà une note.

Les notes ne sont exportées **que** lors de l'enregistrement au format HTML. Les surbrillances restent présentes dans la plupart des formats d'exportation, y compris RTF et PDF.

## Vérification orthographique

En mode de relecture, vous pouvez accéder au correcteur orthographique du système depuis le menu Action : {% appmenu {{gear}}, Proofing, Show Spelling Errors %}. Cela sera lent sur les documents volumineux, et un avertissement s'affichera pour vous prévenir si le traitement doit prendre plus de 30 secondes environ. Comme le correcteur orthographique ne fonctionne pas dans l'aperçu web de Marked, une « astuce » a été mise en place pour que cela fonctionne, et ce n'est pas la plus rapide.

Une fois la vérification orthographique effectuée, vous pouvez ouvrir le panneau des suggestions orthographiques pour activer la vérification grammaticale ainsi que voir les suggestions de correction des erreurs. Marked *ne peut pas* modifier ces éléments directement dans le document, vous devez retourner à votre document original pour exploiter les résultats.

*Raccourcis :* {% kbd ctrl opt cmd S %} lancera le correcteur orthographique. {% kbd ctrl opt cmd N %} passera à l'erreur suivante dans le document, et {% kbd ctrl opt cmd G %} affichera le panneau des suggestions.
