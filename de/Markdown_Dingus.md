# <%= @title %>

Der Markdown Dingus ist ein spezielles Testtool, das hilft
Sie verstehen, wie verschiedene Markdown-Prozessoren mit Ihrem umgehen
Inhalt. Es bietet eine Schnittstelle mit drei Fenstern, wo Sie können
Bearbeiten Sie Markdown, sehen Sie sich die generierte HTML-Quelle an und sehen Sie sich die an
gerenderte Vorschau gleichzeitig.

Der Dingus teilt einige einfache Handhabungen mit denen von Marked
Vorschau, wie z. B. eine spezielle Behandlung von abgeschirmten Codeblöcken.
[Custom Rules](Custom_Processor.html) wird __nicht__ ausgeführt
(Dirigent). Es verwendet die meisten Standardeinstellungen und ignoriert die Einstellungen
wie „GitHub Zeilenumbrüche“ und „GitHub Kontrollkästchen“, also die
Das Ergebnis kann von dem abweichen, was Sie in einem normalen Marked sehen
Vorschau.

## Custom Regeln gelten nicht

Der Dingus ist eine __Prozessor-Sandbox__: Ihr Markdown geht
direkt an den von Ihnen gewählten integrierten Prozessor (MultiMarkdown,
CommonMark (GFM), Discount oder Kramdown). [Custom Rules](Custom_Processor.html)
nie dort ausführen – keine Vorverarbeitungsaktionen, Suchen/Ersetzen-Regeln,
Shell-Befehle, Text/Datei einfügen oder andere Conductor-Schritte.

In einer normalen Vorschau können Custom-Regeln den Markdown ändern.
Legen Sie vor dem Rendern Stile fest, fügen Sie CSS oder JavaScript ein und
mehr. Nichts davon passiert, wenn Sie im Dingus bearbeiten.
Das Ändern der Custom-Regeln bei geöffnetem Dingus ist nicht möglich
Aktualisieren Sie die Vorschau.

Die Dingus __can__ verwenden dasselbe [preview CSS styles](Custom_Styles.html)
als Hauptfenster (über das Stilmenü im Ausgabebereich).
Das ist nur der Schein; es ist nicht dasselbe wie das Ausführen von Custom
Regeln.

__Open in Dingus__ aus einer Vorschau lädt das Dokument
aktueller Markdown-Puffer. Wenn Custom Regeln bereits wann ausgeführt wurden
Diese Datei wurde in Marked geöffnet. Möglicherweise sehen Sie deren Auswirkungen in
der Text (z. B. durch eine Regel eingefügter Text), aber der
Dingus wendet Regeln während der Eingabe nicht erneut an. Zum Testen von Custom
Regeln, verwenden Sie eine standardmäßige Marked-Vorschau oder speichern Sie sie aus dem Dingus
und öffnen Sie die Datei mit __Open in Marked__.

## Was ist ein „Dingus“?

Ein „Dingus“ ist ein aus der Webentwicklung entlehnter Begriff
bezieht sich auf ein einfaches Testtool oder eine Sandbox-Umgebung. Die
Mit Markdown Dingus können Sie mit der Syntax von Markdown experimentieren
Sehen Sie sofort, wie verschiedene Prozessoren es interpretieren.

## Zugriff auf Dingus

Auf den Markdown Dingus kann zugegriffen werden
[<!--MKPH0-->][2]. Es ist besonders
nützlich, wenn Sie:

* Erlernen der neuen Markdown-Syntax
* Fehlerbehebung bei Rendering-Problemen
* Auswahl zwischen verschiedenen Prozessoren
* Schreiben von Dokumentationen, die auf mehreren Ebenen funktionieren müssen
  Systeme

## Drei-Fenster-Layout

![][1]

Das Fenster Dingus ist in drei synchronisierte Bereiche unterteilt:

### 1. Markdown Eingabe (linker Bereich)

* __Syntax-Hervorhebung__: Ihr Markdown wird mit hervorgehoben
  Farben, um die Struktur klar zu machen
* __Live-Bearbeitung__: Geben Sie Änderungen ein und sehen Sie, wie sie sofort angezeigt werden
  in den anderen Bereichen
* __Große Schriftart__: 21pt Menlo-Schriftart für komfortables Bearbeiten

__Options-Dropdown__ (oben rechts im linken Bereich): Die
Mit dem Menü **Optionen** können Sie Folgendes umschalten:

* __Zeilennummern anzeigen__: Zeigt links einen Zwischenraum an
  eine Zeilennummer pro Absatz (umbrochene Zeilen zählen als eine).
  Linie).
* __Unsichtbare anzeigen__: Zeigt Leerzeichen als Mittelpunkte (·), Tabulatoren als
  ein Rechtspfeil (→) und Zeilenumbrüche als Wagenrücklauf
  Symbol (↵) in einem hellen Grau, damit Sie Streuner erkennen können
  Leerzeichen.
* __Gremlins hervorheben__: Setzt einen hellroten Hintergrund ein
  Nicht-ASCII-Zeichen (z. B. geschweifte Anführungszeichen, Emoji) und ein dunkles Zeichen
  Roter Hintergrund bei problematischen unsichtbaren Zeichen (z. B.
  Leerzeichen mit der Breite Null). Normale Tabulator- und Zeilenumbruchzeichen sind
  nicht hervorgehoben.

Ihre Auswahl wird gespeichert und beim nächsten Öffnen wiederhergestellt
der Dingus.

__Suchleiste__: Drücken Sie **⌘F**, um die Suchleiste unter dem anzuzeigen
Bezeichnung „Markdown Eingabe“. Sie können im suchen und ersetzen
Editor verwenden Sie **⌘G** für „Weitersuchen“ und **⇧⌘G** für „Suchen“.
Zurück und ersetzen Sie eine oder alle Übereinstimmungen. Drücken Sie die Schließen-Taste
Klicken Sie erneut auf die Schaltfläche oder **⌘F**, um die Suchleiste auszublenden.

### 2. HTML Quelle (mittlerer Bereich)

* __Generated HTML__: Sehen Sie genau, was HTML das ausgewählte ist
  Prozessor erstellt
* __Syntax hervorgehoben__: HTML ist zur Vereinfachung farblich gekennzeichnet
  Lesen

### 3. Gerenderte Vorschau (rechter Bereich)

* __Live-Vorschau__: Sehen Sie, wie Ihr Markdown wann aussehen wird
  gerendert
* __Emoji-Unterstützung__: Emojis im GitHub-Stil wie `:zzz:` sind
  in Bilder umgewandelt
* __Auto-Scrolling__: Scrollt automatisch, um Ihre anzuzeigen
  aktuelle Bearbeitungsposition

## Bearbeiten im Dingus

Der Markdown-Eingabebereich enthält intelligente Bearbeitungsfunktionen für
Machen Sie das Schreiben von Markdown schneller und natürlicher.

### Smart Newline (Return-Taste)

Durch Drücken der Eingabetaste wird die aktuelle Zeile angepasst:

* __Lists__: In einer Listenzeile (`-`, `*` , `+` oder `1.` ),
  Fügt ein neues Listenelement mit der richtigen Markierung ein. Nummeriert
  Listen werden mit der nächsten Nummer fortgesetzt.
* __Blockquotes__: Fügt in einer Zeile, die mit `>` beginnt, ein ein
  neue Blockquote-Zeile.
* __Code-Zäune__: Auf einer Linie mit drei oder mehr Backticks
  (z. B. ` ``` `), fügt eine Leerzeile zwischen der Öffnung ein
  und Zäune schließen.
* __Andere Zeilen__: Fügt eine normale neue Zeile ein.

### Zeichenpaarung

Wenn Sie ein Anfangszeichen eingeben, öffnet sich der Editor automatisch
fügt das Schlusszeichen ein und platziert den Cursor dazwischen
sie. Unterstützte Paare: `"` `'` `(` `[` `` ` `` `<` .

* __Mit Auswahl__: Schließt den ausgewählten Text in das Paar ein.
* __Ohne Auswahl__: Fügt das Paar mit dem Cursor ein
  zwischen ihnen.
* __Type-over__: Wenn das nächste Zeichen bereits das ist
  Wenn Sie das schließende Trennzeichen eingeben, bewegt sich der Cursor bei erneuter Eingabe daran vorbei
  es, anstatt ein Duplikat einzufügen.
- __Leerzeichen in leerem Paar__: Wenn sich der Cursor zwischen einem leeren Paar befindet (z. B. `(|)`), wird durch die Eingabe eines Leerzeichens das Schlusszeichen durch ein Leerzeichen ersetzt.

### Tastenkombinationen

| Verknüpfung | Aktion |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⌘F** | Ein- oder Ausblenden der Suchleiste im Markdown-Eingabebereich |
| **⌘G** | Weitersuchen (wenn die Suchleiste sichtbar ist) |
| **⇧⌘G** | Vorheriges suchen (wenn die Suchleiste sichtbar ist) |
| **⌘B** | Fett: Auswahl in `**` umschließen oder `**\|**` mit Cursor zwischen | einfügen
| **⌘I** | Kursiv: Auswahl in `_` umbrechen oder `_\|_` mit Cursor zwischen | einfügen
| **⇧⌘L** | Zykluslistenmarkierung (ungeordnet ↔ geordnet) |
| **Tabulatortaste** | Zeile oder Listenelement einrücken |
| **Umschalt+Tabulator** | Zeile oder Listenelement ausrücken |
| **⌃⌘→** | Zeile oder Listenelement einrücken (wie Tab) |
| **⌃⌘←** | Zeile oder Listenelement ausrücken (wie Umschalt+Tab) |
| **⌃⌘ ↑** | Absatz nach oben verschieben (Absatz einschließlich Zeilenumbruch ausschneiden, eine Zeile nach oben einfügen) |
| **⌃⌘↓** | Absatz nach unten verschieben (Absatz einschließlich Zeilenumbruch ausschneiden, eine Zeile nach unten einfügen) |
| **⌘K** | Fügen Sie einen Markdown-Link ein oder umschließen Sie ihn: Umschließen Sie die Auswahl als `[text]()` und platzieren Sie den Cursor in der URL, oder fügen Sie `[]()` mit dem Cursor zwischen den Klammern ein, wenn keine Auswahl vorhanden ist |
| **F6** | Magischer Referenzlink: Auswahl als `[text][n]` umschließen und eine `[n]: `-Definition am Ende des Dokuments anfügen; wenn der Cursor auf einer vorhandenen Referenz steht, zwischen Inline-Marker und Definition springen |
| **F7** | Magische Fußnote: `[^n]` an der Cursorposition (oder nach dem aktuellen Wort) einfügen und eine passende `[^n]: `-Definition am Ende des Dokuments anfügen; wenn der Cursor auf einer vorhandenen Fußnote steht, zwischen Marker und Definition springen |
| **⌘U** | Ausgabebereich umschalten (Quelle/Vorschau) |
| **⌥⌘ ↑** | Auswahl erweitern: Wort → innere/äußere Trennzeichen → Satz → Absatz → zusammenhängender Block (z. B. eine Tabelle oder ein Codeblock) → umschließende Liste/Blockzitat/Codeblock → Dokument |
| **⌥⌘↓** | Vertragsauswahl durch die gleichen Ebenen zurück zur ursprünglichen Caret-Position |

Tab/Umschalt+Tab (und ⌃⌘←/⌃⌘→) respektieren die Listenstruktur und
Blockzitate: Sie rücken Listenelemente ein/aus und fügen ein oder hinzu
Entfernen Sie `>` aus Blockquote-Zeilen. Absatz nach oben/unten verschieben
Wählt den gesamten Absatz unter dem Cursor aus (einschließlich seiner
nachgestellte neue Zeile), schneidet es aus und fügt es über oder unter dem ein
angrenzenden Absatz, damit Absätze nicht zusammengeführt werden.

### Magische Links und Fußnoten (F6 / F7)

Der Dingus-Editor kann __Referenz-Links__ und
__Fußnoten__ für Sie erstellen, vergibt automatisch die nächste freie Nummer
und fügt die passende Definition am Ende des Dokuments an.

* __F6 (magischer Referenzlink)__: Mit markiertem Text wird die
  Auswahl als `[text][n]` umschlossen und am Ende des Dokuments eine neue
  `[n]: `-Zeile hinzugefügt, in die Sie die URL eingeben können. Zum Erstellen
  eines neuen Referenzlinks ist eine Auswahl erforderlich. Steht der Cursor
  bereits auf einem Referenzlink oder seiner Definition, springt **F6**
  zwischen Inline-Marker und Definition (oder legt die Definition an, falls sie fehlt).
* __F7 (magische Fußnote)__: Fügt an der Cursorposition---oder nach dem
  aktuellen Wort, wenn der Cursor darin steht---einen nummerierten Fußnotenmarker
  `[^n]` ein und hängt `[^n]: ` an; bei markiertem Text wird der markierte Text
  als Fußnotentext verwendet. Steht der Cursor auf einem vorhandenen Fußnotenmarker
  oder einer Definition, springt **F7** zwischen beiden.

Referenz- und Fußnotennummern werden automatisch vergeben, sodass Sie keine IDs
von Hand verwalten müssen. Beide Shortcuts funktionieren nicht
in abgegrenzten oder eingerückten Codeblöcken.

### Intelligentes URL-Einfügen

Beim Einfügen enthält die Zwischenablage eine URL des Formulars
`protocol://...` ohne Leerzeichen:

* __Mit einer Auswahl__: Die Auswahl wird in eine umgewandelt
  Markdown Link: `[selected text](url)` .
* __Ohne Auswahl__: Die URL wird als eingefügt
  Selbstverlinkung: `<url>` .

Dadurch ist es einfach, kopierte URLs in Links umzuwandeln
manuelle Eingabe.

### Intelligente Auswahl (⌥⌘ ↑ / ⌥⌘↓)

Der Dingus-Editor unterstützt die __semantische Auswahlerweiterung__:

* __⌥⌘ ↑__ beginnt beim Caretzeichen und erweitert die Auswahl
  durch:
	- das aktuelle Wort
	- Innen und außen abgegrenzter Inhalt (Anführungszeichen, Klammern,
   Klammern und umzäunte Codeblöcke)
	- der aktuelle Satz
	- der aktuelle Absatz
	- der zusammenhängende, nicht leere Zeilenblock (z. B. a
   ganze Tabelle oder mehrzeiliger Codeblock ohne Leerzeilen)
	– das umschließende Listenelement, Blockzitat oder Codeblock
	- das gesamte Dokument
* __⌥⌘↓__ geht durch die gleichen Ebenen zurück, bis es
  kehrt zur ursprünglichen Caret-Position zurück.

Jeder Druck bewegt sich immer zu einem strikt größeren oder kleineren Wert
Auswahl, sodass Sie währenddessen nie „No-Op“-Tastendrücke erhalten
erweitern oder verkleinern.

## Verwendung des Dingus als Editor

Der Dingus ist nicht dazu gedacht, einen vollständigen Text zu ersetzen
Editor, aber es kann sehr praktisch für __schnelle Bearbeitungen mit einem sein
Live-Vorschau__, insbesondere wenn Sie genau sehen möchten, wie
Änderungen werden gerendert. Das gesamte Textbearbeitungsverhalten
Hier gilt die Beschreibung in [Editing in the Dingus][3].

### Eine Datei öffnen/eine neue Datei erstellen

* __Erstellen Sie eine neue Datei im Dingus__
	- Wählen Sie __{% appmenu File, New, New Markdown File %}__
   (⌘N).
	- Wenn Sie dazu aufgefordert werden, wählen Sie __Dingus__, um eine neue, nicht gespeicherte Datei zu starten
   Dingus Dokument.
	– Neue Dingus-Dokumente werden mit ausgewählten Beispielinhalten geöffnet;
   Beginnen Sie einfach mit der Eingabe, um es zu ersetzen.
* __Öffnen Sie eine vorhandene Datei im Dingus__
	- Verwenden Sie __{% appmenu File, Open in Dingus... %}__ (⌥⌘O) oder
   Klicken Sie bei aktivem Fenster Dingus im Status auf __Öffnen…__
   Bar. Der Befehl öffnet dann bei Bedarf das Fenster Dingus
   zeigt das Fenster „Öffnen“ an.
	- Wählen Sie eine unterstützte Klartext-/Markdown-Datei aus. Es ist
   Der Inhalt ersetzt den aktuellen Dingus-Puffer.
* __Öffnen Sie ein Marked-Vorschaudokument im Dingus__
	- Verwenden Sie in einem normalen Vorschaufenster __{% appmenu Preview,
   Open in Dingus %}__ (⌥⌘E).
	- Der Markdown des aktuellen Dokuments wird in den Dingus geladen.
   So können Sie experimentieren, ohne die Originaldatei anzufassen
   bis Sie sich zum Speichern entscheiden. Custom Regeln werden nicht angewendet in
   der Dingus; siehe [Custom Rules do not apply](#custom-rules-do-not-apply).

### Eine Datei speichern

* __Änderungen an der aktuellen Datei speichern__
	- Klicken Sie im Fenster Dingus in der Statusleiste auf __Speichern.
   oder nutzen
    __{% appmenu File, Save Dingus %}__ (⌘S).
	- Wenn das Dokument Dingus noch nicht gespeichert wurde, werden Sie es tun
   wird zur Eingabe eines Speicherorts und Dateinamens aufgefordert; danach ⌘S
   aktualisiert die gleiche Datei.
* __Speichern unter / in eine neue Datei duplizieren__
	- Verwenden Sie __{% appmenu File, Save Dingus As... %}__ (⌥⌘S).
	– Dies öffnet immer ein __Speichern unter__-Dialogfeld und schreibt das
   aktuellen Dingus-Inhalt in eine neue Datei kopieren, ohne ihn zu überschreiben
   das Original.

### Vorschau in Marked

* __Öffnen Sie das Dingus-Dokument als vollständige Marked-Vorschau__
	- Klicken Sie in der Statusleiste von Dingus auf __In Marked__ öffnen oder verwenden Sie

__{% appmenu File, Open Dingus in Marked %}__ (⌘P).
	- Wenn das Dokument Dingus nicht gespeichert ist oder nicht gespeicherte Änderungen aufweist,
   Sie werden zunächst zum Speichern aufgefordert. dann öffnet Marked a
   Standardvorschau für diese Datei.

Mit diesen Befehlen können Sie Dingus als behandeln
Leichter Editor für schnelle Korrekturen und Experimente
Wechseln Sie zu einer vollständigen Marked-Vorschau oder zu Ihrem regulären Editor, wenn
Sie sind bereit für eine umfangreichere Bearbeitung.

## Prozessorauswahl

Verwenden Sie das Dropdown-Menü oben, um zwischen verschiedenen zu wechseln
Markdown Prozessoren:

* __MultiMarkdown__: Voll ausgestatteter Prozessor mit Tabellen,
  Fußnoten und mathematische Unterstützung
* __CommonMark (GFM)__: Standardmäßiger, schneller Prozessor nach dem
  CommonMark-Spezifikation
* __Rabatt__: GitHub Aromatisiert Markdown mit Aufgabe
  Listen und Tabellen
* __Kramdown__: Fortschrittlicher Prozessor mit zusätzlichen Funktionen
  wie IALs und Typografie

## Warum den Dingus verwenden?

### Prozessorunterschiede verstehen

Verschiedene Markdown-Prozessoren handhaben die Syntax unterschiedlich. Die
Dingus hilft Ihnen:

* __Ausgabe vergleichen__: Sehen Sie genau, wie jeder Prozessor rendert
  das gleiche Markdown
* __Debug-Probleme__: Identifizieren Sie, warum bei einer bestimmten Syntax dies nicht der Fall ist
  Funktioniert wie erwartet
* __Syntax lernen__: Verstehen Sie die subtilen Unterschiede
  zwischen Prozessorimplementierungen

### Testen vor dem Schreiben

Bevor Sie sich in Ihrem Markdown auf einen bestimmten Stil festlegen
Dokumente:

* __Validate Syntax__: Stellen Sie sicher, dass Ihr Markdown gerendert wird
  richtig
* __Prozessoren auswählen__: Entscheiden Sie, welcher Prozessor am besten funktioniert
  für Ihre Inhalte
* __Experimentieren Sie sicher__: Probieren Sie neue Syntax aus, ohne sie zu beeinträchtigen
  Ihre tatsächlichen Dokumente

## Häufige Anwendungsfälle

### Unterschiede in der Tabellensyntax

Einige Prozessoren handhaben die Tabellensyntax anders. Der Dingus
Hier können Sie sehen, welcher Prozessor Ihren Tisch am besten unterstützt
Formatierungsanforderungen.

### Fußnotenunterstützung

Nicht alle Prozessoren unterstützen Fußnoten. Verwenden Sie den Dingus, um
Überprüfen Sie, ob die Fußnotensyntax mit dem von Ihnen gewählten Prozessor funktioniert.

### Mathematik und Sonderzeichen

Testen Sie, wie verschiedene Prozessoren mit Mathematik umgehen
Ausdrücke und spezielle typografische Zeichen.

## Tipps für den effektiven Einsatz

1. __Einfach beginnen__: Beginnen Sie mit dem einfachen Markdown und schrittweise
   Komplexität hinzufügen
2. __Edgefälle testen__: Probieren Sie ungewöhnliche Syntaxkombinationen aus
   Prozessorgrenzen verstehen
3. __Nebeneinander vergleichen__: Wechseln Sie zwischen Prozessoren zu
   Unterschiede klar erkennen
4. __Verwenden Sie echte Inhalte__: Kopieren Sie tatsächliche Inhalte von Ihrem
   Dokumente zum Testen realer Szenarien

Der Dingus ist ein leistungsstarkes Tool für jeden, der es möchte
die Nuancen verschiedener Markdown-Implementierungen verstehen
und stellen Sie sicher, dass ihre Inhalte in verschiedenen Bereichen korrekt gerendert werden
Plattformen und Prozessoren.

[1]: images/dingus-interface-800.jpg @2x width=800px height=573px class=center
[2]: x-marked-3://dingus
[3]: #editing-in-the-dingus

