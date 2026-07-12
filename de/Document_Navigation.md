# <%= @title %>

Auf dieser Seite wird beschrieben, wie Sie sich in langen Vorschauen bewegen: über das [Inhaltsverzeichnis](#table-of-contents), die [schnelle Suche](#fast-search), [Lesezeichen](#bookmarks-and-mini-map) und die [Mini-Übersicht](#minimap). Informationen zu Tastaturkurzbefehlen für den Bildlauf, die überall gelten (z. B. {% kbd j %}/{% kbd k %}), finden Sie unter [Tastaturnavigation](Interface_Features.html#keyboardnavigation) auf der Seite [Oberflächenfunktionen](Interface_Features.html).

## Inhaltsverzeichnis

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Wenn Ihr Dokument Überschriften enthält, wird in der Symbolleiste eine Listenschaltfläche angezeigt. Klicken Sie darauf, um das Inhaltsverzeichnis aufzuklappen. Klicken Sie auf eine Überschrift, um zu diesem Abschnitt der Vorschau zu springen. Verwenden Sie {% kbd j %}/{% kbd k %} (nach unten/oben), um durch die Liste zu navigieren, und {% kbd Enter %} oder {% kbd o %}, um zur hervorgehobenen Überschrift zu springen.

**Filterleiste:** Drücken Sie bei geöffnetem Inhaltsverzeichnis {% kbd Space %} (Leertaste), um das Eingabefeld zu öffnen. Geben Sie einen beliebigen Teil eines Überschriftennamens ein (Marked verwendet Abgleich im TextMate-Stil – Sie können beispielsweise den ersten Buchstaben jedes Wortes eingeben) und drücken Sie die Tabulatortaste ({% kbd ⇥ %}) oder den Abwärtspfeil ({% kbd ↓ %}), um durch die gefilterte Liste zu navigieren.

Durch Drücken von {% kbd cmd T %} wird das Inhaltsverzeichnis ebenfalls geöffnet (oder geschlossen).

Wenn [„Abschnitte über Überschriften einklappen“](Interface_Features.html#collapsibleheadlines) unter {% prefspane General %} aktiviert ist, wird durch Klicken bei gedrückter Befehlstaste auf einen Eintrag im Inhaltsverzeichnis der betreffende Abschnitt ein- oder ausgeklappt; übergeordnete Abschnitte werden bei Bedarf eingeblendet.

Im Vollbildmodus erscheint das Inhaltsverzeichnis als feste Seitenleiste und nicht als Popup-Menü. Um dieses Layout in einer normalen Fenstervorschau zu verwenden, nutzen Sie den Vollbildschalter unten rechts im Inhaltsverzeichnisfenster.

![Vollbild umschalten][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Eine kompakte Übersicht der Tasten finden Sie unter [Tastaturkurzbefehle](Keyboard_Shortcuts.html#TableofContentsNavigation).

Siehe auch das [Video zur Dokumentnavigation auf YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Vollbildmodus für das Inhaltsverzeichnis

Wenn ein Marked-Vorschaufenster im Vollbildmodus angezeigt wird, kann das Inhaltsverzeichnis zur ständigen Navigation links fixiert bleiben. Es lässt sich weiterhin mit {% kbd cmd T %} ein- und ausblenden; wenn Sie in diesem Layout außerhalb des Inhaltsverzeichnisses klicken, wird es oft nicht geschlossen.

Klicken Sie in einem normalen Fenster auf das Symbol unten im Inhaltsverzeichnisfenster, um es als Seitenleiste anzudocken. Klicken Sie auf das Symbol oben in der Seitenleiste, um zum Popup-Modus zurückzukehren.

### Anpassen, wo das Inhaltsverzeichnis erscheint

Das Inhaltsverzeichnis kann mit der [speziellen Syntax](Special_Syntax.html#tocplacement) `<!--TOC-->` in das exportierte Dokument eingefügt werden.

Fügen Sie `max#` hinzu (zum Beispiel `<!--TOC max2-->`), um die Anzahl der angezeigten Überschriftenebenen zu begrenzen.

## Schnelle Suche

**Schnelle Navigation** kombiniert das Inhaltsverzeichnis mit fokussiertem Filter, sodass Sie mit minimalem Tippaufwand springen können:

- Drücken Sie {% kbd f %} in der Vorschau, um das Inhaltsverzeichnis mit **fokussiertem Filterfeld** zu öffnen (derselbe Gedanke wie das Öffnen des Inhaltsverzeichnisses und anschließendes Drücken von {% kbd Space %}, nur ohne den zusätzlichen Schritt).
- Geben Sie einen Teil eines beliebigen Überschriftentitels ein; die Liste filtert auf Übereinstimmungen.
- Bleibt nur eine Überschrift übrig, springen Sie mit der Eingabetaste ({% kbd ↩ %}) direkt dorthin.
- Sind noch mehrere Überschriften übrig, drücken Sie die Tabulatortaste ({% kbd ⇥ %}), um das Filterfeld zu verlassen, bewegen Sie sich mit {% kbd j %}/{% kbd k %} oder den Pfeiltasten und drücken Sie dann {% kbd o %} oder die Eingabetaste ({% kbd ↩ %}), um zur Überschrift zu springen und das Inhaltsverzeichnis zu schließen.
- Mit der Tabulatortaste kehrt der Fokus wieder zum Suchfeld zurück.

> **Zur Erinnerung:** Wenn Sie das Inhaltsverzeichnis öffnen und {% kbd Space %} drücken, öffnet sich die Filterleiste – praktisch, wenn das Inhaltsverzeichnis bereits sichtbar ist.

(In früherer Dokumentation wurde dies als „Fast Switcher“ bezeichnet; es handelt sich um dieselbe Funktion.)

## Lesezeichen und Mini-Übersicht {#bookmarks-and-mini-map}

Verwenden Sie das Vorschaumenü {% appmenu Gear %} und {% kbd Tab %} ({% kbd ⇥ %}) zum Fokussieren des Dokuments neben der [Suche](Interface_Features.html#search), um beim Überfliegen Lesezeichen zu setzen und erneut aufzurufen.

### Lesezeichen setzen

Setzen Sie Lesezeichen an der Scrollposition mit {% kbd shift 1 %}–{% kbd shift 9 %} und springen Sie mit {% kbd 1 %}–{% kbd 9 %} zurück. Verwenden Sie {% kbd n %} und {% kbd p %} für das nächste/vorherige Lesezeichen in **Dokumentreihenfolge**; {% kbd shift n %} und {% kbd shift p %} für das nächste/vorherige in **numerischer** Reihenfolge.

Durch Ändern des Stils oder der Seitengröße kann sich die Position verschieben, an der ein Lesezeichen erscheint. Lesezeichen sind als vorübergehende Hilfen beim Durchsehen gedacht: Sie bleiben nicht zwischen Dokumentsitzungen bestehen, überdauern jedoch Aktualisierungen und Bearbeitungen der Vorschau.

**Lesezeichen für Überschriften:** Halten Sie die Wahltaste gedrückt und drücken Sie {% kbd opt 1 %}–{% kbd opt 9 %}, um die Überschrift, die dem oberen Rand des Sichtbereichs am nächsten liegt (oder die letzte Überschrift davor), mit einem Lesezeichen zu versehen.

**Nächster freier Platz:** {% kbd cmd D %} (oder das Backtick-Zeichen {% kbd \`\` %} für Vim-Benutzer) fügt ein Lesezeichen im nächsten verfügbaren nummerierten Platz hinzu.

Drücken Sie {% kbd 0 %}, um die Lesezeichenleiste aufzuklappen (mit Überschriftentiteln, sofern verfügbar). Wenn die [Mini-Übersicht](#minimap) aktiviert ist, wird sie durch {% kbd 0 %} gleichzeitig angezeigt. Drücken Sie Escape oder erneut {% kbd 0 %}, um die Leiste wieder einzuklappen.

Drücken Sie zweimal {% kbd x %} ({% kbd xx %}), um alle Lesezeichen zu löschen.

Es gibt [weitere Tastaturkurzbefehle für die Vorschau](Keyboard_Shortcuts.html); drücken Sie {% kbd h %} in der Vorschau für eine Schnellübersicht oder {% kbd opt cmd K %} für die vollständige Referenz.

### Mini-Übersicht {#minimap}

Wenn die Mini-Übersicht unter {% prefspane Preview %} aktiviert ist, öffnet {% kbd 0 %} eine skalierte Miniaturansicht des gesamten Dokuments entlang der Lesezeichenleiste. Klicken Sie auf eine beliebige Stelle der Übersicht, um die vollständige Vorschau dorthin zu scrollen. Gespeicherte Lesezeichen erscheinen als horizontale Linien mit Nummern (und ggf. Überschriften).

Halten Sie die **Befehlstaste** gedrückt und bewegen Sie den Zeiger über die Mini-Übersicht, um eine vergrößerte Lupe zu erhalten. Halten Sie die **Wahltaste** gedrückt und ziehen Sie, um zu scrollen – so, als würden Sie die Bildlaufleiste ziehen.

Die Übersicht wird neu generiert, wenn sich die Fenstergröße oder das Layout ändert. Bei sehr langen Dokumenten kann das erste Drücken von {% kbd 0 %} einen Moment dauern; Marked erstellt die Mini-Übersicht beim ersten Laden nicht automatisch, sondern erst, wenn Sie sie anfordern.

Drücken Sie {% kbd 0 %} oder Escape, um die Mini-Übersicht zu schließen.

**Leistungshinweis:** Das Generieren der Übersicht kann die Vorschau bei sehr großen Dokumenten kurz anhalten; dies geschieht nur, wenn die Übersicht sichtbar ist, oder nach einer Größenänderung.

### Zoom-Übersicht (verwandt)

Eine Übersicht im Textmaßstab ohne die Mini-Übersicht finden Sie unter [Zoom-Übersicht](Zoom_Overview.html) ({% kbd z %}).
