# <%= @title %>

Durch Öffnen von {% appmenu Ablage, Neu, Streaming-Vorschau %} erhält Marked Live-Updates über eine benannte Zwischenablage, anstatt eine Datei auf der Festplatte zu überwachen. Die Quell-App muss in Marked integriert werden.

[Curio](Curio.html), [Drafts](Drafts.html), [nvALT](nvALT.html), [nvUltra](nvUltra.html), [The Archive](The_Archive.html) und [Traverse](Traverse.html) dokumentieren ihre eigenen Einstellungen und Menübefehle. Bear und andere nutzen denselben Weg: Öffnen Sie die Streaming-Vorschau in Marked, aktivieren Sie die Integration in Ihrem Editor und beginnen Sie mit der Eingabe; Aktualisierungen kommen nahezu in Echtzeit an.

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

### Herkunfts-App und Format deklarieren [declaring-the-origin-app-and-format]

Setzen Sie ein Schlüsselwort `source` oder `format` in einen HTML-Kommentar an den Anfang des gestreamten Textes. Marked liest den Kommentar und entfernt ihn aus der Vorschau, damit die Notiz mit GFM- und MultiMarkdown-Prozessoren kompatibel bleibt. Ein Leerzeichen nach dem Doppelpunkt ist optional (`source:Bear.app` und `source: Bear.app` sind gleich), und die Schlüsselwörter werden ohne Rücksicht auf Groß- und Kleinschreibung erkannt.

Beide Werte sind frei wählbar. Für einige Werte hat Marked ein eingebautes Verhalten, und jeder Wert steht im [Benutzerdefinierten Prozessor](Custom_Processor.html) (Conductor) als **Streaming-Vorschau-Quelle** und **Streaming-Vorschau-Format** zur Verfügung. Diese Kriterien akzeptieren **ist**, **ist nicht**, **enthält** und **enthält nicht**.

**`source: APP_NAME`** nennt die Herkunfts-App, per App-Name oder Bundle-ID. Darüber kann Marked diese App gesondert behandeln. `source: Bear.app` und `source: Drafts.app` schalten das Vorschauverhalten dieser Apps ein. Auf jeden anderen Namen kann eine Conductor-Regel reagieren, sodass Sie für diese App eigene Aktionen ausführen können:

```html
<!--source:Bear.app-->
```

**`format: fountain`** schaltet die [Fountain](Fountain_for_Screenwriters.html)-Verarbeitung ein, sodass der Stream als Drehbuch statt als Markdown angezeigt wird. Andere Formatwerte ändern den Prozessor nicht; sie sind für Conductor-Regeln gedacht, zum Beispiel **Streaming-Vorschau-Format** `ist` `fountain`.

```html
<!--format:fountain-->
```

Ein Kommentar kann beide Schlüsselwörter enthalten:

```html
<!--
source: Bear.app
format: fountain
-->
```

### Programmgesteuertes Öffnen der Streaming-Vorschau [opening-the-streaming-preview-programatically]

Ihre App kann die Streaming-Vorschau programmgesteuert mithilfe der URL-Handler-Methode `x-marked-3://stream/` öffnen. Diese Methode akzeptiert auch einen `x-success`-Parameter, in dem Sie eine Bundle-ID einer App übergeben können, die nach Abschluss aktiviert werden soll.
