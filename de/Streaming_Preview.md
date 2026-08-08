# <%= @title %>

Durch Öffnen von {% appmenu Ablage, Neu, Streaming-Vorschau %} erhält Marked Live-Updates über eine benannte Zwischenablage, anstatt eine Datei auf der Festplatte zu überwachen. Die Quell-App muss in Marked integriert werden.

[Curio](Curio.html), [Drafts](Drafts.html) und [The Archive](The_Archive.html) dokumentieren ihre eigenen Einstellungen und Menübefehle. nvUltra, nvALT, Bear und andere nutzen einen gemeinsamen Weg: Öffnen Sie die Streaming-Vorschau in Marked, aktivieren Sie die Integration in Ihrem Editor und beginnen Sie mit der Eingabe; Aktualisierungen kommen nahezu in Echtzeit an.

## Entwickler [developers]

Um die Streaming-Vorschau in Ihre App zu integrieren, müssen Sie lediglich den Markdown-Text für die Vorschau in einer benannten Zwischenablage ablegen. Verwenden Sie zum Aktualisieren den folgenden Code (Objective-C), vorzugsweise mit einer didEndEditing-Methode oder in gedrosselten Intervallen:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Deklarieren einer Basis-URL für relative Assets [declaring-a-base-url-for-relative-assets]

Sie können auch eine Basis-URL für die Streaming-Vorschau bereitstellen, sodass relative URLs in Bildern und anderen Assets wie in der Quell-App funktionieren. Wenn die Basis-URL einen Dateinamen enthält, werden dessen Name und Dateiendung benutzerdefinierten Prozessoren zur Verfügung gestellt, dies ist jedoch nicht erforderlich. Um die Basis-URL einzuschließen, fügen Sie einfach ein NSURL-Objekt in die Zwischenablage ein:

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

Oder in Swift:

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Wenn die Mac App Store-Version von Marked verwendet wird und die Basis-URL nicht über Sandboxing zugänglich ist, wird beim ersten Laden der URL in der Vorschau eine Berechtigung angefordert.

### Deklarieren der Quellanwendung [declaring-the-source-application]

Apps können sich auch selbst als Quelle des Vorschauinhalts deklarieren, indem sie eine `source`-Metadatenzeile einfügen. Dies erfolgt normalerweise innerhalb eines HTML-Kommentars, um die Kompatibilität mit GFM- und MultiMarkdown-Prozessoren zu gewährleisten. Geben Sie einfach den Namen oder die Bundle-ID der App an:

```html
<!--
source: Bear.app
-->
```

### Programmgesteuertes Öffnen der Streaming-Vorschau [opening-the-streaming-preview-programatically]

Ihre App kann die Streaming-Vorschau programmgesteuert mithilfe der URL-Handler-Methode `x-marked-3://stream/` öffnen. Diese Methode akzeptiert auch einen `x-success`-Parameter, in dem Sie eine Bundle-ID einer App übergeben können, die nach Abschluss aktiviert werden soll.
