# <%= @title %>

Marked comprend les catalogues de documentation [Apple DocC](https://www.swift.org/documentation/docc/) (`.docc` bundles). Lorsque vous prévisualisez Markdown qui se trouve à l'intérieur ou à côté d'un catalogue, Marked peut résoudre les références d'image **sans extension** aux fichiers du dossier `Resources` du catalogue, y compris les variantes `~dark` et `@2x`.

Pour les documents Markdown normaux qui utilisent des **chemins avec des extensions de fichier** (`images/icon.png`), voir [Variantes d'images](Image_Variants.html). Cette fonctionnalité fonctionne partout ; la résolution DocC est spécifique au catalogue.

## Activation de la résolution DocC [enabling-docc-resolution]

Dans {% prefspane Apps %}, activez **Résoudre les références d'image DocC** (activé par défaut).

La détection DocC s'exécute lorsque Marked trouve un ancêtre de catalogue `.docc` du document ouvert. Aucun schéma d'URL spécial ni intégration Xcode n'est requis : ouvrez le Markdown du catalogue de la même manière que n'importe quel autre fichier.

## Références sans extension [extensionless-references]

Dans un catalogue DocC, les auteurs référencent généralement des images **sans chemin ni extension** :

```markdown
![Order flow](OrderStateTransitions)
```

Marked résout `OrderStateTransitions` en `Resources/OrderStateTransitions.png` (ou un autre type pris en charge) lorsque ce fichier existe dans le catalogue.

Les références qui incluent déjà un chemin et une extension (`images/chart.png`) sont laissées à [Variantes d'image](Image_Variants.html) et ne sont pas réécrites par la résolution DocC.

## Mode sombre et variantes Retina [dark-mode-and-retina-variants]

Les catalogues DocC contiennent souvent plusieurs fichiers par image :

| Rôle | Exemple dans `Resources/` |
|------|------------------------------|
| Lumière (1x) | `diagram.png` |
| Sombre (1x) | `diagram~dark.png` |
| Lumière (2x) | `diagram@2x.png` |
| Sombre (2x) | `diagram~dark@2x.png` |

Lorsqu'il existe plusieurs variantes, Marked émet le même balisage réactif `<picture>` décrit dans [Variantes d'image](Image_Variants.html). Une référence à un seul fichier se résout toujours en un chemin normal `<img>` ou `![](Resources/...)`.

## HTML et Markdown [html-and-markdown]

La résolution DocC s'applique lors de la passe d'inclusion de Marked :

- **Sources Markdown** : références `![alt](ImageName)`
- **Sources HTML** : `<img src="ImageName">` sans extension

Les deux sont mis à jour avant le rendu de l'aperçu.

## Surveillance de fichiers [file-watching]

Les images résolues dans le dossier du catalogue `Resources` sont ajoutées à la liste de surveillance de Marked. La modification d'un fichier de variantes en externe met à jour l'aperçu sans actualisation manuelle.

## Sujets connexes [related-topics]

- [Variantes d'image](Image_Variants.html) : détection des chemins `~dark` et `@2x` basés sur les extensions dans n'importe quel projet
- [Xcode Playgrounds](Xcode_Playgrounds.html) : aperçu des commentaires Swift Playgrounds
- [Paramètres : Applications](Settings_Apps.html) : Préférences DocC et variantes d'image
