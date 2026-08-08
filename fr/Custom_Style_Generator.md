# <%= @title %>

Le générateur de styles personnalisés est un outil Web qui vous permet de créer des styles personnalisés pour Marked sans écrire manuellement du CSS. Il fournit une interface visuelle avec des contrôles pour la typographie, les couleurs, l'espacement, etc., avec un aperçu en direct qui se met à jour à mesure que vous apportez des modifications.

## Accéder au générateur [accessing-the-generator]

Le générateur de styles est disponible sur [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/). Vous pouvez l'utiliser directement dans votre navigateur Web, aucune installation requise.

![Générateur de styles][img-style-generator]

[img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Pour commencer [getting-started]

Lorsque vous ouvrez le générateur pour la première fois, vous verrez :

- **Volet d'aperçu** (à gauche) : un aperçu en direct de votre style appliqué à un exemple de contenu markdown
- **Volet Contrôles** (à droite) : Tous les contrôles de style organisés en sections
- **Barre d'outils** (en haut) : titre du style, sélecteur de thème de base et option d'importation CSS

### Choisir un thème de base [choosing-a-base-theme]

Commencez par sélectionner un **Thème de base** dans la liste déroulante. Cela constitue une base pour votre style : vous pouvez ensuite en personnaliser chaque aspect. Les options populaires incluent Blank (pour repartir de zéro), Default et divers thèmes intégrés.

### Importation de CSS existants [importing-existing-css]

Si vous disposez d'un fichier CSS existant que vous souhaitez utiliser comme point de départ, cliquez sur **Importer CSS** et sélectionnez votre fichier. Le générateur chargera ces styles et vous pourrez ensuite les modifier à l'aide des commandes.

## Contrôles de style [style-controls]

Le générateur organise les contrôles en sections logiques :

### Typographie de base [base-typography]

Contrôlez les paramètres de typographie fondamentaux :

- **Utiliser le rythme** : lorsqu'il est activé, utilise une échelle typographique mathématique pour des tailles et un espacement de titre cohérents.
- **Taille de police de base** : la taille de police racine (généralement 16 px)
- **Hauteur de ligne** : L'espacement entre les lignes de texte
- **Rapport d'échelle** : Le rapport utilisé pour l'échelle typographique (affecte la taille des titres)

### Disposition [layout]

Ajustez l'espacement et l'indentation :

- **Marge intérieure du conteneur** : espace autour de la zone de contenu
- **Retrait du paragraphe** : retrait de la première ligne des paragraphes
- **Retrait de liste** : Indentation pour les listes
- **Retrait de citation** : Marge gauche pour les blockquotes

### Polices [fonts]

Configurez les familles de polices et les épaisseurs :

- **Polices d'en-tête** : liste de polices séparées par des virgules pour les titres (par exemple, "Georgia, serif")
- **Polices du corps** : liste de polices séparées par des virgules pour le corps du texte
- **Poids de l'en-tête** : poids de la police pour les titres (100 à 900)
- **Poids corporel** : poids de la police pour le corps du texte
- **Poids gras** : poids de la police pour le texte en gras
- **Espacement des lettres** : espacement des caractères pour les en-têtes et le corps du texte

### Polices Google [google-fonts]

Ajoutez des polices Google à votre style :

1. Tapez un nom de police dans le champ de recherche (des suggestions de saisie semi-automatique apparaissent)
2. Spécifiez éventuellement les styles (par exemple, "400,400i,700" pour régulier, italique, gras)
3. Cliquez sur **Ajouter** pour l'inclure
4. Utilisez **Parcourir Google Fonts** pour explorer le catalogue complet avec des aperçus

Les polices ajoutées apparaissent dans une liste sous les contrôles ; cliquez sur le × pour les supprimer.

### Couleurs [colors]

Définir les couleurs pour divers éléments :

- **Arrière-plan** : Couleur d'arrière-plan de la page
- **Texte de base** : Couleur du texte par défaut
- **Couleur de l'en-tête** : couleur de tous les titres (peut être remplacée par niveau de titre)
- **Couleur du corps du texte** : couleur du corps du texte
- **Couleur des liens** : Couleur des liens
- **Couleur d'accentuation** : Couleur du texte souligné (`<em>`)
- **Couleur du texte fort** : Couleur pour un texte fort (`<strong>`)
- **Arrière-plan du texte surligné** : Couleur d'arrière-plan pour le texte en surbrillance (`<mark>`)

Les couleurs d'en-tête individuelles (H1 à H6) peuvent être définies séparément : utilisez **Réinitialiser** pour effacer un remplacement et revenir à la couleur d'en-tête.

### Mode sombre [dark-mode]

Activez le **Mode sombre** pour prévisualiser et configurer les couleurs du mode sombre. Lorsqu'il est activé, vous verrez des commandes de couleur distinctes pour les variantes du mode sombre. Les styles du mode sombre s'appliquent lorsque `.inverted` est défini sur l'élément body dans Marked.

Utilisez **Générer des couleurs** pour créer automatiquement une palette en mode sombre basée sur les couleurs de votre mode clair.

### Images [images]

Contrôler l'apparence de l'image :

- **Largeur maximale** : largeur maximale des images (par exemple, "100 %", "800 px")
- **Rayon de bordure** : coins arrondis (par exemple, "8px", "0")
- **Alignement** : document par défaut, gauche, centre ou droite

### Citations [blockquotes]

Citations de style :

- **Largeur de la bordure gauche** : épaisseur de la bordure gauche
- **Couleur de la bordure gauche** : Couleur de la bordure gauche
- **Couleur d'arrière-plan** : Couleur d'arrière-plan pour les guillemets
- **Style de police** : Normal ou Italique
- **Marge gauche** : espacement à partir du bord gauche
- **Marge gauche imbriquée** : espacement pour les guillemets imbriqués (peut être "hérité")

Des contrôles séparés sont disponibles pour les blockquotes en mode sombre.

### Listes [lists]

Configurer l'apparence de la liste :

- **Position du style de liste** : à l'intérieur ou à l'extérieur (là où les puces/numéros apparaissent)
- **Marge gauche** : espacement à partir du bord gauche
- **Marge gauche imbriquée** : espacement pour les listes imbriquées (peut être "hériter")

### Listes de définitions [definition-lists]

Listes de définitions de styles (`<dl>`, `<dt>`, `<dd>`) :

- **Retrait DL** : indentation globale
- Paramètres **DT** (terme) : taille, épaisseur et style de police
- Paramètres **DD** (définition) : taille, épaisseur, style et indentation de la police

### Tableaux [tables]

Style de table complet :

- **Couleur d'arrière-plan** : arrière-plan du tableau
- **Couleur de bordure** : Couleur de bordure pour les cellules
- **Couleur du texte du tableau** : Couleur du texte par défaut dans les tableaux
- **Lignes/colonnes alternées** : activez les rayures zébrées avec des couleurs personnalisées
- **Bordure** : Afficher/masquer le contour du tableau
- **Grille** : Afficher/masquer les lignes de grille internes
- **Alignement** : Gauche ou Centre
- **Rayon de bordure** : coins arrondis
- **Largeur maximale** : largeur maximale du tableau
- **Marge intérieure des cellules** : espacement interne
- Paramètres **En-tête** : épaisseur, taille et style de la police
- Paramètres **Légende** : épaisseur, taille, style et couleur du texte de la police

Des contrôles séparés sont disponibles pour les tableaux en mode sombre.

### Blocs de code [code-blocks]

Blocs de code de style et code en ligne :

- **Famille de polices de code** : pile de polices monospace
- **Arrière-plan** : Couleur d'arrière-plan
- **Couleur de la bordure** : Couleur de la bordure
- **Rayon de bordure** : coins arrondis
- **Mode de retour à la ligne** : Aucun retour à la ligne (`pre`), Conserver + retour à la ligne (`pre-wrap`), ou Normal (`wrap`)
- **Marge intérieure du code** : espacement interne

Des commandes séparées sont disponibles pour les blocs de code du mode sombre.

### Notes de bas de page [footnotes]

Notes de bas de page de style :

- **Couleur des marqueurs** : Couleur des marqueurs de notes de bas de page
- **Couleur du texte** : Couleur du texte de la note de bas de page
- **Style de police du texte** : Normal ou Italique

Des commandes séparées sont disponibles pour les notes de bas de page du mode sombre.

### Ombre portée [drop-shadow]

Ajoutez des ombres portées aux éléments :

1. Choisissez l'ombre **Force** : Douce, Moyenne ou Forte
2. Sélectionnez les éléments auxquels appliquer les ombres :
   - Images
   - Blocs de code
   - Citations
   - Tableaux

## CSS personnalisé [custom-css]

Pour une personnalisation avancée au-delà des contrôles disponibles, utilisez le bouton **CSS personnalisé** pour ouvrir un éditeur de code. Tout CSS que vous ajoutez ici sera ajouté au style généré et automatiquement étendu pour fonctionner dans la structure du document Marked.

L'éditeur inclut la coloration syntaxique et la validation : les CSS non valides seront signalés par des messages d'erreur.

## Aperçu en direct [live-preview]

Le volet d'aperçu montre votre style appliqué à un exemple de contenu markdown, notamment :

- Titres (H1 à H6)
- Paragraphes avec diverses mises en forme en ligne
- Tableaux
- Blocs de code
- Images
- Listes (ordonnées et non ordonnées)
- Citations
- Listes de définitions
- Notes de bas de page
- Listes de tâches

Les modifications sont mises à jour en temps réel à mesure que vous ajustez les commandes.

## Sauvegarde et partage [saving-and-sharing]

Une fois que vous êtes satisfait de votre style, vous avez plusieurs options :

### Afficher le CSS [view-css]

Cliquez sur **Afficher CSS** pour voir le CSS généré complet dans une fenêtre contextuelle. Vous pouvez le copier dans votre presse-papiers ou le consulter avant de l'enregistrer.

### Enregistrer le CSS [save-css]

Cliquez sur **Enregistrer CSS** pour télécharger votre style sous forme de fichier CSS. Vous serez invité à saisir des métadonnées (titre, auteur, description) avant de télécharger.

### Ajouter à Marked [add-to-marked]

Cliquez sur **Ajouter à Marked** pour ajouter directement le style à votre installation Marked. Cela nécessite que Marked soit en cours d'exécution et ouvrira une boîte de dialogue pour confirmer le nom du style et les informations sur l'auteur.

### Partager le style [share-style]

Cliquez sur **Partager le style** pour publier votre style dans la [Galerie de styles Marked](https://markedapp.com/styles) pour que d'autres puissent l'utiliser. Vous devrez fournir :

- Titre du style
- Votre nom
- URL de l'auteur (facultatif)
- Description
- Remarque (facultatif)

Un aperçu de votre style apparaîtra dans la boîte de dialogue de partage avant la publication.

## Métadonnées [metadata]

Utilisez la section métadonnées (extensible via le bouton fléché à côté du titre du style) pour définir :

- **Auteur** : votre nom (persiste au fil des sessions)
- **URL de l'auteur** : URL de votre site Web ou de votre profil
- **Description** : une description du style
- **Remarque** : Notes supplémentaires (non incluses dans les styles partagés)

Ces métadonnées sont incluses dans l'en-tête du fichier CSS et utilisées lors du partage de styles.

## Conseils [tips]

- Commencez avec un thème de base proche de ce que vous souhaitez, puis personnalisez-le
- Utilisez le thème **Blank** si vous souhaitez un contrôle complet à partir de zéro
- Activez **Rhythm** pour une typographie mathématiquement cohérente
- Testez votre style avec la bascule **Mode sombre** si vous envisagez de le prendre en charge
- Utilisez **Custom CSS** avec parcimonie : la plupart des besoins peuvent être satisfaits avec les contrôles intégrés
- Prévisualisez votre style avec différents types de contenu avant de le partager

## Compatibilité du navigateur [browser-compatibility]

Le générateur de styles fonctionne mieux dans les navigateurs modernes (Chrome, Firefox, Safari, Edge). Il nécessite que JavaScript soit activé.
