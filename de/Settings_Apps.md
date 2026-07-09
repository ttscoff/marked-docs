# <%= @title %>

Optionen unter {% prefspane Apps %}:

(Siehe [Zusätzliche App-Unterstützung](Additional_Application_Support.html))

![Einstellungen: Apps][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Allgemeine Einstellungen

Texteditor
: Wählen Sie einen Texteditor, der das aktuelle Dokument erhält, wenn Sie {% kbd cmd E %} drücken.

Neue Dateien automatisch bearbeiten
: Beim Befehl „Neue Datei“ öffnet diese Option die erstellte Datei automatisch in Ihrem gewählten externen Editor.

Textdatei-Links öffnen in:
: Legt fest, wie sich Marked verhält, wenn ein in einem Vorschaufenster angeklickter Link zu einer lokalen Textdatei führt.

Bildeditor
: Wählen Sie eine Anwendung, die geöffnet wird, wenn Sie mit Rechtsklick auf ein lokales Bild „Bild bearbeiten“ wählen.

Bildanmerkungs-/Markup-Editor
: Wählen Sie eine Anwendung, die geöffnet wird, wenn Sie mit Rechtsklick auf ein lokales Bild „Bild kommentieren“ wählen.

Ist kein Editor gewählt, zeigt Marked beim Bearbeiten oder Kommentieren ein Menü der installierten Anwendungen. Das Menü enthält gängige Markdown-, Bild- und Anmerkungswerkzeuge, die auf Ihrem Mac gefunden werden, eine Option **Andere…**, um eine beliebige App aus `/Applications` zu wählen, und **Diese App immer verwenden** (standardmäßig aktiviert), um Ihre Wahl als Standard zu speichern. Über die Löschen-Schaltfläche (Kreis mit X) neben jedem Auswählen-Steuerelement unter {% prefspane Apps %} entfernen Sie eine Auswahl und kehren zur Übersicht zurück.

### Anwendungsspezifische Einstellungen

Kommentare und Anmerkungen standardmäßig anzeigen
: Ist dies aktiviert, erscheinen in Scrivener-, Fountain-, Word- und CriticMarkup-Dokumenten gemachte Anmerkungen hervorgehoben in der Vorschau. Deaktivieren, um sie ganz auszublenden. Beim Lesen eines Dokuments lassen sie sich auch über das Menü {% appmenu {{gear}}, Korrekturlesen ({{ctrl}}{{cmd}}C) %} umschalten.
: Sind Kommentare aktiviert, erscheinen Kommentare und Fußnoten in einer Seitenleiste. Fahren Sie über einen Kommentar, wird auf seine Stelle im Dokument verwiesen.

#### DocC

[(Infos zur DocC-Unterstützung)](DocC_Support.html)

DocC-Bildverweise auflösen
: Löst innerhalb eines `.docc`-Dokumentationskatalogs erweiterungslose `![](ImageName)`-Verweise auf Bilder im `Resources`-Ordner des Katalogs auf, einschließlich `~dark`- und `@2x`-Varianten.

Dunkle und @2x-Bildvarianten auflösen
: Erkennt bei lokalen Bildern mit Dateierweiterung (`images/icon.png`) zugehörige `~dark`- und `@2x`-Dateien im selben Ordner und erzeugt responsives `<picture>`-Markup. Funktioniert in jedem Markdown- oder HTML-Dokument, nicht nur in DocC-Katalogen. Siehe [Bildvarianten](Image_Variants.html).

#### Hookmark

hook://-URLs in Bildern und Links auflösen
: Marked kann von Hookmark erzeugte URLs lesen und zu ihrem Pfad auf der Festplatte auflösen.

#### Leanpub/GitBook

Leanpub-Unterstützung aktivieren
: Interpretiert Dateien namens `Book.txt` als Indexdateien und verarbeitet spezielle Leanpub-Syntax.

GitBook-Unterstützung aktivieren
: Interpretiert Dateien namens `SUMMARY.md` als Indexdateien für GitBook-Dokumentation.

#### Markdownifier

Inline-Links verwenden
: Vom Markdownifier erstellte Markdown-Dokumente verwenden Inline- statt Referenzlinks.

#### MarsEdit

Beitragstitel als Markdown-Überschrift (h1) einfügen
: Verwendet den Titel des ausgewählten Beitrags als Markdown-Überschrift.

Metadaten als Tabelle anzeigen
: Ist dies aktiviert, werden Metadaten wie Kategorien und Titel als Markdown-Tabelle in der Vorschau angezeigt.

#### Ordner

Nur diese Erweiterungen in der Vorschau anzeigen
: Beim Öffnen eines Ordners sucht Marked das zuletzt geänderte Dokument und greift dabei standardmäßig auf Erweiterungen wie `md`, `mmd` und `html` zurück. Die Liste hier überschreibt die Standardeinstellung.

#### Scrivener

[(Infos zur Scrivener-Unterstützung)](Scrivener_Support.html)

Dokumenttitel als Markdown-Überschriften einfügen
: Wertet die Titel von Seiten und verschachtelten Seiten aus, um hierarchische Markdown-Überschriften zu erzeugen.

Kompilierungsmetadaten (Titel, Autor) hinzufügen, wenn diese fehlen
: Hat ein Scrivener-Projekt kein `metadata`-Dokument und keinen vorhandenen MultiMarkdown-Header, werden Titel und Autor aus den Kompilierungseinstellungen des Projekts (`Settings/compile.xml`) vorangestellt.

.scriv-Dateien in Scrivener öffnen, wenn sie in Marked geöffnet werden
: Wird ein Scrivener-Dokument in Marked geöffnet, wird es automatisch auch in Scrivener geöffnet.

#### Word

Änderungsverfolgung <-> CriticMarkup konvertieren
: Ist dies aktiviert, wird die Änderungsverfolgung in Word-Dokumenten beim Import in CriticMarkup umgewandelt, und CriticMarkup wird beim Export von DOCX-Dateien in die Word-Änderungsverfolgung umgewandelt.

#### Mindmaps/Gliederungen {#MindMapsOutlines}

Als Mermaid-Mindmaps einbetten
: Jedes Kontrollkästchen steuert ein eingebundenes Format. Ist es **ein**, wird die eingebundene Datei in ein Mermaid-Mindmap-Diagramm (Tidy-Tree-Layout) umgewandelt. Ist es **aus**, verwendet Marked die Alternative für dieses Format.
: **Mindmaps** – iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). Ein: Mermaid-Mindmap. Aus: iThoughts bindet sein Vorschaubild ein; MindManager und FreeMind werden in verschachtelte Markdown-Listen umgewandelt.
: **OPML-Dateien** (.opml). Ein: Mermaid-Mindmap. Aus: verschachtelte Markdown-Liste.
: **OmniOutliner-Gliederungen** (.ooutline). Ein: Mermaid-Mindmap. Aus: verschachtelte Markdown-Liste (oder Checkliste, wo zutreffend).
: **Bike-Gliederungen**. Ein: Mermaid-Mindmap. Aus: verschachtelte Markdown-Liste.
