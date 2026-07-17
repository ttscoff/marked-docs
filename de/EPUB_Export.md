# <%= @title %>

Marked exportiert standardkonforme EPUB-Dateien aus Ihrer Markdown-Vorschau. Sie verwenden dieselben integrierten und eigenen Stile wie die Bildschirmvorschau und sind in **Apple Books**, **Kobo** und anderen gängigen EPUB-Readern lesbar.

Der typische Arbeitsablauf lautet: **zuerst die Vorschau prüfen, dann EPUB exportieren**. Öffnen oder kompilieren Sie Ihr Dokument in Marked, wählen Sie einen Stil, lesen Sie es in der Live-Vorschau Korrektur und exportieren Sie es, sobald das Buch fertig ist.

## EPUB exportieren [exporting-an-epub]

Öffnen Sie den [Exportbereich](Exporting.html#drawer) ({% kbd shift cmd e %}) oder wählen Sie im Zahnradmenü **Speichern unter** und anschließend **EPUB**.

Im Dialog zum Speichern von EPUB können Sie Folgendes festlegen:

* **Titel** – standardmäßig aus den MultiMarkdown-Metadaten oder dem Dateinamen
* **Autor** – standardmäßig Ihr macOS-Benutzername; der zuletzt eingegebene Name wird für den nächsten Export gespeichert
* **Datum** – ISO-Format; kann beim Speichern bearbeitet werden
* **Titelbild** – optionale PNG- oder JPG-Datei; ist keines festgelegt, erzeugt Marked eine Standardvorschau

Marked bettet lokale Bilder in das EPUB ein und kann externe Bilder herunterladen, sodass die fertige Datei eigenständig ist. Vor dem Speichern prüft Marked das exportierte EPUB auf wohlgeformtes XHTML. So entstehen Dateien, die den EPUB-Standards für Verteilung und Barrierefreiheit entsprechen.

Unter [Exportprofile](Exporting.html#export-profiles) erfahren Sie, wie Sie EPUB-Metadaten und Exporteinstellungen zur erneuten Verwendung speichern.

## Gestaltung mit integrierten Stilen [styling-with-built-in-themes]

Der für Ihr Dokument gewählte **Vorschaustil** bestimmt das Erscheinungsbild des EPUB. Jeder integrierte Marked-Stil – Swiss, GitHub, Manuscript und alle weiteren – kann für den EPUB-Export verwendet werden.

1. Wählen Sie einen Stil aus dem Stilmenü des Vorschaufensters (oder legen Sie einen Standard in {% prefspane Style %} fest).
2. Überprüfen Sie Typografie, Überschriften, Codeblöcke und Bilder in der Live-Vorschau.
3. Exportieren Sie als EPUB – Marked bündelt das CSS des Stils im EPUB-Paket.

Zusätzlich zum Vorschaustil wendet Marked exportspezifisches CSS an, damit E-Reader Elemente wie Fußnoten, Tabellen und Codeblöcke mit Syntaxhervorhebung korrekt darstellen. Dokumente im Gliederungsmodus verwenden dafür optimierte Exportstile. [Leanpub](Multi-File_Documents.html)-Indizes namens `Book.txt` verwenden automatisch den Leanpub-Exportstil.

I> EPUB-Reader ignorieren manche CSS-Regeln, die nur für das Web gedacht sind (feste Positionierung, Viewport-Techniken usw.). Die Vorschau in Marked zeigt das angestrebte Ergebnis, E-Reader können Abstände und Schriften jedoch vereinfachen. Prüfen Sie das EPUB vor der Veröffentlichung in Apple Books oder Ihrem Ziel-Reader.

## Gestaltung mit eigenen Stilen [styling-with-custom-themes]

[Eigene Stile](Custom_Styles.html) funktionieren für EPUB genauso wie für die Vorschau und PDF:

* Fügen Sie CSS-Dateien unter {% prefspane Style %} oder im [Stil-Manager](Custom_Styles.html) hinzu.
* Wählen Sie vor dem Export den eigenen Stil aus.
* Marked bettet Ihr Stylesheet in das exportierte EPUB ein.

Tipps für EPUB-taugliches eigenes CSS:

* Verwenden Sie flexible Layouts, relative Einheiten und `max-width: 100%` für Bilder (`#wrapper img { max-width: 100%; }` ist eine gute Grundlage).
* Vermeiden Sie `@media print`-Regeln für die E-Book-Gestaltung; EPUB verwendet die allgemeinen Bildschirmstile sowie das Export-Stylesheet von Marked.
* Die [Dunkelmodus](Previewing.html)-Invertierung der Vorschau verwendet `@media screen`-Abfragen. Die meisten EPUB-Reader verwenden das helle Stylesheet, sofern die Reader-App nicht selbst einen dunklen Stil anwendet.
* Verwenden Sie [Zusätzliches CSS](Custom_Styles.html) in den Stileinstellungen, um alle Stile gleichzeitig anzupassen, beispielsweise mit einer einheitlichen Schriftgröße für alle Exporte.

Hinweise zur Erstellung finden Sie unter [Eigenes CSS erstellen](Writing_Custom_CSS.html).

## Syntaxhervorhebung und Mathematik [syntax-highlighting-and-math]

Wenn unter {% prefspane Export %} **Syntaxhervorhebung beim Export einschließen** aktiviert ist, werden Codeblöcke mit denselben Syntaxfarben wie in der Vorschau exportiert. Mit [MathJax](MathJax.html) gerenderte Formeln werden in der für E-Reader erforderlichen Form in das EPUB eingebunden.

## Metadaten in Ihrer Quelldatei [metadata-in-your-source-file]

Sie können EPUB-Metadaten im Dokument anstelle des Speicherdialogs festlegen. Verwenden Sie am Anfang einer Markdown-Datei (oder auf einer Scrivener-Metadatenseite) Schlüssel im MultiMarkdown-Stil:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` akzeptiert einen zum Dokument relativen oder einen absoluten Pfad. PNG und JPG werden unterstützt. Beim Export überschreiben die Werte aus dem Dialog vorhandene Metadaten oder ergänzen fehlende Angaben.

## Bücher mit mehreren Dateien [multi-file-books]

Stellen Sie bei längeren Werken die Kapitel mit [Dokumenten aus mehreren Dateien](Multi-File_Documents.html) zusammen – über Indexdateien, Scrivener-Exporte, Leanpub-`Book.txt` oder Indizes im GitBook-Stil. Marked überwacht die eingebundenen Dateien, zeigt eine Vorschau des gesamten Buchs und exportiert aus dem kompilierten HTML ein EPUB.

Die Überschriften im kompilierten Dokument bilden das [EPUB-Inhaltsverzeichnis](Document_Navigation.html) für die Navigation in Apple Books und anderen Readern.

## Lesen und Veröffentlichen [reading-and-publishing]

Exportierte EPUBs lassen sich direkt in **Apple Books** öffnen (doppelklicken Sie auf die Datei oder wählen Sie **Ablage → Zur Mediathek hinzufügen**). Sie funktionieren auch in Kobo, Thorium, Calibre und den meisten EPUB-3-kompatiblen Apps.

### Apple Books [apple-books]

Ziehen Sie eine exportierte `.epub`-Datei in die Bücher-App oder fügen Sie sie über **Ablage → Importieren** hinzu. Eigene Typografie und das Titelbild aus Ihrem Marked-Stil bleiben erhalten. Prüfen Sie das Layout vor der Freigabe mit Apple Books auf dem Mac, iPad oder iPhone.

### Kindle Direct Publishing (KDP) [kindle-direct-publishing-kdp]

EPUB ist ein zulässiges Upload-Format für [Kindle Direct Publishing](https://kdp.amazon.com/). Exportieren Sie die `.epub`-Datei aus Marked und laden Sie sie hoch; Amazon konvertiert sie für die Auslieferung auf Kindle-Geräten. KDP akzeptiert auch [DOCX](Working_With_DOCX.html). Die aktuellen Anforderungen finden Sie in Amazons Übersicht der [unterstützten E-Book-Formate](https://kdp.amazon.com/en_US/help/topic/G200634390).

Für neue KDP-Titel **ist MOBI nicht erforderlich**. Marked exportiert kein MOBI.

Optional können Sie das Kindle-Layout vor dem Hochladen mit Amazons kostenlosem [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) prüfen.

## Verwandt [related]

* [HTML-Export](HTML_Export.html) – eigenständiges HTML mit eingebetteten Stilen und Bildern
* [Exportieren](Exporting.html) – Exportbereich, Profile und weitere Formate
* [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html) – Arbeitsablauf vor dem Export prüfen
* [Eigene Stile](Custom_Styles.html) und [Generator für eigene Stile](Custom_Style_Generator.html)
* [Dokumente mit mehreren Dateien](Multi-File_Documents.html) – Bücher und Kapitelindizes
* [AppleScript-Export](AppleScript_Support.html) – EPUB-Export automatisieren
