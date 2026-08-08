<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Bozze] [bozze] su Mac può eseguire il mirroring della bozza attiva in Contrassegnato utilizzando l'**Anteprima streaming contrassegnato**, lo stesso canale basato sugli appunti descritto in [Anteprima streaming](Streaming_Preview.html). Puoi anche inviare la bozza corrente una volta con un'**azione** della community (nessun aggiornamento in tempo reale finché non la esegui di nuovo).

## Anteprima in streaming (Bozze per Mac) [streaming-preview-drafts-for-mac]

1. In Contrassegnato, scegli {% appmenu File, New, Streaming Preview %} in modo che sia pronta una finestra di anteprima dello streaming.
2. In **Bozze per Mac**, apri **Impostazioni** e attiva **Abilita supporto anteprima streaming app contrassegnate**.
3. Utilizza **Apri contrassegnato** se Drafts lo offre per portare avanti Marked, quindi modifica in Drafts; l'anteprima si aggiorna man mano che la bozza cambia.

![][bozzepref]

Quando questa opzione è attiva, Drafts spinge Markdown su Marked tramite l'integrazione che Marked espone per le anteprime in streaming (invece di fare affidamento sulla visione di un file su disco).

### Fatti segnare [get-marked]

Se nel foglio delle impostazioni di Drafts viene visualizzato **Get Marked App**, utilizzalo quando Marked non è ancora installato.

## Anteprima nell'azione contrassegnata (aggiornamento manuale) [preview-in-marked-action-manual-refresh]

Installa l'azione della community [**Anteprima in contrassegnato**](https://actions.getdrafts.com/a/11f) dalla directory delle bozze. Invia la **bozza di testo corrente** a Marked utilizzando un URL `x-marked://preview?text=…` (Drafts sostituisce i contenuti della bozza). **I contenuti non vengono aggiornati in tempo reale**: esegui nuovamente l'azione ogni volta che desideri che Marked corrisponda alla bozza.

Questo approccio è utile per controlli occasionali mentre l'**anteprima in streaming** è adatta a sessioni di scrittura continue.

Drafts funziona anche su iPhone e iPad; L'integrazione dell'anteprima in streaming qui documentata si applica a **Drafts per Mac** con Marked sullo stesso Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/