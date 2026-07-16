# <%= @title %>

Der Custom Style Generator ist ein webbasiertes Tool, mit dem Sie eigene Stile für Marked erstellen können, ohne CSS von Hand zu schreiben. Er bietet eine visuelle Benutzeroberfläche mit Steuerelementen für Typografie, Farben, Abstände und mehr sowie eine Live-Vorschau, die aktualisiert wird, wenn Sie Änderungen vornehmen.

## Zugriff auf den Generator [accessing-the-generator]

Der Style Generator ist unter [https://markedapp.com/style-generator/](https://markedapp.com/style-generator/) verfügbar. Sie können ihn direkt im Webbrowser verwenden – keine Installation nötig.

![Style Generator][img-style-generator]

  [img-style-generator]: images/style-generator-800.jpg @2x width=800 class=center

## Erste Schritte [getting-started]

Wenn Sie den Generator zum ersten Mal öffnen, sehen Sie Folgendes:

- **Vorschaubereich** (links): Eine Live-Vorschau Ihres Stils, der auf Beispiel-Markdown-Inhalte angewendet wird
- **Steuerelementbereich** (rechts): Alle Stilsteuerelemente in Abschnitten organisiert
- **Symbolleiste** (oben): Stiltitel, Basisthemenauswahl und CSS-Importoption

### Auswählen eines Basisthemas [choosing-a-base-theme]

Wählen Sie zunächst ein **Basisthema** aus der Dropdown-Liste aus. Dies bildet die Grundlage für Ihren Stil – Sie können ihn dann in jedem Aspekt individuell anpassen. Zu den beliebten Optionen gehören „Blank“ (Neuanfang), „Default“ und verschiedene integrierte Designs.

### Vorhandenes CSS importieren [importing-existing-css]

Wenn Sie eine bestehende CSS-Datei haben, die Sie als Ausgangspunkt verwenden möchten, klicken Sie auf **CSS importieren** und wählen Sie Ihre Datei aus. Der Generator lädt diese Stile und Sie können sie dann mithilfe der Steuerelemente ändern.

## Stil-Steuerelemente [style-controls]

Der Generator organisiert Steuerelemente in logische Abschnitte:

### Basistypografie [base-typography]

Steuern Sie die grundlegenden Typografieeinstellungen:

- **Rhythmus verwenden**: Wenn diese Option aktiviert ist, wird eine mathematische typografische Skala für einheitliche Überschriftengrößen und -abstände verwendet
- **Grundschriftgröße**: Die Grundschriftgröße (normalerweise `16px`)
- **Zeilenhöhe**: Der Abstand zwischen Textzeilen
- **Skalierungsverhältnis**: Das für die typografische Skalierung verwendete Verhältnis (beeinflusst die Überschriftengrößen)

### Layout [layout]

Abstand und Einzug anpassen:

- **Wrapper-Innenabstand**: Platz um den Inhaltsbereich
- **Absatzeinzug**: Einzug der ersten Zeile für Absätze
- **Listeneinzug**: Einrückung für Listen
- **Blockzitat-Einzug**: Linker Rand für Blockzitate

### Schriftarten [fonts]

Konfigurieren Sie Schriftfamilien und -stärken:

- **Kopfzeilen-Schriftarten**: Durch Kommas getrennte Liste von Schriftarten für Überschriften (z. B. „Georgia, serif“)
- **Textschriftarten**: Durch Kommas getrennte Liste von Schriftarten für den Textkörper
- **Kopfzeilenstärke**: Schriftstärke für Überschriften (100–900)
- **Textkörperstärke**: Schriftstärke für den Fließtext
- **Fettstärke**: Schriftstärke für fetten Text
- **Buchstabenabstand**: Zeichenabstand für Kopfzeilen und Textkörper

### Google-Schriftarten [google-fonts]

Fügen Sie Google Fonts zu Ihrem Stil hinzu:

1. Geben Sie einen Schriftartnamen in das Suchfeld ein (es werden Vorschläge zur automatischen Vervollständigung angezeigt).
2. Geben Sie optional Stile an (z. B. „400,400i,700“ für normal, kursiv, fett)
3. Klicken Sie auf **Hinzufügen**, um es einzuschließen
4. Verwenden Sie **Google Fonts durchsuchen**, um den vollständigen Katalog mit Vorschauen zu erkunden

Hinzugefügte Schriftarten werden in einer Liste unter den Steuerelementen angezeigt. Klicken Sie auf das ×, um sie zu entfernen.

### Farben [colors]

Farben für verschiedene Elemente festlegen:

- **Hintergrund**: Hintergrundfarbe der Seite
- **Basistext**: Standardtextfarbe
- **Kopfzeilenfarbe**: Farbe für alle Überschriften (kann pro Überschriftenebene überschrieben werden)
- **Textkörperfarbe**: Farbe des Textkörpers
- **Linkfarbe**: Farbe für Links
- **Hervorhebungsfarbe**: Farbe für hervorgehobenen Text (`<em>`)
- **Strong-Farbe**: Farbe für stark hervorgehobenen Text (`<strong>`)
- **Mark-Hintergrund**: Hintergrundfarbe für hervorgehobenen Text (`<mark>`)

Einzelne Überschriftenfarben (H1–H6) können separat eingestellt werden – verwenden Sie **Zurücksetzen**, um eine Überschreibung zu löschen und zur Kopfzeilenfarbe zurückzukehren.

### Dunkler Modus [dark-mode]

Schalten Sie **Dunkelmodus** um, um eine Vorschau der Farben im Dunkelmodus anzuzeigen und diese zu konfigurieren. Wenn diese Option aktiviert ist, werden separate Farbsteuerelemente für Dunkelmodusvarianten angezeigt. Dunkelmodus-Stile gelten, wenn `.inverted` am `body`-Element in Marked gesetzt ist.

Verwenden Sie **Farben generieren**, um automatisch eine Dunkelmodus-Palette basierend auf Ihren Hellmodus-Farben zu erstellen.

### Bilder [images]

Bilddarstellung steuern:

- **Max. Breite**: Maximale Breite für Bilder (z. B. `100%`, `800px`)
- **Randradius**: Abgerundete Ecken (z. B. „8px“, „0“)
- **Ausrichtung**: Dokumentstandard, links, zentriert oder rechts

### Blockzitate [blockquotes]

Blockzitate im Stil:

- **Breite des linken Randes**: Dicke des linken Randes
- **Farbe des linken Randes**: Farbe des linken Randes
- **Hintergrundfarbe**: Hintergrundfarbe für Blockzitate
- **Schriftstil**: Normal oder Kursiv
- **Linker Rand**: Abstand vom linken Rand
- **Verschachtelter linker Rand**: Abstand für verschachtelte Blockzitate (kann `inherit` sein)

Für Blockzitate im Dunkelmodus stehen separate Steuerelemente zur Verfügung.

### Listen [lists]

Konfigurieren Sie das Erscheinungsbild der Liste:

- **Position des Listenstils**: Innen oder außen (wo Aufzählungszeichen/Zahlen erscheinen)
- **Linker Rand**: Abstand vom linken Rand
- **Verschachtelter linker Rand**: Abstand für verschachtelte Listen (kann `inherit` sein)

### Definitionslisten [definition-lists]

Stildefinitionslisten (`<dl>`, `<dt>`, `<dd>`):

- **DL-Einzug**: Gesamteinzug
- **DT** (Begriff)-Einstellungen: Schriftgröße, -stärke und -stil
- **DD** (Definition)-Einstellungen: Schriftgröße, -stärke, -stil und -einzug

### Tabellen [tables]

Umfassendes Tabellen-Styling:

- **Hintergrundfarbe**: Tabellenhintergrund
- **Randfarbe**: Randfarbe für Zellen
- **Tabellentextfarbe**: Standardtextfarbe in Tabellen
- **Abwechselnde Zeilen/Spalten**: Zebrastreifen mit benutzerdefinierten Farben aktivieren
- **Rand**: Tabellenumriss ein-/ausblenden
- **Gitter**: Interne Gitterlinien ein-/ausblenden
- **Ausrichtung**: Links oder Mitte
- **Randradius**: Abgerundete Ecken
- **Max. Breite**: Maximale Tabellenbreite
- **Zell-Innenabstand**: Innenabstand
- **Kopfzeile**-Einstellungen: Schriftstärke, -größe und -stil
- Einstellungen für **Beschriftung**: Schriftstärke, -größe, -stil und Textfarbe

Für Dunkelmodustabellen stehen separate Steuerelemente zur Verfügung.

### Codeblöcke [code-blocks]

Stilcodeblöcke und Inline-Code:

- **Code-Schriftfamilie**: Monospace-Schriftstapel
- **Hintergrund**: Hintergrundfarbe
- **Randfarbe**: Randfarbe
- **Randradius**: Abgerundete Ecken
- **Wrap-Modus**: Kein Umbruch (`pre`), Erhalten + Umbruch (`pre-wrap`) oder Normal (`wrap`)
- **Code-Padding**: Innenabstand

Für Codeblöcke im Dunkelmodus stehen separate Steuerelemente zur Verfügung.

### Fußnoten [footnotes]

Stil-Fußnoten:

- **Markierungsfarbe**: Farbe der Fußnotenmarkierungen
- **Textfarbe**: Farbe des Fußnotentextes
- **Textschriftstil**: Normal oder Kursiv

Für Fußnoten im Dunkelmodus stehen separate Steuerelemente zur Verfügung.

### Schlagschatten [drop-shadow]

Schlagschatten zu Elementen hinzufügen:

1. Wählen Sie Schatten **Stärke**: Weich, Mittel oder Stark
2. Wählen Sie aus, auf welche Elemente Schatten angewendet werden sollen:
   - Bilder
   - Codeblöcke
   - Blockzitate
   - Tabellen

## Custom CSS [custom-css]

Für erweiterte Anpassungen, die über die verfügbaren Steuerelemente hinausgehen, verwenden Sie die Schaltfläche **Custom CSS**, um einen Code-Editor zu öffnen. Jegliches CSS, das Sie hier hinzufügen, wird an den generierten Stil angehängt und automatisch so angepasst, dass es innerhalb der Dokumentstruktur von Marked funktioniert.

Der Editor umfasst Syntaxhervorhebung und -validierung – ungültiges CSS wird mit Fehlermeldungen gekennzeichnet.

## Live-Vorschau [live-preview]

Im Vorschaubereich wird Ihr Stil angezeigt, der auf Beispiel-Markdown-Inhalte angewendet wird, einschließlich:

- Überschriften (H1–H6)
- Absätze mit verschiedenen Inline-Formatierungen
- Tabellen
- Codeblöcke
- Bilder
- Listen (geordnet und ungeordnet)
- Blockzitate
- Definitionslisten
- Fußnoten
- Aufgabenlisten

Änderungen werden in Echtzeit aktualisiert, wenn Sie die Steuerelemente anpassen.

## Speichern und Teilen [saving-and-sharing]

Sobald Sie mit Ihrem Stil zufrieden sind, haben Sie mehrere Möglichkeiten:

### CSS anzeigen [view-css]

Klicken Sie auf **CSS anzeigen**, um das vollständig generierte CSS in einem Popover anzuzeigen. Sie können es in Ihre Zwischenablage kopieren oder vor dem Speichern überprüfen.

### CSS speichern [save-css]

Klicken Sie auf **CSS speichern**, um Ihren Stil als CSS-Datei herunterzuladen. Vor dem Herunterladen werden Sie aufgefordert, Metadaten (Titel, Autor, Beschreibung) einzugeben.

### Zu Marked hinzufügen [add-to-marked]

Klicken Sie auf **Zu Marked hinzufügen**, um den Stil direkt zu Ihrer Marked-Installation hinzuzufügen. Dazu muss Marked ausgeführt werden und ein Dialogfeld zur Bestätigung des Stilnamens und der Autoreninformationen wird geöffnet.

### Stil teilen [share-style]

Klicken Sie auf **Stil teilen**, um Ihren Stil im [Marked Style Gallery](https://markedapp.com/styles) zu veröffentlichen, damit andere ihn verwenden können. Sie müssen Folgendes bereitstellen:

- Stiltitel
- Ihr Name
- Autoren-URL (optional)
- Beschreibung
- Hinweis (optional)

Vor der Veröffentlichung wird im Freigabedialog eine Vorschau Ihres Stils angezeigt.

## Metadaten [metadata]

Verwenden Sie den Metadatenbereich (erweiterbar über die Pfeilschaltfläche neben dem Stiltitel), um Folgendes festzulegen:

- **Autor**: Ihr Name (bleibt sitzungsübergreifend bestehen)
- **Autoren-URL**: Ihre Website- oder Profil-URL
- **Beschreibung**: Eine Beschreibung des Stils
- **Hinweis**: Zusätzliche Hinweise (nicht in freigegebenen Stilen enthalten)

Diese Metadaten sind im Header der CSS-Datei enthalten und werden beim Teilen von Stilen verwendet.

## Tipps [tips]

- Beginnen Sie mit einem Basisthema, das Ihren Wünschen entspricht, und passen Sie es dann an
- Verwenden Sie das Design **Blank**, wenn Sie die vollständige Kontrolle von Grund auf wünschen
- Aktivieren Sie **Rhythmus** für mathematisch konsistente Typografie
- Testen Sie Ihren Stil mit dem **Dunkelmodus**-Schalter, wenn Sie ihn unterstützen möchten
- Verwenden Sie **Custom CSS** sparsam – die meisten Anforderungen können mit den integrierten Steuerelementen erfüllt werden
- Zeigen Sie eine Vorschau Ihres Stils mit verschiedenen Inhaltstypen an, bevor Sie ihn teilen

## Browserkompatibilität [browser-compatibility]

Der Style Generator funktioniert am besten in modernen Browsern (Chrome, Firefox, Safari, Edge). Er benötigt aktiviertes JavaScript.
