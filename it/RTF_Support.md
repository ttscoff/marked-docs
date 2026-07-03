<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked può aprire direttamente documenti Rich Text Format (`.rtf`) e RTFD (`.rtfd`). Trascina un file su Contrassegnato o usa {% appmenu File, Open... ({{cmd}}O) %}. Il documento viene convertito in Markdown per l'anteprima e l'esportazione.

Funziona bene con i documenti di **Pages**, **TextEdit**, **Word** e altre app che salvano RTF o RTFD. Marked è ancora uno strumento di **anteprima**: modifichi nell'applicazione originale e Marked si aggiorna quando salvi.

## Come funziona la conversione

Marked converte RTF in HTML utilizzando il motore di testo del sistema, quindi in Markdown. Il convertitore:

- Associa le **dimensioni dei caratteri dei paragrafi grandi** ai livelli dell'intestazione (rispetto alle dimensioni del corpo più comuni nel documento)
- Conserva il **grassetto**, il *corsivo* e i collegamenti ove possibile
- Estrae **immagini** da pacchetti RTFD e allegati incorporati
- **Non** tratta i nomi dei file RTF come didascalie delle immagini (vedi Immagini di seguito)

La stessa pipeline di conversione viene utilizzata per la compilazione Scrivener RTF e per i file RTF inclusi in altri documenti.

## Anteprima dal vivo

Quando salvi il file RTF o RTFD in un'altra applicazione, Marked rileva la modifica e aggiorna automaticamente l'anteprima.

## Immagini

RTF non definisce un campo "didascalia" separato nel modo in cui Cocoa esporta in HTML. Ciò che appare come una didascalia nel tuo layout è solitamente **testo normale** nel paragrafo successivo e Marked lo mantiene come corpo del testo.

Le immagini incorporate e le immagini all'interno dei bundle RTFD (ad esempio `pastedGraphic.png` in un'esportazione di Pages) vengono copiate in una cartella di cache in `~/Library/Caches/Marked/Watchers/`. I percorsi delle immagini di anteprima puntano ai file memorizzati nella cache fino all'esportazione.

Marked **non** utilizza il nome del file immagine come testo alternativo o didascalia di una figura MultiMarkdown. Non dovresti vedere `pastedGraphic.png` sotto l'immagine a meno che tu non abbia digitato quel testo nel documento.

## Esportazione e altre funzionalità

Dopo la conversione, Marked tratta il documento come altre fonti compilate (simili a [Scrivener](Scrivener_Support.html) e [DOCX](Working_with_DOCX.html)): esportazione, statistiche e la maggior parte delle funzionalità di anteprima vengono eseguite rispetto al Markdown generato archiviato nella cache degli Osservatori.

## Limitazioni

La qualità della conversione dipende dall'applicazione di origine. In generale:

- I **Titoli** vengono dedotti dalla dimensione del carattere, non dagli stili del contorno di Word/Pagine
- **Layout complesso** (tabelle a più colonne utilizzate solo per il posizionamento, caselle di testo) potrebbe non essere mappato in modo pulito su Markdown
- Le **Equazioni** in RTF non sono supportate nell'anteprima (vedi [MathJax](MathJax.html) per la matematica Markdown)
- **Legacy `.doc`** (Word binario) non è supportato; salva prima come DOCX o RTF

Per incollare una volta senza salvare un file, utilizza invece [Anteprima Appunti](Opening_Files.html#from-the-clipboard).

## Argomenti correlati

- [Supporto PDF](PDF_Support.html) -- apre documenti PDF come origini Markdown
- [Lavorare con DOCX](Working_with_DOCX.html) -- Documenti Word con rilevamento delle modifiche e commenti
- [Apertura file](Opening_Files.html) -- trascina e rilascia, Apri recenti, appunti
- [Esportazione](Exporting.html) -- Copia Rich Text e salva RTFD (esportazione), distinto dall'apertura di RTF come file sorgente