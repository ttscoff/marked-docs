# <%= @title %>

I> Auf dieser Seite geht es um die *Darstellung* der Vorschau – Stile, Zoom, Dunkelmodus und die Statusleiste. Informationen zum Einrichten der Live-Vorschau in Ihrem Editor finden Sie unter [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html).

Ändern Sie, wie Sie Dinge sehen.

## Einen Stil auswählen [choosing-a-style]

![][1]

   [1]: images/StylePicker.jpg @2x width=896px height=195px class=center

Unter {% prefspane Style %} legen Sie einen Standardstil für neue Dokumente fest. Wenn Sie das Stilmenü in der Symbolleiste in den Fenstereinstellungen aktiviert haben, können Sie den Stil direkt im Vorschaufenster für jedes Dokument anpassen. Ihre Stilauswahl wird gespeichert und ist die erste Wahl für Export- und Druckoptionen.

Eigene Stile, die in den Stileinstellungen hinzugefügt wurden, sind in beiden Menüs verfügbar.

Stile lassen sich mit Tastaturkurzbefehlen auswählen. Öffnen Sie das Stilmenü, um den Tastaturkurzbefehl für jeden Stil zu sehen. Die Kurzbefehle werden in der Reihenfolge der Stile vergeben: Die ersten 9 Stile in der Liste erreichen Sie mit {% kbd cmd 1 %} – {% kbd cmd 9 %}, die nächsten 10 mit {% kbd cmd opt 1 %} – {% kbd cmd opt 0 %} usw.

## Gliederungsmodus [outline-mode]

Wenn es sich bei Ihrem Dokument um eine hierarchische Liste handelt, die beispielsweise aus einer Mindmap- oder Gliederungsanwendung generiert wurde, können Sie den Gliederungsmodus im Zahnradmenü aktivieren, um eine spezielle Formatierung im APA- oder Dezimal-Gliederungsstil anzuwenden.

Der automatische Gliederungsmodus kann für bestimmte Dateierweiterungen unter {% prefspane Style %} aktiviert werden.

## Textzoom [text-zoom]

![][2]

   [2]: images/textzoom.jpg @2x width=800px height=414px class=center

Sie können die Textgröße mit {% kbd cmd shift + %} und {% kbd cmd shift - %} ändern oder das Zoom-Menü unter Vorschau in der Menüleiste bzw. im Zahnradmenü des Dokumentfensters verwenden. Marked merkt sich Ihre Änderungen für das nächste Mal (und die Zukunft). Mit {% kbd cmd 0 %} setzen Sie den Zoom auf 100 % zurück (oder über **Zoom zurücksetzen** im Zoom-Menü).

## Dunkelmodus/Hoher Kontrast [dark-modehigh-contrast]

Wenn Sie hellen Text auf dunklem Hintergrund bevorzugen, ist Marked genau das Richtige für Sie. Im Menü **Vorschau** kehren Sie mit {% appmenu Vorschau, Dunkelmodus ({{opt}}{{cmd}}I) %} die Farben eines der Standardschemata um und erhalten ein Hell-auf-Dunkel-Ergebnis; und wenn ein eigener Stil [richtig aufgebaut](Writing_Custom_CSS.html) ist, funktioniert das auch dort.

## Statusleiste ein-/ausblenden [showhide-status-bar]

Die Statusleiste am unteren Rand des Vorschaufensters lässt sich über den Menüpunkt {% appmenu Vorschau, Statusleiste anzeigen ({{ctrl}}/) %} umschalten. Ist sie ausgeblendet, können Sie sie einblenden und bedienen, indem Sie mit dem Mauszeiger über den Bereich am unteren Rand der Vorschau fahren.
