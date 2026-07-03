<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Accedi alla modalità correzione di bozze dal menu a forma di ingranaggio. Si tratta di una funzionalità sperimentale progettata principalmente per gli editor che ricevono testo da altri e necessitano di inserire commenti e fornire feedback.

La modalità di correzione di bozze congela gli aggiornamenti del documento, impedendo la perdita di annotazioni e note durante l'aggiornamento del documento. Nella barra in alto viene visualizzato un indicatore rosso per ricordarti che la modalità di correzione di bozze è attiva.

Navigazione tramite tastiera, aggiunta di segnalibri ed evidenziazione di parole chiave sono tutte funzioni durante la correzione.

## Annotazioni

Durante la modalità di correzione di bozze, la selezione del testo nel documento genererà un popup che ti consentirà di selezionare tra diversi tipi di evidenziazione. Fai clic sul tipo di evidenziazione che desideri aggiungere al testo oppure annulla facendo clic sul pulsante "Annulla" o semplicemente facendo clic all'esterno del popup.

## Note

![Annotazioni][1]

[1]: images/Annotating.jpg class=center

Una volta aggiunta un'evidenziazione, puoi aggiungervi brevi note facendo clic sull'evidenziazione. Il popup ora conterrà un campo di testo in cui potrai inserire qualsiasi nota pertinente al testo evidenziato. Le note possono essere eliminate e modificate facendo clic su un punto evidenziato che contiene già una nota.

Le note vengono esportate **solo** durante il salvataggio in HTML. Le evidenziazioni rimangono nella maggior parte dei formati di esportazione, inclusi RTF e PDF.

## Controllo ortografico

In modalità correzione di bozze, puoi accedere al controllo ortografico a livello di sistema dal menu a forma di ingranaggio: {% appmenu {{gear}}, Proofing, Highlight All Spelling Errors %}. Questo sarà lento su documenti di grandi dimensioni e verrà visualizzato un avviso che ti avvisa se il processo richiederà più di 30 secondi circa. Poiché il controllo ortografico non funziona nell'anteprima web di Marked, è stato implementato un "hack" per farlo funzionare, e non è rapido.

Una volta eseguito il controllo ortografico, puoi aprire il pannello Supposti ortografici per attivare il controllo grammaticale e visualizzare i suggerimenti per correggere gli errori. Contrassegnato come *impossibile* modificarli sul posto, devi tornare al documento originale per utilizzare i risultati.

*Scorciatoie:* {% kbd ctrl opt cmd S %} eseguirà il controllo ortografico. {% kbd ctrl opt cmd N %} passerà all'errore successivo nel documento e {% kbd ctrl opt cmd G %} mostrerà il pannello delle ipotesi.