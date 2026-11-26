# <%= @title %>

FerventMind-Mindmaps (`.fvmd`) lassen sich in Marked öffnen. Marked entpackt das Paket und zeigt die `text.md` an, die FerventMind darin gespeichert hat.

## Markdown in der Mindmap [markdown-in-the-map]

Wie dieses Markdown aussieht, legen Sie in FerventMind fest, unter **Settings > Files And Export** in der Gruppe **Markdown**. Marked zeigt die gespeicherte Datei unverändert an.

![FerventMind Files And Export][fm-export]

**Headings** legt fest, wie viele Ebenen als Überschriften erhalten bleiben. **Visible topics only** lässt Themen in eingeklappten Zweigen weg. **Notes** und **Task checkboxes** bestimmen, ob Notizen und Aufgaben in dieses Markdown übernommen werden. Diese Einstellungen gelten für den Markdown-Export, für Copy As und für die Markdown-Kopie, die in jeder Mindmap für Apps wie Marked gespeichert wird. Eine einzelne Mindmap kann sie unter **Definitions • MAP** überschreiben.

Fehlt einer älteren Mindmap die `text.md`, erstellt Marked eine Gliederung aus `map.xml`: Der Titel wird zur Überschrift der Ebene 1, die nächste Ebene zu Überschriften der Ebene 2, und tiefere Themen werden zu verschachtelten Aufzählungspunkten. Notizen werden zum Text des jeweiligen Abschnitts. Eine erledigte Aufgabe erscheint als abgehaktes Kontrollkästchen, eine teilweise erledigte mit ihrem Prozentwert. Als Bilder dienen die Dateien unter `assets/`, ohne Bildunterschrift mit dem Dateinamen.

## Vorschau in Marked [preview-in-marked]

Wählen Sie in FerventMind **View → Preview in Marked**, um eine [Streaming-Vorschau](Streaming_Preview.html) zu öffnen. Marked aktualisiert sie laufend, während Sie arbeiten.

## Eine Mindmap einbinden [including-a-map]

Wenn Sie eine `.fvmd` einbinden, gilt die Option **FerventMind-Dateien** unter **Als Mermaid-Mindmaps einbetten:** in {% prefspane Apps %}. Ist sie aktiviert, erzeugt Marked aus der Mindmap ein Mermaid-Diagramm. Ist sie deaktiviert, bettet Marked die `preview.png` der Mindmap ein. Siehe [Mindmaps und Gliederungen einbetten](Embedding_Mind_Maps_and_Outlines.html).

## Im Editor öffnen [open-in-editor]

**Im Editor öffnen** ({% kbd cmd E %}) startet FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
