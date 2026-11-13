# <%= @title %>

Door {% appmenu File, New, Streaming Preview %} te openen, ontvangt Marked live updates via een benoemd plakbord in plaats van een bestand op schijf te bekijken. De bron-app moet integreren met Marked.

[Curio](Curio.html), [Drafts](Drafts.html) en [The Archive](The_Archive.html) en [Traverse](Traverse.html) documenteren hun eigen schakelaars en menuopdrachten. nvUltra, nvALT, Bear en anderen gebruiken hetzelfde kanaal: open streaming preview in Marked, schakel integratie in uw editor in en begin met typen; updates arriveren bijna in realtime.

## Ontwikkelaars [developers]

Om het streamingvoorbeeld met uw app te integreren, hoeft u alleen maar de markdown-tekst op een benoemd klembord te plaatsen. Gebruik de volgende code (Objective-C) om bij te werken, bij voorkeur via een didEndEditing-methode of met beperkte intervallen:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### De herkomst-app en de indeling aangeven [declaring-the-origin-app-and-format]

Zet een trefwoord `source` of `format` in een HTML-commentaar bovenaan de verstuurde tekst. Marked leest het commentaar en haalt het uit het voorbeeld, zodat de notitie compatibel blijft met GFM- en MultiMarkdown-processors. Een spatie na de dubbele punt is optioneel (`source:Bear.app` en `source: Bear.app` zijn hetzelfde), en het trefwoord negeert hoofdletters.

Beide waarden zijn vrije tekst. Voor een paar ervan heeft Marked ingebouwd gedrag, en elke waarde is beschikbaar in de [Custom Processor](Custom_Processor.html) (Conductor) als **Bron van streamingvoorbeeld** en **Formaat van streamingvoorbeeld**. Die criteria accepteren **is**, **is niet**, **bevat** en **bevat niet**.

**`source: APP_NAME`** noemt de herkomst-app, met de appnaam of de bundle id. Marked gebruikt dat om een speciale behandeling voor die app toe te voegen. `source: Bear.app` en `source: Drafts.app` zetten het voorbeeldgedrag van die apps aan. Elke andere naam kan nog steeds door een Conductor-regel worden vergeleken, zodat je je eigen acties voor die app kunt uitvoeren:

```html
<!--source:Bear.app-->
```

**`format: fountain`** zet de [Fountain](Fountain_for_Screenwriters.html)-behandeling aan, zodat de stroom als een scenario wordt getoond in plaats van als Markdown. Elke andere formaatwaarde verandert de processor niet. Die is er zodat een Conductor-regel hem kan vergelijken, bijvoorbeeld **Formaat van streamingvoorbeeld** `is` `fountain`.

```html
<!--format:fountain-->
```

Eén commentaar kan beide trefwoorden bevatten:

```html
<!--
source: Bear.app
format: fountain
-->
```

### Het streamingvoorbeeld programmatisch openen [opening-the-streaming-preview-programatically]

Uw app kan het streamingvoorbeeld programmatisch openen met behulp van de `x-marked-3://stream/` url-handlermethode. Deze methode accepteert ook een `x-success` parameter waarin u een bundel-ID van een app kunt doorgeven om deze na voltooiing te activeren.