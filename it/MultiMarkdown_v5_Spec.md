<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Dai un'occhiata a [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) per sperimentare il processore MultiMarkdown.

## Cos'è il MultiMarkdown?

MultiMarkdown è un processore Markdown esteso progettato per funzionare con documenti completi anziché solo con frammenti di pagine Web. Estende la sintassi Markdown originale con funzionalità che consentono la conversione in più formati di output tra cui documenti HTML, LaTeX, PDF, ODF e Microsoft Word.

## Caratteristiche principali

- **Incentrato sui documenti**: progettato per documenti completi, non solo frammenti web
- **Output multiformato**: converte in HTML, LaTeX, PDF, ODF, RTF e Word
- **Contenuto rispetto alla presentazione**: si concentra sulla struttura e sul significato del documento
- **Multipiattaforma**: funziona su qualsiasi sistema operativo con qualsiasi editor di testo
- **Estensibile**: ricco set di funzionalità per requisiti di documenti complessi
- **Versione 5**: riscrittura completa con prestazioni e affidabilità migliorate

## Filosofia e obiettivi progettuali

MultiMarkdown segue il principio secondo cui **il contenuto è più importante della presentazione**. L'obiettivo è rappresentare il significato dei documenti (questo è un elenco, quella è una tabella, ecc.) piuttosto che dettare caratteri, colori o stili.

L'obiettivo è essere utilizzabile per l'80% dei documenti scritti dall'80% delle persone, rendendolo adatto a romanzi, tesi, documentazione tecnica e gran parte degli altri contenuti scritti.

## Principali funzionalità ed estensioni

### 1. **Supporto metadati**

- Metadati del documento nella parte superiore dei file
- Titolo, autore, data e variabili personalizzate
- Inclusione automatica nelle intestazioni di output

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**Variabili dei metadati**

- Utilizzare i valori dei metadati in tutto il documento
- Sintassi: `[%variable_name]`
- Sostituzione automatica durante la lavorazione

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Tabelle avanzate**

**Supporto completo delle tabelle**

- Intestazioni, allineamento e strutture di tabelle complesse
- Supporto per didascalie ed etichette delle tabelle
- Riferimenti incrociati alle tabelle

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Caratteristiche del tavolo**

- Allineamento delle colonne utilizzando i due punti
- Didascalie ed etichette delle tabelle
- Riferimenti incrociati con `[Table 1]`
- Supporto per strutture di tabelle complesse

### 3. **Note a piè di pagina e citazioni**

**Note a piè di pagina**

- Note a piè di pagina in stile riferimento con sintassi `[^1]`
- Numerazione e collegamento automatici
- Supporto per le note a piè di pagina in linea

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Supporto per le citazioni**

- Formattazione delle citazioni accademiche
- Generazione della bibliografia
- Supporto per vari stili di citazione

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

E di seguito è riportata la descrizione del riferimento da seguire
utilizzati in bibliografia.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

Nell'output HTML, le citazioni sono indistinguibili dalle note a piè di pagina.

Non è necessario utilizzare un localizzatore (ad esempio p. 23) e non ci sono regole speciali su cosa può essere utilizzato come localizzatore se si sceglie di utilizzarne uno. Se preferisci omettere il localizzatore, usa semplicemente una serie vuota di parentesi quadre prima della citazione:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

Non ci sono regole sul formato della chiave di citazione che usi (ad esempio Doe:2006), ma deve essere preceduto da `#`, proprio come le note a piè di pagina usano `^`.

### 4. **Riferimenti incrociati**

**Riferimenti incrociati automatici**

- Collegamento a titoli, tabelle, figure ed equazioni
- Generazione automatica delle etichette
- Supporto per etichette personalizzate

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1 [section-2-1]
```

**Tipi di riferimento**

- Intestazioni: `[Section 1]`, `[Heading Title]`
- Tabelle: `[Table 1]`, `[Table: Caption]`
- Cifre: `[Figure 1]`, `[Figure: Caption]`
- Equazioni: `[Equation 1]`

### 5. **Elenchi di definizioni**

**Coppie di definizione dei termini**

- Supporto per elenchi di definizioni
- Definizioni multiple per termine
- Output HTML `<dl>` corretto

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Blocchi di codice protetti**

**Blocchi di codice specifici della lingua**

- Triplo backtick con specifica della lingua
- Supporto per l'evidenziazione della sintassi
- Rilevamento automatico della lingua

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML ⟦14⟧ output

### 7. **Math Support**

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Attributi di immagini e collegamenti**

**Link e immagini migliorati**

- Supporto per attributi HTML
- Larghezza, altezza, testo alternativo e altro
- Migliore integrazione con i formati di output

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusione**

**Inclusione file**

- Includere altri file all'interno dei documenti
- Supporto per include nidificate
- Risoluzione automatica del percorso

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Caratteristiche di transizione**

- Inclusione file con `{{filename}}`
- Supporto per percorsi relativi e assoluti
- Supporto per la transclusione nidificata
- Generazione di manifesti per i file inclusi

### 10. **Integrazione CriticMarkup**

**Modifica monitoraggio**

- Supporto per la sintassi CriticMarkup
- Tieni traccia di aggiunte, eliminazioni e commenti
- Funzionalità di modifica collaborativa

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Sommario**

**Generazione automatica del sommario**

- `{{TOC}}` segnaposto per il sommario
- Struttura gerarchica basata sulle rubriche
- Generazione TOC personalizzabile

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **Abbreviazioni**

**Abbreviazioni in stile HTML**

- Definire le abbreviazioni per l'espansione automatica
- Supporto per tooltip e spiegazioni
- Output HTML `<abbr>` corretto

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 rispetto ad altri gusti Markdown

| Caratteristica | MultiMarkdown v5 | Marchio comune (GFM) | Sconto | Kramdown | Norma |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tabelle | Sì | No | Sì | Sì | No |
| Barrato | Sì | No | Sì | No | No |
| Elenchi attività | Sì | No | Sì | No | No |
| Codice recintato | Sì | Sì | Sì | Sì | No |
| Matematica | Sì | No | No | Sì | No |
| Note a piè di pagina | Sì | No | Sì | Sì | No |
| Elenchi di definizioni | Sì | No | No | Sì | No |
| Abbreviazioni | Sì | No | No | Sì | No |
| Elenchi di attributi | Sì | No | No | Sì | No |
| Estensioni | Sì | No | Limitato | Sì | No |
| Tipografia | Sì | No | Base | Sì | No |
| Collegamenti automatici | Sì | No | Sì | No | No |
| Riferimenti incrociati | Sì | No | No | No | No |
| Citazioni | Sì | No | No | No | No |
| Trasclusione | Sì | No | No | No | No |
| Metadati | Sì | No | No | No | No |

## Vantaggi principali di MultiMarkdown v5

1. **Incentrato sui documenti**: progettato per documenti completi, non solo frammenti web
2. **Output multiformato**: conversione in HTML, LaTeX, PDF, ODF, RTF e Word
3. **Supporto accademico**: citazioni, note a piè di pagina e riferimenti incrociati
4. **Funzionalità professionali**: metadati, transclusione e formattazione avanzata
5. **Multipiattaforma**: funziona su qualsiasi sistema operativo
6. **A prova di futuro**: il formato testo semplice garantisce compatibilità a lungo termine
7. **Estensibile**: ricco set di funzionalità per requisiti di documenti complessi

## Casi d'uso comuni

**Scrittura accademica**

- Tesi, dissertazioni e documenti di ricerca
- Gestione delle citazioni e generazione della bibliografia
- Riferimenti incrociati e note a piè di pagina

**Documentazione tecnica**

- Documentazione API e guide per l'utente
- Specifiche tecniche e manuali
- Documentazione del codice con evidenziazione della sintassi

**Pubblicazione**

- Libri, articoli e relazioni
- Output multiformato per diverse piattaforme
- Formattazione professionale dei documenti

**Gestione dei contenuti**

- Siti web di documentazione
- Basi di conoscenza e wiki
- Progetti di scrittura collaborativa

## Migliori pratiche

1. **Utilizza metadati**: sfrutta la parte iniziale di YAML per le informazioni sui documenti
2. **Struttura con intestazioni**: utilizza la gerarchia delle intestazioni corretta per la generazione del sommario
3. **Sfrutta i riferimenti incrociati**: utilizza il collegamento automatico per una migliore navigazione
4. **Organizza con Transclusion**: suddividi documenti di grandi dimensioni in file gestibili
5. **Verifica output**: verifica la formattazione tra diversi formati di output
6. **Utilizza citazioni**: implementa pratiche adeguate per le citazioni accademiche

## Migrazione da altri gusti Markdown

La maggior parte dei Markdown standard funziona con MultiMarkdown senza modifiche. Per sfruttare le funzionalità MMD:

1. **Aggiungi metadati**: includi la parte anteriore YAML per le informazioni sul documento
2. **Utilizza riferimenti incrociati**: sostituisci i collegamenti manuali con riferimenti automatici
3. **Implementa citazioni**: aggiungi la formattazione corretta delle citazioni accademiche
4. **Struttura con transclusione**: suddivide documenti di grandi dimensioni in file più piccoli
5. **Sfrutta le tabelle**: utilizza le funzionalità avanzate delle tabelle per la presentazione dei dati

## Risorse

- [Guida per l'utente di MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [Guida alla sintassi MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [Repository GitHub MultiMarkdown](https://github.com/fletcher/MultiMarkdown-5)
- [Documentazione MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/)

---

*Questa documentazione riguarda MultiMarkdown v5.1.0. Per le informazioni più aggiornate, fare sempre riferimento alla documentazione ufficiale di MultiMarkdown su [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*