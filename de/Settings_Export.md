# <%= @title %>

Optionen unter {% prefspane Export %}:

(Siehe [Exportieren](Exporting.html) für weitere Informationen)

![Einstellungen: Export][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Exportprofil [export-profile]

Exportprofil
: Wählen Sie ein gespeichertes Profil aus dem Popup-Menü. Profile speichern einen vollständigen Satz an Exporteinstellungen für schnelles Wechseln zwischen Arbeitsabläufen (zum Beispiel Druck-PDF vs. Web-HTML). Siehe [Exportprofile](Exporting.html#export-profiles).

Neu
: Erstellt ein neues Profil aus den aktuellen Einstellungen.

Verwalten
: Öffnet den Profilmanager zum Umbenennen, Duplizieren oder Löschen von Profilen.

### Drucken/PDF [printpdf]

Links/Hervorhebungen für PDF/Print deaktivieren
: Entfernt beim Drucken die Formatierung (Unterstreichung und Farbe) von Links.

URL als Textanmerkung einfügen
: Beim Drucken oder PDF-Export erscheint die URL eines Links hinter dem verlinkten Text.

Horizontale Linien durch Seitenumbrüche ersetzen
: Wandelt horizontale Linien im Dokument in Seitenumbrüche um (das erzwingt zusätzlich Fußnoten auf einer neuen Seite).

Bilder beim Kopieren von HTML einbetten
: Ist dies aktiviert, wird beim Kopieren von HTML in die Zwischenablage nach lokalen Bildern gesucht; sie werden Base64-codiert und als Data-URLs in den Quelltext eingebettet.

Hintergrundfarben und Bilder drucken
: Standardmäßig druckt bzw. exportiert Marked mit weißem Hintergrund. Wenn Sie Hintergrundfarben und Bilder aus eigenen Stilen einbinden möchten, aktivieren Sie diese Option.

Verwaiste Überschriften vermeiden
: Diese Option verhindert, dass Überschriften des nächsten Abschnitts am Seitenende ohne nachfolgenden Inhalt stehen.

Erstes H1 ausschließen
: Ignoriert die erste Überschrift der Ebene 1 im Dokument, wenn H1 als Seitenumbrüche verwendet werden.

Erstes H1 als Ersatztitel verwenden
: Bei Apps wie Bear oder der Streaming-Vorschau können Sie mit dieser Option den Dateinamen durch den Inhalt des ersten H1 im Dokument ersetzen. Sind Metadaten für „title“ angegeben, haben diese immer Vorrang.

Seitenumbrüche einfügen vor
: Verwendet Überschriften der Ebene 1/2 als Abschnittstrenner, die immer auf einer neuen Seite beginnen. Wählen Sie „Fußnoten“, um vor allen Fußnoten im Dokument stets einen Seitenumbruch einzufügen.

Seitenumbrüche in der Vorschau anzeigen
: Zeigt eine helle gestrichelte Linie, wo Umbrüche mit der Syntax &lt;!\--BREAK\--&gt; oder durch Aktivieren der Auto-Umbruch-Optionen in den Export-Einstellungen eingefügt werden.

Benutzerdefinierte Schriftgröße für Export/Druck
: Ist dies gesetzt, wird der gesamte Text anhand der gewählten Punktgröße skaliert (Standard ist eine Basis von 10 Punkt).

Ränder
: Legt die Druckränder (in Punkt) für oben, unten, links und rechts fest.

Inhaltsverzeichnis ausdrucken
: Bindet ein automatisches Inhaltsverzeichnis in Druck/PDF ein.

Seitenumbruch danach
: Bricht nach einem eingefügten Inhaltsverzeichnis automatisch auf eine neue Seite um.

Inhaltsverzeichnis-Ebenenmarkierungen
: Legen Sie über die Dropdown-Menüs die Listenmarkierung für jede Einrückungsebene eines Inhaltsverzeichnisses fest.

### Kopf- und Fußzeilen [headers-and-footers]

Konfigurieren Sie Schrift, Logo, Kopf-/Fußzeilenfelder, Datums- und Zeitformate, das Einschließen auf der ersten Seite, den Versatz der Seitennummerierung und Trennlinien. Feld-Platzhalter sind unter anderem `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1` und `%h2`.

Siehe [Kopf- und Fußzeilen](Exporting.html#headers-and-footers) in [Exportieren](Exporting.html) für die Platzhalter-Referenz und Beispiele. Siehe [Datums- und Zeitformate](Exporting.html#dateandtimeformats) für die Formatcodes von `%date` und `%time`.

Auf erster Seite einschließen
: Sind die Optionen für Kopf- und/oder Fußzeile deaktiviert, wird der jeweilige Typ auf der ersten Seite nicht gedruckt.

Datumsformat
: strftime-artige Formatzeichenkette für `%date` in Kopf- und Fußzeilen. Siehe [Datums- und Zeitformate](Exporting.html#dateandtimeformats).

Zeitformat
: strftime-artige Formatzeichenkette für `%time` in Kopf- und Fußzeilen. Siehe [Datums- und Zeitformate](Exporting.html#dateandtimeformats).

Versatz der Seitennummerierung
: Passt an, mit welcher Nummer die Seitennummerierung beginnt. Haben Sie zum Beispiel auf der ersten Seite ein Inhaltsverzeichnis und möchten, dass die Nummerierung auf der zweiten Seite beginnt, setzen Sie den Versatz auf -1. Seite 2 wird dann zu Seite 1, und die Gesamtseitenzahl wird entsprechend angepasst.

Trennlinie
: Druckt eine horizontale Linie unter der Kopfzeile und/oder über der Fußzeile.

Standardformate wiederherstellen
: Setzt die Datums- und Zeitformat-Zeichenketten auf Markeds Standardwerte zurück (`%m-%d-%Y` und `%I:%M %p`). Siehe [Datums- und Zeitformate](Exporting.html#dateandtimeformats).
