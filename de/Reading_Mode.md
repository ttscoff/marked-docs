# <%= @title %>

Der Lesemodus merkt sich Ihre Position in langen Dokumenten, hebt den aktuellen Block hervor und lässt Sie dauerhafte Hervorhebungen speichern.

## Lesemodus starten [entering-reading-mode]

Wählen Sie {% appmenu Vorschau, Lesemodus %} oder drücken Sie {% kbd ctrl opt r %}. Läuft gerade Speed Read, beendet Marked es, bevor der Lesemodus startet.

Der aktuelle Absatz, die Überschrift, das Listenelement, Bild, der Codeblock, die Tabelle oder eine andere Leseeinheit erhält eine Markierung am linken Rand. Die Tastaturnavigation bewegt sich weich von Block zu Block und hält die aktuelle Einheit im oberen Drittel der Vorschau. Scrollen Sie von Hand, wandert der Fokus mit, ohne dass die Seite springt.

## Navigation und Fortsetzen [navigation-and-resume]

Solange der Lesemodus aktiv ist:

- {% kbd j %} oder {% kbd down %}: zur nächsten Leseeinheit.
- {% kbd k %} oder {% kbd up %}: zur vorherigen Leseeinheit.
- {% kbd h %}: hebt die Auswahl hervor oder schaltet die Hervorhebung der aktuellen Einheit um, wenn nichts ausgewählt ist.

Marked speichert die Leseposition für jedes Dokument. Weicht eine gespeicherte Position von der aktuellen Ansicht ab, bietet der Lesemodus beim Start zwei Möglichkeiten:

- **Fortsetzen** kehrt zur gespeicherten Leseposition zurück.
- **Hier starten** verwendet die Leseeinheit, die gerade in der Vorschau sichtbar ist.

## Fokusmodus [focus-mode]

Klicken Sie oben in der Vorschau auf das Werkzeug „Fokusmodus“, um alle Blöcke außer der aktuellen Leseeinheit abzudunkeln. Der Fokusmodus folgt der aktuellen Einheit, während Sie navigieren. Ein erneuter Klick stellt die übrigen Blöcke wieder her; beim Verlassen des Lesemodus endet der Fokusmodus automatisch.

## Hervorhebungen anlegen und bearbeiten [creating-and-editing-highlights]

Wählen Sie Text aus und drücken Sie {% kbd h %}, um eine Inline-Hervorhebung anzulegen. Ohne Auswahl hebt {% kbd h %} die gesamte aktuelle Leseeinheit hervor; ein erneuter Druck entfernt diese Hervorhebung wieder. Bei der ersten Hervorhebung fragt Marked nach einer Signatur, die es beim Erzeugen von CriticMarkup verwendet. Ändern lässt sie sich unter {% prefspane Preview %}.

### Auswahl-Popup

Wählen Sie Text aus, dann erscheint das Auswahl-Popup mit mittig angeordneten Symbolschaltflächen:

- **Hervorheben** legt eine Inline-Hervorhebung an (oder **X** entfernt die letzte automatische Hervorhebung, solange automatisches Hervorheben aktiv ist).
- **Kommentar hinzufügen** öffnet einen Dialog, um eine Notiz zur Hervorhebung anzulegen oder zu bearbeiten. Ist die Auswahl noch nicht hervorgehoben, hebt Marked sie zuerst hervor.

Ist **Popup-Statistiken zur Textauswahl** aktiviert, zeigt das Popup außerdem die Wortanzahl der Auswahl.

### Kommentare zu Hervorhebungen [highlight-comments]

Kommentare sind etwas anderes als Signaturen. Eine Signatur ordnet die Hervorhebung jemandem zu; ein Kommentar ist Ihre Notiz dazu.

Legen Sie einen Kommentar über das Kommentarsymbol im Auswahl-Popup an oder bearbeiten Sie ihn dort. Alternativ klicken Sie bei gedrückter Control-Taste auf eine Hervorhebung und wählen **Kommentar hinzufügen…** oder **Kommentar bearbeiten…**. Mit **Kommentar löschen** entfernen Sie die Notiz, ohne die Hervorhebung zu löschen.

Hervorhebungen mit Kommentar zeigen einen kleinen Punkt als Hinweis. Ist die Kommentar-Seitenleiste eingeblendet (**Vorschau > Kommentare anzeigen**), erscheinen die Kommentare des Lesemodus dort mit einer Verbindungslinie zur zugehörigen Hervorhebung, zusammen mit CriticMarkup- und anderen Dokumentkommentaren.

### Automatische Hervorhebungen

Klicken Sie oben in der Vorschau auf das Hervorhebungswerkzeug, um Text automatisch beim Auswählen hervorzuheben. Ein Klick auf das Hervorhebungssymbol im Auswahl-Popup macht die letzte automatische Hervorhebung rückgängig; ein erneuter Klick auf das Werkzeug oben schaltet das automatische Hervorheben wieder aus.

Inline-Hervorhebungen zeigen Anfasser an Anfang und Ende, sobald Sie darauf zeigen oder sie auswählen. Ziehen Sie an einem Anfasser, um den hervorgehobenen Bereich zu vergrößern oder zu verkleinern. Änderungen werden automatisch gesichert und beim Aktualisieren oder erneuten Öffnen des Dokuments wiederhergestellt.

Klicken Sie auf eine Hervorhebung, um sie zu fokussieren, und drücken Sie dann Entfernen oder Rückschritt, um sie zu löschen. Klicken Sie bei gedrückter Control-Taste auf eine Hervorhebung und wählen Sie **Teilen…**, um das Teilen-Fenster von macOS mit Dokumenttitel und hervorgehobenem Text zu öffnen, **Kommentar hinzufügen…** oder **Kommentar bearbeiten…**, um eine Notiz anzuhängen, oder **Kommentar löschen**, um sie zu entfernen.

Die Einstellung **Hervorhebungen anzeigen, wenn der Lesemodus aus ist** legt fest, ob gespeicherte Hervorhebungen sichtbar bleiben, nachdem Sie den Modus verlassen haben.

## Hervorhebungen exportieren [exporting-highlights]

Wählen Sie **Vorschau > Hervorhebungen exportieren…** oder klicken Sie in der Lesemodus-Symbolleiste auf das Export-Werkzeug. Formate: Markdown, HTML (im aktuellen Vorschaustil), Klartext, CSV (Readwise-kompatibel, mit Kommentaren in der Spalte **Note** und Signaturen in **Signature**) und JSON (mit einem Feld `comment` je Hervorhebung).

Beim HTML-Export stehen die Kommentare als Blockzitate unter der jeweils hervorgehobenen Passage.

Das JSON-Format ist Markeds Austauschformat. Legen Sie die Datei als `Document.markedhighlights.json` neben ein Markdown-Dokument oder lassen Sie sie beim Export eines TextBundle automatisch einschließen.

## Hervorhebungen importieren [importing-highlights]

Wählen Sie **Vorschau > Hervorhebungen importieren…** und dann eine JSON-Datei mit Marked-Hervorhebungen. Der Abgleich erfolgt über die id: neue ids kommen hinzu, übereinstimmende ids werden aktualisiert, und Ihre vorhandenen Hervorhebungen, die nicht in der Datei stehen, bleiben erhalten.

Öffnen Sie ein TextBundle, das `highlights.json` enthält, führt Marked diese Hervorhebungen automatisch zusammen. Solange ein TextBundle geöffnet ist, sichert Marked Änderungen an Hervorhebungen und Kommentaren auch dorthin zurück, ohne `text.md` zu verändern.

## Hervorhebungen im TextBundle [textbundle-highlights]

Aktivieren Sie beim **TextBundle sichern** die Option **Hervorhebungen einschließen**, um `highlights.json` in das Bundle (oder TextPack) einzubetten. Geben Sie das Bundle weiter, damit Mitarbeitende es in Marked öffnen und einen gemeinsamen Satz Hervorhebungen pflegen können.

## CriticMarkup-Aktionen [criticmarkup-actions]

Unabhängig von Export und Import bietet das Vorschau-Menü zwei CriticMarkup-Aktionen für gespeicherte Hervorhebungen:

- **Hervorhebungen als CriticMarkup kopieren** kopiert alle Hervorhebungen im CriticMarkup-Format, ohne die Quelldatei zu ändern.
- **Hervorhebungen in Dokument einfügen…** fragt nach einer Bestätigung und umschließt dann eindeutig zuordenbaren Quelltext mit CriticMarkup. Fehlende, doppelte oder überlappende Treffer überspringt Marked und meldet das Ergebnis.

Mit Signatur und Kommentar entsteht <code>{=<span>=</span>hervorgehobener Text==}{&gt;&gt;Signatur: Kommentar&lt;&lt;}</code>. Nur mit Kommentar verwendet Marked <code>{=<span>=</span>hervorgehobener Text==}{&gt;&gt;Kommentar&lt;&lt;}</code>. Nur mit Signatur entsteht <code>{=<span>=</span>hervorgehobener Text==}{&gt;&gt;Signatur&lt;&lt;}</code>. Ohne beides legt Marked lediglich die Markierung <code>{=<span>=</span>hervorgehobener Text==}</code> an.

## Hervorhebungen drucken [printing-highlights]

Lesemodus-Hervorhebungen werden beim Drucken und beim Sichern als PDF standardmäßig einbezogen. Über **Lesemodus-Hervorhebungen einschließen** im Druckdialog ändern Sie das für die aktuelle Ausgabe. Die entsprechende Einstellung unter {% prefspane Export %} legt den Standard für künftige Druck- und PDF-Ausgaben fest.
