# <%= @title %>

Sehen Sie Ihre Dokumente auf *Ihre* Art.

## Eigene Stile verwenden [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Am einfachsten erkunden Sie Eigene Stile über die [Galerie für Eigene Stile][2]. Dort sehen Sie die verfügbaren Stile in Aktion, installieren sie per Klick und können sogar [eigene Kreationen einreichen][6].

Um eigene Stylesheets von Ihrem lokalen Laufwerk zu Marked hinzuzufügen, nutzen Sie {% prefspane Style %}. Neue Stile erscheinen in den Dropdown-Menüs der Fenstereinstellungen und an jedem Fenster und werden nach dem Basisdateinamen der hinzugefügten CSS-Datei benannt. Bewahren Sie Ihre eigenen CSS-Dateien an einem sicheren Ort auf Ihrem Laufwerk auf. Verschieben Sie sie, werden sie aus Marked entfernt, bis Sie sie vom neuen Ort erneut hinzufügen. Schließen Sie geöffnete Dokumente und entfernen Sie den Stil in den Einstellungen, bevor Sie eine von Marked genutzte CSS-Datei löschen oder umbenennen. Es geht nichts kaputt, wenn Sie das nicht tun, aber es vermeidet Verwirrung.

Fügen Sie Eigene Stile über den Stil-Manager mit der Hinzufügen-Schaltfläche hinzu oder indem Sie eine oder mehrere CSS-Dateien auf den Einstellungsbereich ziehen.

## Stile mit dem Stil-Manager verwalten [managing-styles-with-the-style-manager]

Der Stil-Manager gibt Ihnen einen zentralen Ort, um jeden integrierten und eigenen Stil zu pflegen. Klicken Sie unter {% prefspane Style %} auf die Schaltfläche **Stile verwalten…**, oder ziehen Sie einfach CSS-Dateien auf das Einstellungsfenster – Marked importiert sie, öffnet den Stil-Manager und wählt die neu hinzugefügte Zeile für Sie aus. Auch das Ziehen von CSS-Dateien direkt auf das Stil-Manager-Fenster funktioniert; ziehen Sie mehrere Dateien, aktualisiert sich das Overlay zu „N Eigene Stile hinzufügen“, sodass klar ist, dass Sie einen Stapel importieren.

![][img-style-manager]

Im Stil-Manager finden Sie eine sortierbare Tabelle, die integrierte und eigene Stile mischt. Jede Zeile bietet:

- Ein Kontrollkästchen **Aktiviert**, das den Stil sofort zum Stil-Menü, zum Standardstil-Popup und zu den Tastaturkurzbefehlen hinzufügt bzw. daraus entfernt. Deaktivieren Sie den gerade aktiven Stil, wird automatisch zum nächsten verfügbaren Eintrag gewechselt.
- Eine Spalte **Name**, die Sie inline bearbeiten können; Änderungen bleiben erhalten und wirken sich auf jedes Menü aus. Klicken Sie auf den Namen des Stils, um ihn direkt zu bearbeiten.
- Eine Spalte **Quelle**, die „Integriert“, „Eigen“ oder „Dupliziert“ ausweist.
- Einen **Aktionen**-Block mit Schaltflächen für **Bearbeiten** (öffnet die CSS-Datei in Ihrem Editor), **Duplizieren** (erstellt eine Kopie und eine neue CSS-Datei auf der Festplatte), **Im Finder anzeigen** (zeigt die Datei im Finder) und **Löschen** (mit Optionen, die Referenz zu entfernen oder die CSS-Datei in den Papierkorb zu legen).

Zeilen ordnen Sie per Drag-and-drop um, und die Reihenfolge steuert sowohl das Stil-Menü als auch die `⌘/#`-Kurzbefehl-Zuweisungen – Sie ziehen Stile also buchstäblich in die gewünschten Plätze. Sie können auch externe CSS-Dateien an bestimmte Positionen ziehen; die Ablage-Markierung bestimmt, wo der neue Stil eingefügt wird.

### Live-Vorschau [live-preview]

Der rechte Bereich zeigt eine Vorschau, die den ausgewählten Stil in einem vollständigen HTML-Dokument mit einem umfassenden Satz an Überschriften, Listen, Tabellen, Codeblöcken usw. rendert. Die Vorschau verwendet das tatsächliche CSS auf der Festplatte, sodass Änderungen in Ihrem externen Editor sofort erscheinen. Ein Kontrollkästchen schaltet die Dunkelmodus-Vorschau um.

Weitere Stile zur Verwendung (oder als Beispiele für eigene) finden Sie [auf GitHub][1] (die [Beispiele][2] geben einen schnellen Überblick). Einzelheiten und Tipps unter [Eigenes CSS schreiben][3].

## Zusätzliches CSS [additional-css]

Unter {% prefspane Style %} finden Sie die Option „Zusätzliches CSS“ mit einer Schaltfläche „CSS bearbeiten“. Ein Klick darauf öffnet ein Fenster, in dem Sie universelle CSS-Regeln hinzufügen, die auf alle Stile angewendet werden. Beachten Sie, dass die Spezifität der Regeln wichtig sein kann, wenn Sie einen Teil von Markeds Standardformatierung überschreiben. Der Hauptteil des Dokuments ist in ein `div` mit der ID „#wrapper“ eingeschlossen. Stellen Sie diese einem Selektor voran, gelingen Überschreibungen leichter, z. B.:

    #wrapper img { width: 100%; height: auto; }

CSS in diesem Feld wird auf jedes Dokument angewendet, egal welchen Stil es verwendet. Wollen Sie eigenes CSS anhand von Bedingungen anwenden, verwenden Sie die Aktionen „Stil festlegen“, „CSS-Datei einfügen“ oder „CSS einfügen“ in den Eigenen Regeln unter {% prefspane Processor %}.

## Drucken und PDF-Export [print-and-pdf-export]

Marked fügt bei jeder Vorschau einen integrierten `@media print`-Block (`mkprintstyles`) ein. Er setzt Standardwerte wie eine **10-pt**-Basis auf `html`, `body` und `#wrapper` (oder die Größe aus **Benutzerdefinierte Schriftgröße für Export/Druck** unter {% prefspane Export %}, wenn diese Option aktiviert ist) und normalisiert Absatztext mit `p { font-size: 1em; }` und `li p { font-size: 1em; }`, damit reine Bildschirm-Regeln wie `p { font-size: 1.1429em; }` den Fließtext in PDFs und im Druck nicht aufblähen.

Der PDF-Export kann auf dem versteckten WebView, das zur Erzeugung dient, **print**- oder **screen**-Medien verwenden. Integrierte Designs nutzen typischerweise print-Medien; **eigene Stile** und [Fountain](Fountain_for_Screenwriters.html)-Dokumente verwenden oft screen-Medien, damit das Layout der Vorschau entspricht. Das heißt, `@media print { ... }`-Regeln werden beim PDF-Export nicht immer angewendet.

Für zuverlässiges Styling bei PDF und Druck-/PDF-Vorschau stellen Sie den Selektoren die Klasse `mkprinting` voran, die Marked beim Export dem `<body>` hinzufügt (Einzelheiten und Beispiele unter [Eigenes CSS schreiben](Writing_Custom_CSS.html#printstyles)). Sie können `.mkprinting` allein verwenden oder es mit `@media print` kombinieren, wenn Sie beide Wege abdecken müssen.

Um Größen festzulegen, die von Markeds Druckstandards abweichen, fügen Sie explizite Regeln in Ihr eigenes CSS (oder in „Zusätzliches CSS“) ein. Verwenden Sie `!important`, wenn Sie Markeds eingefügte Druckstile überschreiben müssen – zum Beispiel:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}
```

Regeln ohne `!important` können gegen spätere Regeln in `mkprintstyles` oder gegen andere unqualifizierte Selektoren in Ihrem Stylesheet verlieren, die im Druck ebenfalls gelten. Druck-spezifische Anpassungen in `@media print`- und/oder `.mkprinting`-Regeln (statt nur in Bildschirm-Regeln) unterzubringen, macht das Vorschau- und Exportverhalten leichter nachvollziehbar.

## CSS-Änderungen überwachen [watching-css-changes]

Im Abschnitt „Eigene Stile“ unter {% prefspane Style %} können Sie ein Kontrollkästchen aktivieren, damit Marked zusätzlich zur bearbeiteten Markdown-Datei die aktive CSS-Datei überwacht. Werden an einer der beiden Dateien Änderungen erkannt, aktualisiert sich die Vorschau. Das ist praktisch, um eigene Stile zu bearbeiten, ohne ständig zu aktualisieren, und lässt sich auch für einfache Webentwicklung nutzen.

Ebenso hilfreich ist es für grundlegende Webdesign-Arbeit und CSS-Experimente (etwa das Erstellen eigener Stile). Laden Sie eine Markdown-Datei mit allem Markup, das Sie gestalten wollen, erstellen Sie einen eigenen Stil und beobachten Sie die Vorschau, die sich beim Bearbeiten live ändert.

## Eigenes CSS schreiben [writing-custom-css]

Wenn Sie sich mit CSS auskennen, können Sie eigene Stylesheets für Marked erstellen. Einzelheiten unter [Eigenes CSS schreiben][3]. Wann immer Sie etwas Neues erstellen, denken Sie daran, es zur [Galerie][2] [einzureichen][6], um es mit anderen zu teilen. Decken Sie die im Leitfaden aufgeführten Grundlagen ab und fügen Sie oben den Metadaten-Kommentar ein.

### Automatische Eigene Stile mit dem Style Stealer [automatic-custom-styles-with-stylestealer]

Sie können sogar automatisch einen Stil anhand einer bestehenden Website erzeugen – mit dem [Style Stealer][4]. Damit laden Sie eine Webseite, greifen die berechneten Stile aller wichtigen in Markdown vorkommenden Elemente ab und speichern sie als eigenen Stil.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Verwalten Sie Eigene Stile (umbenennen, umsortieren, duplizieren und löschen) über den [Stil-Manager](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
