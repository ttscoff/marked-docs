# <%= @title %>

Optionen unter {% prefspane Preview %}:

![Einstellungen: Vorschau][1]

[1]: images/screenshots/preferences-Preview.jpg @2x width=714px height=1031px class=preferencepane-scroll

### Vorschauverhalten [preview-behavior]

Navigation für die Mini-Übersicht aktivieren
: Erzeugt eine visuelle Übersicht des Dokuments, die beim Drücken von „0“ erscheint. Bei großen Dokumenten kann das Rendern kurz verzögert sein.

Überschriften klappen Abschnitte ein
: Ein Klick auf ein Überschriftenelement klappt den Abschnitt zwischen ihm und der nächsten Überschrift ein.

{% kbd cmd %}&#8209;Klick erforderlich
: Ist dies aktiviert, klappen Überschriften nur ein oder aus, wenn Sie bei gedrückter Befehlstaste darauf klicken.

Vorschau- und Quelltext-Scrollen synchronisieren
: Sofern Ihr Editor das unterstützt, hält Marked die Vorschau an der entsprechenden Stelle im Quelldokument.

Geschwindigkeitsablesung mit Scrollposition synchronisieren
: Hält das [Speed Reading](Speed_Reading.html)-Overlay an der Scrollposition der Vorschau ausgerichtet. Das lässt sich auch über das Speed-Read-Overlay umschalten.

### Zum Bearbeiten scrollen [scroll-to-edit]

Zum Bearbeiten scrollen
: Beim Aktualisieren der Vorschau kann Marked die erste Stelle bestimmen, an der sich das Dokument geändert hat, und automatisch dorthin scrollen. So bleibt die Vorschau mit Ihrer aktuellen Position im bearbeiteten Dokument synchron. Die Markierung der letzten Bearbeitung ist der erste Unterschied im Dokument seit der letzten Aktualisierung. Aktivieren Sie „Diff-Reihenfolge umkehren“, gilt stattdessen der letzte Unterschied im Dokument (von oben nach unten) als letzte Bearbeitung.

Markierung für die letzte Bearbeitung anzeigen
: An der Stelle der ersten erkannten Bearbeitung erscheint eine kleine rote Markierung. Schalten Sie sie aus, um sie unsichtbar zu machen. (Erfordert **Zum Bearbeiten scrollen**.)

Alle Diff-Marker anzeigen
: Ist dies aktiviert, werden alle Unterschiede zwischen der letzten Aktualisierung und dem aktuellen Inhalt am Rand hervorgehoben. Sie können mit <kbd>e</kbd> (vorwärts) und {% kbd shift E %} (rückwärts) durch die Änderungen navigieren; sie werden dabei in die Mitte der Ansicht gescrollt.

Diff-Reihenfolge umkehren
: Ist dies aktiviert, werden Unterschiede in umgekehrter Reihenfolge (von unten nach oben) markiert. Das betrifft die Navigation: <kbd>e</kbd> navigiert nach oben, {% kbd shift E %} nach unten. Die „letzte Bearbeitung“ wird zum letzten Unterschied im Dokument.

### Zusätzliche Funktionen [additional-features]

Das Inhaltsverzeichnis verfolgt die Scrollposition
: Das Inhaltsverzeichnis hebt den aktuellen Abschnitt hervor.

Popup-Statistiken zur Textauswahl
: Zeigt bei jeder Auswahl ein Popup mit der Wortanzahl für den ausgewählten Text an.

Link-Popover aktivieren
: Zeigt ein Popup-Menü, wenn externe Links angeklickt und vor dem Loslassen gehalten werden.

URLs bei Aktualisierung automatisch validieren
: Validiert URLs beim Laden und Aktualisieren des Dokuments. Zeigt nur bei Fehlern Ergebnisse an.
: Führt bei jeder Dokumentaktualisierung die [Link-Validierung](Link_Validation.html) aus (bei sehr vielen Links kann das langsam sein und sollte vermieden werden).

### Wiki-Verlinkung [wiki-linking]

[[Wiki-Links]] konvertieren
: Aktiviert Markeds [Wiki-Navigation](Wiki_Navigation.html) für die `[[wiki link]]`-Syntax.

Standarderweiterung
: Die Dateinamenserweiterung, die Marked beim Auflösen von Wiki-Links ohne Erweiterung verwendet (zum Beispiel `md`).

### Aussehen [appearance]

Dunkelmodus
: Zeigt alle Fenster im Modus „Hoher Kontrast“ – mit dunkler Oberfläche und, falls vorhanden, der invertierten Version des aktuellen Stils (gilt möglicherweise nicht für Eigene Stile).

Systemeinstellung anpassen
: Schaltet den Dunkelmodus automatisch um, wenn der macOS-Dunkelmodus systemweit ein- oder ausgeschaltet wird.

Vollständigen Pfad im Fenstertitel anzeigen
: Ist dies aktiviert, zeigt Marked den vollständigen Pfad zum aktuellen Dokument im Fenstertitel an.
