# <%= @title %>

Der Style Manager bietet eine zentrale Schnittstelle zur Verwaltung aller Ihrer
integrierte und Custom-Stile. Es gibt Ihnen die vollständige Kontrolle darüber
Stile erscheinen in Menüs, in ihrer Reihenfolge, in Tastaturkürzeln und mehr.

## Öffnen des Style-Managers

Um den Stil-Manager zu öffnen, klicken Sie im {% prefspane Style %} auf die Schaltfläche **Stile verwalten…**
Bereich, oder verwenden Sie {% appmenu Stil, Stile verwalten (~@$m) %}. Sie können CSS-Dateien auch direkt in das Einstellungsfenster ziehen --- Marked
importiert sie, öffnet den Stil-Manager und wählt die neu hinzugefügte Zeile aus
Du.

![Style Manager][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## Die Stiltabelle

Der Stil-Manager zeigt alle Ihre Stile in einer sortierbaren Tabelle an, die gemischt ist
integrierte und benutzerdefinierte Stile nahtlos. Jede Zeile in der Tabelle enthält mehrere
Spalten:

### Kontrollkästchen aktiviert

Das Kontrollkästchen **Aktiviert** fügt den Stil sofort zum Stil hinzu oder entfernt ihn daraus
Menü, Standardstil-Popup und Tastaturkürzel. Wenn Sie einen Stil deaktivieren,
Es ist in den Menüs ausgeblendet, verbleibt aber zur einfachen erneuten Aktivierung im Stil-Manager.

Wenn Sie den aktuell aktiven Stil deaktivieren, wechselt Marked automatisch zum
Nächster verfügbarer aktivierter Stil.

### Namensspalte

In der Spalte **Name** wird der Anzeigename des Stils angezeigt. Sie können diesen Namen bearbeiten
inline, indem Sie direkt darauf klicken; Änderungen bleiben bestehen und werden auf jedes Menü übertragen
wo der Stil erscheint. Dies ist besonders nützlich für benutzerdefinierte Stile, bei denen Sie
Möglicherweise möchten Sie einen aussagekräftigeren Namen als den Dateinamen.

Integrierte Stile haben gesperrte Namen, die nicht bearbeitet werden können. Um eine anzupassen
Wenn Sie den Namen des integrierten Stils verwenden möchten, duplizieren Sie ihn zuerst, um eine bearbeitbare Kopie zu erstellen.

### Quellspalte

Die Spalte **Quelle** gibt an, woher der Stil stammt:

- **Integriert**: Stile, die mit Marked geliefert und in der Anwendung gespeichert werden
  Bündel
- **Custom**: Stile, die Sie aus CSS-Dateien auf Ihrem Laufwerk hinzugefügt haben
- **Dupliziert**: Stile, die durch Duplizieren eines anderen Stils (entweder integriert) erstellt wurden
  oder benutzerdefiniert)

### Spalte „Aktionen“.

Jede Zeile enthält einen Stapel **Aktionen** mit Schaltflächen zum Verwalten dieses Stils:

**Bearbeiten**: Öffnet die CSS-Datei in Ihrem Standardeditor. Integrierte Stile können nicht sein
direkt bearbeitet werden – Sie müssen sie zuerst duplizieren, um eine bearbeitbare Kopie zu erstellen.

**Duplizieren**: Erstellt eine Kopie des Stils und eine neue CSS-Datei auf der Festplatte. Die
Das Duplikat erscheint direkt unter dem ursprünglichen Stil in der Tabelle. Das ist
Die empfohlene Methode zum Anpassen integrierter Stile.

**Anzeigen**: Zeigt die CSS-Datei im Finder an, sodass Sie sie leichter finden können
Ihr Antrieb. Diese Schaltfläche ist nur für benutzerdefinierte Stile mit einem Dateipfad verfügbar.

**Löschen**: Entfernt den Stil aus Marked. Für benutzerdefinierte Stile erhalten Sie Angaben
die Option, entweder nur die Referenz zu entfernen (die CSS-Datei beizubehalten) oder zu verschieben
die CSS-Datei in den Papierkorb. Integrierte Stile können nicht gelöscht werden, sie können jedoch gelöscht werden
deaktiviert.

**Wiederherstellen**: Bei integrierten Stilen stellt diese Schaltfläche den Stil wieder her
Standardzustand, wenn er geändert wurde. Diese Schaltfläche ist nur sichtbar für
Integrierte Stile.

## Stile neu anordnen

Zeilen können per Drag & Drop neu angeordnet werden. Ziehen Sie einfach eine Stilzeile in eine neue
Platz in der Tabelle. Die Reihenfolge, die Sie hier festlegen, steuert:

- Die Menüreihenfolge „Stil“ in den Menüs von Marked
- Tastaturkürzelzuweisungen (`⌘1`–`⌘9` für die ersten neun aktivierten Stile,
  `⌥⌘1`–`⌥⌘0` für die nächsten zehn usw.)

Ziehen Sie Stile in die gewünschten Tastaturkürzel-Slots
besetzen.

## Stile hinzufügen

Es gibt mehrere Möglichkeiten, neue benutzerdefinierte Stile zum Stil-Manager hinzuzufügen:

### Schaltfläche „Hinzufügen“.

Klicken Sie auf die Schaltfläche **Neuen Stil hinzufügen**, um eine Dateiauswahl zu öffnen
Hier können Sie eine oder mehrere CSS-Dateien zum Importieren auswählen. Ausgewählte Dateien werden angezeigt
Zum Stil-Manager hinzugefügt und standardmäßig aktiviert.

### Drag-and-Drop

Sie können CSS-Dateien direkt in das Style-Manager-Fenster ziehen. Beim Ziehen
Dateien über dem Fenster, erscheint ein Overlay mit der Meldung „Füge einen Custom-Stil hinzu“ (oder
„N Custom Stile hinzufügen“ für mehrere Dateien). Legen Sie die Dateien ab, um sie zu importieren.

Sie können CSS-Dateien auch an bestimmte Positionen in der Tabelle ziehen – den Drop
Der Indikator zeigt an, wo der neue Stil eingefügt wird, sodass Sie steuern können
Sowohl Import als auch Positionierung in einer Aktion.

Das Ziehen von CSS-Dateien in den Einstellungsbereich {% prefspane Style %} funktioniert ebenfalls
Importieren Sie sie und öffnen Sie den Style Manager automatisch.

## Live-Vorschau

Im rechten Bereich des Stil-Managers wird eine Live-Vorschau der ausgewählten Elemente angezeigt
Stil. Die Vorschau zeigt ein umfassendes Beispieldokument mit Überschriften,
Listen, Tabellen, Codeblöcke, Blockzitate und andere allgemeine Markdown-Elemente,
alles mit dem tatsächlichen CSS des ausgewählten Stils gestaltet.

Die Vorschau verwendet die CSS-Datei direkt von der Festplatte, also alle Änderungen, die Sie in Ihrer vornehmen
Der externe Editor wird in der Vorschau sofort aktualisiert. Das macht es einfach
Sehen Sie Ihre Änderungen in Echtzeit, während Sie benutzerdefinierte Stile entwickeln.

### Vorschau im Dunkelmodus

Über ein Kontrollkästchen über der Vorschau können Sie zwischen Hell- und Dunkelmodus wechseln
Vorschauen. Dies ist nützlich, um zu testen, wie Stile in beiden Darstellungsmodi aussehen.
insbesondere, wenn Sie Stile erstellen, die sich an das Erscheinungsbild des Systems anpassen.

## Tastaturkürzel

Der Stil-Manager zeigt unterhalb der Tabelle eine Legende an, die zeigt, wie die Tastatur funktioniert
Verknüpfungen werden zugewiesen. Die ersten neun aktivierten Stile erhalten {% kbd cmd 1 %} durch
{% kbd cmd 9 %} ({% kbd cmd 0 %} ist reserviert), die nächsten zehn erhalten {% kbd opt cmd 1 %} bis {% kbd opt cmd 0 %} und so weiter. Sie können die zugewiesenen Tastaturkürzel in jeder Vorschau im Popup-Menü „Stil“ sehen.

## Deaktivierte Stile filtern

Über ein Kontrollkästchen am unteren Rand des Fensters können Sie deaktivierte Elemente ein- oder ausblenden
Stile. Wenn diese Option deaktiviert ist, werden nur aktivierte Stile angezeigt, was die Arbeit erleichtert
Konzentrieren Sie sich auf Ihre aktiven Stile und ordnen Sie sie neu. Wenn diese Option aktiviert ist, werden alle Stile (aktiviert und deaktiviert) angezeigt.
werden angezeigt, sodass Sie Ihre komplette Stilkollektion verwalten können.

## Integrierte Stile wiederherstellen

Die Schaltfläche **Alle integrierten Stile wiederherstellen** unten im Fenster
Stellt alle integrierten Stile auf ihren Standardzustand zurück. Dies ist nützlich, wenn Sie dies getan haben
Sie haben integrierte Stile deaktiviert und möchten sie erneut aktivieren oder zurücksetzen
alle an integrierten Stilen vorgenommenen Änderungen.

## Tipps

- **Nach Häufigkeit organisieren**: Ziehen Sie Ihre am häufigsten verwendeten Stile zum Verschenken nach oben
  ihnen die einfachsten Tastaturkürzel ({% kbd cmd 1 %}, {% kbd cmd 2 %} usw.)

- **Deaktivieren statt löschen**: Anstatt Stile zu löschen, die Sie nicht verwenden,
  deaktivieren Sie sie. Sie bleiben Ihnen aus dem Weg, bleiben aber bei Bedarf verfügbar
  sie später.

- **Duplikat zum Experimentieren verwenden**: Duplizieren Sie einen Stil, bevor Sie ihn zum Hauptstil machen
  Änderungen, sodass Sie jederzeit zum Original zurückkehren können.

- **Vorschau während der Bearbeitung**: Lassen Sie den Stil-Manager während der Bearbeitung von CSS geöffnet
  Dateien, um die Aktualisierung Ihrer Änderungen in Echtzeit im Vorschaufenster zu sehen.

- **Batch-Import**: Sie können mehrere CSS-Dateien gleichzeitig auswählen, wenn Sie den verwenden
  Klicken Sie auf die Schaltfläche „Hinzufügen“ oder ziehen Sie mehrere Dateien, um sie alle in einer Aktion zu importieren.


