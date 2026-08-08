# <%= @title %>

Behalten Sie beim Schreiben den Überblick.

## Wortanzahl und Dokumentstatistik [word-count-and-document-statistics]

![][1]

   [1]: images/WordCount.jpg @2x width=840px height=61px class=center

Die Wortzählung befindet sich in der unteren Statusleiste und kann über {% prefspane General %} unter der Statusleiste aktiviert und deaktiviert werden. Sie können weitere Statistiken im Vorschau- oder Quellfenster über das Zahnradmenü anzeigen, indem Sie auf die Wortanzahl klicken oder Option-Befehl-S ({% kbd opt cmd S %}) eingeben. Halten Sie beim Klicken die Wahltaste ({% kbd opt  %}) gedrückt, um die Lesbarkeitsstatistik anzuzeigen, und halten Sie die Wahltaste ({% kbd opt cmd %}) gedrückt, um das Bedienfeld „Erweiterte Statistiken“ zu öffnen.

Wenn Text ausgewählt ist, werden die Anzeige der Wortanzahl und das Popup-Fenster für Absätze/Sätze/Zeichen mit Informationen nur für die Auswahl aktualisiert.

## Wortanzahl für die Auswahl [word-count-for-selection]

![Word count popup on text selection][2]

   [2]: images/wordcountforselection.jpg @2x width=749px height=144px class=center

Wenn Sie Text in der Vorschau auswählen, zeigt die Wortanzahl am unteren Rand des Fensters Statistiken nur für den ausgewählten Text an.

Wenn „Wortanzahl für Auswahl anzeigen“ im {% prefspane Preview %} aktiviert ist, wird neben dem Cursor ein kleines Popup angezeigt, das die Wort-/Zeilen-/Zeichenanzahl für den ausgewählten Text anzeigt. Dies wird einfach dadurch beseitigt, dass Sie die Maus vom Popup wegbewegen.

Die Zoomfunktion ist praktisch, um größere Textabschnitte schnell auszuwählen und zu zählen. Geben Sie {% kbd z %} ein, um herauszuzoomen und Ihre Auswahl zu treffen.

## Lesbarkeitsstatistik [readability-statistics]

![Readability stats bar][3]

   [3]: images/screenshots/mainwindow-feature-stats-lower-crop.jpg @2x width=1089px height=111px class=center

Zusätzliche Statistiken von Flesch/Kincaid und dem Nebelindex sind mit {% kbd opt shift cmd S %} verfügbar.

### Informationen zur Lesbarkeit [readability-information]

**Flesch Reading Ease:** Höhere Werte kennzeichnen leichter lesbare Texte; niedrigere Werte weisen auf schwierigere Passagen hin.

**90,0–100,0**: durchschnittlicher 11-jähriger Schüler
**60,0–70,0**: 13- bis 15-jährige Schüler
**0,0–30,0**: Hochschulabsolventen

**Flesch-Kincaid-Klassenstufe:** Die Anzahl der Schuljahre, die im Allgemeinen erforderlich sind, um diesen Text zu verstehen.

**Gunning Fog Index:** misst die Lesbarkeit englischer Schrift. Der Index schätzt die Jahre der formalen Bildung, die erforderlich sind, um den Text beim ersten Lesen zu verstehen. Ein Nebelindex von 12 erfordert das Leseniveau eines US-amerikanischen Oberstufenschülers (ca. 18 Jahre alt).

## Erweiterte Statistiken [advanced-statistics]

![Advanced Statistics popup][adv]

[adv]: images/screenshots/mainwindow-feature-stats-info-crop.jpg @2x width=800px height=800px class=center

Wenn Sie im Zahnradmenü „Erweiterte Statistiken“ auswählen oder {% kbd cmd I %} drücken, wird ein Bereich mit erweiterten Dokumentstatistiken angezeigt, darunter die durchschnittliche Wort- und Satzlänge sowie die durchschnittliche Wortkomplexität.

### Schwebende erweiterte Statistiken [floating-advanced-statistics]

![Floating Info Window][floating]

[floating]: images/floatinginfo.jpg @2x width=999px height=522px class=center

Durch Drücken von {% kbd shift cmd I %} wird ein schwebendes Fenster mit allen detaillierten Statistiken und Lesbarkeitsinformationen geöffnet. Dieses Bedienfeld kann im Vordergrund bleiben, wenn Sie zu Ihrem Editor wechseln, sodass Sie sehen können, wie Ihre Statistiken bei jedem Speichern aktualisiert werden, unabhängig davon, ob die Vorschau sichtbar ist oder nicht. Durch Drücken des Symbols `<` wird die zugehörige Marked-Vorschau wieder in den Vordergrund gerückt. Wenn Sie die Optionstaste gedrückt halten und auf dieselbe Schaltfläche klicken, wird die Datei Markdown in Ihrem Standardtexteditor geöffnet (eingestellt in {% prefspane Apps %}).

### Wortziele [word-targets]

Wenn Sie beim Schreiben ein bestimmtes Ziel für die Wortzahl haben, können Sie oben in Ihrem Dokument einen Metadatenschlüssel „Ziel:“ hinzufügen. Marked verfolgt dann Ihren Fortschritt und zeigt einen Abschlussindikator im Bereich „Detaillierte Statistiken“ ({% kbd cmd I %}) und in den schwebenden Statistiken ({% kbd shift cmd I %}) an.

![][targetwordcount]

[targetwordcount]: images/wordtargets.jpg @2x width=740px height=191px class=center


## Wortwiederholungen visualisieren [visualizewordrepetition]

Wenn Sie im Zahnradmenü „Wortwiederholung visualisieren“ auswählen (oder {% kbd ctrl cmd W %} drücken), wird zu einer speziellen Ansicht gewechselt, die Nicht-Textelemente entfernt und Wörter hervorhebt, die in Ihrem Dokument wiederholt werden. Wiederholte Wörter werden hellrosa hervorgehoben. Wenn Sie mit der Maus über ein hervorgehobenes Wort fahren, werden die übereinstimmenden Wörter im gesamten Dokument heller hervorgehoben. Wenn Sie auf ein hervorgehobenes Wort klicken, wird der Hintergrund abgedunkelt und die Hervorhebung bleibt zur weiteren Überprüfung erhalten.

![Word Repetition][4]

[4]: images/screenshots/mainwindow-word-repetition.jpg @2x width=1369px height=1084px

Sie können in diesem Modus auch die „Zoom“-Funktion (Typ „z“) verwenden, mit der Sie ein wiederholtes Wort hervorheben und dann schnell das gesamte Dokument scannen können, um zu sehen, wo sich die Wiederholungen konzentrieren.

Wörter werden anhand ihres „Stamms“ verglichen, was bedeutet, dass „Teil“, „teilweise“ und „Teile“ als wiederholte Wörter betrachtet werden. Dies berücksichtigt Silben und Konjugation bei der Überprüfung der Wiederholungsdichte.

**Umfang**

Der Umfang der Wiederholungsprüfung kann in der unteren Symbolleiste des Dokuments geändert werden und auf Dokument oder Absatz eingestellt werden. Der Dokumentmodus ist Standard; Wenn Sie „Absatz“ auswählen, werden nur Wiederholungen innerhalb jedes Textblocks gezählt. Wiederholungen werden weiterhin im gesamten Dokument hervorgehoben, aber nur gezählt, wenn ein Wort mehr als einmal in einem einzelnen Absatz vorkommt.

**Wörter ignorieren**

Sie können ein Wort und alle seine verschiedenen Konjugationen und Pluralisationen vorübergehend ausschließen, indem Sie bei gedrückter Wahltaste auf das markierte Wort klicken. Vorübergehend ignorierte Wörter werden in der unteren rechten Ecke der Vorschau angezeigt. Durch Klicken auf ein Wort in der Liste der ignorierten Wörter wird es in der Visualisierung wiederhergestellt.

Um Wörter dauerhaft zu ignorieren, können Sie eine Liste im {% prefspane Proofing %} auf der Registerkarte „Wiederholungen ignorieren“ bearbeiten. Wörter (oder Wortstämme), die dieser Liste einzeln pro Zeile hinzugefügt werden, werden immer ignoriert. Um dieser Liste automatisch ein Wort hinzuzufügen, klicken Sie bei gedrückter Wahltaste und Umschalttaste in der Wortwiederholungsvisualisierung darauf.

**Wortwiederholungsmodus verlassen**

Sie können die Wortwiederholungsansicht schließen, indem Sie das Symbol „Schließen“ neben der Bereichsauswahl in der unteren Symbolleiste verwenden oder die Escape-Taste drücken.
