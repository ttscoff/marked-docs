Marked Not Installed
<%= @title %>

Marked enthält ein Wiki-Navigationssystem, mit dem Sie mithilfe einfacher [[wiki]]-Links schnell zwischen verwandten Textdateien wechseln können. Dieses System ist für eine nahtlose Navigation konzipiert und funktioniert am besten, wenn es so konfiguriert ist, dass Links im aktuellen Fenster geöffnet werden.

Optimale Einstellungen

Um die Wiki-Verlinkung zu verwenden, aktivieren Sie [[wiki links]] konvertieren unter {% prefspane Preview %} und legen Sie die Standarderweiterung fest, die Marked bei der Suche nach passenden Dateien verwendet.

Um das beste Erlebnis zu erzielen, setzen Sie „Links zu Textdateien öffnen in:“ auf „das aktuelle Fenster“ unter {% prefspane Apps %}. Dadurch wird sichergestellt, dass sich die Navigation natürlich anfühlt und der Verlauf erhalten bleibt.

Wenn Markdown-Syntaxfehler hervorheben unter {% prefspane Proofing %} aktiviert ist, wird [[wiki link]]-Syntax, die mit keinem Dateinamen im aktuellen Verzeichnis übereinstimmt, rot hervorgehoben, um anzuzeigen, dass eine referenzierte Datei nicht vorhanden ist. Diese Hervorhebungen werden aktualisiert, wenn Dateien hinzugefügt werden, jedoch erst, nachdem die aktuelle Datei gespeichert oder neu geladen wurde. Wenn Sie auf einen hervorgehobenen Link zu einer fehlenden Datei klicken, bietet Marked Ihnen an, eine neue Datei zu erstellen und bei Bedarf die Standarderweiterung anzuhängen. Die neue leere Datei wird in Marked geöffnet, und wenn „Neue Dateien automatisch bearbeiten“ aktiviert ist, wird Ihr Editor mit der neuen Datei geöffnet.

Wie Wiki-Links funktionieren

Wiki-Links verwenden das Format: [[wiki link]].
Wenn Sie auf einen Wiki-Link klicken, sucht Marked nach einer passenden Datei im gleichen Verzeichnis wie das aktuelle Dokument.
Die Datei muss die in den Einstellungen von Marked angegebene Erweiterung haben (z. B. .md), es sei denn, Sie geben im Link einen vollständigen Dateinamen mit Erweiterung an (z. B. [[notes.txt]]).
Wenn Sie für den Link einen vom Dateinamen abweichenden Text verwenden möchten, fügen Sie ihn nach einem Pipe-Zeichen (|) im Link ein, z. B. [[wiki linking|A note about linking]], der als [A note about linking](wiki-link.md) angezeigt wird.
Wenn ein Wiki-Link mit einem # beginnt, wird er als Ankerlink auf derselben Seite behandelt. Ankernamen werden normalisiert, indem alles kleingeschrieben und alle Leerzeichen durch Bindestriche ersetzt werden. Bei Prozessoren, die Überschriften-IDs ohne Bindestriche erzeugen (wie MultiMarkdown) – z. B. erhält ## wiki links die ID wikilinks –, kann diese Navigation fehlschlagen. Geben Sie in diesen Fällen die richtige Link-ID an, bei Bedarf mit Pipe-Zeichen und Titel, z. B. [[#wikilinks|#wiki links]].
Passende Dateinamen

Wenn Sie einen Link wie [[wiki link]] verwenden, sucht Marked nach einer Datei mit einem der folgenden Namen (vorausgesetzt, Ihre Standarderweiterung ist .md):

wiki link.md
WikiLink.md
wiki-link.md
Wiki-Link.md
wiki_link.md
Wiki_Link.md
wikilink.md
WikiLink.md
(und andere Kombinationen aus Leerzeichen, Bindestrichen, Unterstrichen und Binnengroßschreibung)
Der Abgleich erfolgt stets ohne Beachtung der Groß-/Kleinschreibung und ist bei den Trennzeichen flexibel. Wenn Sie im Link eine Erweiterung angeben (z. B. [[notes.txt]]), sucht Marked genau nach dieser Datei.

Backlinks

Wenn eine Textdatei geöffnet wird und die Wiki-Navigation aktiviert ist, werden die übrigen Dateien im Verzeichnis nach [[links]] auf die aktuelle Datei durchsucht. Dies geschieht im Hintergrund, und das geöffnete Dokument wird mit einer Liste der Backlinks aktualisiert, sofern welche gefunden werden. Um die Backlinks anzuzeigen, muss die Kommentar-Seitenleiste geöffnet sein. Wenn sie geschlossen ist, verwenden Sie das Zahnradmenü (Korrekturlesen->Kommentare anzeigen) oder drücken Sie {% kbd ^@c %}, um sie zu öffnen.

Navigationsverlauf

Marked verfolgt Ihre Navigation über Wiki-Links und ermöglicht Ihnen, sich vor und zurück durch Ihren Dateiverlauf zu bewegen – genau wie in einem Webbrowser.

Zurück: {% kbd @[ %}
Vorwärts: {% kbd @] %}
Sie können auch das Menü Verlauf verwenden, um zu einer beliebigen zuvor besuchten Datei zu springen.
