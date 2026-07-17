# <%= @title %>

## What is Markdown? [what-is-markdown]

Markdown is a lightweight markup language that allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid HTML. The overriding design goal for Markdown's formatting syntax is to make it as readable as possible.

## Basic Syntax [basic-syntax]

### Headers [headers]

Create headers using hash symbols (`#`). The number of hashes determines the header level:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Emphasis [emphasis]

**Bold text** using double asterisks or double underscores:

```markdown
**Bold text**
__Bold text__
```

*Italic text* using single asterisks or single underscores:

```markdown
*Italic text*
_Italic text_
```

### Lists [lists]

**Unordered lists** using asterisks, plus signs, or hyphens:

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

**Ordered lists** using numbers followed by periods:

```markdown
1. First item
2. Second item
3. Third item
```

### Links [links]

**Inline links** with the text in square brackets and the URL in parentheses:

```markdown
[Link text](http://example.com)
```

**Reference links** with the text in square brackets and a reference in square brackets:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Automatic links** by wrapping URLs in angle brackets:

```markdown
<http://example.com>
<user@example.com>
```

### Images [images]

Images use similar syntax to links but with an exclamation mark at the beginning:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Blockquotes [blockquotes]

Create blockquotes using the greater-than symbol (`>`) at the beginning of each line:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Code [code]

**Inline code** using backticks:

```markdown
Use `code` in your text.
```

**Code blocks** by indenting with four spaces or one tab:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Horizontal Rules [horizontal-rules]

Create horizontal rules using three or more hyphens, asterisks, or underscores:

```markdown
---

***

___
```

### Line Breaks [line-breaks]

**Hard line breaks** by ending a line with two or more spaces:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Soft line breaks** by simply pressing Enter (creates a space in HTML):

```markdown
This line
continues on the next line with a space.
```

### Escaping Characters [escaping-characters]

Escape special characters using backslashes:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Common characters that can be escaped:
- `\` backslash
- `` ` `` backtick
- `*` asterisk
- `_` underscore
- `{}` curly braces
- `[]` square brackets
- `()` parentheses
- `#` hash
- `+` plus
- `-` minus
- `.` period
- `!` exclamation mark

## Best Practices [best-practices]

1. **Use blank lines** to separate different elements for better readability
2. **Be consistent** with your formatting choices (e.g., use either `*` or `_` for emphasis)
3. **Keep it simple** - Markdown is designed to be readable as plain text
4. **Test your output** to ensure it renders as expected
5. **Use meaningful link text** instead of generic phrases like "click here"

## Common Patterns [common-patterns]

### Nested Lists [nested-lists]

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Lists with Paragraphs [lists-with-paragraphs]

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Blockquotes with Other Elements [blockquotes-with-other-elements]

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Summary [summary]

Markdown provides a simple, readable way to format text that can be easily converted to HTML. The key is to keep it simple and readable while using the basic syntax elements consistently. With practice, you'll find that Markdown becomes second nature and makes writing structured content much easier.

---

*This tutorial covers the core Markdown syntax as defined in the original specification. For more advanced features, see the documentation for specific Markdown processors like CommonMark (GFM), MultiMarkdown, or GitHub Flavored Markdown.*
