# <%= @title %>

Optionen unter {% prefspane General %}:

![Einstellungen: Allgemein][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Fenster [window]

Neue Fenster im Vordergrund halten
: Stellt neue Fenster automatisch so ein, dass sie über anderen Anwendungen schweben.

Fenster bei Aktualisierung öffnen
: Wird in einer überwachten Datei eine Änderung erkannt, hebt sich das Vorschaufenster dieses Dokuments über die anderen Fenster auf Ihrem Schreibtisch, ohne Marked zu aktivieren.

Im Hintergrund durchscheinend
: Blendet das Fenster ab, wenn es nicht fokussiert ist. Stellen Sie die Deckkraft mit dem Schieberegler ein.

Speicherintensive Funktionen bei großen Dokumenten deaktivieren
: Deaktiviert bei Dokumenten über 100 KB einige prozessorintensive Funktionen wie einklappbare Überschriften.

Neue Dokumente geöffnet in
: Wählen Sie **Fenster**, **Tabs** oder **Automatisch** (folgt der macOS-Systemeinstellung für Tabs). Bei Tabs navigieren Sie mit {% kbd cmd shift [/] %} und dem [Schnell-öffnen-Bedienfeld](Quick_Open.html).

Aktualisiertes Dokument nach vorne bringen
: Wird eine Vorschau aktualisiert, wird ihr Tab ausgewählt oder ihr Fenster nach vorne geholt – **aber nur innerhalb von Marked**. Ist eine andere Anwendung im Vordergrund (z. B. Ihr Texteditor), bleibt Marked im Hintergrund; der richtige Tab ist ausgewählt, sodass er bereitsteht, wenn Sie zu Marked zurückwechseln. Um die Vorschau über alle Anwendungen zu heben, ohne Marked zu aktivieren, verwenden Sie stattdessen **Fenster bei Aktualisierung öffnen**.

Den Fokus wieder auf die vorherige App richten
: Führt eine Aktion beim Anheben oder Nach-vorne-holen dazu, dass Marked in den Vordergrund tritt, wird der Tastaturfokus bei aktivierter Option an die App zurückgegeben, die vor der Aktualisierung vorne war (etwa Ihr Texteditor). Ist die Option deaktiviert, nimmt Marked diese Fokusübergabe nie vor. Tritt Marked nicht in den Vordergrund, hat die Option keine Wirkung.

### Statusleiste [status-bar]

Stilauswahl anzeigen
: Zeigt die Stilauswahl in der unteren Leiste des Vorschaufensters an.

Wortanzahl anzeigen
: Zeigt die Wortanzahl (und die Statistik-Schaltfläche) in der unteren Leiste des Vorschaufensters an.

Die Anzahl der Wörter schließt Folgendes aus
: Bei der Berechnung der Wortanzahl lässt sich jede beliebige Kombination aus Folgendem ignorieren:

- **Fußnoten/Zitate**
- **Blockzitate**
- **Eingerückte Codeblöcke** (mit Backticks abgegrenzte Codeblöcke werden immer ausgeschlossen)
- **Bildunterschriften**

### Tastenkürzel [shortcuts]

Klicken Sie auf das Kurzbefehl-Feld, um eine Tastenkombination aufzuzeichnen, die eine Aktion auslöst:

Marked aktivieren
: Wechselt zu Marked, wenn diese Tastenkombination in einer beliebigen Anwendung gedrückt wird.

Erstes Fenster öffnen
: Holt das vorderste (zuletzt aktive) Marked-Vorschaufenster in den Vordergrund, ohne die aktuelle Anwendung zu verlassen.

Aktionspalette öffnen
: Öffnet die Befehlspalette der [Schnellaktionen](Quick_Actions.html), während Marked aktiv ist. Dieser Kurzbefehl gilt für {% appmenu Ablage, Schnellaktionen… %} und funktioniert nur innerhalb von Marked (nicht aus anderen Anwendungen).

Warnungen zurücksetzen
: Stellt alle Warndialoge wieder her, die Sie zuvor ausgeblendet haben, sodass sie erneut erscheinen können.
