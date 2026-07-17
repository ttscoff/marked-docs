# <%= @title %>

Hat eine über [Markeds Include-Syntax oder die iA-Writer-Block-Syntax][include] eingebundene Datei die Dateiendung `.csv` oder `.tsv`, versucht Marked, sie zu lesen und in eine MultiMarkdown-Tabelle umzuwandeln. Das klappt mit den meisten gängigen Formaten, also mit Komma- und Tabulator-Trennung ebenso wie mit weiteren Trennzeichen und Quoting-Varianten, die Marked automatisch erkennt.

Ein Vorteil von CSV-Dateien gegenüber handgeschriebenen Markdown-Tabellen: Zeilenumbrüche innerhalb einer Zelle werden automatisch in `<br>`-Tags umgewandelt. In einer MultiMarkdown-Tabelle müssten Sie diese Tags von Hand einfügen – CSV spart Ihnen also zusätzlich Zeit.

Am Rande: Es gibt eine hervorragende App namens [TableFlip][], die das Bearbeiten von Tabellen im Dokument erheblich vereinfacht. Sie ist einen Blick wert, wenn Sie häufig mit Tabellendaten arbeiten.

Eingebundene CSV-Dateien werden auf Änderungen überwacht: Sie arbeiten einfach in der ursprünglichen CSV-Datei weiter, und Marked aktualisiert die Vorschau beim Speichern automatisch.

Umgewandelte Tabellen landen auch im Markdown-Export. So stellen Sie mit Marked Dokumente mit strukturierten Daten zusammen und exportieren sie als eine einzige Datei.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/
