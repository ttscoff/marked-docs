# <%= @title %>

La flexibilité est la clé.

## Menu Action [gear-menu]

![][4]

[4]: images/gearmenu.jpg @2x width=740px height=235px class=center

Le menu Action fournit la plupart des fonctionnalités de la barre de menus, ainsi que certaines fonctions spécifiques à l'aperçu. Cliquez simplement sur l'icône Action en bas à droite de la fenêtre pour accéder à ces fonctions.

## Rester au premier plan [keep-on-top]

![][5]

[5]: images/KeepOnTopPin.jpg @2x width=740px height=345px class=center

L'icône de verrouillage en bas à gauche amènera la fenêtre d'aperçu au premier plan et la maintiendra là (la fera flotter) lors du passage à d'autres applications. Vous pouvez définir une transparence sur la fenêtre dans le {% prefspane General %} qui permettra à la fenêtre de s'estomper lors de l'utilisation d'autres applications.

Cette fonctionnalité peut également être activée avec {% kbd shift-opt-cmd-f %}.

## Valeurs par défaut au niveau de la fenêtre [window-level-defaults]

Dans le {% prefspane General %}, vous pouvez utiliser « Conserver les nouvelles fenêtres en haut » pour définir les nouvelles fenêtres pour qu'elles restent toujours au-dessus des autres fenêtres, et/ou pour que les fenêtres s'élèvent en haut lorsque leur document associé est mis à jour. Les fenêtres configurées pour s'élever lors de la mise à jour ne « voleront pas le focus » de votre éditeur : elles s'élèveront uniquement pour devenir visibles, sans devenir actives.

## Afficher la source [view-source]

![][6]

[6]: images/view_source.jpg @2x width=740px height=345px class=center

Vous pouvez basculer entre les vues d'aperçu et de code source avec le bouton dans le coin supérieur droit. Cette vue peut également être basculée avec U.

## Recherche [search]

![][7]

[7]: images/SearchBarFull.jpg @2x width=818px height=195px class=center

La barre de recherche est accessible avec {% kbd cmd F %} et vous permet de rechercher dans l'aperçu un mot ou une phrase. Une fois la recherche effectuée, vous pouvez utiliser {% kbd cmd G %} et {% kbd shift cmd G %} pour naviguer vers l'avant et vers l'arrière dans des résultats supplémentaires.

Les cases à cocher sur le côté droit de la barre de recherche vous permettent d'affiner la recherche en fonction de la casse, des mots entiers uniquement et des expressions régulières. En plus de la recherche d'expressions régulières, les recherches par caractères génériques (*?) fonctionnent toujours, même lorsque l'option regex est désactivée.

Vous pouvez également entourer un terme ou une expression de recherche de barres obliques pour l'interpréter automatiquement comme une expression régulière (par exemple '/term.+?\b/').


Utilisez la fonction de recherche en combinaison avec la mise en favoris pour enregistrer les emplacements au fur et à mesure que vous les trouvez. Appuyez sur Tab ({% kbd ⇥ %}) pour concentrer le document, puis tapez Shift-[1-9] pour définir un signet sur ce numéro. Vous pouvez revenir au signet en tapant simplement le numéro (sans la touche Maj) ou en utilisant n/p pour les parcourir dans l'ordre des documents. N/P naviguera par ordre numérique. Pour les signets, la table des matières, la mini-carte et la recherche rapide d'en-tête, voir [Navigation dans le document](Document_Navigation.html). Consultez la section [Aperçu de la navigation](Keyboard_Shortcuts.html#previewnavigation) pour plus d'options, ou tapez "?" à tout moment dans l'aperçu.

> **Remarque :** La recherche ne peut pas passer d'un élément à l'autre, ce qui signifie qu'une chaîne de recherche ne peut pas continuer entre un paragraphe et un titre, entre les éléments d'une liste, etc.

Vous pouvez cocher les cases « Mots entiers », « Sensible à la casse » et « Regex » en utilisant respectivement {% kbd ctrl shift 1 %}, {% kbd 2 %} et {% kbd 3 %}.

### Recherche avancée ### [advanced-search]

Vous pouvez utiliser des caractères génériques dans une recherche non-regex. `*` correspondra à n'importe quelle série de caractères autres que des espaces et `?` correspondra à n'importe quel caractère unique.

Démarrer une recherche avec un `*` en fera une recherche de sélecteur jQuery. Vous pouvez utiliser n'importe quel sélecteur jQuery et tous les éléments correspondants seront mis en surbrillance et navigables avec {% kbd cmd G %} et {% kbd shift cmd G %}. Pour limiter la portée d'une recherche de texte à un certain type d'élément, ajoutez les termes de recherche entre guillemets doubles après la définition du sélecteur :

    *h2 "Alice"

C'est l'équivalent de `*h2:contains(Alice)`

## Navigation dans les documents (TOC, signets, Mini Map) [document-navigation-toc-bookmarks-mini-map]

La page [Navigation du document](Document_Navigation.html) couvre la table des matières (y compris l'ouverture du filtre avec {% kbd Space %}), la recherche rapide avec {% kbd f %}, les signets et la mini-carte.

## Navigation au clavier [keyboardnavigation]

La fenêtre d'aperçu peut être parcourue rapidement à l'aide de raccourcis clavier. Utilisez {% kbd j %} et {% kbd k %} pour monter et descendre, et maintenez la touche Shift ({% kbd J %}/{% kbd K %}) enfoncée pour vous déplacer plus rapidement. {% kbd t %} et {% kbd b %} se déplaceront en haut et en bas du document (tout comme {% kbd gg %} et {% kbd G %}, pour les fans de Vim). {% kbd u %} et {% kbd d %} se déplaceront d'une demi-page de haut en bas.

### Saut d'en-tête [header-jumping]

En appuyant sur les touches virgule ({% kbd , %}) et point ({% kbd . %}), vous passerez en arrière et en avant dans tous les en-têtes du document. Maintenir Shift ({% kbd shift  %}) permettra de sauter uniquement entre les en-têtes de niveau 1 et 2.


## Plein écran [full-screen]

Le mode plein écran peut être basculé à partir du menu Aperçu ou en tapant {% kbd ctrl cmd F %}.

## Cliquer sur des liens externes [clicking-external-links]

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Cliquer sur un lien externe dans l'aperçu de votre document l'ouvrira dans votre navigateur par défaut. Si vous cliquez et maintenez, lorsque vous relâchez, Marked vous proposera trois options : vous pouvez copier l'URL du lien dans votre presse-papiers, valider le lien ou ouvrir le lien dans votre navigateur par défaut. Cliquez simplement n'importe où dans votre aperçu pour fermer la fenêtre. Cette fonctionnalité peut être désactivée dans le {% prefspane Preview %} ("Activer les popovers de lien").

Voir une [vidéo de présentation sur YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Titres pliables ## [collapsibleheadlines]

Lorsque « Réduire les sections des titres » est activé dans le {% prefspane Preview %}, cliquer sur les titres réduira la section entre ce titre et le titre suivant au même niveau. Les sous-sections de cette section sont masquées. En option, vous pouvez limiter ce comportement à {% kbd cmd %} clics.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Maintenir enfoncé {% kbd opt  %} lorsque vous cliquez (ou {% kbd cmd %}-clic) développera/réduira toutes les sections enfants situées sous le titre cliqué. En maintenant la touche {% kbd shift  %} (Maj) enfoncée tout en cliquant, toutes les autres sections seront réduites au même niveau, révélant uniquement la section cliquée.

Les sections réduites sont marquées d'un surlignage jaune à droite du titre, et le curseur indiquera ce qui se passera lorsque vous cliquerez sur l'élément.

Si une modification est effectuée et doit être visible, ou si vous cliquez sur une section de table des matières qui se trouve actuellement dans une section réduite, les sections parent nécessaires seront développées pour la révéler.

Vous pouvez réduire/développer toutes les sections d'un document à la fois avec « Réduire toutes les sections » ({% kbd opt cmd left  %}) et « Développer toutes les sections » ({% kbd opt cmd right  %}).

Voir la [Vidéo de navigation dans les documents sur YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2) pour plus de détails.

## Indicateurs/bascules de processeur personnalisés ## [custom-processor-indicatorstoggles]

![][indicators]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Lorsque le processeur personnalisé et/ou le préprocesseur sont activés, des voyants lumineux apparaissent dans la barre d'outils. Ceux-ci peuvent être utilisés pour voir si le processeur est activé ou non pour le document actuel (l'indicateur sera mis en surbrillance) et cliquer dessus activera respectivement l'utilisation du préprocesseur et du processeur personnalisés.

## Faites défiler pour modifier [scrolltoedit]

La fonctionnalité « faire défiler pour modifier » dans Marked assure le suivi des différences entre la dernière mise à jour et la précédente, en essayant de trouver le point où vous avez effectué vos modifications les plus récentes. Marked suit toujours cela et une petite ligne rouge apparaît dans l'aperçu pour vous montrer l'emplacement du premier changement détecté. Dans le {% prefspane Preview %}, vous pouvez activer « Faire défiler jusqu'à la première modification » et lorsqu'un aperçu est mis à jour, il fera défiler doucement la vue jusqu'à cet emplacement.

Avec « Faire défiler jusqu'à la première modification » désactivé, vous pouvez toujours appuyer sur la touche « e » à tout moment dans l'aperçu pour accéder au dernier point de modification stocké.

## Défilement automatique [autoscroll]

Voir la page dédiée [Autoscroll](Autoscroll.html). Lorsque vous utilisez le défilement automatique comme téléprompteur, [une syntaxe spéciale peut insérer des pauses](Special_Syntax.html#pauses).

## Aperçu du zoom [zoom-overview]

Voir la page [Zoom Overview](Zoom_Overview.html) ({% kbd z %} dans l'aperçu ; fonctionne également en répétition de mots avec {% kbd ctrl cmd w %}).

## Référence Markdown [markdown-reference]

![][11]

[11]: images/markdown_reference.jpg @2x width=1148px height=267px class=center

Sélectionnez Référence Markdown dans le menu {% appmenu Help %} pour afficher un guide qui flotte au-dessus de vos autres fenêtres. C'est pratique pour ceux qui apprennent encore la syntaxe de Markdown. Vous pouvez ouvrir ce panneau via le clavier en utilisant {% kbd opt cmd M %}.

## Raccourcis clavier globaux [global-keyboard-shortcuts]

Dans le {% prefspane General %}, vous pouvez désigner un raccourci clavier personnalisé pour activer Marked, et un autre pour élever uniquement la fenêtre avant vers le haut sans quitter votre éditeur.
