# <%= @title %>

Diese Optionen finden Sie im Dialogblatt **Apex konfigurieren**. Sie öffnen es unter {% prefspane Processor %}, wenn **Apex (beta)** der Standardprozessor ist. Alle Optionen hier gelten ausschließlich für Apex. Mathematik, CriticMarkup, Hashtags, Dateieinbindungen und Überschriften-IDs bleiben in Markeds übrigen Einstellungen.

Was Apex ist und welche Syntax es abdeckt, steht unter [Apex (Beta)](Apex.html).

Die Kontrollkästchen im Dialogblatt überschreiben dieselben Einstellungen in einer Apex-Metadatendatei. Dateipfade sind optional. Einen Pfad, den Marked nicht lesen kann, überspringt es; die Vorschau läuft trotzdem.

## Dateien [files]

CSL
: Eine Citation-Style-Language-Datei (`.csl`), die Apex beim Formatieren eines Literaturverzeichnisses verwendet. Bleibt das Feld leer, gilt der Stil, der im Dokument oder in der Metadatendatei angegeben ist.

Bibliografie
: Eine oder mehrere Bibliografiedateien. Zulässig sind BibTeX (`.bib`), CSL JSON (`.json`) und CSL YAML (`.yml`, `.yaml`). Mit **Hinzufügen** ergänzen Sie eine weitere Datei. Apex sucht in diesen Dateien, wenn es Zitate auflöst.

Konkordanz
: Eine oder mehrere Konkordanzdateien (`.tsv`, `.txt` oder `.csv`), die beim Erstellen eines Index verwendet werden. Mit **Hinzufügen** ergänzen Sie eine weitere Datei.

Metadatendatei
: Eine externe Metadatendatei (`.yml`, `.yaml`, `.txt` oder `.md`), die vor dem Apex-Lauf eingebunden wird. Setzen beide denselben Schlüssel, haben die Dokumentmetadaten weiterhin Vorrang. Die Kontrollkästchen in diesem Dialogblatt gehen den Werten der Metadatendatei vor.

## Syntax [syntax]

Standardmäßig aktiviert, sofern nicht anders angegeben.

Tabellen
: Pipe-Tabellen mit Kopfzeile und Trennzeile.

Fußnoten
: Referenzfußnoten (`[^id]`) und Inline-Fußnoten.

Definitionslisten
: Listen aus Begriff und Definition (`: definition`).

Hoch-/Tiefstellung
: `^super^` und `~sub~`. Schalten Sie das ab, wenn einzelne Tilden nicht als Tiefstellung gelten sollen. Markeds Einstellung **`~text~` als Unterstreichung rendern** ist davon unabhängig und steht im Konflikt mit der Tiefstellung.

Durchstreichung
: `~~deleted~~`.

URLs und E-Mails automatisch verlinken
: Nackte `https://`-URLs und E-Mail-Adressen werden zu Links.

Abgegrenzte Divs
: `::: name`-Blöcke, die einen Abschnitt in ein `<div>` einschließen.

Spans in eckigen Klammern
: Inline-Attributspans wie `[text]{.class}`.

Alphabetische Listen
: Listen, die mit `a.` oder `A.` beginnen, zusätzlich zu Zahlen.

Gemischte Listenzeichen
: Eine Liste darf `*`, `+` und `-` mischen und bleibt trotzdem eine Liste.

Markdown in HTML
: Markdown innerhalb von HTML-Block-Tags wird verarbeitet. Manches Markup kann trotzdem brechen.

Metadatentransformationen
: `[%key]`-Platzhalter werden aus den Dokumentmetadaten ersetzt.

## Tabellen und Bilder [tables-and-images]

Gittertabellen
: Tabellen im Gitterstil, gezeichnet mit `+` und `|`. Standardmäßig deaktiviert.

Lockere Tabellen
: Pipe-Tabellen dürfen die Pipes am Zeilenanfang und -ende weglassen. Standardmäßig aktiviert.

Ausrichtung pro Zelle
: Ausrichtungsmarker in einer Tabellenzelle überschreiben die Spaltenausrichtung. Standardmäßig aktiviert.

Bildunterschriften
: Der Bildtitel – oder der Alternativtext, wenn es keinen Titel gibt – wird als sichtbare Bildunterschrift angezeigt. Standardmäßig aktiviert.

Nur Titel als Bildunterschrift
: Ausschließlich der Bildtitel wird als Bildunterschrift verwendet, der Alternativtext bleibt unberücksichtigt. Standardmäßig deaktiviert. Wirkt nur, wenn **Bildunterschriften** aktiviert ist.

## Links und Indizes [links-and-indexes]

Wiki-Links
: Apex wandelt `[[wiki links]]` um. Standardmäßig deaktiviert. Ist die Option aktiv, überspringt Marked für dieses Dokument seinen eigenen Durchlauf „Wiki-Links umwandeln" aus den Vorschau-Einstellungen, und Apex löst die Zieldatei unter Umständen anders auf als Marked. Die Standard-Dateiendung stammt aus Markeds Wiki-Link-Einstellungen.

Wiki-Link-URLs bereinigen
: Erzeugte Wiki-Link-URLs werden in Kleinbuchstaben umgewandelt, Apostrophe entfernt und alle übrigen Zeichen, die weder Buchstaben noch Ziffern sind, ersetzt. Standardmäßig deaktiviert. Nur verfügbar, wenn **Wiki-Links** aktiviert ist.

Indexverarbeitung
: Erkennt Indexmarker (MultiMarkdown-, mmark-, Leanpub- und textindex-Stil). Standardmäßig aktiviert.

Indexausgabe unterdrücken
: Indexmarker werden weiterhin gelesen, der erzeugte Index aber nicht ausgegeben. Standardmäßig deaktiviert.

## Callouts (extra) [callouts-extra]

Beide standardmäßig deaktiviert. Callouts von Obsidian und Bear (`> [!NOTE]`) verarbeitet Marked vor Apex; sie werden hier nicht gesteuert.

Python-Markdown-Callouts (!!!)
: Callouts im Stil `!!! note`.

Quarto-Callouts
: Quarto-Blöcke der Form `::: {.callout-note}`.

## Barrierefreiheit [accessibility]

Beide standardmäßig deaktiviert.

ARIA-Labels
: Fügt ARIA-Attribute hinzu, die die Struktur des von Apex erzeugten HTML beschreiben.

Überschriften-<a>-Anker
: Gibt an jeder Überschrift einen `<a>`-Anker aus statt nur einer `id` an der Überschrift.
