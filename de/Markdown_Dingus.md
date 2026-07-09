# <%= @title %>

Der Markdown-Dingus ist ein spezialisiertes Testwerkzeug, mit dem Sie nachvollziehen können, wie verschiedene Markdown-Prozessoren Ihren Inhalt behandeln. Er bietet eine dreigeteilte Oberfläche, in der Sie gleichzeitig Markdown bearbeiten, den erzeugten HTML-Quelltext ansehen und die gerenderte Vorschau sehen.

Der Dingus teilt sich einige Low-Level-Behandlungen mit Markeds Vorschau, etwa die besondere Behandlung abgegrenzter Codeblöcke. Er führt __keine__ [Eigenen Regeln](Custom_Processor.html) (Conductor) aus. Er verwendet weitgehend die Standardeinstellungen und ignoriert Einstellungen wie „GitHub-Zeilenumbrüche“ und „GitHub-Kontrollkästchen“, sodass das Ergebnis von dem abweichen kann, was Sie in einer normalen Marked-Vorschau sehen.

## Eigene Regeln gelten nicht

Der Dingus ist eine __Prozessor-Sandbox__: Ihr Markdown geht direkt an den integrierten Prozessor, den Sie wählen (MultiMarkdown, CommonMark (GFM), Discount oder Kramdown). [Eigene Regeln](Custom_Processor.html) laufen dort nie – keine Präprozessor-Aktionen, keine Suchen/Ersetzen-Regeln, keine Shell-Befehle, kein Text/Datei einfügen und keine anderen Conductor-Schritte.

In einer normalen Vorschau können Eigene Regeln das Markdown vor dem Rendern ändern, Stile setzen, CSS oder JavaScript einfügen und mehr. Nichts davon passiert, wenn Sie im Dingus bearbeiten. Ändern Sie Eigene Regeln bei geöffnetem Dingus, aktualisiert das seine Vorschau nicht.

Der Dingus __kann__ dieselben [Vorschau-CSS-Stile](Custom_Styles.html) wie das Hauptfenster verwenden (über das Stilmenü im Ausgabebereich). Das betrifft nur das Aussehen; es ist nicht dasselbe wie das Ausführen Eigener Regeln.

__In Dingus öffnen__ aus einer Vorschau lädt den aktuellen Markdown-Puffer des Dokuments. Sind beim Öffnen dieser Datei in Marked bereits Eigene Regeln gelaufen, sehen Sie deren Auswirkungen womöglich im Text (zum Beispiel von einer Regel eingefügten Text), aber der Dingus wendet die Regeln während der Eingabe nicht erneut an. Um Eigene Regeln zu testen, nutzen Sie eine normale Marked-Vorschau oder speichern Sie aus dem Dingus und öffnen die Datei mit __In Marked öffnen__.

## Was ist ein „Dingus“?

„Dingus“ ist ein aus der Webentwicklung entlehnter Begriff für ein einfaches Testwerkzeug oder eine Sandbox-Umgebung. Mit dem Markdown-Dingus experimentieren Sie mit Markdown-Syntax und sehen sofort, wie verschiedene Prozessoren sie interpretieren.

## Zugriff auf den Dingus

Den Markdown-Dingus erreichen Sie über [{% appmenu Hilfe, Markdown-Dingus öffnen %}][2]. Besonders nützlich ist er, wenn Sie:

* neue Markdown-Syntax lernen möchten
* Rendering-Probleme beheben wollen
* zwischen verschiedenen Prozessoren den für Ihren Anwendungsfall am besten passenden suchen
* Dokumentation schreiben, die über mehrere Systeme hinweg funktionieren muss

## Drei-Fenster-Layout

![][1]

Das Dingus-Fenster ist in drei synchronisierte Bereiche unterteilt:

### 1. Markdown-Eingabe (linker Bereich)

* __Syntaxhervorhebung__: Ihr Markdown wird farblich hervorgehoben, damit die Struktur klar wird
* __Live-Bearbeitung__: Tippen Sie und sehen Sie Änderungen sofort in den anderen Bereichen
* __Große Schrift__: 21-pt-Menlo-Schrift für komfortables Bearbeiten

__Options-Dropdown__ (oben rechts im linken Bereich): Über das Menü **Optionen** schalten Sie um:

* __Zeilennummern anzeigen__: Zeigt am linken Rand eine Spalte mit einer Zeilennummer pro Absatz (umbrochene Zeilen zählen als eine Zeile).
* __Unsichtbare anzeigen__: Zeigt Leerzeichen als Mittelpunkte (·), Tabulatoren als Rechtspfeil (→) und Zeilenumbrüche als Zeilenschaltungssymbol (↵) in hellem Grau, damit Sie verirrte Steuerzeichen erkennen.
* __Gremlins hervorheben__: Legt einen hellroten Hintergrund auf Nicht-ASCII-Zeichen (z. B. typografische Anführungszeichen, Emoji) und einen dunkelroten Hintergrund auf problematische unsichtbare Zeichen (z. B. Zeichen ohne Breite). Normale Tabulator- und Zeilenumbruchzeichen werden nicht hervorgehoben.

Ihre Auswahl wird gespeichert und beim nächsten Öffnen des Dingus wiederhergestellt.

__Suchleiste__: Drücken Sie **⌘F**, um die Suchleiste unter der Beschriftung „Markdown-Eingabe“ einzublenden. Sie können im Editor suchen und ersetzen, mit **⌘G** weitersuchen und mit **⇧⌘G** rückwärts suchen sowie eine oder alle Übereinstimmungen ersetzen. Über die Schließen-Schaltfläche oder erneut **⌘F** blenden Sie die Suchleiste aus.

### 2. HTML-Quelltext (mittlerer Bereich)

* __Erzeugtes HTML__: Sehen Sie genau, welches HTML der gewählte Prozessor erzeugt
* __Syntaxhervorhebung__: Die HTML-Syntax ist zum leichteren Lesen farblich gekennzeichnet

### 3. Gerenderte Vorschau (rechter Bereich)

* __Live-Vorschau__: Sehen Sie, wie Ihr Markdown gerendert aussieht
* __Emoji-Unterstützung__: Emojis im GitHub-Stil wie `:zzz:` werden in Bilder umgewandelt
* __Auto-Scrollen__: Scrollt automatisch zu Ihrer aktuellen Bearbeitungsposition

## Bearbeiten im Dingus

Der Markdown-Eingabebereich bietet intelligente Bearbeitungsfunktionen, die das Schreiben von Markdown schneller und natürlicher machen.

### Intelligenter Zeilenumbruch (Return-Taste)

Ein Druck auf Return passt sich an die aktuelle Zeile an:

* __Listen__: In einer Listenzeile (`-`, `*`, `+` oder `1.`) fügt er ein neues Listenelement mit der richtigen Markierung ein. Nummerierte Listen laufen mit der nächsten Nummer weiter.
* __Blockzitate__: In einer Zeile, die mit `>` beginnt, fügt er eine neue Blockzitat-Zeile ein.
* __Code-Blöcke__: In einer Zeile mit drei oder mehr Backticks (z. B. ` ``` `) fügt er eine Leerzeile zwischen öffnendem und schließendem Element ein.
* __Andere Zeilen__: Fügt einen normalen Zeilenumbruch ein.

### Zeichenpaarung

Wenn Sie ein öffnendes Zeichen tippen, fügt der Editor automatisch das schließende Zeichen ein und setzt den Cursor dazwischen. Unterstützte Paare: `"` `'` `(` `[` `` ` `` `<`.

* __Mit Auswahl__: Umschließt den ausgewählten Text mit dem Paar.
* __Ohne Auswahl__: Fügt das Paar ein und setzt den Cursor dazwischen.
* __Type-over__: Ist das nächste Zeichen bereits das schließende Trennzeichen, bewegt ein erneutes Tippen den Cursor daran vorbei, statt ein Duplikat einzufügen.
- __Leerzeichen im leeren Paar__: Steht der Cursor zwischen einem leeren Paar (z. B. `(|)`), ersetzt ein Leerzeichen das schließende Zeichen durch ein Leerzeichen.

### Tastenkürzel

| Kürzel | Aktion |
| :------------ | :--- |
| **⌘F** | Suchleiste im Markdown-Eingabebereich ein- oder ausblenden |
| **⌘G** | Weitersuchen (wenn die Suchleiste sichtbar ist) |
| **⇧⌘G** | Rückwärts suchen (wenn die Suchleiste sichtbar ist) |
| **⌘B** | Fett: Auswahl in `**` umschließen oder `**\|**` mit Cursor dazwischen einfügen |
| **⌘I** | Kursiv: Auswahl in `_` umschließen oder `_\|_` mit Cursor dazwischen einfügen |
| **⇧⌘L** | Listenmarkierung durchschalten (ungeordnet ↔ geordnet) |
| **Tab** | Zeile oder Listenelement einrücken |
| **Umschalt+Tab** | Zeile oder Listenelement ausrücken |
| **⌃⌘→** | Zeile oder Listenelement einrücken (wie Tab) |
| **⌃⌘←** | Zeile oder Listenelement ausrücken (wie Umschalt+Tab) |
| **⌃⌘↑** | Absatz nach oben verschieben (Absatz samt Zeilenumbruch ausschneiden, eine Zeile höher einfügen) |
| **⌃⌘↓** | Absatz nach unten verschieben (Absatz samt Zeilenumbruch ausschneiden, eine Zeile tiefer einfügen) |
| **⌘K** | Markdown-Link einfügen oder umschließen: Auswahl als `[text]()` umschließen und den Cursor in die URL setzen, oder ohne Auswahl `[]()` mit dem Cursor zwischen den Klammern einfügen |
| **F6** | Magischer Referenzlink: Auswahl als `[text][n]` umschließen und am Dokumentende eine `[n]: `-Definition anfügen; steht der Cursor auf einer vorhandenen Referenz, zwischen Inline-Marker und Definition springen |
| **F7** | Magische Fußnote: `[^n]` an der Cursorposition (oder nach dem aktuellen Wort) einfügen und am Dokumentende eine passende `[^n]: `-Definition anfügen; steht der Cursor auf einer vorhandenen Fußnote, zwischen Marker und Definition springen |
| **⌘U** | Ausgabebereich umschalten (Quelltext/Vorschau) |
| **⌥⌘↑** | Auswahl erweitern: Wort → innere/äußere Trennzeichen → Satz → Absatz → zusammenhängender Block (z. B. eine Tabelle oder ein Codeblock) → umschließende Liste/Blockzitat/Codeblock → Dokument |
| **⌥⌘↓** | Auswahl über dieselben Ebenen zurück bis zur ursprünglichen Cursorposition verkleinern |

Tab/Umschalt+Tab (und ⌃⌘←/⌃⌘→) berücksichtigen Listenstruktur und Blockzitate: Sie rücken Listenelemente ein oder aus und fügen `>` in Blockzitat-Zeilen hinzu oder entfernen es. „Absatz nach oben/unten verschieben“ wählt den gesamten Absatz unter dem Cursor aus (samt nachfolgendem Zeilenumbruch), schneidet ihn aus und fügt ihn über oder unter dem angrenzenden Absatz ein, damit Absätze nicht verschmelzen.

### Magische Links und Fußnoten (F6 / F7)

Der Dingus-Editor kann für Sie __Referenzlinks__ und __Fußnoten__ anlegen, vergibt automatisch die nächste freie Nummer und hängt die passende Definition am Dokumentende an.

* __F6 (magischer Referenzlink)__: Mit markiertem Text wird die Auswahl als `[text][n]` umschlossen und am Dokumentende eine neue `[n]: `-Zeile ergänzt, in die Sie die URL eintragen. Zum Anlegen eines neuen Referenzlinks ist eine Auswahl nötig. Steht der Cursor bereits auf einem Referenzlink oder seiner Definition, springt **F6** zwischen Inline-Marker und Definition (oder legt die Definition an, falls sie fehlt).
* __F7 (magische Fußnote)__: Fügt an der Cursorposition – oder nach dem aktuellen Wort, wenn der Cursor darin steht – einen nummerierten Fußnotenmarker `[^n]` ein und hängt `[^n]: ` an; bei markiertem Text wird der markierte Text als Fußnotentext verwendet. Steht der Cursor auf einem vorhandenen Fußnotenmarker oder einer Definition, springt **F7** zwischen beiden.

Referenz- und Fußnotennummern werden automatisch vergeben, sodass Sie keine IDs von Hand verwalten müssen. Beide Tastenkürzel funktionieren nicht in abgegrenzten oder eingerückten Codeblöcken.

### Intelligentes URL-Einfügen

Wenn Sie einfügen und die Zwischenablage eine URL der Form `protocol://...` ohne Leerzeichen enthält:

* __Mit Auswahl__: Die Auswahl wird in einen Markdown-Link umgewandelt: `[selected text](url)`.
* __Ohne Auswahl__: Die URL wird als Selbstlink eingefügt: `<url>`.

So verwandeln Sie kopierte URLs bequem in Links, ohne sie von Hand zu tippen.

### Intelligente Auswahl (⌥⌘↑ / ⌥⌘↓)

Der Dingus-Editor unterstützt eine __semantische Auswahlerweiterung__:

* __⌥⌘↑__ beginnt an der Cursorposition und erweitert die Auswahl über:
	- das aktuelle Wort
	- innere und äußere abgegrenzte Inhalte (Anführungszeichen, eckige Klammern, runde Klammern und abgegrenzte Codeblöcke)
	- den aktuellen Satz
	- den aktuellen Absatz
	- den zusammenhängenden, nicht leeren Zeilenblock (zum Beispiel eine ganze Tabelle oder einen mehrzeiligen Codeblock ohne Leerzeilen)
	- das umschließende Listenelement, Blockzitat oder den umschließenden Codeblock
	- das gesamte Dokument
* __⌥⌘↓__ geht dieselben Ebenen wieder zurück, bis die ursprüngliche Cursorposition erreicht ist.

Jeder Druck führt immer zu einer strikt größeren oder kleineren Auswahl, sodass beim Erweitern oder Verkleinern nie ein „No-Op“-Tastendruck entsteht.

## Den Dingus als Editor verwenden

Der Dingus soll keinen vollwertigen Texteditor ersetzen, ist aber sehr praktisch für __schnelle Bearbeitungen mit Live-Vorschau__, besonders wenn Sie genau sehen wollen, wie sich Änderungen rendern. Das gesamte in [Bearbeiten im Dingus][3] beschriebene Textbearbeitungsverhalten gilt auch hier.

### Eine Datei öffnen / eine neue Datei erstellen

* __Eine neue Datei im Dingus erstellen__
	- Wählen Sie __{% appmenu Ablage, Neu, Neue Markdown-Datei %}__ (⌘N).
	- Wählen Sie bei der Nachfrage __Dingus__, um ein neues, ungespeichertes Dingus-Dokument zu beginnen.
	- Neue Dingus-Dokumente öffnen sich mit ausgewähltem Beispielinhalt; tippen Sie einfach los, um ihn zu ersetzen.
* __Eine vorhandene Datei im Dingus öffnen__
	- Verwenden Sie __{% appmenu Ablage, In Dingus öffnen… %}__ (⌥⌘O), oder klicken Sie bei aktivem Dingus-Fenster in der Statusleiste auf __Öffnen…__. Der Befehl öffnet bei Bedarf das Dingus-Fenster und zeigt dann das Öffnen-Fenster.
	- Wählen Sie eine beliebige unterstützte Klartext-/Markdown-Datei; ihr Inhalt ersetzt den aktuellen Dingus-Puffer.
* __Ein Marked-Vorschaudokument im Dingus öffnen__
	- Verwenden Sie in einem normalen Vorschaufenster __{% appmenu Vorschau, In Dingus öffnen %}__ (⌥⌘E).
	- Das Markdown des aktuellen Dokuments wird in den Dingus geladen, sodass Sie experimentieren können, ohne die Originaldatei anzutasten, bis Sie speichern. Eigene Regeln werden im Dingus nicht angewendet; siehe [Eigene Regeln gelten nicht](#eigene-regeln-gelten-nicht).

### Eine Datei speichern

* __Änderungen an der aktuellen Datei speichern__
	- Klicken Sie im Dingus-Fenster in der Statusleiste auf __Speichern__ oder verwenden Sie __{% appmenu Ablage, Dingus speichern %}__ (⌘S).
	- Wurde das Dingus-Dokument noch nicht gespeichert, werden Sie nach Speicherort und Dateinamen gefragt; danach aktualisiert ⌘S dieselbe Datei.
* __Speichern unter / in eine neue Datei duplizieren__
	- Verwenden Sie __{% appmenu Ablage, Dingus speichern unter… %}__ (⌥⌘S).
	- Das öffnet immer einen __Speichern unter__-Dialog und schreibt den aktuellen Dingus-Inhalt in eine neue Datei, ohne das Original zu überschreiben.

### In Marked ansehen

* __Das Dingus-Dokument als vollständige Marked-Vorschau öffnen__
	- Klicken Sie in der Dingus-Statusleiste auf __In Marked öffnen__ oder verwenden Sie __{% appmenu Ablage, Dingus in Marked öffnen %}__ (⌘P).
	- Ist das Dingus-Dokument ungespeichert oder hat es ungespeicherte Änderungen, werden Sie zuerst zum Speichern aufgefordert; dann öffnet Marked eine normale Vorschau für diese Datei.

Mit diesen Befehlen nutzen Sie den Dingus als leichten Editor für schnelle Korrekturen und Experimente und springen dann zu einer vollständigen Marked-Vorschau oder Ihrem gewohnten Editor, wenn Sie umfangreicher bearbeiten wollen.

## Prozessorauswahl

Verwenden Sie das Dropdown-Menü oben, um zwischen verschiedenen Markdown-Prozessoren zu wechseln:

* __MultiMarkdown__: Voll ausgestatteter Prozessor mit Tabellen, Fußnoten und Mathematik-Unterstützung
* __CommonMark (GFM)__: Standardkonformer, schneller Prozessor nach der CommonMark-Spezifikation
* __Discount__: GitHub Flavored Markdown mit Aufgabenlisten und Tabellen
* __Kramdown__: Fortgeschrittener Prozessor mit Zusatzfunktionen wie IALs und Typografie

## Warum den Dingus verwenden?

### Prozessorunterschiede verstehen

Verschiedene Markdown-Prozessoren behandeln Syntax unterschiedlich. Mit dem Dingus können Sie:

* __Ausgabe vergleichen__: Sehen Sie genau, wie jeder Prozessor dasselbe Markdown rendert
* __Probleme debuggen__: Erkennen Sie, warum eine bestimmte Syntax nicht wie erwartet funktioniert
* __Syntax lernen__: Verstehen Sie die feinen Unterschiede zwischen den Prozessor-Implementierungen

### Vor dem Schreiben testen

Bevor Sie sich in Ihren Dokumenten auf einen bestimmten Markdown-Stil festlegen:

* __Syntax prüfen__: Stellen Sie sicher, dass Ihr Markdown korrekt rendert
* __Prozessoren wählen__: Entscheiden Sie, welcher Prozessor am besten zu Ihrem Inhalt passt
* __Sicher experimentieren__: Probieren Sie neue Syntax aus, ohne Ihre echten Dokumente zu beeinflussen

## Häufige Anwendungsfälle

### Unterschiede in der Tabellensyntax

Manche Prozessoren behandeln Tabellensyntax unterschiedlich. Der Dingus zeigt Ihnen, welcher Prozessor Ihre Tabellenformatierung am besten unterstützt.

### Fußnoten-Unterstützung

Nicht alle Prozessoren unterstützen Fußnoten. Prüfen Sie mit dem Dingus, ob die Fußnotensyntax mit Ihrem gewählten Prozessor funktioniert.

### Mathematik und Sonderzeichen

Testen Sie, wie verschiedene Prozessoren mathematische Ausdrücke und besondere Typografie-Zeichen behandeln.

## Tipps für den effektiven Einsatz

1. __Einfach anfangen__: Beginnen Sie mit einfachem Markdown und steigern Sie die Komplexität schrittweise.
2. __Grenzfälle testen__: Probieren Sie ungewöhnliche Syntax-Kombinationen, um die Grenzen der Prozessoren auszuloten.
3. __Nebeneinander vergleichen__: Wechseln Sie zwischen Prozessoren, um Unterschiede klar zu erkennen.
4. __Echte Inhalte verwenden__: Kopieren Sie tatsächliche Inhalte aus Ihren Dokumenten, um realistische Szenarien zu testen.

Der Dingus ist ein mächtiges Werkzeug für alle, die die Feinheiten verschiedener Markdown-Implementierungen verstehen und sicherstellen wollen, dass ihre Inhalte über verschiedene Plattformen und Prozessoren hinweg korrekt rendern.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #bearbeiten-im-dingus
