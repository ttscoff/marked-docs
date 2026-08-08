<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

Contrassegnato consentirà di impostare determinati attributi di un documento nel formato di metadati MultiMarkdown (dettagliato di seguito). Puoi usarli per definire caratteristiche e stili che influiscono solo su quel documento senza alterare le impostazioni predefinite.

La maggior parte delle intestazioni MultiMarkdown vengono ignorate dall'anteprima, ma le seguenti sono consentite e influiscono sul rendering. Puoi includere altri metadati di cui eseguire il rendering nell'output finale, Marked ignorerà semplicemente le chiavi non elencate di seguito. Se salvi come HTML e *non* includi un modello, Marked renderà tutte le chiavi di metadati come previsto.

## Formato dei metadati [metadata-format]

I metadati vengono inseriti nella parte superiore del file Markdown o immediatamente dopo qualsiasi intestazione YAML. Sono costituiti da una chiave, seguita da due punti, spazi o tabulazioni opzionali e dal valore:

	Metadati di esempio: chiave di esempio

Più voci di metadati devono trovarsi su righe separate, ma senza interruzioni di riga tra di esse. L'ultima voce di metadati deve essere seguita da una riga vuota prima dell'inizio del testo del documento.

	Primo: questa è la prima voce di metadati
	Secondo: questa è la seconda voce
	Terzo: l'ultima voce di metadati

	# L'inizio del testo del documento

## Chiavi di metadati contrassegnate [marked-metadata-keys]

### Nascondere i metadati per altri processori [hidingmeta]

**Nota:** se utilizzi un processore personalizzato o pubblichi il tuo Markdown direttamente su una fonte che non elabora questi metadati, puoi comunque utilizzarlo aggiungendo marcatori di commento HTML prima e dopo i metadati. A differenza di MultiMarkdown e di altri processori, Marked individuerà questi tag ovunque nel documento e li elaborerà/rimuoverà dall'output. Pertanto, quanto segue nell'intestazione fornirà i risultati desiderati in Contrassegnato, ma non verrà visualizzato altrove:

	<!--
	Stile contrassegnato: il mio stile personalizzato
	Processore personalizzato: vero
	-->

*Assicurati solo che la chiave dei metadati inizi all'inizio della riga senza spazi o tabulazioni e non inserire nient'altro sulla riga dopo il valore.*

### Stili per documento [per-document-styles]

Il tasto "Stile contrassegnato:" imposterà uno stile di anteprima per il documento. Il valore può essere il nome di uno stile predefinito o un nome o percorso per qualsiasi [Stile personalizzato](Custom_Styles.html) definito nelle impostazioni. Se questa chiave viene trovata e corrisponde a uno stile conosciuto da Marked, quello stile verrà utilizzato per l'anteprima ogni volta che viene caricato il documento che la contiene.

**Esempio**

	Stile contrassegnato: Cittadino onesto

### Linguaggio delle citazioni [quotes-language]

Per impostazione predefinita, Marked utilizza virgolette in stile inglese. Puoi modificarlo in base al documento con il tasto "Lingua virgolette:". Le lingue disponibili sono:

*olandese
* inglese
*francese
*tedesco
* guillemets
*svedese

**Esempio**

	Citazioni Lingua: francese

	Crea «virgolette» in lingua francese.

### Livello di intestazione di base [base-header-level]

È possibile impostare il livello di intestazione da cui Marked inizia a contare con il tasto "Base Header Level:". Dovrebbe essere un numero compreso tra 1 e 6 e modificherà il modo in cui vengono visualizzate le intestazioni "#". Se imposti il livello dell'intestazione su 3, quella che normalmente sarebbe un'intestazione di primo livello (h1) viene renderizzata come un'intestazione di terzo livello (h3) e le intestazioni successive nella gerarchia vengono spostate verso l'alto di 2.

**Esempio**

	Livello intestazione base: 3

	# Questo titolo verrà visualizzato come h3

	## Questo titolo sarà un h4

	Rende come:

	<h3>Questo titolo verrà visualizzato come h3</h3>

	<h4>Questo titolo sarà un h4</h4>

### Processori personalizzati [custom-processors]

Come dettagliato in [Processore personalizzato](Custom_Processor.html#preprocessor), puoi abilitare o disabilitare un processore personalizzato e un preprocessore personalizzato utilizzando i metadati:

    Processore personalizzato: vero
    Preprocessore personalizzato: falso

"true" o "false" attiva e disattiva il pre/processore.

Il valore "Processore" può essere impostato su "multimarkdown" o "sconto" per forzare l'utilizzo dell'uno o dell'altro dei processori interni. Questa impostazione per documento non modificherà l'impostazione predefinita in {% prefspane Processor %}.

### Stampa intestazioni/piè di pagina [print-headersfooters]

Puoi sovrascrivere le impostazioni in {% prefspane Export %} per la stampa di intestazioni e piè di pagina utilizzando i seguenti tasti:

	stampa intestazione a sinistra:
	stampa centro intestazione:
	stampa intestazione a destra:
	stampa piè di pagina a sinistra:
	stampa centro piè di pagina:
	stampa piè di pagina a destra:

Questi possono includere [variabili di stampa](Exporting.html#headers-and-footers) come `%title`, `%page`, `%total`, ecc., nonché riferimenti ad altri metadati utilizzando `%md_[key without spaces]`.

### Margini di stampa [print-margins]

Imposta i margini della pagina per la stampa e l'output PDF impaginato con il tasto `Margins:`. I valori sono in punti; i suffissi come `px`, `pt` e `em` vengono ignorati. Fornisci due numeri per i margini verticali e orizzontali oppure quattro numeri per i margini superiore, destro, inferiore e sinistro:

	Margini: 10 20
	Margini: 10, 20, 10, 20

I margini dei metadati sovrascrivono le impostazioni {% prefspane Export %} e i campi dei margini nel pannello di esportazione PDF.

### Inserimento di JavaScript [inserting-javascript]

Questo metodo specifica i dati inclusi nel tag `<head>` del documento. Marked ignora la maggior parte dei valori per questa chiave, tranne nell'output dell'intero documento, ma rispetterà gli script inclusi in questo modo. I tag di script definiti qui non saranno nell'intestazione, tuttavia verranno aggiunti prima del tag di chiusura `</body>`. jQuery è già caricato e puoi trarne vantaggio in qualsiasi script che inserisci.

**Esempio**

	Intestazione XHTML: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-o-

	Intestazione XHTML: <script src="myfancyscript.js"></script>