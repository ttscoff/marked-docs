# <%= @title %>

[Visual Studio Code][vscode] enthält Marked nicht standardmäßig, aber Sie können eine Community-Erweiterung für die **Live-Vorschau von Markdown** in Marked verwenden – mit Vorschau, Export und Korrektur, während Sie weiter in VS Code schreiben.

## Schnellstart

1. Installieren Sie eine **Open in Marked**-Erweiterung für VS Code (siehe [Open in Marked extension][ext] unten).
2. Öffnen Sie Ihre Markdown-Datei in VS Code.
3. Senden Sie die Datei an Marked – die Vorschau wird beim Speichern aktualisiert.

## In der Erweiterung Marked öffnen

Die [Open in Marked extension][ext] (Visual Studio Marketplace) fügt eine Aktion **In Marked öffnen** hinzu: eine Editor-Titelschaltfläche, **{% kbd shift cmd m %}**, Kontextmenüs im Editor und Datei-Explorer, optional **Ordner öffnen** für den Dateibrowser von Marked, eine Statusleistenanzeige und optionales automatisches Speichern vor dem Öffnen. In den Einstellungen können Sie den Pfad zur Marked-App festlegen, wenn diese sich nicht am Standardspeicherort befindet.

I> Die Erweiterung wurde ursprünglich für Marked 2 veröffentlicht. Marked 3 verwendet dieselbe Art der Datei- und URL-Übergabe, sodass diese Integration weiterhin funktioniert. Falls sich etwas ändert, prüfen Sie die [extension page][ext] oder das Repository des Autors auf Aktualisierungen.

## Anforderungen

Marked läuft nur auf macOS. Installieren Sie [Marked 3][marked] und die Erweiterung und zeigen Sie dann bei Bedarf den **App-Pfad** auf Ihre Marked-App.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/
