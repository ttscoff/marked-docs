<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Markiert bietet Ihnen Optionen.

## Live-Vorschau-Workflow

1. Ziehen Sie eine Markdown-Datei auf „Markiert“ (oder verwenden Sie {% appmenu File, Open... ({{cmd}}O) %}).
2. Bearbeiten Sie die Datei in Ihrem bevorzugten Editor.
3. Speichern --- Markiert aktualisiert die Vorschau automatisch.

Siehe [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html) für Tresorüberwachung, Streaming-Vorschau und editorspezifische Anleitungen.

## Zum Dock-Symbol ziehen

Der einfachste Weg, „Markiert“ für eine Datei zu verwenden, die Sie bereits bearbeiten, besteht darin, das Dokumentsymbol aus der Symbolleiste Ihres Editors oder aus dem Finder auf das Markiert-Symbol in Ihrem Dock zu ziehen. Marked beginnt sofort mit der Verfolgung aller darauf abgelegten Markdown-Dateien (oder Textdateien). Sie können Dateien auch direkt aus dem Finder ziehen.

## Verwenden des Menüs

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

Sie können Markdown-Dateien natürlich auch direkt über den Menüpunkt {% appmenu File, Open... ({{cmd}}O) %} öffnen. Markiert funktioniert auch ohne Texteditor einwandfrei. Sie können Ihren Markdown mit nur einem Klick in der Vorschau anzeigen und konvertieren.

Markiert kann auch **`.rtf`- und `.rtfd`**-Dateien direkt öffnen (z. B. Exporte aus Pages oder TextEdit). Sie werden zur Vorschau und Aktualisierung in Markdown konvertiert, wenn Sie sie in der Original-App speichern. Einzelheiten, einschließlich Bilder und Einschränkungen, finden Sie unter [RTF- und RTFD-Unterstützung](RTF_Support.html).

Markiert kann **`.pdf`** Dateien auf die gleiche Weise öffnen: Die Konvertierung wird im Hintergrund ausgeführt und die Vorschau wird nach Abschluss aktualisiert. Dies funktioniert am besten für kürzere, textbasierte PDFs; Große Handbücher und gescannte Dokumente sind langsamer und ungenauer. Einzelheiten und Einschränkungen finden Sie unter [PDF-Unterstützung](PDF_Support.html).

## Aus der Zwischenablage

Wenn Sie kompatiblen Text (z. B. Markdown) in Ihrer Zwischenablage haben, können Sie eine sofortige Vorschau öffnen, indem Sie {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} auswählen. Wenn Sie eine Auswahl aus einem Webbrowser oder einer anderen App kopiert haben, die HTML oder RTF in die Zwischenablage legt, konvertiert Marked sie zur Vorschau in Markdown. Wenn Sie RTF aus einer App wie TextEdit oder Pages einfügen, werden größere Schriftgrößen grob in Überschriftenebenen konvertiert (z. B. wird sehr großer Text zu einer Überschrift der Ebene 1, kleinerer großer Text zu einer Überschrift der Ebene 2 usw.). Sie können mehrere Zwischenablagevorschauen gleichzeitig öffnen und diese in einer neuen Datei speichern, indem Sie {% appmenu File, Save Transient Preview %} wählen.

## Ein neues Dokument erstellen

Mit Markiert können Sie mit dem Befehl {% appmenu File, New ({{cmd}}N) %} eine neue, leere Textdatei erstellen. Sie werden sofort nach einem Speicherort für die Datei gefragt und Sie können die Option „Neue Dateien automatisch bearbeiten“ in {% prefspane Apps %} neben der Schaltfläche „Texteditor“ aktivieren, um die neu erstellte Datei automatisch in Ihrem Standardeditor zu öffnen.

## Zuletzt geöffnet

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked verfolgt auch die neuesten Dokumente. Die Menüoption {% appmenu File, Open Recent %} zeigt Ihnen die Dateien an, die Sie geöffnet hatten, und ermöglicht Ihnen, zu ihnen zurückzukehren. Mit {% kbd shift cmd R %} können Sie die zuletzt angezeigte Datei schnell wieder öffnen. Verwenden Sie {% kbd shift cmd P %} oder [Schnellaktionen](Quick_Actions.html), um Menü- und Vorschaubefehle über die Tastatur auszuführen. Es gibt auch viele andere Tastaturkürzel. Wenn Sie sie lernen möchten, finden Sie eine Tabelle unter [Tastatur Verknüpfungen](Keyboard_Shortcuts.html).

## Neue Ansicht in aktuelle Datei [Multiview]

Verwenden Sie {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, auch im Vorschau-Kontextmenü), um ein zu öffnen
zweites Vorschaufenster für dieselbe gespeicherte Datei. Beide Fenster
Sehen Sie sich die Datei auf der Festplatte an und aktualisieren Sie sie, wenn Sie sie in Ihrem speichern
Editor, aber jede Ansicht behält ihre eigene Scroll-Position,
Lesezeichen, Vorschaustil und [Benutzerdefinierte Regel
überschreibt](Custom_Processor.html#manuallyenabled).

**Beispielhafter Anwendungsfall:** Sie bearbeiten ein langes Manuskript in
MultiMarkdown mit Ihrem gewohnten Stil und Prozessor. Öffnen Sie ein
Zweite Ansicht, wechseln Sie zu einem Korrekturstil und heften Sie einen Prozess an
Regel, die einen anderen integrierten Prozessor ausführt, und aktivieren Sie einen
Manuelle Regel, die Revisionsmarkierungen hervorhebt. Sie vergleichen
Entwurfs- und Proof-Layouts nebeneinander erstellen, ohne zwei beibehalten zu müssen
Kopien der Datei.

Wenn mehr als eine Ansicht einer Datei geöffnet ist, der Fenstertitel
Enthält **Ansicht 2**, **Ansicht 3** usw., damit Sie es erkennen können
Sie können die Fenster im Fenstermenü und in Mission Control auseinanderhalten.

Für nicht gespeicherte Dokumente sind keine alternativen Ansichten verfügbar.
Vorschauen in der Zwischenablage, Streaming-Vorschauen oder ordnerbasiert
Projekte, die keiner einzelnen Datei auf der Festplatte zugeordnet sind.

## Schnell öffnen ##

Sie können schnell zwischen geöffneten Dokumenten wechseln, zuletzt verwendete Dokumente öffnen oder das Dialogfeld „Datei->Öffnen“ mit dem [Schnellöffnen-Bedienfeld](Quick_Open.html) ({% kbd cmd shift o %}) öffnen.