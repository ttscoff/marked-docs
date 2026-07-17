# <%= @title %>

Check out the [Markdown Dingus](x-marked-3://dingus?processor=commonmark) to experiment with the CommonMark (GFM) processor.


## What is CommonMark? [what-is-commonmark]

CommonMark is a strongly specified, highly compatible implementation of Markdown. It was created to address the ambiguities and inconsistencies in John Gruber's original Markdown specification, which led to divergent implementations across different platforms and tools.

## Why CommonMark Exists [why-commonmark-exists]

The original Markdown specification by John Gruber was intentionally ambiguous in many areas, leading to different interpretations by various implementations. This created problems where the same Markdown document would render differently on different platforms (GitHub, StackOverflow, Reddit, etc.).

CommonMark provides:

- **Unambiguous specifications** for all Markdown syntax
- **Comprehensive test suite** to ensure consistent behavior
- **Clear precedence rules** for conflicting syntax
- **Detailed parsing algorithm** that can be implemented consistently

## Key Differences from Standard Markdown [key-differences-from-standard-markdown]

### 1. **Stricter Parsing Rules** [1-stricter-parsing-rules]

CommonMark enforces more consistent parsing behavior:

**Blank Lines Before Block Elements**

- CommonMark requires blank lines before headings, blockquotes, and lists
- Standard Markdown often allows these without blank lines

```markdown
Text
# Heading
```

*CommonMark: Requires blank line before heading*

*Standard Markdown: Often allows without blank line*

### 2. **List Item Parsing** [2-list-item-parsing]

**Indentation Requirements**

- CommonMark has specific rules for list item indentation
- Sublists must be indented consistently (typically 4 spaces)
- Standard Markdown implementations vary on this

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**List Continuation**

- CommonMark has clear rules for when list items are "loose" vs "tight"
- Loose lists wrap items in `<p>` tags, tight lists don't

### 3. **Code Block Handling** [3-code-block-handling]

**Fenced Code Blocks**

- CommonMark standardizes fenced code block syntax with backticks or tildes
- Requires consistent indentation and closing markers


    ```language
    code here
    ```


**Indented Code Blocks**

- CommonMark requires blank lines before indented code blocks
- Standard Markdown often allows them without blank lines

### 4. **Link and Image Processing** [4-link-and-image-processing]

**Reference Link Precedence**

- CommonMark has clear rules for which reference definition takes precedence
- Multiple definitions for the same reference are handled consistently

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Link Parsing Order**

- CommonMark processes links before emphasis
- This affects how nested syntax is interpreted

### 5. **Emphasis and Strong Emphasis** [5-emphasis-and-strong-emphasis]

**Nested Emphasis Rules**

- CommonMark has specific algorithms for handling nested `*` and `_` markers
- Prevents ambiguous parsing of complex emphasis patterns

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Delimiter Processing**

- CommonMark uses a "delimiter stack" algorithm for consistent emphasis parsing
- Standard Markdown implementations vary in their approach

### 6. **HTML Block Processing** [6-html-block-processing]

**HTML Block Detection**

- CommonMark has 7 different types of HTML blocks with specific rules
- Each type has different requirements for start/end conditions

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Line Break Handling** [7-line-break-handling]

**Hard Line Breaks**

- CommonMark requires two spaces at end of line for hard breaks
- Single line breaks become soft breaks (ignored in HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Entity and Character References** [8-entity-and-character-references]

**Numeric Character References**

- CommonMark supports both decimal and hexadecimal numeric references
- Standard Markdown support varies

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## CommonMark Parsing Algorithm [commonmark-parsing-algorithm]

CommonMark uses a two-phase parsing approach:

### Phase 1: Block Structure [phase-1-block-structure]

1. **Line Processing**: Each line is analyzed for block-level markers
2. **Container Blocks**: Blockquotes, lists, and other containers are identified
3. **Leaf Blocks**: Headings, code blocks, paragraphs are processed
4. **Reference Links**: Link definitions are collected for later use

### Phase 2: Inline Structure [phase-2-inline-structure]

1. **Inline Processing**: Text within blocks is parsed for inline elements
2. **Emphasis Parsing**: Uses delimiter stack algorithm for consistent emphasis
3. **Link Resolution**: Reference links are resolved using collected definitions
4. **Entity Processing**: Character references are converted to actual characters

## Benefits of CommonMark [benefits-of-commonmark]

1. **Predictable Behavior**: Same input always produces same output
2. **Cross-Platform Compatibility**: Works consistently across different tools
3. **Comprehensive Testing**: Extensive test suite ensures reliability
4. **Clear Documentation**: Detailed specification eliminates guesswork
5. **Future-Proof**: Well-defined extension points for new features

## Implementation Notes [implementation-notes]

CommonMark is designed to be:

- **Specification-compliant**: Follows the official CommonMark spec exactly
- **Test-driven**: Passes the official CommonMark test suite
- **Extensible**: Can be extended with additional features while maintaining compatibility
- **Fast**: Optimized parsing algorithms for performance

## Resources [resources]

- [CommonMark Specification](https://spec.commonmark.org/0.31.2/)
- [CommonMark Test Suite](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Online testing tool
- [CommonMark Discussion Forum](https://talk.commonmark.org/)

---

*This documentation covers CommonMark 0.31.2 (2024-01-28). For the most current information, always refer to the official specification.*
