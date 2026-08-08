<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

[MarsEdit] [me] memorizza i post all'interno del suo database, non come file sciolti sul disco. Marked utilizza quindi un flusso di lavoro di anteprima dedicato che comunica con l'applicazione MarsEdit in esecuzione.

## Finestra di anteprima di MarsEdit [marsedit-preview-window]

Scegli {% appmenu File, New, MarsEdit Preview %}. Marked chiede ad AppleScript di leggere il **post in primo piano in MarsEdit** (gli ID bundle di Red Sweater per direct, Mac App Store, Setapp e MarsEdit 4/5 vengono riconosciuti). Mantieni MarsEdit in esecuzione con un documento aperto mentre lavori.

- **Aggiornamento manuale:** salva dall'anteprima di Marked se desideri forzare un aggiornamento.
- **Aggiornamenti automatici:** abilita la visione in modo che ogni salvataggio automatico di MarsEdit si aggiorni Contrassegnato.

Se non è disponibile alcun post, Marked mostra un breve errore nell'anteprima invece del testo non aggiornato.

### Post estesi [extended-posts]

Il contenuto nel campo **esteso** di MarsEdit è separato nell'anteprima e nel sorgente di Marked utilizzando un divisore `<!--more-->` in stile WordPress in modo che i siti orientati all'impaginazione (WordPress, Jekyll, ecc.) vedano ancora l'interruzione. Il commento è innocuo altrove.

### Tag e categorie nei metadati [tags-and-categories-in-metadata]

I tag e le categorie di MarsEdit sono esposti al blocco di metadati MultiMarkdown. Con il processore MultiMarkdown ({% prefspane Processor %}), puoi fare riferimento a loro come:

    Contrassegnato: [%tags]
    Inserito in: [%categorie]

[me]: https://www.red-sweater.com/marsedit/