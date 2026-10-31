# <%= @title %>

W> **Die Apex-Unterstützung in Marked ist in der Beta-Phase.** Das Verhalten kann sich ändern, während die Integration reift. Probleme, unerwartete Darstellung oder fehlende Syntax melden Sie bitte unter [support.markedapp.com](https://support.markedapp.com).

Apex ist ein **vereinheitlichter Markdown-Prozessor**: eine einzige Engine, die die Funktionen abdecken will, für die man sonst CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown oder Kramdown wählt – ohne die jeweils anderen Varianten aufzugeben.

In Marked läuft **Apex (Beta)** immer im **vereinheitlichten** Modus von Apex (alle diese Funktionsfamilien gleichzeitig aktiv). Einen eigenen „CommonMark-Modus“ oder „Kramdown-Modus“ von Apex wählen Sie in Marked noch nicht; das kann später kommen.

Im [Markdown-Dingus](x-marked-3://dingus?processor=apex) können Sie mit Apex experimentieren. Eine kompakte Übersicht finden Sie unter {% appmenu Hilfe, Markdown-Referenz %} im Reiter **Apex**.

---

## Warum es Apex gibt [why-apex-exists]

Die Markdown-„Varianten“ haben sich aus guten Gründen auseinanderentwickelt – GitHub brauchte Aufgabenlisten und Tabellen, MultiMarkdown Fußnoten und Metadaten, Kramdown Attributlisten –, doch wer sich für einen Prozessor entscheidet, verzichtet meist auf die Syntax eines anderen.

Apex will diese Erweiterungen **zusammenführen**, sodass ein einziges Dokument Folgendes nutzen kann:

- gewohnte CommonMark-/GFM-Schreibweisen (abgegrenzter Code, Aufgabenlisten, Durchstreichung, GFM-Tabellen)
- Fußnoten, Abkürzungen und Metadaten im MultiMarkdown-Stil
- Kramdown-freundliche Definitionslisten, Mathematik und (für Fortgeschrittene) Attributlisten
- auf Marked zugeschnittene Annehmlichkeiten wie Callouts, CriticMarkup und Inhaltsverzeichnis-Marker

Die vollständige Dokumentation des Projekts steht im [Apex-Wiki](https://github.com/ApexMarkdown/apex/wiki). Diese Seite behandelt, was Sie im Alltag in Markeds Vorschau brauchen.

---

## Apex in Marked aktivieren [enabling-apex-in-marked]

1. Öffnen Sie {% prefspane Processor %}.
2. Stellen Sie **Markdown verarbeiten mit** auf **Apex (Beta)**.
3. Oder legen Sie es pro Dokument über Metadaten fest, etwa `Processor: apex` (Aliasse: `apex-beta`, `unified`).

Die Aliasse funktionieren auch in AppleScript, in den Conductor-Aktionen „Prozessor ausführen“, in der Standardausgabe eines benutzerdefinierten Prozessors (`APEX`) und in `x-marked://`-URLs für Voreinstellungen.

T> In dieser Beta löst Marked seine eigenen Dateieinbindungen (`<<[file]` und verwandte Marked-Include-Pfade) weiterhin auf, bevor Apex läuft. Die native Include-Engine von Apex bleibt in Marked wegen der Sandbox ausgeschaltet. Nutzen Sie die Einbindungsfunktionen von Marked wie gewohnt.

---

## Grundlegende Syntax, die Apex ergänzt oder vereinheitlicht [basic-syntax]

Standard-Markdown (Überschriften, Hervorhebung, Links, Bilder, Listen, Blockzitate, Code) funktioniert wie erwartet. Die folgenden Punkte sind die Extras, die beim Umstieg auf Apex am häufigsten gebraucht werden.

### Aufgabenlisten [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Durchstreichung [strikethrough]

```markdown
~~removed text~~
```

### Tabellen [tables]

GFM-Pipe-Tabellen mit Trennzeile unter der Kopfzeile und Spaltenausrichtung:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Erweiterte Tabellenfunktionen (Zeilenverbund `^^`, Spaltenverbund, Beschriftungen, Gittertabellen, CSV) sind im Wiki beschrieben: [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Fußnoten [footnotes]

Im Referenzstil:

```markdown
See the note[^1].

[^1]: Footnote text.
```

Die aus MultiMarkdown und Kramdown bekannten Inline-Schreibweisen werden ebenfalls unterstützt. Einzelheiten: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Definitionslisten [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Hoch- und Tiefstellung [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Mathematik [math]

Inline `$x^2$` und abgesetzt `$$...$$` (die Darstellung in der Vorschau steuern weiterhin Markeds MathJax-/KaTeX-Einstellungen).

### Callouts [callouts]

Im Stil von Obsidian und Bear:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Siehe auch Markeds [Marked-Spezialsyntax](Special_Syntax.html) und die Wiki-Seite [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts) von Apex.

### CriticMarkup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Aktivieren Sie CriticMarkup in Marked wie gewohnt; Apex kann die Critic-Syntax in der Verarbeitungskette darstellen. Siehe [CriticMarkup](CriticMarkup.html).

### Abkürzungen [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Emoji-Kurzcodes [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadaten [metadata]

YAML-Front-Matter, Kopfzeilen im MultiMarkdown-Stil (`Key: Value`) und Pandoc-Titelblöcke werden erkannt. Werte fügen Sie, wo unterstützt, mit `[%key]` ein.

Einzelheiten zur Konfiguration im Wiki: [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) und [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms).

### Inhaltsverzeichnis-Marker [table-of-contents-markers]

Apex versteht gängige Marker für Inhaltsverzeichnisse, darunter:

- `<!--TOC-->`
- `{{TOC}}` oder `{{TOC:2-4}}`
- `{:toc}` im Kramdown-Stil

Eine Überschrift schließen Sie mit `{:.no_toc}` aus, wo IAL verfügbar ist. Mehr: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Spezielle Marker [special-markers]

Auf Marked zugeschnittene HTML-Kommentare wie `<!--BREAK-->` (Seitenumbruch) und `<!--PAUSE:N-->` (Autoscroll) funktionieren auch in Apex-Vorschauen weiter.

---

## Fortgeschrittene Themen (Wiki) [advanced-topics-wiki]

Für Funktionen, die mächtig, im Vorschau-Alltag aber seltener sind, nutzen Sie das [Apex-Wiki](https://github.com/ApexMarkdown/apex/wiki):

| Thema | Wiki |
|------|------|
| Indexerstellung | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Zitate / Literaturverzeichnis | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Inline-Attributlisten, Spans, abgegrenzte Divs | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Dokumente aus mehreren Dateien und Einbindungen | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Formate für Überschriften-IDs | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Bilder in mehreren Formaten | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Kompatibilitätsmodi (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugins und Filter | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Siehe auch [see-also]

- [Prozessor wählen](Choosing_a_Processor.html) – wann MultiMarkdown, CommonMark, Kramdown, Discount oder Apex die richtige Wahl ist
- [Einstellungen: Verarbeitung](Settings_Processor.html)
- [Markdown-Dingus](Markdown_Dingus.html)
- [Startseite des Apex-Wikis](https://github.com/ApexMarkdown/apex/wiki)
- Probleme melden: [support.markedapp.com](https://support.markedapp.com)
