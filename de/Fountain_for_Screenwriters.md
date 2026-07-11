# <%= @title %>

[Fountain](http://fountain.io/) ist eine spezielle Textauszeichnungssprache, die zum Schreiben von Drehbüchern entwickelt wurde. Drehbuchautoren, die mit der Fountain-Syntax schreiben, können Marked verwenden, um eine Vorschau ihrer Arbeit anzuzeigen.

Wenn Sie eine Datei mit der Erweiterung „.fountain“ öffnen, wird automatisch die Fountain-Unterstützung für das Fenster aktiviert. Für die Vorschau und den Export wird ein standardmäßiges Fountain-Stylesheet angewendet.

Sie können die Verarbeitung jedes Dokuments als Fountain erzwingen, indem Sie das Zahnradmenü unten rechts im Vorschaufenster öffnen und **Als Fountain verarbeiten** auswählen.

Abschnitts- und Szenenüberschriften werden im Inhaltsverzeichnis angezeigt, um eine schnelle Navigation durch Ihr Drehbuch zu ermöglichen.

## Scrippets

Sie können auch „Scrippets“ in einem regulären Dokument verwenden, um einzelne Abschnitte mit Fountain bearbeiten und formatieren zu lassen. Umgeben Sie einfach Ihr Fountain-Markup im Hauptdokument mit `[scrippet]`-Tags:

[scrippet]
    Ihr Drehbuchtext...
    [/scrippet]

Sie können auch Standard-Tags im Marked-Stil verwenden:

<!--SCRIPPET-->
    Ihr Drehbuchtext...
    <!--/SCRIPPET-->
