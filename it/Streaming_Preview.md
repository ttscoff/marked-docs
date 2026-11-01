<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Aprendo {% appmenu File, New, Streaming Preview %}, Marked riceve aggiornamenti in tempo reale su un tavolo di montaggio con nome invece di guardare un file su disco. L'app di origine deve integrarsi con Marked.

[Curio](Curio.html), [Drafts](Drafts.html) e [The Archive](The_Archive.html) e [Traverse](Traverse.html) documentano i propri interruttori e comandi di menu. nvUltra, nvALT, Bear e altri utilizzano lo stesso canale: apri l'anteprima in streaming in Marked, abilita l'integrazione nel tuo editor e inizia a digitare; gli aggiornamenti arrivano quasi in tempo reale.

## Sviluppatori [developers]

Per integrare l'anteprima in streaming con la tua app, devi solo inserire il testo markdown da visualizzare in anteprima negli appunti con nome. Utilizzare il seguente codice (Objective-C) per aggiornare, preferibilmente su un metodo didEndEditing o a intervalli limitati:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Dichiarare l'app di origine e il formato [declaring-the-origin-app-and-format]

Metti una parola chiave `source` o `format` in un commento HTML all'inizio del testo inviato. Marked legge il commento e lo toglie dall'anteprima, così la nota resta compatibile con i processori GFM e MultiMarkdown. Lo spazio dopo i due punti è facoltativo (`source:Bear.app` e `source: Bear.app` sono uguali) e la parola chiave non distingue maiuscole e minuscole.

Entrambi i valori sono liberi. Marked ha un comportamento integrato per alcuni di essi, e ogni valore è disponibile nel [Custom Processor](Custom_Processor.html) (Conductor) come **Origine dell'anteprima in streaming** e **Formato dell'anteprima in streaming**. Quei criteri accettano **è**, **non è**, **contiene** e **non contiene**.

**`source: APP_NAME`** indica l'app di origine, con il nome dell'app o il bundle id. Marked lo usa per aggiungere una gestione particolare per quell'app. `source: Bear.app` e `source: Drafts.app` attivano il comportamento di anteprima di quelle app. Qualsiasi altro nome può essere confrontato da una regola di Conductor, così puoi eseguire le tue azioni per quell'app:

```html
<!--source:Bear.app-->
```

**`format: fountain`** attiva la gestione di [Fountain](Fountain_for_Screenwriters.html), quindi il flusso viene mostrato come una sceneggiatura invece che come Markdown. Qualsiasi altro valore di formato non cambia il processore. Serve perché una regola di Conductor possa confrontarlo, per esempio **Formato dell'anteprima in streaming** `è` `fountain`.

```html
<!--format:fountain-->
```

Un commento può contenere entrambe le parole chiave:

```html
<!--
source: Bear.app
format: fountain
-->
```

### Apertura dell'anteprima dello streaming in modo programmatico [opening-the-streaming-preview-programatically]

La tua app può aprire l'anteprima dello streaming a livello di codice utilizzando il metodo del gestore URL `x-marked-3://stream/`. Questo metodo accetta anche un parametro `x-success` in cui puoi passare un ID bundle di un'app da attivare al completamento.