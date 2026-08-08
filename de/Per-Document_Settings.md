# <%= @title %>

Mit Marked lassen sich bestimmte Attribute eines Dokuments im MultiMarkdown-Metadatenformat festlegen (siehe unten). Damit definieren Sie Merkmale und Stile, die nur dieses Dokument betreffen, ohne die Standardeinstellungen zu ändern.

Die meisten MultiMarkdown-Header ignoriert die Vorschau, die folgenden sind jedoch zulässig und beeinflussen das Rendering. Sie können weitere Metadaten aufnehmen, die in der endgültigen Ausgabe erscheinen sollen; Marked ignoriert einfach Schlüssel, die unten nicht aufgeführt sind. Speichern Sie als HTML *ohne* Vorlage, stellt Marked alle Metadatenschlüssel wie erwartet dar.

## Metadatenformat [metadata-format]

Metadaten stehen am Anfang der Markdown-Datei oder direkt nach etwaigen YAML-Headern. Sie bestehen aus einem Schlüssel, gefolgt von einem Doppelpunkt, optionalen Leerzeichen oder Tabulatoren und dem Wert:

	Beispiel-Metadatum: Beispielwert

Mehrere Metadateneinträge sollten je in einer eigenen Zeile stehen, aber ohne Leerzeilen dazwischen. Auf den letzten Metadateneintrag muss eine Leerzeile folgen, bevor der Dokumenttext beginnt.

	Erstens: Dies ist der erste Metadateneintrag
	Zweitens: Dies ist der zweite Eintrag
	Drittens: der letzte Metadateneintrag

	# Der Anfang des Dokumenttextes

## Markeds Metadatenschlüssel [marked-metadata-keys]

### Metadaten für andere Prozessoren ausblenden [hidingmeta]

**Hinweis:** Wenn Sie einen benutzerdefinierten Prozessor verwenden oder Ihr Markdown direkt an einer Quelle veröffentlichen, die diese Metadaten nicht verarbeitet, können Sie sie trotzdem nutzen, indem Sie vor und nach den Metadaten HTML-Kommentarmarkierungen einfügen. Anders als MultiMarkdown und andere Prozessoren findet Marked diese Tags an beliebiger Stelle im Dokument und verarbeitet/entfernt sie aus der Ausgabe. Folgendes im Header liefert daher in Marked das gewünschte Ergebnis, erscheint aber sonst nirgends:

	<!--
	Marked Style: Mein eigener Stil
	Custom Processor: true
	-->

*Achten Sie nur darauf, dass der Metadatenschlüssel am Zeilenanfang ohne Leerzeichen oder Tabulatoren beginnt, und schreiben Sie nach dem Wert nichts weiter in die Zeile.*

### Stile pro Dokument [per-document-styles]

Der Schlüssel `Marked Style:` legt einen Vorschaustil für das Dokument fest. Der Wert kann der Name eines Standardstils oder ein Name bzw. Pfad zu einem [Eigenen Stil](Custom_Styles.html) sein, den Sie in den Einstellungen definiert haben. Wird dieser Schlüssel gefunden und passt er zu einem Marked bekannten Stil, wird dieser Stil bei jedem Laden des Dokuments für die Vorschau verwendet.

**Beispiel**

	Marked Style: Upstanding Citizen

### Sprache der Anführungszeichen [quotes-language]

Standardmäßig verwendet Marked Anführungszeichen im englischen Stil. Pro Dokument ändern Sie das mit dem Schlüssel `Quotes Language:`. Verfügbare Sprachen sind:

* dutch
* english
* french
* german
* guillemets
* swedish

**Beispiel**

	Quotes Language: french

	Erzeugt französische «Anführungszeichen».

### Basis-Überschriftenebene [base-header-level]

Mit dem Schlüssel `Base Header Level:` legen Sie fest, ab welcher Überschriftenebene Marked zu zählen beginnt. Das sollte eine Zahl von 1 bis 6 sein und ändert, wie `#`-Überschriften gerendert werden. Setzen Sie die Ebene auf 3, wird das, was normalerweise eine Überschrift erster Ebene (h1) wäre, als Überschrift dritter Ebene (h3) gerendert, und nachfolgende Überschriften in der Hierarchie werden um 2 verschoben.

**Beispiel**

	Base Header Level: 3

	# Diese Überschrift wird als h3 gerendert

	## Diese Überschrift wird ein h4

	Wird gerendert als:

	<h3>Diese Überschrift wird als h3 gerendert</h3>

	<h4>Diese Überschrift wird ein h4</h4>

### Benutzerdefinierte Prozessoren [custom-processors]

Wie unter [Benutzerdefinierter Prozessor](Custom_Processor.html#preprocessor) beschrieben, aktivieren oder deaktivieren Sie einen benutzerdefinierten Prozessor und Präprozessor über Metadaten:

    Custom Processor: true
    Custom Preprocessor: false

`true` oder `false` schalten den Prä-/Prozessor ein und aus.

Der Wert von `Processor:` kann auf `multimarkdown` oder `discount` gesetzt werden, um einen der internen Prozessoren zu erzwingen. Diese Einstellung pro Dokument ändert nicht die Standardeinstellung unter {% prefspane Processor %}.

### Kopf-/Fußzeilen drucken [print-headersfooters]

Die Einstellungen unter {% prefspane Export %} für Druck-Kopf- und -Fußzeilen überschreiben Sie mit den folgenden Schlüsseln:

	print header left:
	print header center:
	print header right:
	print footer left:
	print footer center:
	print footer right:

Darin können [Druckvariablen](Exporting.html#headers-and-footers) wie `%title`, `%page`, `%total` usw. vorkommen sowie Verweise auf andere Metadaten über `%md_[Schlüssel ohne Leerzeichen]`.

### Druckränder [print-margins]

Die Seitenränder für Druck und paginierten PDF-Export legen Sie mit dem Schlüssel `Margins:` fest. Werte sind in Punkten; Suffixe wie `px`, `pt` und `em` werden ignoriert. Geben Sie zwei Zahlen für vertikale und horizontale Ränder an oder vier Zahlen für oben, rechts, unten und links:

	Margins: 10 20
	Margins: 10, 20, 10, 20

Metadaten-Ränder überschreiben die Einstellungen unter {% prefspane Export %} und die Randfelder im PDF-Export-Panel.

### JavaScript einbinden [inserting-javascript]

Diese Methode gibt Daten an, die im `<head>`-Tag des Dokuments enthalten sind. Marked ignoriert die meisten Werte dieses Schlüssels außer bei der Ausgabe des vollständigen Dokuments, berücksichtigt aber so eingebundene Skripte. Hier definierte Skript-Tags landen nicht im Header, sondern werden vor dem schließenden `</body>`-Tag angehängt. jQuery ist bereits geladen, und Sie können das in allen eingefügten Skripten nutzen.

**Beispiel**

	XHTML Header: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		– oder –

	XHTML Header: <script src="myfancyscript.js"></script>
