# <%= @title %>

Marked enthält native **Verknüpfungen**-Aktionen (App Intents) zum Öffnen von Dateien, Ändern von Vorschaustilen und Exportieren von Dokumenten. Diese Aktionen werden in der Shortcuts-App angezeigt, wenn Sie nach **Marked** suchen, und sind auf **macOS 13 (Ventura)** oder höher verfügbar.

Informationen zur skriptbasierten Automatisierung mit einem vollständigen Objektmodell finden Sie unter [AppleScript Support](AppleScript_Support.html). Informationen zu URL-basierten Workflows aus der Shell finden Sie unter [URL Handler](URL_Handler.html).

## Aktionen finden

1. Öffnen Sie die **Shortcuts**-App.
2. Erstellen Sie eine neue Verknüpfung oder bearbeiten Sie eine vorhandene.
3. Durchsuchen Sie die Aktionsbibliothek nach **Marked**.

Aktionen sind unter **Dokumente** und **Exportieren** gruppiert. Marked registriert auch Siri-Sätze wie „Datei mit Marked exportieren“ und „In Marked öffnen“ für schnelle Verknüpfungen.

## Aktionsübersicht

| Aktion | Zweck |
| --- | --- |
| **Datei öffnen in Marked** | Öffnen Sie eine Markdown- oder Textdatei in einem Vorschaufenster. |
| **Vorschaustil festlegen** | Ändern Sie das Vorschauthema für ein geöffnetes Dokument (oder öffnen Sie zuerst eine Datei). |
| **Datei öffnen und exportieren** | Öffnen Sie eine Datei und exportieren Sie sie dann in ein anderes Format. |
| **Dokument exportieren** | Exportieren Sie ein geöffnetes Dokument (Frontfenster oder eine bestimmte Datei). |
| **Offene Dokumente exportieren** | Exportieren Sie jedes Dokument, das derzeit in Marked geöffnet ist. |

Alle Exportaktionen geben die exportierte Datei (oder Dateien) als Shortcuts **Datei**-Ausgabe zurück, sodass Sie sie an den nächsten Schritt (Mail, Finder, eine andere App) übergeben können.

## Datei in Marked öffnen

**Parameter:** **Datei** – das zu öffnende Dokument (aus dem Finder, dem Freigabeblatt oder einem vorherigen Verknüpfungsschritt).

Marked öffnet die Datei in einem Vorschaufenster. Verwenden Sie diese Option, wenn Sie in Marked eine Vorschau anzeigen oder bearbeiten möchten, bevor Sie etwas anderes tun.

## Vorschaustil festlegen

**Parameter:**

- **Stil** – Vorschau des Stils aus einer Auswahl (gleiche Namen wie das Vorschau-Stil-Menü und der Stil-Manager).
- **Datei** (optional) – eine bestimmte Datei. Wenn es weggelassen wird, verwendet Marked das Frontdokument. Wenn die Datei noch nicht geöffnet ist, wird sie zuerst von Marked geöffnet.

Durch das Festlegen eines Stils wird die Vorschau mit diesem Thema neu geladen (dasselbe gilt für die Auswahl eines Stils aus dem Vorschau-Stilmenü).

## Aktionen exportieren

Exportaktionen haben dieselben Kernoptionen:

| Parameter | Beschreibung |
| --- | --- |
| **Formatieren** | Markdown, HTML, Paginiert PDF, Fortlaufend PDF, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack oder OPML. |
| **Profil** (optional) | Ein gespeichertes Exportprofil von {% prefspane Export %}. |
| **Stil** (optional) | Vorschaustil, der vor dem Export angewendet werden soll (vollständiges Neuladen der Vorschau). |
| **Seitengröße** (optional) | Name der Seitengröße drucken, z. B. `A4` oder `Letter`. |
| **Ränder** (optional) | Margin-Kurzschrift (siehe unten). |
| **Schriftgröße** (optional) | Basisschriftgröße in Punkt für den PDF-Export, z. B. `14` oder `12pt`. |
| **Ausgabedatei** / **Ausgabeordner** (optional) | Zielpfad. Wenn es weggelassen wird, schreibt Marked mit der richtigen Erweiterung neben die Quelldatei. |

**Anmerkungen**

- **Paginated PDF** verwendet dieselbe Drucklayout-Pipeline wie {% appmenu Ablage, Exportieren als, PDF speichern (paginiert) %}. Es ist nicht für rohe HTML-Vorschaudokumente verfügbar.
- **HTML**-Export verwendet die gerenderte Vorschau (was Sie in der WebView sehen), nicht die rohe Markdown-Quelldatei.
- **Kontinuierlich PDF** erfasst das aktuelle Vorschau-WebView-Layout.
- **Schriftgröße** aktiviert die gleiche benutzerdefinierte Export-/Druck-Schriftgrößenoption von {% prefspane Export %}. Fountain-Dokumente sind davon nicht betroffen.

### Datei öffnen und exportieren

Am besten für Finder-Workflows: Wählen Sie eine Markdown-Datei aus, öffnen Sie sie in Marked und exportieren Sie sie in einem Schritt.

**Parameter:** **Datei** (erforderlich), plus die oben genannten Exportoptionen.

Beispielverwendung: eine Schnellaktion, die Dateien aus dem Finder übernimmt und **Paginiertes PDF** mit einem ausgewählten Profil und Stil exportiert.

### Dokument exportieren

Exportieren Sie ein Dokument, das in Marked **bereits geöffnet** ist.

**Parameter:**

- **Datei** (optional) – eine bestimmte geöffnete Datei. Wenn es weggelassen wird, exportiert Marked das vordere Dokument.
- Exportoptionen und **Ausgabedatei** wie oben.

Verwenden Sie dies, wenn Marked bereits ausgeführt wird und Sie die aktuelle Vorschau exportieren möchten, ohne die Datei erneut zu öffnen.

### Geöffnete Dokumente exportieren

Exportieren Sie **jedes** Vorschaudokument, das derzeit in Marked geöffnet ist.

**Parameter:**

- **Format** und Exportoptionen (Profil, Stil, Seitengröße, Ränder, Schriftgröße).
- **Ausgabeordner** (optional) – Verzeichnis für exportierte Dateien. Wenn es weggelassen wird, wird jede Datei zusammen mit ihrem Quelldokument exportiert.

Nützlich für den Batch-Export nach Durchsicht mehrerer Kapitel oder Notizen in Marked.

## Margin-Kurzschrift

Wenn **Ränder** für eine Exportaktion festgelegt ist, verwenden Sie eine Zeichenfolge mit ein bis vier Maßen. Einheiten: `in`, `cm`, `mm`, `pt` oder `"` für Zoll. Eine Zahl ohne Einheit wird als Punkt behandelt.

| Wert | Bedeutung |
| --- | --- |
| `1in` | Alle Seiten |
| `1in 2in` | Oben und unten `1in`, links und rechts `2in` |
| `1in 2in 1in` | Oben `1in`, links und rechts `2in`, unten `1in` |
| `1in 2in 1in 2in` | Oben, rechts, unten, links |

Dies entspricht dem Schlüssel `margins` in den Exportdatensätzen [AppleScript](AppleScript_Support.html#with-options-properties-record).

## Beispiel-Workflows

### Finder-Datei zu PDF

1. **Datei öffnen und exportieren**
2. **Datei** – Eingabe aus Share Sheet oder Finder Quick Action.
3. **Format** – Paginiert PDF.
4. **Stil** – optionales Thema (zum Beispiel Amblin).
5. **Profil** – optionales gespeichertes Exportprofil.
6. **Ausgabedatei** – optional; Lassen Sie das Feld leer, um `filename.pdf` neben die Quelle zu schreiben.

### Exportieren Sie, was in Marked geöffnet ist

1. **Dokument exportieren**
2. Lassen Sie **Datei** leer, um das vordere Fenster zu verwenden.
3. Wählen Sie **Format** und optional ein Profil oder einen Stil.

### Batch-Export geöffneter Dokumente

1. **Offene Dokumente exportieren**
2. Wählen Sie **Format** (zum Beispiel EPUB).
3. Legen Sie optional **Ausgabeordner** fest, um alle Exporte in einem Verzeichnis zu sammeln.

### Stylen und dann exportieren (zwei Schritte)

1. **Vorschaustil festlegen** – Wählen Sie einen Stil aus (optional als Ziel für eine bestimmte **Datei**).
2. **Dokument exportieren** – dieselbe Datei oder dasselbe Frontdokument mit dem gewünschten **Format**.

Sie können **Style** auch direkt an eine Exportaktion übergeben; Marked wendet das Design an und wartet vor dem Exportieren auf das erneute Laden der Vorschau.

## Exportpfade und Sandboxing

- Wenn **Ausgabedatei** oder **Ausgabeordner** weggelassen wird, schreibt Marked neben das Quelldokument.
- Marked kann Zwischenordner erstellen, wenn der Exportpfad **im Ordner des geöffneten Dokuments** liegt.
– Exporte außerhalb des Ordners des Dokuments erfordern einen beschreibbaren Pfad, auf den Marked zugreifen kann (Speicherort des Dokuments, sicherheitsbezogene Lesezeichen oder Ordner, die Sie über Dialogfelder zum Öffnen gewährt haben).

Siehe [AppleScript Support](AppleScript_Support.html#export-paths-and-sandboxing) für die gleichen Sandbox-Regeln.

## Legacy `convert_to` Aktion

Das AppleScript-Wörterbuch stellt weiterhin **`convert_to`** für die Konvertierung von Markdown-Texten oder -Dateien ohne geöffnete Vorschau bereit. Die oben genannten nativen Shortcuts-Aktionen werden bevorzugt: Sie öffnen Dokumente ordnungsgemäß, warten auf das Laden der Vorschau und unterstützen den paginierten PDF-Export asynchron.

Weitere Informationen zum Legacy-Befehl finden Sie unter [Shortcuts and <!--MKPH0--> in AppleScript Support](AppleScript_Support.html#shortcuts-and-convert_to).

## Fehlerbehebung: Aktionen werden nicht in den Verknüpfungen angezeigt

Verknüpfungen indizieren **eine** Marked-Installation pro Bundle-ID (`com.brettterpstra.marked`). Es bevorzugt die Kopie mit der **höchsten Build-Nummer** (`CFBundleVersion`), nicht unbedingt die App, die Sie gerade in Xcode erstellt haben.

Wenn Marked nicht unter **Apps** in der Shortcuts-Aktionsbibliothek angezeigt wird:

1. Listen Sie jede Kopie auf der Festplatte auf:
   ```bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Entfernen oder benennen Sie veraltete Kopien um (z. B. ein altes `Marked.app` auf dem Desktop oder in `/Applications`, das aus einem Build **ohne** Shortcuts-Metadaten kopiert wurde).
3. Führen Sie den Build aus, den Shortcuts verwenden sollen (Xcode **Run**, oder öffnen Sie `.app` direkt in DerivedData).
4. Beenden Sie die **Shortcuts**-App und öffnen Sie sie erneut.

Ein Build, der Verknüpfungen enthält, enthält `Contents/Resources/Metadata.appintents`. Sie können Folgendes überprüfen:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

Beim Start protokolliert Marked `[MKShortcuts] Registering App Intents` in Console.app, wenn die Registrierung ausgeführt wird (macOS 13+).

## Debuggen

Aktivieren Sie den **Debug-Modus** in {% prefspane Advanced %}. Marked protokolliert Exportschritte auf Infoebene mit dem Präfix `[AppleScript]` in Console.app und im Protokollviewer von Marked (die Exportpipeline wird mit AppleScript geteilt).

## Fehler

Häufige Meldungen, wenn eine Aktion fehlschlägt:

- Es ist kein Marked-Dokument verfügbar (nichts geöffnet und keine Datei angegeben).
- Diese Datei ist in Marked nicht geöffnet (verwenden Sie **Datei öffnen** oder **Datei öffnen und exportieren**).
- Unbekannter Name des Exportprofils oder Vorschaustils.
- Zeitüberschreitung beim Warten auf das Laden oder Neuladen der Vorschau.
- Fehler bei der Exportpfadberechtigung oder Fehler bei der Generierung des paginierten PDF.