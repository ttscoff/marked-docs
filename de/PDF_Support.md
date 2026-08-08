# <%= @title %>

Marked kann PDF-Dokumente (`.pdf`) direkt öffnen. Ziehen Sie eine Datei auf Marked oder verwenden Sie {% appmenu Ablage, Öffnen… ({{cmd}}O) %}. Das Dokument wird zur Vorschau und zum Export in Markdown konvertiert.

Der PDF-Import funktioniert am besten bei **kleineren, textbasierten PDFs** (Folien, Artikel, kurze Berichte). Große Handbücher, Bücher und gescannte Dokumente werden unterstützt, aber oft langsam oder unvollständig konvertiert – siehe **Einschränkungen** unten.

Marked ist immer noch ein **Vorschau**-Tool: Sie bearbeiten das PDF nicht in Marked. Verwenden Sie {% kbd cmd E %}, um das PDF in der **Vorschau** (oder Ihrem Systemstandard) zu öffnen, und Marked wird aktualisiert, wenn sich die Datei auf der Festplatte ändert.

## So funktioniert die Konvertierung [how-conversion-works]

Der PDF-Import verwendet die Bibliothek [pdf22md](https://github.com/twardoch/pdf22md) (MIT-Lizenz; siehe [pdf22md-Lizenz](PDF22MD_License.html)). Marked führt die Konvertierung im Hintergrund aus und zeigt gleichzeitig einen kurzen **Konvertierungshinweis** an.

Der Konverter:

- Extrahiert **Text** aus digitalen PDFs mit PDFKit
- Verwendet **Vision OCR** auf Seiten, auf denen eingebetteter Text fehlt (häufig bei Scans)
- Erkennt **Überschriften** nach Möglichkeit anhand der Schriftgröße
- Speichert **Bilder** in einem Ordner `assets` neben dem generierten Markdown

Marked aktiviert die optionale KI-Bereinigung von pdf22md in der App **nicht**. Die Konvertierungsqualität hängt davon ab, wie das PDF erstellt wurde.

## Cache und Live-Vorschau [cache-and-live-preview]

Das konvertierte Markdown und die Bilder werden im Watchers-Cache von Marked gespeichert (`~/Library/Caches/Marked/Watchers/PDF/`). Der ursprüngliche PDF-Pfad bleibt die Dokumentquelle für die Dateiüberwachung.

Wenn Sie das PDF in einer anderen Anwendung speichern oder ersetzen, erkennt Marked die Änderung und führt automatisch eine erneute Konvertierung durch (dasselbe Verhalten beim zusammengeführten Neuladen wie [RTF](RTF_Support.html) und [Scrivener](Scrivener_Support.html)).

## Export und andere Funktionen [export-and-other-features]

Nach der Konvertierung behandelt Marked das Dokument wie andere kompilierte Quellen: Export, Statistiken und die meisten Vorschaufunktionen werden für das generierte Markdown ausgeführt. Bildpfade in der Vorschau verweisen auf zwischengespeicherte Assets, bis Sie sie exportieren.

## Einschränkungen [limitations]

Sie sollten keine zu hohen Erwartungen haben – die Umwandlung von PDF zu Markdown ist nützlich, nicht perfekt.

**Was gut funktioniert**

- **Vektor- und textbasierte PDFs** mit echtem eingebettetem Text (exportiert aus Word, Pages, InDesign usw.)
- **Mäßige Länge** – ein paar Dutzend Seiten werden normalerweise in angemessener Zeit mit guter Struktur umgewandelt

**Was ist unzuverlässig**

- **OCR (gescannte PDFs)** – Vision füllt fehlenden Text aus, aber die Genauigkeit ist im Vergleich zu einem speziellen OCR-Tool oft schlecht; Rechnen Sie mit Tippfehlern, abgehackten Wörtern und fehlenden Spalten
- **Tabellen** – das Layout wird anhand der Textpositionen erraten; Zusammengeführte Zellen, verschachtelte Tabellen und komplexe Gitter überleben selten als saubere Markdown-Tabellen
- **Bildplatzierung** – Abbildungen werden nach `assets/` extrahiert, aber Ausrichtung, Beschriftungen und Textumbruch um Bilder werden nicht zuverlässig beibehalten

**Größe und Leistung**

- **Große PDFs** (Benutzerhandbücher, Lehrbücher, lange Handbücher) können **sehr lange** zum Konvertieren benötigen, viel Speicher verbrauchen oder kein brauchbares Markdown erzeugen. Marked bleibt reaktionsfähig, während die Konvertierung im Hintergrund ausgeführt wird. Es gibt jedoch keine Garantie dafür, dass ein 500-seitiges Handbuch erfolgreich übernommen wird
- Wenn die Konvertierung mit wenig oder keinem Inhalt abgeschlossen wird, zeigt Marked einen Fehler an und hinterlässt keine leere Vorschau

**Weitere Grenzen**

- **Passwortgeschützte PDFs** werden in Version 1 nicht unterstützt
- **Eingebettete PDF-Bilder in Markdown** (`![]()`, die auf eine `.pdf`-Datei verweisen) haben nichts mit dem PDF-Import zu tun – nur das Öffnen eines `.pdf` als Hauptdokument löst die Konvertierung aus

Für Word-Dokumente verwenden Sie [Arbeiten mit DOCX](Working_With_DOCX.html). Verwenden Sie für Rich Text [RTF- und RTFD-Unterstützung](RTF_Support.html).

## Verwandte Themen [related-topics]

- [Dateien öffnen](Opening_Files.html) – Drag & Drop, Zuletzt geöffnet, Zwischenablage
- [Export](Exporting.html) – Speichern Sie HTML, PDF, DOCX und Markdown aus der Vorschau
- [pdf22md-Lizenz](PDF22MD_License.html) – MIT-Lizenztext eines Drittanbieters
