<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Le mappe mentali e i contorni possono essere incorporati nell'anteprima di Markdown utilizzando la [sintassi di inclusione di Marked] [include] o la [sintassi del blocco IA Writer] [ia]. Il comportamento dipende dal formato del file e dall'impostazione "Incorpora mappe come diagrammi della sirena" in {% prefspane Apps %} in *Mappe mentali/Contorni*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Formati supportati [supported-formats]

### iPensieri X (.itmz) [ithoughts-x-itmz]

I file delle mappe mentali di iThoughts sono archivi zip contenenti dati della mappa e un'immagine di anteprima opzionale.

### MindManager (.mmap) [mindmanager-mmap]

I file MindManager sono archivi zip contenenti `Document.xml`. Sono supportati anche i pacchetti MindManager decompressi (una cartella contenente `Document.xml`) e percorsi diretti a `Document.xml`.

### Mente libera (.mm) [freemind-mm]

I file delle mappe mentali di FreeMind utilizzano l'estensione `.mm` e memorizzano i dati come XML. Marked rileva il formato FreeMind controllando che il contenuto del file inizi con `<map`; in caso contrario (ad esempio, uno snippet di codice), il file viene incluso come testo semplice. I file FreeMind sono supportati per l'incorporamento della mappa mentale della sirena.

###OPML (.opml)

OPML (Outline Processor Markup Language) è un formato XML per profili gerarchici, ampiamente utilizzato da delineatori e lettori di feed. iThoughts e altre app possono esportare in OPML. Le conversioni contrassegnate includevano file OPML in diagrammi della mappa mentale della sirena.

### Bike (.bike) [bike-bike]

Vedi [Bike](Bike.html) per aprire un file `.bike`. Le strutture Bike incluse seguono la casella **Bike outlines**: attiva, una mappa mentale Mermaid (il nome del file, senza `.bike`, è il nodo radice); disattiva, un elenco Markdown nidificato senza titolo del documento.

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

Vedi [Tree Outliner](Tree_Outliner.html). La casella **Tree Outliner outlines** controlla sia l'apertura di un file `.treeoutline` sia l'inclusione. Attiva, disegna una mappa mentale Mermaid con il titolo del documento come radice. Disattiva, compila titoli ed elenchi; **Headings through level** nel gruppo *Tree Outliner* stabilisce fino a che livello arrivano i titoli.

## Incorpora mappe come diagrammi della sirena [embed-maps-as-mermaid-diagrams]

Quando **abilitato** (impostazione predefinita), le conversioni contrassegnate includevano mappe mentali e contorni nei diagrammi [Sirena](https://mermaid.js.org/):

**iThoughts, MindManager, FreeMind, OPML e Bike** — Resi come diagrammi di mappe mentali a forma di sirena con il layout ad albero ordinato. Per iThoughts e MindManager, le informazioni sulla forma (arrotondato, rettangolo, esagono, ecc.) vengono conservate ove disponibili. FreeMind (`.mm`) e OPML utilizzano lo stesso formato di mappa mentale. I contorni della bici (`.bike`) utilizzano il nome file incluso (meno l'estensione) come nodo radice della mappa mentale. Le etichette dei nodi sono testo semplice (i collegamenti diventano testo del collegamento; le attività vengono visualizzate come prefissi ☐ / ☑). La sirena è inclusa per impostazione predefinita in ogni anteprima di Markdown.

**Limitazione:** L'incorporamento della mappa mentale (diagrammi Sirena) non funziona con il parser Discount. Utilizza MultiMarkdown, CommonMark (GFM) o Kramdown per le anteprime delle mappe mentali.

Quando **disabilitato**:

- **iThoughts**: l'immagine di anteprima incorporata (`preview.png`) dal file .itmz è incorporata come immagine base64. Il testo alternativo dell'immagine utilizza il nome del file.
- **MindManager**: la struttura è incorporata come elenco Markdown nidificato.
- **FreeMind**: la struttura è incorporata come elenco Markdown nidificato.
- **OPML**: la struttura è incorporata come elenco Markdown nidificato (nessuna mappa mentale).
- **Bici**: il contorno è incorporato come elenco Markdown nidificato (no H1); gli elementi di intestazione di livello superiore diventano H2, le intestazioni nidificate sono in grassetto e le attività diventano caselle di controllo GitHub.

## Includi la sintassi [include-syntax]

Utilizzare la stessa sintassi degli altri file include:

	<<[percorso/verso/map.itmz]
	<<[percorso/alla/mappa.mmap]
	<<[percorso/alla/mappa.mm]
	<<[percorso/al/profilo.opml]
	<<[percorso/verso/profilo.bici]
	<<[path/to/outline.treeoutline]

Oppure con la sintassi del blocco iA Writer:

	/percorso/a/map.itmz

I percorsi possono essere relativi al documento principale o assoluti (iniziando con `/` o `~`). Per i dettagli vedere [Documenti multi-file](Multi-File_Documents.html).

## Conversione OPML [opml-conversion]

I file OPML utilizzano elementi `<outline>` nidificati con un attributo `text`. Quando "Incorpora come diagramma della Sirena" è abilitato (vedi [Impostazioni: App](Settings_Apps.html)), la conversione produce una mappa mentale della Sirena utilizzando lo stesso formato di iThoughts e MindManager:

- I contorni figli di `<body>` diventano il livello superiore (o i figli di una radice "Contorno" se sono presenti più elementi di livello superiore)
- I contorni nidificati definiscono la gerarchia
- Mancante o vuoto `text` viene visualizzato come `(unnamed)`
- Il testo è ripulito; i personaggi speciali vengono scappati per la Sirena

## Conversione bici [bike-conversion]

I file Bike `.bike` sono HTML con una `<ul>` radice ed elementi `<li>`. In modalità elenco, ogni riga è un elemento di elenco: le righe `data-type="heading"` sono in grassetto e le righe `data-type="task"` sono caselle GitHub (spuntate quando `data-done` ha un orario, o quando `data-checked` / `data-completed` è vero). La formattazione e i link nel testo del nodo diventano Markdown. Aprire un file `.bike` usa sempre questo elenco. Quando un file incluso è incorporato come mappa mentale Mermaid, il nome del file (senza estensione) è l'unico nodo radice e le etichette sono testo semplice per la sintassi mindmap di Mermaid.
