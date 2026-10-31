# <%= @title %>

A [Traverse][traverse] tartalmazza a **Stream to Marked** parancsot. Az exportmenüben jelenik meg, ha a Marked 2 vagy a Marked 3 telepítve van.

## Stream to Marked [stream-to-marked]

Nyissa meg az exportmenüt (a felfelé mutató nyilas gombot), és válassza a **Stream to Marked** lehetőséget.

![Stream to Marked a Traverse exportmenüjében][stream]

A Traverse attól függően küld tartalmat, hogy milyen a vázlat:

- Ha hozzáadta a **Type** attribútumot, a Traverse ugyanazt a Markdownt küldi, amelyet a Markdown-exporthoz használ.
- Ha a vázlat **[Fountain](Fountain_for_Screenwriters.html)** formátumú, a Traverse ezt a szöveget küldi előnézetre.
- Ha egyik sincs kiválasztva, a Traverse egy egyszerű Markdown-listát küld.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
