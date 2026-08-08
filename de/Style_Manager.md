# <%= @title %>

Der Stil-Manager bietet eine zentrale Oberfläche, um alle Ihre integrierten und Eigenen Stile zu verwalten. Sie steuern damit vollständig, welche Stile in den Menüs erscheinen, in welcher Reihenfolge, mit welchen Tastaturkurzbefehlen und mehr.

## Den Stil-Manager öffnen [opening-the-style-manager]

Um den Stil-Manager zu öffnen, klicken Sie unter {% prefspane Style %} auf die Schaltfläche **Stile verwalten…** oder verwenden Sie {% appmenu Stil, Stile verwalten (~@$m) %}. Sie können CSS-Dateien auch direkt auf das Einstellungsfenster ziehen: Marked importiert sie, öffnet den Stil-Manager und wählt die neu hinzugefügte Zeile für Sie aus.

![Stil-Manager][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## Die Stil-Tabelle [the-style-table]

Der Stil-Manager zeigt alle Ihre Stile in einer sortierbaren Tabelle, die integrierte und eigene Stile nahtlos mischt. Jede Zeile der Tabelle enthält mehrere Spalten:

### Kontrollkästchen „Aktiviert“ [enabled-checkbox]

Das Kontrollkästchen **Aktiviert** fügt den Stil sofort zum Stil-Menü, zum Standardstil-Popup und zu den Tastaturkurzbefehlen hinzu bzw. entfernt ihn daraus. Deaktivieren Sie einen Stil, wird er aus den Menüs ausgeblendet, bleibt aber zur einfachen Reaktivierung im Stil-Manager.

Deaktivieren Sie den gerade aktiven Stil, wechselt Marked automatisch zum nächsten verfügbaren aktivierten Stil.

### Spalte „Name“ [name-column]

Die Spalte **Name** zeigt den Anzeigenamen des Stils. Sie können diesen Namen direkt bearbeiten, indem Sie darauf klicken; Änderungen bleiben erhalten und wirken sich auf jedes Menü aus, in dem der Stil erscheint. Das ist besonders bei eigenen Stilen nützlich, wenn Sie einen aussagekräftigeren Namen als den Dateinamen möchten.

Integrierte Stile haben gesperrte Namen, die sich nicht bearbeiten lassen. Um den Namen eines integrierten Stils anzupassen, duplizieren Sie ihn zuerst, um eine bearbeitbare Kopie zu erhalten.

### Spalte „Quelle“ [source-column]

Die Spalte **Quelle** gibt an, woher der Stil stammt:

- **Integriert**: Stile, die mit Marked geliefert werden und im App-Bundle liegen
- **Eigen**: Stile, die Sie aus CSS-Dateien auf Ihrem Laufwerk hinzugefügt haben
- **Dupliziert**: Stile, die durch Duplizieren eines anderen Stils entstanden sind (integriert oder eigen)

### Spalte „Aktionen“ [actions-column]

Jede Zeile enthält einen **Aktionen**-Block mit Schaltflächen zum Verwalten des jeweiligen Stils:

**Bearbeiten**: Öffnet die CSS-Datei in Ihrem Standardeditor. Integrierte Stile lassen sich nicht direkt bearbeiten – duplizieren Sie sie zuerst, um eine bearbeitbare Kopie zu erhalten.

**Duplizieren**: Erstellt eine Kopie des Stils und eine neue CSS-Datei auf der Festplatte. Das Duplikat erscheint direkt unter dem Originalstil in der Tabelle. Das ist der empfohlene Weg, um integrierte Stile anzupassen.

**Im Finder anzeigen**: Zeigt die CSS-Datei im Finder, damit Sie die Datei auf Ihrem Laufwerk leicht finden. Diese Schaltfläche gibt es nur bei eigenen Stilen mit einem Dateipfad.

**Löschen**: Entfernt den Stil aus Marked. Bei eigenen Stilen können Sie wählen, ob nur die Referenz entfernt wird (die CSS-Datei bleibt) oder die CSS-Datei in den Papierkorb wandert. Integrierte Stile lassen sich nicht löschen, aber deaktivieren.

**Wiederherstellen**: Bei integrierten Stilen setzt diese Schaltfläche den Stil auf seinen Standardzustand zurück, falls er geändert wurde. Sie ist nur bei integrierten Stilen sichtbar.

## Stile neu anordnen [reordering-styles]

Zeilen lassen sich per Drag-and-drop umsortieren. Ziehen Sie eine Stilzeile einfach an eine neue Position in der Tabelle. Die hier festgelegte Reihenfolge steuert:

- die Reihenfolge des Stil-Menüs in Markeds Menüs
- die Tastaturkurzbefehl-Zuweisungen (`⌘1`–`⌘9` für die ersten neun aktivierten Stile, `⌥⌘1`–`⌥⌘0` für die nächsten zehn usw.)

Ziehen Sie Stile also in die Kurzbefehl-Plätze, die sie belegen sollen.

## Stile hinzufügen [adding-styles]

Es gibt mehrere Wege, neue eigene Stile zum Stil-Manager hinzuzufügen:

### Hinzufügen-Schaltfläche [add-button]

Klicken Sie auf die Schaltfläche **Neuen Stil hinzufügen**, um eine Dateiauswahl zu öffnen, in der Sie eine oder mehrere CSS-Dateien zum Import auswählen. Ausgewählte Dateien werden dem Stil-Manager hinzugefügt und standardmäßig aktiviert.

### Drag-and-drop [drag-and-drop]

Sie können CSS-Dateien direkt auf das Stil-Manager-Fenster ziehen. Ziehen Sie Dateien über das Fenster, erscheint ein Overlay mit „Eigenen Stil hinzufügen“ (bzw. „N Eigene Stile hinzufügen“ bei mehreren Dateien). Lassen Sie die Dateien los, um sie zu importieren.

Sie können CSS-Dateien auch an bestimmte Positionen in der Tabelle ziehen – die Ablage-Markierung zeigt, wo der neue Stil eingefügt wird, sodass Sie Import und Positionierung in einem Schritt steuern.

Ziehen Sie CSS-Dateien auf den Einstellungsbereich {% prefspane Style %}, werden sie ebenfalls importiert und der Stil-Manager öffnet sich automatisch.

## Live-Vorschau [live-preview]

Der rechte Bereich des Stil-Managers zeigt eine Live-Vorschau des ausgewählten Stils. Die Vorschau rendert ein umfassendes Beispieldokument mit Überschriften, Listen, Tabellen, Codeblöcken, Blockzitaten und anderen gängigen Markdown-Elementen, alles mit dem tatsächlichen CSS des ausgewählten Stils gestaltet.

Die Vorschau verwendet die CSS-Datei direkt von der Festplatte, sodass Änderungen in Ihrem externen Editor sofort in der Vorschau erscheinen. So sehen Sie Ihre Änderungen beim Entwickeln eigener Stile in Echtzeit.

### Vorschau im Dunkelmodus [dark-mode-preview]

Ein Kontrollkästchen über der Vorschau schaltet zwischen Hell- und Dunkelmodus-Vorschau um. Das ist praktisch, um zu testen, wie Stile in beiden Erscheinungsmodi aussehen – besonders, wenn Sie Stile erstellen, die sich an das Systemerscheinungsbild anpassen.

## Tastaturkurzbefehle [keyboard-shortcuts]

Der Stil-Manager zeigt unter der Tabelle eine Legende, wie die Tastaturkurzbefehle vergeben werden. Die ersten neun aktivierten Stile erhalten {% kbd cmd 1 %} bis {% kbd cmd 9 %} ({% kbd cmd 0 %} ist reserviert), die nächsten zehn erhalten {% kbd opt cmd 1 %} bis {% kbd opt cmd 0 %} usw. Die zugewiesenen Tastaturkurzbefehle sehen Sie im Stil-Popup-Menü jeder Vorschau.

## Deaktivierte Stile filtern [filtering-disabled-styles]

Ein Kontrollkästchen am unteren Fensterrand steuert die Anzeige deaktivierter Stile. Ist es nicht markiert, werden nur aktivierte Stile angezeigt, sodass Sie sich leichter auf Ihre aktiven Stile konzentrieren und sie umsortieren können. Ist es markiert, werden alle Stile (aktiviert und deaktiviert) angezeigt, sodass Sie Ihre gesamte Stilsammlung verwalten.

## Integrierte Stile wiederherstellen [restoring-builtin-styles]

Die Schaltfläche **Alle integrierten Stile wiederherstellen** am unteren Fensterrand setzt alle integrierten Stile auf ihren Standardzustand zurück. Das ist nützlich, wenn Sie integrierte Stile deaktiviert haben und sie wieder aktivieren möchten, oder wenn Sie Änderungen an integrierten Stilen zurücksetzen wollen.

## Tipps [tips]

- **Nach Häufigkeit ordnen**: Ziehen Sie Ihre meistgenutzten Stile nach oben, damit sie die einfachsten Tastaturkurzbefehle erhalten ({% kbd cmd 1 %}, {% kbd cmd 2 %} usw.).

- **Deaktivieren statt löschen**: Statt ungenutzte Stile zu löschen, deaktivieren Sie sie. Sie sind dann aus dem Weg, bleiben aber verfügbar, falls Sie sie später brauchen.

- **Zum Experimentieren duplizieren**: Duplizieren Sie einen Stil, bevor Sie größere Änderungen vornehmen, damit Sie jederzeit zum Original zurückkehren können.

- **Beim Bearbeiten in der Vorschau prüfen**: Lassen Sie den Stil-Manager beim Bearbeiten der CSS-Dateien geöffnet, um Ihre Änderungen in Echtzeit im Vorschaubereich zu sehen.

- **Stapel-Import**: Über die Hinzufügen-Schaltfläche können Sie mehrere CSS-Dateien auf einmal auswählen oder mehrere Dateien in einem Schritt hineinziehen.
