<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

La velocità di rendering e le prestazioni complessive di Marked possono variare notevolmente in base alle impostazioni e al tipo di contenuto presente nel documento. Esistono diversi fattori che possono portare a un rendering lento o a lunghi ritardi:

* **Time Machine.** Se Time Machine è in esecuzione e il tuo sistema registra molta attività del disco, potresti scoprire che Marked è più lento nel rispondere alle modifiche nel documento. La velocità di elaborazione non viene influenzata, ma solo il tempo di reazione.
* **Rendering di un documento Markdown contenente molto codice HTML.** L'elaborazione richiederà sempre più tempo. Discount lo gestisce un po' meglio di MultiMarkdown, quindi se questa è una necessità potresti prendere in considerazione la possibilità di cambiare il processore predefinito (**Avvertenza:** perderai le note a piè di pagina e alcune altre funzionalità di MultiMarkdown).
* **Utilizzo di molte inclusioni.** Che si tratti di inclusioni di codice o di un file di unione di indici, per raccogliere tutti i pezzi Mark impiega un secondo. Lo stesso vale per i documenti Scrivener di grandi dimensioni. Non c'è molto che puoi fare per risolvere questo problema, Marked farà del suo meglio per stare al passo con il modo in cui scegli di strutturare il tuo documento.
* **Condizioni del disco rigido.** Se il tuo disco rigido è quasi pieno, il tuo indice Spotlight è danneggiato o le tue autorizzazioni non sono state riparate da un po', Marked potrebbe avere difficoltà a rilevare le modifiche al file che sta guardando. Ottimizzare l'unità riparando le autorizzazioni spesso aiuta e ricostruire l'indice Spotlight è spesso una soluzione per i problemi contrassegnati.