# <%= @title %>

Door {% appmenu File, New, Streaming Preview %} te openen, ontvangt Marked live updates via een benoemd plakbord in plaats van een bestand op schijf te bekijken. De bron-app moet integreren met Marked.

[Curio](Curio.html), [Drafts](Drafts.html) en [The Archive](The_Archive.html) documenteren hun eigen schakelaars en menuopdrachten. nvUltra, nvALT, Bear en anderen gebruiken hetzelfde kanaal: open streaming preview in Marked, schakel integratie in uw editor in en begin met typen; updates arriveren bijna in realtime.

## Ontwikkelaars

Om het streamingvoorbeeld met uw app te integreren, hoeft u alleen maar de markdown-tekst op een benoemd klembord te plaatsen. Gebruik de volgende code (Objective-C) om bij te werken, bij voorkeur via een didEndEditing-methode of met beperkte intervallen:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Een basis-URL declareren voor relatieve assets

U kunt ook een basis-URL opgeven voor het streamingvoorbeeld, zodat relatieve URL's in afbeeldingen en andere elementen kunnen functioneren zoals in de bron-app. Als de basis-URL een bestandsnaam bevat, worden de naam en extensie ervan beschikbaar gemaakt voor aangepaste verwerkers, maar dit is niet verplicht. Om de basis-URL op te nemen, plaatst u eenvoudigweg een NSURL-object op het klembord:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Of in Swift:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Als de Mac App Store-versie van Marked wordt gebruikt en de baseURL niet toegankelijk is via sandboxing, wordt om toestemming gevraagd de eerste keer dat de URL in de preview wordt geladen.

### De brontoepassing declareren

Apps kunnen zichzelf ook aangeven als de bron van de voorbeeldinhoud door een `source` metadataregel op te nemen. Dit wordt doorgaans gedaan binnen een HTML opmerking om compatibiliteit met zowel GFM- als MultiMarkdown-processors mogelijk te maken. Vermeld eenvoudig de naam van de app of het bundel-ID:

```html
<!--
source: Bear.app
-->
```

### Het streamingvoorbeeld programmatisch openen

Uw app kan het streamingvoorbeeld programmatisch openen met behulp van de `x-marked-3://stream/` url-handlermethode. Deze methode accepteert ook een `x-success` parameter waarin u een bundel-ID van een app kunt doorgeven om deze na voltooiing te activeren.