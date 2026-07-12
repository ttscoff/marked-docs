# <%= @title %>

Zahlen sind genauso wichtig wie Worte.

## Formeln mit MathJax in der Vorschau

![][1]

   [1]: images/mathjax.jpg @2x width=713px height=512px class=center

Wenn Sie MathJax unter {% prefspane Style %} aktivieren, werden die nötigen Skripte und das CSS in die Vorschau eingebunden. Dann können Sie in Ihrem Markdown-Dokument die MultiMarkdown-Mathe-Syntax verwenden, und die Ergebnisse werden angezeigt.

Beispiel für MMD-MathJax-Syntax:

    \\\\[ {e}^{i\pi } 1=0 \\\\]

Wenn Sie MathJax in eine exportierte HTML-Datei aufnehmen, wird statt des eingebetteten MathJax-Codes ein CDN-Link verwendet. Zum Anzeigen des gerenderten MathML ist dann eine Internetverbindung nötig.

## MathJax-Quelle: Lokal oder CDN

Bei aktiviertem MathJax kann Marked es aus einer von zwei Quellen laden:

- **Lokal**: eine in der App gebündelte Kopie von MathJax v3 (lädt schneller, funktioniert offline).
- **CDN**: das offizielle MathJax-v3-CDN (immer aktuell, ohne Einfluss auf die App-Größe).

Über das Aufklappmenü **MathJax-Quelle** unter {% prefspane Style %} wählen Sie:

- **Lokal** – verwendet die ES5-Komponente `tex-chtml.js` aus dem App-Bundle.
- **CDN** – lädt dieselbe Komponente vom CDN. Dafür ist eine Internetverbindung nötig.

Exportierte HTML-Dateien beziehen MathJax immer von einem CDN, unabhängig von der Vorschau-Quelle, sodass sie eigenständig und klein bleiben.

## Gleichungsnummerierung

Die Gleichungsnummerierung aktivieren Sie unter {% prefspane Style %}. Das funktioniert mit MathJax und KaTeX, ist intern aber unterschiedlich umgesetzt. Für MathJax v3 überträgt Marked Ihre Einstellungen in die passende MathJax-Konfiguration, sodass gilt:

- „Gleichungen nummerieren“ steuert, ob überhaupt Nummern angezeigt werden.
- Die Option „Seite“ steuert, ob die Nummern links oder rechts erscheinen.
- Die Option „Nur AMS“ beschränkt die Nummerierung auf Gleichungen im AMS-Stil.

Diese Optionen entsprechen im Hintergrund den MathJax-Einstellungen `tex.tags` und `tex.tagSide`.

## Zusätzliche Pakete

MathJax v3 ist modular aufgebaut. Marked aktiviert immer die TeX/AMS-Kernpakete; zusätzliche Pakete können Sie optional unter {% prefspane Style %} einschalten:

- **Physik** (`physics`) – physikalische Notation und praktische Kurzbefehle.
- **Chemie** (`mhchem`) – Chemie-Gleichungen.
- **Bra–ket** (`braket`) – Diracsche Bra-ket-Notation.
- **Fette Symbole** (`boldsymbol`) – fette mathematische Symbole.

Klicken Sie auf **Zusätzliche Pakete…**, um eine kleine Auswahlliste zu öffnen, in der Sie diese Pakete ein- oder ausschalten. Änderungen greifen, sobald Marked das nächste Mal Mathematik in der Vorschau rendert.

## Erweiterte MathJax-Konfiguration

Zusätzlich zu Markeds Standardeinstellungen können Sie eigene Konfigurationen anwenden, indem Sie im Feld **Erweiterte Konfiguration** ein gültiges JSON-Objekt hinzufügen. Dieses Feld wird vor dem Laden von MathJax in das MathJax-v3-Konfigurationsobjekt (`window.MathJax`) eingefügt. Es kann [beliebige von MathJax v3 unterstützte Optionen](https://docs.mathjax.org/en/latest/options/) enthalten, zum Beispiel:

    {
        "tex": {
            "inlineMath": [["$","$"],["\\\\(","\\\\)"]],
            "displayMath": [["$$","$$"],["\\\\[","\\\\]"]],
            "macros": {
                "tr": "{\\\\scriptscriptstyle\\\\mathrm{T}}"
            },
            "packages": { "[+]": ["physics"] }
        }
    }

Dieses Beispiel passt die TeX-Trennzeichen an, fügt ein `\tr`-Makro hinzu und aktiviert zusätzlich zum Standardsatz das `physics`-Paket. Mit diesen Einstellungen wird alles Folgende korrekt gerendert:

    Inline formula using parens, \\\\({x}^{2} {y}^{2}=1\\\\), or with dollar signs, ${x}^{2} {y}^{2}=1$.

    Display with escaped brackets:

    \\\\[ {e}^{i\pi } 333=0 \label{testme} \\\\]

    Or with double dollar signs:

    $${x}_{1,2}=\\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a}$$

![][2]

   [2]: images/mathjax2.jpg @2x width=837px height=260px class=center

Die zusätzliche Konfiguration erweitert das bestehende Objekt, sodass nur die angegebenen Eigenschaften überschrieben werden. Nicht angegebene Optionen behalten den Standardwert des aktuellen Presets.

Beachten Sie: Beim MultiMarkdown-Prozessor mit nicht standardmäßigen Trennzeichen werden Zeichen innerhalb des Ausdrucks interpretiert, sodass Symbole wie `*` und `^` typografische Änderungen auslösen, die den MathJax-Prozessor durcheinanderbringen. Am besten verwenden Sie in solchen Fällen den Discount-Prozessor in den [Prozessor-Einstellungen](x-marked-3://pref/processor).

Marked vollführt etwas Magie, sobald MathJax oder KaTeX aktiviert ist, und wandelt die Mathe-Syntax so um, dass sie möglichst gut mit dem aktuellen Prozessor (MultiMarkdown oder Discount) verträglich ist. Das sollte in allen Fällen gut klappen; falls es doch Probleme macht, [kontaktieren Sie den Support](https://support.markedapp.com/questions/add)!


## KaTeX

[katex]: https://katex.org/

[KaTeX][] steht als Alternative zu MathJax bereit. Es ist leichtgewichtiger und lädt daher schneller, was bei Dokumenten mit vielen Formeln von Vorteil sein kann. Dafür hat es weniger Funktionen, und manche Gleichungen, die mit MathJax (oder LaTeX) funktionieren, werden womöglich nicht unterstützt.

## Automatische Gleichungsnummerierung [numbering]

Die Gleichungsnummerierung aktivieren Sie unter {% prefspane Style %}. Das funktioniert mit MathJax und KaTeX. Sie können wählen, ob die Nummern links oder rechts neben der Gleichung erscheinen.

### In MathJax

In MathJax wird dafür diese Einstellung verwendet:

    {
      TeX: { equationNumbers: { autoNumber: "all" } }
    }

Wenn Sie nur AMS-Gleichungen nummerieren möchten, wählen Sie „Nur AMS“ rechts neben dem Aufklappmenü „Seite“.

### In KaTeX

KaTeX bietet keine Gleichungsnummerierung. Um sie in Marked nachzubilden, wird CSS verwendet, und alle abgesetzten Gleichungen werden nummeriert.

## Exportprobleme

Rich-Text-Formate können keine Gleichungen darstellen (weder über MathJax noch über KaTeX). Sie werden im Ausgabedokument ausgeblendet, denn der Versuch, die speziellen Schriftarten einzubetten, führt zu einem größeren Chaos, als man sich vorstellen mag … Das möchte ich irgendwann beheben, im Moment ist es aber eine Einschränkung.

