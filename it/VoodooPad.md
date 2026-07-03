<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[VoodooPad][vp] raggruppa ogni pagina in un singolo file di database. Trascina `.vpdoc` su Contrassegnato per visualizzare in anteprima la pagina attualmente in primo piano in VoodooPad; usa {% kbd cmd S %} in VoodooPad ogni volta che hai bisogno di Marked per ricaricare dal disco.

Marked guarda il documento su disco e scambia l'anteprima quando cambi pagina all'interno di VoodooPad.

## Immagini incorporate

Quando fai riferimento a immagini con Markdown o HTML e il file binario risiede **all'interno** del database VoodooPad, Marked può estrarlo per l'anteprima. Le immagini che sono solo **alias** (file trascinati per riferimento) non vengono archiviate nel pacchetto: puntano a quelle con percorsi assoluti o percorsi relativi a `.vpdoc` sul disco in modo che Marked possa risolverle.

[vp]: https://www.voodoopad.com/