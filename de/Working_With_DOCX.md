# <%= @title %>

Marked bietet umfangreiche Unterstützung für die Arbeit mit Microsoft-Word-Dateien. Der typische Ablauf ist **zuerst Vorschau, dann DOCX-Export**: Öffnen oder überwachen Sie Ihr Markdown in Marked, feilen Sie in der Live-Vorschau an Stil und Korrektur, und exportieren Sie erst nach Word, wenn das Dokument fertig ist.

## DOCX-Dateien öffnen

Marked kann eine DOCX-Datei lesen und in sauberes Markdown umwandeln. Gültige Stilelemente wie Überschriften und Listen werden in ihr Markdown-Äquivalent überführt.

Änderungsverfolgung und Kommentare werden in CriticMarkup umgewandelt. Hervorhebungen werden zu `<mark>`-Tags, gegebenenfalls mit Farben.

## DOCX-Dateien exportieren

Über das Export-Panel erzeugen Sie aus Ihrem Markdown eine DOCX-Datei. Im Speicherdialog können Sie einen integrierten Stil angeben – dieser Stil lässt sich in Word ganz einfach ändern, indem Sie die Designauswahl öffnen und ein neues Design wählen.

### Kopf- und Fußzeilen

Wenn Sie Kopf- und Fußzeilen in {% prefspane Export %} konfigurieren, sind diese im exportierten DOCX enthalten. Standardplatzhalter wie `%title`, `%date`, `%page` und `%total` werden beim Export ersetzt. `%logo` und `%image` betten das Logo aus den Kopf-/Fußzeileneinstellungen ein. `%md_*`-Metadatenvariablen werden aus den MultiMarkdown-Metadaten des Dokuments aufgelöst. `%h1`–`%h6` werden zu Word-**STYLEREF**-Feldern, die an die exportierten Überschriftenstile gebunden sind; Word füllt sie aus, wenn Sie das Dokument öffnen. Die vollständige Variablenliste sowie die Unterschiede zwischen dem Verhalten bei DOCX und bei Druck/PDF finden Sie unter [Export](Exporting.html#headers-and-footers).

## Änderungsverfolgung

CriticMarkup-Syntax in einem Markdown-Dokument wird beim Export nach DOCX in die Word-Änderungsverfolgung umgewandelt. Kommentare zu Einfügungen, Löschungen und Ersetzungen erscheinen in Word in der rechten Spalte, sobald die Änderungsverfolgung aktiviert ist.

Beim Importieren einer DOCX-Datei in Marked wird die Änderungsverfolgung passend in CriticMarkup und `<mark>`-Tags umgewandelt.

## Mathematik

Im Dokument angezeigte MathJax- und KaTeX-Gleichungen werden für die Darstellung in Word in MathML umgewandelt. Diese Umwandlung ist nicht perfekt, ergibt aber in den meisten Fällen einen gültigen Formelblock im Word-Dokument. Das gilt nur für den Export – Formelblöcke in Word-Dokumenten werden beim Import nicht umgewandelt.

## Eigene Exportstile hinzufügen

Sie können eigene Exportstile hinzufügen, indem Sie eine Vorlage und eine `styles.xml`-Datei in `~/Library/Application Support/Marked/Custom Word Styles/` ablegen. So erstellen Sie diese:

1. Öffnen Sie eine mit Marked erzeugte DOCX-Datei in Word.
2. Bearbeiten Sie dort die Formatvorlage jedes Elements – Rechtsklick auf die Formatvorlage, dann **Ändern…** – und wählen Sie im Dialog **Formatvorlage ändern** jeweils **Neue auf dieser Vorlage basierende Dokumente**.
3. Speichern Sie die DOCX-Datei.
4. Erzeugen Sie daraus ein Design: Gehen Sie im Menüband auf **Entwurf**, öffnen Sie links den **Designs**-Katalog und klicken Sie auf **Aktuelles Design speichern…**. Benennen Sie es so, wie es in Markeds Stil-Menü erscheinen soll, und speichern Sie es unter `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, wobei `STYLENAME` der Name Ihres Stils ist.
5. Wechseln Sie in den Finder und suchen Sie die aus Word gespeicherte DOCX-Datei. Duplizieren Sie sie, benennen Sie die Kopie in `FILENAME.zip` um und doppelklicken Sie zum Entpacken darauf.
6. Im entpackten Dokument sehen Sie einen Ordner `word`, der eine `styles.xml`-Datei enthält. Kopieren Sie diese `styles.xml` in denselben Ordner wie oben und benennen Sie sie `STYLENAME.xml` (wobei `STYLENAME` der Name Ihres Stils ist). Die `.thmx`- und die `.xml`-Datei sollten denselben Basisnamen tragen (nur mit unterschiedlicher Endung).

Beim nächsten DOCX-Export aus Marked erscheint Ihr neuer Stil im Stil-Menü des Speicherdialogs.
