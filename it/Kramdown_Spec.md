<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Dai un'occhiata al [Markdown Dingus](x-marked-3://dingus?processor=kramdown) per sperimentare il processore Kramdown.

## Cos'è il Kramdown? [what-is-kramdown]

Kramdown è un convertitore superset veloce e puro Ruby Markdown che estende la sintassi originale di Markdown con funzionalità presenti in altre implementazioni come Maruku, PHP Markdown Extra e Pandoc. Fornisce una sintassi rigorosa con regole definite pur mantenendo la compatibilità con la maggior parte dei documenti Markdown.

## Caratteristiche principali [key-characteristics]

- **Rubino veloce e puro**: scritto interamente in Ruby per prestazioni e portabilità
- **Sintassi rigorosa**: fornisce regole definite e specifiche chiare
- **Funzionalità migliorate**: include molte estensioni non presenti nel Markdown standard
- **Integrazione Jekyll**: processore Markdown predefinito per il generatore di siti statici Jekyll
- **Completo**: supporta elementi sia a livello di blocco che di intervallo con ampia personalizzazione

## Principali differenze rispetto al ribasso standard [major-differences-from-standard-markdown]

### 1. **Elementi a livello di blocco migliorati** [1-enhanced-block-level-elements]

**Elenchi di definizioni**

- Kramdown supporta elenchi di definizioni (non in Markdown standard)
- Utilizza `:` per separare i termini dalle definizioni

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tabelle**

- Supporto completo delle tabelle con intestazioni, allineamento e formattazione
- Più completa della sintassi di base della tabella Markdown

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Blocchi matematici**

- Supporto per espressioni matematiche utilizzando la sintassi LaTeX
- Supporto per la matematica sia in linea che a blocchi

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Marcatura avanzata del testo** [2-advanced-text-markup]

**Note a piè di pagina**

- Supporto completo delle note a piè di pagina con numerazione automatica
- Note a piè di pagina in stile riferimento con sintassi `[^1]`

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abbreviazioni**

- Supporto per abbreviazioni in stile HTML
- Espansione automatica delle abbreviazioni definite

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Simboli tipografici**

- Conversione automatica di caratteri tipografici comuni
- Virgolette intelligenti, trattini, puntini di sospensione, ecc.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Elenchi di attributi ed estensioni** [3-attribute-lists-and-extensions]

**Definizioni dell'elenco di attributi (ALD)**

- Definire set di attributi riutilizzabili
- Supporto per ID, classi e attributi personalizzati

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Elenchi di attributi in linea (IAL)**

- Allega attributi a elementi specifici
- Supporto sia a livello di blocco che a livello di span

```markdown
This *is*{:.underline} some ⟦3⟧{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Estensioni**

- Sistema di estensione personalizzato per funzionalità aggiuntive
- Estensioni integrate per commenti e opzioni

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Supporto avanzato del blocco codice** [4-enhanced-code-block-support]

**Specifica della lingua**

- Evidenziazione automatica della sintassi per blocchi di codice protetti
- Supporto per molti linguaggi di programmazione

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**Blocchi di codice standard**

- Migliorata la gestione dei blocchi di codice rientrati
- Migliore integrazione con altri elementi del blocco

### 5. **Regole di analisi più severe** [5-stricter-parsing-rules]

**Riavvolgimento della linea**

- Supporto per contenuti rigidi (sintassi pigra)
- Regole chiare su quando è consentito il ritorno a capo della riga
- Non consigliato per la leggibilità ma supportato per la compatibilità

**Gestione delle schede**

- Presuppone che le tabulazioni siano multipli di quattro
- Le tabulazioni sono consentite solo all'inizio delle righe per il rientro
- Non deve essere preceduto da spazi

**Confini del blocco**

- Regole chiare su quando gli elementi devono iniziare/terminare sui confini del blocco
- Comportamento coerente tra diversi tipi di elementi

### 6. **Supporto avanzato per collegamenti e immagini** [6-advanced-link-and-image-support]

**Collegamenti automatici**

- Rilevamento automatico del collegamento migliorato
- Migliore gestione degli URL e degli indirizzi email

**Link di riferimento**

- Migliorata l'elaborazione dei collegamenti di riferimento
- Migliore risoluzione dei conflitti per più definizioni

**Attributi dell'immagine**

- Supporto per gli attributi dell'immagine tramite IAL
- Larghezza, altezza, testo alternativo e altri attributi HTML

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **Integrazione HTML** [7-html-integration]

**Blocchi HTML**

- Migliore gestione dell'HTML all'interno di Markdown
- Supporto per attributi ed elaborazione HTML
- Più flessibile rispetto alla gestione HTML Markdown standard

**Intervalli HTML**

- HTML in linea con supporto per gli attributi
- Migliore integrazione con la sintassi Markdown

### 8. **Espressioni matematiche** [8-mathematical-expressions]

**Matematica in linea**

- `$...$` sintassi per espressioni matematiche in linea
- Sintassi compatibile con LaTeX

**Blocca matematica**

- `$$...$$` sintassi per espressioni matematiche a blocchi
- Supporto per equazioni e formule complesse

## Kramdown vs altri gusti Markdown [kramdown-vs-other-markdown-flavors]

| Caratteristica | Kramdown | Marchio comune (GFM) | GitHub aromatizzato | MultiMarkdown | Norma |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Barrato | No | Sì | No | No | No |
| Elenchi attività | No | No | Sì | Sì | No |
| Codice recintato | Sì | Sì | Sì | Sì | No |
| Matematica | Sì | No | Sì | Sì | No |
| Note a piè di pagina | Sì | Sì | Sì | Sì | No |
| Elenchi di definizioni | Sì | No | No | Sì | No |
| Abbreviazioni | Sì | No | No | No | No |
| Elenchi di attributi | Sì | No | No | No | No |
| Tipografia | Sì | No | No | Sì | No |

## Principali vantaggi di Kramdown [key-advantages-of-kramdown]

1. **Set completo di funzionalità**: include molte estensioni non presenti in altre implementazioni
2. **Integrazione Jekyll**: integrazione perfetta con il generatore di siti statici Jekyll
3. **Ecosistema Ruby**: implementazione Pure Ruby con un buon supporto per gli strumenti Ruby
4. **Estensibilità**: sistema di estensione personalizzato per funzionalità aggiuntive
5. **Supporto attributi**: ricco sistema di attributi per la personalizzazione dell'output HTML
6. **Supporto matematico**: supporto integrato per espressioni matematiche LaTeX
7. **Analisi rigorosa**: regole di analisi chiare e inequivocabili

## Casi d'uso comuni [common-use-cases]

**Siti Jekyll**

- Processore predefinito per la generazione di siti statici Jekyll
- Eccellente per documentazione e siti blog

**Documentazione tecnica**

- Supporto matematico per la scrittura scientifica e tecnica
- Elenchi di attributi per la personalizzazione HTML avanzata

**Scrittura accademica**

- Supporto delle note a piè di pagina per citazioni e riferimenti
- Espressioni matematiche per formule ed equazioni

**Gestione dei contenuti**

- Estensioni per funzionalità personalizzate
- Elenchi di attributi per metadati e stili

## Risorse [resources]

- [Documentazione sulla sintassi Kramdown](https://kramdown.gettalong.org/syntax.html)
- [Documentazione del convertitore Kramdown](https://kramdown.gettalong.org/converter.html)
- [Guida all'integrazione di Jekyll](https://jekyllrb.com/docs/configuration/markdown/)
- [Repository Kramdown GitHub](https://github.com/gettalong/kramdown)

## Migrazione dal ribasso standard [migration-from-standard-markdown]

La maggior parte dei documenti Markdown standard funzionano con Kramdown senza modifiche. Per sfruttare le funzionalità di Kramdown:

1. **Aggiungi elenchi di definizioni**: converti glossari ed elenchi di termini
2. **Utilizza elenchi di attributi**: aggiungi ID, classi e attributi personalizzati
3. **Implementa le note a piè di pagina**: converti i riferimenti tra parentesi

## Migliori pratiche [best-practices]

1. **Evita la sintassi pigra**: non fare affidamento sull'hard-wrapping per la leggibilità
2. **Utilizza elenchi di attributi**: sfrutta gli IAL per stili e metadati
3. **Rientro coerente**: quando possibile, utilizza gli spazi invece delle tabulazioni

---

*Questa documentazione riguarda Kramdown 2.5.1. Per le informazioni più aggiornate, fare sempre riferimento alla documentazione ufficiale su [kramdown.gettalong.org](https://kramdown.gettalong.org/).*