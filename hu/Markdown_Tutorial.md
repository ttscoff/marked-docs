<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## Mi az a Markdown?

A Markdown egy könnyű jelölőnyelv, amely lehetővé teszi, hogy könnyen olvasható, könnyen írható egyszerű szöveges formátum használatával írjon, majd átalakítsa azt szerkezetileg érvényes HTML-vé. A Markdown formázási szintaxisának elsődleges tervezési célja az, hogy a lehető legjobban olvasható legyen.

## Alapszintaxis

### Fejlécek

Hozzon létre fejléceket hash szimbólumok (`#`) használatával. A hash-ek száma határozza meg a fejléc szintjét:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Hangsúly

**félkövér szöveg** dupla csillaggal vagy dupla aláhúzással:

```markdown
**Bold text**
__Bold text__
```

*Dőlt szöveg* egyetlen csillaggal vagy aláhúzással:

```markdown
*Italic text*
_Italic text_
```

### Listák

**Rendezés nélküli listák** csillagokkal, pluszjelekkel vagy kötőjelekkel:

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

**Rendezett listák** számokkal, majd pontokkal:

```markdown
1. First item
2. Second item
3. Third item
```

### Linkek

**Inline linkek**, szögletes zárójelben a szöveggel és zárójelben az URL-lel:

```markdown
[Link text](http://example.com)
```

**Hivatkozási hivatkozások**, szögletes zárójelben a szöveggel és szögletes zárójelben egy hivatkozással:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Automatikus linkek** az URL-ek szögletes zárójelekbe helyezésével:

```markdown
<http://example.com>
<user@example.com>
```

### Képek

A képek a hivatkozásokhoz hasonló szintaxist használnak, de az elején felkiáltójellel:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Idézetblokk

Hozzon létre idézőjeleket a nagyobb, mint szimbólum (`>`) használatával az egyes sorok elején:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Kód

**Inline kód** backtick használatával:

```markdown
Use ⟦4⟧ in your text.
```

**Kódblokkok** négy szóközzel vagy egy tabulátorral történő behúzással:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Vízszintes szabályok

Hozzon létre vízszintes szabályokat három vagy több kötőjel, csillag vagy aláhúzás segítségével:

```markdown
---

***

___
```

### Sortörések

**Kemény sortörés** egy sor két vagy több szóközzel történő befejezésével:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Lágy sortörések** az Enter megnyomásával (szóközt hoz létre a HTML-ben):

```markdown
This line
continues on the next line with a space.
```

### Menekülő karakterek

Speciális karakterek kilépése fordított perjelekkel:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Gyakori karakterek, amelyek megkerülhetők:
- `\` fordított perjel
- `` ` `` backtick
- `*` csillag
- `_` aláhúzás
- `{}` göndör fogszabályzó
- `[]` szögletes zárójel
- `()` zárójel
- `#` hash
- `+` plusz
- `-` mínusz
- `.` időszak
- `!` felkiáltójel

## Bevált gyakorlatok

1. **Használjon üres sorokat** a különböző elemek elválasztásához a jobb olvashatóság érdekében
2. **Legyen következetes** a formázási választásaival (például használja a `*` vagy a `_` karaktereket a kiemeléshez)
3. **Legyen egyszerű** - A Markdownt úgy tervezték, hogy egyszerű szövegként is olvasható legyen
4. **Tesztelje le a kimenetet**, hogy megbizonyosodjon arról, hogy a várt módon jelenik meg
5. **Használjon értelmes linkszöveget** olyan általános kifejezések helyett, mint a "kattintson ide"

## Gyakori minták

### Beágyazott listák

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Listák bekezdésekkel

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Az idézetek blokkolása más elemekkel

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Összegzés

A Markdown egyszerű, olvasható módot biztosít a szöveg formázására, amely könnyen konvertálható HTML-be. A kulcs az, hogy egyszerű és olvasható legyen, miközben az alapvető szintaktikai elemeket következetesen használja. Gyakorlattal rá fog jönni, hogy a Markdown másodlagossá válik, és sokkal könnyebbé teszi a strukturált tartalom írását.

---

*Ez az oktatóanyag az eredeti specifikációban meghatározott Markdown alapvető szintaxist ismerteti. A fejlettebb funkciókért tekintse meg az egyes Markdown processzorok, például a CommonMark (GFM), a MultiMarkdown vagy a GitHub Flavored Markdown dokumentációját.*