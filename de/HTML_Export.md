# <%= @title %>

Marked exportiert HTML aus Ihrer **Live-Vorschau** – genau die gerenderte Ausgabe, die Sie auf dem Bildschirm sehen. Verwenden Sie den HTML-Export, wenn Sie ein Snippet für ein Blog oder CMS oder eine eigenständige `.html`-Datei mit eingebetteten Stilen und Bildern benötigen, die Sie in jedem Browser öffnen oder beliebig hosten können.

Der typische Arbeitsablauf lautet: **zuerst die Vorschau prüfen, dann HTML exportieren**. Öffnen oder kompilieren Sie Ihr Dokument in Marked, wählen Sie einen Stil, lesen Sie es in der Live-Vorschau Korrektur und exportieren Sie es, sobald das Markup richtig aussieht.

## Zwei Wege zum HTML-Code [two-ways-to-get-html]

### HTML kopieren (Snippet) [copy-html-snippet]

**HTML kopieren** legt den HTML-Quelltext der Vorschau in der Zwischenablage ab. Von dort können Sie ihn in WordPress, Ghost, Squarespace, ein Forum, eine E-Mail-Vorlage oder jede andere App einfügen, die HTML-Fragmente akzeptiert.

* Zahnradmenü → **HTML kopieren** oder bei fokussierter Vorschau {% kbd shift cmd C %}
* Kopiert den **gerenderten HTML-Inhalt** (kein vollständiges Dokument mit `<html>`-Rahmen)
* Optional: Aktivieren Sie unter {% prefspane Export %} **Bilder beim Kopieren von HTML einbetten**, um lokale Bilder als Base64-codierte `data:`-URLs in den kopierten Quelltext einzubetten

Diese Methode eignet sich, wenn das Ziel bereits ein eigenes Stylesheet verwendet und Sie nur das Markup des Inhalts benötigen.

### HTML speichern (Datei) [save-html-file]

**HTML speichern** schreibt eine vollständige `.html`-Datei auf die Festplatte.

* Zahnradmenü → **HTML speichern**, {% kbd cmd S %} oder **HTML** im [Exportbereich](Exporting.html#drawer) ({% kbd shift cmd e %})
* Wählen Sie im Speicherdialog einen Dateinamen und Speicherort
* Konfigurieren Sie die Exportoptionen im Zusatzbereich des Dialogs (siehe unten)

Eine HTML-Datei eignet sich zum Archivieren, zum Weitergeben einer eigenständigen Datei oder zum direkten Öffnen des Ergebnisses in einem Browser.

## Optionen für „HTML speichern“ [save-html-options]

Der Dialog „HTML speichern“ enthält eine Auswahl für Exportprofile und folgende Optionen:

![Optionen für „HTML speichern“][savehtml]

**Stil in Ausgabe einschließen**

Ist diese Option aktiviert, bettet Marked das CSS des ausgewählten Vorschaustils in einen `<style>`-Block der exportierten Datei ein. Wählen Sie im Stilmenü neben dem Kontrollkästchen einen integrierten Stil oder einen [eigenen Stil](Custom_Styles.html). Die Ausgabe ist ein vollständiges HTML-Dokument mit `<!DOCTYPE html>`, `<head>` und einem `div` mit der ID `#wrapper` um Ihren Inhalt – entsprechend der Vorschau.

Ist die Option deaktiviert, speichert Marked ein minimales HTML-Dokument, das nur den gerenderten Inhalt enthält (ohne CSS des Marked-Stils). Verwenden Sie diese Variante, wenn Sie reines HTML in ein anderes System einfügen oder importieren möchten, das eigene Stile bereitstellt.

**Lokale Bilder für eigenständiges HTML einbetten**

Wenn **Stil in Ausgabe einschließen** aktiviert ist, können Sie lokale Bilder als Base64-codierte `data:`-URLs in die HTML-Datei einbetten. So entsteht eine einzelne Datei, die Sie ohne separaten `images/`-Ordner per E-Mail versenden, hochladen oder hosten können.

* Funktioniert mit Bildern, die über **relative oder absolute Pfade** auf dem lokalen Laufwerk referenziert werden
* Vermeiden Sie `file:///`-URLs – sie lassen sich nicht zuverlässig einbetten
* Externe Bilder (http/https) bleiben externe URLs, sofern Sie sie nicht zuerst herunterladen
* Die Base64-Einbettung kann große Dateien erzeugen; verwenden Sie sie, wenn Portabilität wichtiger ist als die Dateigröße

**JavaScript mit Syntaxhervorhebung einbinden**

Wenn die Syntaxhervorhebung unter {% prefspane Preview %} aktiviert ist, fügt diese Option CSS und JavaScript von highlight.js über ein CDN hinzu, damit Codeblöcke in der exportierten Datei farblich hervorgehoben bleiben. Zum Laden der CDN-Ressourcen benötigt das exportierte HTML eine Internetverbindung.

**CDN-Link für MathJax oder KaTeX einschließen**

Wenn [MathJax](MathJax.html) oder KaTeX für die Vorschau aktiviert ist, können Sie die passenden CDN-Skripte in das gespeicherte HTML einschließen, damit Gleichungen in einem Browser gerendert werden. Wie bei der Syntaxhervorhebung ist hierfür beim Anzeigen der Datei Netzwerkzugriff erforderlich, es sei denn, Sie hosten die Skripts selbst.

**CriticMarkup Exporttyp**

Bei Dokumenten mit [CriticMarkup](CriticMarkup.html) können Sie wählen, ob der Export den bearbeiteten Text, den Originaltext oder das vollständige Markup zeigt.

**Exportprofil**

Wählen Sie ein gespeichertes [Exportprofil](Exporting.html#export-profiles), um Ihre bevorzugten HTML-Exporteinstellungen für eingebettete Stile, Bilder, Syntaxhervorhebung und Mathematik in einem Schritt wiederherzustellen.

## Gestaltung mit integrierten und eigenen Stilen [styling-with-built-in-and-custom-themes]

Der **Vorschaustil** bestimmt das Erscheinungsbild des HTML-Dokuments, wenn **Stil in Ausgabe einschließen** aktiviert ist:

1. Wählen Sie einen Stil aus dem Stilmenü des Vorschaufensters (oder legen Sie einen Standard in {% prefspane Style %} fest).
2. Überprüfen Sie Typografie, Überschriften, Codeblöcke und Bilder in der Live-Vorschau.
3. Speichern Sie HTML mit demselben Stil, der im Exportdialog ausgewählt wurde.

Jeder integrierte Marked-Stil – Swiss, GitHub, Manuscript und alle weiteren – kann eingebettet werden. [Eigene Stile](Custom_Styles.html) und Stile aus dem [Stil-Manager](Custom_Styles.html) funktionieren genauso.

I> Manche CSS-Regeln, die nur für die Vorschau gedacht sind (feste Positionierung, Viewport-Techniken, Dunkelmodus-Invertierung mit `@media screen`), lassen sich außerhalb von Marked nicht immer unverändert darstellen. Prüfen Sie die gespeicherte Datei vor der Veröffentlichung in einem Browser.

Hinweise zur Erstellung finden Sie unter [Eigenes CSS erstellen](Writing_Custom_CSS.html).

## Metadaten und MultiMarkdown-Header [metadata-and-multimarkdown-headers]

MultiMarkdown-Metadaten oben in Ihrer Quelldatei können sich auf den HTML-Export auswirken:

* **`Title:`** – wird beim Speichern eines vollständigen HTML-Dokuments für das Element `<title>` verwendet
* **`XHTML Header:`** / **`HTML Header:`** – fügt zusätzliche Tags in das exportierte `<head>` ein (Skripte, Link-Tags, Meta-Tags)
* Andere Metadatenschlüssel werden entsprechend dem gewählten [Markdown-Prozessor](Choosing_a_Processor.html) verarbeitet

Wenn Sie Metadaten für Exporteinstellungen verwenden, die Schlüssel aber nicht in anderen Ausgaben sichtbar sein sollen, schließen Sie sie in HTML-Kommentare ein. Marked findet und verarbeitet auskommentierte Metadaten an jeder Stelle im Dokument. Siehe [Dokumentspezifische Einstellungen](Per-Document_Settings.html).

## Dokumente mit mehreren Dateien [multi-file-documents]

Verwenden Sie für Bücher und Kapitelsammlungen [Dokumente mit mehreren Dateien](Multi-File_Documents.html). Marked zeigt eine Vorschau des zusammengeführten Dokuments und exportiert aus dem kompilierten Ergebnis eine HTML-Datei. Eingebundene Dateien werden durch HTML-Kommentare mit ihren Quellpfaden gekennzeichnet – hilfreich, wenn Sie prüfen möchten, aus welchem Kapitel ein Abschnitt stammt.

## Einfügen in andere Anwendungen [pasting-into-other-applications]

| Ziel | Vorgeschlagener Ansatz |
| :-- | :-- |
| Blog / CMS mit eigenem Stil | **HTML kopieren** (Snippet ohne eingebettetes Marked-CSS) |
| Statische Website oder Archiv | **HTML speichern** mit **Stil in Ausgabe einschließen** |
| E-Mail oder Dateifreigabe (ein Anhang) | **HTML speichern** mit **Lokale Bilder einbetten** |
| WordPress, Ghost, Notion usw. | **HTML kopieren**; aktivieren Sie **Bilder beim Kopieren von HTML einbetten**, wenn der Editor lokale Pfade nicht auflöst |
| Weitere Bearbeitung in einem Code-Editor | **HTML speichern** ohne eingebetteten Stil oder das Snippet kopieren und manuell einbetten |

[Formatierten Text kopieren](Exporting.html#rtfexportoptions) im Zahnradmenü ist eine Alternative, wenn die Ziel-App formatierten Text statt HTML-Quelltext akzeptiert.

## Verwandte Themen [related-topics]

* [Exportieren](Exporting.html) – Exportbereich, Profile und weitere Formate
* [EPUB-Export](EPUB_Export.html) – E-Book-Ausgabe mit eingebettetem CSS
* [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html) – Arbeitsablauf vor dem Export prüfen
* [Eigene Stile](Custom_Styles.html) und [Einstellungen: Export](Settings_Export.html)
* [HTML-spezifische Einstellungen](HTML_Specific_Settings.html) – Prozessoroptionen für die HTML-Ausgabe
* [AppleScript-Export](AppleScript_Support.html) – Kopieren und Speichern von HTML automatisieren

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r
