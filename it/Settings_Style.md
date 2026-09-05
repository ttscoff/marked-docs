# <%= @title %>

Le opzioni nel {% prefspane Style %}:

![Impostazioni: Stile][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout e tipografia [layout-and-typography]

Limita larghezza testo nell'anteprima
: Imposta una larghezza massima per il corpo dell'anteprima usando il cursore (in pixel).

Sillabazione automatica nei paragrafi
: Consente alle parole di andare a capo automaticamente tramite la sillabazione.

Evita le righe vedove nei titoli e nei paragrafi
: Forza uno spazio unificatore (non interrompibile) tra le ultime due parole di titoli e paragrafi, per evitare che una singola parola vada a capo da sola.

Genera virgolette e punteggiatura tipograficamente corrette
: Usa SmartyPants per le virgolette intelligenti, la conversione dei puntini di sospensione e altre funzioni tipografiche (MultiMarkdown).

Racchiudi i marcatori delle note a piè di pagina tra parentesi quadre
: Se selezionata, usa la formattazione predefinita di MultiMarkdown per i marcatori delle note a piè di pagina ([1]). Deseleziona per rimuovere le parentesi quadre.

Abilita Struttura per le estensioni
: Attiva automaticamente la modalità Struttura per i file con le estensioni elencate.

Usa lo stile APA
: Usa strutture in stile APA invece del formato Decimale predefinito.

Formatta i blocchi verbatim (codice) come poesia
: Se selezionata, il codice indentato con tabulazioni, delimitato o incluso viene visualizzato come poesia invece che come blocco di codice (senza syntax highlighting, con uno stile speciale a seconda del tema).

Consenti ai temi di mandare a capo il testo nei blocchi di codice
: Se selezionata, i temi possono causare il ritorno a capo all'interno dei blocchi `pre>code`. Se deselezionata, l'overflow orizzontale scorrerà sempre.

Manda sempre a capo il codice
: Forza il ritorno a capo nei blocchi di codice indipendentemente dalle impostazioni del tema (sovrascrive il comportamento di ritorno a capo del tema).

Rileva e formatta il testo RTL
: Rileva la lingua per ogni elemento del documento e applica di conseguenza lo stile da destra a sinistra.

### Tema [theme]

Gestisci stili
: Apre la finestra [Gestione stili](Style_Manager.html). Aggiungi file CSS dal tuo disco per farli comparire nei menu di selezione degli stili. Usa il pulsante `Add New Style` oppure trascina i file CSS in questa finestra. Trascina per riordinare e usa le caselle di controllo per attivare o disattivare gli stili.

Altri temi
: Apre la galleria di temi online per sfogliare e installare stili aggiuntivi.

Stile predefinito
: Lo stile selezionato qui verrà caricato per tutte le nuove finestre, a meno che non sia [indicato uno stile specifico del documento nei metadati](Per-Document_Settings.html) (ad es. "Marked Style: Grump").

Monitora le modifiche al CSS
: Quando questa opzione è attiva, Marked monitorerà lo stile corrente per rilevare modifiche su disco, facilitando la modifica di stili personalizzati e lo sviluppo web.

CSS aggiuntivo
: Il CSS aggiunto qui viene inserito dopo il foglio di stile normale di ogni tema. È una sovrapposizione parziale, non un sostituto completo del tema.
: Marked riscrive i selettori in questo campo (ad esempio, le regole di stampa dovrebbero usare `body.mkprinting #wrapper …`). Non esiste alcun controllo di dimensione o validità --- vedi [Creare CSS personalizzato](Writing_Custom_CSS.html#additional-css-settings).
: Questo si applica a tutti i documenti e a tutti gli stili, incluso l'export HTML quando gli stili sono inclusi. Se vuoi applicare CSS personalizzato ai documenti in base a determinate condizioni, usa Regole personalizzate in {% prefspane Processor %}.

### Includi script [include-scripts]

Syntax Highlighting
: Attiva l'evidenziazione della sintassi di highlight.js per i [blocchi di codice](Syntax_Highlighting.html). Seleziona un tema dal menu a comparsa.
: Se l'opzione **Only if language specified** è selezionata, l'evidenziazione della sintassi verrà applicata solo ai blocchi di codice delimitati (fenced) per cui è stato specificato un linguaggio.

Abilita MathJax
: Carica [MathJax](MathJax.html) per visualizzare le equazioni MathML. Scegli **Locale** (incluso) o **CDN** dal menu a comparsa.
: **Pacchetti aggiuntivi** apre un foglio per includere pacchetti MathJax extra (ad esempio Fisica e Chimica).
: **Configurazione avanzata** apre un foglio per la configurazione personalizzata di MathJax.

Abilita KaTeX
: Carica [KaTeX](MathJax.html#katex) come alternativa a MathJax. È possibile selezionare solo uno dei due.

Numera le equazioni
: Se applicabile, Marked aggiungerà numeri di figura alle equazioni renderizzate. Scegli **Lato sinistro** o **Lato destro** per la numerazione. Se usi MathJax, puoi scegliere **Solo AMS** per numerare solo le equazioni AMS.

Mermaid
: Carica [mermaid.js](https://mermaid.js) da una CDN per abilitare la creazione di diagrammi in stile Markdown. L'hook necessario per il rendering dei diagrammi Mermaid a ogni aggiornamento del documento viene incluso automaticamente.

Panoramica e zoom dei diagrammi
: Quando sono presenti diagrammi Mermaid, abilita lo zoom con {% kbd cmd %}-scroll e la panoramica facendo clic e trascinando.
