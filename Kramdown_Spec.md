# <%= @title %>

Check out the [Markdown Dingus](x-marked-3://dingus?processor=kramdown) to experiment with the Kramdown processor.

## What is Kramdown? [what-is-kramdown]

Kramdown is a fast, pure-Ruby Markdown-superset converter that extends the original Markdown syntax with features found in other implementations like Maruku, PHP Markdown Extra, and Pandoc. It provides a strict syntax with definite rules while maintaining compatibility with most Markdown documents.

## Key Characteristics [key-characteristics]

- **Fast and Pure Ruby**: Written entirely in Ruby for performance and portability
- **Strict Syntax**: Provides definite rules and clear specifications
- **Enhanced Features**: Includes many extensions not found in standard Markdown
- **Jekyll Integration**: Default Markdown processor for Jekyll static site generator
- **Comprehensive**: Supports both block-level and span-level elements with extensive customization

## Major Differences from Standard Markdown [major-differences-from-standard-markdown]

### 1. **Enhanced Block-Level Elements** [1-enhanced-block-level-elements]

**Definition Lists**

- Kramdown supports definition lists (not in standard Markdown)
- Uses `:` to separate terms from definitions

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tables**

- Full table support with headers, alignment, and formatting
- More comprehensive than basic Markdown table syntax

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Math Blocks**

- Support for mathematical expressions using LaTeX syntax
- Both inline and block math support

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Advanced Text Markup** [2-advanced-text-markup]

**Footnotes**

- Full footnote support with automatic numbering
- Reference-style footnotes with `[^1]` syntax

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abbreviations**

- Support for HTML-style abbreviations
- Automatic expansion of defined abbreviations

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Typographic Symbols**

- Automatic conversion of common typographic characters
- Smart quotes, em dashes, ellipses, etc.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Attribute Lists and Extensions** [3-attribute-lists-and-extensions]

**Attribute List Definitions (ALDs)**

- Define reusable attribute sets
- Support for IDs, classes, and custom attributes

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Inline Attribute Lists (IALs)**

- Attach attributes to specific elements
- Both block-level and span-level support

```markdown
This *is*{:.underline} some `code`{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Extensions**

- Custom extension system for additional functionality
- Built-in extensions for comments and options

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Enhanced Code Block Support** [4-enhanced-code-block-support]

**Language Specification**

- Automatic syntax highlighting for fenced code blocks
- Support for many programming languages

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**Standard Code Blocks**

- Improved handling of indented code blocks
- Better integration with other block elements

### 5. **Stricter Parsing Rules** [5-stricter-parsing-rules]

**Line Wrapping**

- Support for hard-wrapped content (lazy syntax)
- Clear rules for when line wrapping is allowed
- Not recommended for readability but supported for compatibility

**Tab Handling**

- Assumes tab stops at multiples of four
- Tabs only allowed at beginning of lines for indentation
- Must not be preceded by spaces

**Block Boundaries**

- Clear rules for when elements must start/end on block boundaries
- Consistent behavior across different element types

### 6. **Advanced Link and Image Support** [6-advanced-link-and-image-support]

**Automatic Links**

- Enhanced automatic link detection
- Better handling of URLs and email addresses

**Reference Links**

- Improved reference link processing
- Better conflict resolution for multiple definitions

**Image Attributes**

- Support for image attributes through IALs
- Width, height, alt text, and other HTML attributes

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **HTML Integration** [7-html-integration]

**HTML Blocks**

- Better handling of HTML within Markdown
- Support for HTML attributes and processing
- More flexible than standard Markdown HTML handling

**HTML Spans**

- Inline HTML with attribute support
- Better integration with Markdown syntax

### 8. **Mathematical Expressions** [8-mathematical-expressions]

**Inline Math**

- `$...$` syntax for inline mathematical expressions
- LaTeX-compatible syntax

**Block Math**

- `$$...$$` syntax for block mathematical expressions
- Support for complex equations and formulas

## Kramdown vs Other Markdown Flavors [kramdown-vs-other-markdown-flavors]

| Feature          | Kramdown | CommonMark (GFM) | GitHub Flavored | MultiMarkdown | Standard |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Strikethrough    | No       | Yes        | No              | No            | No       |
| Task Lists       | No       | No         | Yes             | Yes           | No       |
| Fenced Code      | Yes      | Yes        | Yes             | Yes           | No       |
| Math             | Yes      | No         | Yes             | Yes           | No       |
| Footnotes        | Yes      | Yes        | Yes             | Yes           | No       |
| Definition Lists | Yes      | No         | No              | Yes           | No       |
| Abbreviations    | Yes      | No         | No              | No            | No       |
| Attribute Lists  | Yes      | No         | No              | No            | No       |
| Typography       | Yes      | No         | No              | Yes           | No       |

## Key Advantages of Kramdown [key-advantages-of-kramdown]

1. **Comprehensive Feature Set**: Includes many extensions not found in other implementations
2. **Jekyll Integration**: Seamless integration with Jekyll static site generator
3. **Ruby Ecosystem**: Pure Ruby implementation with good Ruby tooling support
4. **Extensibility**: Custom extension system for additional functionality
5. **Attribute Support**: Rich attribute system for HTML output customization
6. **Mathematical Support**: Built-in support for LaTeX math expressions
7. **Strict Parsing**: Clear, unambiguous parsing rules

## Common Use Cases [common-use-cases]

**Jekyll Sites**

- Default processor for Jekyll static site generation
- Excellent for documentation and blog sites

**Technical Documentation**

- Math support for scientific and technical writing
- Attribute lists for advanced HTML customization

**Academic Writing**

- Footnote support for citations and references
- Mathematical expressions for formulas and equations

**Content Management**

- Extensions for custom functionality
- Attribute lists for metadata and styling

## Resources [resources]

- [Kramdown Syntax Documentation](https://kramdown.gettalong.org/syntax.html)
- [Kramdown Converter Documentation](https://kramdown.gettalong.org/converter.html)
- [Jekyll Integration Guide](https://jekyllrb.com/docs/configuration/markdown/)
- [Kramdown GitHub Repository](https://github.com/gettalong/kramdown)

## Migration from Standard Markdown [migration-from-standard-markdown]

Most standard Markdown documents work with Kramdown without modification. To take advantage of Kramdown's features:

1. **Add Definition Lists**: Convert glossaries and term lists
2. **Use Attribute Lists**: Add IDs, classes, and custom attributes
3. **Implement Footnotes**: Convert parenthetical references

## Best Practices [best-practices]

1. **Avoid Lazy Syntax**: Don't rely on hard-wrapping for readability
2. **Use Attribute Lists**: Leverage IALs for styling and metadata
3. **Consistent Indentation**: Use spaces instead of tabs when possible

---

*This documentation covers Kramdown 2.5.1. For the most current information, always refer to the official documentation at [kramdown.gettalong.org](https://kramdown.gettalong.org/).*
