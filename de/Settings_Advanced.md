# <%= @title %>

Optionen unter {% prefspane Advanced %}:

![Einstellungen: Erweitert][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

YAML- und Pandoc-Metadaten
: - **Ignorieren:** Lässt sie genau so, wie sie im Dokument stehen – nützlich, wenn Ihr Prozessor oder Präprozessor das YAML tatsächlich verwendet.
: - **Vor dem Rendern entfernen**: Der YAML-Block wird entfernt.
: - **Als MMD-Metadaten behandeln:** Wandelt den YAML- oder Pandoc-Metadatenblock in das MultiMarkdown-Format um.

MultiMarkdown-Metadaten-Header entfernen
: Ist dies aktiviert, werden MultiMarkdown-Metadaten am Anfang des Dokuments vor dem Rendern entfernt.
: Das kann nützlich sein, wenn Sie einen Nicht-MultiMarkdown-Prozessor verwenden, der die Metadaten sonst im gerenderten Dokument anzeigen würde. Die Metadaten werden vor dem Entfernen weiterhin gelesen, sodass Marked-spezifische Syntax weiterhin erkannt wird.

Gehostete Bilder zwischenspeichern
: Marked speichert Bilder in der Vorschau standardmäßig nicht zwischen, weil es sie auf Änderungen überwacht und sofort aktualisiert. Wenn Sie über eine Web-URL referenzierte Bilder verwenden, können Sie das Zwischenspeichern dieser Bilder aktivieren, um das Rendern bei langsamen Verbindungen zu beschleunigen.

Lesbarkeitsstatistik analysieren
: Wenn Sie keine [Statistiken](Document_Statistics.html) berechnen lassen möchten, deaktiviert dies diese Verarbeitung. Bei sehr großen Dokumenten kann das die Leistung verbessern. Zeichen-, Wort- und Satzzählung funktionieren weiterhin.

Systemweite Suche-Zwischenablage verwenden
: Mit dieser Option übernimmt Marked den zuletzt in einem anderen Editor verwendeten Suchbegriff, und alles, was in Marked gesucht wird, wird auch in anderen Anwendungen zum Suchbegriff. Ist sie deaktiviert, sucht Marked unabhängig.

{% kbd cmd E %} für „Mit Auswahl suchen“ verwenden
: Standardmäßig öffnet {% kbd cmd E %} den Standardeditor. Ist diese Option aktiviert, funktioniert {% kbd cmd E %} wie in den meisten Textbearbeitungsprogrammen und verwendet den ausgewählten Text für die Suche; „Im Editor öffnen“ lässt sich dann mit {% kbd opt cmd E %} auslösen.

Debug-Modus
: Aktiviert die Debug-Protokollierung. Nutzen Sie sie zur eigenen Fehlersuche und beim Melden eines Problems. Wählen Sie __Hilfe → Debug-Protokoll öffnen__, um die Aktivität anzuzeigen.
: Die Einstellung _Alle_ zeigt Infomeldungen, Warnungen und Fehlermeldungen. Sie können sie auch so einstellen, dass nur Fehler oder Fehler und Warnungen angezeigt werden.

Einstellungen sichern
: Sie können Ihre Einstellungen in einer JSON-Datei sichern, mit der sich die Einstellungen wiederherstellen oder auf einen neuen Rechner übertragen lassen.
