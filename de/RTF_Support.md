# <%= @title %>

Marked kann Dokumente im Rich Text Format (`.rtf`) und RTFD (`.rtfd`) direkt öffnen. Ziehen Sie eine Datei auf Marked oder verwenden Sie {% appmenu Ablage, Öffnen… ({{cmd}}O) %}. Das Dokument wird zur Vorschau und zum Export in Markdown konvertiert.

Dies funktioniert gut mit Dokumenten aus **Pages**, **TextEdit**, **Word** und anderen Apps, die RTF oder RTFD speichern. Marked ist immer noch ein **Vorschau**-Tool: Sie bearbeiten es in der Originalanwendung und Marked wird beim Speichern aktualisiert.

## So funktioniert die Konvertierung

Marked konvertiert RTF mithilfe der Systemtext-Engine in HTML und dann in Markdown. Der Konverter:

- Ordnet **große Absatzschriftgrößen** den Überschriftenebenen zu (relativ zur häufigsten Textgröße im Dokument)
- Behält **Fett**, *Kursiv* und Links nach Möglichkeit bei
- Extrahiert **Bilder** aus RTFD-Bundles und eingebetteten Anhängen
- Behandelt RTF-Dateinamen **nicht** als Bildunterschriften (siehe Bilder unten)

Die gleiche Konvertierungspipeline wird für die Kompilierung von Scrivener RTF und für RTF-Dateien verwendet, die in anderen Dokumenten enthalten sind.

## Live-Vorschau

Wenn Sie die RTF- oder RTFD-Datei in einer anderen Anwendung speichern, erkennt Marked die Änderung und aktualisiert die Vorschau automatisch.

## Bilder

RTF definiert kein separates „Beschriftungsfeld“ in der Art und Weise, wie Cocoa nach HTML exportiert. Was in Ihrem Layout wie eine Bildunterschrift aussieht, ist normalerweise **normaler Text** im nächsten Absatz, und Marked behält diesen als Fließtext bei.

Eingebettete Bilder und Bilder in RTFD-Bundles (z. B. `pastedGraphic.png` in einem Pages-Export) werden in einen Cache-Ordner unter `~/Library/Caches/Marked/Watchers/` kopiert. Vorschaubildpfade verweisen auf diese zwischengespeicherten Dateien, bis Sie sie exportieren.

Marked verwendet den Bilddateinamen **nicht** als Alternativtext oder als MultiMarkdown-Bildunterschrift. Unter dem Bild sollte kein `pastedGraphic.png` angezeigt werden, es sei denn, Sie haben diesen Text in das Dokument eingegeben.

## Export und andere Funktionen

Nach der Konvertierung behandelt Marked das Dokument wie andere kompilierte Quellen (ähnlich wie [Scrivener](Scrivener_Support.html) und [DOCX](Working_With_DOCX.html)): Export, Statistiken und die meisten Vorschaufunktionen werden mit dem generierten Markdown ausgeführt, das im Watchers-Cache gespeichert ist.

## Einschränkungen

Die Konvertierungsqualität hängt von der Quellanwendung ab. Im Allgemeinen:

- **Überschriften** werden aus der Schriftgröße abgeleitet, nicht aus den Gliederungsstilen von Word/Pages
- **Komplexes Layout** (mehrspaltige Tabellen, die nur zur Positionierung verwendet werden, Textfelder) wird möglicherweise nicht sauber auf Markdown abgebildet
- **Gleichungen** in RTF werden in der Vorschau nicht unterstützt (siehe [MathJax](MathJax.html) für Mathematik in Markdown)
- **Legacy `.doc`** (binäres Word) wird nicht unterstützt; Speichern Sie zuerst als DOCX oder RTF

Für ein einmaliges Einfügen ohne Speichern einer Datei verwenden Sie stattdessen die [Zwischenablage-Vorschau](Opening_Files.html#from-the-clipboard).

## Verwandte Themen

- [PDF-Unterstützung](PDF_Support.html) – PDF-Dokumente als Markdown-Quellen öffnen
- [Arbeiten mit DOCX](Working_With_DOCX.html) – Word-Dokumente mit Änderungsverfolgung und Kommentaren
- [Dateien öffnen](Opening_Files.html) – Drag & Drop, Zuletzt geöffnet, Zwischenablage
- [Export](Exporting.html) – Kopieren Sie Rich Text und speichern Sie RTFD (Export), im Gegensatz zum Öffnen von RTF als Quelldatei