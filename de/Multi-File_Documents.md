# <%= @title %>

Marked erlaubt mehrere verschiedene Syntaxen, um eine Datei in eine andere einzubinden.

## Marked-Syntax

Sie binden externe Dateien in ein einzelnes Vorschaudokument ein, indem Sie am Zeilenanfang die spezielle Syntax `<<[path/file]` verwenden. Über und unter der Zeile sollten Leerzeilen stehen, und der Pfad wird relativ zum Hauptdokument angenommen, sofern er nicht mit einem Schrägstrich (`/`) oder einer Tilde (`~`) beginnt. Schrägstrich (Wurzelverzeichnis) und Tilde (Home-Verzeichnis) dienen zum Definieren absoluter Pfade. Liegen die externen Dateien im selben Ordner wie das Hauptdokument, ist kein Pfad nötig – geben Sie einfach den Dateinamen (Groß-/Kleinschreibung beachten, samt Erweiterung) in die eckigen Klammern ein.

Mit den Metadaten-Headern „Include Base“ oder „Transclude Base“ ändern Sie den Basispfad für eingebundene Dateien, z. B.:

    Transclude Base: ~/Desktop

*Beim Betrachten von Dokumenten mit eingebundenen Dateien können Sie „I“ (Umschalt-I) drücken, um zu sehen, welche eingebundene Datei sich im sichtbaren Bereich befindet. Drücken Sie Return, während der Pfad der eingebundenen Datei angezeigt wird, öffnet sich die Datei im Standardeditor.*

Mit dieser Funktion bauen Sie große Dokumente/Bücher aus mehreren Dateien (z. B. eine Datei pro Kapitel) und legen die Reihenfolge in einer einzigen Indexdatei fest. Wie die Dateien benannt oder die Ordner organisiert sind, spielt keine Rolle: Die Datei, die Sie in Marked öffnen, gilt als Index, und die darin aufgeführten Dateien werden eingebunden. Ein Beispiel für eine Indexdatei eines dreiteiligen Dokuments:

Ordnerstruktur:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Index.md:

    # Document title

    ## Section 1

    <<[sections/section1.md]

    ## Section 2

    <<[sections/section2.md]

    ## Section 3

    <<[sections/section3.md]

Öffnen Sie Index.md in Marked, wird der Inhalt mit allen drei eingebundenen Dateien darin ausgeklappt angezeigt. Alle eingebundenen Dateien werden auf Änderungen überwacht. Anders als das in Marked geöffnete Dokument stützt sich die Verfolgung eingebundener Dateien auf Spotlight, um Aktualisierungen zu erhalten, und die Dateien müssen in einem von Spotlight indizierten Ordner auf Ihrer Festplatte liegen.

Über [Varianten dieser Syntax](Special_Syntax.html#includingcode) binden Sie auch Codefragmente sowie rohes HTML oder Text ein.

Der endgültige HTML-Export eines Dokuments mit Einbindungen enthält am Anfang und Ende des importierten Texts HTML-Kommentare mit dem relativen Pfad der eingebundenen Datei.

**Hinweis:** Je mehr Dateien ein Dokument einbindet, desto länger dauert die Gesamtkompilierung der Vorschau. Marked versucht zu optimieren und zwischenzuspeichern, aber mit wachsender Dokumentgröße sind gewisse Renderverzögerungen zu erwarten.

## MultiMarkdown-Transclude-Syntax

Sie können auch die `{{filename}}`-Syntax nach der neueren MultiMarkdown-Spezifikation verwenden. Marked erkennt `Transclude Base: path` in MMD-Metadaten und nutzt es als Basis für die Dateieinbindung.

„Transclude Base“ wird nur im übergeordneten Dokument erkannt, nicht in zusätzlich eingebundenen Dokumenten. Alle verschachtelten Einbindungen müssen Pfade haben, die auf der ursprünglichen „Transclude Base“ oder auf dem Speicherort des übergeordneten Dokuments beruhen.

Die abgegrenzte Code-Syntax, die MultiMarkdown zum Einbinden von Dateien ohne Verarbeitung bietet, funktioniert in Marked nicht. Verwenden Sie dafür die Syntax `<<(file)` (Codeblock) oder `<<{file}` (roh).

## IA-Writer-Block-Syntax

Marked 2.5.11+ unterstützt die [Content-Block][ia]-Syntax von IA Writer. Das ist eine Referenz, die in einer eigenen Zeile mit einem Schrägstrich (`/`) beginnt. Es kann ein Codebeispiel, ein Bild, eine Markdown-Datei oder eine CSV-Datei sein. Alles wird passend anhand der Erweiterung der eingebundenen Datei behandelt, und CSVs werden nach Möglichkeit [in Markdown-Tabellen umgewandelt][csv].

In IA Writer werden eingebundene Dateien in den iCloud-Container geholt und brauchen nicht immer „echte“ Pfade. In Marked sollten Sie diese Syntax mit einem Pfad (absolut oder relativ) verwenden, sofern die eingebundenen Dateien nicht bereits im selben Ordner wie die Vorschaudatei liegen. Der erste Schrägstrich wird ignoriert; bei einem absoluten Pfad beginnen Sie also mit zwei Schrägstrichen.

Ein Codeausschnitt im selben Ordner wie das Vorschaudokument:

    /snippet.h

Relativer Pfad zu einem Unterordner namens „images“:

    /images/image.png "optional title"

Absoluter Pfad zum Ordner „Dokumente“:

    //Users/username/Documents/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Wie Gliederungs-, Mindmap- und CSV-Einbindungen umgewandelt werden

Binden Sie bestimmte Dateitypen mit `<<[path]` oder der IA-Writer-Block-Syntax ein, wandelt Marked sie um, statt den rohen Dateiinhalt einzufügen. Das Verhalten bei Gliederungen und Mindmaps hängt von der Dateierweiterung und Ihren Einstellungen unter [Einstellungen: Apps → Mindmaps/Gliederungen][mindmaps] ab. CSV-/TSV-Dateien werden immer in Markdown-Tabellen umgewandelt (siehe [Tabellen aus CSV-Dateien erstellen][csv]).

| Format | Erweiterung | Wenn „Als Mermaid einbetten“ **ein** ist | Wenn **aus** |
|--------|------------|-----------------------------------|--------------|
| **iThoughts X** | .itmz | Mermaid-Mindmap-Diagramm (Tidy-Tree) | Vorschaubild aus der .itmz |
| **MindManager** | .mmap | Mermaid-Mindmap-Diagramm | Verschachtelte Markdown-Liste |
| **FreeMind** | .mm | Mermaid-Mindmap-Diagramm | Verschachtelte Markdown-Liste |
| **OPML** | .opml | Mermaid-Mindmap-Diagramm | Verschachtelte Markdown-Liste |
| **OmniOutliner** | .ooutline | Mermaid-Mindmap-Diagramm | Verschachtelte Markdown-Liste |
| **Bike** | .bike | Mermaid-Mindmap (Dateiname als Wurzelknoten) | Verschachtelte Markdown-Liste (kein Dokumenttitel) |
| **CSV / TSV** | .csv, .tsv | Markdown-Tabelle ||
| **RTF / RTFD** | .rtf, .rtfd | Markdown über RTF-Konvertierung (siehe [RTF- und RTFD-Unterstützung](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown über PDF-Konvertierung beim Öffnen als Hauptdokument (siehe [PDF-Unterstützung](PDF_Support.html)) ||

Jedes Gliederungs-/Mindmap-Format hat unter *Mindmaps/Gliederungen* ein eigenes Kontrollkästchen (Mindmaps, OPML-Dateien, Bike-Gliederungen, OmniOutliner-Gliederungen). Schalten Sie ein Format aus, gilt das „Aus“-Verhalten nur für diesen Typ. Formatdetails finden Sie unter [Mindmaps und Gliederungen einbetten](Embedding_Mind_Maps_and_Outlines.html), und unter [Einstellungen: Apps][mindmaps] ändern Sie diese Optionen. Einzelheiten zur CSV-Konvertierung unter [Tabellen aus CSV-Dateien erstellen][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Buchformate

Marked unterstützt auch Indexdateien in Formaten wie [Leanpub][lp], [GitBook][gb] und mmd\_merge (MultiMarkdown). Dateien in solchen Buchformat-Indizes werden auf Änderungen überwacht, und das Ergebnis ist eine vollständige Vorschau Ihres kompilierten Dokuments – genau wie im „Index.md“-Beispiel oben.

### Leanpub

Aktivieren Sie unter {% prefspane Apps %} die Leanpub/GitBook-Unterstützung, werden Dateien namens „Book.txt“ automatisch als Leanpub-Indexdateien behandelt. Das ältere Format „frontmatter:“ wird ebenfalls erkannt.

[Leanpub-Dokumentation.][lpdocs]

Beispiel für eine Leanpub-Book.txt:

    frontmatter:
    Acknowledgments.txt
    Preface.txt
    Introduction.txt
    mainmatter:
    Markdown.txt
    Sample Books.txt
    Inserting Images.txt


### mmd_merge

Für mmd\_merge verlangt Marked, dass die erste Zeile „#merge“ lautet (ein spezieller Marked-Auslöser für mmd\_merge, der als Kommentar behandelt und von anderen Prozessoren ignoriert wird).

[mmd_merge-Dokumentation.][mmdm]

mmd_merge-Beispiel:

    #merge
    metadata.txt
    Chapter-1.md
        sub-chapter-1-1.md
        sub-chapter-1-2.md
    Chapter-2.md
        sub-chapter-2-1.md
        sub-chapter-2-2.md
    FAQ.md
    Acknowledgments.md

### GitBook

Die GitBook-Formatierung verwendet eine Markdown-Liste für Struktur und Inhaltsverzeichnis. Ist die GitBook-Unterstützung unter {% prefspane Apps %} aktiviert, wird eine Datei namens SUMMARY.md gelesen und automatisch ins mmd_merge-Format umgewandelt, was eine vollständige Vorschau Ihres GitBook-Dokuments ermöglicht.

[GitBook-Dokumentation.][gbdocs]

Beispiel für eine GitBook-SUMMARY.md:

    # Summary

    * [Part I](part1/README.md)
        * [Writing is nice](part1/writing.md)
        * [GitBook is nice](part1/gitbook.md)
    * [Part II](part2/README.md)
        * [We love feedback](part2/feedback_please.md)
        * [Better tools for authors](part2/better_tools.md)

GitBook erlaubt Anker im Inhaltsverzeichnis der SUMMARY.md, aber Marked ignoriert diese und bindet das Basisdokument nur einmal ein.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Vorschaufunktionen für Mehrdatei-Dokumente

![Grenzen eingebundener Dateien][2]

   [2]: images/includeboundaries.png @2x width=859px height=239px class=center

Beim Betrachten eines Dokuments mit eingebundenen Dateien helfen Ihnen zwei Funktionen zu erkennen, welche Datei Sie gerade sehen.

* **Tastatur:** Ein Druck auf {% kbd shift I %} zeigt kurz ein Popup mit dem Titel der Datei, die an der aktuellen Scrollposition der Vorschau sichtbar ist.
    * Drücken Sie {% kbd Return %} direkt nach {% kbd I %}, wird die angezeigte Datei in Ihrem externen Editor bearbeitet.
* **Maus:** Wählen Sie im Zahnradmenü „Grenzen eingebetteter Dateien anzeigen“ ({% kbd ctrl cmd B %}), erscheint links in der Vorschau ein farbiger Balken, der segmentiert Anfang und Ende der eingebundenen Dateien markiert. Er zeigt auch verschachtelte Einbindungen. Fahren Sie über einen Abschnitt des Balkens, erscheint der Dateiname; ein Klick öffnet die Datei im gewählten Editor.
