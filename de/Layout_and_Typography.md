# <%= @title %>

Marked bietet Standardeinstellungen zur Verbesserung der Typografie und des Exportlayouts sowie detaillierte Optionen für weitere Anpassungen.

## Typografie

### Silbentrennung und Witwen

Mit der Option „Automatische Silbentrennung in Absätzen“ kann Marked bestimmen, wo eine Zeile am besten getrennt werden sollte, um das Satzbild eines Absatzes zu verbessern. Dies ist besonders bei Blocksatz nützlich, kann aber auch den Lesefluss in längeren Absätzen verbessern.

Wenn die Option „Witwen in Überschriften und Absätzen verhindern“ aktiviert ist, werden Umbrüche in Überschriften und Absätzen erzwungen, um zu verhindern, dass einzelne, kurze Wörter alleine in einer Zeile landen.

Marked hält Überschriften automatisch mit dem folgenden Element zusammen, damit beim Export in ein seitenbasiertes Format (PDF, Druck) keine verwaisten Überschriften entstehen.

### Satzzeichen

Wenn Ihr Prozessor auf MultiMarkdown eingestellt ist, haben Sie die Möglichkeit, die „intelligente Interpunktion“ mithilfe der Option „Typografisch korrekte Anführungszeichen und Interpunktion generieren“ zu aktivieren oder zu deaktivieren. Wenn diese Option aktiviert ist, werden gepaarte doppelte und einfache Anführungszeichen in „geschweifte“ Anführungszeichen umgewandelt, Apostrophe werden durch typografisch korrekte Symbole ersetzt und andere automatische Anpassungen werden durchgeführt.

### Fußnotenmarkierungen

Im Abschnitt „Layout und Typografie“ von {% prefspane Style %} ist _Fußnotenmarkierungen mit eckigen Klammern umgeben_ standardmäßig aktiviert, wenn der MultiMarkdown-Prozessor verwendet wird, und erstellt Fußnotenmarkierungen innerhalb des Dokuments, die von eckigen Klammern umgeben sind (z. B. „[1]“). Um die Erstellung der eckigen Klammern zu deaktivieren, deaktivieren Sie diese Option.

## Gliederungsmodus

Im Gliederungsmodus wird jede Datei, die eine hierarchische Reihe von Überschriften enthält, als APA- oder Dezimalgliederung angezeigt. Standardmäßig wird der APA-Stil verwendet; diese Einstellung kann jedoch deaktiviert werden.

Im {% prefspane Style %} unter „Layout und Typografie“ können Sie Dateinamenerweiterungen hinzufügen, für die der Gliederungsmodus automatisch aktiviert wird. Dies ist besonders nützlich für OPML und unterstützte Mindmap-Dateien (wie iThoughtsX und MindNode). Die Erweiterung sollte nur der alphanumerische Teil des Dateinamens sein, der nach dem letzten Punkt erscheint.

Schalten Sie den Standard-Gliederungsmodus mit dem Kontrollkästchen „APA-Stil verwenden“ um. Dies kann vorübergehend über das Zahnradmenü eines Dokumentfensters umgeschaltet werden.


## Poesie

Die Option _Style wörtliche Codeblöcke als Poesie_ in {% prefspane Style %} führt dazu, dass Blöcke, die um 4 oder mehr Leerzeichen eingerückt sind, im Stil „Poesie“ des Themas angezeigt werden. Dies ist normalerweise ein nicht syntaxhervorgehobener, kursiver Abschnitt.

Zeilenumbrüche bleiben in diesen Blöcken standardmäßig erhalten, sodass Sie auf einfache Weise Gedichte und lyrische Abschnitte in ein Dokument integrieren können, für das keine anderen Codeblöcke erforderlich sind.

> Diese Einstellung fügt eine „Poetry“-Körperklasse hinzu, die in benutzerdefinierten Designs verwendet werden kann, um Codeblöcke und andere Elemente zu formatieren, wenn der „Poetry-Modus“ aktiviert ist.

## Codeblockumbruch

Mit „Designs erlauben, Text in Codeblöcke einzuschließen“ lässt der Vorschaustil bestimmen, wie Codeblöcke formatiert werden. Das Deaktivieren dieser Option zwingt alle Codeblöcke dazu, den horizontalen Überlauf zu scrollen, anstatt ihn zu umbrechen, unabhängig vom aktuellen Vorschaustil.

## Arbeiten im Vollbildmodus

Wenn Sie Marked im Vollbildmodus (Strg-Befehl-F) verwenden, möchten Sie möglicherweise die Breite des angezeigten Texts begrenzen, um eine zentrierte Spalte mit lesbarem Inhalt zu erstellen. Über das Kontrollkästchen „Textbreite in der Vorschau begrenzen“ wird ein Schieberegler aktiviert, mit dem Sie die maximale Breite des angezeigten Inhalts festlegen können. Dies betrifft auch die Nicht-Vollbildanzeige.

