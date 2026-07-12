# <%= @title %>

La palette Actions rapides est un lanceur de commandes consultable pour Marked. Elle rassemble les actions de la barre de menu principale et du **menu Action** de l'aperçu, ainsi que les commandes clavier propres à l'aperçu qui n'apparaissent dans aucun menu (comme **Défilement automatique**). Utilisez-la lorsque vous savez ce que vous voulez faire mais ne vous souvenez pas dans quel menu le trouver.

## Ouvrir la palette Actions rapides

Ouvrez la palette avec {% kbd shift cmd P %} ou depuis {% appmenu File, Quick Actions… %}. Le panneau apparaît sous forme de fenêtre flottante au-dessus de votre document actuel.

Appuyez à nouveau sur le même raccourci, ou appuyez sur **Échap**, pour fermer la palette. Si la palette est déjà ouverte, choisir **Actions rapides…** dans le menu la ferme également.

## Personnaliser le raccourci

Le raccourci par défaut est {% kbd shift cmd P %}. Pour le modifier, ouvrez {% prefspane General %} et enregistrez une nouvelle combinaison sous **Ouvrir la palette d'actions** dans la section **Raccourcis**.

Contrairement à **Activer Marked** et **Élever la première fenêtre**, le raccourci Actions rapides ne fonctionne que lorsque Marked est l'application active. Il met à jour le raccourci du menu {% appmenu File, Quick Actions… %} pour correspondre à votre paramètre.

## Recherche et filtrage

Tapez dans le champ de recherche en haut du panneau pour filtrer les commandes en temps réel. La correspondance est approximative et tolérante :

- L'ordre des mots n'a pas d'importance (`view source` correspond à **Basculer la vue source**)
- Les initiales fonctionnent bien (`sv` correspond à **Vue source**)
- La correspondance condensée trouve les commandes sans espaces (`akdoc` correspond à **Poser des questions sur le document**)

Chaque résultat affiche le nom de la commande à gauche et son raccourci clavier (si disponible) à droite en gris. Certaines commandes affichent également un chemin de navigation (par exemple `Aperçu › Défilement automatique`) lorsque l'action provient d'un sous-menu ou du moteur d'aperçu.

## Ce qui apparaît dans la liste

La palette inclut :

- Les **commandes de menu** de la barre de menu principale, y compris les menus dynamiques comme **Style**, **Historique**, et les onglets **Fenêtre** ouverts
- Les commandes du **menu Action** de la fenêtre d'aperçu
- Les **raccourcis d'aperçu** de la carte clavier propre à l'aperçu (les mêmes commandes affichées dans le HUD d'aide de l'aperçu), y compris la navigation, le défilement automatique, les signets, la recherche et d'autres actions propres à l'aperçu

Lorsque la même commande apparaît à plusieurs endroits, Marked affiche le chemin de menu le plus court et fusionne les informations de raccourci des doublons.

## Navigation au clavier

Naviguez dans la palette Actions rapides entièrement au clavier :

- **Touches fléchées ↑/↓** : se déplacer dans la liste filtrée
- **Retour** : exécuter la commande sélectionnée
- **Échap** : fermer la palette
- **Raccourcis avec la touche ⌘** : ferment la palette et exécutent la commande de menu correspondante (par exemple, appuyez sur {% kbd cmd U %} pour exécuter **Basculer la vue source** au lieu de la sélectionner dans la liste)

La frappe simple (sans la touche Commande) filtre le champ de recherche. Les raccourcis à touche unique propres à l'aperçu, comme `s` pour le défilement automatique, filtrent la liste ; appuyez sur **Retour** pour exécuter la commande sélectionnée.

## Exécuter des commandes

Sélectionner une commande de menu l'exécute de la même manière que si vous la choisissiez dans le menu, y compris pour les éléments dynamiques et ceux du menu Action.

Sélectionner un **raccourci d'aperçu** exécute l'action associée dans l'aperçu actif (par exemple, activer/désactiver le défilement automatique ou passer au titre suivant). Ces commandes nécessitent un document ouvert avec un aperçu ; si aucun aperçu n'est disponible, la palette s'ouvre quand même mais les actions propres à l'aperçu n'auront aucun effet.

Pour changer de fichier associé, voir [Ouverture rapide](Quick_Open.html). Pour la référence complète des raccourcis clavier de l'aperçu, voir [Raccourcis clavier](Keyboard_Shortcuts.html) ou appuyez sur {% kbd h %} dans l'aperçu pour afficher le HUD d'aide.
