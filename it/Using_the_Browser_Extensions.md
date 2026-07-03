<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked include estensioni del browser che ti consentono di inviare URL di pagine o contenuti selezionati direttamente in Marked 3.

## Installa

Scarica e installa da [https://markedapp.com/extensions](https://markedapp.com/extensions):

-Firefox/Zen
- Cromato/Coraggioso/Bordo
- Safari (in bundle)

## Come funziona l'estensione

Quando fai clic su un pulsante di estensione, si apre un URL personalizzato gestito da Marked 3 utilizzando lo schema `x-marked-3://markdownify`.

### `Markdownify URL`

Nel popup dell'estensione, fai clic su **`Markdownify URL`** per inviare l'URL della pagina corrente a Marked.

### `Markdownify Selection`

Nel popup dell'estensione, fai clic su **`Markdownify Selection`** quando hai una selezione nella pagina.

Marked riceve l'HTML per la selezione corrente e lo converte in Markdown.

### Seleziona sezione (modalità di selezione del blocco)

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Fare clic su **Seleziona sezione** per accedere alla "modalità di selezione della sezione":

- Passa il mouse sopra la pagina per evidenziare gli elementi del blocco che puoi selezionare.
- Fare clic su un blocco per inviarlo immediatamente a Marked (invio singolo).
- Cmd-clic sui blocchi per selezionare più blocchi (Cmd-clic di nuovo per rimuovere un blocco).
- Premi Invio per inviare i blocchi attualmente selezionati.
- Premere Esc per annullare la modalità di selezione della sezione.

Durante la selezione, il popup fornisce anche controlli di zoom per aiutarti a fare clic su sezioni piccole o dense:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` rimpicciolisce
- **Adatta altezza** esegue lo zoom in modo che la pagina si adatti all'altezza del viewport
- `+` ingrandisce