# <%= @title %>

Marked inclut un système de navigation wiki qui permet de naviguer rapidement entre des fichiers texte liés à l'aide de simples liens `[[wiki]]`. Ce système est conçu pour une navigation fluide et fonctionne au mieux lorsqu'il est configuré pour ouvrir les liens dans la fenêtre actuelle.

## Réglages optimaux

Pour utiliser les liens wiki, activez **Convertir les `[[liens wiki]]`** dans {% prefspane Preview %}, et définissez l'extension par défaut que Marked utilisera lors de la recherche de fichiers correspondants.

Pour une expérience optimale, réglez **« Les liens vers des fichiers texte doivent s'ouvrir dans : »** sur *« la fenêtre actuelle »* dans {% prefspane Apps %}. Cela garantit une navigation naturelle et la préservation de l'historique.

Si **Mettre en évidence les erreurs de syntaxe Markdown** est activé dans {% prefspane Proofing %}, la syntaxe `[[lien wiki]]` qui ne correspond à aucun nom de fichier du répertoire actuel sera mise en évidence en rouge, pour indiquer qu'un fichier référencé n'existe pas. Ces mises en évidence se mettent à jour à mesure que des fichiers sont ajoutés, mais uniquement après l'enregistrement ou le rechargement du fichier actuel. Cliquer sur un lien mis en évidence vers un fichier manquant proposera de créer un nouveau fichier pour vous, en ajoutant l'extension par défaut si nécessaire. Le nouveau fichier vide sera ouvert dans Marked, et si Éditer automatiquement les nouveaux fichiers est activé, votre éditeur s'ouvrira avec le nouveau fichier.

## Fonctionnement des liens wiki

- Les **liens wiki** utilisent le format : `[[lien wiki]]`.
- Lorsque vous cliquez sur un lien wiki, Marked recherche un fichier correspondant dans le **même répertoire** que le document actuel.
- Le fichier doit avoir l'extension spécifiée dans les réglages de Marked (par exemple, `.md`), sauf si vous indiquez un nom de fichier complet avec son extension dans le lien (par exemple, `[[notes.txt]]`).
- Si vous souhaitez utiliser un texte de lien différent du nom de fichier, ajoutez-le après une barre verticale (`|`) dans le lien, par exemple `[[wiki linking|Une note sur les liens]]`, qui s'affichera comme `[Une note sur les liens](wiki-link.md)`.
- Si un lien wiki commence par un `#`, il sera considéré comme un lien d'ancrage sur la même page. Les noms d'ancrage sont normalisés en les mettant en minuscules et en remplaçant tous les espaces par des tirets. Pour les processeurs qui créent des ID d'en-tête sans tirets (comme MultiMarkdown) - par exemple, `## wiki links` obtient l'ID `wikilinks` - cette navigation peut être rompue. Dans ce cas, spécifiez l'ID de lien correct, avec une barre verticale et un titre si nécessaire, par exemple `[[#wikilinks|#wiki links]]`.

### Correspondance des noms de fichiers

Lorsque vous utilisez un lien tel que `[[lien wiki]]`, Marked recherche un fichier portant l'un des noms suivants (en supposant que votre extension par défaut est `.md`) :

- `lien wiki.md`
- `LienWiki.md`
- `lien-wiki.md`
- `Lien-Wiki.md`
- `lien_wiki.md`
- `Lien_Wiki.md`
- `lienwiki.md`
- `LienWiki.md`
- (et d'autres combinaisons d'espaces, de tirets, de tirets bas et de casse mixte)

**Toute correspondance ignore la casse et s'adapte aux séparateurs utilisés.**
Si vous spécifiez une extension dans le lien (par exemple, `[[notes.txt]]`), Marked recherchera ce fichier exact.

## Rétroliens

Lorsqu'un fichier texte est ouvert et que la navigation wiki est activée, le reste des fichiers du répertoire est analysé à la recherche de `[[liens]]` vers le fichier actuel. Cette opération s'effectue en arrière-plan, et le document ouvert est mis à jour avec une liste de rétroliens si certains sont trouvés. Pour consulter les rétroliens, la barre latérale des commentaires doit être ouverte. Si elle est fermée, utilisez le menu Action (**Relecture->Afficher les commentaires**) ou appuyez sur {% kbd ^@c %} pour l'ouvrir.


## Historique de navigation

Marked suit votre navigation à travers les liens wiki, vous permettant de vous déplacer **en arrière et en avant** dans l'historique de vos fichiers, tout comme dans un navigateur web.

- **Précédent :** {% kbd @[ %}
- **Suivant :** {% kbd @] %}

Vous pouvez également utiliser le menu **Historique** pour accéder à n'importe quel fichier consulté précédemment.
