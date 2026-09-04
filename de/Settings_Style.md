# <%= @title %>

Optionen im {% prefspane Style %}:

![Einstellungen: Stil][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout und Typografie [layout-and-typography]

Textbreite in der Vorschau begrenzen
: Legt mit dem Schieberegler eine maximale Breite für den Vorschau-Text fest (in Pixel).

Automatische Silbentrennung in Absätzen
: Erlaubt es, Wörter automatisch durch Silbentrennung umzubrechen.

Hurenkinder in Überschriften und Absätzen verhindern
: Erzwingt ein geschütztes Leerzeichen zwischen den letzten beiden Wörtern von Überschriften und Absätzen, damit kein einzelnes Wort in eine neue Zeile umbricht.

Typografisch korrekte Anführungszeichen und Interpunktion erzeugen
: Verwendet SmartyPants für typografische Anführungszeichen, die Umwandlung von Auslassungspunkten und weitere Typografie-Funktionen (MultiMarkdown).

Fußnotenmarker in eckige Klammern setzen
: Wenn aktiviert, wird die MultiMarkdown-Standardformatierung für Fußnotenmarker verwendet ([1]). Deaktivieren Sie die Option, um die eckigen Klammern zu entfernen.

Gliederungsmodus für Dateierweiterungen aktivieren
: Aktiviert den Gliederungsmodus automatisch für Dateien mit den aufgeführten Erweiterungen.

APA-Stil verwenden
: Verwendet Gliederungen im APA-Stil anstelle des standardmäßigen Dezimalformats.

Wörtliche (Code-)Blöcke als Gedicht darstellen
: Wenn aktiviert, werden tab-eingerückter, abgegrenzter oder eingebundener Code als Gedicht statt als Codeblock dargestellt (keine Syntaxhervorhebung, spezielles Styling je nach Stil).

Stilen erlauben, Text in Codeblöcken umzubrechen
: Wenn aktiviert, dürfen Stile einen Zeilenumbruch innerhalb von `pre>code`-Blöcken bewirken. Wenn deaktiviert, wird bei horizontalem Überlauf immer gescrollt.

Code immer umbrechen
: Erzwingt den Zeilenumbruch in Codeblöcken unabhängig von den Stil-Einstellungen (überschreibt das Umbruchverhalten des Stils).

RTL-Text erkennen und formatieren
: Erkennt die Sprache für jedes Element im Dokument und formatiert sie bei Bedarf von rechts nach links (RTL).

### Stil [theme]

Stile verwalten
: Öffnet das Fenster [Stil-Manager](Style_Manager.html). Fügen Sie CSS-Dateien von Ihrer Festplatte hinzu, damit sie in den Stilauswahlmenüs erscheinen. Verwenden Sie die Schaltfläche `Add New Style` oder ziehen Sie CSS-Dateien in dieses Fenster. Ziehen Sie zum Umsortieren, und verwenden Sie die Kontrollkästchen, um Stile zu aktivieren oder zu deaktivieren.

Weitere Stile
: Öffnet die Online-Stilgalerie, um zusätzliche Stile zu durchsuchen und zu installieren.

Standardstil
: Der hier ausgewählte Stil wird für alle neuen Fenster geladen, sofern nicht [in den Metadaten ein dokumentspezifischer Stil angegeben ist](Per-Document_Settings.html) (z. B. „Marked Style: Grump“).

CSS-Änderungen verfolgen
: Wenn aktiviert, überwacht Marked den aktuellen Stil auf Änderungen auf der Festplatte, was die Bearbeitung eigener Stile und die Webentwicklung erleichtert.

Zusätzliches CSS
: Hier hinzugefügtes CSS wird nach dem normalen Stylesheet jedes Stils angehängt. Es handelt sich um eine partielle Ergänzung, keinen vollständigen Ersatzstil.
: Marked schreibt Selektoren in diesem Feld um (Druckregeln sollten beispielsweise `body.mkprinting #wrapper …` verwenden). Es gibt keine Größen- oder Gültigkeitsprüfung – siehe [Eigenes CSS erstellen](Writing_Custom_CSS.html#additional-css-settings).
: Dies gilt für alle Dokumente und alle Stile, einschließlich des HTML-Exports, wenn Stile eingeschlossen werden. Wenn Sie eigenes CSS abhängig von Bedingungen auf Dokumente anwenden möchten, verwenden Sie Eigene Regeln unter {% prefspane Processor %}.

### Skripte laden [include-scripts]

Syntaxhervorhebung
: Aktiviert die highlight.js-[Syntaxhervorhebung](Syntax_Highlighting.html) für Codeblöcke. Wählen Sie einen Stil aus dem Einblendmenü.
: Wenn **Nur bei angegebener Sprache** aktiviert ist, wird die Syntaxhervorhebung nur auf abgegrenzte Codeblöcke mit angegebener Sprache angewendet.

MathJax aktivieren
: Lädt [MathJax](MathJax.html) zur Anzeige von MathML-Gleichungen. Wählen Sie **Lokal** (im Programm enthalten) oder **CDN** aus dem Einblendmenü.
: **Zusätzliche Pakete** öffnet ein Sheet, um weitere MathJax-Pakete einzubinden (zum Beispiel Physics und Chemistry).
: **Erweiterte Konfiguration** öffnet ein Sheet für eine benutzerdefinierte MathJax-Konfiguration.

KaTeX aktivieren
: Lädt [KaTeX](MathJax.html#katex) als Alternative zu MathJax. Es kann jeweils nur eines von beiden ausgewählt werden.

Gleichungen nummerieren
: Falls zutreffend, fügt Marked den gerenderten Gleichungen Abbildungsnummern hinzu. Wählen Sie für die Nummerierung **Linke Seite** oder **Rechte Seite**. Bei Verwendung von MathJax können Sie **Nur AMS** wählen, um nur AMS-Gleichungen zu nummerieren.

Mermaid
: Lädt [mermaid.js](https://mermaid.js) von einem CDN, um Markdown-artiges Diagrammzeichnen zu ermöglichen. Der für die Darstellung von Mermaid-Diagrammen bei jeder Dokumentaktualisierung erforderliche Hook wird automatisch eingebunden.

Diagramme verschieben und zoomen
: Wenn Mermaid-Diagramme vorhanden sind, aktiviert dies das Zoomen per {% kbd cmd %}-Scrollen und das Verschieben durch Klicken und Ziehen.
