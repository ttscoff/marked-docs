<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Curio][curio] è un'app visiva per brainstorming e per prendere appunti che può trasmettere in streaming l'elemento che stai modificando nel canale **anteprima in streaming** di Marked.

## Stream selezionato per contrassegnato [stream-selected-to-marked]

1. In Contrassegnato, scegli {% appmenu File, New, Streaming Preview %} in modo che sia pronta una finestra di anteprima dello streaming.
2. In Curio, attiva **Visualizza → Stream selezionato per contrassegnato**.

Quando fai doppio clic per modificare una figura, una nota, un elenco o un altro elemento in Curio, il relativo Markdown passa all'anteprima in streaming e si aggiorna mentre scrivi.

Aggiornamenti contrassegnati quasi in tempo reale, seguendo lo stesso contratto degli appunti `mkStreamingPreview` delle altre app integrate: vedi [Dettagli tecnici](Streaming_Preview.html#developers) in [Anteprima streaming](Streaming_Preview.html).

Se le anteprime smettono di aggiornarsi, conferma che una finestra di anteprima dello streaming sia aperta in Contrassegnato e attiva **Stream selezionato in Contrassegnato** una volta in Curio.

[curio]: https://www.zengobi.com/products/curio/