# <%= @title %>

Cette page décrit comment parcourir les aperçus longs : la [Table des matières](#table-of-contents), la [recherche rapide](#fast-search), les [signets](#bookmarks-and-mini-map) et la [Mini carte](#minimap). Pour les raccourcis de défilement qui s'appliquent partout (tels que {% kbd j %}/{% kbd k %}), voir [Navigation au clavier](Interface_Features.html#keyboardnavigation) sous [Fonctionnalités de l'interface](Interface_Features.html).

## Table des matières [table-of-contents]

![][8]

[8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Si votre document contient des en-têtes, un bouton de liste apparaît dans la barre d'outils. Cliquez dessus pour développer la table des matières ; cliquez sur un titre pour accéder à cette section de l'aperçu. Utilisez {% kbd j %}/{% kbd k %} (bas/haut) pour vous déplacer dans la liste, et {% kbd Enter %} ou {% kbd o %} pour accéder à l'en-tête en surbrillance.

**Barre de filtre :** Avec la table des matières ouverte, appuyez sur {% kbd Space %} (barre d'espace) pour ouvrir le champ de saisie anticipée. Tapez n'importe quelle partie d'un nom de titre (Marked utilise la correspondance de style TextMate : par exemple, vous pouvez taper la première lettre de chaque mot) et appuyez sur Tab ({% kbd ⇥ %}) ou sur la flèche vers le bas ({% kbd ↓ %}) pour vous déplacer dans la liste filtrée.

Appuyer sur {% kbd cmd T %} ouvre (ou ferme) également la table des matières.

Si ["Réduire les sections des titres"](Interface_Features.html#collapsibleheadlines) est activé dans le {% prefspane General %}, maintenir la touche Commande tout en cliquant sur un élément de la table des matières réduira ou développera cette section, révélant les sections parent si nécessaire.

En mode plein écran, la table des matières apparaît sous la forme d'une barre latérale fixe au lieu d'un menu contextuel. Pour utiliser cette mise en page dans un aperçu fenêtré normal, utilisez la bascule plein écran en bas à droite du panneau TOC.

![Basculer en plein écran][12]

[12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Pour une liste condensée de touches, voir [Raccourcis clavier](Keyboard_Shortcuts.html#TableofContentsNavigation).

Voir également la [Vidéo de navigation dans les documents sur YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Mode plein écran pour la table des matières [full-screen-mode-for-the-table-of-contents]

Lorsqu'une fenêtre d'aperçu Marked est en plein écran, la table des matières peut rester fixe sur la gauche pour une navigation constante. Il bascule toujours avec {% kbd cmd T %} ; cliquer en dehors de la table des matières ne la fera souvent pas disparaître dans cette mise en page.

Dans une fenêtre normale, cliquez sur l'icône en bas du panneau TOC pour l'ancrer en tant que barre latérale ; cliquez sur l'icône en haut de la barre latérale pour la remettre en mode contextuel.

### Personnalisation de l'endroit où la table des matières apparaît [customizing-where-the-toc-appears]

La Table des Matières peut être injectée dans le document exporté en utilisant la [syntaxe spéciale](Special_Syntax.html#tableofcontents) `<!--TOC-->`.

Ajoutez `max#` (par exemple `<!--TOC max2-->`) pour limiter le nombre de niveaux de titre qui apparaissent.

## Recherche rapide [fast-search]

**Navigation rapide** combine la table des matières avec le filtre ciblé afin que vous puissiez sauter avec un minimum de saisie :

- Appuyez sur {% kbd f %} dans l'aperçu pour ouvrir la table des matières avec le **champ de filtre focalisé** (même idée que d'ouvrir la table des matières puis d'appuyer sur {% kbd Space %}, sans l'étape supplémentaire).
- Tapez une partie de n'importe quel titre de titre ; la liste filtre les correspondances.
- S'il ne reste qu'un seul titre, appuyer sur Retour ({% kbd ↩ %}) permet d'y accéder directement.
- S'il reste plusieurs titres, appuyez sur Tab ({% kbd ⇥ %}) pour quitter le champ de filtre, déplacez-vous avec {% kbd j %}/{% kbd k %} ou les touches fléchées, puis appuyez sur {% kbd o %} ou Retour ({% kbd ↩ %}) pour accéder au titre et fermer la table des matières.
- L'onglet renvoie à nouveau le focus sur le champ de recherche.

> **Rappel de raccourci :** Ouvrir la table des matières et appuyer sur {% kbd Space %} ouvre la barre de filtre, pratique lorsque la table des matières est déjà visible.

(Les documents précédents appelaient cela « Fast Switcher » ; il s'agit de la même fonctionnalité.)

## Signets et mini-carte [bookmarks-and-mini-map]

Utilisez le menu d'aperçu {% appmenu Gear %} et la touche {% kbd Tab %} ({% kbd ⇥ %}), qui bascule le focus entre le document et le champ de [recherche](Interface_Features.html#search), pour placer et retrouver des signets pendant que vous parcourez le document.

### Définir des favoris [setting-bookmarks]

Définissez les signets sur la position de défilement en utilisant {% kbd shift 1 %}--{% kbd shift 9 %} et revenez en arrière en utilisant {% kbd 1 %}--{% kbd 9 %} seul. Utilisez {% kbd n %} et {% kbd p %} pour suivant/précédent dans **l'ordre des documents** ; {% kbd shift n %} et {% kbd shift p %} pour le suivant/précédent dans l'ordre **numérique**.

La modification du style ou de la taille de la page peut se déplacer là où un signet apparaît. Les signets sont conçus comme des aides à la révision temporaires : ils ne persistent pas entre les sessions de document, mais ils survivent aux actualisations et aux modifications de l'aperçu.

**Signets de titre :** Maintenez Option enfoncée et appuyez sur {% kbd opt 1 %}--{% kbd opt 9 %} pour ajouter le titre le plus proche du haut de la fenêtre (ou le dernier titre avant le haut) aux favoris.

**Prochain emplacement libre :** {% kbd cmd D %} (ou la touche accent grave {% kbd \`\` %}, pour les utilisateurs de vim) ajoute un signet dans le prochain emplacement numéroté disponible.

Appuyez sur {% kbd 0 %} pour développer la bande de signets (les titres des titres le cas échéant). Lorsque la [Mini Map](#minimap) est activée, {% kbd 0 %} l'affiche en même temps. Appuyez à nouveau sur Échap ou sur {% kbd 0 %} pour réduire.

Appuyez deux fois sur {% kbd x %} ({% kbd xx %}) pour effacer tous les favoris.

Il existe [plus de raccourcis d'aperçu](Keyboard_Shortcuts.html) ; appuyez sur {% kbd h %} dans l'aperçu pour une liste tête haute, ou sur {% kbd opt cmd K %} pour la référence complète.

### Mini-carte [minimap]

Si la mini-carte est activée dans les paramètres {% prefspane Preview %}, {% kbd 0 %} ouvre une vignette mise à l'échelle de l'ensemble du document le long de la bande de signets. Cliquez n'importe où sur la carte pour y faire défiler l'aperçu complet. Les signets enregistrés apparaissent sous forme de lignes horizontales avec des chiffres (et des titres le cas échéant).

Maintenez **Commande** et déplacez-vous sur la mini-carte pour obtenir une loupe agrandie ; maintenez **Option** et faites glisser pour faire défiler comme si vous faisiez glisser la barre de défilement.

La carte se régénère lorsque la taille ou la disposition de la fenêtre change. Sur les documents très longs, appuyer une fois sur {% kbd 0 %} peut prendre un moment ; Marked évite de créer automatiquement la mini-carte lors du chargement initial jusqu'à ce que vous le demandiez.

Appuyez sur {% kbd 0 %} ou Échap pour fermer la mini-carte.

**Remarque sur les performances :** La génération de la carte peut suspendre brièvement l'aperçu de documents volumineux ; cela ne s'exécute que lorsque la carte est visible ou après un redimensionnement.

### Aperçu du zoom (connexe) [zoom-overview-related]

Pour un aperçu à l'échelle du texte sans la mini-carte, voir [Aperçu du zoom](Zoom_Overview.html) ({% kbd z %}).
