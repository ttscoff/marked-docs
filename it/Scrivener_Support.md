<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Usa insieme i tuoi due strumenti di scrittura preferiti.

> Marked può ancora leggere i file Scrivener 2.0, ma lo sviluppo si concentrerà sulla versione 3 dopo Marked 2.5.11.

## Nozioni di base su Scrivener 3.0 [scrivener-30-basics]

Trascina un progetto Scrivener (.scriv) su Marked e verrà compilato e visualizzato in anteprima. Se scegli l'opzione per aprire i file .scriv in Scrivener (sopra), Marked avvierà Scrivener anche quando trascini il file su Marked.

Come con altri documenti, le modifiche ai file Scrivener vengono aggiornate in tempo reale al momento del salvataggio. Inoltre, quando un documento Scrivener è in primo piano in Marked, {% kbd cmd E %} lo aprirà automaticamente in Scrivener.

## Filtraggio dei documenti del raccoglitore [filtering-binder-documents]

Quando apri un progetto Scrivener in Marked, il contenuto di anteprima viene creato solo dai documenti del raccoglitore selezionati. Il filtraggio è sempre attivo per `.scriv` file; il pannello dei filtri è solo un modo conveniente per modificare ciò che è incluso.

Apri il pannello da **Proofing > Filtra documenti Scrivener** ({% kbd opt-cmd-f %}). La voce di menu mostra un segno di spunta mentre il pannello è visibile. La chiusura del pannello non disattiva il filtraggio né reimposta le selezioni.

Il pannello dei filtri elenca le sezioni del raccoglitore del tuo progetto (Bozza, Ricerca e altri raccoglitori di livello superiore tranne Cestino). Ogni sezione è compressa per impostazione predefinita. Espandi una sezione per visualizzarne i documenti e le cartelle in una struttura:

- Seleziona o deseleziona qualsiasi **documento di testo** per includerlo o escluderlo dall'anteprima.
- Fare clic sulla riga di una **cartella** per selezionare o deselezionare tutti i suoi discendenti. Un trattino nella casella di controllo indica che sono selezionati solo alcuni discendenti.
- Le righe con **Includi in compilazione** disattivate in Scrivener appaiono in grigio, ma puoi comunque selezionarle per visualizzarne l'anteprima in Contrassegnato.
- **Immagini, PDF e altri elementi del raccoglitore non di testo** vengono visualizzati nell'elenco ma non possono essere selezionati.
- I file **RTF mancanti** vengono ancora visualizzati; se aggiungi contenuto in Scrivener mentre Marked è aperto, l'anteprima si aggiorna al salvataggio come qualsiasi altra modifica di Scrivener.

Utilizza **Seleziona tutto** e **Deseleziona tutto** nella parte superiore del pannello per l'intero progetto. Ogni intestazione di sezione ha i pulsanti **Tutti** e **Nessuno** solo per quella sezione. **Deseleziona tutto** significa che nessun documento viene controllato.

Se non viene selezionato nulla, l'anteprima mostra un breve messaggio con un collegamento per aprire il pannello dei filtri (`x-marked://scrivenerfilter`). Puoi utilizzare quell'URL negli script o in altre app per sollevare il pannello per il documento Scrivener anteriore in Marked.

Le selezioni delle caselle di controllo vengono salvate per progetto Scrivener (tramite l'identificatore del progetto nel file `.scrivx`) e ripristinate la prossima volta che apri il progetto in Marked. La prima volta che si apre un progetto, Marked seleziona solo i documenti del raccoglitore **Bozza** il cui flag **Includi in compilazione** è Sì (o non impostato, che Scrivener considera Sì). La ricerca e altri raccoglitori iniziano senza controllo; Gli elementi Draft esclusi dalla compilazione iniziano deselezionati ma rimangono selezionabili nell'elenco.

I progetti Scrivener 2 mostrano solo il raccoglitore **Bozza** nel pannello dei filtri. I progetti Scrivener 3 includono tutti i raccoglitori tranne Cestino.

Il pannello dei filtri può rimanere aperto insieme ad altri strumenti come **Visualizza ripetizione parole**. La modifica di una casella di controllo ricompila l'anteprima dopo un breve ritardo; se un progetto di grandi dimensioni è ancora in fase di compilazione, Marked annulla l'importazione in corso e ricomincia con la nuova selezione.

## Intestazioni Markdown dai titoli Scrivener [markdown-headers-from-scrivener-titles]

Marked può anche creare intestazioni Markdown gerarchiche in base alle pagine del file Scrivener. Per abilitarlo, basta selezionare l'opzione mostrata sopra.

## Metadati MultiMarkdown [multimarkdown-metadata]

Se il primo documento nella cartella Bozza è denominato "metadati", verrà trattato come metadati MultiMarkdown all'inizio del documento di anteprima. Nessuna intestazione verrà inserita per questa sezione, indipendentemente dall'impostazione "Intestazioni Markdown dai titoli Scrivener" (descritta sopra), consentendo al processore MultiMarkdown di leggerla come metadati e consentire sostituzioni e opzioni di esportazione di conseguenza.

Puoi rendere questo file formattato in YAML se il tuo processore è uno che gestisce YAML.

Se non utilizzi un documento `metadata`, Marked può anche anteporre metadati MultiMarkdown dalle impostazioni di compilazione del tuo progetto (`Settings/compile.xml`), utilizzando gli stessi campi **Titolo** e **Autore** che Scrivener esporterebbe in MultiMarkdown. Questo è abilitato per impostazione predefinita (tasto preferenza `scrivenerCompileMetadata`). I campi di metadati personalizzati vengono inclusi solo quando vengono visualizzati nelle impostazioni di compilazione **MMD Metadata**** del progetto, non nei campi personalizzati per documento.

## Collegamenti [links]

Per i collegamenti esterni (HTTP), è possibile utilizzare la sintassi Markdown o la formattazione dei collegamenti di Scrivener. Marked convertirà il formato Scrivener in Markdown prima dell'elaborazione.

## Commenti [comments]

Marked può elaborare commenti e note a piè di pagina creati in linea all'interno del documento.

## Tabelle [tables]

Marked può convertire le tabelle Scrivener di base. Se desideri includere una tabella nel tuo output, tuttavia, è meglio farlo nel [formato tabella MultiMarkdown](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (Un'app chiamata [TableFlip](http://tableflipapp.com/) può rendere la generazione di questi un compito semplice.)

## Funzionalità aggiuntive di Scrivener [additional-scrivener-features]

Oltre alle funzionalità di compilazione e anteprima di base, Marked supporta anche alcune convenzioni specifiche di Scrivener. Innanzitutto, nel tuo documento Scrivener, puoi utilizzare "Preserva formattazione" in linea o su un blocco di testo autonomo e verrà convertito in blocchi di codice nell'anteprima.

Marked legge anche le note a piè di pagina _inline_ di Scrivener. Se inserisci una nota a piè di pagina all'interno o alla fine di un paragrafo, verrà convertita in una nota a piè di pagina MultiMarkdown nell'anteprima.

## Utilizzo delle immagini nel documento Scrivener [using-images-in-your-scrivener-document]

Le immagini possono essere incorporate nel documento Scrivener o referenziate con la sintassi delle immagini Markdown. La versione Markdown di un tag immagine è `![alt text](path/to/image.ext "optional title/description")`. È possibile utilizzare anche il formato di riferimento:

    ![testo alternativo][img1]

    [img1]: /percorso/dell'immagine.ext "descrizione facoltativa"

Il percorso di base per l'output HTML nell'Anteprima verrà impostato sulla cartella contenente il documento Scrivener. Pertanto, il posizionamento delle immagini nella stessa cartella del documento di lavoro consentirà l'accesso diretto ad esse. Se il tuo documento Scrivener è in `~/Desktop/TestDoc.scriv` e hai un'immagine chiamata "testimage.png" in `~/Desktop/testimage.png`, puoi aggiungere l'immagine al tuo documento utilizzando:

    ![Immagine di prova](testimage.png)

I percorsi relativi basati sulla cartella principale del documento funzioneranno, mentre i percorsi assoluti consentiranno l'accesso alle immagini ovunque ma potrebbero non essere altrettanto portabili per l'output HTML.

## Nota sulla sicurezza [security-note]

Una cartella cache verrà creata in ~/Library/Application Support/Marked quando apri il file .scriv in Marked. Questa non è una cartella protetta, quindi se il documento originale si trova su un disco crittografato o protetto in altro modo, tieni presente che il suo contenuto non sarà crittografato nella cache. Per una protezione limitata, puoi assicurarti che questa cache non venga visualizzata in Spotlight aggiungendo ~/Library/Application Support/Marked alle tue impostazioni sulla privacy in Spotlight.

Vedi [Ulteriori integrazioni dell'app](Additional_Application_Support.html) per l'anteprima degli appunti, i collegamenti wiki, gli script e l'elenco completo delle guide per app.