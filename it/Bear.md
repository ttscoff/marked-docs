<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

[Bear] [bear] può inviare un'anteprima dal vivo direttamente a Marked.

## Invio da Bear [sending-from-bear]

In Bear scegli **Anteprima in Contrassegnato** dal menu **Visualizza** (il testo può variare leggermente in base alla versione di Bear). Marked riceve un TextBundle, quindi le immagini e le risorse incorporate generalmente viaggiano con il testo.

Anche le immagini a cui si fa riferimento con percorsi assoluti o `https` URL vengono risolte purché Marked possa raggiungerle.

## Nota sul Mac App Store [mac-app-store-note]

Se utilizzi la build **Mac App Store** di Marked e macOS continua a chiedere l'autorizzazione per aprire le directory durante l'anteprima da Bear, [contatta il supporto di Marked](http://support.markedapp.com) per un passaggio gratuito all'edizione a download diretto, che evita quel particolare attrito sandbox.

## Tag [tags]

I tag in stile orso possono essere visualizzati come tali attivando **#Il testo è tag** e **Tag stile** sotto {% prefspane Processor %}.

W> Questa impostazione può confondere Marked se scrivi titoli regolari senza spazi dopo `#`.

## Nomi di file ed esportazione [filenames-and-export]

Se attivi **Utilizza il primo H1 come titolo di riserva** in {% prefspane Export %}, quel titolo può guidare il nome del file e il segnaposto `%title` quando stampi o esporti PDF da Marked.

I> Uno stile di anteprima che si avvicina all'aspetto di Bear [è disponibile sumarkedapp.com/styles](https://markedapp.com/styles/preview?style=bear).

L'anteprima dello streaming da Bear è riepilogata nella pagina [Anteprima streaming](Streaming_Preview.html) e in [Ulteriori integrazioni dell'app](Additional_Application_Support.html).

[bear]: https://bear.app/