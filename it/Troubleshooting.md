<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

### Modalità di debug [debug-mode]

Puoi abilitare la registrazione del debug aprendo {% prefspane Advanced %} e selezionando la casella di controllo **Modalità debug** nella parte inferiore del riquadro. Verrà visualizzato un menu a discesa in cui puoi impostare il livello di registrazione che desideri vedere:

- **Solo errori**: verranno registrati solo gli errori gravi
- **Errori e avvisi**: visualizza inoltre avvisi meno urgenti
- **Tutto**: visualizza errori, avvisi e messaggi di debug a livello di informazioni. Questa è l'impostazione consigliata per la risoluzione dei problemi.

{% note %}
TODO: Funziona ancora?
Puoi anche accedere a queste opzioni tenendo premuto il tasto {% kbd opt  %} quando apri {% appmenu Help %} nella barra dei menu.
{% endnote %}

### Visualizzazione del registro [viewing-the-log]

Con la **Modalità Debug** abilitata, puoi aprire il menu {% appmenu Help %} e selezionare Apri registro debug. Verrà aperto il registro di Marked in Console.app, che verrà aggiornato in tempo reale man mano che i messaggi di registro vengono aggiunti durante l'utilizzo di Marked.

### Risoluzione dei problemi relativi alle regole personalizzate [troubleshooting-custom-rules]

[Preprocessori e processori personalizzati](Custom_Processor.html) ottengono la propria interfaccia di registro. Seleziona {% appmenu Help, Show Custom Rules Log %} per aprire la finestra. Questa finestra visualizzerà un registro colorato che mostra quali regole corrispondono e quali comandi eseguono.

### Segnalazione di un problema [reporting-an-issue]

Usa {% appmenu Help, Report an Issue %} per aprire una finestra che mostra le tue impostazioni per i tasti più comuni e un modello per creare una segnalazione di bug. Utilizza il pulsante "Copia negli appunti" per copiare il contenuto della finestra e fai clic su "Apri sito di supporto" per aprire [il modulo della nuova domanda](https://support.markedapp.com/questions/add) dove puoi incollare il tuo rapporto. Cerco di rispondere alle segnalazioni entro 48 ore.