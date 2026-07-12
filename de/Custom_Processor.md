# <%= @title %>

Mit Eigenen Regeln, Texttransformationen und der Möglichkeit, eigene Befehle auszuführen oder je nach passenden Dateieigenschaften unterschiedliche Prozessoren zu verwenden, gibt Ihnen Marked die volle Kontrolle.

## Eigene Präprozessoren/Prozessoren verwenden

Um benutzerdefinierte Prozessoren hinzuzufügen, öffnen Sie {% prefspane Processor %} und klicken auf **Eigene Regeln**.

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800

Im Editor für Eigene Regeln (auch „Conductor“ genannt) legen Sie Regeln mit Kriterien an, die Dateien anhand von Dateiname, Pfad, Übereinstimmungen im Inhalt, Metadaten und sogar daran abgleichen, ob im selben Verzeichnisbaum wie das geöffnete Dokument weitere Dateien liegen. Trifft eine Regel zu, werden die für sie definierten Aktionen auf diese Datei angewendet.

> Unterhalb des Felds „Prozessor“ legen die Kontrollkästchen unter „Neue Dokumente verwenden eigene:“ fest, ob Regeln für die Präprozessor- und Prozessorphase überhaupt geprüft werden. Lassen Sie diese in der Regel aktiviert; wenn Sie aber alle benutzerdefinierten Prozessoren vollständig übergehen wollen, stellen Sie das hier ein.

![Editor für Eigene Regeln][2]

  [2]: images/CustomRules-800.jpg @2x width=800

Um eine neue Regel zu erstellen, verwenden Sie die Schaltfläche `+` unten in der Regelliste auf der linken Seite. Geben Sie der Regel einen Namen und legen Sie sie als Präprozessor oder Prozessor fest.

Die drei Punkte neben einer Regel stehen für ihren Status „Präprozessor“, „Prozessor“ und „Aktiviert“. Für jede Regel kann entweder „Präprozessor“ oder „Prozessor“ ausgewählt sein. Klicken Sie auf die Punkte, um den Status der Regel zu ändern.

Präprozessor
: Wird ausgeführt, nachdem die Datei zunächst verarbeitet wurde – also nachdem Marked eingebundene Dateien hinzugefügt, Stileinstellungen wie GitHub-Zeilenumbrüche verarbeitet hat usw. –, aber vor der Verarbeitungsphase. Das Dokument liegt zu diesem Zeitpunkt noch als rohes Markdown vor, und Sie können den Inhalt ändern, der an den Prozessor übergeben wird. Trifft kein benutzerdefinierter Prozessor zu oder wird in einem zutreffenden benutzerdefinierten Prozessor keine Aktion **Prozessor ausführen** ausgeführt, kommt der Standardprozessor zum Einsatz.

Prozessor
: Ein benutzerdefinierter Prozessor ersetzt den unter {% prefspane Processor %} festgelegten integrierten Prozessor. Er kann alles, was ein Präprozessor kann, und ergänzt die Aktionen **Befehl ausführen** und **Prozessor ausführen**. Damit können Sie einen eigenen Befehl ausführen, etwa Pandoc, oder für Dateien, die den Kriterien entsprechen, einen anderen integrierten Prozessor verwenden.

Alle Tabellen im Editor für Eigene Regeln lassen sich per Drag-and-drop umsortieren. So beeinflussen Sie die Reihenfolge, in der Regeln ausgeführt werden, die Reihenfolge der Kriterien im Prädikat-Editor und die Reihenfolge der nacheinander auszuführenden Aktionen.

### Prädikat-Editor

![Prädikat-Editor][predicate]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

Sobald eine Regel hinzugefügt ist, definieren Sie im Prädikat-Editor die Kriterien, die bestimmen, ob die Regel für eine bestimmte Datei ausgeführt wird. Wählen Sie über das Dropdown-Menü auf der linken Seite ein Kriterium und bauen Sie das Prädikat dann mit den Feldern für Vergleichsoperator und Wert.

- _Dateiname_ vergleicht nur den Dateinamen der Datei
- _Erweiterung_ vergleicht nur die Erweiterung der Datei
- _Pfad_ vergleicht den vollständigen POSIX-Pfad (Unix) der Datei
- _Baum_ sucht irgendwo im Verzeichnisbaum der Datei nach passenden Dateinamen
- _Text_ vergleicht den Textinhalt der Datei. Setzen Sie den Textwert in Schrägstriche, um daraus eine Suche mit regulärem Ausdruck zu machen.
- _Datei enthält_ prüft, ob die Datei eingebundene Dateien enthält (über eine von [Markeds Einbinde-Syntaxen](Multi-File_Documents.html)).
- _Metadatentyp_ prüft, ob die Datei YAML-, MultiMarkdown- oder Pandoc-Metadaten enthält
- _Metadaten:_-Felder (zum Beispiel _Metadaten: Author_, _Metadaten: Date_, _Metadaten: Title_) prüfen auf bestimmte Metadatenschlüssel. Jeder Metadatenschlüssel erscheint im Dropdown-Menü als _Metadaten:_ gefolgt vom Feldnamen.
- _Manuell aktiviert_ trifft zu, wenn die Regel für das aktuelle Vorschaufenster eingeschaltet wurde (siehe [Manuell aktivierte Regeln](#manuallyenabled) unten). Kombinieren Sie es mit anderen Kriterien in einer Alle-(UND)-Gruppe, damit die Regel nur läuft, wenn Sie sie einschalten _und_ die Datei Ihren übrigen Bedingungen entspricht.

Um alle Dateien abzugleichen (also ein benutzerdefinierter Prozessor, der immer läuft), setzen Sie _Dateiname_ auf `enthält` `*`. Das Sternchen dient als Platzhalter und passt auf alle Dateien.

[Ein Prädikat hinzufügen][addpredicate]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

Klicken Sie auf das Pluszeichen (+) in der Prädikatzeile, um ein weiteres Prädikat hinzuzufügen. Halten Sie beim Klick auf das + die Wahltaste gedrückt, um eine boolesche Gruppe hinzuzufügen, die sich auf „Alle“ (UND) oder „Beliebige“ (ODER) setzen lässt.

### Manuell aktivierte Regeln [manuallyenabled]

Manche Regeln sollen nicht auf jeder Datei laufen, die ihren Kriterien entspricht. Fügen Sie ein Kriterium **Manuell aktiviert** hinzu, wenn eine Regel erst laufen soll, nachdem Sie sie für die aktuelle Vorschau eingeschaltet haben.

Fügen Sie dieses Kriterium über die Schaltfläche **Manuell aktiviert hinzufügen** unter dem Prädikat-Editor ein. Jede Regel kann es nur einmal enthalten. Ist es vorhanden, erscheint die Regel im Untermenü {% appmenu Vorschau, Eigene Regel aktivieren %} für dieses Vorschaufenster.

**Beispiel:** Sie pflegen eine Regel, die Druck-CSS einfügt, Kommentare entfernt und die Überschriftenebenen für den PDF-Export verschiebt. Diese Transformation soll nicht bei jedem Speichern während des Schreibens greifen, sondern nur auf Abruf. Geben Sie der Regel die normalen Dateiabgleich-Kriterien plus **Manuell aktiviert** und schalten Sie sie dann über das Vorschau-Menü (oder einen Auslöser-Kurzbefehl) ein, wenn Sie das Drucklayout prüfen wollen.

#### Auslöser-Kurzbefehl

Enthält eine ausgewählte Regel **Manuell aktiviert**, erscheint neben **Manuell aktiviert hinzufügen** das Feld **Auslöser-Kurzbefehl**. Klicken Sie auf den Rekorder und drücken Sie dann die gewünschte Tastenkombination. Dieser Kurzbefehl schaltet die Regel für die vorderste Marked-Vorschau um (ein, wenn aus; aus, wenn ein). Der Kurzbefehl wird mit der Regel gespeichert und bleibt über Neustarts hinweg erhalten. Leeren Sie das Feld, um den Kurzbefehl zu entfernen.

![Rekorder für den Auslöser-Kurzbefehl im Conductor][manualshortcut]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### Überschreibungen pro Vorschau im Vorschau-Menü

Zwei Untermenüs des Vorschau-Menüs steuern Überschreibungen nur für die aktive Vorschau. Zeigen mehrere Fenster dieselbe Datei, werden die Einstellungen pro [Ansicht](#multiview) gespeichert.

**Eigene Regel aktivieren**
: Listet jede aktivierte Regel auf, die ein Kriterium **Manuell aktiviert** enthält. Setzen Sie bei einer Regel das Häkchen, um sie für diese Vorschau einzuschalten; entfernen Sie es, um sie auszuschalten. Die Vorschau aktualisiert sich sofort.

**Eigene-Regel-Überschreibung**
: Listet die Regeln der Prozessphase auf. Wählen Sie eine aus, um sie *anzuheften*: Während der Prozessphase wird dann nur diese Regel ausgewertet (andere Prozessregeln werden übersprungen). Wählen Sie **Keine (automatisch)**, um zum normalen Regelabgleich zurückzukehren. Das ist nützlich, wenn Sie für eine Vorschau eine bestimmte Prozessor-Pipeline erzwingen wollen, ohne die globalen Eigenen Regeln zu ändern.

#### Überschreiben-Schaltfläche in der Vorschau-Symbolleiste

Sobald eine Vorschau mindestens eine manuell aktivierte Regel oder eine angeheftete Prozess-Überschreibung hat, erscheint in der unteren Symbolleiste ein Verzweigungssymbol (links neben den Steuerelementen für Export und Drawer). Das gefüllte, in der Akzentfarbe eingefärbte Symbol bedeutet, dass Überschreibungen aktiv sind; das Umriss-Symbol bedeutet, dass sie ausgesetzt sind.

![Überschreiben-Schaltfläche für Eigene Regeln in der Vorschau-Symbolleiste][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

Klicken Sie auf die Schaltfläche, um die Überschreibungen für diese Vorschau auszusetzen oder wieder zu aktivieren, ohne dabei die Häkchen Ihrer manuell aktivierten Regeln oder die angeheftete Prozessregel zu verlieren. Ausgesetzte Überschreibungen werden beim erneuten Klick wiederhergestellt. Das geht schneller, als Regeln im Menü abzuwählen, wenn Sie die normale Vorschau mit Ihrer Überschreibungs-Pipeline vergleichen wollen.

### Aktionen

Fügen Sie der Regel über die Schaltfläche *+ Aktion* Aktionen hinzu.

![Eine Aktion hinzufügen][addaction]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

Verfügbar sind unter anderem diese Aktionen:

Stil festlegen
: Legt den Stil für die Vorschau fest. Jeder integrierte Stil und jeder von Ihnen hinzugefügte Eigene Stil steht zur Auswahl.

Befehl ausführen
: Nimmt einen Befehlszeilenbefehl samt aller Argumente entgegen und übergibt den Inhalt der Datei über STDIN. Der Befehl sollte das Ergebnis über STDOUT zurückgeben.

> **Sandboxing im Mac App Store**: Die Mac-App-Store-Version (MAS) von Marked läuft in einer Sandbox-Umgebung, die das Ausführen externer Binärdateien einschränkt. Wenn Sie in der MAS-Version externe Prozessoren wie Pandoc nutzen müssen, kopieren Sie die Binärdatei in das App-Bundle. Und zwar so:
>
> 1. Rechtsklick auf Marked.app → Paketinhalt zeigen
> 2. Zu `Contents/Resources/` navigieren
> 3. Einen Ordner `bin` erstellen, falls noch nicht vorhanden
> 4. Ihre Binärdatei (z. B. `pandoc`) in diesen `bin`-Ordner kopieren
> 5. Sie ausführbar machen: `chmod +x` auf die Binärdatei anwenden
> 6. In der Aktion „Befehl ausführen“ so darauf verweisen:
>
>     `IHR_BINARY_NAME [Argumente]`
>     Oder den vollständigen Pfad verwenden:
>     `/Applications/Marked.app/Contents/Resources/bin/IHR_BINARY_NAME [Argumente]`
>
> **Hinweis**: Skripte mit externen Shebangs (etwa Python-Skripte, die auf `/opt/homebrew/bin/python` verweisen) werden beim Kopieren in das Bundle automatisch über die System-Interpreter ausgeführt. Die MAS-Version hat unter Umständen weiterhin Probleme, Binärdateien auszuführen, die eigentlich Python- oder Ruby-Skripte statt echter Binärdateien sind.
> Nach jedem App-Update müssen Sie die Binärdateien erneut kopieren, da Updates das gesamte Bundle ersetzen. Alternativ nutzen Sie **Hilfe → Crossgrade**, um auf die Version von Marked zu wechseln, die keine solchen Einschränkungen hat.

Eingebettetes Skript ausführen
: Bearbeiten Sie ein vollständiges Skript im integrierten Code-Editor. Wie **Befehl ausführen** sollte es Eingaben über STDIN entgegennehmen und Ausgaben über STDOUT zurückgeben.

Metadaten festlegen
: Fügt Metadaten hinzu oder setzt sie. Geben Sie einen Schlüssel und einen Wert an. Existiert der Schlüssel, wird sein Wert aktualisiert, andernfalls wird er hinzugefügt. Der verwendete Metadatentyp wird automatisch anhand des Dateiinhalts bestimmt (oder anhand des Ergebnisses einer Metadaten-Konvertierungsaktion).
: Sind keine Metadaten vorhanden, werden die Metadaten im MultiMarkdown-Format innerhalb eines HTML-Kommentars hinzugefügt. Marked kann diese Metadaten lesen, sie erscheinen aber in keiner Vorschau, unabhängig vom verwendeten Prozessor.

Metadaten löschen
: Löscht einen Metadateneintrag anhand seines Schlüssels.

Metadaten entfernen
: Löscht alle Metadaten. Betrifft YAML-, MultiMarkdown- und Pandoc-Metadaten.

YAML-Metadaten in MMD konvertieren
: Wandelt einen YAML-Metadatenblock am Anfang der Datei in Metadaten im MultiMarkdown-Stil um.

MMD-Metadaten in YAML konvertieren
: Wandelt einen MultiMarkdown-Metadatenblock in YAML um.

Suchen und Ersetzen
: Führt ein Suchen und Ersetzen im Inhalt der Datei durch.
: Ist die Suchzeichenkette von Schrägstrichen umschlossen (z. B. `/Project \w+/`), wird sie als regulärer Ausdruck behandelt. Mit `$1`, `$2` usw. nehmen Sie Übereinstimmungsgruppen in die Ersetzung auf.
: Das Ersetzungsfeld unterstützt einige Escape-Sequenzen (ein Backslash gefolgt von): `\n` fügt einen Zeilenumbruch ein, `\t` ein Tabulatorzeichen, `\\` einen wörtlichen Backslash, `\$` ein wörtliches Dollarzeichen (statt einer Übereinstimmungsgruppe).
: Jede andere `\X`-Sequenz wird als bloßes `X` behandelt (der Backslash entfällt), aus `\e` wird also `e`. Ein abschließender `\` ohne folgendes Zeichen bleibt als wörtlicher Backslash erhalten.
: Verwenden Sie `[%key]` in der Ersetzung, um einen Wert aus Dokumentmetadaten, Umgebungsvariablen oder Kontext einzufügen (z. B. `[%title]`, `[%MARKED_PATH]`). Schlüssel, die frühere Aktionen derselben Regel oder eine vorhergehende Regel gesetzt haben, stehen zur Verfügung. Nicht gefundene Schlüssel werden durch eine leere Zeichenkette ersetzt.

Titel H1 einfügen
: Fügt ein H1 in das Dokument ein. Es kann entweder aus Metadaten oder aus dem Dateinamen stammen.

Überschriften verschieben
: Passt die Überschriftenebenen von -5 bis +5 an. Setzen Sie dies etwa auf -1, werden alle H1 zu H2, H2 zu H3 usw. Eine positive Zahl hebt die Überschriftenebenen um diesen Betrag an.

Überschriften normalisieren
: Diese Aktion stellt nach Möglichkeit sicher, dass es nur ein H1 im Dokument gibt, und passt alle Überschriftenebenen so an, dass sie in semantischer Reihenfolge stehen und keine Ebenen überspringen, z. B. von H2 direkt zu H4. Ist das Originaldokument schon einigermaßen semantisch geordnet, verfeinert dies die Hierarchie.

Inhaltsverzeichnis einfügen
: Fügt ein Inhaltsverzeichnis ein. Es kann nach dem ersten H1, dem ersten H2 oder am Anfang der Datei stehen (wird dann nach etwaigen Metadaten eingefügt).

Datei einfügen
: Fügt eine ausgewählte Textdatei an einer bestimmten Stelle im Dokument ein. Das kann nach dem ersten H1, nach dem ersten H2, oben, unten oder nach einer Textübereinstimmung sein (verwenden Sie `/pattern/`, um nach einem regulären Ausdruck zu suchen).

Text einfügen
: Bietet einen Popup-Editor, mit dem Sie Text direkt in die Aktion einbetten. Die Positionierungsoptionen sind dieselben wie bei _Datei einfügen_.
: Verwenden Sie `[%key]` an beliebiger Stelle im eingefügten Text, um Werte aus Dokumentmetadaten, Umgebungsvariablen oder dem Marked-Kontext abzurufen (z. B. `[%author]`, `[%MARKED_PATH]`). Das funktioniert unabhängig vom verwendeten Prozessor, Sie brauchen für die Metadaten-Ersetzung also kein MultiMarkdown. Werte aus früheren Aktionen derselben Regel (etwa **Metadaten festlegen**) oder aus einer vorhergehenden Regel werden einbezogen. Nicht gefundene Schlüssel werden durch eine leere Zeichenkette ersetzt.

CSS-Datei einfügen
: Fügt eine ausgewählte CSS-Datei in das Dokument ein. Sie wird nach jeder Stilauswahl geladen und lässt sich verwenden, um vorhandene Stile zu überschreiben oder neue hinzuzufügen.

CSS einfügen
: Bietet einen Popup-CSS-Editor, in dem Sie eigenes CSS direkt zur Aktion hinzufügen. Dieses CSS wird am Anfang des Dokuments nach allen vorhandenen Stilen eingefügt. Die Reihenfolge der eingefügten Stile entspricht der Reihenfolge der Aktionen in der Regel.

JavaScript-Datei einfügen
: Fügt eine ausgewählte JavaScript-Datei am Ende des Dokuments ein. Beachten Sie: Damit das Skript bei jeder Aktualisierung neu geladen wird, brauchen Sie eine Aktion *JavaScript einfügen* mit einem [Update-Hook](#updatehook).

JavaScript von URL einfügen
: Fügt am Ende des Dokuments ein `<script>`-Tag ein, das mit einem CDN oder einer anderen entfernten URL verknüpft ist. Beachten Sie: Damit das Skript bei jeder Aktualisierung neu geladen wird, brauchen Sie eine Aktion *JavaScript einfügen* mit einem [Update-Hook](#updatehook).

JavaScript einfügen
: Bietet einen Popup-JavaScript-Editor, mit dem Sie eigenes JavaScript direkt in die Aktion einbetten. Es wird am Ende des Dokuments eingefügt; die Reihenfolge, in der die Regel das JavaScript ausführt, ergibt sich aus der Reihenfolge der Aktionen, wobei die zuletzt hinzugefügte Aktion zuletzt läuft.
: Beachten Sie: Damit Skripte bei jeder Aktualisierung laufen, brauchen Sie einen [Update-Hook](#updatehook).

URLs selbst verlinken
: Wandelt alle blanken URLs in `<url>` um, was in jedem Prozessor einen Hyperlink erzeugt.

Kurzbefehl ausführen
: Führt einen Apple-Kurzbefehl aus. Jeder ausgeführte Kurzbefehl sollte die Eingabe über STDIN entgegennehmen und am Ende eine Ausgabe zurückgeben (Stoppen und Ausgabe zurückgeben). Wenn Sie Aktionen ausführen möchten, die den Text nicht verändern, weisen Sie die Eingabe einer Variablen zu, führen Ihre Aktionen aus und geben am Ende die ursprüngliche Textvariable aus.

Systemdienst ausführen
: Führt einen beliebigen Systemdienst aus `~/Library/Services` aus. Der Dienst sollte Eingaben annehmen und Ausgaben zurückgeben.

Automator-Workflow ausführen
: Führt eine beliebige Automator-Datei `.workflow` aus. Die Eingabe wird über STDIN übergeben, die Ausgabe wird über STDOUT erwartet.

Regel ausführen
: Ruft aus der aktuellen Regel heraus die Aktionen einer anderen Eigenen Regel auf. Wählen Sie die Zielregel im Popup. Die aufgerufene Regel läuft in derselben Phase (Präprozessor oder Prozess), ohne ihr Prädikat erneut auszuwerten, das macht sie für wiederverwendbare „Zutaten“-Regeln nützlich.

  **Beispiel:** Definieren Sie eine kleine Regel namens „HTML-Kommentare entfernen“ mit einer Aktion **Suchen und Ersetzen** und geben Sie ihr ein Kriterium **Manuell aktiviert**, damit sie nie automatisch läuft. Fügen Sie in Ihrer Hauptregel zur Buchverarbeitung nacheinander mehrere **Regel ausführen**-Aktionen ein: zuerst „Überschriften normalisieren“, dann „HTML-Kommentare entfernen“, dann einen Befehl, der Pandoc aufruft. So bleibt jeder Schritt wartbar, ohne Aktionen über Regeln hinweg zu duplizieren.

  **Verschachtelung:** Eine über **Regel ausführen** aufgerufene Regel kann keine weitere Regel aufrufen. Enthält die Zielregel eine **Regel ausführen**-Aktion, wird diese Aktion übersprungen; alle anderen Aktionen der Zielregel laufen weiterhin. Sie können einer einzelnen Regel mehrere **Regel ausführen**-Aktionen hinzufügen; sie werden der Reihe nach ausgeführt.

  Eine Regel kann sich nicht selbst aufrufen, und Marked erkennt Zyklen (etwa: Regel A ruft Regel B auf, die wiederum Regel A aufruft) und überspringt den verschachtelten Aufruf. Meldungen zu übersprungenen Aufrufen finden Sie im [Protokoll eigener Regeln](#customprocessorlog).

Fortfahren
: Standardmäßig endet die Verarbeitung, sobald eine Regel zutrifft (getrennt für Präprozessoren und Prozessoren, sodass je ein Präprozessor und ein Prozessor zutreffen können). Diese Aktion erzwingt, dass der Regelabgleich fortgesetzt wird, nachdem die Regel ihre Aktionen ausgeführt hat.

### Update-Hook [updatehook]

Marked führt nicht bei jeder Aktualisierung eine vollständige Neudarstellung durch. Wenn Sie also Skripte haben, die Teile des DOM neu rendern sollen, müssen diese ihre Render-Funktion über Markeds Hook-API ausführen.

Das folgende Beispiel verwendet Mermaid, was Sie eigentlich nie tun müssen, da Mermaid inzwischen standardmäßig enthalten ist. So würden Sie aber vorgehen, wenn Sie es manuell einbinden würden.

Fügen Sie eine Aktion **JavaScript einfügen** hinzu und initialisieren Sie im Fenster „JS bearbeiten“ das Skript, dann fügen Sie den Hook hinzu:

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

Dadurch wird `mermaid.run()` jedes Mal ausgeführt, wenn Marked eine Teilaktualisierung durchführt.

### Regeln testen

Die Schaltfläche _Regeln testen_ unter der Regelliste öffnet einen Dialog, in dem Sie eine beliebige Markdown-Datei auswählen können; sie wird dann gegen alle Ihre Regeln getestet. Zutreffende Regeln werden auf der linken Seite mit einer grünen Markierung hervorgehoben. Beim Test gegen eine Datei erscheint neben dem Button eine rote X-Schaltfläche, mit der Sie den Test zurücksetzen und die Hervorhebung der Zeilen entfernen können.

## Drag-and-drop

Das Conductor-Fenster unterstützt erweitertes Drag-and-drop: Es erkennt Dateitypen intelligent und bietet je nach gezogener Datei passende Aktionen an. Für Textdateien gibt es ein geteiltes Overlay, mit dem Sie wählen können, ob Sie die Datei gegen die Regeln testen oder sie als Aktion hinzufügen.

![Drag-and-drop bei Eigenen Regeln][drag]

[drag]: images/draganddropconductor.jpg @2x width=800

### Dateityperkennung

Das System erkennt verschiedene Dateitypen automatisch und zeigt passende Overlay-Meldungen an:

- **CSS-Dateien** (`.css`): zeigt das Overlay „CSS-Datei einfügen“
- **JavaScript-Dateien** (`.js`, `.javascript`): zeigt das Overlay „JS-Datei einfügen“
- **Skriptdateien** (jede ausführbare Datei): zeigt das Overlay „Befehl ausführen“
- **Textdateien**: zeigen das geteilte Overlay
- **Ausführbare Dateien**: zeigen das Overlay „Befehl ausführen“
- **Unbekannte Erweiterungen**: fallen auf den Typ „Text“ zurück und zeigen das geteilte Overlay

## Protokoll eigener Regeln [customprocessorlog]

Wenn Sie merkwürdige Ergebnisse erhalten und sehen möchten, was vor sich geht, zeigt Ihnen das Protokoll eigener Regeln, welche Regeln in welcher Reihenfolge laufen. Öffnen Sie es über **Hilfe → Protokoll eigener Regeln anzeigen**. Auch aufgerufene **Regel ausführen**-Aktionen und übersprungene verschachtelte Aufrufe werden hier protokolliert.

![Protokoll eigener Regeln][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## Mehrere Befehle ausführen

Eine Regel kann mehrere **Befehl ausführen**-Aktionen nacheinander enthalten. Die Ausgabe jedes Befehls wird an den nächsten übergeben. Soll ein Befehl etwas ausgeben und gleichzeitig Markeds Vorschau aktualisiert werden, geben Sie unbedingt den ursprünglichen Inhalt an STDOUT zurück, damit der nächste Befehl oder der integrierte Prozessor ihn verarbeiten kann.

Wenn Sie zum Beispiel mit einem Befehl über Pandoc ein PDF-Dokument aktualisieren möchten, übergeben Sie einfach den ursprünglichen Dateipfad (aus den Umgebungsvariablen) mit den passenden Befehlszeilenoptionen an Pandoc und geben dann den STDIN-Inhalt wieder an STDOUT aus.

## Benutzerdefinierte Prozessoren dynamisch umgehen

Gibt ein benutzerdefinierter Prozessor „NOCUSTOM“ über STDOUT zurück, beendet Marked den benutzerdefinierten Prozessor und fällt auf den internen Standardprozessor zurück. So können Sie einen benutzerdefinierten Prozessor bauen, der anhand der [Umgebungsvariablen](#environmentvariables), des Dateinamens oder der Erweiterung des Dokuments, einer Inhaltsübereinstimmung oder anderer Logik selbst entscheidet, ob er laufen soll.

Gibt ein benutzerdefinierter Prozessor statt `NOCUSTOM` den Wert `MULTIMARKDOWN` oder `DISCOUNT` (oder `GFM`), `KRAMDOWN` oder `COMMONMARK` zurück, wird nur für dieses Dokument der entsprechende interne Prozessor verwendet. Diese Änderung wirkt sich nicht auf den in den Einstellungen festgelegten Standardprozessor aus.

## Umgebungsvariablen [environmentvariables]

Die Aktion **Befehl ausführen** hat einen Umgebungseditor, in dem Sie eigene Umgebungsvariablen setzen können, die dem Befehl oder Skript zur Verfügung stehen. Neben diesen eigenen Variablen bringt Marked einige eigene mit.

Marked führt den benutzerdefinierten Prozessor in einer eigenen Shell aus, das heißt, Standard-Umgebungsvariablen werden nicht automatisch übergeben. Sie können Markeds Umgebungsvariablen nutzen, um Ihre eigenen in Ihren Skripten zu ergänzen. Marked stellt folgende Variablen für Ihre Shell-Skripte bereit:

**MARKED_ORIGIN**
: Der Speicherort (Basisverzeichnis) Ihrer primären Arbeitsdatei (der Ordner des Arbeitstexts, der Scrivener- oder Indexdatei).

**PATH**
: Marked setzt einen Pfad, der die Standard-Ordner für ausführbare Dateien enthält, und hängt das oben genannte Verzeichnis aus `MARKED_ORIGIN` an. Die Standardwerte sind: `/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`. Sie können eigene ergänzen, indem Sie die Variable PATH nach Bedarf setzen und Markeds Pfad anhängen oder überschreiben (z. B. `PATH=/usr/local/yourfolder:$PATH`).

**HOME**
: Das Home-Verzeichnis des angemeldeten Benutzers. Python und andere Skripte, die auf die gesetzte HOME-Variable angewiesen sind, übernehmen dies automatisch; sie steht aber auch für andere Zwecke in Ihren Skripten zur Verfügung.

**MARKED_EXT**
: Die Erweiterung der primären Datei, die verarbeitet wird. Mit dieser Variable können Sie je nach Dateityp unterschiedliche Abläufe skripten. Beispiel: Wenn `$MARKED_EXT == "md"`, führen Sie Ihren bevorzugten Markdown-Prozessor aus; wenn `$MARKED_EXT == "textile"`, führen Sie einen Textile-Prozessor aus.

**MARKED_PATH**
: Der vollständige UNIX-Pfad zur Hauptdatei, die zum Ladezeitpunkt in Marked geöffnet ist.

**MARKED_INCLUDES**
: Eine in Anführungszeichen gesetzte, durch Kommas getrennte Liste der Dateien, die Marked über die verschiedenen [Einbinde-Syntaxen](Special_Syntax.html#pagebreaks) in den übergebenen Text eingefügt hat.

**MARKED_PHASE**
: Wird entweder auf „PROCESS“ oder „PREPROCESS“ gesetzt, sodass Sie mit einem einzigen Skript beide Phasen anhand dieser Variable abwickeln können.

**MARKED_CSS_PATH**
: Der vollständige Pfad zum aktuellen Stylesheet.

### Metadaten-Umgebungsvariablen

Wird die Aktion **Befehl ausführen** in Markeds Conductor-System ausgeführt, werden die Dokumentmetadaten automatisch extrahiert und dem Befehl als Umgebungsvariablen bereitgestellt.

#### So funktioniert es

1. **Metadatenextraktion**: Das System extrahiert Metadaten aus dem Dokument über die vorhandene Methode `extractMetaDataFromString:`, die Folgendes unterstützt:
   - YAML-Front-Matter (`---`-Blöcke)
   - MultiMarkdown-Metadaten (`Schlüssel: Wert`-Zeilen)
   - Pandoc-Metadaten (`%`-Titelblöcke)
   - HTML-Kommentar-Metadaten (`<!-- key: value -->`)

2. **Schlüsselnormalisierung**: Metadatenschlüssel werden für die Verwendung als Umgebungsvariablen normalisiert:
   - in Kleinbuchstaben umgewandelt
   - alle nicht alphanumerischen Zeichen entfernt
   - Leerzeichen und Sonderzeichen entfernt

3. **Format der Umgebungsvariablen**: Jeder Metadatenschlüssel wird zu einer Umgebungsvariablen mit dem Präfix `MD_`:
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### Beispiel

Gegeben sei ein Dokument mit diesen Metadaten:

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

Damit stünden den Befehlen folgende Umgebungsvariablen zur Verfügung:

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### Verwendung in Befehlen

Sie können diese Umgebungsvariablen dann in Ihren **Befehl ausführen**-Aktionen verwenden:

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### Unterstützte Aktionen

Diese Funktion – Metadaten als Umgebungsvariablen – steht zur Verfügung in:

- **Befehl ausführen**-Aktionen
- **Eingebettetes Skript ausführen**-Aktionen

Die Metadaten werden automatisch aus dem Dokumentinhalt extrahiert und jedem Befehl oder Skript bereitgestellt, das über diese Aktionen läuft.

## Aktivieren und Deaktivieren

Die benutzerdefinierten Prozessoren lassen sich für einzelne Dokumente mit {% kbd opt cmd C %} ein- und ausschalten. Sie können einen Präprozessor oder Prozessor für ein Dokument auch automatisch [über Metadaten](#perdocument) am Anfang des Dokuments einschalten.

Der aktuelle Status der Prozessoren wird für jedes Dokument als Kontrollleuchte angezeigt (nur sichtbar, wenn ein Prozessor aktiv ist) – links neben den Symbolleistenelementen in der unteren rechten Symbolleiste der Vorschau.

### Präprozessor [preprocessor]

Wenn Sie Präprozessorregeln einrichten, laufen diese, nachdem Marked alle Marked-spezifischen Aufgaben erledigt hat – etwa das Einbinden externer Dokumente und Codes –, aber bevor der (interne oder benutzerdefinierte) Prozessor läuft. So haben Sie die Gelegenheit, eigene Template-Variablen zu rendern, Ersetzungen vorzunehmen oder auf beliebige andere Weise eigene Inhalte einzufügen.

Marked setzt eine Umgebungsvariable für das Arbeitsverzeichnis (`MARKED_ORIGIN`) auf das übergeordnete Verzeichnis der Datei, die in der Vorschau angezeigt wird. Damit können Sie das Arbeitsverzeichnis eines Skripts wechseln und Dateien mit Pfaden relativ zum Originaldokument einbinden. In Ruby geht das zum Beispiel so:

	Dir.chdir(ENV['MARKED_ORIGIN'])

Ist er aktiviert, lässt sich der benutzerdefinierte Präprozessor für einzelne Dokumente mit {% kbd ctrl opt cmd C %} ein- und ausschalten.

#### Prozessor/Präprozessor pro Dokument [perdocument]

Benutzerdefinierte Prozessoren lassen sich auch pro Dokument festlegen, über das Metadatenformat für [Pro-Dokument-Einstellungen](Per-Document_Settings.html).

Über [Pro-Dokument-Einstellungen](Per-Document_Settings.html) (`Custom Processor:` und `Custom Preprocessor:`) geben Sie an, ob die benutzerdefinierten Prozessoreinstellungen verwendet werden und die Standardeinstellung für ein Dokument überschrieben wird. Jeder andere Wert als „true“ oder „yes“ deaktiviert den benutzerdefinierten Prä-/Prozessor.

Beispielverwendung:

    Custom Processor: true
    Custom Preprocessor: false

Wie auf der Seite [Pro-Dokument-Einstellungen](Per-Document_Settings.html#hidingmeta) beschrieben, können Sie diese Metadaten mit HTML-Kommentarmarkierungen umgeben, um sie vor GitHub und anderen Prozessoren zu verbergen, die sie nicht aus der Ausgabe entfernen:

    <!--
    Custom Processor: true
    Custom Preprocessor: true
    -->

## Einen alternativen Markdown-Prozessor verwenden

Jede Markdown-Variante, die Sie über die Befehlszeile rendern können, lässt sich mit Marked verwenden. Sie muss Eingaben über STDIN annehmen können – dasselbe wie das „Pipen“ Ihres Markdowns auf der Befehlszeile, also `cat myfile.md | myprocessor`. Und sie muss das resultierende HTML über STDOUT zurückgeben, was jeder Prozessor, mit dem ich je gearbeitet habe, standardmäßig tut.

Ermitteln Sie mit `which YOUR_PROCESSOR` im Terminal den Pfad zur ausführbaren Datei und fügen Sie diesen in das Pfadfeld von „Befehl ausführen“ ein – oder ziehen Sie die ausführbare Datei einfach in das Fenster „Eigene Regeln“, während die Regel ausgewählt ist, zu der Sie die Aktion hinzufügen möchten.

Wenn Ihr Prozessor Argumente auf der Befehlszeile benötigt, geben Sie diese ebenfalls in das Feld ein. Manche Prozessoren brauchen Bindestriche, um über STDIN und/oder STDOUT zu funktionieren; `-o - -` signalisiert etwa häufig Eingabe von STDIN und Ausgabe an STDOUT. Einzelheiten finden Sie in der Dokumentation Ihres Prozessors.

Ich habe die Funktion „Benutzerdefinierter Prozessor“ mit Pandoc, Kramdown, marked (Discount), MultiMarkdown 6, Maruku und diversen anderen Varianten getestet.

### Eine Anmerkung zu Pandoc und Sandboxing

Pandoc (und einige andere Befehlszeilen-Tools) laufen nicht in der Mac-App-Store-Version (Sandbox) von Marked. Wenn Sie Pandoc ausführen müssen, holen Sie sich über **Hilfe → Crossgrade** eine kostenlose Lizenz für die direkte (Paddle-)Version. Das gilt für jeden Prozessor, der auf Sandboxing-Probleme stößt: Wenn Marked ihn wegen MAS-Berechtigungsproblemen nicht ausführen kann, bietet es die Schritte zum Crossgrade an. Falls bei Ihnen Probleme auftreten kontaktieren Sie mich bitte über die [Support-Seite](https://support.markedapp.com/questions/add).

### Pandoc als Schweizer Taschenmesser unter den Markdown-Prozessoren

[Pandoc](https://pandoc.org/) ist mit Abstand das flexibelste Allzweck-Werkzeug für die Verarbeitung einer Vielzahl von Markup-Formaten. Mit einem `-f`-Argument und einem der folgenden Werte kann Pandoc Ihr benutzerdefinierter Prozessor für all diese Formate sein:

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

Und viele weitere. Näheres in der [Pandoc-Dokumentation](https://pandoc.org/MANUAL.html). Um eines davon als Eingabeformat zu verwenden, geben Sie einfach Folgendes in Ihr Feld „Befehl ausführen“ ein:

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc eignet sich perfekt für ein Skript, das über die Umgebungsvariable `$MARKED_EXT` bestimmt, welches Format es durch Pandoc laufen lässt – oder für eine Reihe von Regeln mit Erweiterungsabgleich. Ist die Erweiterung `md`, verwenden Sie `pandoc -f gfm` oder `pandoc -f markdown_mmd` (oder geben Sie einfach `NOCUSTOM` über STDOUT zurück, um den Standardprozessor zu nutzen). Ist sie `textile`, führen Sie im Skript `pandoc -f textile` aus. Und ist sie `wiki`, verwenden Sie einen der Wiki-Markup-Prozessoren. Sie verstehen das Prinzip.

Wie Pandoc-Kenner wissen, beherrscht Pandoc auch umfangreiche Bibliografie- und LaTeX-Szenarien. Die meisten Funktionen, die Sie über die Befehlszeile erreichen, stehen in Marked einfach durch das Übergeben von Argumenten zur Verfügung.

## Textile verwenden

Ein paar Leute haben gefragt, wie sie Textile in Marked zum Laufen bringen. Sie brauchen einen Textile-Konverter, der über die Befehlszeile verfügbar ist. Es gibt einige Optionen, darunter Pandoc (siehe oben); falls Sie Pandoc aber noch nicht installiert haben, sind zwei weitere Optionen RedCloth für Ruby und Textile für Perl (setzt installierte Entwickler-Tools voraus). Installieren Sie das eine oder das andere:

1. Installieren Sie Textile von <https://github.com/bradchoate/text-textile> **ODER** `sudo gem install RedCloth` im Terminal
2. Ermitteln Sie mit `which textile` oder `which redcloth` den Pfad, den Sie in den Pfadeinstellungen des benutzerdefinierten Prozessors verwenden

Jetzt ist Marked eine Textile-Vorschau für Sie!

## AsciiDoc verwenden

1. Installieren Sie [AsciiDoctor](http://asciidoctor.org/).
2. Aktivieren Sie unter {% prefspane Processor %} eine Eigene Regel, die auf Ihre AsciiDoc-Dateien passt.
3. Legen Sie die Regel als Prozessor fest und fügen Sie eine Aktion „Befehl ausführen“ hinzu
    1. Ermitteln Sie den Pfad zu `asciidoc`, der etwa `/usr/bin/asciidoc` oder `/opt/local/bin/asciidoc` lautet. Im Zweifel finden Sie ihn mit `which asciidoc`
    2. Geben Sie als Befehl `[PFAD zu asciidoc] --backend html5 -o - -` ein (das `-` am Ende sendet die Ausgabe an STDOUT)

Dadurch wird das aktuelle Dokument an STDIN gesendet und das erzeugte HTML über STDOUT angezeigt.

Weitere Informationen finden Sie in [diesem Gist](https://gist.github.com/mojavelinux/6324279) von [Dan Allen](https://gist.github.com/mojavelinux).
