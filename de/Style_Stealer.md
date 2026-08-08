# <%= @title %>

Extrahieren und stehlen Sie Stile von jeder Website.

## Was ist der Style Stealer? [what-is-the-style-stealer]

Der Style Stealer ist ein Tool, mit dem Sie CSS-Stile von jeder Website extrahieren und als [Eigene Stile](Custom_Styles.html) auf Ihre Markdown-Dokumente anwenden. Er ist perfekt für:

- **Blogger**, die das Design ihrer Lieblingswebsites anpassen möchten
- **Autoren**, die Dokumente erstellen müssen, die zu einer bestimmten Marke oder Publikation passen
- **Entwickler**, die schnell Prototypen mit vorhandenen Designsystemen erstellen möchten
- **Jeder**, der das Erscheinungsbild einer gut gestalteten Website einfangen möchte

> Der Style Stealer setzt voraus, dass eine Website relativ übersichtlich aufgebaut ist und klare Markup-Unterteilungen hat. Er funktioniert nicht auf jeder Website, macht auf den meisten aber einen guten Job.

> Um die besten Ergebnisse zu erzielen, geben Sie eine Seite ein, die möglichst viel Textinhalt enthält. Um beispielsweise Stile aus einem Blog zu extrahieren, öffnen Sie direkt einen Artikel oder Beitrag und nicht die Hauptindexseite.

## So verwenden Sie den Style Stealer [how-to-use-the-style-stealer]

### Schritt 1: Öffnen Sie den Style Stealer [step-1-open-the-style-stealer]

Greifen Sie über **Hilfe** → **Style Stealer** auf den Style Stealer zu.

### Schritt 2: Geben Sie eine URL ein [step-2-enter-a-url]

Geben Sie im URL-Feld die Adresse der Website ein, von der Sie Stile extrahieren möchten. Der Style Stealer funktioniert mit jeder öffentlich zugänglichen Website. Wenn sich die Website hinter einer Paywall befindet, müssen Sie sich möglicherweise anmelden, um den Inhalt extrahieren zu können.

![Style Stealer Preview][preview]

  [preview]: images/style-stealer-preview.jpg @2x width=800

### Schritt 3: Laden und navigieren [step-3-load-and-navigate]

Klicken Sie auf **Extrahieren** oder drücken Sie {% kbd return  %}, um die Website zu laden. Nach dem Laden können Sie:

- **Navigieren** Sie mit Cmd-Klick auf Links durch die Website
- **Fahren Sie** mit dem Zeiger über Inhaltsbereiche, um sie hervorgehoben zu sehen
- **Klicken** Sie auf den Hauptinhaltsbereich, aus dem Sie Stile extrahieren möchten

Der von Ihnen ausgewählte Hauptinhaltsbereich sollte nur Überschriften, Absätze, Listen usw. enthalten. Wählen Sie keinen Inhaltsbereich aus, der Menüs, Seitenleisten oder andere überflüssige Inhalte enthält. Häufig befindet sich eine Überschrift in einem vom regulären Absatzinhalt getrennten Container. Versuchen Sie in diesen Fällen zunächst, den kleinsten Behälter auszuwählen, der noch beides enthält. Wenn die Ergebnisse schlecht sind, klicken Sie erneut auf **Extrahieren** und wählen Sie erneut nur den Container aus, der die Absätze enthält.

### Schritt 4: Stile extrahieren [step-4-extract-styles]

Wenn Sie auf den Inhaltsbereich klicken, werden die für diesen Bereich geltenden Stile extrahiert. Die Vorschau wird mit einer generischen Seite neu geladen, die alle gängigen HTML-Elemente und die Art und Weise zeigt, wie die extrahierten Stile auf sie angewendet werden.

Sie können diesen Eigenen Stil dann in Ihrem Ordner für eigenes CSS speichern, um ihn in jedem Dokument zu verwenden. Klicken Sie auf die Schaltfläche **Speichern** oder drücken Sie {% kbd cmd S %} zum Speichern. Der Stil wird nach der Domain der eingegebenen URL benannt.

![][img3]

  [img3]: images/style-stealer-stolen-800.jpg @2x width=800px height=637px class=center

## Was extrahiert wird [what-gets-extracted]

Der Style Stealer erfasst einen umfassenden Satz an Stilen, darunter:

### Typografie [typography]

- **Schriftfamilien** und -größen für alle Überschriftenebenen (H1-H6)
- **Absatzstil** einschließlich Zeilenhöhe und -abstand
- **Textfarben** und Hintergrundfarben
- **Schriftstärken** und -stile (fett, kursiv usw.)

### Layout und Abstand [layout-and-spacing]

- **Ränder und Innenabstände** für alle Elemente
- **Rand**-Stile und -Farben
- **Hintergrundfarben** einschließlich `body`-Hintergründen für dunkle Designs

### Interaktive Elemente [interactive-elements]

- **Link-Stile** einschließlich Hover und besuchte Zustände
- Stylen von **Schaltflächen** und Formularelementen
- **Listen**-Styling (Aufzählungszeichen, Zahlen, Einrückungen)

### Besondere Merkmale [special-features]

- Gestaltung des **Ersten Absatzes**
- **Blockquote**-Formatierung
- **Code** und vorformatierter Textstil
- **Tabellen**-Styling
- **Benutzerdefinierte Schriftarten** und Web-Schriftarten

## Erweiterte Funktionen [advanced-features]

### Medienblockierung [media-blocking]

Der Style Stealer blockiert automatisch Medieninhalte (Videos, Bilder, Audio), um Abstürze zu verhindern und sich auf die Textgestaltung zu konzentrieren. Dies gewährleistet einen reibungslosen Extraktionsprozess auch auf medienintensiven Websites.

### Pseudo-Selektor-Unterstützung [pseudo-selector-support]

Das Tool erfasst CSS-Pseudoselektoren wie:

- `:hover` Zustände für Links und Schaltflächen
- `:visited` Linkstatus
- `:first-child` Absatzstil
- `::first-letter` für Initialen

### Intelligente Filterung [smart-filtering]

Der Style Stealer filtert intelligent heraus:

- Standard-Browserstile
- Unnötige Herstellerpräfixe
- Widersprüchliche oder redundante Regeln
- Stile, die den Text unleserlich machen würden

### Debug-Modus [debug-mode]

Aktivieren Sie den Debug-Modus im Style Stealer, um eine detaillierte Protokollierung des Extraktionsprozesses anzuzeigen. Dies ist hilfreich, um Fehler zu beheben oder zu verstehen, welche Stile erfasst werden.

## Tipps für beste Ergebnisse [tips-for-best-results]

### Wählen Sie den richtigen Inhaltsbereich [choose-the-right-content-area]

- Klicken Sie auf den **Hauptinhaltsbereich** der Seite, nicht auf Kopfzeilen, Seitenleisten oder Fußzeilen
- Suchen Sie nach dem Bereich, der den Artikeltext, den Blogbeitrag oder den Hauptinhalt enthält
- Vermeiden Sie Bereiche mit starkem JavaScript oder dynamischen Inhalten

### Dunkle Designs handhaben [handle-dark-themes]

Der Style Stealer erfasst automatisch die `body`-Hintergrundfarben und eignet sich daher perfekt zum Extrahieren dunkler Design-Stile. Die Vorschau zeigt, wie Ihr Inhalt mit dem extrahierten dunklen Stil aussieht.

### Überlegungen zur Schriftart [font-considerations]

- **Web-Schriftarten** werden erfasst und in die extrahierten Stile einbezogen
  - Schriftarten, die von einer Remote-URL (z. B. Google Fonts) geladen werden, behalten diese URL bei. Von Daten-URLs geladene Schriftarten werden im generierten Stylesheet dupliziert.
- **Systemschriftarten** weichen auf verschiedenen Systemen elegant auf Alternativen aus
- **Das Laden der Schriftart** kann in der Vorschau einen Moment dauern

### Testen Sie Ihre Stile [testing-your-styles]

Nach dem Speichern der extrahierten Stile:

1. Wenden Sie sie auf ein Testdokument an
2. Überprüfen Sie, wie sie mit Ihrem tatsächlichen Inhalt aussehen
3. Nehmen Sie Anpassungen vor, indem Sie:
   1. Öffnen Sie das {% prefspane Style %}
   2. Wählen Sie den neuen Stil in der Tabelle „Eigene Stile“ aus
   3. Klicken Sie auf „Im Finder anzeigen“, um die Datei im Finder zu zeigen
   4. Öffnen Sie die Datei in einem beliebigen Nur-Text-Editor (TextEdit funktioniert im Nur-Text-Modus) und nehmen Sie bei Bedarf Anpassungen vor

## Fehlerbehebung [troubleshooting]

### Website wird nicht geladen [website-wont-load]

- Überprüfen Sie, ob die URL korrekt und öffentlich zugänglich ist
- Einige Websites blockieren möglicherweise den automatisierten Zugriff
- Probieren Sie eine andere Seite auf derselben Website aus

### Stile sehen anders aus [styles-look-different]

- Die extrahierten Stile basieren auf dem spezifischen Inhalt, den Sie ausgewählt haben
- Einige Websites verwenden komplexes CSS, das möglicherweise nicht perfekt übersetzt werden kann
- Verwenden Sie zusätzliches CSS oder bearbeiten Sie das Stylesheet, um Feinanpassungen vorzunehmen

### Fehlende Stile [missing-styles]

- Stellen Sie sicher, dass Sie den Hauptinhaltsbereich ausgewählt haben, nicht eine Seitenleiste oder Kopfzeile
- Einige Stile können über JavaScript angewendet werden und werden nicht erfasst
- Überprüfen Sie die Debug-Konsole auf detaillierte Extraktionsinformationen

## Tastaturkürzel [keyboard-shortcuts]

- {% kbd return  %} – URL zur Extraktion laden
- {% kbd cmd S %} – Extrahierten Stil als Eigenen Stil (CSS-Datei) speichern
- {% kbd cmd  %}-Click – Navigieren Sie während der Vorschau durch Links

## Integration mit Eigenen Stilen [integration-with-custom-styles]

Extrahierte Stile werden in Ihrem Ordner für eigenes CSS gespeichert und lassen sich:

- über das Stil-Menü auf jedes Dokument **anwenden**
- mit einem beliebigen Texteditor **ändern**
- durch Kopieren der CSS-Datei mit anderen **teilen**
- mit anderen eigenen Stilen **kombinieren**

Mit dem Style Stealer können Sie ganz einfach eine Bibliothek mit wunderschönen Stilen erstellen, die von den am besten gestalteten Websites im Internet inspiriert sind.
