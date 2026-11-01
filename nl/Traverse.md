# <%= @title %>

[Traverse][traverse] bevat de opdracht **Stream to Marked**. Die verschijnt in het exportmenu wanneer Marked 2 of Marked 3 is geïnstalleerd.

## Stream to Marked [stream-to-marked]

Open het exportmenu (de knop met een pijl omhoog) en kies **Stream to Marked**.

![Stream to Marked in het exportmenu van Traverse][stream]

Wat Traverse stuurt, hangt van het overzicht af:

- Hebt u het kenmerk **Type** toegevoegd, dan stuurt Traverse dezelfde Markdown als bij Markdown-export.
- Als het formaat in Traverse op **[Fountain](Fountain_for_Screenwriters.html)** staat, schakelt het voorbeeld de Fountain-behandeling automatisch in. Traverse zet `<!--format:fountain-->` voor de verzonden tekst, en die opmerking zet de behandeling aan. Zie [Streaming Preview](Streaming_Preview.html).
- Is geen van beide gekozen, dan stuurt Traverse een eenvoudige Markdown-lijst.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
