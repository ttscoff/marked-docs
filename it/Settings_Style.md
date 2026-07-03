<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Opzioni in {% prefspane Style %}:

![Impostazioni: Stile][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout e tipografia

Limita la larghezza del testo in Anteprima
: imposta una larghezza massima per il corpo dell'anteprima utilizzando il cursore (in pixel).

Sillabazione automatica nei paragrafi
: consente alle parole di interrompersi automaticamente con la sillabazione.

Previeni le vedove nei titoli e nei paragrafi
: forza uno spazio unificatore tra le ultime due parole dei titoli e dei paragrafi per evitare che le singole parole vadano a capo su una nuova riga.

Genera virgolette e punteggiatura tipograficamente corrette
: utilizza SmartyPants per virgolette intelligenti, conversione di ellissi e altre funzionalità tipografiche (MultiMarkdown).

Circondare i marcatori delle note a piè di pagina con parentesi quadre
: se selezionato, utilizza la formattazione MultiMarkdown predefinita per i marcatori delle note a piè di pagina ([1]). Deseleziona per rimuovere le parentesi quadre.

Abilita Outline per le estensioni
: attiva automaticamente la modalità Struttura per i file con le estensioni elencate.

Utilizza lo stile APA
: utilizza contorni in stile APA invece del formato decimale predefinito.

Lo stile letterale (codice) blocca come poesia
: se selezionato, il codice con rientro di tabulazione, delimitato o incluso viene visualizzato come poesia invece che come blocco di codice (nessuna evidenziazione della sintassi e stile speciale a seconda del tema).

Consenti ai temi di racchiudere il testo all'interno di blocchi di codice
: Se selezionato, i temi possono causare il ritorno a capo entro `pre>code` blocchi. Se deselezionato, l'overflow orizzontale scorrerà sempre.

Avvolgi sempre il codice
: forza il ritorno a capo dei blocchi di codice indipendentemente dalle impostazioni del tema (sostituisce il comportamento di ritorno a capo del tema).

Rileva e modella il testo RTL
: rileva la lingua per elemento nel documento e lo stile da destra a sinistra di conseguenza.

### Tema

Gestisci stili
: Apre la finestra [Gestione stili](Style_Manager.html). Aggiungi file CSS dal tuo disco per visualizzarli nei menu di selezione stile. Utilizza il pulsante `Add New Style` o trascina i file CSS in questa finestra. Trascina per riordinare e utilizza le caselle di controllo per abilitare o disabilitare gli stili.

Altri temi
: apre la galleria di temi online per sfogliare e installare stili aggiuntivi.

Stile predefinito
: Lo stile selezionato qui verrà caricato per tutte le nuove finestre, a meno che uno [stile specifico del documento sia indicato nei metadati](Per-Document_Settings.html) (ad esempio "Stile contrassegnato: Grump").

Tieni traccia delle modifiche CSS
: Quando è abilitato, Marked controllerà lo stile corrente per le modifiche del disco, aiutando nella modifica dello stile personalizzato e nello sviluppo web.

CSS aggiuntivi
: I CSS aggiunti qui verranno inclusi dopo il normale foglio di stile con tutti i temi. Tra le altre cose, puoi usarlo per sovrascrivere le impostazioni su tutta la linea senza modificare gli stili interni.
: Questo vale per tutti i documenti e tutti gli stili. Se desideri applicare CSS personalizzati ai documenti in base alle condizioni, utilizza le regole personalizzate in {% prefspane Processor %}.

### Includi script

Evidenziazione della sintassi
: attiva highlight.js [evidenziazione della sintassi](Syntax_Highlighting.html) per i blocchi di codice. Seleziona un tema dal menu a discesa.
: Se è selezionato **Solo se la lingua specificata**, l'evidenziazione della sintassi verrà applicata solo ai blocchi di codice protetti con una lingua specificata.

Abilita MathJax
: Carica [MathJax](MathJax.html) per visualizzare le equazioni MathML. Scegli **Locale** (in bundle) o **CDN** dal menu a discesa.
: **Pacchetti aggiuntivi** apre un foglio per includere pacchetti MathJax aggiuntivi (ad esempio Fisica e Chimica).
: **Configurazione avanzata** apre un foglio per la configurazione personalizzata di MathJax.

Abilita KaTeX
: Carica [KaTeX](Mathjax.html#katex) come alternativa a MathJax. È possibile selezionare solo l'uno o l'altro.

Equazioni numeriche
: Se applicabile, Marked aggiungerà i numeri delle figure alle equazioni renderizzate. Scegli **Lato sinistro** o **Lato destro** per la numerazione. Se utilizzi MathJax, puoi scegliere **Solo AMS** per numerare solo le equazioni AMS.

Sirena
: carica [mermaid.js](https://mermaid.js) da un CDN per abilitare la creazione di diagrammi in stile Markdown. Il gancio richiesto per eseguire il rendering dei diagrammi della Sirena in ogni aggiornamento del documento è incluso automaticamente.

Diagrammi di panoramica e zoom
: Quando sono presenti i diagrammi delle sirene, attiva lo zoom con lo scorrimento di {% kbd cmd %} e la panoramica facendo clic e trascinando.