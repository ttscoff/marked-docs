# <%= @title %>

Marked lässt Ihnen die Wahl.

## Live-Vorschau-Workflow

1. Ziehen Sie eine Markdown-Datei auf Marked (oder verwenden Sie {% appmenu Ablage, Öffnen… ({{cmd}}O) %}).
2. Bearbeiten Sie die Datei in Ihrem bevorzugten Editor.
3. Speichern Sie – Marked aktualisiert die Vorschau automatisch.

Siehe [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html) für Vault-Überwachung, Streaming-Vorschau und editorspezifische Anleitungen.

## Zum Dock-Symbol ziehen

Am einfachsten verwenden Sie Marked für eine Datei, die Sie gerade bearbeiten, indem Sie das Dokumentsymbol aus der Symbolleiste Ihres Editors oder aus dem Finder auf das Marked-Symbol im Dock ziehen. Marked beginnt sofort, jede darauf abgelegte Markdown-Datei (oder Textdatei) zu überwachen. Sie können Dateien auch direkt aus dem Finder ziehen.

## Über das Menü

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

Sie können Markdown-Dateien natürlich auch direkt über die Menüoption {% appmenu Ablage, Öffnen… ({{cmd}}O) %} öffnen. Marked funktioniert auch *ohne* Texteditor einwandfrei. Sie können Markdown mit nur einem Klick in der Vorschau anzeigen und konvertieren.

Marked kann auch **`.rtf`- und `.rtfd`-Dateien** direkt öffnen (z. B. Exporte aus Pages oder TextEdit). Sie werden für die Vorschau in Markdown konvertiert und beim Speichern in der Original-App aktualisiert. Details, einschließlich Bildern und Einschränkungen, finden Sie unter [RTF- und RTFD-Unterstützung](RTF_Support.html).

Marked kann **`.pdf`-Dateien** auf die gleiche Weise öffnen: Die Konvertierung läuft im Hintergrund, und sobald sie abgeschlossen ist, wird die Vorschau aktualisiert. Das funktioniert am besten bei kürzeren, textbasierten PDFs; große Handbücher und gescannte Dokumente sind langsamer und ungenauer. Details und Einschränkungen finden Sie unter [PDF-Unterstützung](PDF_Support.html).

## Aus der Zwischenablage

Wenn Sie kompatiblen Text (z. B. Markdown) in Ihrer Zwischenablage haben, können Sie eine sofortige Vorschau öffnen, indem Sie {% appmenu Ablage, Neu, Zwischenablage-Vorschau ({{shift}}{{cmd}}V) %} auswählen. Falls Sie eine Auswahl aus einem Webbrowser oder einer anderen App kopiert haben, die HTML oder RTF in die Zwischenablage gelegt hat, konvertiert Marked sie für die Vorschau in Markdown. Wenn Sie RTF aus einer App wie TextEdit oder Pages einfügen, werden größere Schriftgrößen grob in Überschriftenebenen umgewandelt (z. B. wird sehr großer Text zu einer Überschrift der Ebene 1, kleinerer großer Text zur Ebene 2 usw.). Sie können mehrere Zwischenablage-Vorschauen gleichzeitig geöffnet haben und sie über {% appmenu Ablage, Schnellvorschau speichern %} in einer neuen Datei speichern.

## Ein neues Dokument erstellen

Mit Marked können Sie über den Befehl {% appmenu Ablage, Neu ({{cmd}}N) %} eine neue, leere Textdatei erstellen. Sie werden sofort nach einem Speicherort für die Datei gefragt, und unter {% prefspane Apps %} können Sie neben der Schaltfläche „Texteditor“ die Option „Neue Dateien automatisch bearbeiten“ aktivieren, um die neu erstellte Datei automatisch in Ihrem Standardeditor zu öffnen.

## Zuletzt geöffnet

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked merkt sich auch die zuletzt geöffneten Dokumente. Die Menüoption {% appmenu Ablage, Zuletzt geöffnet %} zeigt Ihnen die Dateien, die Sie geöffnet hatten, und lässt Sie dorthin zurückkehren. Mit {% kbd shift cmd R %} öffnen Sie schnell die zuletzt angezeigte Datei wieder. Verwenden Sie {% kbd shift cmd P %} oder [Schnellaktionen](Quick_Actions.html), um Menü- und Vorschaubefehle über die Tastatur auszuführen. Es gibt noch viele weitere Tastaturkurzbefehle. Wenn Sie sie lernen möchten, finden Sie eine Übersicht unter [Tastaturkurzbefehle](Keyboard_Shortcuts.html).

## Neue Ansicht der aktuellen Datei [multiview]

Mit {% appmenu Ablage, Neue Ansicht der aktuellen Datei %} ({% kbd shift cmd N %}, auch im Kontextmenü der Vorschau) öffnen Sie ein zweites Vorschaufenster für dieselbe gespeicherte Datei. Beide Fenster überwachen die Datei auf der Festplatte und aktualisieren sich, sobald Sie im Editor speichern. Jede Ansicht behält aber ihre eigene Scroll-Position, ihre Lesezeichen, ihren Vorschaustil und ihre [über Eigene Regeln gesetzten Überschreibungen](Custom_Processor.html#manuallyenabled).

**Beispiel:** Sie bearbeiten ein langes Manuskript in MultiMarkdown mit Ihrem gewohnten Stil und Prozessor. Öffnen Sie eine zweite Ansicht, wechseln Sie dort zu einem Korrekturstil, heften Sie eine Prozessregel an, die einen anderen integrierten Prozessor ausführt, und aktivieren Sie eine manuelle Regel, die Revisionsmarkierungen hervorhebt. So vergleichen Sie Entwurf und Korrekturfassung nebeneinander, ohne zwei Kopien der Datei pflegen zu müssen.

Sind mehrere Ansichten einer Datei geöffnet, enthält der Fenstertitel **Ansicht 2**, **Ansicht 3** und so weiter, damit Sie die Fenster im Menü „Fenster“ und in Mission Control auseinanderhalten können.

Alternative Ansichten sind nicht verfügbar für ungespeicherte Dokumente, Vorschauen aus der Zwischenablage, Streaming-Vorschauen oder ordnerbasierte Projekte, die keiner einzelnen Datei auf der Festplatte entsprechen.

## Schnell öffnen ##

Mit dem [Schnell-öffnen-Panel](Quick_Open.html) ({% kbd cmd shift o %}) wechseln Sie schnell zwischen offenen Dokumenten, rufen zuletzt geöffnete Dokumente auf oder öffnen den Öffnen-Dialog.
