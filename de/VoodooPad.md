# <%= @title %>

[VoodooPad][vp] bündelt jede Seite in einer einzigen Datenbankdatei. Ziehen Sie `.vpdoc` auf Marked, um eine Vorschau der Seite anzuzeigen, die derzeit in VoodooPad ganz vorne liegt. Verwenden Sie {% kbd cmd S %} in VoodooPad, wann immer Sie Marked zum Neuladen von der Festplatte benötigen.

Marked überwacht das Dokument auf der Festplatte und aktualisiert die Vorschau, wenn Sie in VoodooPad die Seite wechseln.

## Eingebettete Bilder

Wenn Sie Bilder mit Markdown oder HTML referenzieren und sich die Binärdatei **in** der VoodooPad-Datenbank befindet, kann Marked sie für die Vorschau extrahieren. Bilder, die nur **Aliase** sind (Dateien, die per Referenz eingefügt werden), werden nicht im Bundle gespeichert – verweisen Sie auf Bilder mit absoluten Pfaden oder Pfaden relativ zum `.vpdoc` auf der Festplatte, damit Marked sie auflösen kann.

[vp]: https://www.voodoopad.com/
