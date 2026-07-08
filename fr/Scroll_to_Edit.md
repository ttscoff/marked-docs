# <%= @title %>

La fonctionnalité de défilement vers la modification de Marked suit les différences entre la dernière mise à jour et la précédente, afin de repérer l'endroit où vous avez effectué votre dernière modification. Marked effectue toujours ce suivi, et un petit trait rouge apparaît dans l'aperçu pour indiquer l'emplacement de la première modification détectée. Dans le panneau de préférences Comportement, vous pouvez activer « Défiler vers la première modification » : lorsque l'aperçu se met à jour, la vue défilera alors doucement jusqu'à cet emplacement.

Si « Défiler vers la première modification » est désactivé, vous pouvez toujours appuyer sur la touche « e » à tout moment dans l'aperçu pour accéder au dernier point de modification enregistré.


### Remarques sur le défilement vers la modification

Cette fonctionnalité est excellente lorsqu'elle fonctionne bien, mais elle comporte de nombreuses subtilités. En particulier lors des toutes premières mises à jour du document, le défilement peut sembler saccadé. Si vos modifications se trouvent toutes à l'intérieur d'un seul élément très volumineux (un paragraphe excessivement long, par exemple), le repère ne pourra que s'en approcher. De même, si vous ajoutez un ou deux mots à la fin du document, le marqueur de modification restera positionné dans l'élément précédent tant qu'il n'y aura pas assez de contenu pour s'ancrer dans le nouvel élément.
