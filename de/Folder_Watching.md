# <%= @title %>

Legen Sie einen **Ordner** mit Klartextnotizen auf Marked ab. Marked öffnet ein Vorschaufenster, das immer die **zuletzt bearbeitete** geeignete Datei in diesem Ordner verfolgt (.md, .txt, .markdown usw., entsprechend den Dateitypfiltern von Marked).

Aktualisierungen erfolgen immer dann, wenn eine überwachte Datei gespeichert wird: Wenn die neueste Datei dieselbe wie zuvor ist, scrollt Marked in Richtung des erkannten Bearbeitungsbereichs. Wenn Sie zwischen Dokumenten wechseln, wechselt die gesamte Vorschau zur aktiven Datei.

## Funktioniert gut mit nvUltra, nvALT und ähnlichen Tools [works-well-with-nvultra-nvalt-and-similar-tools]

Notebook-Apps, die einzelne Dateien auf der Festplatte belassen (klassische Bibliotheken im **nvALT**-, **nvUltra**-, **Notational Velocity**-Stil, synchronisierte Git-Ordner, Dropbox-Scratch-Ordner usw.) lassen sich auf natürliche Weise mit der Ordnerüberwachung kombinieren – Sie schreiben in ein Fenster und lassen Marked daneben angeheftet, ohne die Vorschau manuell erneut zu öffnen.

**nvUltra** bietet im Kontextmenü außerdem **[Preview File(s) in Marked](nvUltra.html)** an, wenn Sie bestimmte Notizen direkt in Marked öffnen möchten, und im Menü View **[Enable Marked Streaming Preview](nvUltra.html#streaming-preview)** für eine Live-Vorschau während der Eingabe. **nvALT** streamt automatisch, solange es geöffnet ist. Siehe [nvALT](nvALT.html).

Marked verwendet dasselbe Überwachungsverhalten auch unter anderen Menünamen, wenn Sie viele kleine Kapitel zu einem Leseerlebnis zusammenfassen. Siehe auch [Mehrteilige Dokumente](Multi-File_Documents.html) für Manuskripte, die bewusst mehrere Markdown-Quellen zusammenführen.

## Einen Ordner durchsehen [review-a-folder]

Wenn Sie eine Reihe von Dateien der Reihe nach lesen möchten, etwa eine Folge generierter Prompts oder Kapitelentwürfe, schalten Sie für den Ordner den Durchsichtsmodus ein. Wählen Sie in einem Ordnerfenster **Verlauf > Diesen Ordner durchsehen**. Wenn Sie gerade eine einzelne Datei ansehen, öffnet derselbe Befehl deren Ordner im Durchsichtsmodus.

Im Durchsichtsmodus:

- Marked öffnet die erste Datei, die Sie noch nicht durchgesehen haben, in Finder-Namensreihenfolge (`file2.md` kommt vor `file10.md`).
- **Verlauf > Als durchgesehen markieren und weiter** (⌃⌘↩) hakt die aktuelle Datei ab und öffnet die nächste nicht durchgesehene.
- Der Fenstertitel und die Durchsichts-Seitenleiste zeigen Ihren Fortschritt an, etwa „42 / 118“.
- Klicken Sie in der Seitenleiste auf eine Datei, um sie zu öffnen, oder auf ihr Kästchen, um sie als durchgesehen oder nicht durchgesehen zu markieren. Ein Strich im Kästchen bedeutet, dass sich die Datei nach Ihrer Durchsicht geändert hat; sie zählt dann wieder als nicht durchgesehen.
- Das Einblendmenü der Seitenleiste zeigt alle Dateien, nur nicht durchgesehene oder nur durchgesehene Dateien. **Verlauf > Durchsichts-Seitenleiste anzeigen** blendet die Seitenleiste aus oder ein.
- Wenn andere Dateien im Ordner gespeichert werden, aktualisiert sich die Anzahl, ohne dass Marked von der Datei wegwechselt, die Sie gerade lesen.

Marked merkt sich den Fortschritt für jeden Ordner, und ein Ordner, den Sie gerade durchsehen, öffnet sich wieder im Durchsichtsmodus. Der Durchsichtsmodus listet nur Dateien direkt im Ordner auf, keine Dateien in Unterordnern. Wählen Sie erneut **Diesen Ordner durchsehen**, um den Durchsichtsmodus auszuschalten; Ihr Fortschritt bleibt erhalten.
