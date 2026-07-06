# <%= @title %>

Ouverture rapide donne un accès rapide à vos documents ouverts et à vos fichiers récents.

## Ouvrir le panneau Ouverture rapide

Accédez au panneau Ouverture rapide avec {% kbd shift cmd O %} ou depuis le menu {% appmenu File, Quick Open %}. Le panneau apparaît sous forme de fenêtre flottante au-dessus de votre document actuel, vous permettant de basculer rapidement entre les documents ouverts ou d'ouvrir des fichiers récents.

![Panneau Ouverture rapide][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Sections de documents

Le panneau Ouverture rapide organise les documents en sections claires :

### Documents ouverts

En haut de la liste, vous verrez tous les documents actuellement ouverts. Les documents sont regroupés visuellement par fenêtre :

- **Fenêtres à onglets** : les documents dans des fenêtres à onglets affichent « Fenêtre avec X onglets » comme sous-titre, indiquant le nombre d'onglets dans ce groupe de fenêtre
- **Fenêtres autonomes** : les documents dans des fenêtres individuelles affichent « Fenêtre » comme sous-titre

Chaque document ouvert affiche :
- le nom de fichier du document comme titre principal
- les informations de regroupement de fenêtre comme sous-titre
- une icône de document

### Documents récents

Sous les documents ouverts, un séparateur « Documents récents » divise la liste. La section des documents récents affiche jusqu'à 10 de vos fichiers les plus récemment ouverts qui ne sont pas actuellement ouverts. Chaque document récent affiche :

- le nom de fichier du document comme titre principal
- « Récent » comme sous-titre
- une icône de document

### Ouvrir autre chose

En bas de la liste, l'option « Ouvrir autre chose… » vous permet d'ouvrir le sélecteur de fichiers standard de macOS pour sélectionner n'importe quel fichier. Cette option affiche :

- « Ouvrir autre chose… » comme titre principal
- « Ouvrir un fichier ou un dossier » comme sous-titre
- une icône de dossier

## Recherche et filtrage

Tapez dans le champ de recherche en haut du panneau pour filtrer la liste en temps réel. La recherche porte sur :

- les noms de fichiers des documents
- les chemins de fichiers complets

Au fur et à mesure que vous tapez, la liste se met à jour immédiatement pour n'afficher que les documents correspondants. L'option « Ouvrir autre chose… » reste toujours visible en bas des résultats filtrés.

## Navigation au clavier

Naviguez dans le panneau Ouverture rapide entièrement au clavier :

- **Touches fléchées ↑/↓** : se déplacer vers le haut et le bas dans la liste
- **Retour** : ouvrir le document ou l'option sélectionné
- **Échap** : fermer le panneau Ouverture rapide
- **Commande (⌘)** : maintenir enfoncée pour révéler les chemins de fichiers (voir ci-dessous)

## Afficher les chemins de fichiers

Maintenez la touche **Commande (⌘)** enfoncée pendant que le panneau Ouverture rapide est ouvert pour voir le chemin de fichier complet de chaque document dans la zone de sous-titre. Les chemins dans votre dossier personnel sont affichés à l'aide du raccourci `~` (par exemple, `~/Documents/file.md`). Relâchez la touche Commande pour revenir à la vue normale affichant le regroupement de fenêtre ou l'information « Récent ».

Ceci est particulièrement utile lorsque vous avez plusieurs fichiers portant le même nom ouverts, ou lorsque vous devez vérifier l'emplacement exact d'un document.

## Ouvrir des documents

- **Documents ouverts** : sélectionner un document ouvert amène sa fenêtre au premier plan et bascule vers l'onglet de ce document s'il se trouve dans une fenêtre à onglets
- **Documents récents** : sélectionner un document récent l'ouvre dans une nouvelle fenêtre ou l'ajoute comme onglet (selon votre préférence « Ouvrir les documents en onglets » dans {% prefspane General %})
- **Ouvrir autre chose…** : sélectionner cette option ouvre la boîte de dialogue standard du sélecteur de fichiers de macOS
