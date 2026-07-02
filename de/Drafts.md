# <%= @title %>

[Drafts][drafts] auf dem Mac kann den aktiven Entwurf mithilfe der **Marked-Streaming-Vorschau** in Marked spiegeln – über denselben Zwischenablage-basierten Kanal, der unter [Streaming Preview](Streaming_Preview.html) beschrieben wird. Sie können den aktuellen Entwurf auch einmalig mit einer Community-**Aktion** senden (ohne Live-Updates, bis Sie die Aktion erneut ausführen).

## Streaming-Vorschau (Drafts für Mac)

1. Wählen Sie in Marked {% appmenu File, New, Streaming Preview %} aus, damit ein Streaming-Vorschaufenster bereit ist.
2. Öffnen Sie in **Drafts für Mac** die **Einstellungen** und aktivieren Sie **Enable Marked App Streaming Preview support**.
3. Verwenden Sie **Open Marked**, wenn Drafts es anbietet, um Marked in den Vordergrund zu holen, und bearbeiten Sie dann in Drafts weiter. Die Vorschau wird aktualisiert, wenn sich Ihr Entwurf ändert.

![][draftsprefs]

Wenn diese Option aktiviert ist, sendet Drafts Markdown über die Integration, die Marked für Streaming-Vorschauen bereitstellt, an Marked (anstatt sich auf die Anzeige einer Datei auf der Festplatte zu verlassen).

### Marked beziehen

Wenn **Get Marked App** im Einstellungsblatt von Drafts angezeigt wird, verwenden Sie es, wenn Marked noch nicht installiert ist.

## Vorschau in Aktion Marked (manuelle Aktualisierung)

Installieren Sie die Community-Aktion [**Preview in Marked**](https://actions.getdrafts.com/a/11f) aus dem Drafts-Verzeichnis. Sie sendet den **aktuellen Entwurfstext** über eine `x-marked://preview?text=…`-URL an Marked (Drafts ersetzt dabei Ihren Entwurfsinhalt). **Inhalte werden nicht live aktualisiert**: Führen Sie die Aktion immer dann erneut aus, wenn Marked den aktuellen Stand des Entwurfs anzeigen soll.

Dieser Ansatz ist praktisch für gelegentliche Überprüfungen, während die **Streaming-Vorschau** für kontinuierliche Schreibsitzungen geeignet ist.

Drafts läuft auch auf iPhone und iPad; die hier dokumentierte Streaming-Vorschau-Integration gilt für **Drafts für Mac** mit Marked auf demselben Mac.

[draftsprefs]: images/Drafts_streaming_preview_preference.png width=842px height=182px class=center

[drafts]: https://getdrafts.com/
