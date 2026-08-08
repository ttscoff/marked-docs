# <%= @title %>

Markeds URL-Handler bietet zusätzliche Skripting- und Workflow-Möglichkeiten. Sie können zum Beispiel in den Notizen einer anderen App eine URL hinterlegen, die beim Klick eine Datei in Marked öffnet. Es stehen mehrere Aktionen zur Verfügung, wie unten aufgeführt.

## Das URL-Schema [the-url-scheme]

Markeds URL-Schema ist `x-marked` und wird mit Optionen wie `x-marked://open?file=/Users/username/Desktop/report.md` aufgerufen.

Sie können gezielt Marked 3 ansprechen, indem Sie `x-marked-3` statt `x-marked` verwenden. Methoden und Parameter sind genau dieselben wie bei `x-marked`, aber nur Marked 3 reagiert auf `x-marked-3`.

## Aufruf über die Befehlszeile/Skripte [calling-from-the-command-linescripts]

Den URL-Handler rufen Sie über die Befehlszeile oder ein Skript mit dem macOS-[`open`-Befehl](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/) auf:

	open 'x-marked://open?file=filename.md'
	open 'x-marked://refresh?file=filename.md'

### Aufruf im Hintergrund [calling-in-the-background]

Sie können den `open`-Befehl mit dem Flag `-g` aufrufen, um das Ergebnis im Hintergrund auszuführen, ohne den Fokus zu wechseln. Um den Befehl im Hintergrund auszuführen und das Fenster nach vorne zu holen, ohne den Fokus zu stehlen:

	open -g 'x-marked://open?file=filename.md&raise=true'

## Optionale Parameter [optional-parameters]

### x-success [x-success]

Jeder Befehl kann einen **x-success**-Abfrageparameter mitgeben. Setzen Sie ihn auf eine URL, die nach der Ausführung des Befehls aufgerufen wird. Zum Beispiel: `x-marked://open/?file=filename.md&x-success=ithoughts:`. Sie können auch eine Bundle-ID (etwa `com.googlecode.iterm`) angeben, um eine App ohne eigenes URL-Schema zu öffnen.

### raise [raise]

Ein **raise**-Parameter kann bei jedem Befehl mitgegeben werden, der einen `file`-Parameter akzeptiert oder alle Fenster betrifft. Nach der Aktion werden die betroffenen Fenster über alle anderen Fenster (aller Apps) gehoben, bevor der Befehl zurückkehrt oder einen Callback ausführt.

	"x-marked://refresh?file=filename.md&raise=true"

### speedread [speedread]

Ein **speedread**-Parameter kann bei URL-Handler-Befehlen mitgegeben werden, die ein Vorschaudokument öffnen (`open`, `paste`, `preview` und `stream`). Setzen Sie `speedread=1`, um Speed Read automatisch zu starten, sobald die Ziel-Vorschau bereit ist.

Beispiele:

	x-marked://open?file=/Users/username/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	x-marked://paste?speedread=1

# Verfügbare Befehle [available-commands]

Die folgenden Befehle stehen für den `x-marked`-URL-Handler zur Verfügung.

## addstyle [addstyle]

Fügt Marked einen neuen eigenen Stil hinzu.

##### Parameter: [parameters]

**css**: URL-kodierter CSS-Text, der in einen eigenen Stil geschrieben wird. Erforderlich, sofern kein **file**-Parameter übergeben wird.

**file**: Vollständiger Pfad (POSIX) zu einer CSS-Datei, die Marked hinzugefügt wird. Erforderlich, sofern kein **css**-Parameter übergeben wird.

**name**: Der Name des zu erzeugenden Stils.

Beim **css**-Parameter wird dieser sowohl als Dateiname beim Schreiben auf die Festplatte (mit angehängtem `.css`) als auch als Menüeintragsname verwendet. Für **css** ist er erforderlich, für **file** optional (dann wird der Dateiname verwendet, als wäre der name-Parameter leer).

	x-marked://addstyle?name=My+new+style&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

Geben Sie beim file-Parameter einen Namen an, erhält der Menüeintrag diesen Namen statt des Dateinamens. Verwenden Sie denselben Namen erneut mit einem anderen Pfad, wird der Menüeintrag mit dem neuen Pfad aktualisiert, statt einen zweiten Eintrag mit demselben Namen hinzuzufügen.

## defaults [defaults]

Setzt Benutzereinstellungen. Akzeptiert eine Liste von Schlüsseln und Werten als Abfrageparameter. Nur bereits vorhandene Schlüssel werden gesetzt. Erfordert die Einstellungsänderung eine Aktualisierung, aktualisieren sich alle Fenster automatisch, sofern nicht `refresh=0` übergeben wird.

Verwenden Sie bei booleschen Werten 1 für wahr und 0 für falsch.

##### Parameter: [parameters-2]

**refresh** _(optional)_: bei 0 wird das automatische Aktualisieren offener Vorschaufenster deaktiviert

* Standard: 1 (wahr)

##### Beispiel: [example]

	x-marked://defaults?syntaxHighlight=1&includeMathJax=0

Die `defaults`-Methode ist vor allem dafür gedacht, dass der Entwickler Links zu speziellen Funktionen bereitstellen kann, die sonst vielleicht nicht in den Einstellungen verfügbar sind. Es gibt aber auch ein paar Standardoptionen, die Sie beim Automatisieren umschalten möchten. Einige gängige Einstellungen, die Sie bei der Automatisierung steuern könnten:

syntaxHighlight
: Syntaxhervorhebung aktivieren oder deaktivieren

includeMathJax
: interne MathJax-Verarbeitung aktivieren oder deaktivieren

processor
: auf `multimarkdown` oder `mmd` setzen, um den Prozessor auf MultiMarkdown umzustellen; `discount` oder `gfm`, um den Discount-Prozessor zu verwenden

h1IsPageBreak, h2IsPageBreak, breakBeforeFootnotes
: Automatische Seitenumbrüche beim Export vor Überschriftenebene 1 und 2 sowie vor Fußnoten.


## dingus [dingus]

Öffnet den Markdown Dingus, um verschiedene Markdown-Prozessoren zu testen.

	x-marked://dingus

##### Parameter: [parameters-3]

**processor** (optional): Legt fest, welcher Prozessor standardmäßig ausgewählt wird. Gültige Werte:

- `multimarkdown` – MultiMarkdown-Prozessor
- `commonmark` – CommonMark-(GFM-)Prozessor
- `discount` oder `discount (gfm)` – Discount-Prozessor
- `kramdown` – Kramdown-Prozessor

Beispiele:

- `x-marked://dingus?processor=kramdown` – öffnet mit ausgewähltem Kramdown
- `x-marked://dingus?processor=commonmark` – öffnet mit ausgewähltem CommonMark (GFM)

*Hinweis:* Dies öffnet das Markdown-Dingus-Fenster, in dem Sie verschiedene Markdown-Prozessoren (MultiMarkdown, CommonMark (GFM), Discount und Kramdown) nebeneinander testen und vergleichen können. Ideal, um mit Markdown-Syntax zu experimentieren und die Unterschiede der Prozessoren zu verstehen.

## stylestealer / steal [stylestealer-steal]

Öffnet das Style-Stealer-HUD. Praktisch, wenn Sie CSS von einer Live-Seite erfassen oder eine manuelle Inhaltsextraktion starten möchten, ohne es über die Oberfläche aufzurufen.

	Synonyme: x-marked://stylestealer … , x-marked://steal …

##### Parameter: [parameters-4]

**url** _(optional)_: Eine URL, die im Style-Stealer-Fenster vorausgefüllt wird. Wird sie weggelassen, öffnet das HUD leer.

Beispiele:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify [importurl-markdownify]

Öffnet das Fenster „Import URL“ (Content Extractor), damit Sie die Markdownifier-Pipeline manuell ausführen können. Die Extraktion erfolgt dabei **nicht** automatisch – das übernimmt der `extract`-Befehl weiter unten.

	Synonyme: x-marked://importurl … , x-marked://markdownify …

##### Parameter: [parameters-5]

**url** _(optional)_: Füllt das Feld „Import URL“ aus. Wird sie weggelassen, öffnet das Fenster mit leerem Feld und wartet darauf, dass Sie einen Link einfügen.
**html** _(optional, nur markdownify)_: Bei `x-marked://markdownify` sollte dies URL-kodiertes rohes HTML sein. Marked wandelt das HTML nach denselben Regeln wie die Zwischenablage-Vorschau in Markdown um und öffnet es in einem temporären Dokument, als hätten Sie dieses HTML in ein Zwischenablage-Vorschau-Fenster eingefügt.

Beispiele:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## do [do]

Führt einen JavaScript-Befehl in einem Dokumentfenster aus. Markeds gesamte JavaScript-API ist [hier dokumentiert](https://markedapp.com/help/jsapi/).

##### Parameter: [parameters-6]

**js** _(erforderlich)_: Abfragestring mit einem JavaScript-Befehl

* Akzeptiert Pfadparameter, die auf Dateinamen verweisen, oder „all“
* Durch / getrennte Pfade durchsuchen mehrere Dateien
* Teildateinamen werden zur besten Übereinstimmung vervollständigt

		x-marked://do/filename1/filename2?js=...
		x-marked://do/all?js=...

**file**: Abfrageparameter mit kommagetrennten Pfaden/Dateinamen

	x-marked://do?file=filename1,filename2&js=...

Arbeitet mit dem vordersten Fenster, wenn kein Dateiname angegeben ist (oder „all“ nicht übergeben wird)

## help [help]

Öffnet Markeds internes Hilfesystem, optional mit Angabe eines Themas. Das ist primär für den internen Gebrauch gedacht, aber über URL zugänglich. Eine URL zu einem beliebigen Abschnitt lässt sich kopieren, indem Sie mit der rechten Maustaste auf das Lesezeichensymbol rechts neben einer Überschrift klicken und __Link kopieren__ wählen. Die In-App-Hilfe und -Suche von **Marked 3** verwenden für diese Links das `x-marked-3`-Schema, damit macOS sie in Marked 3 öffnet, wenn auch Marked 2 installiert ist; die Beispiele unten nutzen diese Form.

##### dingus [dingus-2]

Öffnet den Markdown Dingus, um verschiedene Markdown-Prozessoren zu testen.

	x-marked://dingus

######## Parameter:

**processor** (optional): Legt fest, welcher Prozessor standardmäßig ausgewählt wird. Gültige Werte:

- `multimarkdown` – MultiMarkdown-Prozessor
- `commonmark` – CommonMark-(GFM-)Prozessor
- `discount` oder `discount (gfm)` – Discount-Prozessor
- `kramdown` – Kramdown-Prozessor

Beispiele:

- `x-marked://dingus?processor=kramdown` – öffnet mit ausgewähltem Kramdown
- `x-marked://dingus?processor=commonmark` – öffnet mit ausgewähltem CommonMark (GFM)

*Hinweis:* Dies öffnet das Markdown-Dingus-Fenster, in dem Sie verschiedene Markdown-Prozessoren (MultiMarkdown, CommonMark (GFM), Discount und Kramdown) nebeneinander testen und vergleichen können. Ideal, um mit Markdown-Syntax zu experimentieren und die Unterschiede der Prozessoren zu verstehen.

##### Parameter: [parameters-7]

**page** _(optional)_: Der genaue Titel einer vorhandenen Seite, optional mit Anker-Hash

	x-marked-3://help?page=Document_Statistics

Leerzeichen werden durch Unterstriche ersetzt, gemäß der Namenskonvention für Markeds Hilfedateien. Statt eines Hashs (#) kann ein Doppelpunkt (:) verwendet werden, um einen Anker anzugeben.

Das Ziel kann auch allein über den Pfad angegeben werden (ohne Query-String):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## extract [extract]

Extrahiert Inhalte von einer Web-URL und öffnet sie als neues Dokument in Marked.

	x-marked://extract?url=https://example.com

##### Parameter: [parameters-8]

**url** _(erforderlich)_: Die Web-URL, aus der Inhalte extrahiert werden. Muss mit `http://` oder `https://` beginnen

**window** _(optional)_: Name für das Fenster

**id** _(optional)_: Namespace-Bezeichner

**base** _(optional)_: Basis-URL für relative Links

**raise** _(optional)_: Auf `true` setzen, um das Fenster nach dem Öffnen nach vorne zu holen

**manual** _(optional)_: Auf `true` setzen, um das manuelle Extraktionsfenster des Style Stealer zu öffnen, statt automatisch zu extrahieren.

- Bei `manual=true` öffnet Marked den Style Stealer, füllt das URL-Feld vor (falls angegeben), unterdrückt einen automatischen Öffnen-Dialog und lässt Sie Stile/Inhalte interaktiv auswählen und extrahieren, bevor Sie speichern.
- Wird er weggelassen oder auf `false` gesetzt, führt Marked den automatischen Extraktor (Markdownifier) aus und öffnet das Ergebnis direkt als neues temporäres Dokument.

##### Beispiele: [examples]

	x-marked://extract?url=https://news.ycombinator.com

	x-marked://extract?url=https://github.com&window=GitHub&raise=true

	x-marked://extract?url=https://example.com/article&manual=true

	x-marked://extract?url=https://blog.example.com/post-title

*Hinweis:* Dieser Befehl nutzt Markeds Dienst zur Inhaltsextraktion, um Webseiten abzurufen, sauberen Inhalt mit Readability zu extrahieren, ihn in Markdown umzuwandeln und das Ergebnis in einem neuen temporären Dokument zu öffnen. Der extrahierte Inhalt enthält Metadaten (Titel, Quell-URL, Datum) und ist als sauberes Markdown formatiert. Ideal, um Webinhalte schnell zu erfassen und zu bearbeiten.

## open [open]

Öffnet das angegebene Dokument in Marked.

	x-marked://open?file=/Users/username/Desktop/report.md

##### Parameter: [parameters-9]

**file** *(erforderlich)*: Der vollständige POSIX-Pfad zum zu öffnenden Dokument oder eine kommagetrennte Liste von Pfaden

**speedread** *(optional)*: Auf `1` setzen, um nach dem Öffnen automatisch Speed Read zu starten.

`open` akzeptiert auch einen Pfad, dessen Komponenten zu einer einzigen URL zusammengesetzt werden

	x-marked://open/~/nvALT2.2

Existiert der angegebene Dateipfad nicht oder lässt er sich nicht öffnen, kommt Marked trotzdem in den Vordergrund. Ein Aufruf ohne den *file*-Parameter oder mit leerem Wert öffnet einfach Marked.

Marked öffnet Dateien auch, wenn dem URL-Handler nur der Pfad einer Datei übergeben wird, z. B. `x-marked:///Users/username/Desktop/report.md`.

## paste [paste]

Erstellt ein neues Dokument aus dem aktuellen Inhalt der Zwischenablage.

	x-marked://paste

##### Parameter: [parameters-10]

**speedread** *(optional)*: Auf `1` setzen, um nach dem Öffnen der Zwischenablage-Vorschau automatisch Speed Read zu starten.

*Hinweis:* Dies erstellt ein temporäres Dokument über den Befehl „Zwischenablage-Vorschau“. Beliebiger Text in Ihrer Zwischenablage wird einem neuen, leeren Dokument hinzugefügt, das dann in Marked geöffnet wird. Wird es ohne Speichern geschlossen, wird es verworfen.

## preview [preview]

Zeigt angegebenen Text in einem neuen Dokument in der Vorschau.

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parameter: [parameters-11]

**text** *(erforderlich)*: Der in die Vorschau einzufügende Text. Prozentkodierter Text wird vor dem Anzeigen des Dokuments dekodiert.

**speedread** *(optional)*: Auf `1` setzen, um nach dem Öffnen des Vorschautexts automatisch Speed Read zu starten.

## stream [stream]

Öffnet ein Fenster mit einer Streaming-Zwischenablage-Vorschau.

	x-marked://stream

##### Parameter: [parameters-12]

**speedread** *(optional)*: Auf `1` setzen, um nach dem Öffnen der Streaming-Vorschau automatisch Speed Read zu starten.

*Hinweis:* Dies erstellt ein temporäres Dokument über den Befehl „Zwischenablage-Vorschau“. Der übergebene Text wird einem neuen, leeren Dokument hinzugefügt, das dann in Marked geöffnet wird. Wird es ohne Speichern geschlossen, wird es verworfen.

## refresh [refresh]

Aktualisiert eine Dokumentvorschau oder alle offenen Vorschauen.

##### Parameter: [parameters-13]

**file**: Abfrageparameter mit kommagetrennten Pfaden/Dateinamen (die Dateien müssen in Marked geöffnet sein). Ein Aufruf ohne `file`-Parameter oder mit `?file=all` aktualisiert alle offenen Fenster.

Der *file*-Parameter kann unvollständig sein; Marked aktualisiert alle offenen Fenster mit einer teilweisen Übereinstimmung im *Dateinamen* (nicht im vollständigen Pfad). „all“ aktualisiert alle Fenster.

	x-marked://refresh

	x-marked://refresh?file=/Users/username/Desktop/report.md

	x-marked://refresh?file=report.md

Wird ohne `file`-Parameter, aber mit in der URL angegebenen Dokumentpfaden aufgerufen, durchsuchen durch / getrennte Pfade mehrere Dateien, und Teildateinamen werden zur besten Übereinstimmung vervollständigt.

	x-marked://refresh/filename1/filename2

## style [style]

Setzt den Vorschaustil (CSS) für ein oder mehrere Dokumente.

##### Parameter: [parameters-14]

**css** _(erforderlich)_: Abfragestring mit dem Namen oder Pfad eines Stils. Die Stile müssen in Markeds Stil-Menü als Standard- oder manuell hinzugefügte eigene Stile vorhanden sein.

* Akzeptiert Pfadparameter, die auf Dateinamen verweisen, oder „all“
* Durch / getrennte Pfade durchsuchen mehrere Dateien
* Teildateinamen werden zur besten Übereinstimmung vervollständigt

		x-marked://style/filename1/filename2?css=...
		x-marked://style/all?css=...

**file**: Abfrageparameter mit kommagetrennten Pfaden/Dateinamen

	x-marked://style?file=filename1,filename2&css=...

Diese Methode arbeitet mit dem vordersten Fenster, wenn kein Dateiname angegeben ist (oder „all“ nicht übergeben wird).
