<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane Advanced %}:

![Impostazioni: Avanzate][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

Metadati YAML e Pandoc
: - __Ignora:__ Lascia esattamente come esiste nel documento, utile se il tuo processore o preprocessore utilizza effettivamente YAML.
: - __Rimuovi prima del rendering__: il blocco YAML viene rimosso
: - __Tratta come metadati MMD:__ Converte il blocco di metadati YAML o Pandoc nel formato MultiMarkdown.

Elimina le intestazioni dei metadati MultiMarkdown
: Se abilitato, i metadati MultiMarkdown nella parte superiore del documento verranno rimossi prima del rendering.
: questo può essere utile se stai utilizzando un processore non MultiMarkdown che altrimenti visualizzerebbe i metadati nel documento renderizzato. I metadati vengono comunque letti prima della rimozione, quindi la sintassi specifica di Marked verrà comunque riconosciuta.

Immagini ospitate nella cache
: Marked non memorizza nella cache le immagini nell'anteprima per impostazione predefinita, poiché controlla le modifiche in quelle immagini e le aggiorna immediatamente. Se utilizzi immagini a cui viene fatto riferimento tramite un URL web, puoi attivare la memorizzazione nella cache di tali immagini per accelerare il rendering su connessioni più lente.

Analizzare le statistiche di leggibilità
: Se preferisci non calcolare le [statistiche](Document_Statistics.html), l'elaborazione verrà disabilitata. Ciò può fornire alcuni miglioramenti delle prestazioni su documenti molto grandi. Il conteggio dei caratteri, delle parole e delle frasi continuerà a funzionare.

Utilizza il tavolo di montaggio Trova a livello di sistema
: questa opzione consentirà a Marked di riprendere qualsiasi termine di ricerca utilizzato più recentemente in un altro editor e qualsiasi cosa cercata in Marked diventerà la ricerca anche in altre applicazioni. Disabilitarlo rende la funzione di ricerca di Marked indipendente.

Utilizzare {% kbd cmd E %} per Trova con selezione
: Per impostazione predefinita, {% kbd cmd E %} apre l'editor predefinito. Se questa opzione è abilitata, {% kbd cmd E %} funzionerà come nella maggior parte delle applicazioni di modifica del testo, utilizzando il testo selezionato per Trova e Apri nell'editor può essere attivato con {% kbd opt cmd E %}.

Modalità di debug
: abilita la registrazione del debug. Utilizzalo per la risoluzione dei problemi e quando segnali un problema. Seleziona __Aiuto->Apri registro debug__ per visualizzare l'attività.
: l'impostazione su _Tutto_ mostrerà messaggi informativi, avvisi e messaggi di errore. Puoi anche impostarlo per mostrare solo errori o errori e avvisi.

Backup delle impostazioni
: è possibile eseguire il backup delle impostazioni in un file JSON che può essere utilizzato per ripristinare le impostazioni o trasferirle su un nuovo computer.