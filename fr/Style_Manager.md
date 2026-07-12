# <%= @title %>

Le Gestionnaire de styles offre une interface centralisée pour gérer l'ensemble de vos
styles intégrés et personnalisés. Il vous donne un contrôle complet sur les
styles qui apparaissent dans les menus, leur ordre, leurs raccourcis clavier, et plus encore.

## Ouvrir le Gestionnaire de styles

Pour ouvrir le Gestionnaire de styles, cliquez sur le bouton **Gérer les styles…** dans le panneau
{% prefspane Style %}, ou utilisez {% appmenu Style, Manage Styles (~@$m) %}. Vous pouvez également glisser des fichiers CSS directement sur la fenêtre des préférences : Marked
les importera, ouvrira le Gestionnaire de styles, et sélectionnera pour vous la ligne
nouvellement ajoutée.

![Gestionnaire de styles][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## Le tableau des styles

Le Gestionnaire de styles affiche tous vos styles dans un tableau triable qui mélange
sans distinction styles intégrés et styles personnalisés. Chaque ligne du tableau contient
plusieurs colonnes :

### Case à cocher Activé

La case à cocher **Activé** ajoute ou retire immédiatement le style du menu Style,
du menu contextuel Style par défaut, et des raccourcis clavier. Lorsque vous désactivez un style,
il est masqué des menus mais reste dans le Gestionnaire de styles pour être facilement réactivé.

Si vous désactivez le style actuellement actif, Marked bascule automatiquement vers le
prochain style activé disponible.

### Colonne Nom

La colonne **Nom** affiche le nom d'affichage du style. Vous pouvez modifier ce nom
directement en cliquant dessus ; les modifications sont conservées et propagées à
tous les menus où le style apparaît. Ceci est particulièrement utile pour les styles personnalisés,
lorsque vous souhaitez un nom plus descriptif que le nom du fichier.

Les styles intégrés ont des noms verrouillés qui ne peuvent pas être modifiés. Pour personnaliser
le nom d'un style intégré, dupliquez-le d'abord pour créer une copie modifiable.

### Colonne Source

La colonne **Source** indique la provenance du style :

- **Intégré** : styles fournis avec Marked et stockés dans le bundle de l'application
- **Personnalisé** : styles que vous avez ajoutés depuis des fichiers CSS de votre disque
- **Dupliqué** : styles créés en dupliquant un autre style (intégré ou personnalisé)

### Colonne Actions

Chaque ligne comporte une pile **Actions** avec des boutons permettant de gérer ce style :

**Modifier** : Ouvre le fichier CSS dans votre éditeur par défaut. Les styles intégrés ne peuvent
pas être modifiés directement -- vous devrez d'abord les dupliquer pour créer une copie modifiable.

**Dupliquer** : Crée une copie du style ainsi qu'un nouveau fichier CSS sur le disque. La
copie apparaît immédiatement sous le style d'origine dans le tableau. C'est
la méthode recommandée pour personnaliser les styles intégrés.

**Afficher** : Affiche le fichier CSS dans le Finder, ce qui facilite sa localisation sur
votre disque. Ce bouton n'est disponible que pour les styles personnalisés disposant d'un chemin de fichier.

**Supprimer** : Retire le style de Marked. Pour les styles personnalisés, vous aurez
le choix entre retirer uniquement la référence (en conservant le fichier CSS) ou
déplacer le fichier CSS vers la Corbeille. Les styles intégrés ne peuvent pas être supprimés,
mais ils peuvent être désactivés.

**Restaurer** : Pour les styles intégrés, ce bouton restaure le style à son
état par défaut s'il a été modifié. Ce bouton n'est visible que pour les
styles intégrés.

## Réorganiser les styles

Les lignes peuvent être réorganisées par glisser-déposer. Faites simplement glisser une ligne de style vers une nouvelle
position dans le tableau. L'ordre défini ici détermine :

- L'ordre du menu Style dans les menus de Marked
- L'attribution des raccourcis clavier (`⌘1`–`⌘9` pour les neuf premiers styles activés,
  `⌥⌘1`–`⌥⌘0` pour les dix suivants, et ainsi de suite)

Glissez les styles vers les emplacements de raccourcis clavier que vous souhaitez leur
attribuer.

## Ajouter des styles

Il existe plusieurs façons d'ajouter de nouveaux styles personnalisés au Gestionnaire de styles :

### Bouton Ajouter

Cliquez sur le bouton **Ajouter un nouveau style** pour ouvrir un sélecteur de fichiers
vous permettant de choisir un ou plusieurs fichiers CSS à importer. Les fichiers sélectionnés seront
ajoutés au Gestionnaire de styles et activés par défaut.

### Glisser-déposer

Vous pouvez glisser des fichiers CSS directement sur la fenêtre du Gestionnaire de styles. Lorsque vous glissez
des fichiers au-dessus de la fenêtre, une incrustation apparaît indiquant « Ajouter un style personnalisé » (ou
« Ajouter N styles personnalisés » pour plusieurs fichiers). Déposez les fichiers pour les importer.

Vous pouvez également glisser des fichiers CSS vers des positions spécifiques du tableau : l'indicateur de
dépôt montre où le nouveau style sera inséré, ce qui vous permet de contrôler
à la fois l'importation et le positionnement en une seule action.

Glisser des fichiers CSS sur le panneau de préférences {% prefspane Style %} les
importera également et ouvrira automatiquement le Gestionnaire de styles.

## Aperçu en direct

Le panneau de droite du Gestionnaire de styles affiche un aperçu en direct du
style sélectionné. L'aperçu affiche un document d'exemple complet comportant des titres,
des listes, des tableaux, des blocs de code, des citations en bloc, et d'autres éléments Markdown courants,
tous stylés avec le CSS réel du style sélectionné.

L'aperçu utilise directement le fichier CSS depuis le disque : toute modification effectuée dans votre
éditeur externe se répercute donc instantanément dans l'aperçu. Cela facilite
la visualisation de vos modifications en temps réel lorsque vous développez des styles personnalisés.

### Aperçu en mode sombre

Une case à cocher au-dessus de l'aperçu vous permet de basculer entre les aperçus en mode
clair et en mode sombre. Ceci est utile pour tester l'apparence des styles dans les deux modes
d'apparence, en particulier si vous créez des styles qui s'adaptent à l'apparence du système.

## Raccourcis clavier

Le Gestionnaire de styles affiche une légende sous le tableau indiquant comment les raccourcis
clavier sont attribués. Les neuf premiers styles activés reçoivent {% kbd cmd 1 %} à
{% kbd cmd 9 %} ({% kbd cmd 0 %} est réservé), les dix suivants reçoivent {% kbd opt cmd 1 %} à {% kbd opt cmd 0 %}, et ainsi de suite. Vous pouvez consulter les raccourcis clavier attribués dans le menu contextuel Style de n'importe quel aperçu.

## Filtrer les styles désactivés

Une case à cocher en bas de la fenêtre vous permet d'afficher ou de masquer les styles
désactivés. Lorsqu'elle est décochée, seuls les styles activés sont affichés, ce qui facilite
la concentration sur vos styles actifs et leur réorganisation. Lorsqu'elle est cochée, tous les styles (activés et désactivés)
sont affichés, ce qui vous permet de gérer l'ensemble de votre collection de styles.

## Restaurer les styles intégrés

Le bouton **Restaurer tous les styles intégrés** en bas de la fenêtre
restaure tous les styles intégrés à leur état par défaut. Ceci est utile si vous avez
désactivé des styles intégrés et souhaitez les réactiver, ou si vous souhaitez annuler
toute modification apportée aux styles intégrés.

## Astuces

- **Organiser par fréquence d'utilisation** : glissez vos styles les plus utilisés vers le haut pour leur
  attribuer les raccourcis clavier les plus accessibles ({% kbd cmd 1 %}, {% kbd cmd 2 %}, etc.)

- **Désactiver plutôt que supprimer** : plutôt que de supprimer les styles que vous n'utilisez pas,
  désactivez-les. Ils resteront hors de votre chemin tout en restant disponibles si vous en avez besoin
  plus tard.

- **Utiliser la duplication pour expérimenter** : dupliquez un style avant d'y apporter des
  modifications majeures, afin de pouvoir toujours revenir à l'original.

- **Prévisualiser pendant l'édition** : gardez le Gestionnaire de styles ouvert pendant que vous modifiez des fichiers
  CSS pour voir vos modifications se mettre à jour en temps réel dans le panneau d'aperçu.

- **Import par lots** : vous pouvez sélectionner plusieurs fichiers CSS à la fois avec le
  bouton Ajouter, ou glisser plusieurs fichiers pour tous les importer en une seule action.

