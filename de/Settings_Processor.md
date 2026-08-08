# <%= @title %>

Optionen unter {% prefspane Processor %}:

![Einstellungen: Prozessor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Markdown verarbeiten mit [process-markdown-with]

Standard-Markdown-Prozessor. Der CommonMark-Prozessor empfiehlt sich für GitHub-Nutzer, MultiMarkdown ist ideal für Schreibende, und Discount und Kramdown haben spezielle Einsatzzwecke. Marked gleicht einige Syntax-Unterschiede aus. Weitere Informationen unter __Hilfe → Markdown-Referenz__.

Eigene Regeln
: Klicken Sie auf die Schaltfläche „Eigene Regeln“, um den Editor für Eigene Regeln zu öffnen. Dort legen Sie je nach passenden Kriterien verschiedene Prozessoren und Dokumenttransformationen fest. Einzelheiten unter [Eigene Regeln](Custom_Processor.html).

Neue Dokumente verwenden eigene
: Ist dies aktiviert, verwenden neue Dokumente automatisch Ihren gespeicherten **Präprozessor** und/oder **Prozessor** aus den Eigenen Regeln, ohne dass Sie pro Dokument etwas einrichten müssen.

Vollständiger Festplattenzugriff
: Klicken Sie auf **Gewähren**, um Marked die Berechtigung zu geben, beim Einsatz benutzerdefinierter Prozessoren oder anderer Funktionen mit erweitertem Dateizugriff auch Dateien außerhalb seiner Sandbox zu lesen.

Um die Unterschiede zwischen den Prozessoren zu erkunden, schauen Sie sich den [Markdown-Dingus](Markdown_Dingus.html) an.

### HTML [html]

IDs für Überschriften generieren
: Erzeugt Überschriften-IDs anhand des Inhalts der h1–h6-Tags.

Zufällige Fußnoten-IDs verwenden
: Erzeugt zufällige Fußnoten-IDs, um Konflikte zu vermeiden, wenn mehrere Dokumente auf einer Seite angezeigt werden.

Markdown innerhalb von HTML verarbeiten
: Standardmäßig wird Markdown innerhalb von HTML-Tags meist ignoriert. Diese Option zwingt Marked, auch innerhalb von Blockelementen weiterzuverarbeiten. Beachten Sie, dass manches Markup Probleme verursachen kann.

### Darstellung [rendering]

Zeilenumbrüche in Absätzen beibehalten
: Berücksichtigt Zeilenumbrüche im Absatztext und ersetzt sie durch harte Umbrüche, statt sie mit der vorherigen Zeile zusammenzufügen.

GitHub-Kontrollkästchen rendern
: Rendert `- [ ]` und `- [x]` zum Erstellen von Kontrollkästchen in Listen. Die Kontrollkästchen werden in der Vorschau dargestellt, sind in Marked aber nicht funktional.

GitHub-:emoji: rendern
: Rendert `:name:`-Shortcodes als Emoji im GitHub-Stil in der Vorschau.

\#Text ist ein Tag
: Erlaubt, Hashtags (`#` direkt gefolgt von Text ohne Leerzeichen) als Tags statt als Überschriften zu interpretieren. Für Bear-Nutzer ist das die Standardeinstellung.

Tags formatieren
: Ist **#Text ist ein Tag** aktiviert, werden erkannte Tags mit Kapsel-Stil angezeigt. Tags lassen sich über {% appmenu {{gear}}, Korrekturlesen, Kommentare anzeigen %} ein- oder ausblenden.

![#Text ist ein Tag aktiviert][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

`==highlight==` und `~~delete~~` rendern
: Ist diese Option aktiviert, wird `==highlight==`-Text als HTML-`<mark>`-Tag gerendert, das als gelbe Hervorhebung erscheint, sofern ein Stil es nicht anders festlegt. Zusätzlich wird die Syntax `~~delete~~` mit einem `<del>`-Tag gerendert.

: Ist **Als CriticMarkup rendern** aktiviert, wird die Syntax `==highlight==` und `~~delete~~` in CriticMarkup umgewandelt, das sich dann in der Original-, Markup- und bearbeiteten Ansicht anzeigen lässt.

`~text~` als Unterstreichung rendern
: Ist diese Option aktiviert, wird `~text~` in einzelnen Tilden als unterstrichen gerendert. Das steht im Konflikt mit der MultiMarkdown-Syntax für Tiefstellung und ist standardmäßig deaktiviert.
