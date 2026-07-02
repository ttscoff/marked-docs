# Glossary — German (de)

Agreed translations for recurring terms. The lead translator maintains this file; contributors follow it consistently. Terms are aligned with the localized Marked app strings (`de.lproj`) so the docs match what users see in the UI.

| English | Translation | Notes |
|---------|-------------|-------|
| Marked | Marked | Produktname, unverändert |
| Markdown | Markdown | Lehnwort, unverändert |
| **headline / heading** | **Überschrift** | NICHT „Schlagzeile" (haeufiger MT-Fehler, im UI bereits korrigiert) |
| preview | Vorschau | App: „Vorschaufenster", „in der Vorschau" |
| export | Export / exportieren | App-Menü: „Exportieren…", „Exportieren als" |
| import | Import / importieren | |
| Settings | Einstellungen | App-Menü: „Einstellungen…" (im Fließtext; Tag `{% prefspane %}` behält engl. Pane-ID) |
| Preferences | Einstellungen | synonym zu Settings |
| gear menu | Zahnradmenü | Token `{{gear}}` bleibt unverändert |
| processor | Prozessor | Markdown-Prozessor |
| preprocessor | Präprozessor | |
| style / theme | Stil | App: „Stil", „Eigenen Stil erzeugen", „Stil-Manager" |
| proofing | Korrektur / Korrekturlesen | App: „Korrekturmodus", „Korrekturlesen" |
| Table of Contents | Inhaltsverzeichnis | |
| bookmark | Lesezeichen | |
| Mini Map | Mini-Übersicht | Marked-Begriff (App: „Mini-Übersicht") |
| Quick Actions | Schnellaktionen | |
| Quick Open | Schnell öffnen | App-Menü: „Schnell öffnen" |
| Custom Processor | Benutzerdefinierter Prozessor | |
| Custom Rules | Eigene Regeln | App: „Eigene Regeln bearbeiten" |
| clipboard | Zwischenablage | |
| streaming preview | Streaming-Vorschau | |
| keyboard shortcut | Tastaturkurzbefehl | App-Menü: „Tastaturkurzbefehle" |
| syntax highlighting | Syntaxhervorhebung | |
| footnote | Fußnote | |
| line break | Zeilenumbruch | |
| page break | Seitenumbruch | |
| indentation level | Einrückungsebene | |
| word repetition | Wortwiederholung | App: „Wortwiederholungen visualisieren" |
| readability | Lesbarkeit | App: „Lesbarkeitsstatistik" |
| word count / character count | Wortanzahl / Zeichenanzahl | |
| dark mode | Dunkelmodus | App: „Dunkelmodus" |
| status bar / toolbar | Statusleiste / Symbolleiste | |
| sidebar | Seitenleiste | |
| header / footer (print) | Kopfzeile / Fußzeile | |
| CriticMarkup, MultiMarkdown, CommonMark, MathJax, KaTeX | (unverändert) | Technische Namen, engl. belassen |
| Scrivener, Obsidian, Bear, Drafts, … | (unverändert) | App-Namen, engl. belassen |
| macOS, Finder, Dock, AppleScript | (unverändert) | Apple-Systembegriffe |

## Do not translate (keep English)

- File names and code identifiers (`Exporting.md`, `Exporting.html`)
- `{% prefspane General %}`, `{% kbd cmd S %}`, `{{cmd}}`, `{{gear}}`, etc.
- URL schemes: `x-marked-3://`
- Version numbers and build metadata

## Ambiguous terms (settled choices)

| English | Chosen translation | Avoid (reason) |
|---------|-------------------|----------------|
| headline / heading | Überschrift | „Schlagzeile" (= newspaper headline, falsche Bedeutung) |
| you (address) | Sie | „du" — die App siezt durchgehend, siehe SYNTAX.md |
| resolve (image variants) | auflösen / ermitteln | nicht „auflösen" i.S.v. „dissolve" prüfen — Kontext beachten |
