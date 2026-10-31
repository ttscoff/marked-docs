# <%= @title %>

W> **Apex-ondersteuning in Marked is in bèta.** Het gedrag kan nog veranderen naarmate de integratie verder uitrijpt. Meld problemen, onverwachte weergave of ontbrekende syntax via [support.markedapp.com](https://support.markedapp.com).

Apex is een **uniforme Markdown-processor**: één engine die de functies probeert te bieden waarvoor mensen doorgaans CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown of Kramdown kiezen --- zonder de andere varianten los te laten.

In Marked draait **Apex (bèta)** altijd in Apex's **uniforme** modus (al die functiefamilies samen ingeschakeld). Je kiest in Marked nog geen aparte Apex-"CommonMark-modus" of "Kramdown-modus"; dat kan later nog komen.

Bekijk de [Markdown Dingus](x-marked-3://dingus?processor=apex) om met Apex te experimenteren, of open {% appmenu Help, Markdown Reference %} en kies het tabblad **Apex** voor een compact spiekbriefje.

---

## Waarom Apex bestaat [why-apex-exists]

Markdown-"varianten" zijn om goede redenen uit elkaar gegroeid --- GitHub had takenlijsten en tabellen nodig, MultiMarkdown had voetnoten en metadata nodig, Kramdown had attribuutlijsten nodig --- maar als je voor één processor kiest, moet je meestal de syntax van een andere loslaten.

Apex heeft als doel die uitbreidingen te **bundelen**, zodat één document kan gebruikmaken van:

- Alledaagse CommonMark/GFM-gewoontes (fenced code, takenlijsten, doorhalen, GFM-tabellen)
- Voetnoten, afkortingen en metadata-gewoontes in MultiMarkdown-stijl
- Kramdown-vriendelijke definitielijsten, wiskunde en (voor gevorderd gebruik) attribuutlijsten
- Marked-georiënteerde extraatjes zoals callouts, Critic Markup en TOC-markeringen

De volledige documentatie van de bron vind je op de [Apex-wiki](https://github.com/ApexMarkdown/apex/wiki). Deze pagina behandelt wat je dagelijks nodig hebt in de preview van Marked.

---

## Apex inschakelen in Marked [enabling-apex-in-marked]

1. Open {% prefspane Processor %}.
2. Zet **Standaard Markdown-processor** op **Apex (bèta)**.
3. Of overschrijf dit per document met metadata zoals `Processor: apex` (aliassen: `apex-beta`, `unified`).

Aliassen werken ook vanuit AppleScript, Conductor-acties "Run Processor", de stdout van een aangepaste processor (`APEX`), en standaard-URL's van `x-marked://`.

T> In deze bèta breidt Marked nog steeds zijn eigen bestandsincludes uit (`<<[file]` en gerelateerde Marked-includepaden) voordat Apex draait. Apex's eigen include-engine staat in Marked uitgeschakeld, met het oog op sandboxing. Gebruik gewoon de includefuncties van Marked zoals je al deed.

---

## Basissyntax die Apex toevoegt of verenigt [basic-syntax]

Standaard Markdown (koppen, nadruk, links, afbeeldingen, lijsten, blockquotes, code) werkt zoals je zou verwachten. Hieronder staan de extra's die mensen het vaakst nodig hebben bij de overstap naar Apex.

### Takenlijsten [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Doorhalen [strikethrough]

```markdown
~~removed text~~
```

### Tabellen [tables]

GFM-tabellen met verticale strepen, kopscheidingen en kolomuitlijning:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Geavanceerde tabelfuncties (rowspan `^^`, colspan, bijschriften, rastertabellen, CSV) staan gedocumenteerd op de wiki: [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Voetnoten [footnotes]

In referentiestijl:

```markdown
See the note[^1].

[^1]: Footnote text.
```

Inline-stijlen die je kent van MultiMarkdown/Kramdown worden ook ondersteund. Details: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Definitielijsten [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Superscript en subscript [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Wiskunde [math]

Inline `$x^2$` en als blok `$$...$$` (de MathJax/KaTeX-voorkeuren van Marked bepalen nog steeds de vormgeving in de preview).

### Callouts [callouts]

In Obsidian/Bear-stijl:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Zie ook de [Speciale syntax](Special_Syntax.html) van Marked en de Apex-wikipagina [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts).

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Schakel Critic Markup in Marked in zoals je gewend bent; Apex kan de critic-syntax weergeven in de processor-pipeline. Zie [CriticMarkup](CriticMarkup.html).

### Afkortingen [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Emoji-shortcodes [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadata [metadata]

YAML-frontmatter, headers in MultiMarkdown-stijl `Key: Value` en Pandoc-titelblokken worden herkend. Voeg waarden in met `[%key]` waar dit wordt ondersteund.

Configuratiedetails: [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) en [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) op de wiki.

### Markeringen voor inhoudsopgave [table-of-contents-markers]

Apex herkent gangbare TOC-markeringen, waaronder:

- `<!--TOC-->`
- `{{TOC}}` of `{{TOC:2-4}}`
- Kramdown-stijl `{:toc}`

Sluit een kop uit met `{:.no_toc}` waar IAL beschikbaar is. Meer info: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Speciale markeringen [special-markers]

Marked-georiënteerde HTML-commentaren zoals `<!--BREAK-->` (pagina-einde) en `<!--PAUSE:N-->` (automatisch scrollen) blijven werken in Apex-previews.

---

## Geavanceerde onderwerpen (wiki) [advanced-topics-wiki]

Raadpleeg de [Apex-wiki](https://github.com/ApexMarkdown/apex/wiki) voor functies die krachtig maar minder alledaags zijn in de dagelijkse preview:

| Onderwerp | Wiki |
|------|------|
| Index genereren | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citaten / bibliografie | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Inline Attribute Lists, spans, fenced divs | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Documenten met meerdere bestanden & includes | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Indelingen voor kop-ID's | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Afbeeldingen in meerdere formaten | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Compatibiliteitsmodi (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plug-ins & filters | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Zie ook [see-also]

- [Een processor kiezen](Choosing_a_Processor.html) --- wanneer je kiest voor MultiMarkdown, CommonMark, Kramdown, Discount of Apex
- [Instellingen: Processor](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Apex-wiki-startpagina](https://github.com/ApexMarkdown/apex/wiki)
- Problemen melden: [support.markedapp.com](https://support.markedapp.com)
