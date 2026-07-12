# <%= @title %>

## Callouts

## Bear/Obsidian ##

Marked unterstützt Callouts mit der von Obsidian und Bear verwendeten Syntax – ein speziell formatiertes Blockzitat:

	> [!NOTE] Note title
	> Additional text

Beim „NOTE“ in `[!NOTE]` wird Groß-/Kleinschreibung nicht beachtet. Es kann eines von diesen sein:

- NOTE
- ABSTRACT, SUMMARY, TLDR
- INFO
- TODO
- TIP, HINT, IMPORTANT
- SUCCESS, CHECK, DONE
- QUESTION, HELP, FAQ
- WARNING, CAUTION, ATTENTION
- FAILURE, FAIL, MISSING
- DANGER, ERROR
- BUG
- EXAMPLE
- QUOTE, CITE

Damit werden speziell formatierte Blöcke erstellt.

Mit einem `+` oder `-` machen Sie das Callout ausklappbar. Ein Pluszeichen (`+`) bedeutet, dass das Callout ausklappbar ist, standardmäßig aber geöffnet. Ein Minuszeichen (`-`) bedeutet, dass das Callout ausklappbar ist, standardmäßig aber geschlossen.

  ![Callouts in Marked][callouts]

[callouts]: images/callouts-800.jpg @2x width=800

### Xcode Playground ###

Bei der Vorschau von Xcode-Playground-Dateien unterstützt Marked die native Callout-Syntax von Xcode Playground:

	- Attention: Optional title
	Callout content goes here.

Beim Callout-Typ (z. B. „Attention“) wird Groß-/Kleinschreibung nicht beachtet; er kann einer der folgenden Xcode-Playground-Callout-Typen sein:

- **Attention** – als Info-Callout gestaltet
- **Author** – Metadaten-Callout
- **Authors** – Metadaten-Callout
- **Bug** – Fehler-/Gefahren-Callout
- **Complexity** – Callout im Notiz-Stil
- **Copyright** – Metadaten-Callout
- **Custom Callout** – Callout im Beispiel-Stil
- **Date** – Metadaten-Callout
- **Example** – Beispiel-Callout
- **Experiment** – Callout im Tipp-Stil
- **Important** – Callout im Info-Stil
- **Invariant** – Callout im Notiz-Stil
- **Note** – Note-Callout
- **Precondition** – Callout im Notiz-Stil
- **Postcondition** – Callout im Notiz-Stil
- **Remark** – Callout im Notiz-Stil
- **Requires** – Callout im Notiz-Stil
- **See Also** – Callout im Info-Stil
- **Since** – Metadaten-Callout
- **Version** – Metadaten-Callout
- **Warning** – Warn-Callout

Der optionale Titel nach dem Doppelpunkt wird als Callout-Titel verwendet. Wird kein Titel angegeben, dient der Name des Callout-Typs als Titel.

Der Callout-Inhalt folgt unmittelbar in der nächsten Zeile (keine Leerzeile nötig). Der Inhalt reicht bis zu einer Leerzeile, dem nächsten Callout, einem abgegrenzten Codeblock oder dem Ende des Dokuments.

Beispiel:

````markdown
- Important: Performance Note
This algorithm has O(n log n) complexity.

- Example: Quick Sort
Here's how to implement it:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

Sie können den Titel auch ganz weglassen:

	- Warning
	This is a warning without a custom title.

Diese Callouts werden automatisch in Markeds Callout-Format umgewandelt und passend gestaltet. Der ursprüngliche Callout-Typ bleibt im Attribut `data-callout` erhalten und ermöglicht bei Bedarf eigenes CSS-Styling.

> Diese Funktion greift nur bei der Vorschau von Xcode-Playground-Dateien (`.playground`). Normale Markdown-Dateien verarbeiten diese Syntax nicht.


## Inhaltsverzeichnis [tableofcontents]

Mit `<!--TOC-->` legen Sie fest, wo im Dokument das Inhaltsverzeichnis erscheinen soll. Ist das gesetzt, überschreibt es die Option in den Einstellungen und wird immer im Vorschaufenster sowie beim Speichern und Drucken angezeigt. Das Inhaltsverzeichnis erscheint nur einmal, auch wenn der Inhalt mehrere `<!--TOC-->`-Bezeichner enthält.

Fügen Sie dem obigen Tag `max#` hinzu (wobei # eine Ziffer von 1 bis 5 ist), steuern Sie die Tiefe des angezeigten Inhaltsverzeichnisses. `<!--TOC max2-->` zeigt zum Beispiel nur Überschriften der ersten und zweiten Ebene in der Liste. Mit `<!--TOC min2-->` geben Sie eine minimale Überschriftenebene an. Höchst- und Mindestwerte beziehen sich auf die tatsächlichen Überschriftenebenen, nicht auf die Verschachtelungsebene. Maximum und Minimum lassen sich zusammen verwenden.

Marked erkennt auch das MultiMarkdown-Format `{{TOC}}` und das Pandoc-Format `{{TOC:2-6}}`, wobei `2-6` der Bereich der minimalen und maximalen einzubeziehenden Überschriftenebenen ist.

Standardmäßig wird das Inhaltsverzeichnis auf der ersten Seite des Dokuments gedruckt, wenn „Inhaltsverzeichnis drucken“ unter {% prefspane Export %} aktiviert ist. Ist im Dokument eine Markierung vorhanden, wird es stattdessen an dieser Stelle platziert.

I> Die Art der Nummerierung oder Beschriftung jeder Ebene einer verschachtelten Inhaltsverzeichnis-Hierarchie legen Sie unter {% prefspane Export %} fest.

## Seitenumbrüche

Einen Seitenumbruch für die Druck-/PDF-Ausgabe erzwingen Sie mit dieser Syntax:

```html
<!--BREAK-->
```

Steht das Token allein in einer Zeile, erzeugt es Markup, das an dieser Stelle eine neue Seite erzwingt. Marked versteht auch das Leanpub-Format:

	{::pagebreak /}

## Autoscroll-Pausen [pauses]

Marked kann mit der [Autoscroll](Autoscroll.html)-Funktion als Teleprompter dienen (fügen Sie dazu den [Teleprompter-Stil](https://markedapp.com/styles/preview?style=teleprompter) hinzu). Dabei kann es nützlich sein, Pausen ins Dokument einzubauen. Das geht so:

```html
<!--PAUSE:X-->
```

Dabei ist `X` die Anzahl der Sekunden, die Marked pausieren soll. `<!--PAUSE:15-->` erzeugt also eine 15-sekündige Pause, sobald diese Stelle im Dokument die Bildschirmmitte erreicht.

## Dateien einbinden

Den Inhalt zusätzlicher Dateien fügen Sie mit dieser Syntax ein:

	<<[folder/filename]

Der Pfad zur Datei kann relativ zur Indexdatei oder absolut sein. Einbindungen lassen sich verschachteln; dieselbe Syntax funktioniert auch innerhalb einer eingebundenen Datei. Bei relativen Pfaden sollten Einbindungen in verschachtelten Dateien relativ zu dieser Datei sein. ***Allerdings*** verarbeitet MultiMarkdown alles ausgehend vom Speicherort der zuerst geöffneten Datei, daher sollten alle Bildpfade und sonstigen Einbettungen relativ zur ersten übergeordneten Datei sein – selbst wenn sie in untergeordneten Dokumenten stehen.

MultiMarkdown-Metadaten und YAML-Header werden vor dem Rendern automatisch aus den eingebundenen Dateien entfernt. Das verhindert, dass die Header im Dokument auftauchen; beachten Sie aber, dass Metadaten wie „base header level“ in eingebundenen Dokumenten ignoriert werden.

T> Beim Anzeigen von Dokumenten mit eingebundenen Dateien können Sie „I“ (Umschalt-i) drücken, um zu sehen, welche eingebundene Datei sich im sichtbaren Bereich befindet.

Weitere Informationen finden Sie unter [„Multi-File Documents“][ext].

[ext]: Multi-File_Documents.html

## Code einbinden

Marked kann externe Dateien als Code einbinden – mit einer Syntax, die den Datei-Einbindungen oben ähnelt:

	<<(folder/filename)

Beachten Sie die runden statt der eckigen Klammern. Aus Kompatibilität mit der Leanpub-Syntax erkennt Marked auch einen vorangestellten Satz eckiger Klammern mit einem Titel, macht damit aber derzeit nichts:

	<<[Code title](folder/filename)

Der Inhalt der angegebenen Datei wird in einen pre>code-Block in Ihrem Dokument eingefügt und steht für die automatische Syntaxhervorhebung zur Verfügung, sofern diese aktiviert ist. Codeblöcke lassen sich nicht verschachteln und werden nicht mit MultiMarkdown verarbeitet. Benutzerdefinierte Prozessoren laufen aber weiterhin über den erzeugten pre>code-Block.

## Unverarbeiteten Text oder HTML einbinden

E> **Hinweis:** Diese Funktion ist für fortgeschrittene Benutzer.

Wollen Sie rohes HTML oder anderen Text einbinden, der nicht von MultiMarkdown (oder Ihrem benutzerdefinierten Prozessor) verarbeitet werden soll, verwenden Sie geschweifte Klammern (`{}`), um eine Datei *nach* der Verarbeitung des restlichen Dokuments einzubinden:

	<<{folder/raw_file.html}

In diesen Dateien wird keine Include-Syntax erkannt (keine Verschachtelung), und der **Rohinhalt** der Datei wird in die endgültige HTML-Ausgabe eingefügt. Das eignet sich hervorragend, um HTML einzufügen, ohne den Textprozessor auszubremsen oder Dinge konvertieren/maskieren zu lassen, wenn Sie das nicht wollen. Seien Sie aber vorsichtig: Es gibt kaum Sicherungen, die dafür sorgen, dass die Formatierung des Dokuments rund um das Eingefügte erhalten bleibt.

