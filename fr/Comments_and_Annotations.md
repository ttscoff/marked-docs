# <%= @title %>

Marked a une gestion particulière des commentaires et annotations.

## Sources d'annotations

Marked reconnaît les commentaires provenant de :

- notes de bas de page Markdown
- commentaires CriticMarkup
- commentaires et modifications Microsoft Word

## La barre latérale des commentaires

Toutes les annotations sont affichées dans une barre latérale et masquées dans l'aperçu du document. Pour afficher la barre latérale des annotations, utilisez **Menu Action → Relecture → Afficher les commentaires**, ou appuyez sur {% kbd ctrl cmd C %}.

![Une note de bas de page dans la barre latérale des commentaires][barre latérale]

[barre latérale]: images/comment-sidebar-800.jpg @2x width=800

Passer la souris sur un commentaire dans la barre latérale tracera une ligne vers son emplacement dans le document. Dans le cas des notes de bas de page, cela indiquera l'endroit où la note de bas de page apparaît dans le texte. Dans le cas des commentaires, elle pointera vers l'emplacement d'origine du commentaire, qui peut être un espace vide dans l'aperçu.

Cliquer sur un commentaire dans la barre latérale déclenche une animation de surbrillance pointant vers son emplacement.

La police et le style de la barre latérale dépendent du style actuel, ils peuvent donc être différents selon les styles.
