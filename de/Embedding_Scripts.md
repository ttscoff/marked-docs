# <%= @title %>

Es gibt mehrere Möglichkeiten, zusätzliche JavaScripts in Marked einzubetten.

## JavaScript pro Dokument einbinden [including-javascript-per-document]

Sie können Skripte in ein einzelnes Dokument einbinden, indem Sie `<script>`-Tags im Inhalt selbst verwenden. Das ist nützlich für Bibliotheken wie [D3](https://d3js.org/) für Datenvisualisierungen, die Sie nur in bestimmten Dokumenten brauchen:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Wenn Sie MultiMarkdown als Prozessor verwenden, können Sie Skripte in den Metadaten angeben; sie werden dann in das Dokument eingefügt. Da Marked nur ein „Snippet“ ausgibt, ist der Schlüssel `XHTML Header` nicht ideal. Verwenden Sie stattdessen `CSS Header` – die Skripte werden dann am Ende des Dokuments eingefügt.

	CSS Header: <script src="file.js"></script>

Wie Sie eingebundene Skripte bei Inhaltsänderungen aktualisieren lassen, steht unter [Hooks](#hooks).

## JavaScript einbinden [including-javascript]

Sie können eigenes JavaScript aus lokalen Dateien, von CDNs oder als eingefügten Rohcode einbinden. Öffnen Sie dazu {% prefspane Style %} und klicken Sie auf die Schaltfläche *Eigene Regeln*.

Richten Sie eine neue Eigene Regel ein oder fügen Sie Skripte zu einer vorhandenen hinzu. Damit Skripte zu jeder Datei hinzugefügt werden, setzen Sie das Prädikat auf „Dateiname enthält *“.

Der Aktionen-Editor einer Eigenen Regel bietet drei Möglichkeiten, Skripte einzubinden:

JavaScript-Datei einfügen
: Lässt Sie eine lokale Datei auswählen, die am Ende des Dokuments eingefügt wird

JavaScript von URL einfügen
: Lässt Sie ein CDN oder eine andere entfernte URL einbinden; am Ende des Dokuments entsteht dann ein `<script>`-Tag mit der verknüpften URL

JavaScript einfügen
: Öffnet einen Code-Editor, in dem Sie eigenen JavaScript-Code schreiben oder einfügen

Diese Skripte werden am Ende der Vorschau vor dem Dokument-Tag eingefügt. Wenn Sie bei jeder Aktualisierung der Vorschau eine Init-Funktion aufrufen oder aktualisieren müssen, lesen Sie [Including Raw JavaScript](Embedding_Scripts.html#hooks) und machen Sie sich mit [hooks](#hooks) von Marked vertraut.

## Mermaid und andere Skripte [mermaid]

jQuery ist standardmäßig enthalten und Sie können es in allen Skripten verwenden, die Sie mit einer der folgenden Methoden zu Marked hinzufügen.

[Mermaid](https://mermaid.js.org/intro/) für Markdown-ähnliche Diagramme ist inzwischen standardmäßig in jedem Dokument enthalten. Jeder abgegrenzte Codeblock mit der Sprache `mermaid` wird automatisch als Diagramm gerendert.

Unten unter {% prefspane Style %} erscheint ein Kontrollkästchen „Diagramme schwenken und zoomen“, sobald Mermaid-Inhalte vorhanden sind. Ist es aktiviert, zoomen Diagramme mit {% kbd cmd %}-Scrollen und lassen sich per Klicken und Ziehen verschieben. Das Skript für diese Funktion wird von einem CDN geladen und erfordert eine Internetverbindung.

Wenn Sie eine bestimmte Bibliothek gern standardmäßig dabei hätten, sagen Sie es mir im [BrettTerpstra.com-Forum](https://forum.brettterpstra.com/) oder über [die Support-Seite](https://support.markedapp.com/questions/add).

## Hooks [hooks]

Seit einigen Versionen lädt Marked beim Aktualisieren von Inhalten nicht mehr die ganze Seite neu, sondern fügt den neuen Inhalt in das DOM ein, ohne dass die Seite geladen werden muss. Das heißt: Eingebundene Skripte, die beim Laden der Seite anspringen, laufen bei einer Aktualisierung des Inhalts nicht erneut an. Dafür bietet Marked die „Hooks“-Funktion. Um einen Hook zu registrieren, binden Sie einen zweiten Skriptblock ein, der die [Funktion `Marked.hooks.register()`](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor) aufruft; sie erwartet einen Auslöser – hier `update` – und eine auszuführende Funktion.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// D3-Visualisierung bei Inhaltsänderung neu ausführen
		d3.selectAll('.chart').each(function() {
			// hier Ihre D3-Render-Logik
		});
	});
</script>
```

Alle [API-Funktionen](https://markedapp.com/jsapi/) von Marked lassen sich in diesem Feld verwenden. (Sie können die API auch in allen geladenen Skripten nutzen.) Zum interaktiven Debuggen und Experimentieren mit der API in einer Live-Vorschau finden Sie im Abschnitt [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) Hinweise zur Verwendung von Safaris Menü „Entwickeln“ mit Marked.

Von da an wird die übergebene Funktion bei jeder Aktualisierung ausgeführt, also immer dann, wenn die überwachte Quelldatei gespeichert wird. Solange das Skript eine Init- oder Render-Funktion besitzt, rufen Sie es per Hook auf und lassen es bei jedem Speichern neu rendern.



*[CDN]: Content Distribution Network
