# <%= @title %>

[Curio][curio] ist eine visuelle Brainstorming- und Notizen-App, die das gerade bearbeitete Element in den **Streaming-Vorschau**-Kanal von Marked streamen kann.

## Auswahl zu Marked streamen

1. Wählen Sie in Marked {% appmenu Ablage, Neu, Streaming-Vorschau %} aus, damit ein Streaming-Vorschaufenster bereit ist.
2. Aktivieren Sie in Curio **View → Stream Selected to Marked**.

Wenn Sie in Curio doppelklicken, um eine Abbildung, Notiz, Liste oder ein anderes Element zu bearbeiten, wird deren Markdown in die Streaming-Vorschau übertragen und beim Schreiben aktualisiert.

Marked wird nahezu in Echtzeit aktualisiert und folgt derselben `mkStreamingPreview`-Zwischenablage-Schnittstelle wie andere integrierte Apps – siehe [Technische Details](Streaming_Preview.html#developers) unter [Streaming-Vorschau](Streaming_Preview.html).

Wenn die Vorschau nicht mehr aktualisiert wird, vergewissern Sie sich, dass in Marked ein Streaming-Vorschaufenster geöffnet ist, und schalten Sie in Curio einmal **Stream Selected auf Marked** um.

[curio]: https://www.zengobi.com/products/curio/
