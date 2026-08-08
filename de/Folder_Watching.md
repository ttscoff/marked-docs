# <%= @title %>

Legen Sie einen **Ordner** mit Klartextnotizen auf Marked ab. Marked öffnet ein Vorschaufenster, das immer die **zuletzt bearbeitete** geeignete Datei in diesem Ordner verfolgt (.md, .txt, .markdown usw., entsprechend den Dateitypfiltern von Marked).

Aktualisierungen erfolgen immer dann, wenn eine überwachte Datei gespeichert wird: Wenn die neueste Datei dieselbe wie zuvor ist, scrollt Marked in Richtung des erkannten Bearbeitungsbereichs. Wenn Sie zwischen Dokumenten wechseln, wechselt die gesamte Vorschau zur aktiven Datei.

## Funktioniert gut mit nvUltra, nvALT und ähnlichen Tools [works-well-with-nvultra-nvalt-and-similar-tools]

Notebook-Apps, die einzelne Dateien auf der Festplatte belassen (klassische Bibliotheken im **nvALT**-, **nvUltra**-, **Notational Velocity**-Stil, synchronisierte Git-Ordner, Dropbox-Scratch-Ordner usw.) lassen sich auf natürliche Weise mit der Ordnerüberwachung kombinieren – Sie schreiben in ein Fenster und lassen Marked daneben angeheftet, ohne die Vorschau manuell erneut zu öffnen.

**nvUltra** bietet in seinem Kontextmenü außerdem **[Preview File(s) in Marked](nvUltra.html)** an, wenn Sie bestimmte Notizen direkt in Marked öffnen möchten, statt Marked an den oben beschriebenen Überwachungsablauf für den gesamten Ordner zu koppeln.

Marked verwendet dasselbe Überwachungsverhalten auch unter anderen Menünamen, wenn Sie viele kleine Kapitel zu einem Leseerlebnis zusammenfassen. Siehe auch [Mehrteilige Dokumente](Multi-File_Documents.html) für Manuskripte, die bewusst mehrere Markdown-Quellen zusammenführen.
