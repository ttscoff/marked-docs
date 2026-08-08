<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane Apps %}:

(Vedi [Supporto aggiuntivo per le app](Additional_Application_Support.html))

![Impostazioni: App][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Impostazioni generali [general-settings]

Editor di testo
: seleziona un editor di testo per ricevere il documento corrente quando digiti {% kbd cmd E %}.

Modifica automaticamente i nuovi file
: Quando si utilizza il comando "Nuovo file", questa opzione aprirà automaticamente il file creato nell'editor esterno scelto.

I collegamenti ai file di testo dovrebbero aprirsi in:
: determina il comportamento di Marked quando un collegamento cliccato in una finestra di anteprima porta a un file di testo locale.

Editor di immagini
: selezionare un'applicazione da aprire quando si fa clic con il pulsante destro del mouse su un'immagine locale e si seleziona "Modifica immagine".

Editor di annotazioni/markup delle immagini
: selezionare un'applicazione da aprire quando si fa clic con il tasto destro del mouse su un'immagine locale e si seleziona "Annota immagine".

Se non viene scelto alcun editor, Marked presenta un menu di applicazioni installate quando modifichi o annoti. Il menu include i comuni strumenti Markdown, immagini e annotazioni presenti sul tuo Mac, un'opzione **Altro…** per scegliere qualsiasi app da `/Applications` e **Usa sempre questa app** (abilitata per impostazione predefinita) per salvare la tua scelta come predefinita. Utilizza il pulsante Cancella (cerchio con una X) accanto a ciascun controllo Scegli in {% prefspane Apps %} per rimuovere una selezione e tornare al selettore.

### Impostazioni specifiche dell'applicazione [application-specific-settings]

Mostra commenti e annotazioni per impostazione predefinita
: se selezionato, le annotazioni effettuate nei documenti Scrivener, Fountain, Word e CriticMarkup verranno visualizzate evidenziate nell'anteprima. Deseleziona per nasconderlo completamente. Questi possono anche essere attivati ​​durante la lettura di un documento dal menu {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%}.
: quando i commenti sono abilitati, i commenti e le note a piè di pagina verranno visualizzati in una barra laterale. Passare il mouse sopra un commento indicherà il punto in cui si trova nel documento.

####Doc

[(Informazioni sul supporto DocC)](DocC_Support.html)

Risolvi i riferimenti alle immagini DocC
: all'interno di un catalogo di documentazione `.docc`, risolvi i riferimenti `![](ImageName)` senza estensione alle immagini nella cartella del catalogo `Resources`, incluse le varianti `~dark` e `@2x`.

Risolvi varianti di immagini scure e @2x
: per le immagini locali con estensione file (`images/icon.png`), rileva i file associati `~dark` e `@2x` nella stessa cartella ed emette markup reattivo `<picture>`. Funziona con qualsiasi documento Markdown o HTML, non solo con i cataloghi DocC. Vedi [Varianti immagine](Image_Variants.html).

#### Segnapunto [docc]

Risolvi gli URL hook:// nelle immagini e nei collegamenti
: Marked può leggere gli URL creati da Hookmark, risolvendoli nel loro percorso su disco.

#### Leanpub/GitBook [hookmark]

Abilita il supporto Leanpub
: interpreta i file denominati `Book.txt` come file indice e gestisce la sintassi Leanpub speciale.

Abilita il supporto GitBook
: interpreta i file denominati `SUMMARY.md` come file di indice per la documentazione di GitBook.

#### Markdownifier [leanpubgitbook]

Utilizza collegamenti in linea
: i documenti Markdown creati da Markdownifier utilizzeranno collegamenti in linea anziché di riferimento.

#### MarteModifica [markdownifier]

Includi il titolo del post come intestazione Markdown (h1)
: utilizza il titolo del post selezionato come intestazione Markdown.

Mostra i metadati come tabella
: se abilitato, i metadati come categorie e titoli verranno visualizzati come tabella Markdown nell'anteprima.

#### Cartelle [marsedit]

Visualizza in anteprima solo queste estensioni
: Quando si apre una cartella, Marked cercherà il documento modificato più di recente, utilizzando per impostazione predefinita estensioni come `md`, `mmd` e `html`. L'elenco qui sovrascrive l'impostazione predefinita.

#### Scrivener [folders]

[(Informazioni sul supporto Scrivener)](Scrivener_Support.html)

Includi i titoli dei documenti come intestazioni Markdown
: analizza il titolo delle pagine e delle pagine nidificate per creare intestazioni Markdown gerarchiche.

Aggiungi i metadati di compilazione (titolo, autore) quando mancano
: quando un progetto Scrivener non ha un documento `metadata` o un'intestazione MultiMarkdown esistente, anteponi Titolo e Autore dalle impostazioni di compilazione del progetto (`Settings/compile.xml`).

Apri i file .scriv in Scrivener quando vengono aperti in Marked
: quando un documento Scrivener viene aperto in Marked, lo apre automaticamente anche in Scrivener.

#### Parola [scrivener]

Converti il rilevamento delle modifiche <-> CriticMarkup
: se abilitato, il rilevamento delle modifiche nei documenti Word verrà convertito in CriticMarkup al momento dell'importazione e CriticMarkup verrà convertito nel rilevamento delle modifiche di Word durante l'esportazione di file DOCX.

#### Mappe mentali/Contorni [word]

Incorpora come mappe mentali della Sirena
: ciascuna casella di controllo controlla un formato incluso. Quando **attivo**, il file incluso viene convertito in un diagramma della mappa mentale della sirena (layout ad albero ordinato). Quando **disattivato**, Marked utilizza l'alternativa per quel formato.
: **Mappe mentali** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Se attivo: mappa mentale della sirena. Se disattivato: iThoughts incorpora la sua immagine di anteprima; MindManager e FreeMind si convertono in elenchi Markdown nidificati.
: **File OPML** (.opml). Se attivo: mappa mentale della sirena. Se disattivato: elenco Markdown nidificato.
: **Contorni OmniOutliner** (.ooutline). Se attivo: mappa mentale della sirena. Se disattivato: elenco Markdown nidificato (o elenco di controllo, ove applicabile).
: **Profili della bicicletta**. Se attivo: mappa mentale della sirena. Se disattivato: elenco Markdown nidificato.