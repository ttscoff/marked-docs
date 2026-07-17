# <%= @title %>

## Was ist Markdown? [what-is-markdown]

Markdown ist eine leichtgewichtige Auszeichnungssprache. Sie schreiben in einem gut lesbaren und einfach zu erstellenden Klartextformat, das sich anschließend in strukturell gültiges HTML umwandeln lässt. Das wichtigste Gestaltungsziel der Markdown-Syntax ist größtmögliche Lesbarkeit.

## Grundlegende Syntax [basic-syntax]

### Überschriften [headers]

Erstellen Sie Überschriften mit Rautenzeichen (`#`). Die Anzahl der Rautenzeichen bestimmt die Überschriftenebene:

```markdown
# Header 1 [header-1]
## Header 2 [header-2]
### Header 3 [header-3]
#### Header 4 [header-4]
##### Header 5 [header-5]
###### Header 6 [header-6]
```

### Hervorhebung [emphasis]

**Fetter Text** mit doppelten Sternchen oder Unterstrichen:

```markdown
**Bold text**
__Bold text__
```

*Kursiver Text* mit einzelnen Sternchen oder Unterstrichen:

```markdown
*Italic text*
_Italic text_
```

### Listen [lists]

**Ungeordnete Listen** mit Sternchen, Pluszeichen oder Bindestrichen:

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

**Geordnete Listen** mit Zahlen, auf die ein Punkt folgt:

```markdown
1. First item
2. Second item
3. Third item
```

### Links [links]

**Inline-Links** mit dem Text in eckigen Klammern und der URL in runden Klammern:

```markdown
[Link text](http://example.com)
```

**Referenzlinks** mit dem Text und einer Referenz in jeweils eigenen eckigen Klammern:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Automatische Links**, indem Sie URLs in spitze Klammern einschließen:

```markdown
<http://example.com>
<user@example.com>
```

### Bilder [images]

Bilder verwenden eine ähnliche Syntax wie Links, jedoch mit einem Ausrufezeichen am Anfang:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Blockzitate [blockquotes]

Erstellen Sie Blockzitate mit dem Größer-als-Symbol (`>`) am Anfang jeder Zeile:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Code [code]

**Inline-Code** mit Backticks:

```markdown
Use `code` in your text.
```

**Codeblöcke** durch Einrücken mit vier Leerzeichen oder einem Tabulator:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Horizontale Linien [horizontal-rules]

Erstellen Sie horizontale Linien mit drei oder mehr Bindestrichen, Sternchen oder Unterstrichen:

```markdown
---

***

___
```

### Zeilenumbrüche [line-breaks]

**Harte Zeilenumbrüche** erzeugen Sie, indem Sie eine Zeile mit zwei oder mehr Leerzeichen beenden:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Weiche Zeilenumbrüche** erzeugen Sie durch einfaches Drücken der Eingabetaste (daraus wird in HTML ein Leerzeichen):

```markdown
This line
continues on the next line with a space.
```

### Escape-Zeichen [escaping-characters]

Sonderzeichen mit Backslashes maskieren:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Häufige Zeichen, die maskiert werden können:
- `\` Backslash
- `` ` `` Backtick
- `*` Sternchen
- `_` Unterstrich
- `{}` geschweifte Klammern
- `[]` eckige Klammern
- `()` Klammern
- `#` Hash
- `+` Pluszeichen
- `-` Minuszeichen
- `.` Punkt
- `!` Ausrufezeichen

## Bewährte Vorgehensweisen [best-practices]

1. **Verwenden Sie Leerzeilen**, um verschiedene Elemente zur besseren Lesbarkeit zu trennen
2. **Seien Sie konsistent** bei Ihren Formatierungsoptionen (verwenden Sie z. B. entweder `*` oder `_` zur Hervorhebung).
3. **Halten Sie es einfach** – Markdown ist so konzipiert, dass es als einfacher Text lesbar ist
4. **Testen Sie Ihre Ausgabe**, um sicherzustellen, dass sie wie erwartet gerendert wird
5. **Verwenden Sie aussagekräftigen Linktext** anstelle allgemeiner Phrasen wie „hier klicken“

## Häufige Muster [common-patterns]

### Verschachtelte Listen [nested-lists]

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Listen mit Absätzen [lists-with-paragraphs]

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Blockzitate mit anderen Elementen [blockquotes-with-other-elements]

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Zusammenfassung [summary]

Markdown bietet eine einfache, lesbare Möglichkeit, Text zu formatieren und problemlos in HTML umzuwandeln. Halten Sie den Text einfach und lesbar und verwenden Sie die grundlegenden Syntaxelemente konsistent. Mit etwas Übung geht Ihnen Markdown in Fleisch und Blut über und erleichtert das Schreiben strukturierter Inhalte erheblich.

---

*Dieses Tutorial behandelt die Markdown-Kernsyntax aus der ursprünglichen Spezifikation. Erweiterte Funktionen finden Sie in der Dokumentation zu bestimmten Markdown-Prozessoren wie CommonMark (GFM), MultiMarkdown oder GitHub Flavored Markdown.*
