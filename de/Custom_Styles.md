# <%= @title %>

Sehen Sie sich Ihre Dokumente auf *Ihre* Weise an.

## Eigene Stile verwenden [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

Der einfachste Weg, Eigene Stile zu entdecken, ist die
[Eigene Stil-Galerie][2]. Dort können Sie die verfügbaren
Stile in Aktion durchstöbern, sie mit einem Klick installieren
und sogar [eigene Kreationen einreichen][6] zur Aufnahme in die
Galerie.

Um eigene Stylesheets von Ihrer lokalen Festplatte zu Marked
hinzuzufügen, verwenden Sie {% prefspane Style %}. Neue Stile werden den
Einblendmenüs in den Fenstereinstellungen und in jedem Fenster
hinzugefügt und nach dem Basisdateinamen der hinzugefügten
CSS-Datei benannt. Bewahren Sie Ihre eigenen CSS-Dateien an
einem sicheren Ort auf Ihrer Festplatte auf. Wenn sie auf Ihrer
Festplatte verschoben werden, werden sie aus Marked entfernt,
bis Sie sie erneut vom neuen Speicherort hinzufügen. Es
empfiehlt sich, offene Dokumente zu schließen und den Stil aus
den Einstellungen zu entfernen, bevor Sie eine von Marked
verwendete CSS-Datei löschen oder umbenennen. Wenn Sie das
nicht tun, geht dabei nichts kaputt, es erspart Ihnen aber
Verwirrung.

Fügen Sie Eigene Stile über den Stil-Manager mit der
Schaltfläche „Hinzufügen“ hinzu, oder indem Sie eine oder
mehrere CSS-Dateien auf die Einstellungen ziehen.

## Stile mit dem Stil-Manager verwalten [managing-styles-with-the-style-manager]

Der Stil-Manager gibt Ihnen einen zentralen Ort, um alle
integrierten und eigenen Stile zu verwalten. Klicken Sie auf
die Schaltfläche **Stile verwalten…** unter {% prefspane Style %},
oder ziehen Sie CSS-Dateien einfach auf das Einstellungsfenster
--- Marked importiert sie, öffnet den Stil-Manager und wählt
die neu hinzugefügte Zeile für Sie aus. Auch das direkte
Ziehen von CSS-Dateien auf das Fenster des Stil-Managers
funktioniert; werden mehrere Dateien gleichzeitig gezogen,
aktualisiert sich die Einblendung zu „N eigene Stile
hinzufügen“, damit klar ist, dass Sie einen ganzen Stapel
importieren.

![][img-style-manager]

Im Stil-Manager finden Sie eine sortierbare Tabelle, die
integrierte und eigene Stile zusammenfasst. Jede Zeile bietet:

- Ein Kontrollkästchen **Aktiviert**, das den Stil sofort zum
  Menü „Stil“, zum Einblendmenü für den Standardstil und zu
  den Tastaturkurzbefehlen hinzufügt bzw. daraus entfernt. Wird
  der aktuell aktive Stil deaktiviert, wechselt Marked
  automatisch zum nächsten verfügbaren Eintrag.
- Eine Spalte **Name**, die Sie direkt bearbeiten können;
  Änderungen werden gespeichert und in allen Menüs übernommen.
  Klicken Sie auf den Namen des Stils, um ihn direkt zu
  bearbeiten.
- Eine Spalte **Quelle**, die zwischen „Integriert“, „Eigen“
  und „Dupliziert“ unterscheidet.
- Ein Bereich **Aktionen** mit Schaltflächen zum **Bearbeiten**
  (öffnet die CSS-Datei in Ihrem Editor), **Duplizieren**
  (erstellt eine Kopie sowie eine neue CSS-Datei auf der
  Festplatte), **Anzeigen** (zeigt die Datei im Finder) und
  **Löschen** (mit der Option, nur den Verweis zu entfernen
  oder die CSS-Datei in den Papierkorb zu legen).

Zeilen lassen sich per Drag & Drop neu anordnen, und diese
Reihenfolge bestimmt sowohl das Menü „Stil“ als auch die
Zuordnung der `⌘/#`-Kurzbefehle – Sie können Stile also
buchstäblich in die gewünschten Plätze ziehen. Sie können auch
externe CSS-Dateien an bestimmten Positionen ablegen; der
Einfügeindikator zeigt an, wo der neue Stil eingefügt wird.

### Live-Vorschau [live-preview]

Der rechte Bereich zeigt eine Vorschau, die den ausgewählten
Stil in einem vollständigen HTML-Dokument mit einer
umfassenden Auswahl an Überschriften, Listen, Tabellen,
Codeblöcken usw. darstellt. Die Vorschau verwendet das
tatsächliche CSS auf der Festplatte, sodass Änderungen, die
Sie in Ihrem externen Editor vornehmen, sofort übernommen
werden. Ein Kontrollkästchen schaltet die Dunkelmodus-Vorschau
um.

Weitere Stile zur Verwendung (oder als Beispiele für eigene
Kreationen) finden Sie [auf GitHub][1] (siehe die
[Beispiele][2] für einen schnellen Überblick über das
Angebot). Einzelheiten und Tipps finden Sie unter [Eigenes CSS
erstellen][3].

## Zusätzliches CSS [additional-css]

Unter {% prefspane Style %} finden Sie eine Option namens „Zusätzliches
CSS“ mit einer Schaltfläche „CSS bearbeiten“. Ein Klick auf
diese Schaltfläche öffnet ein Fenster, in dem Sie universelle
CSS-Regeln hinzufügen können, die auf alle Stile angewendet
werden. Beachten Sie, dass die Spezifität der Regeln wichtig
sein kann, wenn Sie einen Teil der Standardformatierung von
Marked überschreiben. Der Hauptteil des Dokuments ist in ein
Div mit der ID „#wrapper“ eingebettet. Ein vorangestellter
Selektor mit dieser ID ermöglicht einfachere Überschreibungen,
z. B.:

    #wrapper img { width: 100%; height: auto; }

CSS in diesem Feld wird **an den aktiven Stil angehängt**. Es
ist kein Ersatz für einen vollständigen Eigenen Stil: Ein
Stylesheet, das nur für dieses Feld geschrieben wurde, ist
bewusst unvollständig – würde man es über den Stil-Manager als
Stil laden, bliebe alles ungestylt, was es nicht abdeckt.

Marked **schreibt** Selektoren im Zusätzlichen CSS vor dem
Einfügen **um**. Führende body-Klassen wie `.mkprinting` werden mit
`body` zusammengeführt, statt unter `#wrapper` verschachtelt zu
werden; Druckregeln in diesem Feld sollten daher `body.mkprinting #wrapper …`
verwenden (die vollständigen Umschreibungsregeln finden Sie
unter [Eigenes CSS erstellen](Writing_Custom_CSS.html#additional-css-settings)).
Für das Feld gibt es weder eine Größenbegrenzung noch eine
Gültigkeitsprüfung – ungültiges CSS hat einfach keine Wirkung.

CSS in diesem Feld wird auf jedes Dokument angewendet,
unabhängig davon, welchen Stil es verwendet --- auch beim
HTML-Export, wenn Stile einbezogen werden. Wenn Sie eigenes
CSS anhand bedingter Kriterien anwenden möchten, verwenden Sie
die Aktionen „Stil festlegen“, „CSS-Datei einfügen“ oder „CSS
einfügen“ in {% prefspane Processor %}
Eigene Regeln.

## Druck- und PDF-Export [print-and-pdf-export]

Marked fügt bei jeder Vorschau einen integrierten `@media print`-Block
(`mkprintstyles`) ein. Er setzt Standardwerte wie eine Basisgröße von
**10pt** für `html`, `body` und `#wrapper` (oder die Größe aus
**Benutzerdefinierte Schriftgröße für Export/Druck** unter
{% prefspane Export %}, wenn diese Option aktiviert ist) und normalisiert
Absatztext mit `p { font-size: 1em; }` und `li p { font-size: 1em; }`, sodass reine
Bildschirmregeln wie `p { font-size: 1.1429em; }` den Fließtext in PDFs und
Ausdrucken nicht vergrößern.

Der PDF-Export kann im verborgenen WebView, das für die
Erzeugung verwendet wird, entweder **print**- oder
**screen**-Medien verwenden. Integrierte Stile nutzen in der
Regel Druckmedien; **eigene Stile** und
[Fountain](Fountain_for_Screenwriters.html)-Dokumente
verwenden oft Bildschirmmedien, damit das Layout der Vorschau
entspricht. Das bedeutet, dass `@media print { ... }`-Regeln beim PDF-Export
nicht immer angewendet werden.

Für zuverlässige Formatierung bei PDF- und
Druck-/PDF-Vorschau stellen Sie Selektoren die Klasse `mkprinting`
voran, die Marked beim Export zu `<body>` hinzufügt
(Einzelheiten und Beispiele finden Sie unter [Eigenes CSS
schreiben](Writing_Custom_CSS.html#printstyles)). In einer
**Eigenen Stil**-Datei können Sie `.mkprinting` allein verwenden.
Im **Zusätzlichen CSS** verwenden Sie die body-qualifizierte
Form `body.mkprinting #wrapper …`, da dieses Feld Selektoren umschreibt. Sie
können beide Formen auch mit `@media print` kombinieren, wenn Sie
beide Pfade abdecken möchten.

Um Größen festzulegen, die von den Druckstandards von Marked
abweichen, fügen Sie explizite Regeln in Ihrem eigenen CSS
(oder im Zusätzlichen CSS) hinzu. Verwenden Sie `!important`, wenn
Sie die von Marked eingefügten Druckstile überschreiben müssen
--- zum Beispiel:

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

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

Regeln ohne `!important` können gegenüber späteren Regeln in
`mkprintstyles` oder anderen nicht qualifizierten Selektoren in Ihrem
Stylesheet, die im Druck ebenfalls gelten, den Kürzeren
ziehen. Wenn Sie druckspezifische Anpassungen in `@media print`
und/oder `.mkprinting` / `body.mkprinting`-Regeln unterbringen (statt nur in
Bildschirmregeln), lassen sich Vorschau- und Exportverhalten
leichter nachvollziehen.

## CSS-Änderungen überwachen [watching-css-changes]

Im Abschnitt Eigene Stile unter {% prefspane Style %} können Sie ein
Kontrollkästchen aktivieren, damit Marked zusätzlich zur
Markdown-Datei, die Sie bearbeiten, auch die aktive CSS-Datei
überwacht. Werden an einer der beiden Dateien Änderungen
erkannt, aktualisiert sich die Vorschau. Das ist praktisch, um
eigene Stile zu bearbeiten, ohne ständig neu laden zu müssen,
und eignet sich auch für einfache Webentwicklungsaufgaben.

Das eignet sich auch für einfache Webdesign-Arbeiten und
CSS-Experimente (etwa beim Erstellen eigener Stile). Laden Sie
eine Markdown-Datei mit dem gesamten Markup, das Sie gestalten
möchten, erstellen Sie einen eigenen Stil, und beobachten Sie
die Vorschau, während Sie ihn bearbeiten – Änderungen
erscheinen live.

## Eigenes CSS schreiben [writing-custom-css]

Wenn Sie mit CSS vertraut sind, können Sie eigene Stylesheets
für die Verwendung in Marked erstellen. Einzelheiten finden
Sie unter [Eigenes CSS schreiben][3]. Wenn Sie etwas Neues
erstellen, denken Sie darüber nach, es [einzureichen][6] und
in der [Galerie][2] mit anderen Nutzern zu teilen. Achten Sie
darauf, die im Leitfaden aufgeführten Grundlagen zu
berücksichtigen, und fügen Sie den Metadaten-Kommentar am
Anfang ein.

### Automatische Eigene Stile mit StyleStealer [automatic-custom-styles-with-stylestealer]

Mit dem [Style Stealer][4] können Sie sogar automatisch einen
Stil auf Grundlage einer bestehenden Website erzeugen. Damit
laden Sie eine Webseite und übernehmen die berechneten Stile
für alle wichtigen in Markdown vorkommenden Elemente, um sie
anschließend als eigenen Stil zu speichern.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Eigene Stile verwalten (umbenennen, neu anordnen, duplizieren
und löschen) können Sie über den [Stil-Manager](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
