<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Il gestore URL di Marked fornisce ulteriori funzionalità di scripting e flusso di lavoro. Puoi includere un URL nelle note di un'altra applicazione, ad esempio, che aprirà un file in Contrassegnato quando viene cliccato. È possibile eseguire diverse azioni, come elencato di seguito.

## Lo schema URL

Lo schema URL di Marked è `x-marked`, chiamato con opzioni come `x-marked://open?file=/Users/username/Desktop/report.md`.

Puoi prendere di mira specificamente Marked 3 usando `x-marked-3` invece di `x-marked`. I metodi e i parametri sono esattamente gli stessi di `x-marked`, ma solo Marked 3 risponderà a `x-marked-3`.

## Chiamata dalla riga di comando/dagli script

È possibile richiamare il gestore URL dalla riga di comando o da uno script utilizzando il [comando `open`](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/) di macOS:

	apri 'x-marked://open?file=nomefile.md'
	apri 'x-marked://refresh?file=nomefile.md'

### Chiamata in sottofondo

Puoi chiamare il comando `open` con il flag `-g` per eseguire il risultato in background senza cambiare focus. Per eseguire il comando in background e alzare la finestra in alto senza togliere il focus:

	open -g 'x-marked://open?file=nomefile.md&raise=true'

## Parametri facoltativi

### x-successo

Qualsiasi comando può fornire un parametro di query **x-success**. Impostalo su un URL da chiamare dopo aver eseguito il comando. Ad esempio: `x-marked://open/?file=filename.md&x-success=ithoughts:`. Puoi anche fornire un identificatore del bundle (come `com.googlecode.iterm`) per aprire un'applicazione che non dispone di uno schema URL.

### rilanciare

Un parametro **raise** può essere passato con qualsiasi comando che accetti un parametro `file` o influisca su tutte le finestre. Una volta eseguita l'azione, le finestre interessate verranno sollevate sopra tutte le altre finestre (tutte le applicazioni) prima di ritornare o eseguire una richiamata.

	"x-marked://refresh?file=nomefile.md&raise=true"

### lettura veloce

Un parametro **speedread** può essere passato con i comandi del gestore URL che aprono un documento di anteprima (`open`, `paste`, `preview` e `stream`). Imposta `speedread=1` per avviare automaticamente la lettura veloce non appena l'anteprima del target è pronta.

Esempi:

	x-marked://open?file=/Users/nomeutente/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	x-marked://paste?speedread=1

# Comandi disponibili

I seguenti comandi sono disponibili per il gestore URL `x-marked`.

## aggiungistile

Aggiungi un nuovo stile personalizzato a Contrassegnato.

##### Parametri:

**css**: testo CSS codificato nell'URL da scrivere in uno stile personalizzato. Obbligatorio a meno che non si passi un parametro **file**.

**file**: percorso completo (POSIX) di un file CSS da aggiungere a Marked. Obbligatorio a meno che non si passi un parametro **css**.

**nome**: il nome dello stile da generare.

Con il parametro **css**, questo verrà utilizzato sia come nome del file durante la scrittura su disco, con l'aggiunta di ".css", sia come nome della voce di menu. È obbligatorio per il parametro **css** e facoltativo per **file** (il nome file verrà utilizzato come se il parametro name fosse vuoto).

	x-marked://addstyle?name=My+new+style&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Se includi un nome con il parametro file, la voce di menu otterrà quel nome invece del nome file. Se utilizzi nuovamente lo stesso nome con un percorso diverso, la voce di menu verrà aggiornata con il nuovo percorso anziché aggiungere una seconda voce con lo stesso nome.

## valori predefiniti

Imposta le Impostazioni utente. Accetta un elenco di chiavi e valori come parametri di query. Verranno impostate solo le chiavi esistenti. Se la modifica delle preferenze richiede un aggiornamento, tutte le finestre si aggiorneranno automaticamente a meno che non venga superato `refresh=0`.

Utilizzare 1 per vero e 0 per falso sui valori booleani.

##### Parametri:

**aggiorna** _(opzionale)_: se impostato su 0, l'aggiornamento automatico delle finestre di anteprima aperte è disabilitato

* Predefinito: 1 (vero)

##### Esempio:

x-marked://defaults?syntaxHighlight=1&includeMathJax=0

Il metodo `defaults` è progettato principalmente in modo che lo sviluppatore possa aggiungere collegamenti a funzionalità esoteriche che altrimenti potrebbero non essere disponibili nelle Impostazioni. Tuttavia, potrebbero esserci alcune opzioni standard che vorresti attivare durante l'automazione. Alcune impostazioni comuni che potresti voler controllare durante l'automazione:

syntaxHighlight
: attiva o disattiva l'evidenziazione della sintassi

includeMathJax
: abilita o disabilita la gestione interna di MathJax

processore
: imposta su `multimarkdown` o `mmd` per cambiare il processore in MultiMarkdown, `discount` o `gfm` per utilizzare il processore Discount

h1IsPageBreak, h1IsPageBreak, breakBeforeFootnotes
: interruzioni di pagina automatiche nell'esportazione prima dei livelli di intestazione 1 e 2 e note a piè di pagina.


## dingo

Apri Markdown Dingus per testare diversi processori Markdown.

	x-contrassegnato://dingus

##### Parametri:

**processore** (opzionale): specifica quale processore selezionare per impostazione predefinita. Valori validi:

- `multimarkdown` - Processore MultiMarkdown
- `commonmark` - Processore CommonMark (GFM).
- `discount` o `discount (gfm)` - Processore di sconto
- `kramdown` - Processore Kramdown

Esempi:

- `x-marked://dingus?processor=kramdown` - Si apre con Kramdown selezionato
- `x-marked://dingus?processor=commonmark` - Si apre con CommonMark (GFM) selezionato

*Nota:* Si apre la finestra Markdown Dingus, che consente di testare e confrontare diversi processori Markdown (MultiMarkdown, CommonMark (GFM), Discount e Kramdown) fianco a fianco. Perfetto per sperimentare la sintassi Markdown e comprendere le differenze del processore.

## stylestealer / ruba

Apri l'HUD di Style Stealer. Utile quando desideri acquisire CSS da una pagina live o eseguire una sessione di estrazione manuale del contenuto senza avviarla tramite l'interfaccia utente.

	Sinonimi: x-marked://stylestealer … , x-marked://steal …

##### Parametri:

**url** _(facoltativo)_: un URL da precompilare nella finestra Style Stealer. Se omesso, l'HUD si apre vuoto.

Esempi:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl/markdownify

Apri la finestra "Importa URL" (Estrattore contenuto) in modo da poter eseguire manualmente la pipeline Markdownifier. Questo **non** esegue l'estrazione automaticamente, che viene gestita dal comando `extract` riportato di seguito.

	Sinonimi: x-marked://importurl … , x-marked://markdownify …

##### Parametri:

**url** _(facoltativo)_: precompila il campo URL di importazione. Se omesso, la finestra si apre con un campo vuoto in attesa che tu incolli un collegamento.
**html** _(facoltativo, solo markdownify)_: se fornito su `x-marked://markdownify`, deve essere HTML non elaborato con codifica URL. Marked convertirà l'HTML in Markdown utilizzando le stesse regole dell'Anteprima degli Appunti e lo aprirà in un documento temporaneo, come se avessi incollato l'HTML in una finestra di Anteprima degli Appunti.

Esempi:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## fallo

Esegui un comando JavaScript in una finestra del documento. L'intera API JavaScript di Marked è [documentata qui](https://markedapp.com/help/jsapi/).

##### Parametri:

**js** _(obbligatorio)_: stringa di query contenente un comando JavaScript

* Accetta parametri di percorso che fanno riferimento a nomi di file o "tutti"
* I percorsi divisi per / cercheranno più file
* I nomi file parziali completeranno la migliore corrispondenza

		x-marked://do/nomefile1/nomefile2?js=...
		x-marked://do/all?js=...

**file**: parametro di query contenente percorsi/nomi file separati da virgole

	x-marked://do?file=nomefile1,nomefile2&js=...

Funzionerà sulla finestra in primo piano se non viene fornito un nome file (o non viene passato "tutto")

##aiuto

Aprire il sistema di guida interno Marked, specificando facoltativamente un argomento. Questo è principalmente per uso interno, ma accessibile tramite URL. È possibile copiare l'URL di una determinata sezione facendo clic con il pulsante destro del mouse sull'icona del segnalibro a destra del titolo e selezionando __Copia collegamento__. La guida e la ricerca in-app di **Marked 3** utilizzano lo schema `x-marked-3` per questi collegamenti in modo che macOS li apra in Marked 3 quando è installato anche Marked 2; gli esempi seguenti utilizzano questo formato.

##### dingo

Apri Markdown Dingus per testare diversi processori Markdown.

	x-contrassegnato://dingus

######## Parametri:

**processore** (opzionale): specifica quale processore selezionare per impostazione predefinita. Valori validi:

- `multimarkdown` - Processore MultiMarkdown
- `commonmark` - Processore CommonMark (GFM).
- `discount` o `discount (gfm)` - Processore di sconto
- `kramdown` - Processore Kramdown

Esempi:

- `x-marked://dingus?processor=kramdown` - Si apre con Kramdown selezionato
- `x-marked://dingus?processor=commonmark` - Si apre con CommonMark (GFM) selezionato

*Nota:* Si apre la finestra Markdown Dingus, che consente di testare e confrontare diversi processori Markdown (MultiMarkdown, CommonMark (GFM), Discount e Kramdown) fianco a fianco. Perfetto per sperimentare la sintassi Markdown e comprendere le differenze del processore.

##### Parametri:

**pagina** _(facoltativo)_: il titolo esatto di una pagina esistente, con hash di ancoraggio opzionale

	x-marked-3://help?page=Document_Statistics

Gli spazi vengono sostituiti con caratteri di sottolineatura, secondo la convenzione di denominazione dei file della guida Marked. È possibile utilizzare i due punti (:) al posto del cancelletto (#) quando si specifica un'ancora.

La destinazione può essere specificata solo dal percorso (senza stringa di query):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## estratto

Estrai il contenuto da un URL Web e aprilo come nuovo documento in Marked.

	x-marked://extract?url=https://example.com

##### Parametri:

**url** _(obbligatorio)_: l'URL web da cui estrarre il contenuto. Deve iniziare con `http://` o `https://`

**finestra** _(facoltativo)_: nome della finestra

**id** _(facoltativo)_: identificatore dello spazio dei nomi

**base** _(opzionale)_: URL di base per i collegamenti relativi

**alza** _(opzionale)_: imposta su `true` per alzare la finestra dopo l'apertura

**manuale** _(opzionale)_: imposta su `true` per aprire la finestra di estrazione manuale di Style Stealer invece di eseguire l'estrazione automatica.

- Quando `manual=true`, Marked apre Style Stealer, precompila il campo URL (se fornito), sopprime qualsiasi finestra di dialogo Apri automatica e consente di selezionare ed estrarre in modo interattivo stili/contenuti prima di salvare.
- Se omesso o `false`, Marked esegue l'estrattore automatico (Markdownifier) ​​e apre il risultato direttamente come un nuovo documento temporaneo.

##### Esempi:

	x-marked://extract?url=https://news.ycombinator.com

	x-marked://extract?url=https://github.com&window=GitHub&raise=true

	x-marked://extract?url=https://example.com/article&manual=true

	x-marked://extract?url=https://blog.example.com/post-title

*Nota:* questo comando utilizza il servizio di estrazione dei contenuti di Marked per recuperare pagine Web, estrarre contenuti puliti utilizzando Leggibilità, convertirli nel formato Markdown e aprire il risultato in un nuovo documento temporaneo. Il contenuto estratto include metadati (titolo, URL di origine, data) ed è formattato come Markdown pulito. Perfetto per acquisire e modificare rapidamente contenuti web.

## aperto

Apre il documento specificato in Contrassegnato.

	x-marked://open?file=/Users/nomeutente/Desktop/report.md

##### Parametri:

**file** *(obbligatorio)*: il percorso POSIX completo del documento da aprire o un elenco di percorsi separati da virgole

**speedread** *(opzionale)*: imposta su `1` per avviare automaticamente la lettura veloce dopo l'apertura.

`open` accetta anche un percorso i cui componenti verranno combinati in un unico URL

	x-marked://open/~/nvALT2.2

Se il percorso del file fornito non esiste o non può essere aperto, Marked verrà comunque in primo piano. L'esecuzione senza il parametro *file* o con un valore vuoto aprirà semplicemente Marked.

Contrassegnato aprirà i file anche se sul gestore URL viene chiamato solo il percorso di un file, ad es. `x-marked:///Users/username/Desktop/report.md`.

## incolla

Crea un nuovo documento dal contenuto corrente degli appunti.

	x-contrassegnato://paste

##### Parametri:

**speedread** *(opzionale)*: imposta su `1` per avviare automaticamente la lettura veloce dopo aver aperto l'anteprima degli appunti.

*Nota:* Questo crea un documento temporaneo utilizzando il comando "Anteprima Appunti". Qualsiasi testo negli appunti viene aggiunto a un nuovo documento vuoto, che viene quindi aperto in Contrassegnato. Se chiuso senza salvare, viene scartato.

##anteprima

Visualizza l'anteprima del testo specificato in un nuovo documento.

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parametri:

**testo** *(obbligatorio)*: il testo da inserire nell'anteprima. Il testo codificato in percentuale non verrà codificato prima della visualizzazione del documento.

**speedread** *(opzionale)*: imposta su `1` per avviare automaticamente la lettura veloce dopo aver aperto il testo di anteprima.

## flusso

Apri una finestra di anteprima degli appunti in streaming.

	x-contrassegnato://stream

##### Parametri:

**speedread** *(opzionale)*: imposta su `1` per avviare automaticamente la lettura veloce dopo aver aperto l'anteprima dello streaming.

*Nota:* Questo crea un documento temporaneo utilizzando il comando "Anteprima Appunti". Il testo passato viene aggiunto a un nuovo documento vuoto, che viene quindi aperto in Contrassegnato. Se chiuso senza salvare, viene scartato.

## aggiorna

Aggiorna l'anteprima di un documento o tutte le anteprime aperte.

##### Parametri:

**file**: parametro di query contenente percorsi/nomi file separati da virgole (i file devono essere attualmente aperti in Contrassegnato). La chiamata senza il parametro `file` o `?file=all` aggiornerà tutte le finestre aperte.

Il parametro *file* può essere parziale, Marked aggiornerà tutte le finestre aperte con una corrispondenza parziale nel *nomefile* (non nel percorso completo). Passando "all" si aggiorneranno tutte le finestre.

	x-contrassegnato://refresh

	x-marked://refresh?file=/Users/nomeutente/Desktop/report.md

	x-marked://refresh?file=report.md

Se chiamato senza il parametro `file` ma i percorsi dei documenti specificati nell'URL, i percorsi suddivisi per / cercheranno più file e i nomi file parziali completeranno la corrispondenza migliore.

	x-marked://refresh/nomefile1/nomefile2

##stile

Imposta lo stile di anteprima (CSS) per uno o più documenti.

##### Parametri:

**css** _(richiesto)_: stringa di query contenente il nome o il percorso di uno stile. Gli stili devono essere presenti nel menu Stile di Marked come stili personalizzati predefiniti o aggiunti manualmente.

* Accetta parametri di percorso che fanno riferimento a nomi di file o "tutti"
* I percorsi divisi per / cercheranno più file
* I nomi file parziali completeranno la migliore corrispondenza

		x-marked://stile/nomefile1/nomefile2?css=...
		x-marked://style/all?css=...

**file**: parametro di query contenente percorsi/nomi file separati da virgole

	x-marked://style?file=nomefile1,nomefile2&css=...

Questo metodo funzionerà sulla finestra in primo piano se non viene fornito un nome file (o non viene passato "tutto").