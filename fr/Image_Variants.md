# <%= @title %>

Marked peut créer automatiquement des éléments `<picture>` réactifs pour les images locales lorsque les fichiers compagnons **mode sombre** et **Retina** se trouvent à côté de l'image que vous référencez. Cela utilise les mêmes conventions de dénomination que les catalogues de documentation DocC d'Apple, mais fonctionne pour **n'importe quel document Markdown ou HTML** avec des chemins d'image normaux qui incluent une extension de fichier.

Voir également [Support DocC](DocC_Support.html) pour les références de catalogue sans extension dans les bundles `.docc`.

## Activation des variantes d'image [enabling-image-variants]

Dans {% prefspane Apps %}, activez **Résoudre les variantes d'image sombres et @2x** (activé par défaut) dans les paramètres DocC.

Cette préférence est distincte de **Résoudre les références d'image DocC**, qui s'applique uniquement à l'intérieur des catalogues `.docc`. Vous pouvez en utiliser une, les deux ou aucune selon votre projet.

## Convention de dénomination [naming-convention]

Placez les fichiers de variantes dans le **même dossier** que l'image principale. Marked recherche quatre combinaisons basées sur le nom de base :

| Rôle | Exemple de nom de fichier |
|------|------------------|
| Lumière (1x) | `icon.png` |
| Sombre (1x) | `icon~dark.png` |
| Lumière (2x) | `icon@2x.png` |
| Sombre (2x) | `icon~dark@2x.png` |

L'ordre des suffixes est flexible : `icon@2x~dark.png` et `icon~dark@2x.png` sont traités de la même manière.

Extensions prises en charge : `png`, `jpg`, `jpeg`, `gif`, `svg`, `webp` et `pdf`.

## Ce qui est réécrit [what-gets-rewritten]

Marked scanne votre document **avant** le rendu de l'aperçu final :

- **Marquage :** `![Alt text](images/icon.png)`
- **HTML :** `<img src="images/icon.png" alt="Alt text">`

Si au moins **deux** fichiers de variantes correspondants existent sur le disque, la référence est remplacée par un bloc `<picture>`. Un seul fichier supplémentaire suffit : vous n'avez pas besoin des quatre variantes.

Exemple de sortie lorsque des fichiers clairs, sombres et @2x sont présents :

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

L'aperçu (et l'exportation HTML) suit ensuite l'apparence du système de l'utilisateur pour les variantes sombres et la densité de pixels de l'appareil pour les ressources @2x.

## Ce qui est ignoré [what-is-skipped]

Marked ne réécrit **pas** :

- URL distantes (`http://`, `https://`, `data:`)
- Références qui pointent déjà vers un fichier `~dark`
- `<img>` balises déjà à l'intérieur d'un élément `<picture>` existant
- Noms sans extension comme `![Diagram](diagram)` : utilisez [DocC Support](DocC_Support.html) pour les références de style catalogue

## Aperçu en direct et surveillance des fichiers [live-preview-and-file-watching]

Lorsque des variantes sont détectées, Marked ajoute **chaque fichier de variantes existant** à sa liste de surveillance à côté du document principal. L'enregistrement de `icon~dark.png` dans un éditeur externe déclenche le même rechargement d'image en direct que l'édition de `icon.png`.

## Conseils [tips]

- Référencez l'image **light 1x** dans votre source lorsque cela est possible (`icon.png`, pas `icon~dark.png`). Marked découvre des fichiers associés à partir de ce chemin.
- Si vous n'avez que `@2x` actifs, incluez au moins une autre variante (généralement `~dark`) ou Marked laissera la référence inchangée.
- La résolution de variantes utilise des chemins **relatifs au document** (ou au dossier du fichier inclus pour les inclusions imbriquées), les mêmes règles de chemin de base que [Documents multi-fichiers](Multi-File_Documents.html).

## Sujets connexes [related-topics]

- [Support DocC](DocC_Support.html) : noms d'images sans extension dans les catalogues `.docc`
- [Paramètres : Applications](Settings_Apps.html) : bascule les préférences pour les variantes DocC et d'image
- [Aperçu](Previewing.html) : aperçu en direct et mises à jour des fichiers
