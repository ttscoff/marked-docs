# <%= @title %>

[Traverse][traverse] incluye el comando **Stream to Marked**. Aparece en el menú de exportación cuando Marked 2 o Marked 3 está instalado.

## Stream to Marked [stream-to-marked]

Abra el menú de exportación (el botón con una flecha hacia arriba) y elija **Stream to Marked**.

![Stream to Marked en el menú de exportación de Traverse][stream]

Lo que Traverse envía depende del esquema:

- Si ha añadido el atributo **Type**, Traverse envía el mismo Markdown que usa para la exportación Markdown.
- Si el esquema usa **[Fountain](Fountain_for_Screenwriters.html)**, Traverse envía ese texto para la vista previa.
- Si no hay ninguna de las dos opciones, Traverse envía una lista Markdown sencilla.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
