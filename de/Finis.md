# <%= @title %>

Ziehen Sie ein Finis-Projekt auf Marked, um das kompilierte Buch in der Vorschau zu sehen. Ein Finis-Projekt ist ein `.finis`-Paket. Jedes Kapitel ist eine Markdown-Datei, und `.finis/project.json` speichert die Lesereihenfolge und die Kompilierregeln.

## Ein Projekt öffnen [opening-a-project]

Öffnen Sie das `.finis`-Paket selbst. Marked kompiliert das Buch und zeigt es in einer Vorschau. Der Fenstertitel ist der Projekttitel oder, wenn das Projekt keinen Titel hat, der Paketname.

Drücken Sie **⌘E**, um das Projekt in Finis zu öffnen.

Wenn Sie `project.json` oder ein Kapitel speichern, das zum Buch gehört, wird die Vorschau aktualisiert.

## Was Marked auslässt [what-marked-leaves-out]

Marked folgt den Kompilierregeln, die Finis für das Buch verwendet:

- Dokumente und Ordner, die nicht eingeschlossen sind, werden ausgelassen. Ein ausgelassener Ordner lässt auch alles darin aus.
- Notizen und Leitfäden werden ausgelassen.
- Statuswerte auf der Ausschlussliste des Projekts werden ausgelassen.
- Einträge im Papierkorb von Finis werden ausgelassen.

Marked bietet kein Fenster, in dem Sie Kapitel von Hand auswählen, und wendet keine Finis-Einstellungen für Seitengröße, Cover oder Medien an. Die Vorschau ist das kompilierte Markdown.

## Teile und Kapitel [parts-and-chapters]

Wenn das Projekt Ordner als Teile kompiliert, ist jeder Ordner der ersten Ebene ein Teil. Seine Überschrift hat Ebene 1, und jedes Dokument darin beginnt auf einer neuen Seite.

Wenn das Projekt Ordner als Kapitel kompiliert, ist jeder Ordner der ersten Ebene ein Kapitel. Dokumente darin sind Szenen und bleiben auf derselben Seite.

Wenn das Projekt keinen Ordnermodus festlegt, verwendet Marked Teile, sobald ein Ordner der ersten Ebene einen weiteren Ordner enthält, der selbst eingeschlossene Dokumente enthält. Andernfalls verwendet Marked Kapitel. Ein Buch, das nur aus Dokumenten besteht und keine Ordner hat, erhält keine Teil- oder Kapitelüberschriften und keine Seitenumbrüche zwischen diesen Dokumenten.

## Seitenumbrüche [page-breaks]

Ein Dokument, das eine eigene Seite erhalten soll, beginnt und endet mit einem Seitenumbruch. Marked entfernt die erste Markdown-Überschrift in diesem Dokument, damit sie nicht unter dem erzeugten Titel wiederholt wird. Setext-Überschriften bleiben unverändert.

Aufeinanderfolgende Seitenumbrüche werden zu einem zusammengefasst.

## Überschriften [headings]

Ordnerüberschriften verwenden den Ordnernamen oder den Überschriftstext, den das Projekt für diesen Ordner festlegt. Die Ebene beginnt bei 1 und steigt mit jedem verschachtelten Ordner um eins, höchstens bis Ebene 6. Wenn das Projekt eine Warnung verlangt, sobald eine Überschrift tiefer als Ebene 6 ist, verwendet die Vorschau trotzdem Ebene 6 und zeigt einen einzeiligen Hinweis.

Ein Dokument erhält eine erzeugte Überschrift nur, wenn das Projekt Dokumenttitel verlangt oder wenn dieses Dokument eine Überschrift verlangt und das Projekt Dokumenttitel nicht ausschaltet. Marked entfernt ein nachgestelltes `.md` nur, wenn es den Dateinamen als Überschrift verwendet. Beginnt die Datei bereits mit derselben Überschrift, fügt Marked sie nicht erneut hinzu.

Die Nummerierung gilt nur für Überschriften, die Marked einfügt. Der Stil folgt der Nummerierung des Projekts: keine, arabisch, römisch oder Wörter. Die Bezeichnungen folgen der Projektsprache für Englisch, Italienisch, Französisch, Deutsch, Spanisch und Portugiesisch. Andere Sprachen verwenden englische Bezeichnungen und arabische Ziffern.

## Vorspann [front-matter]

Wenn das Projekt einen Vorspann einschließt, fügt Marked einen MultiMarkdown-Block mit Titel, Untertitel, Autor und Sprache hinzu, soweit dafür Werte vorhanden sind. Beginnt das erste eingeschlossene Dokument bereits mit YAML- oder MultiMarkdown-Metadaten, lässt Marked diesen Block unverändert und fügt keinen weiteren hinzu.

## Bilder [images]

Relative Bild- und Linkpfade werden vom Ordner des Kapitels zum Projektpaket umgeschrieben, sodass Bilder im Projekt auch in der zusammengefügten Vorschau erscheinen. Webadressen, E-Mail-Links und Links, die mit `#` beginnen, bleiben unverändert. Ein Pfad, der das Paket verlassen würde, bleibt unverändert.
