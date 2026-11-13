# <%= @title %>

[Traverse][traverse] include il comando **Stream to Marked**. Compare nel menu di esportazione quando è installato Marked 2 o Marked 3.

## Stream to Marked [stream-to-marked]

Apri il menu di esportazione (il pulsante con la freccia verso l'alto) e scegli **Stream to Marked**.

![Stream to Marked nel menu di esportazione di Traverse][stream]

Ciò che Traverse invia dipende dalla struttura:

- Se hai aggiunto l'attributo **Type**, Traverse invia lo stesso Markdown usato per l'esportazione Markdown.
- Se il formato in Traverse è impostato su **[Fountain](Fountain_for_Screenwriters.html)**, l'anteprima attiva automaticamente il trattamento Fountain. Traverse fa iniziare il testo inviato con `<!--format:fountain-->`, ed è questo commento che attiva il trattamento. Vedi [Streaming Preview](Streaming_Preview.html).
- Se non è selezionato nessuno dei due, Traverse invia un semplice elenco Markdown.

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
