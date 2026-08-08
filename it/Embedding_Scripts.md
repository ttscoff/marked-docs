<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Esistono diversi modi per incorporare JavaScript aggiuntivi in Marked.

## Incluso JavaScript per documento [including-javascript-per-document]

Puoi includere script in un singolo documento utilizzando `<script>` tag nel contenuto stesso. Questo può essere utile per librerie come [D3](https://d3js.org/) per visualizzazioni di dati necessarie solo in documenti specifici:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Se utilizzi MultiMarkdown come processore, puoi includere script nei metadati e verranno inseriti nel documento. Poiché Marked restituisce solo "snippet", la chiave `XHTML Header` non è l'ideale. Usa invece `CSS Header` e gli script verranno inseriti nella parte inferiore del documento.

	Intestazione CSS: <script src="file.js"></script>

Per fare in modo che gli script inclusi si aggiornino quando il contenuto cambia, vedere [Hooks](#hooks).

## Incluso JavaScript [including-javascript]

Puoi includere il tuo JavaScript da file locali, CDN o incollando il codice non elaborato. Per accedervi, apri {% prefspane Style %} e fai clic sul pulsante *Regole personalizzate*.

Imposta una nuova regola personalizzata o aggiungi script a una esistente. Per aggiungere script a ogni file, impostare il predicato su "il nome del file contiene *".

L'editor delle azioni per una regola personalizzata dispone di tre opzioni per includere gli script:

Inserisci il file JavaScript
: consente di selezionare un file locale da inserire alla fine del documento

Inserisci JavaScript dall'URL
: consente di includere un CDN o un altro URL remoto, che creerà un tag `<script>` alla fine del documento con l'URL collegato

Inserisci JavaScript
: apre un editor di codice in cui puoi scrivere/incollare il tuo codice JavaScript

Questi script verranno inseriti alla fine dell'anteprima, prima del tag del documento. Se hai bisogno di chiamare una funzione init o aggiornare ogni volta che l'anteprima si aggiorna, vedi [Incluso JavaScript Raw](Embedding_Scripts.html#hooks) e familiarizza con gli [hook](#hooks) di Marked.

## Sirena e altri script [mermaid]

jQuery è incluso per impostazione predefinita e puoi utilizzarlo in qualsiasi script che aggiungi a Marked utilizzando uno dei metodi seguenti.

[Sirena](https://mermaid.js.org/intro/) per i diagrammi simili a Markdown è ora incluso per impostazione predefinita in ogni documento. Qualsiasi blocco di codice recintato con la lingua `mermaid` verrà automaticamente visualizzato come diagramma.

Nella parte inferiore di {% prefspane Style %}, una casella di controllo per "Diagrammi panoramica e zoom" è disponibile quando è presente il contenuto della Sirena. Selezionando questa casella, i diagrammi verranno ingranditi con lo scorrimento di {% kbd cmd %} e verranno spostati facendo clic e trascinando. Lo script per questa funzionalità è incluso da una CDN e richiede una connessione Internet.

Se c'è una libreria particolare che vorresti vedere inclusa per impostazione predefinita, faccelo sapere sul [forum BrettTerpstra.com](https://forum.brettterpstra.com/) o tramite [il sito di supporto](https://support.markedapp.com/questions/add).

## Ganci [hooks]

A partire dalle versioni recenti, Marked non esegue più un aggiornamento completo della pagina durante l'aggiornamento del contenuto, ma piuttosto inserisce il nuovo contenuto nel DOM senza richiedere il caricamento della pagina. Ciò significa che gli script inclusi che si attivano al caricamento della pagina non verranno attivati ​​nuovamente quando il contenuto viene aggiornato. Marked fornisce una funzione "ganci" per soddisfare questo problema. Per registrare un hook, devi includere un secondo blocco di script che chiama la [`Marked.hooks.register()` funzione](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), che accetta un trigger, in questo caso 'update', e una funzione da eseguire.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

Tutte le [funzionalità API](https://markedapp.com/jsapi/) di Marked possono essere utilizzate in questo campo. (Puoi anche utilizzare l'API in qualsiasi script caricato.) Per il debug interattivo e la sperimentazione con l'API in un'anteprima dal vivo, consulta la sezione [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) per i dettagli sull'utilizzo del menu Sviluppo di Safari con Marked.

Ora, ogni volta che viene eseguito un aggiornamento (ogni volta che il file sorgente guardato viene salvato), verrà eseguita la funzione passata. Finché lo script che stai eseguendo ha una funzione init o render di qualche tipo, puoi chiamarlo con un hook e visualizzarlo ogni volta che il documento viene salvato e viene attivato un aggiornamento.



*[CDN]: Rete di distribuzione dei contenuti