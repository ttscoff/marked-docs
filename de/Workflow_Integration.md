# <%= @title %>

## AppleScript

Marked enthält ein vollständiges [AppleScript-Wörterbuch](AppleScript_Support.html) zum Öffnen von Dateien, zum Steuern der Vorschau (Neuladen, Scrollen, Hervorheben, Autoscrollen, Schnelllesen), zum Lesen von Statistiken, zum Festlegen von Prozessoren, zum Kopieren von HTML oder RTF, zum Ändern von Vorschaustilen und zum Exportieren nach Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF und OPML. **Vorschauüberschriften/Inhaltsverzeichnis** über AppleScript ist [als in Arbeit dokumentiert](AppleScript_Support.html#table-of-contents-work-in-progress) und noch nicht zuverlässig.

Sie können auf die Anwendung, ein bestimmtes Fenster oder ein Dokument abzielen. Zu den Anwendungsbefehlen gehören **open streaming preview**, **preview clipboard** und **close all**. Zu den Dokumentbefehlen gehören **get statistics** und **print with profile**. Exportbefehle akzeptieren ein optionales Export-**profile** oder einen **`with`**-Datensatz für Optionen wie **style**, **pageSize** und **margins**. Zum Beispiel:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

Unter [AppleScript-Unterstützung](AppleScript_Support.html) finden Sie die Befehlsliste, die Kurzschreibweise für Ränder, Sandbox-Hinweise und Debugging-Tipps.

Durch die AppleScript-Integration können Anwendungen wie Tags.app auch direkt in Marked ausgeführt werden.

{% note %}
## Kurzbefehle

Marked bringt ab macOS 13 native [Kurzbefehle-Aktionen](Shortcuts_Integration.html) mit. Verwenden Sie **Datei öffnen und exportieren** für Workflows vom Finder nach PDF, **Dokument exportieren** für alles, was bereits in Marked geöffnet ist, oder **Vorschaustil festlegen**, um Designs vor dem Export zu ändern. Exportaktionen akzeptieren **Profile**, Vorschau-**Stile** und Optionen wie **Seitengröße**, **Ränder** und **Schriftgröße** (gleiche Semantik wie AppleScript `with`-Datensätze).

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## URL-Handler

Der [URL-Handler von Marked][urlhandler] ermöglicht eine umfassende Integration durch einfaches Aufrufen von URLs, entweder über AppleScript oder mit einem einfachen `open`-Befehl in einem Shell-Skript.

## Marked Bonus Pack [marked-bonus-pack]

Das Marked Bonus Pack ist eine Sammlung von Skripten, Befehlen und Diensten. Einige funktionieren mit mehreren Editoren, andere sind spezifisch für bestimmte Editoren. Die Dienste funktionieren im Allgemeinen mit jedem Editor, der über die erforderlichen Fähigkeiten verfügt. Der Rest ist in Ordnern organisiert, die auf der Anwendung basieren, mit der sie arbeiten.

Das Bonus Pack sowie Anleitungen zu Installation und Verwendung finden Sie in diesem [Artikel der Wissensdatenbank](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html

