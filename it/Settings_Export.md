<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Opzioni in {% prefspane Export %}:

(Vedi [Esportazione](Exporting.html) per maggiori informazioni)

![Impostazioni: Esporta][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Esporta profilo

Esporta profilo
: selezionare un profilo salvato dal menu a comparsa. I profili memorizzano un set completo di preferenze di esportazione per il passaggio rapido tra flussi di lavoro (ad esempio, stampa PDF o HTML web). Vedi [Esporta profili](Exporting.html#export-profiles).

Nuovo
: crea un nuovo profilo dalle impostazioni correnti.

Gestisci
: apre il gestore profili per rinominare, duplicare o eliminare i profili.

### Stampa/PDF

Disabilita collegamenti/evidenziazioni durante l'esportazione di PDF o la stampa
: rimuove la formattazione (sottolineatura e colore) dai collegamenti durante la stampa.

Includi l'URL come annotazione di testo
: durante la stampa o l'esportazione di PDF, l'URL di un collegamento verrà visualizzato dopo il testo collegato.

Sostituisci le regole orizzontali con interruzioni di pagina
: trasforma le regole orizzontali nel documento in interruzioni di pagina (questo forzerà inoltre le note a piè di pagina su una nuova pagina).

Incorpora immagini durante la copia di codice HTML
: quando abilitato, la copia dell'HTML negli appunti eseguirà la scansione delle immagini locali e le codificherà in Base64 per includerle come URL di dati nel codice sorgente.

Stampa colori e immagini di sfondo
: Per impostazione predefinita, Marked stamperà/esporterà con uno sfondo bianco. Se desideri includere colori di sfondo e immagini da temi personalizzati, abilita questa opzione.

Evita titoli orfani
: questa opzione impedisce che i titoli della sezione successiva vengano visualizzati nella parte inferiore di una pagina senza contenuto successivo.

Escludere il primo H1
: ignora il primo titolo di livello uno nel documento quando si utilizzano H1 come interruzioni di pagina.

Utilizza il primo H1 come titolo di riserva
: quando si utilizzano app come Bear o l'anteprima in streaming, questa opzione consente di sovrascrivere il nome del file con il contenuto del primo H1 nel documento. Se vengono specificati i metadati per "titolo", questi avranno sempre la precedenza.

Aggiungi interruzioni di pagina prima
: utilizza le intestazioni di livello 1/2 come divisori di sezione, iniziandole sempre su una nuova pagina. Seleziona "Note a piè di pagina" per aggiungere sempre un'interruzione di pagina prima di qualsiasi nota a piè di pagina nel documento.

Indica le interruzioni di pagina nell'anteprima
: mostra una linea tratteggiata leggera in cui vengono inserite le interruzioni con la sintassi <!\--BREAK\--> o selezionando le opzioni di interruzione automatica nelle impostazioni di esportazione.

Dimensione carattere personalizzata per esportazione/stampa
: se impostato, tutto il testo verrà ridimensionato in base all'impostazione del punto selezionata (predefinita su una base di 10 punti).

Margini
: definisce i margini di stampa (specificati in punti) superiore, inferiore, sinistro e destro.

Stampa il sommario
: include il sommario automatico nella stampa/PDF.

Interruzione di pagina dopo
: passa automaticamente a una nuova pagina dopo aver inserito un sommario.

Indicatori di livello del sommario
: utilizzare i menu a discesa per impostare il contrassegno dell'elemento dell'elenco per ciascun livello di rientro in un sommario.

### Intestazioni e piè di pagina

Configura carattere, logo, campi di intestazione/piè di pagina, formati di data e ora, inclusione della prima pagina, offset della numerazione delle pagine e bordi. I segnaposto di campo includono `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2` e altri.

Vedi [Intestazioni e piè di pagina](Exporting.html#headersandfooters) in [Esportazione](Exporting.html) per riferimenti ed esempi di segnaposto. Vedi [Formati di data e ora](Exporting.html#dateandtimeformats) per i codici di formato `%date` e `%time`.

Includi nella prima pagina
: Se l'opzione per l'intestazione e/o il piè di pagina non è selezionata, la prima pagina non verrà stampata del tipo specificato.

Formato data
: stringa di formato in stile strftime per `%date` nelle intestazioni e nei piè di pagina. Vedi [Formati di data e ora](Exporting.html#dateandtimeformats).

Formato ora
: stringa di formato in stile strftime per `%time` nelle intestazioni e nei piè di pagina. Vedi [Formati di data e ora](Exporting.html#dateandtimeformats).

Offset della numerazione delle pagine
: Utilizzato per regolare il numero da cui iniziano i numeri di pagina. Ad esempio, se hai un sommario sulla prima pagina e desideri che la numerazione inizi dalla seconda pagina, imposta l'offset su -1. La pagina 2 sarà ora la pagina 1 e il totale delle pagine verrà modificato di conseguenza.

Confine
: stampa una linea orizzontale sotto l'intestazione e/o sopra il piè di pagina.

Ripristina formati predefiniti
: reimposta le stringhe di formato di data e ora sui valori predefiniti di Marked (`%m-%d-%Y` e `%I:%M %p`). Vedi [Formati di data e ora](Exporting.html#dateandtimeformats).