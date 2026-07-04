# <%= @title %>

Marked inclut un dictionnaire AppleScript pour automatiser l'aperçu, l'export et l'intégration aux flux de travail. Vous pouvez ouvrir des documents, contrôler l'aperçu (rechargement, défilement, surlignages, défilement automatique, lecture rapide), lire les statistiques, modifier les processeurs et les styles, copier du HTML ou du RTF dans le presse-papiers et exporter vers la plupart des mêmes formats disponibles dans le menu {% appmenu File, Export %}. **L'aperçu des titres / table des matières via AppleScript est en cours de développement** (voir ci-dessous).

Pour l'automatisation basée sur les URL (scripts shell, commandes `open` et callbacks), consultez le [gestionnaire d'URL](URL_Handler.html). AppleScript et le gestionnaire d'URL se complètent : utilisez AppleScript lorsque vous devez cibler un document ou une fenêtre spécifique, et les URL lorsqu'un simple appel `open 'x-marked://...'` suffit.

## Consulter le dictionnaire

Dans **Éditeur de script**, choisissez **Fichier → Ouvrir le dictionnaire…** puis sélectionnez Marked. Le dictionnaire répertorie les commandes sur les objets **application**, **document** et **window**, ainsi que les commandes d'exportation dans la suite Marked.

Sur macOS, vous pouvez parcourir les définitions de script avec **Éditeur de script**.

## Cibler Marked

Pour l'installation standard :

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Documents et fenêtres

**Application**

- `documents` -- documents d'aperçu ouverts (liste ordonnée).
- `windows` -- fenêtres d'aperçu.

**Document**

- `name` -- nom d'affichage.
- `path` -- chemin du fichier lorsque le document est enregistré sur le disque.
- `modified` -- indique si le document a des modifications d'éditeur non enregistrées.
- `processor` -- Processeur Markdown pour cet aperçu (lecture/écriture). Noms valides : `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. Modifier `processor` applique une exception par document et recharge l'aperçu ; cela ne change pas la valeur par défaut globale dans {% prefspane Processor %}.
- `preprocessor` -- préprocesseur pour cet aperçu (lecture/écriture). Utilisez `true` ou `false` pour activer ou désactiver le préprocesseur personnalisé, ou un nom de préprocesseur si applicable.
- `source text` -- source Markdown brute (lecture seule).
- `critic markup mode` -- indique si le traitement CriticMarkup est activé (lecture/écriture). Le modifier recharge l'aperçu.
- `is autoscrolling` -- indique si le défilement automatique est actif (lecture seule).
- `is speed reading` -- indique si le mode lecture rapide est actif (lecture seule).
- Commandes de prévisualisation, de lecture, de statistiques et d'exportation (voir ci-dessous).

**Window**

- `document` -- le `MarkdownDocument` affiché dans cette fenêtre.
- `style` -- nom du style d'aperçu actuel (lecture/écriture). Modifier `style` recharge l'aperçu avec le thème choisi (comme sélectionner un style depuis le menu des styles d'aperçu).
- `close`, `save`, `print` -- commandes de fenêtre standard.
- Les mêmes commandes d'aperçu, de lecture, de statistiques et d'exportation que sur les documents (transmises au document de la fenêtre).

Préférez `tell document 1` ou `tell window 1's document` lorsque vous exportez un aperçu spécifique. Les commandes d'exportation sur l'application utilisent la fenêtre principale ou le document actuel lorsqu'aucun destinataire n'est spécifié.

### Exemple : ouvrir et lire le chemin

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Exemple : modifier le style d'aperçu

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

Les noms de style correspondent au menu des styles d'aperçu (nom affiché, nom de ressource CSS comme `swiss`, ou identifiant interne). Les styles personnalisés que vous avez ajoutés dans le Gestionnaire de styles sont pris en charge.

Utilisez **`get preview style names`** sur l'objet application pour lister les noms affichés des styles activés.

### Exemple : processeur et texte source

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Commandes de l'application

Ces commandes s'appliquent à l'objet **application** (pas à un document spécifique).

| Command | Description |
| --- | --- |
| `open streaming preview` | Ouvrez une fenêtre [aperçu du presse-papiers en streaming](Streaming_Preview.html). |
| `preview clipboard` | Ouvre un [aperçu du presse-papiers](Opening_Files.html) de son contenu actuel (identique à {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}). |
| `close all` | Fermez tous les documents d'aperçu ouverts (pas d'invite de sauvegarde ; Marked ne modifie pas les fichiers source). |
| `get available processors` | Liste des noms de processeur : `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Liste les noms affichés des styles d'aperçu activés. |
| `get_available_formats` | Liste les noms de formats pris en charge par `convert_to`. |
| `get_available_profiles` | Répertoriez les noms des profils d'exportation (identiques à la propriété `profiles`). |

Placez Marked au premier plan avec la commande AppleScript standard **`activate`** :

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Contrôle de l'aperçu

Disponibles sur **document** et **window**. La plupart nécessitent une WebView d'aperçu chargée.

| Command | Parameters | Description |
| --- | --- | --- |
| `refresh preview` | — | Rechargez l'aperçu à partir du fichier source (identique à {% appmenu Preview, Refresh %}). |
| `reveal in finder` | — | Révélez le fichier du document dans le Finder. |
| `show highlights` | — | Activez la mise en évidence des mots clés (évitez les mots, les substituts, la voix passive, les listes personnalisées). |
| `full screen` | optional `enabled` boolean | Entrez, quittez ou basculez en mode aperçu plein écran. |
| `scroll to heading` | `title` ou `id` | Faites défiler jusqu'à un titre par son texte visible ou son `id` DOM. |
| `scroll to position` | `percent` ou `line` | Faites défiler par pourcentage de la hauteur du document ou par numéro de ligne approximatif. |
| `copy html` | — | Copiez l'aperçu HTML dans le presse-papiers (menu Action ou {% kbd shift cmd C %} ; voir [Copier HTML](Exporting.html#copyhtml)). |
| `copy rtf` | — | Copiez le texte enrichi dans le presse-papiers. |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## Défilement automatique et lecture rapide

| Command | Description |
| --- | --- |
| `autoscroll` | Démarre le défilement automatique. Un entier `wpm` optionnel définit les mots par minute avant de démarrer. |
| `stop autoscroll` | Arrête le défilement automatique. |
| `pause autoscroll` | Met en pause ou reprend le défilement automatique. |
| `speed read` | Démarre ou bascule la [lecture rapide](Speed_Reading.html). |
| `stop speed read` | Arrête la lecture rapide. |
| `pause speed read` | Mettre en pause ou reprendre la lecture rapide. |

Vérifiez l'état avec les propriétés du document `is autoscrolling` et `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Statistiques

**`get statistics`** renvoie un `statistics_record` contenant des valeurs numériques calculées à partir de la source Markdown actuelle (pas les chaînes formatées affichées dans le tiroir de statistiques).

| Property | Description |
| --- | --- |
| `word_count` | Nombre de mots |
| `sentence_count` | Nombre de phrases |
| `character_count` | Nombre de caractères |
| `paragraph_count` | Nombre de paragraphes |
| `average_words_per_sentence` | Mots moyens par phrase |
| `average_syllables_per_word` | Syllabes moyennes par mot |
| `complex_word_percentage` | Pourcentage de mots complexes |
| `reading_ease` | Indice de lisibilité Flesch |
| `fog_index` | Indice de brouillard Gunning |
| `grade_level` | Niveau scolaire Flesch–Kincaid |
| `gulpease` | Indice Gulpease (lisibilité en italien ; `0` lorsqu'il n'est pas applicable) |
| `gulpease_band` | Bande Gulpease `1`–`4` (si applicable) |
| `reading_time_minutes` | Temps de lecture à **250 mots/min** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Table des matières (en cours de développement)

{% note %}
**En cours de développement — pas encore fiable.** Le dictionnaire inclut une propriété **`headings`** et une commande **`headings`** pour lire les titres imbriqués de l'aperçu (enregistrements `heading_item`). Cette automatisation ne fonctionne **pas correctement** dans les versions actuelles (résultats vides, erreurs de coercition ou « aucun résultat n'a été renvoyé »). Il sera corrigé dans une version ultérieure. Préférez **`scroll to heading`** avec un titre ou un identifiant connu d'ici là.
{% endnote %}

**Comportement prévu** (une fois terminé) : enregistrements `heading_item` imbriqués à partir des en-têtes dans l'**aperçu** (`h1`–`h6`), et non à partir du Markdown brut.

| Property | Description |
| --- | --- |
| `title` | Texte du titre |
| `id` | Attribut `id` du DOM (chaîne vide si absent) |
| `level` | Niveau de titre `1`–`6` |
| `children` | Liste imbriquée d'enregistrements `heading_item` |

**`headings`** (propriété du document) — tous les niveaux. **`headings levels {2, 3}`** (commande) — filtre optionnel : uniquement ces niveaux de titre précis (pas une plage).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Utilisez les valeurs `id` avec **`scroll to heading id "..."`** une fois que l'automatisation des titres est stable.

## Imprimer avec un profil

**`print with profile`** applique temporairement les paramètres d'impression d'un profil d'exportation, puis imprime le document (même ensemble de préférences que les profils d'exportation dans {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

Les noms de profil sont sensibles à la casse. Après l'impression, Marked restaure le profil d'exportation précédemment actif.

## Profils d'exportation

Les profils d'exportation stockent des ensembles de préférences d'export/impression (marges, en-têtes, options de table des matières et autres réglages similaires depuis {% prefspane Export %}).

**Lire les noms de profil**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Exporter avec un profil**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

Les noms de profil sont sensibles à la casse et doivent correspondre exactement à un profil enregistré.

## Commandes d'exportation

Les commandes d'exportation sont disponibles sur les objets **application**, **document** et **window**. Chaque commande nécessite un paramètre **`to`** avec le chemin de sortie (chaîne de chemin POSIX ou objet `file`).

| Command | Output |
| --- | --- |
| `export markdown` | Markdown (.md) |
| `export html` | HTML |
| `export paginated pdf` | PDF paginé (mise en page impression) |
| `export continuous pdf` | PDF à défilement continu |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | Texte OpenDocument |
| `export textbundle` | TextBundle |
| `export rtf` | RTF |
| `export opml` | OPML |

**Notes**

- Le PDF paginé utilise le même pipeline HTML-vers-PDF que {% appmenu File, Export As, Save PDF (Paginated) %}. Il n'est pas disponible pour les documents d'aperçu HTML brut.
- L'export HTML utilise l'**aperçu rendu** (ce que vous voyez dans la WebView), pas le fichier source Markdown brut.
- Le PDF continu capture la mise en page actuelle de la WebView d'aperçu.

### Exportation de base

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Chemins d'exportation et bac à sable

- Utilisez un chemin POSIX complet pour le fichier de destination.
- Marked peut créer des dossiers intermédiaires lorsque le chemin d'exportation se trouve **à l'intérieur du dossier du document ouvert** (par exemple en exportant vers `.../MyProject/build/output.pdf` tout en prévisualisant `.../MyProject/chapter.md`).
- Les exports en dehors du dossier du document nécessitent un chemin accessible en écriture par Marked (emplacement du document enregistré, security-scoped bookmarks, ou dossiers autorisés via des boîtes de dialogue d'ouverture). Si le chemin n'est pas accessible en écriture, la commande renvoie une erreur avant le début de l'export.

## Options `with` (enregistrement de propriétés)

Au lieu de `with profile`, vous pouvez transmettre un enregistrement d'options avec **`with`** ou **`with properties`** :

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript reconnaît directement ces clés (elles sont mappées avant l'export) :

| Key | Description | Example |
| --- | --- | --- |
| `style` | Style d'aperçu à appliquer avant l'export (rechargement complet de l'aperçu) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Nom du format de page d'impression | `"A4"`, `"Letter"` |
| `margins` | Marges d'impression (voir ci-dessous) | `"1in"`, `"1in 2in"` |
| `fontSize` | Remplace la taille de police de base pour l'export/impression, en points (PDF paginé et continu) | `"14"`, `"12pt"` |

`fontSize` active la même option **Taille de police personnalisée pour l'export/impression** depuis {% prefspane Export %}. Cela n'affecte pas les documents Fountain, qui utilisent une taille de scénario fixe.

Lorsque `style` est inclus, Marked applique ce thème, attend que l'aperçu ait fini de se recharger, puis exporte. Vous n'avez pas besoin d'une étape `set style` séparée.

Les autres clés de l'enregistrement peuvent correspondre à des noms de **préférences d'export** issus des profils (mêmes clés stockées dans {% prefspane Export %}, comme `printBackgrounds`, `printTOC`, `topPrintMargin`). Ces valeurs sont appliquées temporairement pour cet export.

Vous ne pouvez pas combiner des sources contradictoires sans précaution : si vous utilisez `with profile`, chargez d'abord ce profil ; si vous utilisez un enregistrement `with`, les clés de profil de cet enregistrement remplacent les réglages actuels pour cet export.

### Raccourci de marges

La valeur `margins` est une chaîne contenant une à quatre mesures. Unités : `in`, `cm`, `mm`, `pt`, ou `"` pour les pouces. Un nombre sans unité est traité comme des points.

| Values | Signification |
| --- | --- |
| `1in` | Tous les côtés |
| `1in 2in` | Haut et bas `1in`, gauche et droite `2in` |
| `1in 2in 1in` | Haut `1in`, gauche et droite `2in`, bas `1in` |
| `1in 2in 1in 2in` | Haut, droite, bas, gauche |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Exemple combiné

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to`

L'objet application expose également les commandes de script héritées :

- **`convert_to`** -- convertit du texte Markdown ou un chemin de fichier vers un format (`html`, `pdf`, `epub`, `docx`, `rtf`, et d'autres), avec éventuellement un `profile` et un `output_path`.
- **`get_available_formats`** -- liste les noms de formats de conversion pris en charge.
- **`get_available_profiles`** -- liste les noms des profils d'exportation (identique à la propriété `profiles`).

`convert_to` reste disponible pour les anciens flux de travail et l'automatisation AppleScript uniquement.

## Débogage

Activez le **mode débogage** dans {% prefspane Advanced %} (ou la préférence de débogage dans les Paramètres). Marked enregistre alors les étapes d'export AppleScript au niveau Info avec le préfixe `[AppleScript]` dans Console.app et dans le visualiseur de journaux de Marked.

Lignes de journal utiles lors du traçage d'une exportation PDF paginée :

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Les exports longs (en particulier le PDF paginé) suspendent l'événement AppleScript jusqu'à la fin, afin que les clients ne dépassent pas le délai en plein export.

## Erreurs

Les exports échoués définissent une chaîne d'erreur de script sur la commande (visible dans Éditeur de script et les gestionnaires `on error`). Messages courants :

- Le chemin d'exportation est requis.
- Le répertoire d'export n'existe pas (en dehors du dossier document).
- Impossible de créer le répertoire d'exportation, ou erreur de permission lors de l'écriture du fichier.
- Nom du style d'aperçu inconnu.
- Délai d'attente pour le rechargement de l'aperçu après le changement de style.
- L'export PDF paginé a expiré ou a échoué pendant la génération des pages.

## Intégration avec d'autres outils

Les applications peuvent utiliser la surface AppleScript de Marked pour lire les métadonnées de document. Pour l'app Raccourcis, consultez [Intégration avec Raccourcis](Shortcuts_Integration.html). Pour les flux de travail basés sur des scripts shell, la surveillance de dossiers, et les callbacks d'éditeur, le [gestionnaire d'URL](URL_Handler.html) est souvent plus simple. Le [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) comprend des scripts et des services supplémentaires.
