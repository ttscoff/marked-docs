# <%= @title %>

Marked kann PDF-Dokumente (`.pdf`) direkt öffnen. Ziehen Sie eine Datei nach Marked oder verwenden Sie {% appmenu Ablage, Öffnen… ({{cmd}}O) %}. Das Dokument wird zur Vorschau und zum Export in Markdown konvertiert.

Der PDF-Import funktioniert am besten bei **kleineren, textbasierten PDFs** (Folien, Artikel, Kurzberichte). Große Handbücher, Bücher und gescannte Dokumente werden unterstützt, aber oft langsam oder unvollständig konvertiert – siehe **Einschränkungen** unten.

Marked ist immer noch ein **Vorschau**-Tool: Sie bearbeiten den PDF nicht in Marked. Verwenden Sie {% kbd cmd E %}, um PDF in der **Vorschau** (oder Ihrem Systemstandard) zu öffnen, und Marked wird aktualisiert, wenn sich die Datei auf der Festplatte ändert.

## So funktioniert die Konvertierung

Der PDF-Import verwendet die Bibliothek [pdf22md](https://github.com/twardoch/pdf22md) (MIT-Lizenz; siehe [pdf22md License](PDF22MD_License.html)). Marked führt die Konvertierung im Hintergrund aus und zeigt gleichzeitig einen kurzen **Konvertierungshinweis** an.

Der Konverter:

- Extrahiert **Text** aus digitalen PDFs mit PDFKit
- Verwendet **Vision OCR** auf Seiten, auf denen eingebetteter Text fehlt (häufig bei Scans)
- Erkennt **Überschriften** nach Möglichkeit anhand der Schriftgröße
- Speichert **Bilder** in einem Ordner `assets` neben dem generierten Markdown

Marked aktiviert die optionale KI-Bereinigung von pdf22md in der App **nicht**. Die Konvertierungsqualität hängt davon ab, wie der PDF erstellt wurde.

## Cache und Live-Vorschau

Konvertierte Markdown und Bilder werden im Watchers-Cache von Marked gespeichert (`~/Library/Caches/Marked/Watchers/PDF/`). Der ursprüngliche PDF-Pfad bleibt die Dokumentquelle für die Dateiüberwachung.

Wenn Sie PDF in einer anderen Anwendung speichern oder ersetzen, erkennt Marked die Änderung und führt automatisch eine erneute Konvertierung durch (dasselbe Verhalten beim zusammengeführten Neuladen wie [RTF](RTF_Support.html) und [Scrivener](Scrivener_Support.html)).

## Export und andere Funktionen

Nach der Konvertierung behandelt Marked das Dokument wie andere kompilierte Quellen: Export, Statistiken und die meisten Vorschaufunktionen werden für den generierten Markdown ausgeführt. Bildpfade in der Vorschau verweisen auf zwischengespeicherte Assets, bis Sie sie exportieren.

## Einschränkungen

Legen Sie Ihre Erwartungen entsprechend fest – PDF-bis-Markdown ist nützlich, nicht perfekt.

**Was gut funktioniert**

- **Vektor- und textbasierte PDFs** mit echtem eingebettetem Text (exportiert aus Word, Pages, InDesign usw.)
- **Mäßige Länge** – ein paar Dutzend Seiten werden normalerweise in angemessener Zeit mit guter Struktur umgewandelt

**Was ist unzuverlässig**

- **OCR (gescannt PDFs)** – Vision füllt fehlenden Text aus, aber die Genauigkeit ist im Vergleich zu einem speziellen OCR-Tool oft schlecht; Rechnen Sie mit Tippfehlern, gebrochenen Wörtern und fehlenden Spalten
- **Tabellen** – das Layout wird anhand der Textpositionen erraten; Zusammengeführte Zellen, verschachtelte Tabellen und komplexe Gitter überleben selten als saubere Markdown-Tabellen
- **Bildplatzierung** – Abbildungen werden nach `assets/` extrahiert, aber Ausrichtung, Beschriftungen und Textumbruch um Bilder werden nicht zuverlässig beibehalten

**Größe und Leistung**

- **Große PDFs** (Benutzerhandbücher, Lehrbücher, lange Handbücher) können **sehr lange** zum Konvertieren benötigen, viel Speicher verbrauchen oder keine nützlichen Markdown erzeugen. Marked bleibt reaktionsfähig, während die Konvertierung im Hintergrund ausgeführt wird. Es gibt jedoch keine Garantie dafür, dass ein 500-seitiges Handbuch erfolgreich abgeschlossen wird
– Wenn die Konvertierung mit wenig oder keinem Inhalt abgeschlossen wird, zeigt Marked einen Fehler an und hinterlässt keine leere Vorschau

**Andere Grenzwerte**

– **Passwortgeschützte PDFs** werden in Version 1 nicht unterstützt
- **Eingebettete PDF-Bilder in Markdown** (`![]()`, die auf eine `.pdf`-Datei verweisen) haben nichts mit dem PDF-Import zu tun – nur das Öffnen eines `.pdf` als Hauptdokument löst die Konvertierung aus

Für Word-Dokumente verwenden Sie [Working with DOCX](Working_with_DOCX.html). Verwenden Sie für Rich Text [RTF and RTFD Support](RTF_Support.html).

## Verwandte Themen

- [Opening Files](Opening_Files.html) – Drag & Drop, Zuletzt geöffnet, Zwischenablage
- [Exporting](Exporting.html) – Speichern Sie HTML, PDF, DOCX und Markdown aus der Vorschau
- [pdf22md License](PDF22MD_License.html) – MIT-Lizenztext eines Drittanbieters