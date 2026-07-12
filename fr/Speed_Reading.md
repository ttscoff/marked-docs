# <%= @title %>

Lecture rapide est un mode de lecture de type RSVP qui affiche un mot à la fois dans une incrustation dédiée.

## Fonctionnement de Lecture rapide

Lecture rapide utilise une méthode appelée **présentation visuelle sérielle rapide** (RSVP, *Rapid Serial Visual Presentation*). Plutôt que de déplacer vos yeux le long des lignes de texte, les mots apparaissent à une position fixe. Cela réduit les mouvements oculaires, les changements de ligne et les retours en arrière qui se produisent normalement pendant la lecture, ce qui peut s'avérer utile pour survoler un texte, revoir un contenu déjà familier, ou parcourir rapidement un texte sans en perdre le fil.

Cette méthode n'a rien de magique et ne garantit pas une meilleure compréhension à des vitesses très élevées. La compréhension en lecture dépend toujours de la complexité du texte, de votre familiarité avec le sujet, et du réglage de vitesse en mots par minute. Pour un contenu dense ou peu familier, une vitesse modérée est généralement plus efficace que de pousser le rythme au maximum.

La lettre rouge marque le point d'ancrage visuel du mot, parfois appelé le **point de reconnaissance optimal**. Pour de nombreux mots, les lecteurs identifient le mot le plus efficacement lorsque leur regard se pose légèrement à gauche du centre plutôt que sur la première lettre. En conservant ce point d'ancrage au même endroit et en le mettant en évidence, Lecture rapide offre à votre œil une cible constante. Il en résulte moins de changements de point focal entre les mots, et un rythme plus régulier à mesure que le texte avance.

## Ouvrir Lecture rapide

Utilisez **Aperçu > Lecture rapide**, l'élément **Lecture rapide** du menu Action de la fenêtre d'aperçu, ou appuyez sur {% kbd ctrl opt S %}. Cet élément de menu est disponible lorsqu'une fenêtre d'aperçu Markdown est active (il est désactivé pour les aperçus HTML bruts et lorsqu'aucun document n'est ouvert).

À l'ouverture, Lecture rapide démarre en pause, afin que vous puissiez vous orienter avant le début de la lecture.

<video controls preload="metadata" poster="images/speedread-poster.png">
  <source src="images/speedread.webm" type="video/webm">
  <source src="images/speedread.mp4" type="video/mp4">
  Votre navigateur ne prend pas en charge la vidéo de démonstration de Lecture rapide.
</video>
<p><em>Incrustation Lecture rapide montrant les contrôles de lecture, l'option de synchronisation et l'accès à l'aide.</em></p>

## Contrôles de l'incrustation

Une fois l'incrustation affichée, les touches suivantes sont disponibles :

| Raccourci | Fonction |
| :-- | :-- |
| {% kbd space %} | Lecture/Pause |
| {% kbd [ %} | Aller au début du paragraphe (appuyez à nouveau pour le paragraphe précédent) |
| {% kbd ] %} | Aller au début du paragraphe suivant |
| {% kbd left %} | Diminuer la vitesse de lecture (mpm) |
| {% kbd right %} | Augmenter la vitesse de lecture (mpm) |
| {% kbd esc %} | Quitter Lecture rapide |

Les crochets sont capturés pour la navigation entre paragraphes, et les flèches gauche/droite sont capturées pour les changements de vitesse : ces touches ne déclenchent donc pas la navigation de l'aperçu tant que Lecture rapide est ouvert. Vous pouvez également cliquer sur le bouton circulaire **X** dans le coin supérieur gauche de l'incrustation pour la fermer.

Les autres raccourcis de navigation habituels de l'aperçu fonctionnent toujours pendant que Lecture rapide est actif, y compris `t`/`gg` (haut), `G`/`b` (bas), et `,`/`.` (navigation entre titres). Voir [Navigation dans l'aperçu](Keyboard_Shortcuts#preview-navigation) pour la liste complète.

La table des matières peut également être utilisée pendant la Lecture rapide. Appuyez sur {% kbd cmd t %} pour l'ouvrir et naviguer, ou appuyez sur {% kbd f %} pour donner immédiatement le focus à la recherche rapide afin de naviguer entre les titres du document.

## Démarrer à partir d'une sélection

Si du texte est sélectionné dans l'aperçu au moment où vous démarrez Lecture rapide, la lecture utilise le texte sélectionné. En l'absence de sélection, Lecture rapide utilise l'intégralité du texte du document.

## Synchronisation avec la position de défilement

Activez **Synchroniser la lecture rapide avec la position de défilement** dans {% prefspane Preview %}, ou utilisez la case à cocher de l'incrustation Lecture rapide, pour garder l'aperçu et la position de Lecture rapide synchronisés.

Lorsque cette option est activée, Lecture rapide démarre au contenu actuellement visible en haut de l'aperçu, plutôt qu'au début du document. À mesure que la lecture avance, l'aperçu défile en même temps que les mots affichés.

Si vous fermez Lecture rapide, faites défiler l'aperçu, puis rouvrez l'incrustation, la lecture démarre à partir de la nouvelle position visible. Si vous activez la case à cocher de l'incrustation alors que Lecture rapide est déjà ouvert, la lecture se réinitialise sur la position de défilement actuelle et se poursuit à partir de là.

## Vitesse mémorisée

La valeur en mpm est enregistrée automatiquement lorsque vous la modifiez avec {% kbd ← %} et {% kbd → %}. La vitesse choisie est restaurée la prochaine fois que vous utilisez Lecture rapide.
