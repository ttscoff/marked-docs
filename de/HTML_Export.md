Marked exportiert HTML aus Ihrer **Live-Vorschau** – demselben gerenderten Ergebnis, das Sie auf dem Bildschirm sehen. Verwenden Sie den HTML-Export, wenn Sie einen Ausschnitt zum Einfügen in einen Blog oder ein CMS benötigen, oder eine eigenständige `.html`-Datei mit eingebetteten Stilen und Bildern, die Sie in jedem Browser öffnen oder überall hosten können.

Der typische Arbeitsablauf lautet **erst Vorschau, dann HTML exportieren**: Öffnen oder kompilieren Sie Ihr Dokument in Marked, wählen Sie einen Stil, lesen Sie in der Live-Vorschau Korrektur und exportieren Sie dann, wenn das Markup stimmt.

## Zwei Wege zu HTML [two-ways-to-get-html]

### HTML kopieren (Ausschnitt) [copy-html-snippet]

**HTML kopieren** legt den HTML-Quelltext der Vorschau in die Zwischenablage – bereit zum Einfügen in WordPress, Ghost, Squarespace, ein Forum, eine E-Mail-Vorlage oder jede App, die HTML-Fragmente akzeptiert.

* Zahnradmenü → **HTML kopieren**, oder {% kbd shift cmd C %} bei fokussierter Vorschau
* Kopiert das **gerenderte Body-HTML** (kein vollständiges Dokument mit `<html>`-Wrapper)
* Optional: Aktivieren Sie **Bilder beim Kopieren von HTML einbetten** unter {% prefspane Export %}, um lokale Bilder als Base64-codierte `data:`-URLs in den eingefügten Quelltext einzubetten

HTML kopieren eignet sich ideal, wenn Ihr Ziel bereits über ein eigenes Stylesheet verfügt und Sie nur das Inhalts-Markup benötigen.

### HTML speichern (Datei) [save-html-file]

**HTML speichern** schreibt eine vollständige `.html`-Datei auf die Festplatte.

* Export → **HTML speichern**, {% kbd cmd S %}, oder **HTML** im [Export-Bedienfeld](Exporting.html#drawer) ({% kbd shift cmd e %})
* Wählen Sie Dateinamen und Speicherort im Sichern-Dialog
* Konfigurieren Sie die Exportoptionen im Dialog (siehe unten)

HTML speichern eignet sich ideal zum Archivieren, zum Teilen einer eigenständigen Datei oder zum direkten Öffnen des Ergebnisses in einem Browser.

## Optionen für „HTML speichern“ [save-html-options]

Der Dialog „HTML speichern“ enthält eine Auswahl für Exportprofile sowie folgende Optionen:

![HTML-Speicheroptionen][savehtml]

**Stil in Ausgabe einbeziehen**

Wenn aktiviert, bettet Marked das CSS des ausgewählten Vorschau-Stils in einen `<style>`-Block innerhalb der exportierten Datei ein. Wählen Sie im Stilmenü neben dem Kontrollkästchen einen beliebigen integrierten Stil oder [Eigenen Stil](Custom_Styles.html). Die Ausgabe ist ein vollständiges HTML-Dokument mit `<!DOCTYPE html>`, `<head>` und einem `#wrapper`-Div um Ihren Inhalt – passend zu dem, was Sie in der Vorschau gesehen haben.

Wenn deaktiviert, speichert Marked ein minimales HTML-Dokument nur mit Ihrem gerenderten Inhalt (ohne Marked-Stil-CSS). Verwenden Sie diese Option, wenn Sie rohes HTML zum Einfügen oder Importieren in ein anderes System benötigen, das sein eigenes Styling mitbringt.

**Lokale Bilder für eigenständiges HTML einbetten**

Wenn **Stil in Ausgabe einbeziehen** aktiviert ist, können Sie zusätzlich lokale Bilder als Base64-codierte `data:`-URLs in die HTML-Datei einbetten. Das Ergebnis ist eine einzelne Datei, die Sie per E-Mail versenden, hochladen oder hosten können, ohne einen separaten `images/`-Ordner.

* Funktioniert mit Bildern, die über **relative oder absolute Pfade** auf Ihrem lokalen Laufwerk eingebunden sind
* Vermeiden Sie `file:///`-URLs – sie lassen sich nicht zuverlässig einbetten
* Externe Bilder (http/https) bleiben externe URLs, sofern Sie sie nicht vorher herunterladen
* Die Base64-Einbettung kann große Dateien erzeugen; verwenden Sie sie, wenn Portabilität wichtiger ist als die Dateigröße

**JavaScript für Syntaxhervorhebung einbeziehen**

Wenn die Syntaxhervorhebung unter {% prefspane Preview %} aktiviert ist, fügt diese Option highlight.js-CSS und -JavaScript von einem CDN hinzu, damit Codeblöcke ihre Farben in der exportierten Datei behalten. Das exportierte HTML benötigt eine Internetverbindung, damit die CDN-Ressourcen geladen werden können.

**MathJax- oder KaTeX-CDN-Link einbeziehen**

Wenn [MathJax](MathJax.html) oder KaTeX für die Vorschau aktiviert ist, können Sie die passenden CDN-Skripte in das gespeicherte HTML einbeziehen, damit Formeln im Browser dargestellt werden. Wie bei der Syntaxhervorhebung ist dafür beim Betrachten der Datei eine Netzwerkverbindung nötig, sofern Sie die Skripte nicht selbst hosten.

**CriticMarkup-Exporttyp**

Bei Dokumenten mit [CriticMarkup](CriticMarkup.html) können Sie wählen, ob der Export den bearbeiteten Text, den Originaltext oder das vollständige Markup zeigt.

**Exportprofil**

Wählen Sie ein gespeichertes [Exportprofil](Exporting.html#export-profiles), um Ihre bevorzugten HTML-Exporteinstellungen (eingebettete Stile, Bilder, Syntaxhervorhebung, Formeln) in einem Schritt wiederherzustellen.

## Gestaltung mit integrierten und eigenen Stilen [styling-with-built-in-and-custom-themes]

Der **Vorschaustil** bestimmt das HTML-Erscheinungsbild, wenn **Stil in Ausgabe einbeziehen** aktiviert ist:

1. Wählen Sie einen Stil im Stilmenü des Vorschaufensters (oder legen Sie einen Standard unter {% prefspane Style %} fest).
2. Prüfen Sie Typografie, Überschriften, Codeblöcke und Bilder in der Live-Vorschau.
3. Speichern Sie das HTML mit demselben im Exportdialog ausgewählten Stil.

Jeder integrierte Marked-Stil – Swiss, GitHub, Manuscript und die übrigen – lässt sich einbetten. [Eigene Stile](Custom_Styles.html) und Stile aus dem [Stil-Manager](Custom_Styles.html) funktionieren genauso.

**Zusätzliches CSS** aus {% prefspane Style %} wird beim HTML-Export einbezogen, wenn Stile eingebettet werden. Das exportierte `<body>` erhält die Klasse `mk-has-additional-css`, damit die von Marked umgeschriebenen Selektoren für zusätzliches CSS passen. Siehe [Eigenes CSS erstellen](Writing_Custom_CSS.html#additional-css-settings).

I> Manches CSS, das nur in der Vorschau gilt (feste Positionierung, Viewport-Tricks, `@media screen`-Umkehrung für den Dunkelmodus), lässt sich außerhalb von Marked nicht eins zu eins übertragen. Öffnen Sie die gespeicherte Datei vor der Veröffentlichung in einem Browser, um das zu prüfen.

Anleitungen zum Erstellen finden Sie unter [Eigenes CSS erstellen](Writing_Custom_CSS.html).

## Metadaten und MultiMarkdown-Kopfzeilen [metadata-and-multimarkdown-headers]

MultiMarkdown-Metadaten am Anfang Ihrer Quelldatei können sich auf den HTML-Export auswirken:

* **`Title:`** – wird beim Speichern eines vollständigen HTML-Dokuments für das Element `<title>` verwendet
* **`XHTML Header:`** / **`HTML Header:`** – fügt zusätzliche Tags in das exportierte `<head>` ein (Skripte, Link-Tags, Meta-Tags)
* Andere Metadaten-Schlüssel werden entsprechend Ihrem [Markdown-Prozessor](Choosing_a_Processor.html) verarbeitet

Wenn Sie Metadaten für Exporteinstellungen verwenden, die Schlüssel aber in anderen Ausgaben nicht sichtbar sein sollen, setzen Sie sie in HTML-Kommentare – Marked findet und verarbeitet auskommentierte Metadaten an jeder Stelle im Dokument. Siehe [Einstellungen pro Dokument](Per-Document_Settings.html).

## Dokumente aus mehreren Dateien [multi-file-documents]

Für Bücher und aus Kapiteln zusammengesetzte Dokumente verwenden Sie [Multi-File-Dokumente](Multi-File_Documents.html). Marked zeigt eine Vorschau des zusammengeführten Dokuments und exportiert aus dem kompilierten Ergebnis eine einzelne HTML-Datei. Eingebundene Dateien werden mit HTML-Kommentaren markiert, die ihre Quellpfade anzeigen – nützlich, um nachzuvollziehen, welches Kapitel zu welchem Abschnitt beigetragen hat.

## Einfügen in andere Anwendungen [pasting-into-other-applications]

| Ziel | Empfohlenes Vorgehen |
| :-- | :-- |
| Blog/CMS mit eigenem Stil | **HTML kopieren** (Ausschnitt, ohne eingebettetes Marked-CSS) |
| Statische Website oder Archiv | **HTML speichern** mit **Stil in Ausgabe einbeziehen** |
| E-Mail oder Dateifreigabe (ein Anhang) | **HTML speichern** mit **Lokale Bilder einbetten** |
| WordPress, Ghost, Notion usw. | **HTML kopieren**; aktivieren Sie **Bilder beim Kopieren von HTML einbetten**, wenn der Editor lokale Pfade nicht auflöst |
| Weitere Bearbeitung in einem Code-Editor | **HTML speichern** ohne eingebetteten Stil, oder Ausschnitt kopieren und manuell einbetten |

[Rich Text kopieren](Exporting.html#rtfexportoptions) (Zahnradmenü) ist eine Alternative, wenn die Zielanwendung formatierten Text statt HTML-Quelltext akzeptiert.

## Verwandte Themen [related-topics]

* [Export](Exporting.html) – Export-Bedienfeld, Profile und weitere Formate
* [EPUB-Export](EPUB_Export.html) – E-Book-Ausgabe mit eingebettetem CSS
* [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html) – Vorschau-Arbeitsablauf vor dem Export
* [Eigene Stile](Custom_Styles.html) und [Einstellungen: Export](Settings_Export.html)
* [HTML-spezifische Einstellungen](HTML_Specific_Settings.html) – Prozessoroptionen für die HTML-Ausgabe
* [AppleScript-Export](AppleScript_Support.html) – HTML-Kopieren und -Speichern automatisieren

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
