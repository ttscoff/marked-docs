# Glossary — German (de)

Agreed translations for recurring terms. The lead translator maintains this file; contributors follow it consistently. Terms are aligned with the localized Marked app strings (`de.lproj`) so the docs match what users see in the UI.

| English | Translation | Notes |
|---------|-------------|-------|
| bookmark | Lesezeichen | |
| clipboard | Zwischenablage | |
| CriticMarkup, MultiMarkdown, CommonMark, MathJax, KaTeX | (unverändert) | Technische Namen, engl. belassen |
| Custom Rules | Eigene Regeln | Benanntes Marked-Feature → App-Menü „Eigene Regeln bearbeiten“. **App ist inkonsistent:** `MainMenu.strings` = „Eigene Regeln bearbeiten“, aber `Settings.strings` (`setting.customRules`, `.button`, `conductorNote`) = „Benutzerdefinierte Regeln“ + `setting.customRules.tooltip` noch englisch. **Kanonisch = „Eigene Regeln“** (Lead-Entscheid 06.07); Settings.strings von Brett anzugleichen |
| Custom Styles (Marked-Stile) | Eigene Stile | App „Eigenen Stil erzeugen“, „Eigene Stil-Galerie“. Im DOCX-Export heißt die Auswahl „DOCX-Stil“ — die Word-Formatvorlagen werden aus den Marked-Stilen generiert |
| custom … (generisch, ohne eigenen Menüpunkt) | benutzerdefiniert … | z. B. custom scripts → benutzerdefinierte Skripte; custom processor → benutzerdefinierter Prozessor |
| dark mode | Dunkelmodus | App: „Dunkelmodus“ |
| export | Export / exportieren | App-Menü: „Exportieren…“, „Exportieren als“ |
| footnote | Fußnote | |
| gear menu | Zahnradmenü | Token `{{gear}}` bleibt unverändert |
| header / footer (print) | Kopfzeile / Fußzeile | |
| **headline / heading** | **Überschrift** | NICHT „Schlagzeile“ (haeufiger MT-Fehler, im UI bereits korrigiert) |
| home directory / home folder | Home-Ordner | das eigene `~`; NICHT „Benutzer-Ordner“ (= `/Users`) |
| import | Import / importieren | |
| indentation level | Einrückungsebene | |
| keyboard shortcut | Tastaturkurzbefehl | App-Menü „Tastaturkurzbefehle“; NICHT bloß „Kurzbefehl“ (mehrdeutig, = Shortcuts-App „Kurzbefehle“); die Kombination selbst → „Tastenkombination“ |
| line break | Zeilenumbruch | |
| macOS, Finder, Dock, AppleScript | (unverändert) | Apple-Systembegriffe |
| Markdown | Markdown | Lehnwort, unverändert |
| Marked | Marked | Produktname, unverändert |
| Mini Map | Mini-Übersicht | Marked-Begriff (App: „Mini-Übersicht“) |
| page break | Seitenumbruch | |
| Preferences | Einstellungen | synonym zu Settings |
| preprocessor | Präprozessor | |
| preview | Vorschau | App: „Vorschaufenster“, „in der Vorschau“ |
| processor | Prozessor | Markdown-Prozessor |
| proofing | Korrektur / Korrekturlesen | App: „Korrekturmodus“, „Korrekturlesen“ |
| Quick Actions | Schnellaktionen | |
| Quick Open | Schnell öffnen | App-Menü: „Schnell öffnen“ |
| readability | Lesbarkeit | App: „Lesbarkeitsstatistik“ |
| Scrivener, Obsidian, Bear, Drafts, … | (unverändert) | App-Namen, engl. belassen |
| Settings | Einstellungen | App-Menü: „Einstellungen…“ (im Fließtext; Tag `{% prefspane %}` behält engl. Pane-ID) |
| sidebar | Seitenleiste | |
| status bar / toolbar | Statusleiste / Symbolleiste | |
| streaming preview | Streaming-Vorschau | |
| style / theme | Stil | App: „Stil“, „Eigenen Stil erzeugen“, „Stil-Manager“ |
| syntax highlighting | Syntaxhervorhebung | |
| Table of Contents | Inhaltsverzeichnis | |
| word count / character count | Wortanzahl / Zeichenanzahl | |
| word repetition | Wortwiederholung | App: „Wortwiederholungen visualisieren“ |

## Conductor / Eigene Regeln (Custom_Processor)

Der Editor für Eigene Regeln heißt bei Marked „Conductor“. Wir führen den **Namen englisch** (nicht „Dirigent“), die **Action-Labels und Kriterien aber deutsch** (Annahme: Brett lokalisiert den Conductor mit; die Labels sind im de-UI noch englisch, daher hier die maßgeblichen Übersetzungen).

| English | Translation | Notes |
|---------|-------------|-------|
| Conductor | Conductor | Feature-Name, engl. belassen; NICHT „Dirigent“ (zwei Altlasten in Additional_Javascript.md/Markdown_Dingus.md noch zu bereinigen) |
| Rules Editor | Editor für Eigene Regeln | App-Menü „Eigene Regeln bearbeiten“ |
| predicate / predicate editor | Prädikat / Prädikat-Editor | |
| Manually enabled | Manuell aktiviert | Kriterium + Schaltfläche „Manuell aktiviert hinzufügen“ |
| Trigger shortcut | Auslöser-Kurzbefehl | |
| Custom Rules Log | Protokoll eigener Regeln | App-Menü „Hilfe, Protokoll eigener Regeln anzeigen“ |
| Set Style / Run Command / Run Embedded Script | Stil festlegen / Befehl ausführen / Eingebettetes Skript ausführen | Conductor-Aktionen |
| Set/Delete/Strip Metadata | Metadaten festlegen / löschen / entfernen | |
| Insert Title H1 / Shift Headers / Normalize Headers | Titel H1 einfügen / Überschriften verschieben / Überschriften normalisieren | „Überschriften”, nicht „Header” |
| Insert TOC / Insert File / Insert Text | Inhaltsverzeichnis einfügen / Datei einfügen / Text einfügen | |
| Run Shortcut / Run System Service / Run Automator Workflow | Kurzbefehl ausführen / Systemdienst ausführen / Automator-Workflow ausführen | „Kurzbefehl“ = Apple-Shortcut |
| Run Rule / Continue | Regel ausführen / Fortfahren | |

## Do not translate (keep English)

- File names and code identifiers (`Exporting.md`, `Exporting.html`)
- `{% prefspane General %}`, `{% kbd cmd S %}`, `{{cmd}}`, `{{gear}}`, etc.
- URL schemes: `x-marked-3://`
- Version numbers and build metadata

## Ambiguous terms (settled choices)

| English | Chosen translation | Avoid (reason) |
|---------|-------------------|----------------|
| headline / heading | Überschrift | „Schlagzeile“ (= newspaper headline, falsche Bedeutung) |
| you (address) | Sie | „du“ — die App siezt durchgehend, siehe SYNTAX.md |
| resolve (image variants) | auflösen / ermitteln | nicht „auflösen“ i.S.v. „dissolve“ prüfen — Kontext beachten |
