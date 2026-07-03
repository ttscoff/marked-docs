<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Aprendo {% appmenu File, New, Streaming Preview %}, Marked riceve aggiornamenti in tempo reale su un tavolo di montaggio con nome invece di guardare un file su disco. L'app di origine deve integrarsi con Marked.

[Curio](Curio.html), [Drafts](Drafts.html) e [The Archive](The_Archive.html) documentano i propri interruttori e comandi di menu. nvUltra, nvALT, Bear e altri utilizzano lo stesso canale: apri l'anteprima in streaming in Marked, abilita l'integrazione nel tuo editor e inizia a digitare; gli aggiornamenti arrivano quasi in tempo reale.

## Sviluppatori

Per integrare l'anteprima in streaming con la tua app, devi solo inserire il testo markdown da visualizzare in anteprima negli appunti con nome. Utilizzare il seguente codice (Objective-C) per aggiornare, preferibilmente su un metodo didEndEditing o a intervalli limitati:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Dichiarare un URL di base per le risorse relative

Puoi anche fornire un URL di base per l'anteprima dello streaming, consentendo agli URL relativi nelle immagini e in altre risorse di funzionare come farebbero nell'app di origine. Se l'URL di base include un nome file, il nome e l'estensione verranno resi disponibili ai processori personalizzati, ma non è obbligatorio farlo. Per includere l'URL di base, inserisci semplicemente un oggetto NSURL negli appunti:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Oppure in Swift:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Se viene utilizzata la versione di Marked del Mac App Store e baseURL non è accessibile tramite sandboxing, verrà richiesta l'autorizzazione la prima volta che l'URL viene caricato nell'anteprima.

### Dichiarazione dell'applicazione sorgente

Le app possono anche dichiararsi come fonte del contenuto di anteprima includendo una riga di metadati `source`. Ciò verrà solitamente eseguito all'interno di un commento HTML per consentire la compatibilità con entrambi i processori GFM e MultiMarkdown. Indica semplicemente il nome dell'app o l'ID del pacchetto:

```html
<!--
source: Bear.app
-->
```

### Apertura dell'anteprima dello streaming in modo programmatico

La tua app può aprire l'anteprima dello streaming a livello di codice utilizzando il metodo del gestore URL `x-marked-3://stream/`. Questo metodo accetta anche un parametro `x-success` in cui puoi passare un ID bundle di un'app da attivare al completamento.