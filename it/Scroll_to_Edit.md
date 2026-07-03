<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La funzione "scorri per modificare" di Marked tiene traccia delle differenze tra l'ultimo aggiornamento e l'ultimo, cercando di trovare il punto in cui hai apportato le modifiche più recenti. Marked ne tiene sempre traccia e nell'anteprima viene visualizzata una piccola linea rossa per mostrare la posizione della prima modifica rilevata. Nel pannello delle preferenze Comportamento, puoi attivare "Scorri fino alla prima modifica" e quando un'anteprima si aggiorna farà scorrere delicatamente la vista fino a quella posizione.

Con "Scorri fino alla prima modifica" disattivato, puoi comunque premere il tasto "e" in qualsiasi momento nell'anteprima per andare all'ultimo punto di modifica memorizzato.


### Note su "Scorri per modificare"

Questa è una funzionalità fantastica quando funziona, ma ci sono molte complicazioni. Soprattutto le prime volte che il documento viene aggiornato, potrebbero verificarsi dei movimenti a scatti nello scorrimento. Se le tue modifiche sono tutte all'interno di un elemento molto grande (un paragrafo eccessivamente lungo, per esempio), potrà solo avvicinarsi al marcatore. Allo stesso modo, se aggiungi una o due parole alla fine del documento, l'indicatore di modifica verrà posizionato nell'elemento sopra finché non ci sarà abbastanza contenuto da ancorare nel nuovo elemento.