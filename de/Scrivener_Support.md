# <%= @title %>

Nutzen Sie Ihre beiden Lieblings-Schreibwerkzeuge gemeinsam.

> Marked kann weiterhin Scrivener-2.0-Dateien lesen, aber ab Marked 2.5.11 konzentriert sich die Entwicklung auf Version 3.

## Scrivener 3.0 Grundlagen

Ziehen Sie ein Scrivener-Projekt (`.scriv`) auf Marked. Es wird kompiliert und in der Vorschau angezeigt. Wenn Sie die Option zum Öffnen von `.scriv`-Dateien in Scrivener (oben) wählen, startet Marked auch Scrivener, wenn Sie die Datei auf Marked ziehen.

Wie bei anderen Dokumenten werden Änderungen an Scrivener-Dateien beim Speichern live aktualisiert. Wenn sich außerdem ein Scrivener-Dokument im Vordergrund in Marked befindet, wird es von {% kbd cmd E %} in Scrivener für Sie geöffnet.

## Ordnerdokumente filtern

Wenn Sie ein Scrivener-Projekt in Marked öffnen, wird der Vorschauinhalt nur aus den von Ihnen ausgewählten Binder-Dokumenten erstellt. Für `.scriv`-Dateien ist die Filterung immer aktiv; das Filterfeld ist lediglich eine praktische Möglichkeit, den Inhalt zu ändern.

Öffnen Sie das Bedienfeld über **Proofing > Scrivener-Dokumente filtern** ({% kbd opt-cmd-f %}). Der Menüpunkt zeigt ein Häkchen, während das Bedienfeld sichtbar ist. Durch das Schließen des Bedienfelds wird die Filterung nicht deaktiviert und Ihre Auswahl wird nicht zurückgesetzt.

Im Filterbereich werden die Ordnerbereiche Ihres Projekts aufgelistet (Entwurf, Recherche und andere Ordner der obersten Ebene außer Papierkorb). Jeder Abschnitt ist standardmäßig minimiert. Erweitern Sie einen Abschnitt, um seine Dokumente und Ordner als Gliederung anzuzeigen:

- Aktivieren oder deaktivieren Sie ein beliebiges **Textdokument**, um es in die Vorschau einzuschließen oder davon auszuschließen.
- Klicken Sie auf eine **Ordnerzeile**, um alle untergeordneten Elemente auszuwählen oder die Auswahl aufzuheben. Ein Strich im Kontrollkästchen bedeutet, dass nur einige Nachkommen ausgewählt sind.
- Zeilen, für die **In Kompilierung einbeziehen** in Scrivener deaktiviert ist, werden ausgegraut angezeigt. Sie können sie jedoch weiterhin aktivieren, um sie in der Marked-Vorschau anzuzeigen.
- **Bilder, PDFs und andere Nicht-Text**-Ordnerelemente werden in der Liste angezeigt, können aber nicht ausgewählt werden.
- **Fehlende RTF**-Dateien werden weiterhin angezeigt. Wenn Sie Inhalte in Scrivener hinzufügen, während Marked geöffnet ist, wird die Vorschau beim Speichern wie bei jeder anderen Scrivener-Änderung aktualisiert.

Verwenden Sie **Alle auswählen** und **Alle abwählen** oben im Bedienfeld für das gesamte Projekt. Jede Abschnittsüberschrift verfügt nur für diesen Abschnitt über die Schaltflächen **Alle** und **Keine**. **Alle abwählen** bedeutet, dass keine Dokumente ausgewählt werden.

Wenn nichts ausgewählt ist, zeigt die Vorschau eine kurze Nachricht mit einem Link zum Öffnen des Filterbereichs (`x-marked://scrivenerfilter`). Sie können diese URL in Skripten oder anderen Apps verwenden, um das Bedienfeld für das vorderste Scrivener-Dokument in Marked aufzurufen.

Ihre Kontrollkästchen-Auswahl wird pro Scrivener-Projekt gespeichert (über die Projektkennung in der Datei `.scrivx`) und wiederhergestellt, wenn Sie das Projekt das nächste Mal in Marked öffnen. Wenn Sie ein Projekt zum ersten Mal öffnen, wählt Marked nur **Entwurf**-Binder-Dokumente aus, deren Flag **In Kompilierung einbeziehen** auf Ja gesetzt ist (oder nicht gesetzt ist, was Scrivener als Ja behandelt). Recherche und andere Ordner sind anfangs deaktiviert; von der Kompilierung ausgeschlossene Entwurfselemente sind anfangs nicht ausgewählt, bleiben aber in der Liste auswählbar.

Scrivener-2-Projekte zeigen im Filterbereich nur den Ordner **Entwurf**. Scrivener-3-Projekte umfassen alle Ordner außer Papierkorb.

Das Filterfeld kann zusammen mit anderen Tools wie **Visualize Word Repetition** geöffnet bleiben. Wenn Sie ein Kontrollkästchen ändern, wird die Vorschau nach einer kurzen Verzögerung neu kompiliert. Wenn ein großes Projekt noch kompiliert wird, bricht Marked den laufenden Import ab und beginnt erneut mit Ihrer neuen Auswahl.

## Markdown-Header aus Scrivener-Titeln

Marked kann für Sie auch hierarchische Markdown-Header basierend auf den Seiten Ihrer Scrivener-Datei erstellen. Aktivieren Sie dazu einfach die oben angezeigte Option.

## MultiMarkdown-Metadaten

Wenn das erste Dokument in Ihrem Entwurfsordner den Namen „Metadaten“ trägt, wird es am Anfang des Vorschaudokuments als MultiMarkdown-Metadaten behandelt. Für diesen Abschnitt wird unabhängig von der Einstellung „Markdown Headers from Scrivener Titles“ (oben beschrieben) kein Header eingefügt, sodass der MultiMarkdown-Prozessor ihn als Metadaten lesen und entsprechende Ersetzungen und Exportoptionen zulassen kann.

Sie können diese Datei im YAML-Format formatieren, wenn Ihr Prozessor YAML verarbeitet.

Wenn Sie kein `metadata`-Dokument verwenden, kann Marked auch MultiMarkdown-Metadaten aus den Kompilierungseinstellungen Ihres Projekts (`Settings/compile.xml`) voranstellen und dabei dieselben Felder **Titel** und **Autor** verwenden, die Scrivener nach MultiMarkdown exportieren würde. Dies ist standardmäßig aktiviert (Präferenzschlüssel `scrivenerCompileMetadata`). Custom-Metadatenfelder werden nur einbezogen, wenn sie in den Kompilierungseinstellungen für **MMD-Metadaten** des Projekts erscheinen, nicht aus benutzerdefinierten Feldern pro Dokument.

## Links

Für externe (HTTP-)Links können Sie entweder Markdown-Syntax oder die Linkformatierung von Scrivener verwenden. Marked konvertiert das Scrivener-Format vor der Verarbeitung in Markdown.

## Kommentare

Marked kann Kommentare und Fußnoten verarbeiten, die inline im Dokument erstellt wurden.

## Tabellen

Marked kann grundlegende Scrivener-Tabellen konvertieren. Wenn Sie jedoch eine Tabelle in Ihre Ausgabe einbinden möchten, verwenden Sie dafür am besten das [MultiMarkdown table format](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (Eine App namens [TableFlip](http://tableflipapp.com/) kann das Generieren dieser Dateien stark vereinfachen.)

## Zusätzliche Scrivener-Funktionen

Zusätzlich zu den grundlegenden Kompilierungs- und Vorschaufunktionen unterstützt Marked auch einige Scrivener-spezifische Konventionen. Erstens können Sie in Ihrem Scrivener-Dokument „Formatierung beibehalten“ inline oder für einen eigenständigen Textblock verwenden, der dann in der Vorschau in Codeblöcke konvertiert wird.

Marked liest auch _inline_-Fußnoten aus Scrivener. Wenn Sie innerhalb oder am Ende eines Absatzes eine Fußnote eingeben, wird diese in der Vorschau in eine MultiMarkdown-Fußnote umgewandelt.

## Verwenden von Bildern in Ihrem Scrivener-Dokument

Bilder können in das Scrivener-Dokument eingebettet oder mit Markdown-Bildsyntax referenziert werden. Die Markdown-Version eines Bild-Tags ist `![alt text](path/to/image.ext "optional title/description")`. Es kann auch das Referenzformat verwendet werden:

![alt text][img1]

    [img1]: /path/to/image.ext "optional description"

Der Basispfad für die HTML-Ausgabe in der Vorschau wird auf den Ordner festgelegt, der das Scrivener-Dokument enthält. Wenn Sie die Bilder also im selben Ordner wie das Arbeitsdokument ablegen, können Sie direkt auf sie zugreifen. Wenn sich Ihr Scrivener-Dokument in `~/Desktop/TestDoc.scriv` befindet und Sie ein Bild mit dem Namen „testimage.png“ in `~/Desktop/testimage.png` haben, können Sie das Bild zu Ihrem Dokument hinzufügen, indem Sie Folgendes verwenden:

![Test image](testimage.png)

Relative Pfade, die auf dem übergeordneten Ordner des Dokuments basieren, funktionieren. Absolute Pfade ermöglichen den Zugriff auf Bilder an beliebigen Orten, sind für die HTML-Ausgabe aber möglicherweise weniger portierbar.

## Sicherheitshinweis

Ein Cache-Ordner wird in `~/Library/Application Support/Marked` erstellt, wenn Sie Ihre `.scriv`-Datei in Marked öffnen. Dies ist kein geschützter Ordner. Wenn sich Ihr Originaldokument also auf einem verschlüsselten Datenträger befindet oder anderweitig geschützt ist, beachten Sie, dass sein Inhalt unverschlüsselt im Cache liegt. Für eingeschränkten Schutz können Sie sicherstellen, dass dieser Cache nicht in Spotlight angezeigt wird, indem Sie `~/Library/Application Support/Marked` zu Ihren Datenschutzeinstellungen in Spotlight hinzufügen.

Unter [Additional app integrations](Additional_Application_Support.html) finden Sie Informationen zur Zwischenablage-Vorschau, zu Wiki-Links, Skripten und zur vollständigen Liste der App-spezifischen Anleitungen.

