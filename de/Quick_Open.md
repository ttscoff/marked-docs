# <%= @title %>

Schnell öffnen bietet raschen Zugriff auf Ihre geöffneten Dokumente und zuletzt verwendeten Dateien.

## Schnell öffnen aufrufen

Rufen Sie das Schnell-öffnen-Panel mit {% kbd shift cmd O %} oder über das Menü {% appmenu Ablage, Schnell öffnen %} auf. Das Panel erscheint als schwebendes Fenster über Ihrem aktuellen Dokument und lässt Sie schnell zwischen geöffneten Dokumenten wechseln oder zuletzt verwendete Dateien öffnen.

![Schnell-öffnen-Panel][qo]

[qo]: images/quick-open-800.jpg @2x width=800

## Dokumentabschnitte

Das Schnell-öffnen-Panel gliedert Dokumente in übersichtliche Abschnitte:

### Geöffnete Dokumente

Oben in der Liste sehen Sie alle aktuell geöffneten Dokumente. Sie sind nach ihrem Fenster gruppiert:

- **Fenster mit Tabs**: Dokumente in Fenstern mit Tabs zeigen als Untertitel „Fenster mit X Tabs“ und geben so an, wie viele Tabs zur Fenstergruppe gehören
- **Eigenständige Fenster**: Dokumente in einzelnen Fenstern zeigen „Fenster“ als Untertitel

Für jedes geöffnete Dokument werden angezeigt:
- der Dateiname des Dokuments als Haupttitel
- die Angabe zur Fenstergruppierung als Untertitel
- ein Dokumentsymbol

### Zuletzt geöffnete Dokumente

Unterhalb der geöffneten Dokumente trennt der Abschnittstitel „Zuletzt geöffnete Dokumente“ die Liste. Dieser Abschnitt zeigt bis zu 10 Ihrer zuletzt geöffneten Dateien, die aktuell nicht geöffnet sind. Für jedes dieser Dokumente werden angezeigt:

- der Dateiname des Dokuments als Haupttitel
- „Zuletzt geöffnet“ als Untertitel
- ein Dokumentsymbol

### Anderes öffnen

Unten in der Liste können Sie mit der Option „Anderes öffnen…“ die Standard-Dateiauswahl von macOS öffnen, um eine beliebige Datei auszuwählen. Diese Option zeigt:

- „Anderes öffnen…“ als Haupttitel
- „Datei oder Ordner öffnen“ als Untertitel
- ein Ordnersymbol

## Suchen und filtern

Tippen Sie oben im Panel in das Suchfeld, um die Liste in Echtzeit zu filtern. Durchsucht werden:

- die Dateinamen der Dokumente
- die vollständigen Dateipfade

Während Sie tippen, aktualisiert sich die Liste sofort und zeigt nur passende Dokumente. Die Option „Anderes öffnen…“ bleibt in den gefilterten Ergebnissen immer unten sichtbar.

## Tastaturnavigation

Das Schnell-öffnen-Panel lässt sich vollständig per Tastatur steuern:

- **Pfeiltasten ↑/↓**: in der Liste nach oben und unten bewegen
- **Eingabetaste**: das ausgewählte Dokument bzw. die ausgewählte Option öffnen
- **Escape**: das Schnell-öffnen-Panel schließen
- **Befehlstaste (⌘)**: gedrückt halten, um Dateipfade einzublenden (siehe unten)

## Dateipfade anzeigen

Halten Sie die **Befehlstaste (⌘)** gedrückt, während das Schnell-öffnen-Panel geöffnet ist, um im Untertitelbereich den vollständigen Dateipfad jedes Dokuments zu sehen. Pfade in Ihrem Home-Ordner werden mit der Abkürzung `~` dargestellt (z. B. `~/Documents/file.md`). Lassen Sie die Befehlstaste los, um zur normalen Ansicht mit Fenstergruppierung oder „Zuletzt geöffnet“-Angabe zurückzukehren.

Das ist besonders nützlich, wenn Sie mehrere Dateien mit demselben Namen geöffnet haben oder den genauen Speicherort eines Dokuments prüfen müssen.

## Dokumente öffnen

- **Geöffnete Dokumente**: Wählen Sie ein geöffnetes Dokument aus, wird dessen Fenster in den Vordergrund geholt und – falls es in einem Fenster mit Tabs liegt – zum Tab dieses Dokuments gewechselt
- **Zuletzt geöffnete Dokumente**: Wählen Sie ein zuletzt geöffnetes Dokument aus, wird es in einem neuen Fenster geöffnet oder als Tab hinzugefügt (abhängig von Ihrer Einstellung „Dokumente in Tabs öffnen“ unter {% prefspane General %})
- **Anderes öffnen…**: Diese Option öffnet den Standard-Dateiauswahldialog von macOS
