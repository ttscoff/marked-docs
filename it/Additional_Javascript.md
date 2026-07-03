<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Puoi includere il tuo JavaScript dai CDN o incollando il codice non elaborato.

## Una nota sul conduttore contrassegnato

Il modo più semplice per implementare JavaScript personalizzato che varia a seconda dei tipi di documenti e delle posizioni è con [Marked Conductor][conductor]. Ti consente di utilizzare una configurazione YAML per aggiungere script utilizzando "filtri". Controlla la [pagina del conduttore] [conduttore] per i dettagli e consulta la [configurazione di esempio] [configurazione di esempio] per gli esempi.

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## Aggiunta di JavaScript dai CDN [cdns]

![][1]

   [1]: images/screenshots/AdditionalJavascript.jpg @2x larghezza=592px altezza=576px classe=centro

Puoi aggiungere URL CDN JavaScript nella finestra "Script aggiuntivi", accessibile da {% prefspane Style %}. Inserisci gli URL CDN, uno per riga. Non includere alcun tag `<script>`, solo l'URL:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> Nota che jQuery è già incluso nella finestra di anteprima.

Questi script verranno inseriti alla fine dell'anteprima, prima del tag del documento. Se è necessario chiamare una funzione init o aggiornarla ogni volta che viene eseguita l'anteprima, vedere [Incluso JavaScript non elaborato](#rawjs). Per ispezionare il DOM ed eseguire il debug di questi script in un'anteprima contrassegnata dal vivo, puoi allegare l'ispettore Web di Safari come descritto in [Ispettore WebKit](Writing_Custom_CSS.html#webkitinspector).


### Incluso JavaScript non elaborato [rawjs]

Nel campo di testo inferiore della finestra Script aggiuntivi, puoi inserire JavaScript non elaborato. Questo sarà incluso all'interno di una coppia `<script></script>`, quindi non includerlo nell'input. Questo campo può contenere qualsiasi comando JavaScript necessario per inizializzare una libreria inclusa, eseguire modifiche DOM o qualsiasi cosa tu voglia fare all'interno di una visualizzazione WebKit. jQuery è già incluso per comodità di manipolazione del DOM.

Questi script verranno eseguiti solo al primo caricamento della finestra. Quando l'anteprima si aggiorna, lo fa sostituendo parti del DOM, quindi gli script che devono agire sul contenuto aggiornato dovrebbero farlo utilizzando [Hooks](Embedding_Scripts.html#hooks).

Includi nel campo JavaScript grezzo una chiamata come questa:

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
