# <%= @title %>

Ziehen Sie eine [Bike][bike]-Gliederung auf Marked, um sie als verschachtelte Markdown-Liste in der Vorschau zu sehen. Überschriftszeilen erscheinen fett, Aufgaben als Kontrollkästchen. Eine einzelne Gliederung ist eine `.bike`-Datei. Bike 2 speichert ein `.biked`-Paket, wenn die Gliederung eingebettete Bilder enthält.

## Eine Bike-Gliederung öffnen [opening-a-bike-outline]

Marked wandelt die Gliederung um, wenn Sie die Datei öffnen:

- Als Überschrift markierte Zeilen werden zu **fett** gesetzten Listeneinträgen.
- Aufgaben werden zu Kontrollkästchen im GitHub-Stil. Eine Aufgabe ist abgehakt, wenn Bike einen Abschlusszeitpunkt speichert oder sie als erledigt markiert.
- Links und Inline-Formatierung im Zeilentext bleiben als Markdown erhalten.

Beim Öffnen einer `.bike`-Datei entsteht immer diese Liste, nie ein Mermaid-Diagramm. Ein `.biked`-Paket folgt der unten beschriebenen Einstellung **Bike-Glieder⁠ungen**.

## Eine Bike-Gliederung einbinden [including-a-bike-outline]

Eine `.bike`-Datei lässt sich auch in ein anderes Markdown-Dokument einbinden. Siehe [Mindmaps und Gliederungen einbetten](Embedding_Mind_Maps_and_Outlines.html).

Die Option **Bike-Glieder⁠ungen** unter {% prefspane Apps %} im Abschnitt *Mind⁠maps und Glieder⁠ungen* gilt für eingebundene Dateien:

- **Ein** (Standard) – ein Mermaid-Diagramm. Der Dateiname ohne `.bike` ist der Stammknoten.
- **Aus** – dieselbe verschachtelte Markdown-Liste wie beim Öffnen der Datei, ohne Dokumenttitel.

## Gliederungen mit Bildern [outlines-with-images]

Bike 2 speichert ein `.biked`-Paket, wenn die Gliederung eingebettete Bilder enthält. Das Paket ist ein TextBundle: `text.bike` und ein Ordner `assets`. Öffnen Sie die `.biked`-Datei selbst. Marked liest die enthaltene Gliederung und verwendet den Paketnamen als Fenstertitel.

Schalten Sie **Bike-Glieder⁠ungen** aus, um das Paket als verschachtelte Liste mit den eingebetteten Bildern zu sehen. **Ein** macht aus der Gliederung ein Mermaid-Diagramm.

[bike]: https://www.hogbaysoftware.com/bike/
