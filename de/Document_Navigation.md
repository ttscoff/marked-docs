# <%= @title %>

Auf dieser Seite wird beschrieben, wie Sie sich in langen Vorschauen bewegen: [Table of Contents](#table-of-contents), [fast search](#fast-search), [bookmarks](#bookmarks-and-mini-map) und [Mini Map](#minimap). Informationen zu Bildlaufverknüpfungen, die überall gelten (z. B. {% kbd j %}/{% kbd k %}), finden Sie unter [Keyboard Navigation](Interface_Features.html#keyboardnavigation) unter [Interface Features](Interface_Features.html).

## Inhaltsverzeichnis

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

Wenn Ihr Dokument Kopfzeilen enthält, wird in der Symbolleiste eine Listenschaltfläche angezeigt. Klicken Sie darauf, um das Inhaltsverzeichnis zu erweitern. Klicken Sie auf eine Überschrift, um zu diesem Abschnitt der Vorschau zu springen. Verwenden Sie {% kbd j %}/{% kbd k %} (nach unten/oben), um durch die Liste zu navigieren, und {% kbd Enter %} oder {% kbd o %}, um zur hervorgehobenen Überschrift zu springen.

**Filterleiste:** Drücken Sie bei geöffnetem Inhaltsverzeichnis {% kbd Space %} (Leertaste), um das Eingabefeld zu öffnen. Geben Sie einen beliebigen Teil eines Überschriftennamens ein (Marked verwendet den TextMate-Stil-Abgleich – Sie können beispielsweise den ersten Buchstaben jedes Wortes eingeben) und drücken Sie die Tabulatortaste ({% kbd ⇥ %}) oder den Abwärtspfeil ({% kbd ↓ %}), um durch die gefilterte Liste zu navigieren.

Durch Drücken von {% kbd cmd T %} wird auch das Inhaltsverzeichnis geöffnet (oder geschlossen).

Wenn ["Headlines Collapse Sections"](Interface_Features.html#collapsibleheadlines) im {% prefspane General %} aktiviert ist, wird dieser Abschnitt durch Gedrückthalten der Befehlstaste beim Klicken auf ein Element im Inhaltsverzeichnis ein- oder ausgeblendet und bei Bedarf übergeordnete Abschnitte angezeigt.

Im Vollbildmodus erscheint das Inhaltsverzeichnis als feste Seitenleiste und nicht als Popup-Menü. Um dieses Layout in einer normalen Fenstervorschau zu verwenden, verwenden Sie den Vollbildschalter unten rechts im Inhaltsverzeichnisfenster.

![Toggle Full Screen][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


Eine komprimierte Liste der Schlüssel finden Sie unter [Keyboard Shortcuts](Keyboard_Shortcuts.html#TableofContentsNavigation).

Siehe auch [Document Navigation video on YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Vollbildmodus für das Inhaltsverzeichnis

Wenn ein Marked-Vorschaufenster im Vollbildmodus angezeigt wird, kann das Inhaltsverzeichnis zur kontinuierlichen Navigation auf der linken Seite fixiert bleiben. Es wechselt immer noch mit {% kbd cmd T %}; Wenn Sie in diesem Layout außerhalb des Inhaltsverzeichnisses klicken, wird es oft nicht geschlossen.

Klicken Sie in einem normalen Fenster auf das Symbol unten im Inhaltsverzeichnisfenster, um es als Seitenleiste anzudocken. Klicken Sie auf das Symbol oben in der Seitenleiste, um in den Popup-Modus zurückzukehren.

### Customisieren, wo das Inhaltsverzeichnis erscheint

Das Inhaltsverzeichnis kann mit [special syntax](Special_Syntax.html#tocplacement) `<!--TOC-->` in das exportierte Dokument eingefügt werden.

Fügen Sie `max#` hinzu (zum Beispiel `<!--TOC max2-->`), um die Anzahl der angezeigten Überschriftenebenen zu begrenzen.

## Schnelle Suche

**Schnelle Navigation** kombiniert das Inhaltsverzeichnis mit dem Filterfokus, sodass Sie mit minimalem Tippaufwand springen können:

- Drücken Sie {% kbd f %} in der Vorschau, um das Inhaltsverzeichnis mit dem **fokussierten Filterfeld** zu öffnen (dieselbe Idee wie das Öffnen des Inhaltsverzeichnisses und das anschließende Drücken von {% kbd Space %}, ohne den zusätzlichen Schritt).
- Geben Sie einen Teil eines beliebigen Überschriftentitels ein. Die Liste filtert nach Übereinstimmungen.
- Wenn nur noch eine Überschrift übrig ist, springen Sie durch Drücken der Eingabetaste ({% kbd ↩ %}) direkt dorthin.
- Wenn noch mehrere Überschriften vorhanden sind, drücken Sie die Tabulatortaste ({% kbd ⇥ %}), um das Filterfeld zu verlassen, bewegen Sie sich mit {% kbd j %}/{% kbd k %} oder den Pfeiltasten und drücken Sie dann {% kbd o %} oder Return ({% kbd ↩ %}), um zur Überschrift zu gelangen und das Inhaltsverzeichnis zu schließen.
- Mit der Tabulatortaste kehrt der Fokus erneut zum Suchfeld zurück.

> **Kurzbefehl-Erinnerung:** Wenn Sie das Inhaltsverzeichnis öffnen und {% kbd Space %} drücken, wird die Filterleiste geöffnet – praktisch, wenn das Inhaltsverzeichnis bereits sichtbar ist.

(In früheren Dokumenten wurde dies als „Fast Switcher“ bezeichnet; es handelt sich um dieselbe Funktion.)

## Lesezeichen und Minikarte {#bookmarks-and-mini-map}

Verwenden Sie das Vorschaumenü {% appmenu {{gear}} %} und {% kbd Tab %} ({% kbd ⇥ %}), um das Dokument neben [search](Interface_Features.html#search) zu fokussieren, um beim Überfliegen Lesezeichen zu platzieren und erneut aufzurufen.

### Lesezeichen setzen

Setzen Sie Lesezeichen an der Scrollposition mit {% kbd shift 1 %}--{% kbd shift 9 %} und springen Sie mit {% kbd 1 %}--{% kbd 9 %} zurück. Verwenden Sie {% kbd n %} und {% kbd p %} für das nächste/vorherige in der **Dokumentenreihenfolge**; {% kbd shift n %} und {% kbd shift p %} für nächstes/vorheriges in **numerischer** Reihenfolge.

Durch Ändern des Stils oder der Seitengröße kann ein Lesezeichen an die Stelle verschoben werden, an der es angezeigt wird. Lesezeichen sind als vorübergehende Überprüfungshilfen gedacht: Sie bleiben nicht zwischen Dokumentsitzungen bestehen, überdauern jedoch Aktualisierungen und Bearbeitungen der Vorschau.

**Lesezeichen für Schlagzeilen:** Halten Sie die Wahltaste gedrückt und drücken Sie {% kbd opt 1 %}--{% kbd opt 9 %}, um die Schlagzeile, die am oberen Rand des Ansichtsfensters liegt (oder die letzte Schlagzeile vor dem oberen Rand), mit einem Lesezeichen zu versehen.

**Nächster freier Slot:** {% kbd cmd D %} (oder Backtick {% kbd \`\` %} für Vim-Benutzer) fügt ein Lesezeichen im nächsten verfügbaren nummerierten Slot hinzu.

Drücken Sie {% kbd 0 %}, um die Lesezeichenleiste zu erweitern (Überschriftentitel, sofern verfügbar). Wenn [Mini Map](#minimap) aktiviert ist, wird es gleichzeitig von {% kbd 0 %} angezeigt. Drücken Sie Escape oder {% kbd 0 %} erneut, um zu reduzieren.

Drücken Sie {% kbd x %} zweimal ({% kbd xx %}), um alle Lesezeichen zu löschen.

Es gibt [more preview shortcuts](Keyboard_Shortcuts.html); Drücken Sie {% kbd h %} in der Vorschau für eine Heads-up-Liste oder {% kbd opt cmd K %} für die vollständige Referenz.

### Minikarte {#minimap}

Wenn die Minikarte in den {% prefspane Preview %}-Einstellungen aktiviert ist, öffnet {% kbd 0 %} eine skalierte Miniaturansicht des gesamten Dokuments entlang der Lesezeichenleiste. Klicken Sie irgendwo auf die Karte, um dort zur vollständigen Vorschau zu scrollen. Gespeicherte Lesezeichen werden als horizontale Linien mit Zahlen (und ggf. Überschriften) angezeigt.

Halten Sie die **Befehlstaste** gedrückt und bewegen Sie sich über die Minikarte, um eine vergrößerte Lupe zu erhalten. Halten Sie die **Option** gedrückt und ziehen Sie zum Scrollen, als würden Sie die Bildlaufleiste ziehen.

Die Karte wird neu generiert, wenn sich die Fenstergröße oder das Layout ändert. Bei sehr langen Dokumenten kann das einmalige Drücken von {% kbd 0 %} einen Moment dauern; Marked verhindert, dass die Minikarte beim ersten Laden automatisch erstellt wird, bis Sie sie anfordern.

Drücken Sie {% kbd 0 %} oder Escape, um die Minikarte zu schließen.

**Leistungshinweis:** Beim Generieren der Karte kann die Vorschau bei großen Dokumenten kurz angehalten werden; Dies wird nur ausgeführt, wenn die Karte sichtbar ist oder nach einer Größenänderung.

### Zoom-Übersicht (verwandt)

Eine Übersicht über den Textmaßstab ohne Minikarte finden Sie unter [Zoom Overview](Zoom_Overview.html) ({% kbd z %}).