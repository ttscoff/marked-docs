# <%= @title %>

L'outil en ligne de commande `mk` donne un accès simple aux fonctionnalités de Marked depuis le terminal, permettant l'automatisation de flux de travail et l'intégration avec des scripts shell et d'autres outils en ligne de commande.

## Installation [installation]

La méthode recommandée pour installer `mk` est d'utiliser Homebrew :

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Si vous n'utilisez pas Homebrew, téléchargez et installez le package signé :

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Programme d'installation PKG signé pour mk. Double-cliquez pour lancer Installateur et suivez les instructions." %}

Une fois `mk.pkg` téléchargé, double-cliquez dessus et suivez les instructions de l'installateur.

## Utilisation de base [basic-usage]

### Ouvrir des fichiers [opening-files]

Ouvrez un fichier markdown dans Marked depuis la ligne de commande :

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Contenu en streaming depuis STDIN [streaming-content-from-stdin]

Diffusez du contenu directement vers l'aperçu en continu de Marked :

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

La fenêtre d'aperçu en continu s'ouvre et affiche le contenu en temps réel, à mesure qu'il est transmis (pipe) depuis d'autres commandes.

## Référence des commandes [command-reference]

### Opérations sur les fichiers [file-operations]

**`mk [file]`** : ouvrir un fichier markdown dans Marked

**`mk [file] --raise`** : ouvrir le fichier et élever la fenêtre au-dessus de toutes les autres

### STDIN et streaming [stdin-and-streaming]

**`mk`** ou **`mk -`** : lire depuis STDIN et ouvrir l'aperçu en continu

**`mk --stream`** : ouvrir la fenêtre d'aperçu en continu sans lire STDIN

### Gestion de l'aperçu [preview-management]

**`mk --refresh`** : actualiser la fenêtre d'aperçu au premier plan

**`mk --refresh all`** : actualiser toutes les fenêtres d'aperçu ouvertes

**`mk --refresh file.md`** : actualiser l'aperçu d'un fichier spécifique (s'il est ouvert)

### Préférences [preferences]

**`mk --pref`** : ouvrir les préférences de Marked (page Général)

**`mk --pref Advanced`** : ouvrir les préférences sur une page spécifique

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** : définir les préférences utilisateur (plusieurs paires autorisées)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Gestion des styles [style-management]

**`mk --style NAME`** : définir le style d'aperçu pour les fenêtres ouvertes

**`mk --add-style FILE`** : ajouter un fichier CSS comme style personnalisé dans Marked

```bash
mk --add-style ~/Styles/custom.css
```

### Exécution de JavaScript [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** : exécuter du JavaScript dans la fenêtre au premier plan

**`mk --dojs "SCRIPT" all`** : exécuter du JavaScript dans toutes les fenêtres

**`mk --dojs "SCRIPT" file.md`** : exécuter du JavaScript dans un ou plusieurs fichiers spécifiques

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Extraction et importation de contenu [content-extraction-and-import]

**`mk --extract URL`** : extraire le contenu d'une URL et l'ouvrir dans Marked

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** : ouvrir la fenêtre d'importation d'URL (éventuellement avec l'URL)

**`mk --stylestealer [URL]`** : ouvrir le HUD de récupération de style (éventuellement avec une URL)

### Commandes utilitaires [utility-commands]

**`mk --paste`** : créer un nouveau document à partir du presse-papiers

**`mk --preview TEXT`** : prévisualiser le texte directement dans un nouveau document

**`mk --dingus`** : ouvrir Markdown Dingus pour tester les processeurs

**`mk --help`** ou **`mk -h`** : afficher les informations d'utilisation

**`mk --version`** ou **`mk -v`** : afficher les informations de version

## Exemples [examples]

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## Intégration [integration]

### Alias shell [shell-aliases]

Ajoutez ceci à votre `~/.zshrc` ou `~/.bash_profile` :

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Scripts [scripts]

Utilisez `mk` dans les scripts shell pour l'automatisation :

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Flux de travail [workflows]

Combinez avec d'autres outils :

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## Open source [open-source]

L'outil en ligne de commande `mk` est open source et disponible sur GitHub :

**https://github.com/ttscoff/mk**

Vous pouvez :
- consulter le code source
- contribuer des améliorations
- signaler des problèmes
- construire à partir des sources si nécessaire

L'outil est écrit en Swift et peut être compilé avec Xcode. Voir le [README](https://github.com/ttscoff/mk) pour les instructions de construction.

## Version [version]

Vérifiez la version de `mk` installée avec :

```bash
mk --version
```

## Fonctionnalités associées [related-features]

- Voir le [gestionnaire d'URL](URL_Handler) pour plus d'informations sur le schéma d'URL de Marked
- Voir [Aperçu en continu](Streaming_Preview) pour plus de détails sur la fonctionnalité d'aperçu en continu
- Voir [Intégration aux flux de travail](Workflow_Integration) pour des exemples d'automatisation
