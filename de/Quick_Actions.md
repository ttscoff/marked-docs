# <%= @title %>

Die Schnellaktionspalette ist ein durchsuchbarer Befehlsstarter für Marked. Sie sammelt Aktionen aus der Hauptmenüleiste und dem **Zahnradmenü** der Vorschau, dazu reine Vorschaubefehle, die in keinem Menü auftauchen (etwa **Automatisches Scrollen**). Nutzen Sie sie, wenn Sie wissen, was Sie tun möchten, sich aber nicht erinnern, in welchem Menü es steckt.

## Die Schnellaktionspalette öffnen

Öffnen Sie die Palette mit {% kbd shift cmd P %} oder über {% appmenu Ablage, Schnellaktionen… %}. Das Panel erscheint als schwebendes Fenster über Ihrem aktuellen Dokument.

Mit derselben Tastenkombination oder mit **Escape** schließen Sie die Palette wieder. Ist die Palette bereits offen, schließt auch die Auswahl von **Schnellaktionen…** im Menü sie.

## Den Tastaturkurzbefehl anpassen

Der Standard-Tastaturkurzbefehl ist {% kbd shift cmd P %}. Um ihn zu ändern, öffnen Sie {% prefspane General %} und legen unter **Aktionspalette öffnen** im Abschnitt **Verknüpfungen** eine neue Tastenkombination fest.

Anders als **Marked aktivieren** und **Erstes Fenster öffnen** funktioniert dieser Tastaturkurzbefehl nur, wenn Marked die aktive Anwendung ist. Er aktualisiert den im Menü {% appmenu Ablage, Schnellaktionen… %} angezeigten Tastaturkurzbefehl passend zu Ihrer Einstellung.

## Suchen und filtern

Tippen Sie oben im Panel in das Suchfeld, um Befehle in Echtzeit zu filtern. Der Abgleich ist unscharf und nachsichtig:

- Die Wortreihenfolge spielt keine Rolle (`umschalten quelltext` findet **Quelltextansicht umschalten**)
- Anfangsbuchstaben funktionieren gut (`db` findet **Dokument befragen**)
- Auch ohne Leerzeichen wird gefunden (`autoscr` findet **Automatisches Scrollen**)

Jedes Ergebnis zeigt links den Befehlsnamen und rechts in Grau den zugehörigen Tastaturkurzbefehl (sofern vorhanden). Manche Befehle zeigen zusätzlich einen Breadcrumb-Pfad (z. B. `Vorschau › Automatisches Scrollen`), wenn die Aktion aus einem Untermenü oder der Vorschau-Engine stammt.

## Was in der Liste erscheint

Die Palette enthält:

- **Menübefehle** aus der Hauptmenüleiste, einschließlich dynamischer Menüs wie **Stil**, **Verlauf** und offener **Fenster**-Tabs
- **Zahnradmenü**-Befehle aus dem Vorschaufenster
- **Vorschau-Tastaturkurzbefehle** aus der internen Tastaturbelegung (dieselben Befehle wie im Hilfe-HUD der Vorschau), darunter Navigation, automatisches Scrollen, Lesezeichen, Suche und weitere reine Vorschauaktionen

Erscheint derselbe Befehl an mehreren Stellen, zeigt Marked den kürzesten Menüpfad und führt die Angaben zu den Tastaturkurzbefehlen aus den Duplikaten zusammen.

## Tastaturnavigation

Navigieren Sie in der Schnellaktionspalette vollständig über die Tastatur:

- **Pfeiltasten ↑/↓**: durch die gefilterte Liste bewegen
- **Eingabetaste**: den ausgewählten Befehl ausführen
- **Escape**: die Palette schließen
- **⌘-Tastenkombinationen**: schließen die Palette und führen den passenden Menübefehl aus (drücken Sie z. B. {% kbd cmd U %}, um **Quelltextansicht umschalten** auszuführen, statt es in der Liste auszuwählen)

Reine Eingabe (ohne Befehlstaste) filtert das Suchfeld. Einzeltasten nur für die Vorschau wie `s` für Automatisches Scrollen filtern die Liste; drücken Sie **Eingabetaste**, um den ausgewählten Befehl auszuführen.

## Befehle ausführen

Wählen Sie einen Menübefehl aus, wird er genauso ausgelöst wie über das Menü – auch dynamische Einträge und Zahnradmenü-Einträge.

Wählen Sie einen **Vorschau-Tastaturkurzbefehl** aus, wird die zugehörige Aktion in der aktiven Vorschau ausgeführt (z. B. automatisches Scrollen umschalten oder zur nächsten Überschrift springen). Diese Befehle brauchen ein geöffnetes Dokument mit Vorschau; ist keine Vorschau verfügbar, öffnet sich die Palette zwar, die reinen Vorschauaktionen bleiben aber wirkungslos.

Zum Wechseln zwischen zusammengehörigen Dateien siehe [Schnell öffnen](Quick_Open.html). Die vollständige Tastaturreferenz der Vorschau finden Sie unter [Tastaturkurzbefehle](Keyboard_Shortcuts.html) oder drücken Sie in der Vorschau {% kbd h %}, um das Hilfe-HUD anzuzeigen.
