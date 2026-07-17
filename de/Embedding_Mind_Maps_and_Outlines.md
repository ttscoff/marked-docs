# <%= @title %>

Mindmaps und Gliederungen können mit [Markeds Include-Syntax][include] oder der [iA-Writer-Block-Syntax][ia] in Ihre Markdown-Vorschau eingebettet werden. Das Verhalten hängt vom Dateiformat ab und von den Kontrollkästchen pro Format unter **Als Mermaid-Mindmaps einbetten:** in {% prefspane Apps %} (*Mind Maps and Outlines*).

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Unterstützte Formate [supported-formats]

### iThoughts X (.itmz) [ithoughts-x-itmz]

iThoughts-Mindmap-Dateien sind ZIP-Archive, die Kartendaten und ein optionales Vorschaubild enthalten.

### MindManager (.mmap) [mindmanager-mmap]

MindManager-Dateien sind ZIP-Archive mit `Document.xml`. Entpackte MindManager-Pakete (ein Ordner mit `Document.xml`) und direkte Pfade zu `Document.xml` werden ebenfalls unterstützt.

### FreeMind (.mm) [freemind-mm]

FreeMind-Mindmap-Dateien verwenden die Erweiterung `.mm` und speichern Daten als XML. Marked erkennt das FreeMind-Format, indem es prüft, ob der Dateiinhalt mit `<map` beginnt; wenn nicht (z. B. ein Code-Snippet), wird die Datei als einfacher Text eingefügt. FreeMind-Dateien werden für die Einbettung von Mermaid-Mindmaps unterstützt.

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) ist ein XML-Format für hierarchische Gliederungen, das häufig von Outlinern und Feed-Readern verwendet wird. iThoughts und andere Apps können nach OPML exportieren. Marked konvertiert eingebundene OPML-Dateien in Mermaid-Mindmap-Diagramme.

### Bike (.bike) [bike-bike]

Bike.app-Gliederungen werden als proprietäre HTML-Dateien (`.bike`) gespeichert. Sie können eine `.bike`-Datei direkt in Marked öffnen: Das Dokument wird als Markdown mit dem Dateinamen (ohne Erweiterung) als Hauptüberschrift (H1), Überschriftenelementen der obersten Ebene als H2, verschachtelten Überschriften als fett gedruckten Listenelementen und Aufgaben als Kontrollkästchen im GitHub-Stil gerendert. Wenn eine `.bike`-Datei über die Include-Syntax eingebunden wird, steuert das Kontrollkästchen **Bike-Gliederungen** unter **Als Mermaid-Mindmaps einbetten:**, ob daraus eine Mermaid-Mindmap (mit dem Dateinamen als Stammknoten) oder eine verschachtelte Markdown-Liste (kein H1) wird.

### OmniOutliner (.ooutline) [omnioutliner-ooutline]

OmniOutliner-Gliederungen lassen sich genauso einbinden. Das Kontrollkästchen **OmniOutliner-Gliederungen** unter **Als Mermaid-Mindmaps einbetten:** steuert, ob als Mermaid oder als Markdown-Liste gerendert wird.

## Als Mermaid-Mindmaps einbetten [embed-as-mermaid-mind-maps]

Unter {% prefspane Apps %} gibt es bei *Mind Maps and Outlines* die Gruppe **Als Mermaid-Mindmaps einbetten:** mit einem Kontrollkästchen pro Format:

- **Bike-Gliederungen**
- **Mindmaps (iThoughts)** (deckt auch FreeMind und MindManager ab)
- **OPML-Dateien**
- **OmniOutliner-Gliederungen**

Ist das Kontrollkästchen eines Formats **aktiviert** (Standard bei den unterstützten Formaten), wandelt Marked eingebundene Dateien dieses Typs in [Mermaid](https://mermaid.js.org/)-Diagramme um:

**iThoughts, MindManager, FreeMind, OPML, Bike & OmniOutliner** – Gerendert als Mermaid-Mindmap-Diagramme mit dem Tidy-Tree-Layout. Bei iThoughts und MindManager bleiben Forminformationen (rund, rechteckig, sechseckig usw.) erhalten, sofern verfügbar. FreeMind (`.mm`) und OPML verwenden dasselbe Mindmap-Format. Bike-Gliederungen (`.bike`) verwenden den eingebundenen Dateinamen (ohne Erweiterung) als Mindmap-Stammknoten. Knotenbezeichnungen bestehen aus reinem Text (Links werden zu Linktext; Aufgaben werden als ☐ / ☑-Präfixe angezeigt). Mermaid ist standardmäßig in jeder Markdown-Vorschau enthalten.

**Einschränkung:** Das Einbetten von Mindmaps (Mermaid-Diagramme) funktioniert nicht mit dem Discount-Parser. Verwenden Sie MultiMarkdown, CommonMark (GFM) oder Kramdown für Mindmap-Vorschauen.

Ist das Kontrollkästchen eines Formats **deaktiviert**:

- **iThoughts** – Das integrierte Vorschaubild (`preview.png`) aus der .itmz-Datei ist als Base64-Bild eingebettet. Der Alternativtext des Bildes verwendet den Dateinamen.
- **MindManager** – Die Gliederung ist als verschachtelte Markdown-Liste eingebettet.
- **FreeMind** – Die Gliederung ist als verschachtelte Markdown-Liste eingebettet.
- **OPML** – Die Gliederung ist als verschachtelte Markdown-Liste eingebettet (keine Mindmap).
- **Bike** – Die Gliederung ist als verschachtelte Markdown-Liste eingebettet (kein H1); Überschriftenelemente der obersten Ebene werden zu H2, verschachtelte Überschriften werden fett dargestellt und Aufgaben werden zu GitHub-Kontrollkästchen.
- **OmniOutliner** – Die Gliederung ist als verschachtelte Markdown-Liste bzw. Checkliste eingebettet.

## Include-Syntax [include-syntax]

Verwenden Sie die gleiche Syntax wie für andere Datei-Includes:

	<<[path/to/map.itmz]
	<<[path/to/map.mmap]
	<<[path/to/map.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]

Oder mit iA Writer-Blocksyntax:

	/path/to/map.itmz

Pfade können relativ zum Hauptdokument oder absolut sein (beginnend mit `/` oder `~`). Weitere Informationen finden Sie unter [Mehrteilige Dokumente](Multi-File_Documents.html).

## OPML-Konvertierung [opml-conversion]

OPML-Dateien verwenden verschachtelte `<outline>`-Elemente mit einem `text`-Attribut. Ist **OPML-Dateien** unter **Als Mermaid-Mindmaps einbetten:** aktiviert (siehe [Einstellungen: Apps](Settings_Apps.html)), erzeugt die Konvertierung eine Mermaid-Mindmap im gleichen Format wie iThoughts und MindManager:

- Untergeordnete Gliederungen von `<body>` werden zur obersten Ebene (oder zu Kindern eines „Outline“-Stamms, wenn es mehrere Elemente der obersten Ebene gibt)
- Verschachtelte Gliederungen definieren die Hierarchie
- Fehlendes oder leeres `text` wird als `(unnamed)` angezeigt
- Text wird bereinigt; Sonderzeichen werden für Mermaid maskiert

## Bike-Konvertierung [bike-conversion]

Bike-`.bike`-Dateien sind HTML mit einem Stammelement `<ul>` und `<li>`. Elemente können `data-type="heading"` (oberste Ebene → H2 beim Öffnen oder im Listenmodus; verschachtelt → fett) oder `data-type="task"` (GitHub-Kontrollkästchen; abgeschlossen, wenn `data-done` einen Zeitstempel hat oder `data-checked` / `data-completed` wahr ist). Inline-Formatierungen und Links im Knotentext werden in Markdown konvertiert. Beim Einbetten als Mermaid-Mindmap wird der Dateiname (ohne Erweiterung) als einzelner Stammknoten verwendet und die Beschriftungen sind als einfacher Text für die Mermaid-Mindmap-Syntax formatiert.
