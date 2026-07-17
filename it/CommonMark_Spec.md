<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Dai un'occhiata a [Markdown Dingus](x-marked-3://dingus?processor=commonmark) per sperimentare il processore CommonMark (GFM).


## Cos'è CommonMark? [what-is-commonmark]

CommonMark è un'implementazione fortemente specificata e altamente compatibile di Markdown. È stato creato per risolvere le ambiguità e le incoerenze delle specifiche Markdown originali di John Gruber, che hanno portato a implementazioni divergenti su piattaforme e strumenti diversi.

## Perché esiste CommonMark [why-commonmark-exists]

La specifica Markdown originale di John Gruber era intenzionalmente ambigua in molte aree, portando a interpretazioni diverse a seconda delle varie implementazioni. Ciò creava problemi in cui lo stesso documento Markdown veniva visualizzato in modo diverso su piattaforme diverse (GitHub, StackOverflow, Reddit, ecc.).

CommonMark fornisce:

- **Specifiche inequivocabili** per tutta la sintassi Markdown
- **Suite di test completa** per garantire un comportamento coerente
- **Regole di precedenza chiare** per sintassi in conflitto
- **Algoritmo di analisi dettagliato** che può essere implementato in modo coerente

## Differenze chiave rispetto al ribasso standard [key-differences-from-standard-markdown]

### 1. **Regole di analisi più severe** [1-stricter-parsing-rules]

CommonMark applica un comportamento di analisi più coerente:

**Righe vuote prima degli elementi del blocco**

- CommonMark richiede righe vuote prima di intestazioni, virgolette ed elenchi
- Il Markdown standard spesso li consente senza righe vuote

```markdown
Text
# Heading
```

*CommonMark: richiede una riga vuota prima dell'intestazione*

*Markdown standard: spesso consente senza riga vuota*

### 2. **Analisi degli elementi dell'elenco** [2-list-item-parsing]

**Requisiti per il rientro**

- CommonMark ha regole specifiche per il rientro delle voci dell'elenco
- Le sottoliste devono essere rientrate in modo coerente (tipicamente 4 spazi)
- Le implementazioni standard di Markdown variano in base a questo

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Continua l'elenco**

- CommonMark ha regole chiare su quando gli elementi dell'elenco sono "sciolti" o "stretti"
- Gli elenchi sciolti racchiudono gli elementi in `<p>` tag, gli elenchi stretti no

### 3. **Gestione del blocco di codice** [3-code-block-handling]

**Blocchi di codice protetti**

- CommonMark standardizza la sintassi dei blocchi di codice recintati con apici inversi o tilde
- Richiede rientro e marcatori di chiusura coerenti


    ```language
    codice qui
    ```


**Blocchi di codice rientrati**

- CommonMark richiede righe vuote prima dei blocchi di codice rientrati
- Il Markdown standard spesso li consente senza righe vuote

### 4. **Link ed elaborazione delle immagini** [4-link-and-image-processing]

**Precedenza del collegamento di riferimento**

- CommonMark ha regole chiare per le quali la definizione di riferimento ha la precedenza
- Più definizioni per lo stesso riferimento vengono gestite in modo coerente

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Ordine di analisi dei collegamenti**

- CommonMark elabora i collegamenti prima dell'enfasi
- Ciò influisce sul modo in cui viene interpretata la sintassi annidata

### 5. **Enfasi e forte enfasi** [5-emphasis-and-strong-emphasis]

**Regole di enfasi nidificate**

- CommonMark dispone di algoritmi specifici per la gestione dei marcatori annidati `*` e `_`
- Impedisce l'analisi ambigua di modelli di enfasi complessi

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Elaborazione delimitatore**

- CommonMark utilizza un algoritmo di "stack delimitatore" per un'analisi dell'enfasi coerente
- Le implementazioni standard di Markdown variano nel loro approccio

### 6. **Elaborazione blocchi HTML** [6-html-block-processing]

**Rilevamento blocchi HTML**

- CommonMark ha 7 diversi tipi di blocchi HTML con regole specifiche
- Ogni tipo ha requisiti diversi per le condizioni di inizio/fine

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Gestione delle interruzioni di riga** [7-line-break-handling]

**Interruzioni di linea dura**

- CommonMark richiede due spazi alla fine della riga per interruzioni forti
- Le interruzioni di riga singole diventano interruzioni soft (ignorate in HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Riferimenti a entità e caratteri** [8-entity-and-character-references]

**Riferimenti a caratteri numerici**

- CommonMark supporta riferimenti numerici sia decimali che esadecimali
- Il supporto Markdown standard varia

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## Algoritmo di analisi CommonMark [commonmark-parsing-algorithm]

CommonMark utilizza un approccio di analisi in due fasi:

### Fase 1: Struttura del blocco [phase-1-block-structure]

1. **Elaborazione linea**: ogni linea viene analizzata per i marcatori a livello di blocco
2. **Blocchi contenitori**: vengono identificati blocchi di quote, elenchi e altri contenitori
3. **Blocchi foglia**: vengono elaborati titoli, blocchi di codice e paragrafi
4. **Link di riferimento**: le definizioni dei link vengono raccolte per un uso successivo

### Fase 2: struttura in linea [phase-2-inline-structure]

1. **Elaborazione in linea**: il testo all'interno dei blocchi viene analizzato per individuare elementi in linea
2. **Emphasis Parsing**: utilizza l'algoritmo dello stack di delimitatori per un'enfasi coerente
3. **Risoluzione dei collegamenti**: i collegamenti di riferimento vengono risolti utilizzando le definizioni raccolte
4. **Elaborazione entità**: i riferimenti ai caratteri vengono convertiti in caratteri effettivi

## Vantaggi di CommonMark [benefits-of-commonmark]

1. **Comportamento prevedibile**: lo stesso input produce sempre lo stesso output
2. **Compatibilità multipiattaforma**: funziona in modo coerente su diversi strumenti
3. **Test completi**: un'ampia suite di test garantisce l'affidabilità
4. **Documentazione chiara**: le specifiche dettagliate eliminano le congetture
5. **A prova di futuro**: punti di estensione ben definiti per nuove funzionalità

## Note di implementazione [implementation-notes]

CommonMark è progettato per essere:

- **Conforme alle specifiche**: segue esattamente le specifiche ufficiali CommonMark
- **Test-driven**: supera la suite di test ufficiale CommonMark
- **Estensibile**: può essere esteso con funzionalità aggiuntive mantenendo la compatibilità
- **Veloce**: algoritmi di analisi ottimizzati per le prestazioni

## Risorse [resources]

- [Specifica CommonMark](https://spec.commonmark.org/0.31.2/)
- [Suite di test CommonMark](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Strumento di test online
- [Forum di discussione CommonMark](https://talk.commonmark.org/)

---

*Questa documentazione riguarda CommonMark 0.31.2 (28-01-2024). Per le informazioni più aggiornate fare sempre riferimento alle specifiche ufficiali.*