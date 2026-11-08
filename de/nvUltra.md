# <%= @title %>

[nvUltra][nvu] indiziert Klartext-Notizbücher auf der Festplatte und kann die ausgewählten Notizen mit einem eingebauten Befehl an Marked übergeben oder die Notiz, die Sie bearbeiten, streamen.

## Vorschau der Datei(en) in Marked [preview-files-in-marked]

Klicken Sie im **Ordnernavigator** von nvUltra (oder überall dort, wo Sie Notizen durchsuchen) **bei gedrückter Strg-Taste** auf die Datei(en), um das Kontextmenü zu öffnen, und wählen Sie **Preview File(s) in Marked**.

![][nvultramenu]

Marked öffnet normale dateigestützte Vorschauen, sodass Ihr MultiMarkdown mit Marked-Stilen, Lesezeichen, Minimap-Schaltern und Exportoptionen gerendert wird. Verwenden Sie dies, wenn Sie direkt aus nvUltra wechseln möchten, ohne Dateien ins Dock zu ziehen.

## Streaming-Vorschau [streaming-preview]

nvUltra kann die Notiz, die Sie gerade bearbeiten, auch während der Eingabe an Marked senden.

1. Wählen Sie in nvUltra im Menü **View** den Befehl **Enable Marked Streaming Preview**.
2. Wählen Sie in Marked {% appmenu Ablage, Neu, Streaming-Vorschau %}.

![Enable Marked Streaming Preview im View-Menü von nvUltra][nvultrastream]

Die Vorschau wird aktualisiert, während Sie die aktuelle Notiz bearbeiten.

## Alternative: Ordnerüberwachung [alternative-folder-watching]

Soll Marked in einem ganzen Ordner **jeder zuletzt bearbeiteten Notiz** folgen? Legen Sie stattdessen den Notizbuchordner auf Marked ab. Siehe **[Ordnerüberwachung](Folder_Watching.html)** für die Überwachung im nvALT-Stil, das Scrollen zu Bearbeitungen und die Unterschiede dieses Arbeitsablaufs zum Öffnen einzelner Dateien.


[nvultramenu]: images/nvUltra_preview_in_marked_menu.png width=854px height=264px class=center

[nvultrastream]: images/nvUltra_enable_marked_streaming_preview.jpg @2x width=455px height=205px class=center

[nvu]: https://nvultra.com/
