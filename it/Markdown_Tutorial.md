<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Cos'è il Markdown?

Markdown è un linguaggio di markup leggero che ti consente di scrivere utilizzando un formato di testo semplice di facile lettura e scrittura, quindi di convertirlo in HTML strutturalmente valido. L'obiettivo di progettazione principale per la sintassi di formattazione di Markdown è renderlo il più leggibile possibile.

## Sintassi di base

### Intestazioni

Crea intestazioni utilizzando i simboli hash (`#`). Il numero di hash determina il livello di intestazione:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Enfasi

**Testo in grassetto** utilizzando doppi asterischi o doppi trattini bassi:

```markdown
**Bold text**
__Bold text__
```

*Testo corsivo* utilizzando asterischi singoli o trattini bassi singoli:

```markdown
*Italic text*
_Italic text_
```

### Elenchi

**Elenchi non ordinati** che utilizzano asterischi, segni più o trattini:

```markdown
* Item 1
* Item 2
* Item 3

+ Item 1
+ Item 2
+ Item 3

- Item 1
- Item 2
- Item 3
```

**Elenchi ordinati** utilizzando numeri seguiti da punti:

```markdown
1. First item
2. Second item
3. Third item
```

### Collegamenti

**Link in linea** con il testo tra parentesi quadre e l'URL tra parentesi:

```markdown
[Link text](http://example.com)
```

**Link di riferimento** con il testo tra parentesi quadre e un riferimento tra parentesi quadre:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Collegamenti automatici** racchiudendo gli URL tra parentesi angolari:

```markdown
<http://example.com>
<user@example.com>
```

### Immagini

Le immagini utilizzano una sintassi simile ai collegamenti ma con un punto esclamativo all'inizio:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Citazioni

Crea virgolette utilizzando il simbolo maggiore di (`>`) all'inizio di ogni riga:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Codice

**Codice in linea** utilizzando i backtick:

```markdown
Use ⟦4⟧ in your text.
```

**Blocchi di codice** rientrando con quattro spazi o una tabulazione:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Regole orizzontali

Crea regole orizzontali utilizzando tre o più trattini, asterischi o caratteri di sottolineatura:

```markdown
---

***

___
```

### Interruzioni di riga

**Interruzioni di riga rigide** terminando una riga con due o più spazi:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Interruzioni di riga morbide** semplicemente premendo Invio (crea uno spazio in HTML):

```markdown
This line
continues on the next line with a space.
```

### Caratteri escape

Escape caratteri speciali utilizzando le barre rovesciate:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Caratteri comuni a cui è possibile eseguire l'escape:
- `\` barra rovesciata
- `` ` `` apice inverso
- `*` asterisco
- `_` trattino basso
- `{}` parentesi graffe
- `[]` parentesi quadre
- `()` parentesi
- `#` cancelletto
- `+` più
- `-` meno
- `.` periodo
- `!` punto esclamativo

## Migliori pratiche

1. **Utilizza righe vuote** per separare i diversi elementi per una migliore leggibilità
2. **Sii coerente** con le tue scelte di formattazione (ad esempio, usa `*` o `_` per dare enfasi)
3. **Mantieni la semplicità**: Markdown è progettato per essere leggibile come testo semplice
4. **Testa il tuo output** per assicurarti che venga visualizzato come previsto
5. **Utilizza link di testo significativi** invece di frasi generiche come "fai clic qui"

## Modelli comuni

### Elenchi nidificati

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Elenchi con paragrafi

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Citazioni con altri elementi

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Riepilogo

Markdown fornisce un modo semplice e leggibile per formattare il testo che può essere facilmente convertito in HTML. La chiave è mantenerlo semplice e leggibile utilizzando in modo coerente gli elementi di sintassi di base. Con la pratica, scoprirai che Markdown diventa una seconda natura e rende molto più semplice la scrittura di contenuti strutturati.

---

*Questo tutorial copre la sintassi principale di Markdown come definita nelle specifiche originali. Per funzionalità più avanzate, consulta la documentazione per processori Markdown specifici come CommonMark (GFM), MultiMarkdown o GitHub Flavored Markdown.*