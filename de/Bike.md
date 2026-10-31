# <%= @title %>

Ziehen Sie eine [Bike][bike]-Gliederung (`.bike`) auf Marked, um sie als verschachtelte Markdown-Liste zu sehen, mit Überschriftszeilen in fett und Aufgaben als Kontrollkästchen.

## Eine Bike-Gliederung öffnen [opening-a-bike-outline]

Marked wandelt die Gliederung um, wenn Sie die Datei öffnen:

- Als Überschrift markierte Zeilen werden **fett** gesetzte Listeneinträge.
- Aufgaben werden Kontrollkästchen im GitHub-Stil. Eine Aufgabe ist abgehakt, wenn Bike einen Abschlusszeitpunkt speichert oder sie als erledigt markiert.
- Links und Inline-Formatierung im Zeilentext bleiben als Markdown erhalten.

Eine geöffnete `.bike`-Datei verwendet immer diese Liste. Die Gliederung wird dabei nicht zu einem Mermaid-Diagramm.

## Eine Bike-Gliederung einbinden [including-a-bike-outline]

Eine `.bike`-Datei lässt sich auch in ein anderes Markdown-Dokument einbinden. Siehe [Mindmaps und Gliederungen einbetten](Embedding_Mind_Maps_and_Outlines.html).

Unter {% prefspane Apps %}, bei *Mindmaps/Gliederungen*, gilt **Bike-Gliederungen** für eingebundene Dateien:

- **Ein** (Standard) – ein Mermaid-Diagramm. Der Dateiname ohne `.bike` ist der Stammknoten.
- **Aus** – dieselbe verschachtelte Markdown-Liste wie beim Öffnen der Datei, ohne Dokumenttitel.

Mermaid-Diagramme brauchen MultiMarkdown, CommonMark (GFM) oder Kramdown. Mit dem Discount-Prozessor werden sie nicht gerendert.

[bike]: https://www.hogbaysoftware.com/bike/
