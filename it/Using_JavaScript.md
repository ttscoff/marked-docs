<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked utilizza molto JavaScript per fornire le funzionalità offerte nell'anteprima. Per questo motivo possono sorgere non poche complicazioni quando gli script vengono inclusi nel corpo del documento.

## Script esterni

Puoi includere alcuni script esterni utilizzando una riga di metadati "Intestazione CSS:" nella parte superiore del documento. Questi script, tuttavia, verranno inseriti non nell'intestazione, ma nel piè di pagina dopo che gli script di jQuery e Marked sono già stati caricati. Questo è l'ideale nella maggior parte dei casi. Potresti comunque riscontrare un comportamento imprevisto, poiché Marked non è in grado di compensare ogni possibile conflitto di script. Le modifiche al DOM possono essere particolarmente problematiche.

    Intestazione CSS: <script src="file.js"></script>

## Include in linea

Esistono molte applicazioni per visualizzare JavaScript nel corpo di un documento, come generatori di grafici o altri strumenti Canvas. A seconda delle impostazioni di configurazione e del processore che stai utilizzando, questi vengono spesso danneggiati. La soluzione è inserire lo script e gli elementi DOM aggiuntivi in ​​un file esterno e utilizzare la sintassi di Mark per [file di inclusione "raw"] [sintassi]. Questi file non vengono trattati in alcun modo; il loro contenuto viene aggiunto al file una volta completato il resto dell'elaborazione.

    Testo ribassato.

    <<{file.html}

    Altro testo Markdown...

Per sperimentare ed eseguire il debug del JavaScript eseguito nell'anteprima di Marked, puoi collegare il Web Inspector di Safari alla finestra di anteprima utilizzando i passaggi in [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml