# <%= @title %>

Marked bietet umfangreiche Unterstützung für die Arbeit mit Microsoft-Word-Dateien. Der typische Ablauf ist **zuerst Vorschau, dann DOCX-Export**: Öffnen oder überwachen Sie Ihr Markdown in Marked, feilen Sie in der Live-Vorschau an Stil und Korrektur, und exportieren Sie erst nach Word, wenn das Dokument fertig ist.

## DOCX-Dateien öffnen [opening-docx-files]

Marked kann eine DOCX-Datei lesen und in sauberes Markdown umwandeln. Gültige Stilelemente wie Überschriften und Listen werden in ihr Markdown-Äquivalent überführt.

Änderungsverfolgung und Kommentare werden in CriticMarkup umgewandelt. Hervorhebungen werden zu `<mark>`-Tags, gegebenenfalls mit Farben.

## DOCX-Dateien exportieren [exporting-docx-files]

Über das Export-Panel erzeugen Sie aus Ihrem Markdown eine DOCX-Datei. Im Speicherdialog können Sie einen integrierten Stil angeben – dieser Stil lässt sich in Word ganz einfach ändern, indem Sie die Designauswahl öffnen und ein neues Design wählen.

### Kopf- und Fußzeilen [headers-and-footers]

Wenn Sie Kopf- und Fußzeilen in {% prefspane Export %} konfigurieren, sind diese im exportierten DOCX enthalten. Standardplatzhalter wie `%title`, `%date`, `%page` und `%total` werden beim Export ersetzt. `%logo` und `%image` betten das Logo aus den Kopf-/Fußzeileneinstellungen ein. `%md_*`-Metadatenvariablen werden aus den MultiMarkdown-Metadaten des Dokuments aufgelöst. `%h1`–`%h6` werden zu Word-**STYLEREF**-Feldern, die an die exportierten Überschriftenstile gebunden sind; Word füllt sie aus, wenn Sie das Dokument öffnen. Die vollständige Variablenliste sowie die Unterschiede zwischen dem Verhalten bei DOCX und bei Druck/PDF finden Sie unter [Export](Exporting.html#headers-and-footers).

## Änderungsverfolgung [change-tracking]

CriticMarkup-Syntax in einem Markdown-Dokument wird beim Export nach DOCX in die Word-Änderungsverfolgung umgewandelt. Kommentare zu Einfügungen, Löschungen und Ersetzungen erscheinen in Word in der rechten Spalte, sobald die Änderungsverfolgung aktiviert ist.

Beim Importieren einer DOCX-Datei in Marked wird die Änderungsverfolgung passend in CriticMarkup und `<mark>`-Tags umgewandelt.

## Mathematik [math]

Im Dokument angezeigte MathJax- und KaTeX-Gleichungen werden für die Darstellung in Word in MathML umgewandelt. Diese Umwandlung ist nicht perfekt, ergibt aber in den meisten Fällen einen gültigen Formelblock im Word-Dokument. Das gilt nur für den Export – Formelblöcke in Word-Dokumenten werden beim Import nicht umgewandelt.

## Eigene Exportstile hinzufügen [adding-custom-export-styles]

Sie können eigene Exportstile hinzufügen, indem Sie ein zusammengehöriges Dateipaar in `~/Library/Application Support/Marked/Custom Word Styles/` ablegen:

- `STYLENAME.xml` – die Absatz- und Zeichenformatvorlagen von Word (aus der `word/styles.xml` eines Dokuments)
- `STYLENAME.thmx` – ein optionales Word-Design für Farben, Schriften und Effekte

Ein Word-**Design** (`.thmx`) speichert die Formatvorlagen, die Sie im Dokument bearbeiten, **nicht**. Die liegen im Dokument selbst (oder in einer Vorlage wie `.dotx` / `Normal.dotm`). Marked benötigt die extrahierte `styles.xml` für die Definitionen der Formatvorlagen und die `.thmx` nur für Designfarben, -schriften und -effekte.

So erstellen Sie einen eigenen Exportstil:

1. Öffnen Sie eine mit Marked erzeugte DOCX-Datei in Word.
2. Bearbeiten Sie die Formatvorlagen, auf die es Ihnen ankommt: Rechtsklick auf eine Formatvorlage im Formatvorlagenkatalog oder im Formatvorlagenbereich, dann **Ändern…** (einen eigenen „Formatvorlagen-Editor“ gibt es nicht). Legen Sie Schriften, Abstände und weitere Formatierung fest und speichern Sie die DOCX-Datei.
3. Optional übernehmen Sie Designfarben, -schriften und -effekte: Öffnen Sie den Reiter **Entwurf**, öffnen Sie den Designs-Katalog und wählen Sie **Aktuelles Design speichern…**. Speichern Sie es unter `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx` – mit dem Namen, der in Markeds Stil-Menü erscheinen soll.
4. Duplizieren Sie im Finder die gespeicherte DOCX-Datei, benennen Sie die Kopie in `FILENAME.zip` um und entpacken Sie sie.
5. Kopieren Sie aus dem entpackten Paket die `word/styles.xml` nach `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.xml` (derselbe Basisname wie die `.thmx`, falls Sie eine erstellt haben).

Beim nächsten DOCX-Export aus Marked erscheint Ihr Stil im Stil-Menü des Speicherdialogs.
