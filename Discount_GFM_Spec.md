# <%= @title %>

Check out the [Markdown Dingus](x-marked-3://dingus?processor=discount) to experiment with the Discount processor.

## What is Discount GFM?

Discount GFM (GitHub Flavored Markdown) is a C-based Markdown processor that implements GitHub's extended Markdown syntax. It's based on the original Discount library but enhanced with GitHub-specific features like tables, task lists, strikethrough text, and automatic URL linking.

## Key Characteristics

- **C-Based Performance**: Fast, native C implementation for optimal performance
- **GitHub Compatibility**: Implements GitHub's Markdown extensions for maximum compatibility
- **Lightweight**: Minimal dependencies and small footprint
- **Extensible**: Supports various Markdown extensions and custom options
- **HTML5 Support**: Generates modern HTML5 output with proper semantic markup

## Major Differences from Standard Markdown

### 1. **GitHub Flavored Markdown Extensions**

**Tables**

- Full support for GitHub-style tables with alignment options
- Headers, separators, and data rows with proper HTML table structure
- Column alignment using colons (`:`) in separator rows

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Task Lists**

- Support for GitHub-style checkboxes in lists
- Interactive checkboxes (rendered as HTML input elements)
- Both checked and unchecked states supported

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Strikethrough Text**

- Text enclosed in double tildes (`~~`) becomes strikethrough
- Uses HTML `<del>` tags for semantic markup
- Supports multiple tildes for emphasis

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Enhanced Code Block Support**

**Fenced Code Blocks**

- Triple backticks (```` ``` ````) for code blocks
- Language specification for syntax highlighting
- No indentation required (unlike standard Markdown)

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

**Smart Link Detection**

- Recognizes URLs without explicit markup
- Handles various URL formats and protocols
- Configurable link safety options

### 4. **Advanced List Features**

**Alphabetic Lists**

- Ordered lists with alphabetic markers (a, b, c, etc.)
- Automatic progression through the alphabet
- Proper HTML `<ol type="a">` output

```markdown
a. First item
b. Second item
c. Third item
```

**Enhanced List Processing**

- Better handling of nested lists
- Improved spacing and indentation
- Support for mixed list types

### 5. **Footnotes Support**

**Reference-Style Footnotes**

- Automatic footnote numbering
- Reference links with `[^1]` syntax
- Footnote definitions at document end

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Automatic Footnote Processing**

- Generates proper HTML footnote structure
- Links between references and definitions
- Sequential numbering throughout document

### 6. **HTML Integration**

**HTML5 Support**

- Full HTML5 tag recognition
- Proper semantic markup generation
- Modern HTML structure and attributes

**Raw HTML Blocks**

- Support for HTML within Markdown
- Proper escaping and sanitization
- Integration with Markdown syntax

### 7. **Enhanced Emphasis Rules**

**Relaxed Emphasis**

- Single underscores (`_`) don't create emphasis in the middle of words
- Better for documenting code and technical content
- Prevents unwanted emphasis in identifiers

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Multiple Emphasis Levels**

- Support for bold, italic, and combined emphasis
- Consistent with standard Markdown emphasis rules
- Proper HTML output with `<strong>` and `<em>` tags

### 8. **Table of Contents Generation**

**Automatic TOC**

- Generates table of contents from headings
- Hierarchical structure based on heading levels
- Configurable TOC generation options

**Heading ID Generation**

- Automatic ID generation for headings
- Anchor links for easy navigation
- Consistent ID formatting

## Discount GFM vs Other Markdown Flavors

| Feature          | Discount | CommonMark (GFM) | Kramdown | MultiMarkdown | Standard |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tables           | Yes          | No         | Yes      | Yes           | No       |
| Strikethrough    | Yes          | No         | No       | Yes           | No       |
| Task Lists       | Yes          | No         | No       | Yes           | No       |
| Fenced Code      | Yes          | Yes        | Yes      | Yes           | No       |
| Math             | No           | No         | Yes      | Yes           | No       |
| Footnotes        | Yes          | No         | Yes      | Yes           | No       |
| Definition Lists | No           | No         | Yes      | Yes           | No       |
| Abbreviations    | No           | No         | Yes      | No            | No       |
| Attribute Lists  | No           | No         | Yes      | No            | No       |
| Extensions       | Limited      | No         | Yes      | Yes           | No       |
| Typography       | Basic        | No         | Yes      | No            | No       |
| Autolinks        | Yes          | No         | No       | No            | No       |
| Alphabetic Lists | Yes          | No         | No       | No            | No       |

## Key Advantages of Discount GFM

1. **GitHub Compatibility**: Perfect for content that needs to work on GitHub
2. **Performance**: Fast C-based implementation
3. **Simplicity**: Focused on core GitHub features without complexity
4. **Reliability**: Stable, well-tested implementation
5. **Standards Compliance**: Follows GitHub's Markdown specification
6. **Lightweight**: Minimal resource usage and dependencies

## Common Use Cases

**GitHub Documentation**

- README files and project documentation
- GitHub Pages and wikis
- Issue and pull request descriptions

**Technical Writing**

- Code documentation and tutorials
- API documentation
- Technical specifications

**Content Management**

- Blog posts and articles
- Documentation websites
- Knowledge bases

**Collaborative Editing**

- Team documentation
- Project planning documents
- Meeting notes and minutes

## Configuration Options

Discount GFM supports various configuration options:

- **Auto-linking**: Enable/disable automatic URL detection
- **Footnotes**: Control footnote processing
- **Table of Contents**: TOC generation settings
- **HTML Safety**: Link validation and sanitization
- **Strict Mode**: Enhanced parsing rules
- **Smart Quotes**: Automatic quote conversion

## Implementation Details

**Parser Options**

- `kGHMarkdownAutoLink`: Enable automatic URL linking
- `kGHMarkdownFootnotes`: Enable footnote processing
- `kGHMarkdownTOC`: Enable table of contents generation
- `kGHMarkdownSafeLinks`: Restrict links to safe protocols
- `kGHMarkdownNoHTMLTags`: Disable HTML tag processing

**Output Features**

- HTML5 semantic markup
- Proper heading hierarchy
- Accessible table structures
- Clean, valid HTML output

## Best Practices

1. **Use Tables Sparingly**: Tables are powerful but can be complex to maintain
2. **Leverage Task Lists**: Great for project management and documentation
3. **Utilize Autolinks**: Let the processor handle URL conversion automatically
4. **Structure with Headings**: Use proper heading hierarchy for better TOC generation
5. **Test on GitHub**: Verify compatibility with GitHub's rendering

## Migration from Standard Markdown

Most standard Markdown works with Discount GFM without changes. To take advantage of GFM features:

1. **Add Tables**: Convert data into GitHub-style table format
2. **Use Task Lists**: Replace bullet points with checkboxes where appropriate
3. **Enable Strikethrough**: Use `~~text~~` for crossed-out content
4. **Leverage Autolinks**: Remove manual link markup for simple URLs
5. **Structure Headings**: Ensure proper heading hierarchy for TOC generation

## Resources

- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [Discount Library Documentation](https://www.pell.portland.or.us/~orc/Code/discount/)
- [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

*This documentation covers Discount GFM as implemented in Marked. For the most current information, always refer to the official GitHub Flavored Markdown specification.*
