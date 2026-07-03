<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Dai un'occhiata al [Markdown Dingus](x-marked-3://dingus?processor=discount) per sperimentare il processore Discount.

## Cos'è lo sconto GFM?

Discount GFM (GitHub Flavored Markdown) è un processore Markdown basato su C che implementa la sintassi Markdown estesa di GitHub. Si basa sulla libreria Discount originale ma migliorata con funzionalità specifiche di GitHub come tabelle, elenchi di attività, testo barrato e collegamento URL automatico.

## Caratteristiche principali

- **Prestazioni basate su C**: implementazione C nativa e veloce per prestazioni ottimali
- **Compatibilità GitHub**: implementa le estensioni Markdown di GitHub per la massima compatibilità
- **Leggero**: dipendenze minime e ingombro ridotto
- **Estensibile**: supporta varie estensioni Markdown e opzioni personalizzate
- **Supporto HTML5**: genera un output HTML5 moderno con markup semantico adeguato

## Principali differenze rispetto al ribasso standard

### 1. **Estensioni Markdown aromatizzate GitHub**

**Tabelle**

- Supporto completo per tabelle in stile GitHub con opzioni di allineamento
- Intestazioni, separatori e righe di dati con la corretta struttura della tabella HTML
- Allineamento delle colonne utilizzando i due punti (`:`) nelle righe separatore

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Elenchi attività**

- Supporto per caselle di controllo in stile GitHub negli elenchi
- Caselle di controllo interattive (rese come elementi di input HTML)
- Sono supportati sia gli stati selezionati che quelli non selezionati

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Testo barrato**

- Il testo racchiuso tra doppie tilde (`~~`) diventa barrato
- Utilizza i tag HTML `<del>` per il markup semantico
- Supporta più tilde per enfatizzare

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Supporto avanzato del blocco codice**

**Blocchi di codice protetti**

- Triplo apice inverso (```` ``` ````) per i blocchi di codice
- Specifica della lingua per l'evidenziazione della sintassi
- Nessuna rientranza richiesta (a differenza del Markdown standard)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatic Language Detection**

- Support for many programming languages
- Proper syntax highlighting when supported
- Fallback to plain text for unsupported languages

### 3. **Automatic URL Linking**

**URL Autolinking**

- Automatic conversion of URLs to clickable links
- Support for http, https, and ftp protocols
- Email addresses automatically converted to mailto links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Rilevamento collegamento intelligente**

- Riconosce gli URL senza markup esplicito
- Gestisce vari formati e protocolli URL
- Opzioni di sicurezza del collegamento configurabili

### 4. **Funzionalità elenco avanzate**

**Elenchi alfabetici**

- Elenchi ordinati con indicatori alfabetici (a, b, c, ecc.)
- Progressione automatica attraverso l'alfabeto
- Output HTML `<ol type="a">` corretto

```markdown
a. First item
b. Second item
c. Third item
```

**Elaborazione elenco migliorata**

- Migliore gestione degli elenchi nidificati
- Spaziatura e rientro migliorati
- Supporto per tipi di elenchi misti

### 5. **Supporto per le note a piè di pagina**

**Note a piè di pagina in stile riferimento**

- Numerazione automatica delle note a piè di pagina
- Collegamenti di riferimento con sintassi `[^1]`
- Definizioni delle note a piè di pagina alla fine del documento

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Elaborazione automatica delle note a piè di pagina**

- Genera una corretta struttura delle note a piè di pagina HTML
- Collegamenti tra riferimenti e definizioni
- Numerazione sequenziale in tutto il documento

### 6. **Integrazione HTML**

**Supporto HTML5**

- Riconoscimento completo dei tag HTML5
- Generazione corretta di markup semantico
- Struttura e attributi HTML moderni

**Blocchi HTML grezzi**

- Supporto per HTML all'interno di Markdown
- Corretta fuoriuscita e sanificazione
- Integrazione con la sintassi Markdown

### 7. **Regole di enfasi migliorate**

**Enfasi rilassata**

- I singoli trattini bassi (`_`) non creano enfasi nel mezzo delle parole
- Meglio per documentare codice e contenuti tecnici
- Previene l'enfasi indesiderata negli identificatori

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Livelli di enfasi multipli**

- Supporto per l'enfasi in grassetto, corsivo e combinata
- Coerente con le regole di enfasi Markdown standard
- Output HTML corretto con tag `<strong>` e `<em>`

### 8. **Generazione del sommario**

**Sommario automatico**

- Genera sommario dalle intestazioni
- Struttura gerarchica basata sui livelli di intestazione
- Opzioni di generazione TOC configurabili

**Generazione ID intestazione**

- Generazione automatica dell'ID per le intestazioni
- Collegamenti di ancoraggio per una facile navigazione
- Formattazione ID coerente

## Sconto GFM rispetto ad altri gusti con ribasso

| Caratteristica | Sconto | Marchio comune (GFM) | Kramdown | MultiMarkdown | Norma |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tabelle | Sì | No | Sì | Sì | No |
| Barrato | Sì | No | No | Sì | No |
| Elenchi attività | Sì | No | No | Sì | No |
| Codice recintato | Sì | Sì | Sì | Sì | No |
| Matematica | No | No | Sì | Sì | No |
| Note a piè di pagina | Sì | No | Sì | Sì | No |
| Elenchi di definizioni | No | No | Sì | Sì | No |
| Abbreviazioni | No | No | Sì | No | No |
| Elenchi di attributi | No | No | Sì | No | No |
| Estensioni | Limitato | No | Sì | Sì | No |
| Tipografia | Base | No | Sì | No | No |
| Collegamenti automatici | Sì | No | No | No | No |
| Elenchi alfabetici | Sì | No | No | No | No |

## Vantaggi principali dello sconto GFM

1. **Compatibilità GitHub**: perfetto per i contenuti che devono funzionare su GitHub
2. **Prestazioni**: implementazione rapida basata su C
3. **Semplicità**: focalizzato sulle funzionalità principali di GitHub senza complessità
4. **Affidabilità**: implementazione stabile e ben testata
5. **Conformità agli standard**: segue le specifiche Markdown di GitHub
6. **Leggero**: utilizzo minimo delle risorse e dipendenze

## Casi d'uso comuni

**Documentazione GitHub**

- File README e documentazione del progetto
- Pagine e wiki GitHub
- Descrizioni delle richieste di rilascio e pull

**Scrittura tecnica**

- Documentazione del codice ed esercitazioni
- Documentazione API
- Specifiche tecniche

**Gestione dei contenuti**

- Post e articoli del blog
- Siti web di documentazione
- Basi di conoscenza

**Modifica collaborativa**

- Documentazione della squadra
- Documenti di pianificazione del progetto
- Appunti e verbali delle riunioni

## Opzioni di configurazione

Lo sconto GFM supporta varie opzioni di configurazione:

- **Collegamento automatico**: attiva/disattiva il rilevamento automatico degli URL
- **Note a piè di pagina**: controlla l'elaborazione delle note a piè di pagina
- **Sommario**: impostazioni di generazione del sommario
- **Sicurezza HTML**: convalida e sanificazione del collegamento
- **Modalità rigorosa**: regole di analisi migliorate
- **Smart Quotes**: conversione automatica del preventivo

## Dettagli di implementazione

**Opzioni analizzatore**

- `kGHMarkdownAutoLink`: abilita il collegamento URL automatico
- `kGHMarkdownFootnotes`: abilita l'elaborazione delle note a piè di pagina
- `kGHMarkdownTOC`: abilita la generazione del sommario
- `kGHMarkdownSafeLinks`: limita i collegamenti ai protocolli sicuri
- `kGHMarkdownNoHTMLTags`: disabilita l'elaborazione dei tag HTML

**Caratteristiche di uscita**

- Markup semantico HTML5
- Gerarchia corretta delle intestazioni
- Strutture dei tavoli accessibili
- Output HTML pulito e valido

## Migliori pratiche

1. **Utilizza le tabelle con parsimonia**: le tabelle sono potenti ma possono essere complesse da gestire
2. **Sfrutta gli elenchi di attività**: ottimo per la gestione e la documentazione dei progetti
3. **Utilizza collegamenti automatici**: lascia che sia il processore a gestire automaticamente la conversione dell'URL
4. **Struttura con intestazioni**: utilizza la gerarchia delle intestazioni corretta per una migliore generazione del sommario
5. **Test su GitHub**: verifica la compatibilità con il rendering di GitHub

## Migrazione dal ribasso standard

La maggior parte dei Markdown standard funzionano con Discount GFM senza modifiche. Per sfruttare le funzionalità GFM:

1. **Aggiungi tabelle**: converti i dati in un formato tabella in stile GitHub
2. **Utilizza elenchi attività**: sostituisci i punti elenco con caselle di controllo ove appropriato
3. **Abilita barrato**: utilizza `~~text~~` per i contenuti barrati
4. **Sfrutta i collegamenti automatici**: rimuovi il markup dei collegamenti manuali per URL semplici
5. **Intestazioni della struttura**: garantire la corretta gerarchia delle intestazioni per la generazione del sommario

## Risorse

- [Specifiche di markdown aromatizzate GitHub](https://github.github.com/gfm/)
- [Documentazione della biblioteca sugli sconti](https://www.pell.portland.or.us/~orc/Code/discount/)
- [Guida al markdown di GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Foglio informativo per il ribasso](https://www.markdownguide.org/cheat-sheet/)

---

*Questa documentazione riguarda lo sconto GFM implementato in Marked. Per le informazioni più aggiornate, fare sempre riferimento alle specifiche ufficiali di GitHub Flavored Markdown.*