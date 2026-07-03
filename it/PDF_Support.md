<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked può aprire direttamente i documenti PDF (`.pdf`). Trascina un file su Contrassegnato o usa {% appmenu File, Open... ({{cmd}}O) %}. Il documento viene convertito in Markdown per l'anteprima e l'esportazione.

L'importazione di PDF funziona meglio su **PDF più piccoli e basati su testo** (diapositive, articoli, brevi report). Sono supportati manuali di grandi dimensioni, libri e documenti scansionati, ma spesso la conversione è lenta o imperfetta. Consulta le **Limitazioni** di seguito.

Marked è ancora uno strumento di **anteprima**: non puoi modificare il PDF all'interno di Marked. Utilizza {% kbd cmd E %} per aprire il PDF in **Anteprima** (o nell'impostazione predefinita del sistema) e Contrassegnato si aggiorna quando il file cambia sul disco.

## Come funziona la conversione

L'importazione di PDF utilizza la libreria [pdf22md](https://github.com/twardoch/pdf22md) (licenza MIT; vedere [licenza pdf22md](PDF22MD_License.html)). Marked esegue la conversione in background mostrando un breve avviso di **Conversione in corso**.

Il convertitore:

- Estrae **testo** da PDF digitali utilizzando PDFKit
- Utilizza **Vision OCR** sulle pagine in cui manca il testo incorporato (comune con le scansioni)
- Rileva i **titoli** dalla dimensione del carattere quando possibile
- Salva le **immagini** in una cartella `assets` accanto al Markdown generato

Marked **non** abilita la pulizia AI opzionale di pdf22md nell'app. La qualità della conversione dipende da come è stato creato il PDF.

## Cache e anteprima dal vivo

Markdown convertito e le immagini vengono archiviate nella cache degli osservatori di Marked (`~/Library/Caches/Marked/Watchers/PDF/`). Il percorso PDF originale rimane l'origine del documento per la visione dei file.

Quando salvi o sostituisci il PDF in un'altra applicazione, Marked rileva la modifica e lo riconverte automaticamente (stesso comportamento di ricarica combinato di [RTF](RTF_Support.html) e [Scrivener](Scrivener_Support.html)).

## Esportazione e altre funzionalità

Dopo la conversione, Marked tratta il documento come altre fonti compilate: esportazione, statistiche e la maggior parte delle funzionalità di anteprima vengono eseguite rispetto al Markdown generato. I percorsi delle immagini nel punto di anteprima delle risorse memorizzate nella cache fino all'esportazione.

## Limitazioni

Imposta le tue aspettative di conseguenza: PDF-to-Markdown è utile, non perfetto.

**Cosa funziona bene**

- **PDF vettoriali e basati su testo** con testo incorporato reale (esportato da Word, Pages, InDesign, ecc.)
- **Lunghezza moderata**: poche dozzine di pagine vengono solitamente convertite in tempi ragionevoli con una buona struttura

**Cosa è inaffidabile**

- **OCR (PDF scansionati)**: Vision riempie il testo mancante, ma la precisione è spesso scarsa rispetto a uno strumento OCR dedicato; aspettatevi errori di battitura, parole interrotte e colonne mancanti
- **Tabelle**: il layout viene ricavato dalle posizioni del testo; celle unite, tabelle nidificate e griglie complesse raramente sopravvivono come tabelle Markdown pulite
- **Posizionamento immagine**: le figure vengono estratte a `assets/`, ma l'allineamento, le didascalie e il testo che avvolge le immagini non vengono conservati in modo affidabile

**Dimensioni e prestazioni**

- La conversione di **PDF di grandi dimensioni** (guide utente, libri di testo, manuali lunghi) potrebbe richiedere **molto tempo**, utilizzare una notevole quantità di memoria o non riuscire a produrre un Markdown utile. Marked rimane reattivo mentre la conversione viene eseguita in background, ma non vi è alcuna garanzia che un manuale di 500 pagine venga completato correttamente
- Se la conversione viene completata con poco o nessun contenuto, Marked mostra un errore anziché lasciare un'anteprima vuota

**Altri limiti**

- **I PDF protetti da password** non sono supportati nella versione v1
- **Le immagini PDF incorporate in Markdown** (`![]()` che fa riferimento a un file `.pdf`) non sono correlate all'importazione di PDF: solo l'apertura di un `.pdf` poiché il documento principale attiva la conversione

Per i documenti Word, utilizzare [Lavorare con DOCX](Working_with_DOCX.html). Per Rich Text, utilizzare [Supporto RTF e RTFD](RTF_Support.html).

## Argomenti correlati

- [Apertura file](Opening_Files.html): trascina e rilascia, Apri recenti, appunti
- [Esportazione](Exporting.html): salva HTML, PDF, DOCX e Markdown dall'anteprima
- [Licenza pdf22md](PDF22MD_License.html): testo della licenza MIT di terze parti