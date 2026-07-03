# <%= @title %>

Marked enthält Browsererweiterungen, mit denen Sie Seiten-URLs oder ausgewählte Inhalte direkt an Marked 3 senden können.

## Installieren

Von [https://markedapp.com/extensions](https://markedapp.com/extensions) herunterladen und installieren:

- Firefox / Zen
- Chrome / Brave / Edge
- Safari (mitgeliefert)

## So funktioniert die Erweiterung

Wenn Sie auf eine Erweiterungsschaltfläche klicken, wird eine benutzerdefinierte URL geöffnet, die Marked 3 über das Schema `x-marked-3://markdownify` verarbeitet.

### `Markdownify URL`

Klicken Sie im Erweiterungs-Popup auf **`Markdownify URL`**, um die aktuelle Seiten-URL an Marked zu senden.

### `Markdownify Selection`

Klicken Sie im Erweiterungs-Popup auf **`Markdownify Selection`**, wenn Sie auf der Seite etwas ausgewählt haben.

Marked empfängt das HTML der aktuellen Auswahl und wandelt es in Markdown um.

### Select Section (Blockauswahlmodus)

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

Klicken Sie auf **Select Section**, um in den „Abschnittsauswahlmodus“ zu gelangen:

- Bewegen Sie den Mauszeiger über die Seite, um Blockelemente hervorzuheben, die Sie auswählen können.
- Klicken Sie auf einen Block, um ihn sofort an Marked zu senden (einmaliges Senden).
- Klicken Sie bei gedrückter Befehlstaste auf Blöcke, um mehrere Blöcke auszuwählen (erneut bei gedrückter Befehlstaste klicken, um einen Block wieder zu entfernen).
- Drücken Sie die Eingabetaste, um die aktuell ausgewählten Blöcke zu senden.
- Drücken Sie Esc, um den Abschnittsauswahlmodus abzubrechen.

Während der Auswahl bietet das Popup außerdem eine Zoom-Steuerung, die Ihnen das Klicken auf kleine oder dichte Abschnitte erleichtert:

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` verkleinert
- **Fit Height** zoomt so, dass die Seite in die Höhe des Ansichtsfensters passt
- `+` vergrößert
