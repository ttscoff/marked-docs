# <%= @title %>

Marked verfügt über einen integrierten Stileditor und kann eigene CSS-Dateien anwenden.

Mit dem Editor erstellen Sie ansprechende Stile – oder wenn Sie gerade genug CSS können, um gefährlich zu sein, verpassen Sie Marked jedes beliebige Aussehen.

## Erste Schritte [getting-started]

Unter [markedapp.com/styles](https://markedapp.com/styles/) gibt es eine Galerie mit Eigenen Stilen, erstellt vom Entwickler und von Nutzern. In der Galerie können Sie Stile in der Vorschau ansehen und direkt in Marked installieren. Jeden installierten Stil können Sie im Finder anzeigen, um ihn zu prüfen und zu ändern. Die Galerie öffnen Sie mit einem internen Viewer über {% appmenu Stil, Eigenen Stil erzeugen %}, oder Sie klicken auf das Stift-Symbol (Bearbeiten) neben einem bearbeitbaren Stil im Stil-Manager. Möchten Sie einen integrierten Stil bearbeiten, müssen Sie ihn zuerst im Manager duplizieren.

Auf GitHub gibt es außerdem ein [Repository für Eigene Stile](https://github.com/ttscoff/MarkedCustomStyles) mit Beispielen. Stöbern Sie dort, nutzen Sie sie und tragen Sie gerne selbst etwas bei. Wenn Sie Ihr Design auf einem der Basis-Designs aufbauen und weitergeben, tragen Sie sich gerne selbst als Mitwirkender in die Credits ein.

Dank Markeds Fähigkeit, eigene CSS-Dateien zu verwenden, sind Ihnen bei der Anpassung Ihrer Vorschau kaum Grenzen gesetzt. Alle CSS3-Optionen, die in Safari funktionieren, funktionieren auch in Marked. Bei Standard-Markdown-Dateien in Marked müssen Sie nur wenige HTML-Elemente behandeln; der gesamte Inhalt steckt in einem `div` mit der ID `wrapper`, alles andere ergibt sich aus dem Markup Ihres Dokuments.

Wenn Sie für den persönlichen Gebrauch gestalten, gibt es keine Regeln. Aktivieren Sie die CSS-Überwachung über das Kontrollkästchen unter dem Auswahlfeld für eigenes CSS; sobald Sie Ihr eigenes CSS bearbeiten und speichern, aktualisiert sich die Vorschau.

**Für den Einstieg gibt es ein [Grundgerüst-Design](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css).**

Wenn Sie Ihre CSS-Kreation teilen möchten, sollten Sie einige Punkte beachten. Erstens gibt es einige Body-Klassen, auf die Stile angewendet werden müssen:

## Body-Klassen [body-classes]

Die folgenden Stile müssen in jedem Marked-CSS enthalten sein, das geteilt werden soll. Über die Body-Klassen können Sie jeden Selektor unter verschiedenen Einstellungsoptionen gezielt ansprechen und ändern.

### Inverted [inverted]

Wenn der Nutzer {% appmenu Vorschau, Dunkelmodus %} auswählt, wird dem Body-Tag die Klasse `inverted` hinzugefügt. Damit sprechen Sie die kontrastreichen Hell-auf-Dunkel-Stile gezielt an.

Invertierte Stile sollen nur in der Vorschau greifen, nicht im Druck – schränken Sie sie daher mit einer Media-Query (`@media screen`) ein. Der folgende Code ist recht universell und lässt sich in den meisten Fällen einfach in Ihr Stylesheet übernehmen; passen Sie ihn aber gern an.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poetry [poetry]

Der Nutzer kann wählen, ob mit Tabulator eingerückter Text als Poesie oder als Code behandelt wird. Der einzige Unterschied: pre/code-Blöcke werden im Poesie-Modus etwas – nun ja – poetischer gestaltet. Die Klasse `poetry` wird auf das Body-Tag angewendet.

Gestalten Sie es so kreativ, wie Sie möchten – hier ist ein einfacher Ausschnitt zum Einstieg:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Sonderfälle [special-cases]

Auch Tabellen, `figure`/`figcaption` sowie die Sonderfälle `a.footnote` und `div.footnotes>a` müssen bedacht werden. Es gibt keine festen Regeln für den Umgang damit; werfen Sie aber einen Blick auf die Standardstile, um ein Gefühl dafür zu bekommen, welche CSS-Regeln Marked braucht.

Der Tabellenstil aller Standardstile nutzt Transparenz bei abwechselnden Zeilen, damit er sich sanft in jeden Hintergrund einfügt. Sie können diese Stile kopieren oder einen eigenen Weg gehen – Hauptsache, Sie gestalten sie überhaupt! Dasselbe gilt für `figure` und `figcaption`; fügen Sie einem Dokument ein Bild mit Alternativtext hinzu, um zu sehen, wie das Markup aussieht, und gestalten Sie es entsprechend.

In einem Dokument enthaltene Fußnoten erzeugen einen Link im Inhalt (`a.footnote`) und am Ende ein `div` mit dem referenzierten Text (`div.footnotes`). Sehen Sie auch hier die Standardstile als Referenz an. Damit sich die Zeilenhöhe in Zeilen mit einer Fußnoten-Referenznummer nicht ändert, binden Sie unbedingt etwas wie dies ein:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Damit der Rücksprung-Pfeil in derselben Zeile bleibt, binden Sie ein:

```css
.footnotes p {display:inline}
```

Ebenso empfiehlt sich eine allgemeine Regel für alle Bilder, damit sie die Seitenbreite nicht überschreiten. Etwa so:

```css
#wrapper img { max-width: 100% }
```

Hat Ihr Design zusätzliches Padding oder eine feste Breite, passen Sie die `max-width` entsprechend an.

## Druckstile [printstyles]

Binden Sie unbedingt Druckstile ein, die Hintergrundfarben, festes Scrollen und reine Vorschau-Bedienelemente entfernen. Marked bietet Ihnen zwei Wege, Druck- und PDF-Ausgabe gezielt anzusprechen.

### `@media print` [media-print]

Standard-CSS-Druckregeln greifen, wenn Sie aus Marked drucken oder wenn der PDF-Export print-Medien verwendet:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### Die Klasse `.mkprinting` [the-mkprinting-class]

Wenn Marked ein Dokument für den **PDF-Export** oder die **Druck-/PDF-Vorschau** ({% kbd cmd P %}) vorbereitet, fügt es dem `<body>`-Tag die Klasse `mkprinting` hinzu (neben Export-Klassen wie `bandw`, `breakAfterTOC` und der `mkstyle--*`-Klasse Ihres Stils). Markeds integrierte Designs nutzen für die meisten druckspezifischen Regeln diese Klasse, statt sich allein auf `@media print` zu verlassen.

Der PDF-Export lädt das versteckte Render-WebView oft mit **screen**-Medien (besonders bei Eigenen Stilen und [Fountain](Fountain_for_Screenwriters.html)-Dokumenten), sodass `@media print`-Blöcke in Ihrem Stylesheet auf die PDF-Ausgabe **nicht** unbedingt angewendet werden. Regeln mit dem Präfix `.mkprinting` greifen beim Export immer, weil es gewöhnliche Klassenselektoren sind und keine Media-Queries.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Für Stile, die **sowohl** beim Drucken über den Browser als auch beim PDF-Export von Marked funktionieren müssen, verdoppeln Sie die entscheidenden Regeln oder kombinieren Sie die Selektoren:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

Beim Debuggen von eigenem Druck-CSS öffnen Sie die Druck-/PDF-Vorschau oder exportieren nach PDF und untersuchen das Dokument dann mit [Safaris Web Inspector](#webkitinspector) – während das Drucklayout aktiv ist, trägt der `<body>` die Klasse `mkprinting`.

Das Ausblenden von Links im Druck wird außerhalb des Haupt-Designs gehandhabt, sodass Nutzer wählen können, ob Hervorhebungen und Unterstreichungen von Links im Ausdruck ausgeblendet werden. Solange Sie einen Basisstil für den Text gesetzt haben, müssen Sie sich darum nicht kümmern.

Also los. Verwandeln Sie Ihr Blog-Design, erstellen Sie einen erstklassigen Druckstil für PDF-Dokumente oder gestalten Sie die perfekte Vorschau für Ihre Art zu schreiben. Wenn Sie etwas Großartiges erschaffen, [teilen Sie es mit der Community](https://markedapp.com/styleshare/).

## Zusätzliche CSS-Einstellungen [additional-css-settings]

Unter {% prefspane Style %} können Sie zusätzliches CSS bearbeiten. Diese Stile werden an jedes geladene Design angehängt und lassen sich für universelle Änderungen an allen Designs nutzen.

Mit [hoher Spezifität](#overridingspecificity), `@media`-Abfragen für Druck und Bildschirm sowie `.mkprinting`-Selektoren für den PDF-Export steuern Sie mit etwas CSS-Wissen nahezu jeden Gestaltungsaspekt.

## WebKit-Inspektor [webkitinspector]

Safaris Web Inspector ist der einfachste Weg, um genau zu sehen, welches HTML und CSS Marked erzeugt, und um live mit Eigenen Stilen zu experimentieren.

### Das Entwickeln-Menü in Safari aktivieren [enabling-the-develop-menu-in-safari]

1. Öffnen Sie Safari und wählen Sie {% appmenu Safari, Einstellungen… %}.
2. Wählen Sie den Tab **Erweitert**.
3. Aktivieren Sie **Funktionen für Web-Entwickler anzeigen** (oder bei älteren macOS-Versionen **Menü „Entwickeln“ in der Menüleiste anzeigen**).

Nach der Aktivierung erscheint in Safaris Menüleiste ein **Entwickeln**-Menü.

![Safari „Entwickeln“-Menü mit Marked-Dokumenten][develop-menu]

### Ein Marked-Dokument untersuchen [inspecting-a-marked-document]

1. Wechseln Sie bei geöffnetem Vorschaufenster in Marked zu Safari.
2. Wählen Sie in der Menüleiste **Entwickeln → _\<Ihr Mac-Name\>_ → Marked → _\<Dokumenttitel\>_**.
3. Safari öffnet ein Web-Inspector-Fenster, das mit der ausgewählten Marked-Vorschau verbunden ist.

Von hier aus können Sie:

- Über den Tab **Elemente** das DOM innerhalb des `#wrapper`-`div` untersuchen und sehen, welche CSS-Regeln greifen.
- Mit dem Mauszeiger über Elemente im DOM-Baum fahren, um sie im Marked-Fenster hervorzuheben.
- Über die Seitenleiste **Stile** Regeln live anpassen und funktionierende Ausschnitte anschließend zurück in einen Eigenen Stil oder in **Zusätzliches CSS** kopieren.
    - Nachdem Sie CSS im Tab „Elemente“ bearbeitet haben, erhalten Sie über den Tab „Änderungen“ eine Zusammenfassung Ihrer Änderungen.

	![Änderungen][css-changes]
- Über den Tab **Konsole** JavaScript gegen die Live-Vorschau ausführen. Die vollständige [Marked-JavaScript-API](https://markedapp.com/help/jsapi/) steht in dieser Konsole zur Verfügung.
- Weitere Tabs wie **Netzwerk** erkunden, wenn Sie die von Ihrem Dokument geladenen Ressourcen debuggen.

![Untersuchen einer Marked-Vorschau mit Safaris Web Inspector][inspecting]

## Eigenes CSS teilen [sharing-custom-css]

Über {% appmenu Stil, Eigenen Stil teilen %} öffnen Sie die Sharing-App in Ihrem Webbrowser. Ziehen Sie Ihr CSS in die Ablagezone (oder klicken Sie, um es von der Festplatte auszuwählen) und laden Sie das CSS für Ihren Eigenen Stil hoch.

Geteilte Stile müssen erst vom Entwickler freigegeben werden, bevor sie in der Galerie erscheinen – Sie sehen also nicht sofort ein Ergebnis.

## Weitere Tipps [other-tips]

### Übergeordnete Spezifität [overridingspecificity]

Innerhalb der Marked-Vorschau wird eine Body-Klasse hinzugefügt, die auf dem Dateinamen des aktuellen Stils basiert. Ist die Vorschau auf „Swiss“ eingestellt, trägt das `<body>`-Tag eine Klasse namens `mkstyle--swiss`. Heißt Ihr eigenes CSS MyCustom.css, lautet die Body-Klasse `mkstyle--mycustom`. Diese können Sie den in den Basisstilen definierten Regeln voranstellen, um sie zu überschreiben. Für absolute Spezifität in einer Regel nehmen Sie zusätzlich die `#wrapper`-ID des Container-`div` hinzu:

	.mkstyle--mycustom #wrapper p+p { ... }

### Inhaltsverzeichnis gestalten [table-of-contents-styling]

Wenn Sie mit dem Token `<!--toc-->` ein [Inhaltsverzeichnis einfügen](Special_Syntax.html#tableofcontents), können Sie die Einstellungen für die Ebenenmarkierungen des Inhaltsverzeichnisses in einem Eigenen Stil überschreiben, indem Sie mit `#wrapper` die Spezifität erhöhen:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Damit verwenden alle Listeneinträge im Inhaltsverzeichnis ein quadratisches Aufzählungszeichen statt des in den Einstellungen definierten – solange Ihr Eigener Stil aktiv ist.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari-Entwickeln-Menü" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Ein Marked-Dokument in Safari untersuchen" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
