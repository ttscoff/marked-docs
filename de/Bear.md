# <%= @title %>

[Bear][bear] kann eine Live-Vorschau direkt an Marked senden.

## Senden von Bear [sending-from-bear]

Wählen Sie in Bear im Menü **Ansicht** die Option **Vorschau in Marked** (der Wortlaut kann je nach Bear-Version leicht variieren). Marked erhält ein TextBundle, sodass eingebettete Bilder und Assets in der Regel zusammen mit dem Text übertragen werden.

Bilder, auf die mit absoluten Pfaden oder `https`-URLs verwiesen wird, werden ebenfalls aufgelöst, solange Marked sie erreichen kann.

## Hinweis zum Mac App Store [mac-app-store-note]

Wenn Sie die **Mac App Store**-Version von Marked verwenden und macOS bei der Vorschau aus Bear wiederholt um Erlaubnis zum Öffnen von Verzeichnissen fragt, [wenden Sie sich an den Marked-Support](http://support.markedapp.com), um kostenlos auf die Direkt-Download-Edition umzusteigen. Dadurch wird diese spezielle Sandbox-Hürde vermieden.

## Tags [tags]

Tags im Bear-Stil können als solche gerendert werden, indem unter {% prefspane Processor %} **#Text ist Tag** und **Stil-Tags** aktiviert werden.

W> Diese Einstellung kann Marked verwirren, wenn Sie normale Überschriften ohne Leerzeichen nach dem `#` schreiben.

## Dateinamen und Export [filenames-and-export]

Wenn Sie **Erstes H1 als Fallback-Titel verwenden** in {% prefspane Export %} aktivieren, kann dieser Titel den Dateinamen und den Platzhalter `%title` steuern, wenn Sie PDFs aus Marked drucken oder exportieren.

I> Ein Vorschaustil, der Bears eigenem Aussehen nahekommt, ist [auf markedapp.com/styles verfügbar](https://markedapp.com/styles/preview?style=bear).

Die Streaming-Vorschau von Bear ist auf der Seite [Streaming-Vorschau](Streaming_Preview.html) und unter [Zusätzliche Anwendungsunterstützung](Additional_Application_Support.html) zusammengefasst.

[bear]: https://bear.app/
