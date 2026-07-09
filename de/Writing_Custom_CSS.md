# <%= @title %>

Marked verfügt über einen integrierten Stileditor und kann benutzerdefinierte CSS-Dateien anwenden.

Sie können den Editor verwenden, um schöne Stile zu erstellen, oder wenn Sie gerade genug CSS kennen, um gefährlich zu sein, können Sie Marked so aussehen lassen, wie Sie möchten.

## Erste Schritte

Es gibt eine Galerie mit Custom-Stilen, die vom Entwickler und von Benutzern unter [markedapp.com/styles](https://markedapp.com/styles/) erstellt wurden. In der Galerie können Sie Stile in der Vorschau anzeigen und direkt in Marked installieren. Jeder installierte Stil kann im Finder zur Prüfung und Änderung angezeigt werden. Die Galerie kann mit einem internen Viewer mit {% appmenu Stil, Eigenen Stil erzeugen %} geöffnet werden, oder klicken Sie auf das Stiftsymbol (Bearbeiten) neben einem bearbeitbaren Stil im Stil-Manager. Wenn Sie einen bearbeiten möchten Wenn Sie einen integrierten Stil verwenden möchten, müssen Sie ihn zunächst im Manager duplizieren.

Es gibt auch einen [repository for Custom Styles](https://github.com/ttscoff/MarkedCustomStyles) auf GitHub mit Beispielen. Fühlen Sie sich frei, dort zu stöbern, es zu nutzen und einen Beitrag zu leisten. Wenn Sie Ihr Thema basierend auf einem der Basisthemen verbreiten, können Sie sich gerne selbst als Mitwirkender in die Credits eintragen.

Mit der Möglichkeit von Marked, benutzerdefinierte CSS-Dateien zu verwenden, sind Ihnen bei der Anpassung Ihrer Vorschau keine Grenzen gesetzt. Alle CSS3-Optionen, die in Safari funktionieren, funktionieren auch in Marked. Bei den standardmäßigen Markdown-Dateien in Marked müssen Sie nur wenige HTML-Elemente verarbeiten; Der gesamte Inhalt befindet sich in einem Div mit der ID „wrapper“, alles andere wird durch Ihr Dokument-Markup bestimmt.

Wenn Sie für den persönlichen Gebrauch entwerfen, gibt es keine Regeln. Aktivieren Sie die CSS-Verfolgung mit dem Kontrollkästchen unter der benutzerdefinierten CSS-Auswahl. Wenn Sie Ihr benutzerdefiniertes CSS bearbeiten und speichern, wird die Vorschau aktualisiert.

**Ein [skeleton theme is available](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) für den Einstieg.**

Wenn Sie planen, Ihre CSS-Erstellung zu teilen, müssen Sie einige Punkte beachten. Erstens gibt es einige Körperklassen, auf die Stile angewendet werden müssen:

## Körperklassen

Die folgenden Stile müssen in jedem Marked-CSS enthalten sein, damit sie geteilt werden können. Mit den Körperklassen können Sie jeden Selektor unter verschiedenen Präferenzoptionen gezielt ansprechen und ändern.

### Invertiert

Wenn der Benutzer {% appmenu Vorschau, Dunkelmodus %} auswählt, wird dem Body-Tag die Klasse „invertiert“ hinzugefügt. Damit können Sie die kontrastreichen Hell-auf-Dunkel-Stile gezielt einsetzen.

Sie möchten, dass invertierte Stile nur auf die Vorschau angewendet werden, nicht auf den Druck. Verwenden Sie daher eine Medienabfrage (@media screen), um sie einzuschränken. Der folgende Code ist ziemlich universell einsetzbar und in den meisten Fällen können Sie ihn aus Kompatibilitätsgründen einfach in Ihr Stylesheet einfügen, Sie können ihn jedoch jederzeit anpassen.

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

### Poesie

Der Benutzer kann wählen, ob es sich bei Text mit Tabulatoreinzug um Poesie oder Code handelt. Der einzige Unterschied besteht darin, dass Vor-/Codeblöcke poetischer gestaltet werden, wenn der Poesiemodus ausgewählt wird. Die Klasse „Poetry“ wird auf das Body-Tag angewendet.

Seien Sie bei der Formatierung so kreativ, wie Sie möchten, aber hier ist ein einfacher Ausschnitt:

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

## Sonderfälle

Tabellen, Abbildungen/Bildunterschriften und der Sonderfall von `a.footnote` und `div.footnotes>a` müssen ebenfalls berücksichtigt werden. Es gibt keine festen Regeln für den Umgang damit, aber werfen Sie einen Blick auf die Standardstile, um eine Vorstellung davon zu bekommen, welche CSS-Regeln Marked benötigt.

Der standardmäßige Tabellenstil aller Standardstile verwendet Transparenz in den abwechselnden Zeilen, damit er sich sanft in jeden Hintergrund einfügt. Sie können diese Stile kopieren oder Ihren eigenen Weg gehen. Stellen Sie einfach sicher, dass Sie sie gestylt haben! Dasselbe gilt für Abbildung und Bildunterschrift; Fügen Sie einem Dokument ein Bild mit Alternativtext hinzu, um zu sehen, wie das Markup aussieht, und um es entsprechend zu formatieren.

In einem Dokument enthaltene Fußnoten stellen einen Link innerhalb des Inhalts dar (a.footnote) und am Ende ein div mit dem referenzierten Text (div.footnotes). Sehen Sie sich auch hier die Standardstile als Referenz an. Um zu vermeiden, dass sich die Zeilenhöhe in Zeilen ändert, die eine Fußnotenreferenznummer enthalten, fügen Sie unbedingt Folgendes ein:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Um den Zurück-Pfeil in derselben Zeile zu halten, schließen Sie Folgendes ein:

```css
.footnotes p {display:inline}
```

Es ist auch eine gute Idee, eine allgemeine Regel für alle Bilder einzufügen, um sie innerhalb der Seitenbreite zu halten. Etwas wie:

```css
#wrapper img { max-width: 100% }
```

Wenn Ihr Design über zusätzliche Polsterung oder eine feste Breite verfügt, ändern Sie die maximale Breite entsprechend.

## Druckstile

Stellen Sie sicher, dass Sie Druckstile einbinden, die jegliche Hintergrundfarben, festes Scrollen usw. entfernen. Verwenden Sie „@media print“, um sie in Ihrem Theme zu definieren.

Das Ausblenden von Links im Druck wird außerhalb des Hauptthemas gehandhabt, sodass Benutzer wählen können, ob Hervorhebungen und Unterstreichungen von Links im Ausdruck ausgeblendet werden sollen. Solange Sie einen Basisstil für den Text festgelegt haben, müssen Sie sich darüber keine Sorgen machen.

Also, nichts wie los. Konvertieren Sie Ihr Blog-Thema, erstellen Sie einen tollen Druckstil für PDF-Dokumente oder erstellen Sie die perfekte Vorschau für Ihren Schreibstil. Wenn Sie etwas Tolles machen, lassen Sie es mich wissen und ich werde es für die gesamte Marked-Community veröffentlichen.

## Zusätzliche CSS-Einstellungen

Im {% prefspane Style %} können Sie zusätzliches CSS bearbeiten. Diese Stile werden an jedes geladene Theme angehängt und können verwendet werden, um universelle Änderungen an allen Themes vorzunehmen.

Mithilfe von [high specificity](#overridingspecificity)- und @media-Abfragen für Druck und Bildschirm können Sie mit ein wenig CSS-Kenntnissen nahezu jeden Stilaspekt steuern.

## WebKit-Inspektor

Der Web Inspector von Safari ist die einfachste Möglichkeit, genau zu sehen, was HTML und CSS Marked generieren, und mit Custom-Stilen live zu experimentieren.

### Aktivieren des Entwicklungsmenüs in Safari

1. Öffnen Sie Safari und wählen Sie {% appmenu Safari, Einstellungen… %}.
2. Wählen Sie die Registerkarte **Erweitert**.
3. Aktivieren Sie **Funktionen für Webentwickler anzeigen** (oder **Entwicklungsmenü in der Menüleiste anzeigen** bei älteren macOS-Versionen).

Nach der Aktivierung erscheint in der Menüleiste von Safari ein **Entwickeln**-Menü.

![Safari Develop menu showing Marked documents][develop-menu]

### Ein Marked-Dokument prüfen

1. Wechseln Sie bei geöffnetem Vorschaufenster in Marked zu Safari.
2. Wählen Sie in der Menüleiste **Entwickeln → _\<Ihr Mac-Name\>_ → Marked → _\<Dokumenttitel\>_**.
3. Safari öffnet ein Web-Inspektor-Fenster, das an die ausgewählte Marked-Vorschau angehängt ist.

Von hier aus können Sie:

– Verwenden Sie die Registerkarte **Elemente**, um das DOM innerhalb des `#wrapper` div zu überprüfen und zu sehen, welche CSS-Regeln angewendet werden.
- Bewegen Sie den Mauszeiger über Elemente im DOM-Baum, um sie im Fenster Marked hervorzuheben.
- Verwenden Sie die Seitenleiste **Stile**, um Regeln live zu optimieren, und kopieren Sie dann Arbeitsausschnitte zurück in einen Custom-Stil oder **zusätzliches CSS**.
    - Nachdem Sie CSS auf der Registerkarte „Elemente“ bearbeitet haben, können Sie eine Zusammenfassung Ihrer Änderungen erhalten, indem Sie die Registerkarte „Änderungen“ auswählen

![Changes][css-changes]
- Verwenden Sie die Registerkarte **Konsole**, um JavaScript für die Live-Vorschau auszuführen. Das vollständige [Marked JavaScript API](https://markedapp.com/help/jsapi/) ist in dieser Konsole verfügbar.
- Erkunden Sie andere Registerkarten wie **Netzwerk**, wenn Sie von Ihrem Dokument geladene Ressourcen debuggen.

![Inspecting a Marked preview with Safari Web Inspector][inspecting]

## Teilen von Custom CSS

Verwenden Sie {% appmenu Stil, Eigenen Stil teilen %}, um die Sharing-App in Ihrem Webbrowser zu öffnen. Ziehen Sie Ihr CSS in die Drop-Zone (oder klicken Sie, um es von der Festplatte auszuwählen) und laden Sie das CSS für Ihren Custom-Stil hoch.

Freigegebene Stile müssen vom Entwickler genehmigt werden, bevor sie in der Galerie angezeigt werden. Sie sehen also keine unmittelbaren Ergebnisse.

## Weitere Tipps

### Übergeordnete Spezifität

Innerhalb der Marked-Vorschau wird eine Body-Klasse hinzugefügt, die auf dem Dateinamen des aktuellen Stils basiert. Wenn die Vorschau auf „Schweiz“ eingestellt ist, gibt es im Tag `<body>` eine Klasse namens `mkstyle--swiss`. Wenn Ihr benutzerdefiniertes CSS MyCustom.css heißt, lautet die Hauptklasse `mkstyle--mycustom`. Sie können dies vor den in den Basisstilen definierten Regeln verwenden, um diese zu überschreiben. Um absolute Spezifität in einer Regel zu erhalten, verwenden Sie auch die #wrapper-ID aus dem Container-Div:

.mkstyle--mycustom #wrapper p+p { ... }

### Gestaltung des Inhaltsverzeichnisses

Wenn Sie das Token `<!--toc-->` für [insert a table of contents](Special_Syntax.html#tableofcontents) verwenden, können Sie die Einstellungen für Inhaltsverzeichnis-Ebenenindikatoren in einem Custom-Stil überschreiben, indem Sie den „#wrapper“ verwenden, um die Spezifität zu erhöhen:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Dies würde dazu führen, dass alle Listenelemente im Inhaltsverzeichnis ein quadratisches Aufzählungszeichen anstelle dessen verwenden, was in den Einstellungen definiert wurde, als Ihr Custom-Stil aktiv ist.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
