# <%= @title %>

So wird aus Ihrem Markdown ein fertiges Dokument.

## Export nach der Vorschau

Die Vorschau von Marked ist die Grundlage für den Export – was Sie im Vorschaufenster sehen, erhalten Sie in PDF, DOCX, EPUB und anderen Formaten (abgesehen von exportspezifischen Einstellungen wie Rändern, Kopfzeilen und Paginierung). Richten Sie zuerst Ihren Stil ein und lesen Sie in der Vorschau Korrektur, und exportieren Sie dann, wenn das Dokument fertig ist. Den vollständigen Vorschau-Workflow finden Sie unter [Live-Markdown-Vorschau auf dem Mac](Live_Markdown_Preview_on_Mac.html).

## Das Export-Panel [drawer]

![Export-Panel][export-panel]

Das **Export-Panel** ist ein tastaturgesteuertes Panel im Spotlight-Stil, das schnellen Zugriff auf alle Exportoptionen bietet. Öffnen Sie es, indem Sie auf das Exportsymbol in der Statusleiste klicken oder {% kbd shift cmd e %} drücken.

![Export-Schaltfläche][expbut]

Im Export-Panel können Sie Ihr Dokument als HTML, einseitiges PDF, paginiertes PDF, RTF-Paket oder als Microsoft-Word-DOC- oder -DOCX-Datei speichern. Sie können es auch in eine neue Markdown-Datei speichern (Marked-spezifische Funktionen werden gerendert und ihre Ergebnisse einbezogen), als OpenDocument (ODT) oder als OPML zur Verwendung in anderen Anwendungen.

## HTML kopieren

Mit der Funktion „HTML kopieren“ legen Sie den HTML-Quelltext Ihrer Vorschau ohne Umwege in die Zwischenablage. Sie erreichen sie über das Zahnradmenü oder einfach mit {% kbd shift cmd C %}. Das kopierte HTML ist ein Schnipsel, der sich direkt in einen Blog, ein Forum oder ein HTML-Dokument einfügen lässt.

Zum Kopieren müssen Sie nicht in der Quelltextansicht sein. Tippen Sie bei fokussierter Vorschau (klicken Sie hinein) einfach {% kbd shift cmd C %}, und eine Popup-Meldung bestätigt Ihnen, dass der Quelltext in der Zwischenablage liegt.

## HTML speichern

![][exporthtmlaccessory]



Mit dem Befehl „HTML speichern“ – erreichbar über das Zahnradmenü oder einfach mit **{% kbd cmd S %}** – speichern Sie ein vollständiges Dokument, das zum Teilen oder Veröffentlichen bereit ist.

Optional können Sie einen der Stile von Marked (oder einen Ihrer [eigenen Stile][custom]) in den Export einbeziehen. So erhalten Sie ein gebrauchsfertiges Dokument mit bereits eingebetteter Formatierung.

Zusätzlich können Sie alle im Dokument enthaltenen lokalen Bilder in das exportierte HTML einbetten. Dann haben Sie ein eigenständiges Dokument, das sich überall hosten lässt, ohne die Bilder mitverschieben zu müssen. Das funktioniert nur mit Bildern, die auf Ihrem lokalen Laufwerk über relative oder absolute Pfade referenziert sind. Vermeiden Sie `file:///`-Pfade, wenn Sie diese Funktion nutzen möchten.

## Markdown auf dem Mac nach PDF exportieren

Die Druck-/PDF-Vorschau ({% kbd cmd P %}) öffnet einen Standard-Druckdialog. Jeder Vorschaustil in Marked hat eigene begleitende Druckstile, die Hintergründe entfernen, Schriftgrößen anpassen und Rahmen bereitstellen. Gedruckt wird auf Basis des aktuell ausgewählten Stils.

Im Druckdialog fallen die Schaltflächen „PDF“ und „Vorschau“ auf. „PDF“ bietet Ihnen je nach verfügbaren Anwendungen verschiedene Optionen für den PDF-Export, und „Vorschau“ exportiert eine PDF-Version direkt in Preview.app, wo Sie sie speichern oder per E-Mail versenden können.

Das Drucken nach PDF über diesen Weg schließt die Paginierung ein. Beim Drucken auf Papier oder in PDF lassen sich Seitenumbrüche manuell einfügen – über die [`<!--BREAK-->`-Syntax][break] oder indem Sie unter {% prefspane Export %} festlegen, dass Überschriften der Ebene 1 und/oder 2 als Abschnittstrenner dienen.

Es gibt außerdem eine Einstellung, um horizontale Linien (`<hr>`) beim Drucken in Seitenumbrüche umzuwandeln. Dabei wird die vom Tag erzeugte Linie durch einen Seitenumbruch ersetzt und aus der finalen Ausgabe entfernt. Die Vorschau bleibt von dieser Einstellung unberührt.

![Druckränder][printmargins]

Seitenränder legen Sie unter {% prefspane Export %} fest; sie wirken sich auf die Druck- und die paginierte PDF-Ausgabe aus.

Die Randeinstellungen können Sie pro Dokument mit dem Metadaten-Schlüssel `Margins:` überschreiben. Werte werden als Punkte interpretiert; Einheitensuffixe wie `px`, `pt` und `em` werden ignoriert. Verwenden Sie zwei Zahlen für vertikale und horizontale Ränder (`10 20`) oder vier Zahlen für oben, rechts, unten und links (`10, 20, 10, 20` oder `10 20 10 20`). Metadaten-Ränder überschreiben die Einstellungen unter {% prefspane Export %}.

### Kopf- und Fußzeilen [headers-and-footers]

Unter {% prefspane Export %} definierte Kopf- und Fußzeilen erscheinen oben und unten auf jeder gedruckten oder als paginiertes PDF gespeicherten Seite sowie im DOCX-Export. Sie können beliebigen Text oben links, oben mittig, oben rechts, unten links, unten mittig und unten rechts einsetzen. Zentrierter Text wird auf der Seite mittig ausgerichtet. Die folgenden Variablen werden in den Zeichenfolgen ersetzt, sofern verwendet:

    %title = Dokumenttitel
    %date = Aktuelles Datum
    %time = Aktuelle Uhrzeit
    %page = Aktuelle Seitenzahl
    %total = Gesamtseitenzahl
    %path = Dateisystempfad zum Dokument
    %filename = Nur der Dateiname des Dokuments
    %basename = Der Dateiname ohne Erweiterung
    %logo/%image = Ein im Bildfeld der Kopf-/Fußzeilen-Einstellungen festgelegtes Logo
    %%(text) = Text, der nur auf der ersten Seite gedruckt wird
    %h1/h2/h3/h4/h5/h6 = Abschnittstitel auf Basis der Markdown-Überschriften
    %sep(X) = Text zwischen Abschnittstiteln, wenn ein Unterabschnitt existiert

**Druck und paginiertes PDF** lösen `%h1`–`%h6` über Markeds Paginierung auf, sodass jede Seite die auf ihr sichtbare Überschriftenhierarchie zeigt. `%sep(X)` und `%md_*`-Metadatenvariablen werden auch in der Druck-/PDF-Ausgabe unterstützt.

**DOCX-Export** bettet `%logo`/`%image` in die Word-Kopf- oder -Fußzeile ein (auf ca. 50 px Höhe skaliert, passend zur Druckvorschau). Überschriften-Platzhalter werden zu Word-**STYLEREF**-Feldern, die auf die exportierten Stile `Heading 1`–`Heading 6` verweisen. Word aktualisiert diese Felder beim Öffnen des Dokuments – anhand von Words eigenem Layout und dessen Seitenumbrüchen, nicht anhand von Markeds Vorschau-Paginierung. `%md_*`-Metadatenvariablen werden beim Export einmalig ersetzt, genau wie in der Druck-/PDF-Ausgabe. `%sep(X)` wird in DOCX-Kopf-/Fußzeilen nicht umgesetzt.

`%title` verwendet die in MultiMarkdown-Metadaten-Headern definierte `Title:`-Angabe; andernfalls greift es auf den Dateinamen ohne Dateierweiterung zurück. Um einen Titel über MMD-Metadaten zu definieren, setzen Sie Folgendes in die erste Zeile des Dokuments:

    Title: The title of your document

Lassen Sie danach eine Leerzeile (oder weitere Metadaten, die Sie definieren möchten, gefolgt von einer Leerzeile).

Sie können auch jeden MMD-Metadaten-Schlüssel als Variable verwenden, indem Sie ihm `%md_` voranstellen und die Wörter des Schlüssels kleingeschrieben zusammenziehen. Wenn Ihr Dokument oben etwa diesen Metadaten-Schlüssel hat:

    Funky Monkey: The funkiest monkey

dann fügt `%md_funkymonkey` in einem Kopf-/Fußzeilenfeld „The funkiest monkey“ an der Stelle dieses Felds in das exportierte Dokument ein. Bei Dokumenten ohne diesen Schlüssel bleibt das Feld leer, sodass Sie Kopf-/Fußzeilen gezielt anhand von Metadaten ergänzen können.

Die Formatcodes für `%date` und `%time` finden Sie unter [Datums- und Uhrzeitformate](Exporting.html#dateandtimeformats).

Mit der Einstellung „Versatz der Seitennummerierung“ legen Sie fest, bei welcher Zahl die Seitenzählung beginnt. Haben Sie zum Beispiel ein Inhaltsverzeichnis auf der ersten Seite und möchten, dass die Zählung auf der zweiten Seite bei 1 beginnt, setzen Sie den Versatz auf -1. Seite 2 ist dann Seite 1 in der Kopf-/Fußzeile (`%page`), und die Gesamtseitenzahl (`%total`) wird entsprechend angepasst.

Sie können auch eine Kopf-/Fußzeilen-Schriftart für ein bestimmtes Dokument angeben, indem Sie oben in der Datei MMD-Metadaten verwenden:

    Header Font: Mensch

Beachten Sie: Wenn Sie einen Schriftfamiliennamen angeben, wird ein Standard-Schriftschnitt gewählt. Eine Variante geben Sie über den Systemnamen der Schrift an. Bei Helvetica Neue Ultralight etwa verwenden Sie `Header Font: HelveticaNeueUltralight`.

Zusätzlich können Sie über die Metadaten eine Kopf-/Fußzeilen-Schriftgröße pro Dokument angeben:

    Header Font Size: 10

### Datums- und Uhrzeitformate

Die Felder **Datumsformat** und **Zeitformat** unter {% prefspane Export %} steuern, wie `%date` und `%time` in Kopf- und Fußzeilen dargestellt werden. Beide Felder nutzen Formatcodes im strftime-Stil: ein `%` gefolgt von einem Buchstaben. Literaler Text (etwa `-`, `:` oder Leerzeichen) wird unverändert übernommen.

**Beispiele**

    %m-%d-%Y     → 06-20-2026   (Standard-Datumsformat von Marked)
    %I:%M %p     → 3:45 PM      (Standard-Zeitformat von Marked)
    %Y-%m-%d     → 2026-06-20
    %B %d, %Y    → Juni 20, 2026
    %a %H:%M     → Fr 15:45

**Häufige Formatcodes**

| Code | Beispiel | Beschreibung |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Vierstellige Jahreszahl |
| `%y` | 26 | Zweistellige Jahreszahl |
| `%m` | 06 | Monat (01–12) |
| `%B` | Juni | Vollständiger Monatsname |
| `%b` | Jun | Abgekürzter Monatsname |
| `%d` | 20 | Tag des Monats (01–31) |
| `%e` | 20 | Tag des Monats (mit Leerzeichen aufgefüllt) |
| `%A` | Freitag | Vollständiger Wochentagsname |
| `%a` | Fr | Abgekürzter Wochentagsname |
| `%H` | 15 | Stunde, 24-Stunden-Format (00–23) |
| `%I` | 03 | Stunde, 12-Stunden-Format (01–12) |
| `%M` | 45 | Minute (00–59) |
| `%S` | 07 | Sekunde (00–59) |
| `%p` | PM | AM oder PM |
| `%x` | (Gebietsschema) | Bevorzugtes Datum des Gebietsschemas |
| `%X` | (Gebietsschema) | Bevorzugte Uhrzeit des Gebietsschemas |
| `%c` | (Gebietsschema) | Bevorzugtes Datum samt Uhrzeit des Gebietsschemas |

**Druck und paginiertes PDF** unterstützen den vollständigen oben gezeigten strftime-Satz plus weitere Codes wie `%j` (Tag des Jahres), `%U`/`%W` (Wochennummer), `%z` (Zeitzonen-Versatz) und `%Z` (Zeitzonenname). Eine vollständige Referenz bietet die [strftime-Spezifikation der Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html).

**DOCX-Export** unterstützt die in der Tabelle oben aufgeführten Codes. Seltenere Codes können ignoriert oder unverändert durchgereicht werden.

Über **Standardformate wiederherstellen** unter {% prefspane Export %} setzen Sie auf `%m-%d-%Y` und `%I:%M %p` zurück.

### Kopf- und Fußzeilen pro Dokument

Sie können Kopf- und Fußzeilen pro Dokument angeben, indem Sie ganz oben im Dokument MultiMarkdown-Metadaten verwenden:

    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date
    Print Footer Right: %page/%total

Diese überschreiben alle Einstellungen in den Voreinstellungen. Hinweis: Wenn Sie einen anderen Prozessor als MultiMarkdown verwenden und nicht möchten, dass die Kopfzeilen im Dokument selbst auftauchen, können Sie HTML-Kommentare nutzen – lassen Sie dabei vor dem Schließen des Kommentars eine Leerzeile:

    <!--
    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date

    -->

## PDF speichern

Diese Option speichert Ihre Vorschau direkt als PDF-Datei auf Ihrem Laufwerk. Ihr Dokument wird vollständig und ohne Seitenumbrüche gerendert. Um Paginierung in die Ausgabe aufzunehmen, verwenden Sie die Druck-/PDF-Optionen im [Export-Panel](#drawer).

## RTF-Exportoptionen

Marked kann RTF-Daten (Rich Text Format) direkt in Ihre Zwischenablage exportieren. Wählen Sie dazu einfach den Befehl „Rich Text kopieren“ aus dem Zahnradmenü.

Marked kann Ihre Datei auch als **RTFD**-Datei (Rich Text Format) speichern. Das RTFD-Format ist ein Bundle-Format, das eine RTF-Datei und alle im Dokument eingebetteten Bilder enthält.

## DOCX exportieren

Beim Export als DOCX entsteht ein gültiges Microsoft-Word-Dokument, in dem Elemente wie Überschriften, Kopf-/Fußzeilen, Hervorhebungen, Listen usw. auf gültige Word-Stile abgebildet sind. So können Sie in Word problemlos Ihr eigenes Design anwenden.

Weitere Details zu Word-Import und -Export finden Sie unter [Mit DOCX arbeiten][DOCX].

## Markdown nach EPUB exportieren

Marked kann zu 100 % gültige, zu 100 % barrierefreie EPUB-Dokumente exportieren. Wählen Sie den Exporttyp EPUB, geben Sie Metadaten wie Titel, Autor und Datum an und fügen Sie optional ein Titelbild hinzu. Die gespeicherte Datei ist in jedem EPUB-Viewer lesbar.

Die für den EPUB-Export nötigen Metadaten können in der Datei selbst stehen, egal ob es sich um ein Markdown-Dokument, eine Scrivener-Datei (mit einer `metadata`-Seite) oder ein anderes Buchformat handelt. Die zu verwendenden Schlüssel sind:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

Der Schlüssel „Cover Image“ kann einen Pfad relativ zum Basisdokument oder einen absoluten Pfad enthalten. PNG- oder JPG-Dateien sind zulässig.

Ist kein Titel gesetzt, wird standardmäßig der Dateiname des Originaldokuments verwendet; ist kein Autor gesetzt, der vollständige Name Ihres macOS-Benutzers.

Das Datum wird immer auf das aktuelle Datum gesetzt und lässt sich derzeit nicht über Metadaten ändern. Beim Speichern können Sie es jedoch anpassen, solange die (ISO-)Formatierung erhalten bleibt.

### Auf Amazon Kindle veröffentlichen (KDP)

EPUB ist ein offenes Format, das viele Lese-Apps und Stores nutzen (Apple Books, Kobo und andere), nicht nur Kindle. Wenn Sie über [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/) veröffentlichen, exportieren Sie EPUB aus Marked und laden diese Datei zu KDP hoch. Amazon wandelt sie für die Leser in sein eigenes Kindle-Lieferformat (KFX) um.

KDP akzeptiert mehrere Manuskriptformate, darunter EPUB und DOCX (das Marked ebenfalls exportieren kann). Die Anforderungen finden Sie in Amazons [unterstützten eBook-Formaten](https://kdp.amazon.com/en_US/help/topic/G200634390) und im [Leitfaden zur eBook-Manuskriptformatierung](https://kdp.amazon.com/en_US/help/topic/G200645680).

**MOBI ist nicht erforderlich.** KDP akzeptiert für neue Titel keine MOBI-Uploads mehr (einschließlich Büchern mit festem Layout, Stand März 2025). Marked exportiert kein MOBI, und Sie brauchen keine separate „Kindle“- oder Mobipocket-Datei für KDP. Wenn Sie Amazons Layout-Werkzeuge bevorzugen, können Sie ein Buch auch mit [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT) vorbereiten, das KPF-Dateien erzeugt.

Vor dem Hochladen möchten Sie vielleicht mit Amazons kostenlosem [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) prüfen, wie Ihr EPUB auf Kindle-Geräten aussieht. Das ist optionale Drittanbieter-Software von Amazon und nicht Teil von Marked.

## Exportprofile

Mit Exportprofilen speichern Sie verschiedene Sätze von Exporteinstellungen und wechseln schnell zwischen ihnen. Das ist besonders nützlich, wenn Sie regelmäßig Dokumente für verschiedene Zwecke exportieren – etwa ein Profil für druckfertige PDFs mit bestimmten Rändern und Kopfzeilen und ein anderes für webfertiges HTML mit eingebetteten Stilen.

### Exportprofile verwenden

Beim ersten Start von Marked wird automatisch ein Profil „Standard“ mit Ihren aktuellen Exporteinstellungen angelegt. In den Exportdialogen (PDF exportieren, HTML speichern usw.) sehen und wählen Sie Profile über das Profil-Aufklappmenü oben im Dialog.

**Ein neues Profil erstellen:**

1. Passen Sie Ihre Exporteinstellungen unter {% prefspane Export %} oder in einem beliebigen Exportdialog an.
2. Klicken Sie im Exportdialog auf das Profil-Aufklappmenü und wählen Sie „Profil hinzufügen…“.
3. Geben Sie einen Namen für Ihr Profil ein (z. B. „Druckqualität“ oder „Webexport“).
4. Die aktuellen Einstellungen werden als dieses Profil gespeichert.

**Ein Profil laden:**

- Wählen Sie in einem beliebigen Exportdialog ein Profil aus dem Aufklappmenü.
- Alle Exporteinstellungen werden sofort auf die gespeicherten Werte dieses Profils aktualisiert.

**Änderungen an einem Profil speichern:**

- Nachdem Sie Exporteinstellungen geändert haben, erscheint neben dem Profil-Aufklappmenü eine Schaltfläche „Speichern“.
- Klicken Sie auf „Speichern“, um das aktuelle Profil mit Ihren Änderungen zu aktualisieren.
- Die Schaltfläche ist nur aktiv, wenn ungespeicherte Änderungen vorliegen.

**Profile verwalten:**

- Wählen Sie „Profile verwalten…“ aus dem Profil-Aufklappmenü, um das Profilverwaltungsfenster zu öffnen.
- Dort können Sie:
  - Profile **umbenennen**, indem Sie auf den Namen doppelklicken
  - ein Profil **duplizieren**, um darauf aufbauend ein neues zu erstellen
  - Profile **löschen** (das Profil „Standard“ lässt sich nicht löschen)
  - alle verfügbaren Profile in einer Liste ansehen

### Was Exportprofile erfassen

Exportprofile speichern alle exportbezogenen Einstellungen, darunter:

- **PDF-Einstellungen**: Seitengröße, Ränder, Kopf-/Fußzeilen, Schriftarten, Seitenumbrüche, Inhaltsverzeichnis
- **HTML-Export**: Stil-Einbettung, Bild-Einbettung, Syntaxhervorhebung, Mathematik-Rendering
- **Markdown-Verarbeitung**: Textumbruch, Linkformatierung, Prozessorregeln
- **CriticMarkup**: Exporttyp und Verarbeitungsoptionen
- **Syntaxhervorhebung**: Spracherkennung und Hervorhebungseinstellungen
- **Mathematik-Rendering**: MathJax-/KaTeX-Einbindung und Gleichungsnummerierung
- **Bildverarbeitung**: Einbettungsoptionen, Kopierverhalten, Pfadeinstellungen
- **Typografie**: Silbentrennung, Hurenkinder/Schusterjungen, Schriftgrößen
- **Exportverhalten**: Dateibenennung, Konfliktlösung

Profile funktionieren über alle Exporttypen hinweg: Markdown, HTML, fortlaufendes PDF, paginiertes PDF, EPUB, DOCX, ODT, TextBundle, RTF und OPML.

### Speicherort der Profile

Profile werden in Ihrem Application-Support-Ordner gespeichert, unter:

    ~/Library/Application Support/Marked/ExportProfiles.plist

So bleiben Ihre Profile erhalten, selbst wenn Sie die App-Einstellungen zurücksetzen, und sie überstehen App-Updates. Sie können diese Datei sichern, um Ihre Profile über Neuinstallationen oder Rechnerwechsel hinweg aufzubewahren.

### Tipps zum Umgang mit Exportprofilen

- **Profile für gängige Arbeitsabläufe anlegen**: Wenn Sie regelmäßig für Druck und Web exportieren, legen Sie für beides je ein Profil an.
- **Beschreibende Namen verwenden**: Profilnamen wie „Druck – A4“ oder „Web – eingebettete Stile“ machen klar, wofür ein Profil gedacht ist.
- **Häufig speichern**: Die Schaltfläche „Speichern“ erscheint immer dann, wenn Sie etwas geändert haben – klicken Sie darauf, um Ihre Anpassungen zu sichern.
- **Von vorhandenen Profilen ausgehen**: Nutzen Sie „Duplizieren“ im Verwaltungsfenster, um Varianten bestehender Profile zu erstellen, statt bei null anzufangen.

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_with_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center
