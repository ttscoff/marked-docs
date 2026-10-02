# <%= @title %>

W> **La prise en charge d'Apex dans Marked est en version bêta.** Le comportement peut évoluer à mesure que l'intégration arrive à maturité. Merci de signaler tout problème, rendu inattendu ou syntaxe manquante sur [support.markedapp.com](https://support.markedapp.com).

Apex est un **processeur Markdown unifié** : un seul moteur qui vise à couvrir les fonctionnalités pour lesquelles on choisit habituellement CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown ou Kramdown --- sans pour autant abandonner les autres variantes.

Dans Marked, **Apex (bêta)** fonctionne toujours en mode **unifié** d'Apex (toutes ces familles de fonctionnalités activées ensemble). Vous ne pouvez pas encore choisir dans Marked un « mode CommonMark » ou un « mode Kramdown » distinct d'Apex ; cela viendra peut-être plus tard.

Consultez le [Markdown Dingus](x-marked-3://dingus?processor=apex) pour expérimenter avec Apex, ou ouvrez {% appmenu Help, Markdown Reference %} et choisissez l'onglet **Apex** pour un aide-mémoire compact.

---

## Pourquoi Apex existe [why-apex-exists]

Les « variantes » de Markdown ont divergé pour de bonnes raisons --- GitHub avait besoin de listes de tâches et de tableaux, MultiMarkdown avait besoin de notes de bas de page et de métadonnées, Kramdown avait besoin de listes d'attributs --- mais choisir un processeur signifie généralement renoncer à la syntaxe d'un autre.

L'objectif d'Apex est de **regrouper** ces extensions afin qu'un même document puisse utiliser :

- les habitudes courantes de CommonMark / GFM (blocs de code avec délimiteurs, listes de tâches, texte barré, tableaux GFM)
- les notes de bas de page, abréviations et habitudes de métadonnées façon MultiMarkdown
- les listes de définitions, les maths et (pour un usage avancé) les listes d'attributs façon Kramdown
- des commodités orientées Marked telles que les callouts, Critic Markup et les marqueurs de table des matières

La documentation complète en amont se trouve sur le [wiki Apex](https://github.com/ApexMarkdown/apex/wiki). Cette page couvre ce dont vous avez besoin au quotidien dans l'aperçu de Marked.

---

## Activer Apex dans Marked [enabling-apex-in-marked]

1. Ouvrez {% prefspane Processor %}.
2. Réglez **Processeur Markdown par défaut** sur **Apex (bêta)**.
3. Ou substituez-le document par document avec des métadonnées telles que `Processor: apex` (alias : `apex-beta`, `unified`).

Les alias fonctionnent également depuis AppleScript, les actions « Run Processor » de Conductor, la sortie standard d'un processeur personnalisé (`APEX`), ainsi que les URL de valeurs par défaut `x-marked://`.

T> Dans cette version bêta, Marked continue d'étendre ses propres inclusions de fichiers (`<<[file]`, et les chemins d'inclusion Marked associés) avant qu'Apex ne s'exécute. Le moteur d'inclusion natif d'Apex est désactivé dans Marked pour des raisons de sandboxing. Utilisez les fonctions d'inclusion de Marked comme vous le faites déjà.

---

## Syntaxe de base ajoutée ou unifiée par Apex [basic-syntax]

Le Markdown standard (titres, emphase, liens, images, listes, citations, code) fonctionne comme vous pouvez vous y attendre. Les éléments ci-dessous sont les ajouts dont les gens ont le plus souvent besoin en passant à Apex.

### Listes de tâches [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Texte barré [strikethrough]

```markdown
~~removed text~~
```

### Tableaux [tables]

Tableaux GFM à barres verticales, avec séparateurs d'en-tête et alignement des colonnes :

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Les fonctionnalités avancées de tableaux (fusion de lignes `^^`, fusion de colonnes, légendes, tableaux en grille, CSV) sont documentées sur le wiki : [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Notes de bas de page [footnotes]

Style référence :

```markdown
See the note[^1].

[^1]: Footnote text.
```

Les styles en ligne familiers de MultiMarkdown / Kramdown sont également pris en charge. Détails : [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Listes de définitions [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Exposant et indice [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Maths [math]

Mode en ligne `$x^2$` et mode bloc `$$...$$` (les préférences MathJax / KaTeX de Marked contrôlent toujours l'habillage de l'aperçu).

### Callouts [callouts]

Style Obsidian / Bear :

```markdown
> [!NOTE]
> Something worth highlighting.
```

Voir aussi la [Syntaxe spéciale](Special_Syntax.html) de Marked et la page wiki [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts) d'Apex.

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Activez Critic Markup dans Marked comme d'habitude ; Apex peut rendre la syntaxe critic dans le pipeline du processeur. Voir [CriticMarkup](CriticMarkup.html).

### Abréviations [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Raccourcis emoji [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Métadonnées [metadata]

Le front matter YAML, les en-têtes façon MultiMarkdown `Key: Value` et les blocs de titre Pandoc sont reconnus. Insérez des valeurs avec `[%key]` lorsque cela est possible.

Détails de configuration : [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) et [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) sur le wiki.

### Marqueurs de table des matières [table-of-contents-markers]

Apex comprend les marqueurs de table des matières courants, notamment :

- `<!--TOC-->`
- `{{TOC}}` ou `{{TOC:2-4}}`
- Style Kramdown `{:toc}`

Excluez un titre avec `{:.no_toc}` lorsque l'IAL est disponible. Plus d'informations : [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Marqueurs spéciaux [special-markers]

Les commentaires HTML orientés Marked tels que `<!--BREAK-->` (saut de page) et `<!--PAUSE:N-->` (défilement automatique) continuent de fonctionner avec les aperçus Apex.

---

## Sujets avancés (wiki) [advanced-topics-wiki]

Consultez le [wiki Apex](https://github.com/ApexMarkdown/apex/wiki) pour les fonctionnalités puissantes mais moins courantes dans l'aperçu au quotidien :

| Sujet | Wiki |
|------|------|
| Génération d'index | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citations / bibliographie | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Listes d'attributs en ligne, spans, divs avec délimiteurs | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Documents multi-fichiers et inclusions | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Formats d'ID d'en-tête | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Images multi-format | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Modes de compatibilité (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugins et filtres | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Voir aussi [see-also]

- [Choisir un processeur](Choosing_a_Processor.html) --- quand choisir MultiMarkdown, CommonMark, Kramdown, Discount ou Apex
- [Paramètres : Processeur](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Accueil du wiki Apex](https://github.com/ApexMarkdown/apex/wiki)
- Signaler un problème : [support.markedapp.com](https://support.markedapp.com)
