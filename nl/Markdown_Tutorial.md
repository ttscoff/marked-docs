# <%= @title %>

## Wat is Markdown? [what-is-markdown]

Markdown is een lichtgewicht opmaaktaal waarmee u kunt schrijven in een gemakkelijk leesbare, gemakkelijk te schrijven tekstindeling en deze vervolgens kunt converteren naar structureel geldige HTML. Het overheersende ontwerpdoel voor de opmaaksyntaxis van Markdown is om deze zo leesbaar mogelijk te maken.

## Basissyntaxis [basic-syntax]

### Kopteksten [headers]

Maak headers met behulp van hash-symbolen (`#`). Het aantal hashes bepaalt het headerniveau:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Nadruk [emphasis]

**Vetgedrukte tekst** met dubbele sterretjes of dubbele onderstrepingstekens:

```markdown
**Bold text**
__Bold text__
```

*Cursieve tekst* met enkele sterretjes of enkele onderstrepingstekens:

```markdown
*Italic text*
_Italic text_
```

### Lijsten [lists]

**Ongeordende lijsten** met sterretjes, plustekens of koppeltekens:

```afwaardering
* Artikel 1
* Artikel 2
* Artikel 3

+ Artikel 1
+ Artikel 2
+ Artikel 3

- Artikel 1
- Artikel 2
- Artikel 3
```

**Geordende lijsten** met cijfers gevolgd door punten:

```markdown
1. First item
2. Second item
3. Third item
```

### Koppelingen [links]

**Inline links** met de tekst tussen vierkante haakjes en de URL tussen haakjes:

```markdown
[Link text](http://example.com)
```

**Referentielinks** met de tekst tussen vierkante haakjes en een verwijzing tussen vierkante haakjes:

```afwaardering
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Automatische links** door URL's tussen punthaken te plaatsen:

```markdown
<http://example.com>
<user@example.com>
```

### Afbeeldingen [images]

Afbeeldingen gebruiken een soortgelijke syntaxis als links, maar met een uitroepteken aan het begin:

```afwaardering
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Blokcitaten [blockquotes]

Maak blokaanhalingstekens met het groter-dan-symbool (`>`) aan het begin van elke regel:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Code [code]

**Inlinecode** met backticks:

```markdown
Use `code` in your text.
```

**Codeblokken** door te inspringen met vier spaties of één tab:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Horizontale regels [horizontal-rules]

Maak horizontale regels met drie of meer koppeltekens, sterretjes of onderstrepingstekens:

```afwaardering
---

***

___
```

### Regeleinden [line-breaks]

**Harde regeleinden** door een regel te beëindigen met twee of meer spaties:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Zachte regeleinden** door simpelweg op Enter te drukken (creëert een spatie in HTML):

```markdown
This line
continues on the next line with a space.
```

### Ontsnappende karakters [escaping-characters]

Ontsnap aan speciale tekens met behulp van backslashes:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Veelvoorkomende tekens waaraan kan worden ontsnapt:
- `\` backslash
- `` ` `` backtick
- `*` sterretje
- `_` onderstrepingsteken
- `{}` accolades
- `[]` vierkante haakjes
- `()` haakjes
- `#` hash
- `+` plus
- `-` min
- `.` periode
- `!` uitroepteken

## Beste praktijken [best-practices]

1. **Gebruik lege regels** om verschillende elementen van elkaar te scheiden voor een betere leesbaarheid
2. **Wees consistent** met uw opmaakkeuzes (gebruik bijvoorbeeld `*` of `_` voor nadruk)
3. **Houd het simpel** - Markdown is ontworpen om leesbaar te zijn als platte tekst
4. **Test uw uitvoer** om er zeker van te zijn dat deze wordt weergegeven zoals verwacht
5. **Gebruik betekenisvolle linktekst** in plaats van algemene zinnen zoals "klik hier"

## Algemene patronen [common-patterns]

### Geneste lijsten [nested-lists]

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Lijsten met alinea's [lists-with-paragraphs]

```afwaardering
1. Eerste artikel

Dit is een paragraaf onder het eerste item.

2. Tweede punt

Dit is een paragraaf onder het tweede item.
```

### Blokcitaten met andere elementen [blockquotes-with-other-elements]

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Samenvatting [summary]

Markdown biedt een eenvoudige, leesbare manier om tekst op te maken die gemakkelijk kan worden geconverteerd naar HTML. De sleutel is om het eenvoudig en leesbaar te houden en tegelijkertijd de basissyntaxiselementen consistent te gebruiken. Door te oefenen zul je merken dat Markdown een tweede natuur wordt en het schrijven van gestructureerde inhoud veel gemakkelijker maakt.

---

*Deze tutorial behandelt de kernsyntaxis van Markdown zoals gedefinieerd in de oorspronkelijke specificatie. Voor meer geavanceerde functies raadpleegt u de documentatie voor specifieke Markdown processors zoals CommonMark (GFM), MultiMarkdown of GitHub Flavoured Markdown.*