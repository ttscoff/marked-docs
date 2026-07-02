# <%= @title %>

[MarsEdit][me] speichert Beiträge in seiner Datenbank und nicht als lose Dateien auf der Festplatte. Marked verwendet daher einen dedizierten Vorschau-Workflow, der mit der laufenden MarsEdit-Anwendung kommuniziert.

## MarsEdit-Vorschaufenster

Wählen Sie {% appmenu File, New, MarsEdit Preview %}. Marked verwendet AppleScript, um den **vordersten Beitrag in MarsEdit** zu lesen (die Bundle-IDs von Red Sweater für Direkt-Download, Mac App Store, Setapp und MarsEdit 4/5 werden erkannt). Lassen Sie MarsEdit während der Arbeit mit geöffnetem Dokument laufen.

- **Manuelle Aktualisierung:** Speichern Sie aus der Vorschau von Marked, wenn Sie eine Aktualisierung erzwingen möchten.
- **Automatische Updates:** Aktivieren Sie die Wiedergabe, damit jede automatische Speicherung von MarsEdit Marked aktualisiert wird.

Wenn kein Beitrag verfügbar ist, zeigt Marked in der Vorschau einen kurzen Fehler anstelle von veraltetem Text an.

### Erweiterte Beiträge

Der Inhalt im **erweiterten** Feld von MarsEdit wird in der Vorschau und Quelle von Marked mithilfe eines `<!--more-->`-Trenners im WordPress-Stil getrennt, sodass auf seitenbezogenen Websites (WordPress, Jekyll usw.) die Unterbrechung weiterhin angezeigt wird. An anderer Stelle ist der Kommentar harmlos.

### Tags und Kategorien in Metadaten

Die Tags und Kategorien von MarsEdit werden im MultiMarkdown-Metadatenblock verfügbar gemacht. Mit dem MultiMarkdown-Prozessor ({% prefspane Processor %}) können Sie sie wie folgt referenzieren:

Tagged: [%tags]
    Posted in: [%categories]

[me]: https://www.red-sweater.com/marsedit/
