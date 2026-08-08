# <%= @title %>

Options dans le {% prefspane Export %} :

(Voir [Exportation](Exporting.html) pour plus d'informations)

![Paramètres : Exporter][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Exporter le profil [export-profile]

Exporter le profil
: Sélectionnez un profil enregistré dans le menu contextuel. Les profils stockent un ensemble complet de préférences d'exportation pour une commutation rapide entre les flux de travail (par exemple, impression PDF ou Web HTML). Voir [Exporter des profils](Exporting.html#export-profiles).

Nouveau
: Créez un nouveau profil à partir des paramètres actuels.

Gérer
: Ouvrez le gestionnaire de profils pour renommer, dupliquer ou supprimer des profils.

### Imprimer/PDF [printpdf]

Désactiver les liens/surlignages lors de l'exportation de PDF ou de l'impression
: Supprime le formatage (souligné et couleur) des liens lors de l'impression.

Inclure l'URL comme annotation de texte
: Lors de l'impression ou de l'exportation d'un PDF, l'URL d'un lien apparaîtra après le texte lié.

Remplacer les règles horizontales par des sauts de page
: Transformez les règles horizontales du document en sauts de page (cela forcera en outre les notes de bas de page sur une nouvelle page).

Incorporer des images lors de la copie HTML
: Lorsqu'elle est activée, la copie du HTML dans le presse-papiers recherchera les images locales et les encodera en Base64 pour les inclure comme URL de données dans le code source.

Imprimer les couleurs et les images d'arrière-plan
: Par défaut, Marked s'imprimera/exportera avec un fond blanc. Si vous souhaitez inclure des couleurs d'arrière-plan et des images de thèmes personnalisés, activez cette option.

Empêcher les titres orphelins
: Cette option empêche les titres de la section suivante d'apparaître en bas d'une page sans laisser de place pour du contenu.

Exclure le premier H1
: Ignorez le premier titre de niveau un du document lorsque vous utilisez des H1 comme sauts de page.

Utiliser le premier H1 comme titre de secours
: Lorsque vous utilisez des applications comme Bear ou l'aperçu en streaming, cette option vous permet de remplacer le nom de fichier par le contenu du premier H1 du document. Si les métadonnées du « titre » sont spécifiées, elles auront toujours la priorité.

Ajouter des sauts de page avant
: Utilisez les en-têtes de niveau 1/2 comme séparateurs de section, en les commençant toujours sur une nouvelle page. Sélectionnez « Notes de bas de page » pour toujours ajouter un saut de page avant toute note de bas de page dans le document.

Indiquer les sauts de page en aperçu
: Affiche une ligne pointillée claire où les sauts sont insérés avec la syntaxe `<!--BREAK-->` ou en cochant les options de saut automatique dans les paramètres d'exportation.

Taille de police personnalisée pour l'exportation/impression
: Si défini, tout le texte sera mis à l'échelle en fonction du paramètre de point sélectionné (par défaut sur une base de 10 points).

Marges
: Définissez les marges d'impression (spécifiées en points) pour le haut, le bas, la gauche et la droite.

Imprimer la table des matières
: Inclure une table des matières automatique dans l'impression/PDF.

Saut de page après
: Passer automatiquement à une nouvelle page après une table des matières insérée.

Marqueurs de niveau de la table des matières
: Utilisez les listes déroulantes pour définir le marqueur d'élément de liste pour chaque niveau d'indentation dans une table des matières.

### En-têtes et pieds de page [headers-and-footers]

Configurez la police, le logo, les champs d'en-tête/pied de page, les formats de date et d'heure, l'inclusion de la première page, le décalage de numérotation des pages et les bordures. Les espaces réservés de champ incluent `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` et autres.

Voir [En-têtes et pieds de page](Exporting.html#headers-and-footers) dans [Exportation](Exporting.html) pour une référence d'espace réservé et des exemples. Voir [Formats de date et d'heure](Exporting.html#dateandtimeformats) pour les codes de format `%date` et `%time`.

Inclure sur la première page
: Si l'option d'en-tête et/ou de pied de page n'est pas cochée, la première page n'imprimera pas le type spécifié.

Format des dates
: Chaîne de format de style strftime pour `%date` dans les en-têtes et pieds de page. Voir [Formats de date et d'heure](Exporting.html#dateandtimeformats).

Format de l'heure
: Chaîne de format de style strftime pour `%time` dans les en-têtes et pieds de page. Voir [Formats de date et d'heure](Exporting.html#dateandtimeformats).

Décalage de la numérotation des pages
: Utilisé pour ajuster le numéro auquel commencent les numéros de page. Par exemple, si vous avez une table des matières sur la première page et que vous souhaitez que la numérotation commence sur la deuxième page, définissez le décalage sur -1. La page 2 sera désormais la page 1 et le nombre total de pages sera ajusté en conséquence.

Bordure
: Imprimez une ligne horizontale sous l'en-tête et/ou au-dessus du pied de page.

Restaurer les formats par défaut
: Réinitialisez les chaînes de format de date et d'heure aux valeurs par défaut de Marked (`%m-%d-%Y` et `%I:%M %p`). Voir [Formats de date et d'heure](Exporting.html#dateandtimeformats).
