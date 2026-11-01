# <%= @title %>

Durch Öffnen von {% appmenu Ablage, Neu, Streaming-Vorschau %} erhält Marked Live-Updates über eine benannte Zwischenablage, anstatt eine Datei auf der Festplatte zu überwachen. Die Quell-App muss in Marked integriert werden.

[Curio](Curio.html), [Drafts](Drafts.html) und [The Archive](The_Archive.html) und [Traverse](Traverse.html) dokumentieren ihre eigenen Einstellungen und Menübefehle. nvUltra, nvALT, Bear und andere nutzen einen gemeinsamen Weg: Öffnen Sie die Streaming-Vorschau in Marked, aktivieren Sie die Integration in Ihrem Editor und beginnen Sie mit der Eingabe; Aktualisierungen kommen nahezu in Echtzeit an.

## Entwickler [developers]

Um die Streaming-Vorschau in Ihre App zu integrieren, müssen Sie lediglich den Markdown-Text für die Vorschau in einer benannten Zwischenablage ablegen. Verwenden Sie zum Aktualisieren den folgenden Code (Objective-C), vorzugsweise mit einer didEndEditing-Methode oder in gedrosselten Intervallen:

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### Herkunfts-App und Format deklarieren [declaring-the-origin-app-and-format]

Setzen Sie ein Schlüsselwort `source` oder `format` in einen HTML-Kommentar an den Anfang des gestreamten Textes. Marked liest den Kommentar und entfernt ihn aus der Vorschau, damit die Notiz mit GFM- und MultiMarkdown-Prozessoren kompatibel bleibt. Ein Leerzeichen nach dem Doppelpunkt ist optional (`source:Bear.app` und `source: Bear.app` sind gleich), und die Schlüsselwörter werden ohne Rücksicht auf Groß- und Kleinschreibung erkannt.

Beide Werte sind frei wählbar. Für einige davon hat Marked ein festes Verhalten, und jeder Wert steht im [Custom Processor](Custom_Processor.html) (Conductor) als **Streaming-Vorschau-Quelle** und **Streaming-Vorschau-Format** zur Verfügung. Diese Kriterien akzeptieren **ist**, **ist nicht**, **enthält** und **enthält nicht**.

**`source: APP_NAME`** nennt die Herkunfts-App, als App-Name oder Bundle-ID. Marked nutzt das, um eine besondere Behandlung für diese App hinzuzufügen. `source: Bear.app` und `source: Drafts.app` schalten das Vorschauverhalten dieser Apps ein. Jeder andere Name lässt sich weiterhin mit einer Conductor-Regel abgleichen, sodass Sie eigene Aktionen für diese App ausführen können:

```html
<!--source:Bear.app-->
```

**`format: fountain`** schaltet die [Fountain](Fountain_for_Screenwriters.html)-Verarbeitung ein, sodass der Stream als Drehbuch statt als Markdown angezeigt wird. Jeder andere Formatwert ändert den Prozessor nicht. Er dient dazu, dass eine Conductor-Regel ihn abgleichen kann, zum Beispiel **Streaming-Vorschau-Format** `ist` `fountain`.

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
