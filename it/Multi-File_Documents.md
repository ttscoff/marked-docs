<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Marked consente diverse sintassi diverse per includere un file all'interno di un altro.

## Sintassi contrassegnata

Puoi includere file esterni in un singolo documento di anteprima utilizzando la sintassi speciale `<<[path/file]` all'inizio di una riga. La riga dovrebbe avere righe vuote sopra e sotto e si presuppone che il percorso sia relativo al documento principale a meno che non inizi con una barra (`/`) o una tilde (`~`). La barra (directory root) e la tilde (directory home) possono essere utilizzate per definire percorsi assoluti ai file. Non è necessario alcun percorso se i file esterni si trovano nella stessa cartella del documento principale, è sufficiente inserire il nome del file (con distinzione tra maiuscole e minuscole e inclusa l'estensione) tra parentesi quadre.

È possibile utilizzare le intestazioni dei metadati "Include Base" o "Transclude Base" per modificare la posizione di base per i file inclusi, ad esempio:

    Trascludi Base: ~/Desktop

*Nota che quando visualizzi documenti con file inclusi, puoi digitare "I" (shift-i) per vedere quale file incluso si trova nell'area visibile. Premendo Invio mentre viene visualizzato il percorso del file incluso si aprirà il file incluso nell'editor predefinito.*

Utilizzando questa funzionalità è possibile creare documenti/libri di grandi dimensioni utilizzando più file (ad esempio un file per ogni capitolo) e quindi specificare l'ordine dei documenti in un unico file di indice. Non importa come vengono nominati i file o come sono organizzate le cartelle; il file che apri in Marked verrà considerato l'indice e verranno inclusi i file elencati al suo interno. Un esempio di file indice per un documento in tre parti:

Struttura delle cartelle:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x larghezza=316px altezza=163px classe=centro

Indice.md:

	# Titolo del documento

	## Sezione 1

	<<[sezioni/sezione1.md]

	## Sezione 2

	<<[sezioni/sezione2.md]

	## Sezione 3

	<<[sezioni/sezione3.md]

Aprendo Index.md in Marked verranno visualizzati i suoi contenuti con tutti e tre i file inclusi espansi all'interno. Tutti i file inclusi verranno controllati per eventuali modifiche. A differenza del documento aperto in Marked, il tracciamento dei file inclusi dipende da Spotlight per ottenere gli aggiornamenti e deve esistere in una cartella indicizzata da Spotlight sul disco.

Puoi anche includere frammenti di codice e codice HTML o testo utilizzando [variazioni di questa sintassi](Special_Syntax.html#includingcode).

L'esportazione HTML finale di un documento contenente include avrà commenti HTML contenenti il ​​percorso relativo del file incluso all'inizio e alla fine del testo importato.

**Nota:** maggiore è il numero di file inclusi in un documento, più lento sarà il tempo di compilazione complessivo dell'anteprima. Marked tenta di ottimizzare e memorizzare nella cache il processo, ma prevede alcuni ritardi nel rendering man mano che le dimensioni del documento aumentano.

## Sintassi di trascrizione MultiMarkdown

Puoi anche utilizzare la sintassi `{{filename}}` basata sulle specifiche MultiMarkdown più recenti. Marked riconoscerà `Transclude Base: path` nei metadati MMD e lo utilizzerà come base per la transclusione dei file.

Transclude Base verrà riconosciuto solo nel documento principale, non nei documenti aggiuntivi inclusi. Tutte le inclusioni nidificate devono avere percorsi basati sulla Transclude Base iniziale o sulla posizione del documento principale.

La sintassi del codice protetto fornita da MultiMarkdown per includere file senza elaborazione non funzionerà in Marked. Per fare ciò, utilizza la sintassi `<<(file)` (blocco di codice) o `<<{file}` (grezzo).

## Sintassi del blocco writer IA

Marked 2.5.11+ supporta la sintassi IA Writer [Content Block][ia]. Questo è un riferimento che inizia con una barra (`/`) sulla propria riga. Può essere un esempio di codice, un'immagine, un file di markdown o un file CSV. Tutto verrà gestito in modo appropriato in base all'estensione del file incluso e, se possibile, i CSV verranno [convertiti in tabelle Markdown][csv].

In IA Writer, i file inclusi vengono inseriti nel contenitore iCloud e non sempre richiedono percorsi "effettivi". In Marked, a meno che i file inclusi non esistano già nella stessa cartella del file visualizzato in anteprima, questa sintassi deve essere utilizzata con un percorso, assoluto o relativo. La prima barra verrà ignorata, quindi se si tratta di un percorso assoluto, inizia con due barre.

Uno snippet di codice nella stessa cartella del documento visualizzato in anteprima:

    /snippet.h

Percorso relativo a una sottodirectory denominata "immagini":

    /images/image.png "titolo opzionale"

Percorso assoluto della cartella Documenti:

    //Utenti/nome utente/Documenti/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## Come vengono convertiti il contorno, la mappa mentale e gli include CSV

Quando includi determinati tipi di file con la sintassi del blocco `<<[path]` o IA Writer, Marked li converte invece di inserire il contenuto del file non elaborato. Il comportamento del contorno e della mappa mentale dipende dall'estensione del file e dalle preferenze di [Impostazioni: App → Mappe mentali/Contorni] [mappe mentali]. I file CSV/TSV vengono sempre convertiti in tabelle Markdown (vedi [Creazione di tabelle utilizzando file CSV][csv]).

| Formato | Estensione | Quando "Incorpora come sirena" è **attiva** | Quando **spento** |
|--------|------------|-------|--------------|
| **iPensieri X** | .itmz | Diagramma della mappa mentale della sirena (albero ordinato) | Immagine di anteprima dal file .itmz |
| **MindManager** | .mmap | Diagramma della mappa mentale della sirena | Elenco Markdown nidificato |
| **MenteLibera** | .mm | Diagramma della mappa mentale della sirena | Elenco Markdown nidificato |
| **OPML** | .opml | Diagramma della mappa mentale della sirena | Elenco Markdown nidificato |
| **OmniOutliner** | .oschema | Diagramma della mappa mentale della sirena | Elenco Markdown nidificato |
| **Bici** | .bici | Mappa mentale della sirena (nome del file come nodo radice) | Elenco Markdown nidificato (nessun titolo del documento) |
| **CSV/TSV** | .csv, .tsv | Tabella di ribasso ||
| **RTF/RTFD** | .rtf, .rtfd | Ribasso tramite conversione RTF (vedi [Supporto RTF e RTFD](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown tramite conversione PDF quando aperto come documento principale (vedi [Supporto PDF](PDF_Support.html)) ||

Ogni formato di contorno/mappa mentale ha la propria casella di controllo sotto *Mappe mentali/contorni* (mappe mentali, file OPML, contorni bici, contorni OmniOutliner). La disattivazione di un formato utilizza il comportamento "disattivato" solo per quel tipo. Vedi [Incorporamento di mappe mentali e contorni](Embedding_Mind_Maps_and_Outlines.html) per i dettagli sul formato e [Impostazioni: App][Mappe mentali] per modificare queste opzioni. Per i dettagli sulla conversione CSV, vedere [Creazione di tabelle utilizzando file CSV][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Formati di libri

Marked supporta anche file indice in formati come [Leanpub][lp], [GitBook][gb] e mmd\_merge (MultiMarkdown). I file inclusi negli indici del formato libro verranno controllati per eventuali modifiche e il risultato sarà un'anteprima completa del documento compilato, proprio come nell'esempio "Index.md" sopra.

### Leanpub

Se abiliti l'opzione in {% prefspane Apps %} sotto il supporto Leanpub/GitBook, i file denominati "Book.txt" verranno trattati automaticamente come file indice Leanpub. Viene riconosciuto anche il vecchio formato "frontmatter:".

[Documentazione Leanpub.][lpdocs]

Esempio di Leanpub Book.txt:

    argomento principale:
    Ringraziamenti.txt
    Prefazione.txt
    Introduzione.txt
    questione principale:
    Markdown.txt
    Libri di esempio.txt
    Inserimento di Images.txt


### mmd_merge

Per mmd\_merge, Marked richiede che la prima riga sia "#merge" (uno speciale trigger Marked per mmd\_merge, trattato come un commento e ignorato da altri processori).

[documentazione mmd_merge.][mmdm]

mmd_merge esempio:

    #unire
    metadati.txt
    Capitolo-1.md
        sottocapitolo-1-1.md
        sottocapitolo-1-2.md
    Capitolo-2.md
        sottocapitolo-2-1.md
        sottocapitolo-2-2.md
    FAQ.md
    Ringraziamenti.md

### GitBook

La formattazione GitBook utilizza un elenco Markdown per creare la struttura e il sommario. Se il supporto GitBook è abilitato in {% prefspane Apps %} sotto Supporto Leanpub/GitBook, un file denominato SUMMARY.md verrà letto e convertito automaticamente nel formato mmd_merge, consentendo un'anteprima completa del documento GitBook.

[Documentazione GitBook.][gbdocs]

Esempio GitBook SUMMARY.md:

    # Riepilogo

    * [Parte I](parte1/README.md)
        * [Scrivere è bello](parte1/writing.md)
        * [GitBook è carino](part1/gitbook.md)
    * [Parte II](parte2/README.md)
        * [Adoriamo il feedback](part2/feedback_please.md)
        * [Strumenti migliori per gli autori](part2/better_tools.md)

GitBook consente l'utilizzo degli ancoraggi nel sommario SUMMARY.md, ma Marked li ignorerà e includerà il documento di base solo una volta.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Funzionalità di anteprima di documenti multi-file

![Confini dei file inclusi][2]

   [2]: images/includeboundaries.png @2x larghezza=859px altezza=239px classe=centro

Quando visualizzi un documento contenente file inclusi, puoi utilizzare due funzionalità per capire quale file stai guardando.

* **Tastiera:** Premendo {% kbd shift I %} verrà visualizzato brevemente un popup che mostra il titolo del file attualmente visibile nella posizione di scorrimento dell'anteprima.
    * Premendo {% kbd Return %} seguito da {% kbd I %} si modificherà il file visualizzato con il proprio editor esterno.
* **Mouse:** Selezionando "Mostra confini dei file inclusi" dal menu Ingranaggio ({% kbd ctrl cmd B %}) verrà aggiunta una barra colorata sul lato sinistro dell'anteprima, segmentata per mostrare l'inizio e la fine dei file inclusi. Mostra anche le inclusioni nidificate. Passando il mouse su una sezione di questa barra verrà mostrato il nome del file che rappresenta e facendo clic su di esso si aprirà quel file nell'editor prescelto.