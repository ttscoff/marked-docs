# appmenu reference — German (de)

Ready-made German menu paths for the `{% appmenu … %}` tags. Translate only the **menu text**; leave the shortcut tokens (`{{cmd}}O`, `(~@$m)`, `(@~k)` …) exactly as they are. Paths are taken from the localized app (`de.lproj`), so they match what the reader sees in Marked.

Entries marked ⚠ could not be confirmed 1:1 in the string tables — check them in the running app before use (menu may be renamed or restructured; if a path doesn't exist, ask the maintainer).

## File → Ablage

| English | German |
|---|---|
| `File, Open... ({{cmd}}O)` | `Ablage, Öffnen… ({{cmd}}O)` |
| `File, Open...` | `Ablage, Öffnen…` |
| `File, Open Recent` | `Ablage, Zuletzt geöffnet` |
| `File, Quick Open` | `Ablage, Schnell öffnen` |
| `File, Quick Actions…` | `Ablage, Schnellaktionen…` |
| `File, New ({{cmd}}N)` | `Ablage, Neu ({{cmd}}N)` |
| `File, New, New Markdown File` | `Ablage, Neu, Neue Markdown-Datei` |
| `File, New, Clipboard Preview ({{shift}}{{cmd}}V)` | `Ablage, Neu, Zwischenablage-Vorschau ({{shift}}{{cmd}}V)` |
| `File, New, Clipboard Preview` | `Ablage, Neu, Zwischenablage-Vorschau` |
| `File, New, Streaming Preview` | `Ablage, Neu, Streaming-Vorschau` |
| `File, New, MarsEdit Preview` | `Ablage, Neu, MarsEdit-Vorschau` |
| `File, New, Markdownify URL (@~k)` | `Ablage, Neu, URL in Markdown umwandeln (@~k)` |
| `File, Save Clipboard Preview` | `Ablage, Zwischenablage-Vorschau speichern` |
| `File, Save Dingus` | `Ablage, Dingus speichern` |
| `File, Save Dingus As...` | `Ablage, Dingus speichern unter…` |
| `File, Open Dingus in Marked` | `Ablage, Dingus in Marked öffnen` |
| `File, Open in Dingus...` | `Ablage, In Dingus öffnen…` |
| `File, Export` | `Ablage, Exportieren…` |
| `File, Export, Paginated PDF` | `Ablage, Exportieren als, PDF speichern (paginiert)` (EN-Tag „Export" = Menü „Exportieren als") |
| `File, Open Dictionary...` | — Menüpunkt existiert nicht (in der App bestätigt); EN-Tag veraltet, bereits gemeldet |

## Preview → Vorschau

| English | German |
|---|---|
| `Preview, Dark Mode ({{opt}}{{cmd}}I)` | `Vorschau, Dunkelmodus ({{opt}}{{cmd}}I)` |
| `Preview, Dark Mode` | `Vorschau, Dunkelmodus` |
| `Preview, Refresh` | `Vorschau, Aktualisieren` |
| `Preview, Show Status Bar ({{ctrl}}/)` | `Vorschau, Statusleiste anzeigen ({{ctrl}}/)` |

## Style → Stil

| English | German |
|---|---|
| `Style, Manage Styles (~@$m)` | `Stil, Stile verwalten (~@$m)` |
| `Style, Generate a Custom Style` | `Stil, Eigenen Stil erzeugen` |
| `Style, Share a Custom Style` | `Stil, Eigenen Stil teilen` |

## Help → Hilfe

| English | German |
|---|---|
| `Help` | `Hilfe` |
| `Help, Markdown Reference` | `Hilfe, Markdown-Referenz` |
| `Help, Report an Issue` | `Hilfe, Problem melden` |
| `Help, Show Custom Rules Log` | `Hilfe, Protokoll eigener Regeln anzeigen` |
| `Help, Markdown Dingus` | `Hilfe, Markdown-Dingus öffnen` |

## Gear menu → `{{gear}}` (token stays, submenu text translated)

| English | German |
|---|---|
| `{{gear}}, Highlight Keywords` | `{{gear}}, Schlüsselwörter hervorheben` |
| `{{gear}}, Proofing, Show Comments` | `{{gear}}, Korrekturlesen, Kommentare anzeigen` |
| `{{gear}}, Proofing, Highlight All Spelling Errors` | `{{gear}}, Korrekturlesen, Rechtschreibfehler anzeigen` (EN-Tag „Highlight All…" = Menü „Rechtschreibfehler anzeigen") |

## Notes

- `{% prefspane General %}` and similar keep the **English pane ID** — never translate those.
- `Safari, Settings…` and other non-Marked menus follow that app's own German UI (`Safari, Einstellungen…`).
- `Proofing` = „Korrekturlesen", `Style` = „Stil", `Preview` = „Vorschau", `File` = „Ablage", `Help` = „Hilfe".
