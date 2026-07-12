# <%= @title %>

### Debug-Modus

Sie können die Debug-Protokollierung aktivieren, indem Sie {% prefspane Advanced %} öffnen und das Kontrollkästchen **Debug-Modus** unten im Bereich aktivieren. Daraufhin wird ein Dropdown-Menü angezeigt, in dem Sie die Protokollierungsstufe festlegen können, die Sie sehen möchten:

- **Nur Fehler**: Es werden nur schwerwiegende Fehler protokolliert
- **Fehler und Warnungen**: Zusätzlich weniger dringende Warnungen anzeigen
- **Alle**: Zeigt Fehler, Warnungen und Debug-Meldungen auf Informationsebene an. Dies ist die empfohlene Einstellung zur Fehlerbehebung.

{% note %}
TODO: Funktioniert das noch?
Sie können auf diese Optionen auch zugreifen, indem Sie beim Öffnen von {% appmenu Hilfe %} in der Menüleiste die Taste {% kbd opt  %} gedrückt halten.
{% endnote %}

### Anzeigen des Protokolls

Wenn der **Debug-Modus** aktiviert ist, können Sie das Menü {% appmenu Hilfe %} öffnen und Debug-Protokoll öffnen auswählen. Dadurch wird das Protokoll von Marked in Console.app geöffnet, das live aktualisiert wird, wenn während der Verwendung von Marked Protokollmeldungen hinzugefügt werden.

### Fehlerbehebung Custom Regeln

[Custom preprocessors and processors](Custom_Processor.html) erhalten eine eigene Protokollschnittstelle. Wählen Sie {% appmenu Hilfe, Protokoll eigener Regeln anzeigen %}, um das Fenster zu öffnen. In diesem Fenster wird ein farbiges Protokoll angezeigt, das zeigt, welche Regeln übereinstimmten und welche Befehle sie ausführten.

### Ein Problem melden

Verwenden Sie {% appmenu Hilfe, Problem melden %}, um ein Fenster zu öffnen, das Ihre Einstellungen für die gängigsten Schlüssel und eine Vorlage zum Erstellen eines Fehlerberichts anzeigt. Verwenden Sie die Schaltfläche „In die Zwischenablage kopieren“, um den Inhalt des Fensters zu kopieren, und klicken Sie auf „Support-Site öffnen“, um [the new-question form](https://support.markedapp.com/questions/add) zu öffnen, wo Sie Ihren Bericht einfügen können. Ich versuche, innerhalb von 48 Stunden auf Meldungen zu antworten.