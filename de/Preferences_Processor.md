# <%= @title %>

Optionen im {% prefspane Processor %}:

![Settings: Processor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Verarbeiten Sie Markdown mit

Standardprozessor Markdown. Der Discount-Prozessor wird für GitHub-Benutzer bevorzugt, MultiMarkdown ist ideal für Autoren. Marked gleicht einige Unterschiede in der Syntax aus. Weitere Informationen finden Sie unter __Help->Markdown Reference__.

Custom Regeln
: Über die Schaltfläche „Custom-Regeln“ öffnen Sie den Custom-Regeleditor, in dem Sie Verarbeitungsoptionen und Dokumenttransformationen anhand von Kriterien festlegen können. Weitere Informationen finden Sie unter [Custom Processor documentation](Custom_Processor.html).

Neue Dokumente verwenden benutzerdefinierte
: Wählen Sie Präprozessor und/oder Prozessor aus, um die Regelverarbeitung für neue Dokumente automatisch zu aktivieren. Wenn Sie Custom-Regeln verwenden, möchten Sie wahrscheinlich, dass beide aktiviert sind.

### HTML

Generieren Sie IDs für Schlagzeilen
: Header-IDs basierend auf dem Inhalt des h1-h6-Tags generieren.

Verwenden Sie zufällige Fußnoten-IDs
: Generieren Sie zufällige Fußnoten-IDs, um Konflikte zu vermeiden, wenn mehrere Dokumente auf einer Seite angezeigt werden.

Verarbeiten Sie Markdown innerhalb von HTML
: Standardmäßig wird Markdown innerhalb von HTML-Tags normalerweise ignoriert. Diese Option zwingt Marked, die Verarbeitung innerhalb von Blockelementen fortzusetzen. Beachten Sie, dass einige Markups Probleme verursachen können.


### Rendern

Behalten Sie Zeilenumbrüche in Absätzen bei
: Zeilenumbrüche im Absatztext berücksichtigen und durch harte Umbrüche ersetzen, anstatt sie mit der vorherigen Zeile zu verketten.

Rendern Sie GitHub-Kontrollkästchen
: Rendern Sie `- [ ]` und `- [x]` zum Erstellen von Kontrollkästchen in Listen. Kontrollkästchen werden zur Vorschau gerendert, sind jedoch innerhalb von Marked nicht funktionsfähig.

\#Text ist Tag
: Ermöglicht die Interpretation von Hashtags (`#` unmittelbar gefolgt von Text ohne Leerzeichen) als Tags und nicht als Überschriften. Diese Funktionalität ist für Bear-Benutzer standardmäßig verfügbar.
: __Style tags__ bewirkt, dass Tags mit „Kapsel“-Formatierung angezeigt werden, um sie vom Text zu unterscheiden. Wenn dies aktiviert ist, können Tags mit {% appmenu {{gear}}, Korrekturlesen, Kommentare anzeigen %} ein-/ausgeblendet werden.

![#Text is tag enabled][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Rendern Sie `==highlight==` und `~~delete~~`
: Wenn diese Option aktiviert ist, wird der `==highlight==`-Text als HTML `<mark>`-Tag gerendert, das als gelbe Hervorhebung angezeigt wird, sofern nicht anderweitig durch einen Stil geändert. Darüber hinaus wird die Syntax `~~delete~~` mit einem Tag `<del>` gerendert.

: Wenn __Render as CriticMarkup__ aktiviert ist, wird die Syntax `==highlight==` und `~~delete~~` in CriticMarkup konvertiert, das dann in der Original-, Markup- und bearbeiteten Ansicht angezeigt werden kann.

Rendern Sie `~text~` als Unterstrich
: Wenn diese Option aktiviert ist, werden `~text~`, die von einzelnen Tilden umgeben sind, unterstrichen dargestellt. Dies steht in Konflikt mit der MultiMarkdown-Syntax für Subskripte und ist standardmäßig deaktiviert.