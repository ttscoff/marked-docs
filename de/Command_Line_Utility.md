# <%= @title %>

Das Befehlszeilentool `mk` bietet einfachen Zugriff auf die Funktionen von Marked vom Terminal aus und ermöglicht so die Automatisierung von Arbeitsabläufen und die Integration mit Shell-Skripten und anderen Befehlszeilentools.

## Installation [installation]

Die empfohlene Methode zur Installation von `mk` ist mit Homebrew:

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Wenn Sie Homebrew nicht verwenden, laden Sie das signierte Paket herunter und installieren Sie es:

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signiertes PKG-Installationsprogramm für mk. Zum Starten doppelklicken und den Anweisungen folgen." %}

Nachdem Sie `mk.pkg` heruntergeladen haben, doppelklicken Sie darauf und befolgen Sie die Anweisungen des Installationsprogramms.

## Grundlegende Verwendung [basic-usage]

### Dateien öffnen [opening-files]

Öffnen Sie eine Markdown-Datei in Marked über die Befehlszeile:

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Öffnen und Fenster über alle anderen heben
```

### Inhalte von STDIN streamen [streaming-content-from-stdin]

Streamen Sie Inhalte direkt in die Streaming-Vorschau von Marked:

```bash
echo "# Hallo Welt" | mk
cat notes.md | mk
mk -  # STDIN explizit verwenden
```

Das Fenster „Streaming-Vorschau“ wird geöffnet und zeigt den Inhalt in Echtzeit an, während er von anderen Befehlen weitergeleitet wird.

## Befehlsreferenz [command-reference]

### Dateioperationen [file-operations]

**`mk [file]`** – Markdown-Datei in Marked öffnen

**`mk [file] --raise`** – Datei öffnen und das Fenster über alle anderen heben

### STDIN und Streaming [stdin-and-streaming]

**`mk`** oder **`mk -`** – Von STDIN lesen und Streaming-Vorschau öffnen

**`mk --stream`** – Streaming-Vorschaufenster öffnen, ohne STDIN zu lesen

### Vorschauverwaltung [preview-management]

**`mk --refresh`** – Vorderstes Vorschaufenster aktualisieren

**`mk --refresh all`** – Alle geöffneten Vorschaufenster aktualisieren

**`mk --refresh file.md`** – Vorschau für eine bestimmte Datei aktualisieren (falls geöffnet)

### Einstellungen [preferences]

**`mk --pref`** – Marked-Einstellungen öffnen (Seite „Allgemein“)

**`mk --pref Advanced`** – Einstellungen für eine bestimmte Seite öffnen

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** – Benutzereinstellungen festlegen (mehrere Paare zulässig)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### Stilverwaltung [style-management]

**`mk --style NAME`** – Vorschaustil für geöffnete Fenster festlegen

**`mk --add-style FILE`** – CSS-Datei als eigenen Stil zu Marked hinzufügen

```bash
mk --add-style ~/Styles/custom.css
```

### JavaScript-Ausführung [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** – JavaScript im vordersten Fenster ausführen

**`mk --dojs "SCRIPT" all`** – JavaScript in allen Fenstern ausführen

**`mk --dojs "SCRIPT" file.md`** – JavaScript in bestimmten Dateien ausführen

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### Inhaltsextraktion und -import [content-extraction-and-import]

**`mk --extract URL`** – Inhalte aus der URL extrahieren und in Marked öffnen

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** – Fenster „URL importieren“ öffnen (optional mit URL)

**`mk --stylestealer [URL]`** – Style-Stealer-HUD öffnen (optional mit URL)

### Hilfsbefehle [utility-commands]

**`mk --paste`** – Neues Dokument aus der Zwischenablage erstellen

**`mk --preview TEXT`** – Text direkt in einem neuen Dokument in der Vorschau anzeigen

**`mk --dingus`** – Markdown-Dingus zum Testen von Prozessoren öffnen

**`mk --help`** oder **`mk -h`** – Nutzungsinformationen anzeigen

**`mk --version`** oder **`mk -v`** – Versionsinformationen anzeigen

## Beispiele [examples]

```bash
# Datei öffnen
mk document.md

# Markdown aus einer Datei streamen
cat notes.md | mk

# Verarbeiten und Vorschau anzeigen
grep -i "important" notes.md | mk

# Alle Vorschauen aktualisieren
mk --refresh all

# Eigenen Stil hinzufügen
mk --add-style ~/Documents/MyTheme.css

# Einstellungen festlegen
mk --defaults syntaxHighlight=1 processor=multimarkdown

# JavaScript in allen Fenstern ausführen
mk --dojs "window.scrollTo(0,0)" all

# Inhalte von einer Webseite extrahieren
mk --extract https://blog.example.com/article

# Text direkt in der Vorschau anzeigen
mk --preview "## Hallo\n\nDies ist **Markdown**-Text!"
```

## Integration [integration]

### Shell-Aliase [shell-aliases]

Fügen Sie zu Ihrem `~/.zshrc` oder `~/.bash_profile` hinzu:

```bash
alias mko='mk --raise'      # Öffnen und nach vorn holen
alias mkr='mk --refresh all' # Alle aktualisieren
```

### Skripte [scripts]

Verwenden Sie `mk` in Shell-Skripten zur Automatisierung:

```bash
#!/bin/bash
# Datei überwachen und Änderungen an Marked streamen
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### Arbeitsabläufe [workflows]

Kombinieren Sie es mit anderen Tools:

```bash
# Zwischenablage in Markdown umwandeln und Vorschau anzeigen
pbpaste | markdown | mk

# Suchen und Vorschau anzeigen
grep -r "TODO" . | head -20 | mk
```

## Open Source [open-source]

Das Befehlszeilentool `mk` ist Open Source und auf GitHub verfügbar:

**https://github.com/ttscoff/mk**

Sie können:
- den Quellcode ansehen
- Verbesserungen beitragen
- Probleme melden
- bei Bedarf aus dem Quellcode bauen

Das Tool ist in Swift geschrieben und lässt sich mit Xcode kompilieren. Build-Anweisungen finden Sie in der [README](https://github.com/ttscoff/mk).

## Version [version]

Überprüfen Sie Ihre installierte `mk`-Version mit:

```bash
mk --version
```

## Verwandte Funktionen [related-features]

- Weitere Informationen zum URL-Schema von Marked finden Sie unter [URL-Handler](URL_Handler.html)
- Weitere Informationen zur Streaming-Vorschau finden Sie unter [Streaming-Vorschau](Streaming_Preview.html)
- Automatisierungsbeispiele finden Sie unter [Workflow-Integration](Workflow_Integration.html)
