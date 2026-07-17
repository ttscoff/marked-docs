# <%= @title %>

Check out the [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) to experiment with the MultiMarkdown processor.

## What is MultiMarkdown? [what-is-multimarkdown]

MultiMarkdown is an extended Markdown processor designed to work with complete documents rather than just web page fragments. It extends the original Markdown syntax with features that enable conversion to multiple output formats including HTML, LaTeX, PDF, ODF, and Microsoft Word documents.

## Key Characteristics [key-characteristics]

- **Document-Focused**: Designed for complete documents, not just web snippets
- **Multi-Format Output**: Converts to HTML, LaTeX, PDF, ODF, RTF, and Word
- **Content Over Presentation**: Focuses on document structure and meaning
- **Cross-Platform**: Works on any operating system with any text editor
- **Extensible**: Rich feature set for complex document requirements
- **Version 5**: Complete rewrite with improved performance and reliability

## Philosophy and Design Goals [philosophy-and-design-goals]

MultiMarkdown follows the principle that **content is more important than presentation**. The focus is on representing the meaning of documents (this is a list, that is a table, etc.) rather than dictating fonts, colors, or styling.

The goal is to be usable for 80% of the documents that 80% of people write, making it suitable for novels, theses, technical documentation, and most other written content.

## Major Features and Extensions [major-features-and-extensions]

### 1. **Metadata Support** [1-metadata-support]

- Document metadata at the top of files
- Title, author, date, and custom variables
- Automatic inclusion in output headers

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**Metadata Variables**

- Use metadata values throughout the document
- Syntax: `[%variable_name]`
- Automatic substitution during processing

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Advanced Tables** [2-advanced-tables]

**Full Table Support**

- Headers, alignment, and complex table structures
- Support for table captions and labels
- Cross-references to tables

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Table Features**

- Column alignment using colons
- Table captions and labels
- Cross-references with `[Table 1]`
- Support for complex table structures

### 3. **Footnotes and Citations** [3-footnotes-and-citations]

**Footnotes**

- Reference-style footnotes with `[^1]` syntax
- Automatic numbering and linking
- Support for inline footnotes

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Citation Support**

- Academic citation formatting
- Bibliography generation
- Support for various citation styles

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

And following is the description of the reference to be
used in the bibliography.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

In HTML output, citations are indistinguishable from footnotes.

You are not required to use a locator (e.g. p. 23), and there are no special rules on what can be used as a locator if you choose to use one. If you prefer to omit the locator, just use an empty set of square brackets before the citation:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

There are no rules on the citation key format that you use (e.g. Doe:2006), but it must be preceded by a `#`, just like footnotes use `^`.

### 4. **Cross-References** [4-cross-references]

**Automatic Cross-References**

- Link to headings, tables, figures, and equations
- Automatic label generation
- Support for custom labels

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1
```

**Reference Types**

- Headings: `[Section 1]`, `[Heading Title]`
- Tables: `[Table 1]`, `[Table: Caption]`
- Figures: `[Figure 1]`, `[Figure: Caption]`
- Equations: `[Equation 1]`

### 5. **Definition Lists** [5-definition-lists]

**Term-Definition Pairs**

- Support for definition lists
- Multiple definitions per term
- Proper HTML `<dl>` output

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Fenced Code Blocks** [6-fenced-code-blocks]

**Language-Specific Code Blocks**

- Triple backticks with language specification
- Syntax highlighting support
- Automatic language detection

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML `<pre><code>` output

### 7. **Math Support** [7-math-support]

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Image and Link Attributes** [8-image-and-link-attributes]

**Enhanced Links and Images**

- Support for HTML attributes
- Width, height, alt text, and more
- Better integration with output formats

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusion** [9-transclusion]

**File Inclusion**

- Include other files within documents
- Support for nested includes
- Automatic path resolution

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Transclusion Features**

- File inclusion with `{{filename}}`
- Support for relative and absolute paths
- Nested transclusion support
- Manifest generation for included files

### 10. **CriticMarkup Integration** [10-criticmarkup-integration]

**Change Tracking**

- Support for CriticMarkup syntax
- Track additions, deletions, and comments
- Collaborative editing features

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Table of Contents** [11-table-of-contents]

**Automatic TOC Generation**

- `{{TOC}}` placeholder for table of contents
- Hierarchical structure based on headings
- Customizable TOC generation

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **Abbreviations** [12-abbreviations]

**HTML-Style Abbreviations**

- Define abbreviations for automatic expansion
- Support for tooltips and explanations
- Proper HTML `<abbr>` output

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 vs Other Markdown Flavors [multimarkdown-v5-vs-other-markdown-flavors]

| Feature          | MultiMarkdown v5 | CommonMark (GFM) | Discount | Kramdown | Standard |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tables           | Yes              | No         | Yes          | Yes      | No       |
| Strikethrough    | Yes              | No         | Yes          | No       | No       |
| Task Lists       | Yes              | No         | Yes          | No       | No       |
| Fenced Code      | Yes              | Yes        | Yes          | Yes      | No       |
| Math             | Yes              | No         | No           | Yes      | No       |
| Footnotes        | Yes              | No         | Yes          | Yes      | No       |
| Definition Lists | Yes              | No         | No           | Yes      | No       |
| Abbreviations    | Yes              | No         | No           | Yes      | No       |
| Attribute Lists  | Yes              | No         | No           | Yes      | No       |
| Extensions       | Yes              | No         | Limited      | Yes      | No       |
| Typography       | Yes              | No         | Basic        | Yes      | No       |
| Autolinks        | Yes              | No         | Yes          | No       | No       |
| Cross-References | Yes              | No         | No           | No       | No       |
| Citations        | Yes              | No         | No           | No       | No       |
| Transclusion     | Yes              | No         | No           | No       | No       |
| Metadata         | Yes              | No         | No           | No       | No       |

## Key Advantages of MultiMarkdown v5 [key-advantages-of-multimarkdown-v5]

1. **Document-Focused**: Designed for complete documents, not just web snippets
2. **Multi-Format Output**: Convert to HTML, LaTeX, PDF, ODF, RTF, and Word
3. **Academic Support**: Citations, footnotes, and cross-references
4. **Professional Features**: Metadata, transclusion, and advanced formatting
5. **Cross-Platform**: Works on any operating system
6. **Future-Proof**: Plain text format ensures long-term compatibility
7. **Extensible**: Rich feature set for complex document requirements

## Common Use Cases [common-use-cases]

**Academic Writing**

- Theses, dissertations, and research papers
- Citation management and bibliography generation
- Cross-references and footnotes

**Technical Documentation**

- API documentation and user guides
- Technical specifications and manuals
- Code documentation with syntax highlighting

**Publishing**

- Books, articles, and reports
- Multi-format output for different platforms
- Professional document formatting

**Content Management**

- Documentation websites
- Knowledge bases and wikis
- Collaborative writing projects

## Best Practices [best-practices]

1. **Use Metadata**: Leverage YAML front matter for document information
2. **Structure with Headings**: Use proper heading hierarchy for TOC generation
3. **Leverage Cross-References**: Use automatic linking for better navigation
4. **Organize with Transclusion**: Break large documents into manageable files
5. **Test Output**: Verify formatting across different output formats
6. **Use Citations**: Implement proper academic citation practices

## Migration from Other Markdown Flavors [migration-from-other-markdown-flavors]

Most standard Markdown works with MultiMarkdown without changes. To take advantage of MMD features:

1. **Add Metadata**: Include YAML front matter for document information
2. **Use Cross-References**: Replace manual links with automatic references
3. **Implement Citations**: Add proper academic citation formatting
4. **Structure with Transclusion**: Break large documents into smaller files
5. **Leverage Tables**: Use advanced table features for data presentation

## Resources [resources]

- [MultiMarkdown User's Guide](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [MultiMarkdown Syntax Guide](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [MultiMarkdown GitHub Repository](https://github.com/fletcher/MultiMarkdown-5)
- [MultiMarkdown Documentation](https://fletcher.github.io/MultiMarkdown-5/)

---

*This documentation covers MultiMarkdown v5.1.0. For the most current information, always refer to the official MultiMarkdown documentation at [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*
