# <%= @title %>

Ziehen Sie eine [Bike][bike]-Gliederung (`.bike`) auf Marked, um sie als verschachtelte Markdown-Liste in der Vorschau zu sehen. Überschriftszeilen erscheinen fett, Aufgaben als Kontrollkästchen.

## Eine Bike-Gliederung öffnen [opening-a-bike-outline]

Marked wandelt die Gliederung um, wenn Sie die Datei öffnen:

- Als Überschrift markierte Zeilen werden zu **fett** gesetzten Listeneinträgen.
- Aufgaben werden zu Kontrollkästchen im GitHub-Stil. Eine Aufgabe ist abgehakt, wenn Bike einen Abschlusszeitpunkt speichert oder sie als erledigt markiert.
- Links und Inline-Formatierung im Zeilentext bleiben als Markdown erhalten.

Beim Öffnen einer `.bike`-Datei entsteht immer diese Liste, nie ein Mermaid-Diagramm.

## Eine Bike-Gliederung einbinden [including-a-bike-outline]

Eine `.bike`-Datei lässt sich auch in ein anderes Markdown-Dokument einbinden. Siehe [Mindmaps und Gliederungen einbetten](Embedding_Mind_Maps_and_Outlines.html).

Die Option **Bike-Gliederungen** unter {% prefspane Apps %} im Abschnitt *Mindmaps und Gliederungen* gilt für eingebundene Dateien:

- **Ein** (Standard) – ein Mermaid-Diagramm. Der Dateiname ohne `.bike` ist der Stammknoten.
- **Aus** – dieselbe verschachtelte Markdown-Liste wie beim Öffnen der Datei, ohne Dokumenttitel.

[bike]: https://www.hogbaysoftware.com/bike/
