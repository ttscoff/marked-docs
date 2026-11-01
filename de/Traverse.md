# <%= @title %>

[Traverse][traverse] enthält den Befehl **Stream to Marked**. Er erscheint im Exportmenü, wenn Marked 2 oder Marked 3 installiert ist.

## Stream to Marked [stream-to-marked]

Öffnen Sie das Exportmenü (die Taste mit dem Pfeil nach oben) und wählen Sie **Stream to Marked**.

![Stream to Marked im Exportmenü von Traverse][stream]

Was Traverse sendet, hängt von der Gliederung ab:

- Haben Sie das Attribut **Type** hinzugefügt, sendet Traverse dasselbe Markdown wie beim Markdown-Export.
- Wenn das Format in Traverse auf **[Fountain](Fountain_for_Screenwriters.html)** gestellt ist, aktiviert die Vorschau die Fountain-Verarbeitung automatisch. Traverse stellt dem gestreamten Text `<!--format:fountain-->` voran, und dieser Kommentar schaltet die Verarbeitung ein. Siehe [Streaming-Vorschau](Streaming_Preview.html).
- Ist keines von beiden gewählt, sendet Traverse eine einfache Markdown-Liste.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
