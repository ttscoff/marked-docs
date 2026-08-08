# <%= @title %>

Optionen unter {% prefspane Style %}:

![Einstellungen: Stil][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout und Typografie [layout-and-typography]

Textbreite in der Vorschau begrenzen
: Legt mit dem Schieberegler eine maximale Breite (in Pixeln) für den Textbereich der Vorschau fest.

Automatische Silbentrennung in Absätzen
: Erlaubt die automatische Silbentrennung von Wörtern.

Hurenkinder in Überschriften und Absätzen verhindern
: Erzwingt ein geschütztes Leerzeichen zwischen den letzten beiden Wörtern von Überschriften und Absätzen, damit einzelne Wörter nicht in eine neue Zeile umbrechen.

Typografisch korrekte Anführungszeichen und Zeichensetzung generieren
: Verwendet SmartyPants für typografische Anführungszeichen, die Umwandlung von Auslassungspunkten und weitere Typografie-Funktionen (MultiMarkdown).

Fußnotenmarkierungen mit eckigen Klammern umgeben
: Ist dies aktiviert, wird die Standard-MultiMarkdown-Formatierung für Fußnotenmarkierungen ([1]) verwendet. Deaktivieren, um die eckigen Klammern zu entfernen.

Gliederung für Erweiterungen aktivieren
: Aktiviert den Gliederungsmodus automatisch für Dateien mit den aufgeführten Erweiterungen.

APA-Stil verwenden
: Verwendet APA-Gliederungen statt des standardmäßigen Dezimalformats.

Wörtliche (Code-)Blöcke als Poesie stilisieren
: Ist dies aktiviert, wird per Tab eingerückter, abgegrenzter oder eingebundener Code als Poesie statt als Codeblock dargestellt (ohne Syntaxhervorhebung und mit je nach Stil besonderer Formatierung).

Stilen erlauben, Text in Codeblöcken umzubrechen
: Ist dies aktiviert, dürfen Stile innerhalb von `pre>code`-Blöcken Umbrüche erzeugen. Ist es deaktiviert, wird bei horizontalem Überlauf immer gescrollt.

Code immer umbrechen
: Erzwingt den Umbruch von Codeblöcken unabhängig von den Stileinstellungen (überschreibt das Umbruchverhalten des Stils).

RTL-Text erkennen und formatieren
: Erkennt die Sprache je Element im Dokument und formatiert Rechts-nach-links-Text entsprechend.

### Stil [theme]

Stile verwalten
: Öffnet das Fenster [Stil-Manager](Style_Manager.html). Fügen Sie CSS-Dateien von Ihrem Laufwerk hinzu, damit sie in den Stilauswahl-Menüs erscheinen. Verwenden Sie die Schaltfläche „Neuen Stil hinzufügen“ oder ziehen Sie CSS-Dateien in dieses Fenster. Ziehen Sie zum Umsortieren, und aktivieren oder deaktivieren Sie Stile über die Kontrollkästchen.

Weitere Stile
: Öffnet die Online-Stil-Galerie, um weitere Stile zu durchsuchen und zu installieren.

Standardstil
: Der hier ausgewählte Stil wird für alle neuen Fenster geladen, sofern nicht in den Metadaten ein [dokumentspezifischer Stil angegeben ist](Per-Document_Settings.html) (z. B. „Marked Style: Grump“).

CSS-Änderungen verfolgen
: Ist dies aktiviert, überwacht Marked den aktuellen Stil auf Änderungen auf der Festplatte, was beim Bearbeiten eigener Stile und in der Webentwicklung hilft.

Zusätzliches CSS
: Hier hinzugefügtes CSS wird bei allen Stilen nach dem normalen Stylesheet eingebunden. Unter anderem können Sie damit Einstellungen flächendeckend überschreiben, ohne interne Stile zu bearbeiten.
: Das gilt für alle Dokumente und alle Stile. Wollen Sie eigenes CSS je nach Bedingung auf Dokumente anwenden, verwenden Sie Eigene Regeln unter {% prefspane Processor %}.

### Skripte einbinden [include-scripts]

Syntaxhervorhebung
: Aktiviert die highlight.js-[Syntaxhervorhebung](Syntax_Highlighting.html) für Codeblöcke. Wählen Sie einen Stil aus dem Dropdown-Menü.
: Ist **Nur wenn Sprache angegeben** aktiviert, wird die Syntaxhervorhebung nur auf abgegrenzte Codeblöcke mit angegebener Sprache angewendet.

MathJax aktivieren
: Lädt [MathJax](MathJax.html) zur Darstellung von MathML-Gleichungen. Wählen Sie **Lokal** (mitgeliefert) oder **CDN** aus dem Dropdown-Menü.
: **Zusätzliche Pakete** öffnet ein Blatt, um weitere MathJax-Pakete einzubinden (zum Beispiel Physics und Chemistry).
: **Erweiterte Konfiguration** öffnet ein Blatt für eine eigene MathJax-Konfiguration.

KaTeX aktivieren
: Lädt [KaTeX](MathJax.html#katex) als Alternative zu MathJax. Es kann nur eines von beiden ausgewählt werden.

Gleichungen nummerieren
: Sofern zutreffend, ergänzt Marked gerenderte Gleichungen um Formelnummern. Wählen Sie **Linke Seite** oder **Rechte Seite** für die Nummerierung. Mit MathJax können Sie **Nur AMS** wählen, um nur AMS-Gleichungen zu nummerieren.

Mermaid
: Lädt [mermaid.js](https://mermaid.js) von einem CDN, um Diagramme im Markdown-Stil zu ermöglichen. Der Hook, der zum Rendern von Mermaid-Diagrammen bei jeder Dokumentaktualisierung nötig ist, wird automatisch eingebunden.

Diagramme schwenken und zoomen
: Sind Mermaid-Diagramme vorhanden, aktiviert dies das Zoomen mit {% kbd cmd %}-Scrollen und das Verschieben durch Klicken und Ziehen.
