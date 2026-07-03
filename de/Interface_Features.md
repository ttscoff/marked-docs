# <%= @title %>

Flexibilität ist der Schlüssel.

## Zahnradmenü

![][4]

   [4]: images/gearmenu.jpg @2x width=740px height=235px class=center

Das Zahnradmenü bietet die meisten Funktionen der Menüleiste sowie einige vorschauspezifische Funktionen. Klicken Sie einfach auf das Zahnrad unten rechts im Fenster, um diese Funktionen zu erreichen.

## Im Vordergrund halten

![][5]

   [5]: images/KeepOnTopPin.jpg @2x width=740px height=345px class=center

Das Schlosssymbol unten links holt das Vorschaufenster in den Vordergrund und hält es dort (schwebend), wenn Sie zu anderen Anwendungen wechseln. Unter {% prefspane General %} können Sie eine Transparenz für das Fenster festlegen, sodass es sich ausblendet, während Sie andere Anwendungen verwenden.

Diese Funktion lässt sich auch mit {% kbd shift-opt-cmd-f %} umschalten.

## Standardeinstellungen auf Fensterebene

Unter {% prefspane General %} können Sie mit „Neue Fenster im Vordergrund halten“ festlegen, dass neue Fenster immer über anderen bleiben, und/oder Fenster so einstellen, dass sie nach oben steigen, sobald das zugehörige Dokument aktualisiert wird. Fenster, die beim Aktualisieren aufsteigen, „stehlen“ Ihrem Editor nicht den Fokus – sie werden nur sichtbar, ohne aktiv zu werden.

## Quelltextansicht

![][6]

   [6]: images/view_source.jpg @2x width=740px height=345px class=center

Mit der Schaltfläche oben rechts wechseln Sie zwischen Vorschau und Quelltextansicht. Diese Ansicht lässt sich auch mit {% kbd cmd U %} umschalten.

## Suchen

![][7]

   [7]: images/SearchBarFull.jpg @2x width=818px height=195px class=center

Die Suchleiste rufen Sie mit {% kbd cmd F %} auf; damit durchsuchen Sie die Vorschau nach einem Wort oder einer Phrase. Nach einer Suche navigieren Sie mit {% kbd cmd G %} und {% kbd shift cmd G %} vorwärts und rückwärts durch weitere Treffer.

Mit den Kontrollkästchen rechts in der Suchleiste grenzen Sie die Suche nach Groß-/Kleinschreibung, nur ganzen Wörtern und regulären Ausdrücken ein. Zusätzlich zur Suche mit regulären Ausdrücken funktionieren Wildcard-Suchen (*?) immer, auch wenn die Regex-Option aus ist.

Sie können einen Suchbegriff oder eine Phrase auch mit Schrägstrichen umschließen, damit er automatisch als regulärer Ausdruck interpretiert wird (z. B. `/term.+?\b/`).


Nutzen Sie die Suche zusammen mit Lesezeichen, um Fundstellen gleich zu speichern. Drücken Sie die Tabulatortaste ({% kbd ⇥ %}), um das Dokument zu fokussieren, und geben Sie dann Umschalt-[1-9] ein, um ein Lesezeichen auf dieser Nummer zu setzen. Zum Lesezeichen springen Sie zurück, indem Sie einfach die Nummer eingeben (ohne Umschalttaste), oder mit n/p in Dokumentreihenfolge durch die Lesezeichen navigieren. Mit N/P navigieren Sie in numerischer Reihenfolge. Zu Lesezeichen, Inhaltsverzeichnis, Mini-Übersicht und schneller Überschriftensuche siehe [Dokumentnavigation](Document_Navigation.html). Weitere Optionen finden Sie im Abschnitt [Vorschau-Navigation](Keyboard_Shortcuts.html#previewnavigation), oder geben Sie in der Vorschau jederzeit „?“ ein.

> **Hinweis:** Die Suche kann nicht über Elementgrenzen hinweggehen – eine Suchzeichenfolge kann sich also nicht zwischen einem Absatz und einer Überschrift, über Listenelemente hinweg usw. fortsetzen.

Die Kontrollkästchen „Ganze Wörter“, „Groß-/Kleinschreibung beachten“ und „Regex“ schalten Sie mit {% kbd ctrl shift 1 %}, {% kbd 2 %} bzw. {% kbd 3 %} um.

### Erweiterte Suche ###

In einer Nicht-Regex-Suche können Sie Platzhalter verwenden. `*` steht für eine beliebige Folge von Zeichen ohne Leerzeichen, `?` für ein einzelnes beliebiges Zeichen.

Beginnt eine Suche mit `*`, wird daraus eine jQuery-Selektor-Suche. Sie können jeden jQuery-Selektor verwenden; alle passenden Elemente werden hervorgehoben und sind mit {% kbd cmd G %} und {% kbd shift cmd G %} ansteuerbar. Um eine Textsuche auf einen bestimmten Elementtyp zu beschränken, hängen Sie die Suchbegriffe in doppelten Anführungszeichen an die Selektordefinition an:

    *h2 "Alice"

Das entspricht `*h2:contains(Alice)`.

## Dokumentnavigation (Inhaltsverzeichnis, Lesezeichen, Mini-Übersicht)

Die Seite [Dokumentnavigation](Document_Navigation.html) behandelt das Inhaltsverzeichnis (samt Öffnen des Filters mit {% kbd Space %}), die Schnellsuche mit {% kbd f %}, Lesezeichen und die Mini-Übersicht.

## Tastaturnavigation

Im Vorschaufenster navigieren Sie schnell per Tastaturkurzbefehl. Mit {% kbd j %} und {% kbd k %} bewegen Sie sich nach oben und unten; halten Sie Umschalt ({% kbd J %}/{% kbd K %}) gedrückt, geht es schneller. {% kbd t %} und {% kbd b %} springen an den Anfang und das Ende des Dokuments (ebenso {% kbd gg %} und {% kbd G %} für Vim-Fans). {% kbd u %} und {% kbd d %} bewegen eine halbe Seite nach oben bzw. unten.

### Zwischen Überschriften springen

Mit Komma ({% kbd , %}) und Punkt ({% kbd . %}) springen Sie rückwärts und vorwärts durch alle Überschriften im Dokument. Halten Sie Umschalt ({% kbd shift  %}) gedrückt, wird nur zwischen Überschriften der Ebenen 1 und 2 gesprungen.


## Vollbild

Den Vollbildmodus schalten Sie über das Menü **Vorschau** oder mit {% kbd ctrl cmd F %} um.

## Klicken auf externe Links

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Wenn Sie in der Vorschau Ihres Dokuments auf einen externen Link klicken, wird er in Ihrem Standardbrowser geöffnet. Wenn Sie klicken und gedrückt halten, bietet Marked beim Loslassen drei Optionen: Sie können die URL des Links in die Zwischenablage kopieren, den Link prüfen oder ihn in Ihrem Standardbrowser öffnen. Klicken Sie einfach irgendwo in die Vorschau, um das Fenster zu schließen. Diese Funktion lässt sich unter {% prefspane Preview %} deaktivieren („Link-Popover aktivieren“).

Ein [Übersichtsvideo auf YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1) gibt es hier.

## Einklappbare Überschriften ##

Wenn unter {% prefspane Preview %} die Option „Überschriften klappen Abschnitte ein“ aktiviert ist, klappt ein Klick auf eine Überschrift den Abschnitt zwischen dieser und der nächsten Überschrift derselben Ebene ein. Unterabschnitte darin werden verborgen. Optional können Sie dieses Verhalten auf {% kbd cmd %}-Klick beschränken.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Halten Sie beim Klicken {% kbd opt  %} gedrückt (oder nutzen Sie {% kbd cmd %}-Klick), werden alle untergeordneten Abschnitte unterhalb der angeklickten Überschrift aus- bzw. eingeklappt. Halten Sie beim Klicken Umschalt ({% kbd shift  %}) gedrückt, werden alle anderen Abschnitte derselben Ebene eingeklappt, sodass nur der angeklickte sichtbar bleibt.

Eingeklappte Abschnitte sind mit einer gelben Markierung rechts neben dem Titel gekennzeichnet, und der Mauszeiger zeigt an, was ein Klick bewirkt.

Wird eine Änderung vorgenommen, die sichtbar sein muss, oder klickt man im Inhaltsverzeichnis auf einen Abschnitt, der aktuell in einem eingeklappten Bereich liegt, werden die nötigen übergeordneten Abschnitte ausgeklappt, um ihn anzuzeigen.

Alle Abschnitte eines Dokuments klappen Sie auf einmal mit „Alle Abschnitte einklappen“ ({% kbd opt cmd left  %}) und „Alle Abschnitte ausklappen“ ({% kbd opt cmd right  %}) ein bzw. aus.

Weitere Einzelheiten zeigt das [Video zur Dokumentnavigation auf YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

## Anzeigen/Schalter für den benutzerdefinierten Prozessor ##

![][indicators]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

Sind der benutzerdefinierte Prozessor und/oder Präprozessor aktiviert, erscheinen in der Symbolleiste Kontrollleuchten. An ihnen sehen Sie, ob der Prozessor für das aktuelle Dokument eingeschaltet ist (die Anzeige leuchtet dann), und ein Klick schaltet die Verwendung des benutzerdefinierten Präprozessors bzw. Prozessors um.

## Zur Bearbeitung scrollen

Die Funktion „Zur Bearbeitung scrollen“ in Marked verfolgt die Unterschiede zwischen dem neuesten und dem vorherigen Update und versucht, die Stelle Ihrer jüngsten Änderungen zu finden. Marked verfolgt das laufend, und in der Vorschau erscheint eine kleine rote Linie an der Stelle der ersten erkannten Änderung. Unter {% prefspane Preview %} können Sie „Zur ersten Bearbeitung scrollen“ aktivieren; dann scrollt die Ansicht bei einer Aktualisierung sanft an diese Stelle.

Ist „Zur ersten Bearbeitung scrollen“ deaktiviert, können Sie in der Vorschau jederzeit die Taste „e“ drücken, um zum zuletzt gespeicherten Bearbeitungspunkt zu springen.

## Autoscroll

Siehe die eigene Seite [Autoscroll](Autoscroll.html). Wenn Sie Autoscroll als Teleprompter nutzen, lassen sich mit [spezieller Syntax](Special_Syntax.html#pauses) Pausen einfügen.

## Zoom-Übersicht

Siehe die Seite [Zoom-Übersicht](Zoom_Overview.html) ({% kbd z %} in der Vorschau; funktioniert auch in der Wortwiederholung mit {% kbd ctrl cmd w %}).

## Markdown-Referenz

![][11]

   [11]: images/markdown_reference.jpg @2x width=1148px height=267px class=center

Wählen Sie im Menü {% appmenu Hilfe %} den Eintrag **Markdown-Referenz**, um einen Leitfaden anzuzeigen, der über Ihren anderen Fenstern schwebt. Praktisch, wenn Sie Markdowns Syntax noch lernen. Dieses Fenster öffnen Sie per Tastatur mit {% kbd opt cmd M %}.

## Globale Tastaturkurzbefehle

Unter {% prefspane General %} können Sie einen eigenen Tastaturkurzbefehl zum Aktivieren von Marked festlegen und einen weiteren, um nur das vorderste Fenster nach oben zu holen, ohne Ihren Editor zu verlassen.
