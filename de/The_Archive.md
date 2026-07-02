# <%= @title %>

[The Archive][archive] verwaltet Ihre Notizen als Dateien auf der Festplatte und kann die von Ihnen bearbeitete Notiz direkt in den **Streaming-Vorschau**-Kanal von Marked spiegeln.

## Streaming-Vorschau zu Marked

1. Öffnen Sie in Marked {% appmenu File, New, Streaming Preview %} (oder verwenden Sie ein vorhandenes Streaming-Vorschaufenster erneut).
2. Wechseln Sie zu „The Archive“ und wählen Sie **Note → Stream Preview to Marked**, sodass „The Archive“ Marked aktiviert und mit dem Senden des vordersten Notiztexts beginnt.

Marked wird aktualisiert, während Sie in The Archive tippen, und folgt demselben `mkStreamingPreview`-Zwischenablagevertrag wie andere integrierte Apps – siehe [Technical details](Streaming_Preview.html#developers) unter [Streaming Preview](Streaming_Preview.html).

Wenn die Vorschau veraltet erscheint, vergewissern Sie sich, dass sich das Streaming-Fenster in Marked noch immer im Vordergrund befindet, und schalten Sie den Menübefehl in The Archive einmal aus und wieder ein.

[archive]: https://www.zettelkasten.de/the-archive/
