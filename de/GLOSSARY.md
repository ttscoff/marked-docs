# Glossary — German (de)

Agreed translations for recurring terms. The lead translator maintains this file; contributors follow it consistently. Terms are aligned with the localized Marked app strings (`de.lproj`) so the docs match what users see in the UI.

| English | Translation | Notes |
|---------|-------------|-------|
| bookmark | Lesezeichen | |
| clipboard | Zwischenablage | |
| CriticMarkup, MultiMarkdown, CommonMark, MathJax, KaTeX | (unverändert) | Technische Namen, engl. belassen |
| Custom Rules | Eigene Regeln | Benanntes Marked-Feature → App-Menü „Eigene Regeln bearbeiten“ |
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
