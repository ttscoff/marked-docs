# <%= @title %>

Ziehen Sie ein Finis-Projekt auf Marked, um das kompilierte Buch in der Vorschau zu sehen. Ein Finis-Projekt ist ein `.finis`-Paket. Jedes Kapitel ist eine Markdown-Datei, und in `.finis/project.json` stehen die Lesereihenfolge und die Kompilierregeln.

## Ein Projekt öffnen [opening-a-project]

Öffnen Sie das `.finis`-Paket selbst. Marked kompiliert das Buch und zeigt es in einer einzigen Vorschau. Als Fenstertitel erscheint der Projekttitel oder, wenn das Projekt keinen Titel hat, der Name des Pakets.

Mit **⌘E** öffnen Sie das Projekt in Finis.

Sobald Sie `project.json` oder ein Kapitel speichern, das zum Buch gehört, aktualisiert sich die Vorschau.

## Was Marked auslässt [what-marked-leaves-out]

Marked hält sich an die Kompilierregeln, die Finis für das Buch verwendet:

- Dokumente und Ordner, die nicht einbezogen sind, fehlen. Fehlt ein Ordner, fehlt auch alles darin.
- Notizen und Leitfäden fehlen.
- Dokumente mit einem Status, der auf der Ausschlussliste des Projekts steht, fehlen.
- Einträge im Papierkorb von Finis fehlen.

Einen Bereich, in dem Sie Kapitel von Hand auswählen, bietet Marked nicht. Finis-Einstellungen für Seitengröße, Cover und Medien wendet Marked ebenfalls nicht an. Die Vorschau zeigt das kompilierte Markdown.

## Teile und Kapitel [parts-and-chapters]

Kompiliert das Projekt Ordner als Teile, ist jeder Ordner der ersten Ebene ein Teil. Seine Überschrift steht auf Ebene 1, und jedes Dokument darin beginnt auf einer neuen Seite.

Kompiliert das Projekt Ordner als Kapitel, ist jeder Ordner der ersten Ebene ein Kapitel. Die Dokumente darin sind Szenen und bleiben auf derselben Seite.

Legt das Projekt keinen Ordnermodus fest, verwendet Marked Teile, wenn ein Ordner der ersten Ebene einen weiteren Ordner enthält, der seinerseits einbezogene Dokumente enthält. Andernfalls verwendet Marked Kapitel. Ein Buch, das nur aus Dokumenten besteht und keine Ordner hat, erhält weder Teil- noch Kapitelüberschriften und keine Seitenumbrüche zwischen diesen Dokumenten.

## Seitenumbrüche [page-breaks]

Ein Dokument, das auf einer eigenen Seite stehen soll, beginnt und endet mit einem Seitenumbruch. Marked entfernt die erste Markdown-Überschrift in diesem Dokument, damit sie unter dem erzeugten Titel nicht doppelt erscheint. Setext-Überschriften lässt Marked dabei stehen.

Folgen mehrere Seitenumbrüche direkt aufeinander, bleibt nur einer übrig.

## Überschriften [headings]

Als Ordnerüberschrift dient der Ordnername oder der Überschriftstext, den das Projekt für den Ordner festlegt. Die Ebene beginnt bei 1 und steigt mit jedem verschachtelten Ordner um eins, höchstens bis Ebene 6. Verlangt das Projekt eine Warnung, wenn eine Überschrift tiefer als Ebene 6 liegt, verwendet die Vorschau trotzdem Ebene 6 und zeigt einen einzeiligen Hinweis.

Eine erzeugte Überschrift erhält ein Dokument nur, wenn das Projekt Dokumenttitel verlangt oder wenn das Dokument selbst eine Überschrift verlangt und das Projekt Dokumenttitel nicht abschaltet. Ein `.md` am Ende entfernt Marked nur, wenn es den Dateinamen als Überschrift verwendet. Beginnt die Datei bereits mit derselben Überschrift, fügt Marked sie nicht noch einmal ein.

Die Nummerierung gilt nur für Überschriften, die Marked einfügt. Der Stil richtet sich nach der Nummerierungseinstellung des Projekts: keine, arabische Ziffern, römische Ziffern oder ausgeschriebene Zahlwörter. Die Bezeichnungen folgen der Projektsprache, wenn diese Englisch, Italienisch, Französisch, Deutsch, Spanisch oder Portugiesisch ist. Bei anderen Sprachen verwendet Marked englische Bezeichnungen und arabische Ziffern.

## Titelei [front-matter]

Bezieht das Projekt eine Titelei ein, fügt Marked einen MultiMarkdown-Block mit Titel, Untertitel, Autor und Sprache hinzu, soweit diese Felder Werte haben. Beginnt das erste einbezogene Dokument bereits mit YAML- oder MultiMarkdown-Metadaten, lässt Marked diesen Block unverändert und fügt keinen weiteren hinzu.

## Bilder [images]

Relative Bild- und Linkpfade schreibt Marked so um, dass sie nicht mehr vom Ordner des Kapitels, sondern vom Projektpaket ausgehen. So erscheinen Bilder aus dem Projekt auch in der zusammengefügten Vorschau. Webadressen, E-Mail-Links und Links, die mit `#` beginnen, bleiben unverändert. Ein Pfad, der aus dem Paket hinausführen würde, bleibt ebenfalls unverändert.
