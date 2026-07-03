<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Le mappe mentali e i contorni possono essere incorporati nell'anteprima di Markdown utilizzando la [sintassi di inclusione di Marked] [include] o la [sintassi del blocco IA Writer] [ia]. Il comportamento dipende dal formato del file e dall'impostazione "Incorpora mappe come diagrammi della sirena" in {% prefspane Apps %} in *Mappe mentali/Contorni*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Formati supportati

### iPensieri X (.itmz)

I file delle mappe mentali di iThoughts sono archivi zip contenenti dati della mappa e un'immagine di anteprima opzionale.

### MindManager (.mmap)

I file MindManager sono archivi zip contenenti `Document.xml`. Sono supportati anche i pacchetti MindManager decompressi (una cartella contenente `Document.xml`) e percorsi diretti a `Document.xml`.

### Mente libera (.mm)

I file delle mappe mentali di FreeMind utilizzano l'estensione `.mm` e memorizzano i dati come XML. Marked rileva il formato FreeMind controllando che il contenuto del file inizi con `<map`; in caso contrario (ad esempio, uno snippet di codice), il file viene incluso come testo semplice. I file FreeMind sono supportati per l'incorporamento della mappa mentale della sirena.

###OPML (.opml)

OPML (Outline Processor Markup Language) è un formato XML per profili gerarchici, ampiamente utilizzato da delineatori e lettori di feed. iThoughts e altre app possono esportare in OPML. Le conversioni contrassegnate includevano file OPML in diagrammi della mappa mentale della sirena.

### Bicicletta (.bici)

I contorni di Bike.app sono archiviati come file HTML proprietari (`.bike`). Puoi aprire un file `.bike` direttamente in Marked: il documento viene visualizzato come Markdown con il nome file (meno l'estensione) come intestazione principale (H1), elementi di intestazione di livello superiore come H2, intestazioni nidificate come elementi di elenco in grassetto e attività come caselle di controllo in stile GitHub. Quando un file `.bike` viene incluso tramite la sintassi di inclusione, l'impostazione "Incorpora come diagramma della sirena" per Bici (in App → Mappe mentali/Contorni) controlla se diventa una mappa mentale della sirena (con il nome del file come nodo radice) o un elenco Markdown nidificato (senza H1).

## Incorpora mappe come diagrammi della sirena

Quando **abilitato** (impostazione predefinita), le conversioni contrassegnate includevano mappe mentali e contorni nei diagrammi [Sirena](https://mermaid.js.org/):

**iThoughts, MindManager, FreeMind, OPML e Bike** — Resi come diagrammi di mappe mentali a forma di sirena con il layout ad albero ordinato. Per iThoughts e MindManager, le informazioni sulla forma (arrotondato, rettangolo, esagono, ecc.) vengono conservate ove disponibili. FreeMind (`.mm`) e OPML utilizzano lo stesso formato di mappa mentale. I contorni della bici (`.bike`) utilizzano il nome file incluso (meno l'estensione) come nodo radice della mappa mentale. Le etichette dei nodi sono testo semplice (i collegamenti diventano testo del collegamento; le attività vengono visualizzate come prefissi ☐ / ☑). La sirena è inclusa per impostazione predefinita in ogni anteprima di Markdown.

**Limitazione:** L'incorporamento della mappa mentale (diagrammi Sirena) non funziona con il parser Discount. Utilizza MultiMarkdown, CommonMark (GFM) o Kramdown per le anteprime delle mappe mentali.

Quando **disabilitato**:

- **iThoughts**: l'immagine di anteprima incorporata (`preview.png`) dal file .itmz è incorporata come immagine base64. Il testo alternativo dell'immagine utilizza il nome del file.
- **MindManager**: la struttura è incorporata come elenco Markdown nidificato.
- **FreeMind**: la struttura è incorporata come elenco Markdown nidificato.
- **OPML**: la struttura è incorporata come elenco Markdown nidificato (nessuna mappa mentale).
- **Bici**: il contorno è incorporato come elenco Markdown nidificato (no H1); gli elementi di intestazione di livello superiore diventano H2, le intestazioni nidificate sono in grassetto e le attività diventano caselle di controllo GitHub.

## Includi la sintassi

Utilizzare la stessa sintassi degli altri file include:

	<<[percorso/verso/map.itmz]
	<<[percorso/alla/mappa.mmap]
	<<[percorso/alla/mappa.mm]
	<<[percorso/al/profilo.opml]
	<<[percorso/verso/profilo.bici]

Oppure con la sintassi del blocco iA Writer:

	/percorso/a/map.itmz

I percorsi possono essere relativi al documento principale o assoluti (iniziando con `/` o `~`). Per i dettagli vedere [Documenti multi-file](Multi-File_Documents.html).

## Conversione OPML

I file OPML utilizzano elementi `<outline>` nidificati con un attributo `text`. Quando "Incorpora come diagramma della Sirena" è abilitato (vedi [Impostazioni: App](Settings_Apps.html)), la conversione produce una mappa mentale della Sirena utilizzando lo stesso formato di iThoughts e MindManager:

- I contorni figli di `<body>` diventano il livello superiore (o i figli di una radice "Contorno" se sono presenti più elementi di livello superiore)
- I contorni nidificati definiscono la gerarchia
- Mancante o vuoto `text` viene visualizzato come `(unnamed)`
- Il testo è ripulito; i personaggi speciali vengono scappati per la Sirena

## Conversione bici

I file Bike `.bike` sono HTML con elementi root `<ul>` e `<li>`. Gli elementi possono avere `data-type="heading"` (livello superiore → H2 quando aperto o in modalità elenco; nidificato → grassetto) o `data-type="task"` (caselle di controllo GitHub; completato quando `data-done` ha un timestamp, o `data-checked` / `data-completed` è vero). La formattazione in linea e i collegamenti nel testo del nodo vengono convertiti in Markdown. Quando si incorpora come mappa mentale della Sirena, il nome del file (meno l'estensione) viene utilizzato come singolo nodo radice e le etichette sono testo semplice formattato per la sintassi della mappa mentale della Sirena.