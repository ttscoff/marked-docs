# <%= @title %>

Het `mk` opdrachtregelprogramma biedt gemakkelijke toegang tot de functies van Marked vanaf de terminal, waardoor workflowautomatisering en integratie met shellscripts en andere opdrachtregelprogramma's mogelijk wordt.

## Installatie [installation]

De aanbevolen manier om `mk` te installeren is met Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Als u Homebrew niet gebruikt, download en installeer dan het ondertekende pakket:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

Na het downloaden van `mk.pkg` dubbelklikt u erop en volgt u de aanwijzingen van het installatieprogramma.

## Basisgebruik [basic-usage]

### Bestanden openen [opening-files]

Open een markdown-bestand in Marked vanaf de opdrachtregel:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### Streaminginhoud van STDIN [streaming-content-from-stdin]

Stream inhoud rechtstreeks naar de streamingpreview van Marked:

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

Het Streaming Preview-venster wordt geopend en geeft de inhoud in realtime weer zoals deze door andere opdrachten wordt doorgegeven.

## Commandoreferentie [command-reference]

### Bestandsbewerkingen [file-operations]

**`mk [file]`** — Open een afwaarderingsbestand in Marked

**`mk [file] --raise`** — Open het bestand en plaats het venster boven alle andere

### STDIN en streaming [stdin-and-streaming]

**`mk`** of **`mk -`** — Lees van STDIN en open Streaming Preview

**`mk --stream`** — Open het streamingvoorbeeldvenster zonder STDIN te lezen

### Voorbeeldbeheer [preview-management]

**`mk --refresh`** — Vernieuw het voorste voorbeeldvenster

**`mk --refresh all`** — Vernieuw alle geopende voorbeeldvensters

**`mk --refresh file.md`** — Vernieuw het voorbeeld voor een specifiek bestand (indien geopend)

### Voorkeuren [preferences]

**`mk --pref`** — Open Marked voorkeuren (pagina Algemeen)

**`mk --pref Advanced`** — Open voorkeuren voor een specifieke pagina

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — Gebruikersvoorkeuren instellen (meerdere paren toegestaan)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Stijlbeheer [style-management]

**`mk --style NAME`** — Stel de voorbeeldstijl in voor geopende vensters

**`mk --add-style FILE`** — Voeg een CSS-bestand toe als aangepaste stijl aan Marked

```bash
mk --add-style ~/Styles/custom.css
```

### JavaScript-uitvoering [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** — Voer JavaScript uit in het voorste venster

**`mk --dojs "SCRIPT" all`** — Voer JavaScript uit in alle vensters

**`mk --dojs "SCRIPT" file.md`** — Voer JavaScript uit in specifieke bestanden

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Inhoud extraheren en importeren [content-extraction-and-import]

**`mk --extract URL`** — Extraheer inhoud uit de URL en open in Marked

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** — Open het import-URL-venster (optioneel met URL)

**`mk --stylestealer [URL]`** — Open Style Stealer HUD (optioneel met URL)

### Hulpprogramma's [utility-commands]

**`mk --paste`** — Maak een nieuw document vanaf het klembord

**`mk --preview TEXT`** — Bekijk een voorbeeld van tekst rechtstreeks in een nieuw document

**`mk --dingus`** — Open Markdown Dingus voor het testen van processors

**`mk --help`** of **`mk -h`** — Gebruiksinformatie weergeven

**`mk --version`** of **`mk -v`** — Versie-informatie weergeven

## Voorbeelden [examples]

``` bash
# Open een bestand
mk document.md

# Stream prijsverlaging vanuit een bestand
kattennotities.md | mk

# Verwerken en bekijken
grep -i "belangrijke" notes.md | mk

# Vernieuw alle voorbeelden
mk --alles vernieuwen

# Voeg een aangepaste stijl toe
mk --add-style ~/Documents/MijnTheme.css

# Stel voorkeuren in
mk --standaard syntaxisHighlight=1 processor=multimarkdown

# Voer JavaScript uit in alle vensters
mk --dojs "window.scrollTo(0,0)" allemaal

# Extraheer inhoud van een webpagina
mk --extract https://blog.example.com/article

# Bekijk direct een voorbeeld van tekst
mk --preview "## Hallo\n\nDit is **markdown** tekst!"
```

## Integratie [integration]

### Shell-aliassen [shell-aliases]

Voeg toe aan je `~/.zshrc` of `~/.bash_profile`:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### Scripts [scripts]

Gebruik `mk` in shellscripts voor automatisering:

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Werkstromen [workflows]

Combineer met ander gereedschap:

``` bash
# Converteer klembord naar prijsverlaging en voorbeeld
pbpaste | afwaardering | mk

# Zoeken en bekijken
grep -r "TODO" . | hoofd -20 | mk
```

## Open-source [open-source]

Het opdrachtregelprogramma `mk` is open source en beschikbaar op GitHub:

**https://github.com/ttscoff/mk**

U kunt:
- Bekijk de broncode
- Verbeteringen bijdragen
- Rapporteer problemen
- Bouw indien nodig vanaf de bron

De tool is geschreven in Swift en kan worden gecompileerd met Xcode. Zie de [README](https://github.com/ttscoff/mk) voor bouwinstructies.

## Versie [version]

Controleer uw geïnstalleerde `mk` versie met:

```bash
mk --version
```

## Gerelateerde functies [related-features]

- Zie [URL Handler](URL_Handler) voor meer informatie over het URL-schema van Marked
- Zie [Streaming Preview](Streaming_Preview) voor details over de streaming preview-functie
- Zie [Workflow Integration](Workflow_Integration) voor automatiseringsvoorbeelden