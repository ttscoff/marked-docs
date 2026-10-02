# <%= @title %>

W> **Il supporto di Apex in Marked è in beta.** Il comportamento potrebbe cambiare con la maturazione dell'integrazione. Segnala problemi, rendering imprevisti o sintassi mancante su [support.markedapp.com](https://support.markedapp.com).

Apex è un **processore Markdown unificato**: un unico motore che si propone di coprire le funzionalità per cui di solito si scelgono CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown o Kramdown, senza rinunciare alle altre varianti.

In Marked, **Apex (beta)** funziona sempre in modalità **unificata** di Apex (tutte queste famiglie di funzionalità attive insieme). In Marked non è ancora possibile scegliere una "modalità CommonMark" o una "modalità Kramdown" separata di Apex; questo potrebbe arrivare in futuro.

Prova il [Markdown Dingus](x-marked-3://dingus?processor=apex) per sperimentare con Apex, oppure apri {% appmenu Help, Markdown Reference %} e scegli la scheda **Apex** per un prontuario compatto.

---

## Perché esiste Apex [why-apex-exists]

Le "varianti" di Markdown si sono differenziate per buoni motivi --- GitHub aveva bisogno di task list e tabelle, MultiMarkdown di note a piè di pagina e metadati, Kramdown di elenchi di attributi --- ma scegliere un processore di solito significa rinunciare alla sintassi di un altro.

L'obiettivo di Apex è **consolidare** queste estensioni, in modo che un unico documento possa utilizzare:

- Le abitudini quotidiane di CommonMark / GFM (codice con fence, task list, testo barrato, tabelle GFM)
- Le abitudini in stile MultiMarkdown per note a piè di pagina, abbreviazioni e metadati
- Elenchi di definizioni, formule matematiche in stile Kramdown e (per usi avanzati) elenchi di attributi
- Funzionalità orientate a Marked come callout, Critic Markup e marcatori per il sommario

La documentazione completa di riferimento si trova sul [wiki di Apex](https://github.com/ApexMarkdown/apex/wiki). Questa pagina copre ciò che serve nell'uso quotidiano con l'anteprima di Marked.

---

## Attivare Apex in Marked [enabling-apex-in-marked]

1. Apri {% prefspane Processor %}.
2. Imposta **Processore Markdown predefinito** su **Apex (beta)**.
3. Oppure esegui l'override per singolo documento con metadati come `Processor: apex` (alias: `apex-beta`, `unified`).

Gli alias funzionano anche da AppleScript, dalle azioni "Run Processor" di Conductor, dall'output standard di processori personalizzati (`APEX`) e dagli URL di default `x-marked://`.

T> In questa beta, Marked continua a espandere i propri include di file (`<<[file]` e i relativi percorsi di include di Marked) prima che Apex venga eseguito. Il motore di include nativo di Apex è disattivato in Marked per motivi di sandboxing. Continua a usare le funzionalità di include di Marked come fai già.

---

## Sintassi base che Apex aggiunge o unifica [basic-syntax]

Il Markdown standard (titoli, enfasi, link, immagini, elenchi, citazioni, codice) funziona come ti aspetti. Gli elementi seguenti sono gli extra di cui si ha più spesso bisogno passando ad Apex.

### Task list [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Testo barrato [strikethrough]

```markdown
~~removed text~~
```

### Tabelle [tables]

Tabelle con pipe in stile GFM, con separatori di intestazione e allineamento delle colonne:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Le funzionalità avanzate delle tabelle (rowspan `^^`, colspan, didascalie, tabelle a griglia, CSV) sono documentate sul wiki: [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Note a piè di pagina [footnotes]

In stile riferimento:

```markdown
See the note[^1].

[^1]: Footnote text.
```

Sono supportati anche gli stili inline familiari da MultiMarkdown / Kramdown. Dettagli: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Elenchi di definizioni [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Apice e pedice [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Formule matematiche [math]

Inline `$x^2$` e a display `$$...$$` (le preferenze MathJax / KaTeX di Marked continuano a controllare l'aspetto dell'anteprima).

### Callout [callouts]

In stile Obsidian / Bear:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Vedi anche la [Sintassi speciale](Special_Syntax.html) di Marked e la pagina wiki di Apex [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts).

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Attiva Critic Markup in Marked come al solito; Apex è in grado di renderizzare la sintassi critic all'interno della pipeline del processore. Vedi [CriticMarkup](CriticMarkup.html).

### Abbreviazioni [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Shortcode emoji [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadati [metadata]

Vengono riconosciuti il front matter YAML, le intestazioni in stile MultiMarkdown `Key: Value` e i blocchi titolo di Pandoc. Inserisci i valori con `[%key]` dove supportato.

Dettagli sulla configurazione: [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) e [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) sul wiki.

### Marcatori per il sommario [table-of-contents-markers]

Apex riconosce i marcatori comuni per il sommario, tra cui:

- `<!--TOC-->`
- `{{TOC}}` oppure `{{TOC:2-4}}`
- In stile Kramdown `{:toc}`

Escludi un titolo con `{:.no_toc}` dove è disponibile IAL. Altro: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Marcatori speciali [special-markers]

I commenti HTML orientati a Marked, come `<!--BREAK-->` (interruzione di pagina) e `<!--PAUSE:N-->` (scorrimento automatico), continuano a funzionare con le anteprime di Apex.

---

## Argomenti avanzati (wiki) [advanced-topics-wiki]

Consulta il [wiki di Apex](https://github.com/ApexMarkdown/apex/wiki) per le funzionalità potenti ma meno comuni nell'uso quotidiano dell'anteprima:

| Argomento | Wiki |
|------|------|
| Generazione di indici | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citazioni / bibliografia | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Elenchi di attributi inline, span, div con fence | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Documenti multi-file e include | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Formati degli ID dei titoli | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Immagini multi-formato | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Modalità di compatibilità (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugin e filtri | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Vedi anche [see-also]

- [Scegliere un processore](Choosing_a_Processor.html) --- quando scegliere MultiMarkdown, CommonMark, Kramdown, Discount o Apex
- [Impostazioni: Processore](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Home del wiki di Apex](https://github.com/ApexMarkdown/apex/wiki)
- Segnala problemi: [support.markedapp.com](https://support.markedapp.com)
