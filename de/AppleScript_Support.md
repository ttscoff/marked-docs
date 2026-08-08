# <%= @title %>

Marked enthält ein AppleScript-Wörterbuch zur Automatisierung der Vorschau, des Exports und der Workflow-Integration. Sie können Dokumente öffnen, die Vorschau steuern (Neuladen, Scrollen, Hervorhebungen, Autoscroll, Schnelllesen), Statistiken lesen, Prozessoren und Stile ändern, HTML oder RTF in die Zwischenablage kopieren und in die meisten der gleichen Formate exportieren, die im Menü {% appmenu Ablage, Exportieren… %} verfügbar sind. **Die Vorschau der Überschriften/Inhaltsverzeichnisse über AppleScript ist in Arbeit** (siehe unten).

Informationen zur URL-basierten Automatisierung (Shell-Skripte, `open`-Befehle und Callbacks) finden Sie unter [URL-Handler](URL_Handler.html). AppleScript und der URL-Handler ergänzen einander: Verwenden Sie AppleScript, wenn Sie auf ein bestimmtes Dokument oder Fenster abzielen müssen, und URLs, wenn ein einfacher `open 'x-marked://...'`-Aufruf ausreicht.

## Wörterbuch anzeigen [viewing-the-dictionary]

Wählen Sie im **Skripteditor** **Ablage → Wörterbuch öffnen…** und dann Marked aus. Das Wörterbuch listet Befehle für die Objekte **application**, **document** und **window** sowie Exportbefehle in der Marked-Suite auf.

Unter macOS können Sie Skriptdefinitionen mit dem **Skripteditor** durchsuchen.

## Marked ansprechen [targeting-marked]

Für die Standardinstallation:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## Dokumente und Fenster [documents-and-windows]

**Anwendung**

- `documents` – Vorschaudokumente öffnen (geordnete Liste).
- `windows` – Vorschaufenster.

**Dokument**

- `name` – Anzeigename.
- `path` – Dateipfad, wenn das Dokument auf der Festplatte gespeichert wird.
- `modified` – ob das Dokument nicht gespeicherte Editoränderungen aufweist.
- `processor` – Markdown-Prozessor für diese Vorschau (Lesen/Schreiben). Gültige Namen: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. Die Einstellung `processor` wendet eine Überschreibung pro Dokument an und lädt die Vorschau neu; der globale Standardwert in {% prefspane Processor %} wird dadurch nicht geändert.
- `preprocessor` – Präprozessor für diese Vorschau (Lesen/Schreiben). Verwenden Sie `true` oder `false`, um den benutzerdefinierten Präprozessor zu aktivieren oder zu deaktivieren, oder ggf. einen Präprozessornamen.
- `source text` – rohe Markdown-Quelle (schreibgeschützt).
- `critic markup mode` – ob die CriticMarkup-Verarbeitung aktiviert ist (Lesen/Schreiben). Durch Ändern wird die Vorschau neu geladen.
- `is autoscrolling` – ob Autoscroll aktiv ist (schreibgeschützt).
- `is speed reading` – ob der Schnelllesemodus aktiv ist (schreibgeschützt).
- Vorschau-, Lese-, Statistik- und Exportbefehle (siehe unten).

**Fenster**

- `document` – das in diesem Fenster angezeigte `MarkdownDocument`.
- `style` – Name des aktuellen Vorschaustils (Lesen/Schreiben). Durch die Einstellung `style` wird die Vorschau mit dem ausgewählten Thema neu geladen (dasselbe wie die Auswahl eines Stils aus dem Vorschau-Stilmenü).
- `close`, `save`, `print` – Standard-Fensterbefehle.
- Dieselben Vorschau-, Lese-, Statistik- und Exportbefehle wie für Dokumente (weitergeleitet an das Dokument des Fensters).

Bevorzugen Sie `tell document 1` oder `tell window 1's document` beim Exportieren einer bestimmten Vorschau. Exportbefehle in der Anwendung verwenden das Schlüsselfenster oder das aktuelle Dokument, wenn kein Empfänger angegeben ist.

### Beispiel: Pfad öffnen und lesen [example-open-and-read-path]

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### Beispiel: Vorschaustil ändern [example-change-preview-style]

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

Stilnamen entsprechen dem Vorschau-Stilmenü (Anzeigename, CSS-Ressourcenname wie `swiss` oder interner Bezeichner). Eigene Stile, die Sie im Stil-Manager hinzugefügt haben, werden unterstützt.

Verwenden Sie **`get preview style names`** für das Anwendungsobjekt, um die Anzeigenamen aktivierter Stile aufzulisten.

### Beispiel: Prozessor und Quelltext [example-processor-and-source-text]

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## Anwendungsbefehle [application-commands]

Diese Befehle gelten für das **Anwendungsobjekt** (kein bestimmtes Dokument).

| Befehl | Beschreibung |
| --- | --- |
| `open streaming preview` | Öffnet ein Fenster mit einer [Streaming-Zwischenablage-Vorschau](Streaming_Preview.html). |
| `preview clipboard` | Öffnet eine [Zwischenablage-Vorschau](Opening_Files.html) des aktuellen Zwischenablage-Inhalts (wie {% appmenu Ablage, Neu, Zwischenablage-Vorschau ({{shift}}{{cmd}}V) %}). |
| `close all` | Schließt alle geöffneten Vorschaudokumente (keine Speicheraufforderung; Marked bearbeitet keine Quelldateien). |
| `get available processors` | Prozessornamen auflisten: `MultiMarkdown`, `Discount`, `CommonMark (GFM)`, `Kramdown`. |
| `get preview style names` | Listet die Anzeigenamen der aktivierten Vorschaustile auf. |
| `get_available_formats` | Liste der unterstützten Formatnamen `convert_to` auf. |
| `get_available_profiles` | Exportprofilnamen auflisten (identisch mit der Eigenschaft `profiles`). |

Holen Sie Marked mit dem Standard-AppleScript-Befehl **`activate`** in den Vordergrund:

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## Vorschausteuerung [preview-control]

Verfügbar für **Dokument** und **Fenster**. Die meisten davon erfordern eine geladene Vorschau-WebView.

| Befehl | Parameter | Beschreibung |
| --- | --- | --- |
| `refresh preview` | — | Lädt die Vorschau aus der Quelldatei neu (wie {% appmenu Vorschau, Aktualisieren %}). |
| `reveal in finder` | — | Zeigt die Dokumentdatei im Finder. |
| `show highlights` | — | Aktiviert die Schlüsselwort-Hervorhebung (zu vermeidende Wörter, Alternativen, Passiv, eigene Listen). |
| `full screen` | optional `enabled` boolean | Vollbild-Vorschaumodus aufrufen, verlassen oder umschalten. |
| `scroll to heading` | `title` oder `id` | Scrollt zu einer Überschrift anhand des sichtbaren Titeltexts oder der DOM-`id`. |
| `scroll to position` | `percent` oder `line` | Scrollt um einen Prozentsatz der Dokumenthöhe oder zu einer ungefähren Zeilennummer. |
| `copy html` | — | Kopiert das Vorschau-HTML in die Zwischenablage (Zahnradmenü oder {% kbd shift cmd C %}; siehe [HTML kopieren](Exporting.html#copyhtml)). |
| `copy rtf` | — | Kopiert Rich Text in die Zwischenablage. |

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

## Autoscroll und Schnelllesen [autoscroll-and-speed-read]

| Befehl | Beschreibung |
| --- | --- |
| `autoscroll` | Startet Autoscroll. Die optionale Ganzzahl `wpm` legt die Wörter pro Minute vor dem Start fest. |
| `stop autoscroll` | Stoppt Autoscroll. |
| `pause autoscroll` | Pausiert Autoscroll oder setzt es fort. |
| `speed read` | Startet [Schnelllesen](Speed_Reading.html) oder schaltet es um. |
| `stop speed read` | Stoppt das Schnelllesen. |
| `pause speed read` | Pausiert das Schnelllesen oder setzt es fort. |

Überprüfen Sie den Status mit den Dokumenteigenschaften `is autoscrolling` und `is speed reading`.

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## Statistik [statistics]

**`get statistics`** gibt einen `statistics_record` mit numerischen Werten zurück, die aus der aktuellen Markdown-Quelle berechnet wurden (nicht die formatierten Zeichenfolgen, die in der Statistikleiste angezeigt werden).

| Eigenschaft | Beschreibung |
| --- | --- |
| `word_count` | Wortanzahl |
| `sentence_count` | Satzanzahl |
| `character_count` | Zeichenanzahl |
| `paragraph_count` | Absatzanzahl |
| `average_words_per_sentence` | Durchschnittliche Wörter pro Satz |
| `average_syllables_per_word` | Durchschnittliche Silben pro Wort |
| `complex_word_percentage` | Komplexer Wortprozentsatz |
| `reading_ease` | Flesch-Lesbarkeit |
| `fog_index` | Gunning-Fog-Index |
| `grade_level` | Flesch-Kincaid-Klassenstufe |
| `gulpease` | Gulpease-Index (italienische Lesbarkeit; `0`, wenn nicht zutreffend) |
| `gulpease_band` | Gulpease-Band `1`–`4` (falls zutreffend) |
| `reading_time_minutes` | Lesezeit bei **250 WPM** |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## Inhaltsverzeichnis (in Arbeit) [table-of-contents-work-in-progress]

{% note %}
**WIP – noch nicht zuverlässig.** Das Wörterbuch enthält eine **`headings`**-Eigenschaft und einen **`headings`**-Befehl zum Lesen verschachtelter Vorschauüberschriften (`heading_item`-Datensätze). Diese Automatisierung funktioniert in aktuellen Builds **nicht richtig** (leere Ergebnisse, Umwandlungsfehler oder „es wurde kein Ergebnis zurückgegeben“). Es wird in einer späteren Version behoben. Bevorzugen Sie bis dahin **`scroll to heading`** mit einem bekannten Titel oder einer bekannten ID.
{% endnote %}

**Geplantes Verhalten** (nach Abschluss): verschachtelte `heading_item` Datensätze aus Überschriften in der **Vorschau** (`h1`–`h6`), nicht aus rohem Markdown.

| Eigenschaft | Beschreibung |
| --- | --- |
| `title` | Überschriftentext |
| `id` | DOM `id` Attribut (leerer String, wenn nicht vorhanden) |
| `level` | Überschriftenebene `1`–`6` |
| `children` | Verschachtelte Liste von `heading_item` Datensätzen |

**`headings`** (Dokumenteigenschaft) – alle Ebenen. **`headings levels {2, 3}`** (Befehl) – optionaler Filter: nur diese Überschriftentiefen (kein Bereich).

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

Verwenden Sie `id`-Werte mit **`scroll to heading id "..."`**, sobald die Überschriftenautomatisierung stabil ist.

## Mit Profil drucken [print-with-profile]

**`print with profile`** wendet die Druckeinstellungen eines Exportprofils vorübergehend an und druckt dann das Dokument (gleiches Einstellungspaket wie Exportprofile von {% prefspane Export %}).

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

Bei Profilnamen muss die Groß-/Kleinschreibung beachtet werden. Nach dem Drucken stellt Marked das zuvor aktive Exportprofil wieder her.

## Exportprofile [export-profiles]

Exportprofile speichern Bündel von Export-/Druckeinstellungen (Ränder, Kopfzeilen, Inhaltsverzeichnisoptionen und ähnliche Einstellungen von {% prefspane Export %}).

**Profilnamen lesen**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**Mit einem Profil exportieren**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

Bei Profilnamen wird die Groß-/Kleinschreibung beachtet und sie müssen genau mit einem gespeicherten Profil übereinstimmen.

## Exportbefehle [export-commands]

Exportbefehle sind für die Objekte **application**, **document** und **window** verfügbar. Jeder Befehl erfordert einen **`to`** Parameter mit dem Ausgabepfad (POSIX-Pfadzeichenfolge oder `file` Objekt).

| Befehl | Ausgabe |
| --- | --- |
| `export markdown` | Markdown (.md) |
| `export html` | HTML |
| `export paginated pdf` | Paginiertes PDF (Drucklayout) |
| `export continuous pdf` | Fortlaufendes PDF (Endlos-Scroll) |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | OpenDocument-Text |
| `export textbundle` | TextBundle |
| `export rtf` | RTF |
| `export opml` | OPML |

**Anmerkungen**

- Paginiertes PDF verwendet dieselbe HTML-zu-PDF-Pipeline wie {% appmenu Ablage, Exportieren als, PDF speichern (paginiert) %}. Es ist nicht für rohe HTML-Vorschaudokumente verfügbar.
- Der HTML-Export verwendet die **gerenderte Vorschau** (was Sie in der WebView sehen), nicht die rohe Markdown-Quelldatei.
- Fortlaufendes PDF erfasst das aktuelle Vorschau-WebView-Layout.

### Einfacher Export [basic-export]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### Exportpfade und Sandboxing [export-paths-and-sandboxing]

- Verwenden Sie einen vollständigen POSIX-Pfad für die Zieldatei.
- Marked kann Zwischenordner erstellen, wenn sich der Exportpfad **im Ordner des geöffneten Dokuments** befindet (z. B. Exportieren nach `.../MyProject/build/output.pdf` während der Vorschau von `.../MyProject/chapter.md`).
- Exporte außerhalb des Ordners des Dokuments erfordern einen beschreibbaren Pfad, auf den Marked zugreifen kann (Speicherort des Dokuments, sicherheitsbezogene Lesezeichen oder Ordner, die Sie über Dialogfelder zum Öffnen gewährt haben). Wenn der Pfad nicht beschreibbar ist, gibt der Befehl vor Beginn des Exports einen Fehler zurück.

## `with`-Optionen (Eigenschaftsdatensatz) [with-options-properties-record]

Anstelle von `with profile` können Sie einen Datensatz mit Optionen mit **`with`** oder **`with properties`** übergeben:

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript erkennt diese Schlüssel direkt (sie werden vor dem Export zugeordnet):

| Schlüssel | Beschreibung | Beispiel |
| --- | --- | --- |
| `style` | Vorschaustil, der vor dem Export angewendet werden soll (vollständiges Neuladen der Vorschau) | `"Amblin"`, `"Swiss"` |
| `pageSize` | Name der Seitengröße drucken | `"A4"`, `"Letter"` |
| `margins` | Druckränder (siehe unten) | `"1in"`, `"1in 2in"` |
| `fontSize` | Überschreiben Sie die Basisschriftgröße für Export/Druck in Punkten (paginiertes und fortlaufendes PDF) | `"14"`, `"12pt"` |

`fontSize` aktiviert die gleiche **Benutzerdefinierte Schriftgröße für Export/Druck**-Option von {% prefspane Export %}. Fountain-Dokumente, die eine feste Drehbuchgröße verwenden, sind davon nicht betroffen.

Wenn `style` enthalten ist, wendet Marked diesen Stil an, wartet, bis die Vorschau neu geladen wird, und exportiert dann. Sie benötigen keinen separaten `set style` Schritt.

Andere Schlüssel im Datensatz können mit **Exportpräferenznamen** aus Profilen übereinstimmen (dieselben Schlüssel, die in {% prefspane Export %} gespeichert sind, z. B. `printBackgrounds`, `printTOC`, `topPrintMargin`). Diese Werte werden temporär für den Export übernommen.

Sie können widersprüchliche Quellen nicht leichtfertig kombinieren: Wenn Sie `with profile` verwenden, laden Sie zuerst dieses Profil; Wenn Sie einen `with`-Datensatz verwenden, überschreiben die Profilschlüssel im Datensatz die aktuellen Einstellungen für diesen Export.

### Kurzschreibweise für Ränder [margin-shorthand]

Der Wert `margins` ist eine Zeichenfolge mit ein bis vier Messungen. Einheiten: `in`, `cm`, `mm`, `pt` oder `"` für Zoll. Eine Zahl ohne Einheit wird als Punkt behandelt.

| Werte | Bedeutung |
| --- | --- |
| `1in` | Alle Seiten |
| `1in 2in` | Oben und unten `1in`, links und rechts `2in` |
| `1in 2in 1in` | Oben `1in`, links und rechts `2in`, unten `1in` |
| `1in 2in 1in 2in` | Oben, rechts, unten, links |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### Kombiniertes Beispiel [combined-example]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to` [convert_to]

Das Anwendungsobjekt macht auch ältere Skriptbefehle verfügbar:

- **`convert_to`** – Markdown-Text oder einen Dateipfad in ein Format konvertieren (`html`, `pdf`, `epub`, `docx`, `rtf` und andere), optional mit einem `profile` und `output_path`.
- **`get_available_formats`** – Liste unterstützter Konvertierungsformatnamen.
- **`get_available_profiles`** – Exportprofilnamen auflisten (identisch mit der Eigenschaft `profiles`).

`convert_to` bleibt für ältere Workflows und reine AppleScript-Automatisierung verfügbar.

## Debuggen [debugging]

Aktivieren Sie den **Debug-Modus** in {% prefspane Advanced %} (oder die Debug-Einstellung in den Einstellungen). Marked protokolliert dann AppleScript-Exportschritte auf Infoebene mit dem Präfix `[AppleScript]` in Console.app und im Protokollviewer von Marked.

Nützliche Protokollzeilen beim Verfolgen eines paginierten PDF-Exports:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

Lange Exporte (insbesondere paginierte PDF) unterbrechen das AppleScript-Ereignis bis zum Abschluss, damit es bei Clients während des Exports nicht zu einer Zeitüberschreitung kommt.

## Fehler [errors]

Fehlgeschlagene Exporte setzen die Skriptfehlerzeichenfolge für den Befehl (sichtbar im Skripteditor und in den `on error`-Handlern). Häufige Meldungen:

- Exportpfad ist erforderlich.
- Exportverzeichnis existiert nicht (außerhalb des Dokumentordners).
- Exportverzeichnis kann nicht erstellt werden oder beim Schreiben der Datei ist ein Berechtigungsfehler aufgetreten.
- Unbekannter Name des Vorschaustils.
- Zeitüberschreitung beim Warten auf das Neuladen der Vorschau nach einer Stiländerung.
- Beim paginierten PDF-Export ist beim Generieren der Seiten eine Zeitüberschreitung aufgetreten oder ein Fehler aufgetreten.

## Integration mit anderen Tools [integration-with-other-tools]

Anwendungen können die AppleScript-Oberfläche von Marked verwenden, um Dokumentmetadaten zu lesen. Für Shell-gesteuerte Workflows, Ordner-Watcher und Editor-Rückrufe ist der [URL-Handler](URL_Handler.html) oft einfacher. Das [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) enthält zusätzliche Skripte und Dienste.