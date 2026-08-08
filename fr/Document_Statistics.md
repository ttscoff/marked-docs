# <%= @title %>

Gardez une trace pendant que vous écrivez.

## Nombre de mots et statistiques de documents [word-count-and-document-statistics]

![][1]

[1]: images/WordCount.jpg @2x width=840px height=61px class=center

Le nombre de mots est situé dans la barre d'état inférieure et peut être activé et désactivé à partir du {% prefspane General %} sous la barre d'état. Vous pouvez afficher d'autres statistiques dans la fenêtre d'aperçu ou source à partir du menu Action, en cliquant sur le nombre de mots ou en tapant Option-Commande-S ({% kbd opt cmd S %}). Maintenez la touche Option ({% kbd opt  %}) enfoncée tout en cliquant pour afficher les statistiques de lisibilité, et maintenez la touche Option-Commande ({% kbd opt cmd %}) enfoncée pour ouvrir le panneau Statistiques avancées.

Si du texte est sélectionné, l'affichage du nombre de mots et la fenêtre contextuelle paragraphe/phrases/caractère seront mis à jour avec des informations uniquement pour la sélection.

## Nombre de mots pour la sélection [word-count-for-selection]

![Pop-up contextuel du nombre de mots lors de la sélection de texte][2]

[2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

Lorsque vous sélectionnez du texte dans l'aperçu, le nombre de mots en bas de la fenêtre affichera les statistiques pour le texte sélectionné uniquement.

Si « Afficher le nombre de mots pour la sélection » est activé dans le {% prefspane Preview %}, une petite fenêtre contextuelle apparaîtra à côté du curseur pour afficher le nombre de mots/lignes/caractères pour le texte sélectionné. Ceci est supprimé simplement en éloignant la souris de la fenêtre contextuelle.

La fonction de zoom est pratique pour sélectionner et obtenir rapidement des comptes pour des morceaux de texte plus volumineux. Tapez {% kbd z %} pour effectuer un zoom arrière et faire votre sélection.

## Statistiques de lisibilité [readability-statistics]

![Barre de statistiques de lisibilité][3]

[3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

Des statistiques supplémentaires de Flesch/Kincaid et du Fog Index sont disponibles avec {% kbd opt shift cmd S %}.

### Informations sur la lisibilité [readability-information]

**Facilité de lecture Flesch :** des scores plus élevés indiquent un matériel plus facile à lire ; les nombres inférieurs marquent les passages plus difficiles à lire.

**90,0--100,0** : élève moyen de 11 ans
**60,0--70,0** : étudiants de 13 à 15 ans
**0,0--30,0** : diplômés universitaires

**Niveau scolaire Flesch-Kincaid :** le nombre d'années d'études généralement requises pour comprendre ce texte.

**Indice Gunning Fog :** mesure la lisibilité de l'écriture anglaise. L'indice estime les années d'éducation formelle nécessaires pour comprendre le texte lors d'une première lecture. Un indice de brouillard de 12 nécessite le niveau de lecture d'un lycéen américain (environ 18 ans).

## Statistiques avancées [advanced-statistics]

![popup Statistiques avancées][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Sélectionner Statistiques avancées dans le menu Action, ou appuyer sur {% kbd cmd I %}, fait apparaître un panneau contenant des statistiques de document plus avancées, y compris la longueur moyenne des mots et des phrases et la complexité moyenne des mots.

### Statistiques avancées flottantes [floating-advanced-statistics]

![Fenêtre d'informations flottante][floating]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Appuyer sur {% kbd shift cmd I %} ouvrira un panneau flottant contenant toutes les statistiques détaillées et les informations de lisibilité. Ce panneau peut rester au premier plan lorsque vous basculez dans votre éditeur, afin que vous puissiez voir vos statistiques mises à jour à chaque fois que vous enregistrez, que l'aperçu soit visible ou non. En appuyant sur l'icône `<`, l'aperçu Marked associé sera ramené au premier plan. Si vous maintenez l'option enfoncée et cliquez sur le même bouton, cela ouvrira le fichier Markdown dans votre éditeur de texte par défaut (défini dans le {% prefspane Apps %}).

### Cibles de mots [word-targets]

Si vous avez un objectif spécifique pour le nombre de mots pendant que vous écrivez, vous pouvez ajouter une clé de métadonnées « cible : » en haut de votre document et Marked suivra votre progression, affichant un indicateur d'achèvement dans le panneau Statistiques détaillées ({% kbd cmd I %}) et dans les statistiques flottantes ({% kbd shift cmd I %}).

![][targetwordcount]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Visualisez la répétition des mots [visualizewordrepetition]

En sélectionnant Visualiser la répétition de mots dans le menu Action (ou en appuyant sur {% kbd ctrl cmd W %}), vous passerez à une vue spéciale qui supprimera les éléments non textuels et mettra en évidence les mots répétés dans votre document. Les mots répétés sont surlignés en rose clair et le survol d'un mot en surbrillance éclaircira les mots correspondants dans tout le document. Cliquer sur un mot en surbrillance assombrit l'arrière-plan et « colle » le surlignage pour un examen plus approfondi.

![Répétition de mots][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

Vous pouvez également utiliser la fonction « zoom » (tapez « z ») dans ce mode, vous permettant de mettre en surbrillance un mot répété, puis de numériser rapidement l'ensemble du document pour voir où les répétitions sont concentrées.

Les mots sont comparés par leur « radical », ce qui signifie que « partie », « en partie » et « parties » seront considérés comme des mots répétés. Cela tient compte des syllabes et de la conjugaison lors de la vérification de la densité de répétition.

**Portée**

La portée du contrôle de répétition peut être modifiée dans la barre d'outils inférieure du document et peut être définie sur Document ou Paragraphe. Le mode Document est celui par défaut ; la sélection de Paragraphe ne compte que les répétitions dans chaque bloc de texte. Les répétitions seront toujours mises en évidence dans l'ensemble du document, mais uniquement comptées si un mot apparaît plus d'une fois dans un seul paragraphe.

**Ignorer les mots**

Vous pouvez exclure temporairement un mot et toutes ses différentes conjugaisons et pluralisations en faisant Option-clic sur le mot en surbrillance. Les mots temporairement ignorés apparaîtront dans le coin inférieur droit de l'aperçu. Cliquer sur un mot dans la liste des mots ignorés le restaurera dans la visualisation.

Pour ignorer définitivement les mots, vous pouvez modifier une liste dans le {% prefspane Proofing %} sous l'onglet Ignorer les répétitions. Les mots (ou radicaux de mots) ajoutés un par ligne dans cette liste seront toujours ignorés. Pour ajouter automatiquement un mot à cette liste, faites Option-Maj-clic sur ce mot dans la visualisation de répétition de mots.

**Quitter le mode répétition de mots**

Vous pouvez fermer la vue de répétition de mots à l'aide de l'icône Fermer à côté du sélecteur de portée dans la barre d'outils inférieure ou en appuyant sur Échap.
