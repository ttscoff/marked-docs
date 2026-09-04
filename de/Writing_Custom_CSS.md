# <%= @title %>

Marked verfügt über einen integrierten Stil-Editor und kann eigene CSS-Dateien anwenden.

Sie können den Editor nutzen, um wunderschöne Stile zu erstellen, oder – wenn Sie gerade genug CSS können, um gefährlich zu sein – Marked so aussehen lassen, wie Sie möchten.

## Erste Schritte [getting-started]

Es gibt eine Galerie mit Eigenen Stilen, die vom Entwickler und von Nutzern erstellt wurden, unter [markedapp.com/styles](https://markedapp.com/styles/). In der Galerie können Sie Stile direkt in Marked in der Vorschau ansehen und installieren. Jeder installierte Stil kann im Finder angezeigt werden, um ihn zu untersuchen und zu bearbeiten. Die Galerie lässt sich mit {% appmenu Style, Generate a Custom Style %} in einem internen Betrachter öffnen, oder Sie klicken im Stil-Manager auf das Bleistift-Symbol (Bearbeiten) neben einem bearbeitbaren Stil. Wenn Sie einen integrierten Stil bearbeiten möchten, müssen Sie ihn im Manager zunächst duplizieren.

Es gibt außerdem ein [Repository für Eigene Stile](https://github.com/ttscoff/MarkedCustomStyles) auf GitHub mit Beispielen. Schauen Sie sich dort gerne um, nutzen Sie die Vorlagen und tragen Sie eigene Beiträge bei. Wenn Sie ein Theme veröffentlichen, das auf einem der Basis-Themes aufbaut, dürfen Sie sich gerne selbst als Mitwirkende(r) in die Credits eintragen.

Mit Marked' Möglichkeit, eigene CSS-Dateien zu verwenden, sind beim Anpassen der Vorschau praktisch keine Grenzen gesetzt. Alle CSS3-Optionen, die in Safari funktionieren, funktionieren auch in Marked. Bei Standard-Markdown-Dateien in Marked müssen Sie nur wenige HTML-Elemente berücksichtigen; der gesamte Inhalt befindet sich in einem div mit der ID „wrapper“, alles Weitere ergibt sich aus der Auszeichnung Ihres Dokuments.

Wenn Sie nur für den Eigenbedarf gestalten, gibt es keine Regeln. Aktivieren Sie die CSS-Verfolgung über das Kontrollkästchen unter dem Auswahlfeld für eigenes CSS – wenn Sie Ihr eigenes CSS bearbeiten und speichern, wird die Vorschau automatisch aktualisiert.

**Ein [Grundgerüst-Theme](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) steht als Ausgangspunkt zur Verfügung.**

Wenn Sie Ihre CSS-Kreation weitergeben möchten, gibt es einige Punkte zu beachten. Zunächst gibt es einige Body-Klassen, denen Stile zugewiesen werden müssen:

## Body-Klassen [body-classes]

Die folgenden Stile müssen in jedem CSS enthalten sein, das für Marked weitergegeben werden soll. Über die Body-Klassen können Sie Selektoren gezielt ansprechen und je nach Einstellungsoption anpassen.

### Invertiert [inverted]

Wenn der Nutzer {% appmenu Preview, Dark Mode %} auswählt, wird dem body-Tag die Klasse „inverted“ hinzugefügt. Damit können Sie die kontrastreichen, hellen Stile auf dunklem Hintergrund gezielt ansprechen.

Invertierte Stile sollen nur in der Vorschau gelten, nicht beim Drucken – schränken Sie das daher mit einer Media Query (@media screen) ein. Der folgende Code ist recht universell einsetzbar; in den meisten Fällen können Sie ihn einfach zur Kompatibilität in Ihr Stylesheet übernehmen, aber passen Sie ihn gerne an.

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

### Lyrik [poetry]

Der Nutzer kann wählen, ob mit Tabs eingerückter Text als Lyrik oder als Code behandelt wird. Der einzige Unterschied besteht darin, dass pre/code-Blöcke im Lyrik-Modus, sagen wir, poetischer gestaltet werden. Dem body-Tag wird die Klasse „poetry“ zugewiesen.

Werden Sie bei der Formatierung so kreativ, wie Sie möchten – hier ein einfaches Grundgerüst:

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

Auch Tabellen, Figure/Figcaption sowie der Sonderfall von `a.footnote` und `div.footnotes>a` müssen berücksichtigt werden. Es gibt keine festen Regeln, wie Sie damit umgehen, aber ein Blick auf die Standardstile vermittelt einen Eindruck, welche CSS-Regeln Marked benötigt.

Die Standard-Tabellengestaltung in allen mitgelieferten Stilen nutzt Transparenz bei den abwechselnden Zeilen, damit sie sich sanft in jeden Hintergrund einfügen. Sie können diese Stile übernehmen oder einen eigenen Weg gehen – stellen Sie nur sicher, dass Sie sie gestaltet haben! Das Gleiche gilt für figure und figcaption; fügen Sie einem Dokument ein Bild mit Alt-Text hinzu, um zu sehen, wie die Auszeichnung ausgegeben wird, und gestalten Sie sie entsprechend.

Fußnoten in einem Dokument erzeugen einen Link im Inhalt (a.footnote) sowie ein div am Ende mit dem referenzierten Text (div.footnotes). Auch hier lohnt ein Blick auf die Standardstile als Referenz. Damit sich der Zeilenabstand bei Zeilen mit einer Fußnoten-Referenznummer nicht ändert, sollten Sie etwas wie Folgendes einbinden:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

Damit der Rücksprungpfeil in derselben Zeile bleibt, fügen Sie hinzu:

```css
.footnotes p {display:inline}
```

Es empfiehlt sich außerdem, eine allgemeine Regel für alle Bilder einzubinden, damit diese die Seitenbreite nicht überschreiten. Etwa so:

```css
#wrapper img { max-width: 100% }
```

Wenn Ihr Theme zusätzliches Padding oder eine feste Breite verwendet, passen Sie max-width entsprechend an.

## Druckstile [printstyles]

Achten Sie darauf, Druckstile einzubinden, die Hintergrundfarben, fixiertes Scrollen und reine Vorschau-Bedienelemente entfernen. Marked bietet Ihnen zwei Möglichkeiten, Druck- und PDF-Ausgabe gezielt anzusprechen.

### `@media print` [media-print]

Beim Drucken aus Marked oder wenn der PDF-Export das Print-Medium verwendet, gelten die üblichen CSS-Druckregeln:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### Die Klasse `.mkprinting` [the-mkprinting-class]

Wenn Marked ein Dokument für den **PDF-Export** oder die **Druck-/PDF-Vorschau** ({% kbd cmd P %}) vorbereitet, fügt es dem `<body>`-Tag die Klasse `mkprinting` hinzu (zusammen mit Export-Klassen wie `bandw`, `breakAfterTOC` und der `mkstyle--*`-Klasse Ihres Stils). Die integrierten Themes von Marked nutzen für die meisten druckspezifischen Regeln diese Klasse, statt sich allein auf `@media print` zu verlassen.

Beim PDF-Export lädt Marked die versteckte Render-WebView häufig mit dem Medium **screen** (insbesondere bei eigenen Stilen und [Fountain](Fountain_for_Screenwriters.html)-Dokumenten), sodass `@media print`-Blöcke in Ihrem Stylesheet auf die PDF-Ausgabe **nicht** angewendet werden. Regeln mit dem Präfix `.mkprinting` gelten beim Export immer, da es sich um gewöhnliche Klassenselektoren und nicht um Media Queries handelt.

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

Bei Stilen, die sowohl beim Drucken über den Browser als auch beim PDF-Export von Marked funktionieren müssen, duplizieren Sie zentrale Regeln oder kombinieren Sie Selektoren:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**Eigener Stil vs. Zusätzliches CSS.** In einem Eigenen Stil-Stylesheet schreiben Sie `.mkprinting #wrapper …` wie oben gezeigt. Im Feld **Zusätzliches CSS** schreibt Marked Selektoren vor dem Einfügen um – verwenden Sie stattdessen die body-qualifizierte Form:

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

Unter [Einstellungen für zusätzliches CSS](#additional-css-settings) erfahren Sie, wie dieses Umschreiben funktioniert und warum `.mkprinting #wrapper …` dort allein nicht passt.

Beim Debuggen eigener Druck-CSS öffnen Sie die Druck-/PDF-Vorschau oder exportieren als PDF und untersuchen das Dokument dann mit [Safaris Web Inspector](#webkitinspector) – `<body>` trägt dann die Klasse `mkprinting`, solange das Druck-Layout aktiv ist.

Das Ausblenden von Links im Druck erfolgt außerhalb des eigentlichen Themes, sodass Nutzer wählen können, ob Link-Hervorhebungen und -Unterstreichungen im Ausdruck ausgeblendet werden. Solange Sie einen Basisstil für den Text festgelegt haben, müssen Sie sich darum nicht kümmern.

Also, legen Sie los. Übertragen Sie Ihr Blog-Theme, gestalten Sie einen genialen Druckstil für PDF-Dokumente, oder entwickeln Sie die perfekte Vorschau für Ihren Schreibstil. Wenn Sie etwas Großartiges erstellt haben, [teilen Sie es mit der Community](https://markedapp.com/styleshare/).

## Einstellungen für zusätzliches CSS [additional-css-settings]

Unter {% prefspane Style %} können Sie **Zusätzliches CSS** bearbeiten. Diese Regeln werden **an das jeweils geladene Theme angehängt**. Sie sind bewusst als teilweise Überlagerung gedacht, nicht als vollständiges Theme. Wenn Sie ein komplettes Stylesheet in dieses Feld einfügen – oder dasselbe Teil-Stylesheet über den [Stil-Manager](Custom_Styles.html) importieren, als wäre es ein Theme – bleibt alles, was das Stylesheet nicht abdeckt, ungestaltet.

### Selektor-Umschreibung [additional-css-selector-rewriting]

Marked schreibt Selektoren im Zusätzlichen CSS um, bevor es sie (als `body.mk-has-additional-css …`) einfügt, damit die Regeln auf die Vorschau begrenzt bleiben:

- Ein Selektorteil, der bereits mit `body` oder `#wrapper` beginnt, erhält das Präfix `body.mk-has-additional-css`, wobei Body-Klassen zusammengeführt statt verschachtelt werden.
- Jeder andere Selektorteil wird unter `body.mk-has-additional-css #wrapper …` eingegrenzt.
- Führende Body-Klassen, die Marked auf `<body>` setzt – darunter `.mkprinting`, `.inverted`, `.poetry`, `.bandw`, `.breakAfterTOC` und `.mkstyle--*` – werden wie `body` behandelt und mit dem body-Selektor zusammengeführt, statt unter `#wrapper` verschachtelt zu werden.

| Eingabe im Zusätzlichen CSS | Ergebnis |
| :-- | :-- |
| `#wrapper h2` | Passt (korrekt eingegrenzt) |
| `body.mkprinting #wrapper p` | Passt beim Drucken/PDF |
| `.mkprinting #wrapper p` | Passt **nicht** (würde ein verschachteltes `#wrapper` erfordern) |
| `:root { --x: 1; }` | Passt **nicht** (für benutzerdefinierte Eigenschaften eher `body` oder `#wrapper` verwenden) |

Für Druckregeln in diesem Feld empfiehlt sich `body.mkprinting #wrapper …`. Dieselbe optische Absicht kann in einer Eigenen-Stil-Datei die kürzere Form `.mkprinting #wrapper …` beibehalten.

Für Zusätzliches CSS gibt es **weder eine Größenbeschränkung noch eine CSS-Gültigkeitsprüfung**. Marked speichert und fügt genau das ein, was Sie eingeben; ungültiges CSS hat in der Vorschau einfach keine Wirkung.

### HTML und andere Exporte [additional-css-exports]

Zusätzliches CSS gilt in der Live-Vorschau, der Druck-/PDF-Vorschau, beim PDF-Export und beim **HTML-Export**, sofern Stile eingebunden werden – das exportierte `<body>` erhält die Klasse `mk-has-additional-css`, damit die umgeschriebenen Selektoren passen. DOCX, ODT und EPUB verwenden eigene Stilpfade und wenden Zusätzliches CSS nicht auf dieselbe Weise an.

Mit [hoher Spezifität](#overridingspecificity), `@media`-Abfragen für Druck und Bildschirm sowie `body.mkprinting`-Selektoren (in diesem Feld) bzw. `.mkprinting`-Selektoren (in Eigenen Stilen) lässt sich mit ein wenig CSS-Kenntnis so gut wie jeder Aspekt der Gestaltung steuern.

## WebKit Inspector [webkitinspector]

Safaris Web Inspector ist der einfachste Weg, um genau zu sehen, welches HTML und CSS Marked erzeugt, und um live mit Eigenen Stilen zu experimentieren.

### Das Entwickler-Menü in Safari aktivieren [enabling-the-develop-menu-in-safari]

1. Öffnen Sie Safari und wählen Sie {% appmenu Safari, Settings… %}.
2. Wählen Sie den Reiter **Erweitert**.
3. Aktivieren Sie **Features für Webentwickler anzeigen** (bzw. **Entwickler-Menü in der Menüleiste anzeigen** unter älteren macOS-Versionen).

Sobald dies aktiviert ist, erscheint in der Menüleiste von Safari ein Menü **Entwickler**.

![Safari-Entwicklermenü mit Marked-Dokumenten][develop-menu]

### Ein Marked-Dokument untersuchen [inspecting-a-marked-document]

1. Öffnen Sie in Marked ein Vorschaufenster und wechseln Sie dann zu Safari.
2. Wählen Sie in der Menüleiste **Entwickler → _\<Name Ihres Macs\>_ → Marked → _\<Dokumenttitel\>_**.
3. Safari öffnet ein Web-Inspector-Fenster, das mit der ausgewählten Marked-Vorschau verbunden ist.

Von hier aus können Sie:

- Im Reiter **Elemente** das DOM innerhalb des `#wrapper`-div untersuchen und sehen, welche CSS-Regeln angewendet werden.
- Elemente im DOM-Baum mit der Maus überfahren, um sie im Marked-Fenster hervorzuheben.
- In der Seitenleiste **Stile** Regeln live anpassen und funktionierende Schnipsel anschließend in einen Eigenen Stil oder in **Zusätzliches CSS** übertragen.
    - Nachdem Sie CSS im Reiter „Elemente“ bearbeitet haben, erhalten Sie über den Reiter „Änderungen“ eine Zusammenfassung Ihrer Bearbeitungen

	![Änderungen][css-changes]
- Im Reiter **Konsole** JavaScript gegen die Live-Vorschau ausführen. In dieser Konsole steht die vollständige [Marked-JavaScript-API](https://markedapp.com/help/jsapi/) zur Verfügung.
- Weitere Reiter wie **Netzwerk** erkunden, wenn Sie von Ihrem Dokument geladene Ressourcen debuggen.

![Untersuchen einer Marked-Vorschau mit Safaris Web Inspector][inspecting]

## Eigenes CSS teilen [sharing-custom-css]

Verwenden Sie {% appmenu Style, Share a Custom Style %}, um die Sharing-App in Ihrem Webbrowser zu öffnen. Ziehen Sie Ihr CSS in die Ablagezone (oder klicken Sie, um es von der Festplatte auszuwählen), und laden Sie das CSS für Ihren Eigenen Stil hoch.

Geteilte Stile müssen vor der Veröffentlichung in der Galerie vom Entwickler freigegeben werden – ein sofortiges Ergebnis ist also nicht zu erwarten.

## Weitere Tipps [other-tips]

### Spezifität überschreiben [overridingspecificity]

Innerhalb der Marked-Vorschau wird eine Body-Klasse hinzugefügt, die auf dem Dateinamen des aktuellen Stils basiert. Ist die Vorschau auf „Swiss“ eingestellt, trägt das `<body>`-Tag eine Klasse namens `mkstyle--swiss`. Heißt Ihr eigenes CSS MyCustom.css, lautet die Body-Klasse `mkstyle--mycustom`. Diese können Sie vor den in den Basisstilen definierten Regeln einsetzen, um diese zu überschreiben. Um in einer Regel absolute Spezifität zu erreichen, verwenden Sie zusätzlich die ID #wrapper des Container-div:

	.mkstyle--mycustom #wrapper p+p { ... }

### Gestaltung des Inhaltsverzeichnisses [table-of-contents-styling]

Wenn Sie mit dem Token `<!--toc-->` ein [Inhaltsverzeichnis einfügen](Special_Syntax.html#tableofcontents), können Sie die Einstellungen für die Ebenenkennzeichnung des Inhaltsverzeichnisses in einem Eigenen Stil überschreiben, indem Sie mit „#wrapper“ die Spezifität erhöhen:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

Dadurch würden alle Listenelemente im Inhaltsverzeichnis einen quadratischen Aufzählungspunkt verwenden statt dem, was in den Einstellungen festgelegt wurde, sobald Ihr Eigener Stil aktiv ist.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
