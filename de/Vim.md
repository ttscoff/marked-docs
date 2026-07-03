# <%= @title %>

[vim-marked][vimrepo] ist ein Vim-Plugin, das den aktuellen Markdown-Puffer in Marked öffnet. Es fügt `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle` und `:MarkedPreview` hinzu, sodass Sie die Datei (oder einen Bereich) an Marked senden können, ohne den Editor zu verlassen.

## Einrichtung

Installieren Sie es mit Ihrem Plugin-Manager; siehe [Projekt-README][vimrepo] für `vim-plug` und andere Optionen. Der Standardwert `g:marked_filetypes` umfasst `markdown` und gängige Varianten. Erweitern Sie die Liste, wenn Sie einen benutzerdefinierten `filetype` verwenden.

## macOS und App-Name

Marked ist nur für macOS verfügbar, daher wird das Plugin auf anderen Systemen nicht geladen. Der Standard-App-Name ist **Marked 2**. Wenn Ihre Kopie von Marked unter einem anderen Namen oder Pfad installiert ist, legen Sie `g:marked_app` entsprechend fest (z. B. auf einen vollständigen Pfad zum App-Bundle). Die README-Datei behandelt Beenden, automatisches Beenden und Fokusverhalten.

I> Dieses Hilfethema ist nicht Teil des vim-marked-Projekts; die neuesten Befehle und Optionen finden Sie im [GitHub-Repository][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked
