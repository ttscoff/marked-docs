<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked può visualizzare in anteprima lo stesso file con diversi processori Markdown integrati. Ognuno di essi effettua diversi compromessi tra il **flusso di lavoro di scrittura** (libri, blog, README di GitHub) e il **controllo dell'output** (ID, classi, metadati). Scegli il valore predefinito in {% prefspane Processor %}; puoi anche sovrascrivere il processore per documento.

Questa pagina riassume le differenze tra i quattro processori principali. Per i dettagli completi sulla sintassi, consultare le pagine di riferimento in **Aiuto → Riferimento Markdown** (ad esempio [Specifica MultiMarkdown v5](MultiMarkdown_v5_Spec.html), [Specifica Kramdown](Kramdown_Spec.html), [Specifica CommonMark](CommonMark_Spec.html), [Specifica GFM sconto](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5) [multimarkdown-v5]

**Ideale per:** Prosa di lunga durata, scrittura accademica o tecnica e tutto ciò che si basa su **metadati**, **citazioni** e funzionalità **specifiche di MultiMarkdown**.

Contrassegnato viene fornito con **MultiMarkdown 5** (consultare la [Guida dell'utente di MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/) per la documentazione upstream).

### Punti di forza [strengths]

- **Documenti narrativi e ricchi di riferimenti:** Note a piè di pagina, bibliografia/citazioni e tabelle sono di prima classe.
- **Metadati:** blocchi di metadati MultiMarkdown standard (`Key: Value` intestazioni) più **transclusione** e altre comodità MMD descritte nella guida v5.
- **Sostituzione dei metadati:** le chiavi dei metadati possono essere inserite nel corpo con una sostituzione in stile `[%key]` in modo che titoli, stringhe dell'autore e valori simili rimangano sincronizzati con l'intestazione.
- **Tabelle, immagini e riferimenti incrociati:** Allineati con le funzionalità documentate per MultiMarkdown 5.

### ID e intestazioni del manuale [ids-and-manual-headings]

- Gli ID delle intestazioni sono **normalizzati** in un modo che tende a produrre caratteri **minuscoli, concatenati** (senza spazi: le parole corrono insieme).
- Per gli **ID intestazioni manuali**, MultiMarkdown utilizza il formato: `## Headline Text [my-id]` (l'identificatore tra parentesi dopo il testo dell'intestazione).

### Quando scegliere qualcos'altro [when-to-pick-something-else]

Se hai bisogno di elenchi di attività **in stile GitHub** e del comportamento esatto dell'attuale parser di GitHub, preferisci **CommonMark (GFM)**. Se hai bisogno di **classi/ID HTML a grana fine** su elementi arbitrari, considera **Kramdown**.

---

## Kramdown [kramdown]

**Ideale per:** Documenti in cui desideri **controllo preciso sull'output HTML**: **classi**, **ID** e attributi personalizzati, in modo che il tuo CSS possa indirizzare blocchi e intervalli specifici.

Il [riferimento alla sintassi di Kramdown](https://kramdown.gettalong.org/syntax.html) è la guida autorevole.

### Punti di forza [strengths-2]

- **Principalmente compatibile** con le abitudini in stile MultiMarkdown per il Markdown quotidiano, aggiungendo le proprie estensioni.
- **Elenchi di attributi in linea e di blocco (IAL):** Allega `{: #id .class key="value"}` a paragrafi, intestazioni, blocchi di codice, collegamenti, immagini e altro --- ideale per siti in stile Jekyll e fogli di stile personalizzati.
- **ID intestazione:** Kramdown normalizza gli ID intestazione generati automaticamente in **parole minuscole, separate da trattino** (ad esempio `my-section-title`). Per gli **ID manuali**, utilizza il modulo `{#id}` dopo il testo del titolo, ad es. Setext: `My Section {#my-section}` poi la sottolineatura, o ATX: `# My Section {#my-section}` (vedi [header](https://kramdown.gettalong.org/syntax.html#headers) di Kramdown per il posizionamento esatto e le regole IAL).
- **Elenchi di definizioni, note a piè di pagina, tipografia intelligente, blocchi matematici:** Ricco set di funzionalità per pubblicare pipeline che richiedono qualcosa di più del "semplice" Markdown.

### Quando scegliere qualcos'altro [when-to-pick-something-else-2]

Se ti affidi alla sostituzione dei metadati **solo MultiMarkdown** (`[%key]`) o a flussi di lavoro di citazione specifici di MMD, **MultiMarkdown** potrebbe essere la soluzione migliore. Per **README e documenti repository** che devono corrispondere a GitHub online, **CommonMark (GFM)** è solitamente più vicino.

---

## CommonMark (Markdown aromatizzato su GitHub / cmark-gfm) [commonmark-github-flavored-markdown-cmark-gfm]

**Ideale per:** **file README**, **descrizioni di problemi/PR** e **documentazione di progetto** che dovrebbero corrispondere il più possibile all'**attuale comportamento Markdown di GitHub**.

Marked utilizza un motore orientato al **GFM** (cmark-gfm). La specifica formale è la [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), basata su [CommonMark](https://commonmark.org/).

### Punti di forza [strengths-3]

- **Corrispondenza più vicina a GitHub:** tabelle, barre barrate, elementi dell'elenco di attività, blocchi di codice delimitati con tag di lingua e collegamenti automatici si comportano come il moderno rendering di GitHub.
- **Analisi inequivocabile:** CommonMark definisce con precisione la precedenza di blocco/inline e le regole dell'elenco: in alcuni casi limite è più rigido rispetto al comportamento "classico" di Markdown.pl, ma **più prevedibile** una volta apprese le regole.
- **Pratico per il testo avvolto:** Le regole dei paragrafi e degli elenchi sono progettate per comportarsi bene con la prosa strutturata (vedere le sezioni delle specifiche su continuazioni ed elenchi pigri).

### ID intestazione [header-ids]

Gli ancoraggi delle intestazioni generate automaticamente sono in genere **minuscoli e separati da trattini**, in linea con il comune slugging in stile GitHub.

### Quando scegliere qualcos'altro [when-to-pick-something-else-3]

GFM non replica i flussi di lavoro **metadati MultiMarkdown**, **IAL Kramdown** o **citazioni MMD**. Per libri, tesi o metadati pesanti, utilizza **MultiMarkdown** o **Kramdown** a seconda dei casi.

---

##Sconto

**Ideale per:** Un processore **veloce, basato su C** che tiene traccia del **Markdown classico** e di un **set di funzionalità più vecchio basato su GitHub**: utile quando si desidera un comportamento più vicino al **Markdown originale** oltre a tabelle, note a piè di pagina ed estensioni correlate senza il regolamento completo di CommonMark.

Casa del progetto: [Sconto](https://www.pell.portland.or.us/~orc/Code/discount/).

### Punti di forza

- **Tabelle in stile PHP Markdown Extra** e molte estensioni (note a piè di pagina, codice protetto quando abilitato, ecc. --- vedere le [Specifiche GFM sconti](Discount_GFM_Spec.html) di Marked per ciò che Marked abilita).
- **Extra "GitHub" facoltativi** nello sconto upstream (ad esempio elenchi di caselle di controllo se compilati con i flag giusti); Contrassegnato documenta la combinazione fornita nella pagina delle specifiche di sconto.
- **Tipografia in stile SmartyPants** e altre comodità descritte sul sito Discount (sebbene tutti i processori inclusi forniscano effettivamente funzionalità tipografiche).
- Filosoficamente vicino a **Markdown di John Gruber** più estensioni pratiche, piuttosto che alla suite completa di test CommonMark.

### Quando scegliere qualcos'altro

Per una **parità pixel-perfetta con github.com** di oggi, preferisci **CommonMark (GFM)**. Per **metadati e citazioni MultiMarkdown**, utilizzare **MultiMarkdown**.

---

## Confronto rapido [discount]

| Preoccupazione | MultiMarkdown | Kramdown | Marchio comune (GFM) | Sconto |
|--------|-------|--------|------------|----------|
| **Uso primario** | Prosa, carte, libri | HTML in stile, siti tipo Jekyll | README, documenti simili a GitHub | MD classico + estensioni |
| **Citazioni / Metadati MMD** | Forte | Tramite una sintassi diversa | No | No |
| **Stile ID intestazione manuale** | `## Title [id]` | `## Title {: #id }` (IAL) | Regole slug specifiche/GitHub | Nessuno |
| **ID intestazione automatica** | Minuscolo concatenato | Minuscolo con trattino | Minuscolo con trattino | Con trattino minuscolo |
| **Attributi extra (classi/ID)** | Meccanismi MMD limitati | **IAL** — molto forte | Limitato | Limitato |

---

## Vedi anche [quick-comparison]

- [Impostazioni: Processore](Settings_Processor.html): processore predefinito e opzioni correlate
- [Markdown Dingus](Markdown_Dingus.html): prova i processori fianco a fianco in Marked
- [Processore personalizzato](Custom_Processor.html): collega la tua toolchain quando necessario