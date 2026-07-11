# <%= @title %>

Schwierige Ausdrücke auffangen und wichtige Phrasen hervorheben.

## Schlüsselwörter hervorheben

Durch die Schlüsselworthervorhebung in Marked können Sie häufig vorkommende Phrasen erkennen, die Sie vermeiden möchten, alternative Begriffe finden oder sie einfach für allgemeine Zwecke hervorheben. Die Liste der Schlüsselwörter, die für jede Kategorie verwendet werden, kann im {% prefspane Proofing %} bearbeitet werden.

Aktivieren Sie die Hervorhebung mit {% kbd shift cmd H %} im Zahnradmenü ({% appmenu {{gear}}, Schlüsselwörter hervorheben %}) oder öffnen Sie die Schlüsselwortschublade mithilfe des Markierungssymbols unten links (neben dem Zahnradmenü). Die Schublade kann auch mit der Tastenkombination {% kbd shift cmd K %} geöffnet werden. Die Hervorhebung wird beim Öffnen der Schublade automatisch aktiviert und kann mit dem Schalter auf der linken Seite der Schublade ein- und ausgeschaltet werden.

## Die Schlüsselwortschublade

![Keyword Drawer][kwd]

[kwd]: images/screenshots/mainwindow-feature-keywords-crop.jpg @2x width=1089px height=503px class=center

Die Schlüsselwortschublade, die beim Aktivieren der Hervorhebung angezeigt wird, bietet schnellen Zugriff auf Hervorhebungsoptionen, einschließlich der Möglichkeit, einzelne Hervorhebungstypen zu aktivieren und zu deaktivieren. Die vertikale Reihe farbiger Beschriftungen auf der linken Seite entspricht den Hervorhebungen im Text. Wenn Sie auf eine Beschriftung klicken, werden die Hervorhebungen für diesen Schlüsselworttyp umgeschaltet.

Links neben jeder Beschriftung befindet sich ein Zielsymbol. Wenn Sie darauf klicken, wird das Dokument zur nächsten Instanz der Hervorhebung in der Dokumentreihenfolge gescrollt. Rechts neben der Beschriftung wird die Gesamtzahl der Hervorhebungen für diesen Typ angezeigt.

Mit der Tastatur können Sie schnell durch die Highlights navigieren. Wenn Sie `[` und `]` eingeben, werden zunächst alle Hervorhebungen vorwärts und rückwärts durchlaufen. Wenn Sie auf ein Zielsymbol klicken, wechseln `[` und `]` zur Navigation genau dieser Art von Hervorhebung. `{` (Umschalttaste-[) und `}` (Umschalttaste-]) navigieren immer durch alle Hervorhebungen, unabhängig vom zuletzt angeklickten Ziel.

Wenn auf ein hervorgehobenes Wort oder eine hervorgehobene Phrase geklickt wird, wird dieser Typ zum Ziel für die Navigation und mit `[` oder `]` wird von diesem Punkt im Dokument aus navigiert.

## Schlüsselwörter bearbeiten

![Proofreading Settings][proofprefs]

  [proofprefs]: images/screenshots/preferences-Proofing.jpg @2x width=689px height=1031px class=preferencepane

Standardmäßig verwendet Marked die Liste [Plain English Campaign's](http://www.plainenglish.co.uk) mit häufig verwendeten Wörtern und Phrasen. Sie können diese einfach ergänzen oder ersetzen, indem Sie sie im {% prefspane Proofing %} bearbeiten. Jedes Feld ist Freiformtext und jede Zeile wird als Suchphrase interpretiert. Verwenden Sie `*` am Anfang einer Phrase oder eines Wortes, um einen beliebigen vorhergehenden Text zu finden, und `?`, um ein einzelnes Zeichen als Platzhalter zu finden.

Reguläre Ausdrücke können verwendet werden, indem der Ausdruck mit Schrägstrichen umgeben wird:

/\\Listig/

Das Obige entspricht allen Wörtern, die auf „ly“ enden, um sie hervorzuheben. Die Syntax für reguläre Ausdrücke in der Schlüsselworthervorhebung von Marked ist [same as JavaScript](http://www.regular-expressions.info/javascript.html).

## Temporäre Schlüsselwörter

Sie können der Schlüsselwortschublade auch temporäre Schlüsselwörter hinzufügen, indem Sie den Notizblock bearbeiten. Genau wie in den Feldern {% prefspane Proofing %} fügen Sie ein Schlüsselwort oder eine Phrase pro Zeile hinzu, wobei reguläre Ausdrücke zulässig sind (umgeben von Schrägstrichen). Klicken Sie nach der Bearbeitung temporärer Schlüsselwörter unbedingt auf die Schaltfläche „Aktualisieren“ (oder drücken Sie {% kbd cmd return  %}), um die Änderungen zu speichern und sie in Ihrem Dokument hervorgehoben anzuzeigen.

Reguläre Ausdrücke funktionieren auch im temporären Schlüsselwortfeld. Umgeben Sie den Text einfach mit Schrägstrichen (`/my expression\b/`).

Temporäre Schlüsselwörter sind für Situationen gedacht, in denen die Schlüsselwortdichte wichtig ist. Sie ermöglichen es Ihnen, schnell zu erkennen, wie oft Sie die Zielwörter verwendet haben, und ihre Positionen im Dokument hervorzuheben. Die Anzahl der Treffer für die temporären Schlüsselwörter wird gut sichtbar in der Schublade angezeigt.

Sehen Sie sich auch den Befehl ["Visualize Word Repetition"][wordrep] an, um überstrapazierte Wörter in Ihrem Text zu finden.

[wordrep]: Document_Statistics.html#visualizewordrepetition

## Passiv

Marked weist auf die Verwendung von „Passiv“ in englischen Texten hin. Als [defined by Wikipedia][passive]:

> Das grammatikalische Subjekt drückt das Thema oder den Patienten des Hauptverbs aus – also die Person oder Sache, die die Handlung erfährt oder deren Zustand sich ändert.

Passiv ist nicht böse, wie Sie über [in posts by linguist Geoffrey K. Pullum][gkp] lesen können. Marked weist auf Passagen im Passiv hin, die Entscheidung über deren Gültigkeit liegt jedoch bei Ihnen.

[passive]: https://en.wikipedia.org/wiki/Passive_voice
[gkp]: http://languagelog.ldc.upenn.edu/nll/?cat=54

## Doppelte Wörter

Doppelte Wörter (z. B. „the the“) werden automatisch orange hervorgehoben, wenn die Schlüsselworthervorhebung aktiviert ist. Dies ist derzeit nicht konfigurierbar, dürfte sich aber beim Korrekturlesen als nützlich erweisen.
