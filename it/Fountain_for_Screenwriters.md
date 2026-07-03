<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Fountain](http://fountain.io/) è un linguaggio di markup di testo specializzato progettato per scrivere sceneggiature. Gli sceneggiatori che scrivono utilizzando la sintassi di Fountain possono utilizzare Marked per visualizzare in anteprima il proprio lavoro. 

L'apertura di qualsiasi file con estensione ".fountain" abiliterà automaticamente il supporto Fountain per la finestra. Verrà applicato un foglio di stile Fountain predefinito per l'anteprima e l'esportazione.

Puoi forzare l'elaborazione di qualsiasi documento come Markdown aprendo il menu Ingranaggio in basso a destra nella finestra di anteprima e selezionando **Elabora come Fountain**.

Le intestazioni delle sezioni e delle scene verranno visualizzate nel sommario per una rapida navigazione nella sceneggiatura.

## Script

Puoi anche utilizzare "script" in un documento normale per elaborare e stilizzare singole sezioni con Fountain. Circonda semplicemente il markup Fountain all'interno del documento principale con i tag `[scrippet]`:

    [copione]
    Il testo della tua sceneggiatura...
    [/scritto]

Puoi anche utilizzare i tag standard in stile Marked:

    <!--SCRIPPET-->
    Il testo della tua sceneggiatura...
    <!--/SCRIPPET-->