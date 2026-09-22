# <%= @title %>

These options are in the **Configure Apex** sheet. Open it from {% prefspane Processor %} when the default processor is **Apex (beta)**. Every option here applies only to Apex. Math, Critic Markup, hashtags, file includes, and header IDs stay in Marked's other settings.

See [Apex (beta)](Apex.html) for what Apex is and the syntax it covers.

Checkboxes in the sheet override the same settings in an Apex metadata file. File paths are optional. A path Marked cannot read is skipped, and the preview still runs.

## Files [files]

CSL
: A Citation Style Language file (`.csl`) used when Apex formats a bibliography. Leave this empty to use the style named in the document or in the metadata file.

Bibliography
: One or more bibliography files. Accepted types are BibTeX (`.bib`), CSL JSON (`.json`), and CSL YAML (`.yml`, `.yaml`). Click **Add** for another file. Apex looks in these files when resolving citations.

Concordance
: One or more concordance files (`.tsv`, `.txt`, or `.csv`) used when building an index. Click **Add** for another file.

Metadata file
: An external metadata file (`.yml`, `.yaml`, `.txt`, or `.md`) merged before Apex runs. Document metadata still takes precedence where both set the same key. Checkbox options in this sheet win over values in the metadata file.

## Syntax [syntax]

On by default unless noted.

Tables
: Pipe tables, including a header row and a separator row.

Footnotes
: Reference footnotes (`[^id]`) and inline footnotes.

Definition lists
: Term-and-definition lists (`: definition`).

Superscript / subscript
: `^super^` and `~sub~`. Turn this off if single tildes should not mean subscript. Marked's **Render ~text~ as underscore** setting is separate and conflicts with subscript.

Strikethrough
: `~~deleted~~`.

Autolink URLs and emails
: Bare `https://` URLs and email addresses become links.

Fenced divs
: `::: name` blocks that wrap a section in a `<div>`.

Bracketed spans
: Inline attribute spans such as `[text]{.class}`.

Alphabetic lists
: Lists that start with `a.` or `A.` as well as numbers.

Mixed list markers
: A list may mix `*`, `+`, and `-` markers and still be one list.

Markdown in HTML
: Markdown inside HTML block tags is processed. Some markup can still break.

Metadata transforms
: `[%key]` placeholders are replaced from document metadata.

## Tables and images [tables-and-images]

Grid tables
: Grid-style tables drawn with `+` and `|`. Off by default.

Relaxed tables
: Pipe tables may omit the leading and trailing pipes. On by default.

Per-cell alignment
: Alignment markers in a table cell override the column alignment. On by default.

Image captions
: An image title, or the alt text when there is no title, becomes a visible caption. On by default.

Title-only captions
: Only the image title is used as the caption. Alt text is ignored. Off by default. Has no effect unless **Image captions** is on.

## Links and indexes [links-and-indexes]

Wiki links
: Apex converts `[[wiki links]]`. Off by default. When this is on, Marked skips its own Preview "Convert wiki links" pass for that document, and Apex may resolve the target file differently than Marked does. The default extension comes from Marked's wiki link settings.

Sanitize wiki link URLs
: Generated wiki-link URLs are lowercased, apostrophes are removed, and other characters that are not letters or numbers are replaced. Off by default. Available only when **Wiki links** is on.

Index processing
: Recognize index markers (MultiMarkdown, mmark, Leanpub, and textindex styles). On by default.

Suppress index output
: Still read index markers, but do not print the generated index. Off by default.

## Callouts (extra) [callouts-extra]

Both are off by default. Obsidian and Bear callouts (`> [!NOTE]`) are handled by Marked before Apex and are not controlled here.

Python-Markdown callouts
: `!!! note` style callouts.

Quarto callouts
: Quarto `::: {.callout-note}` blocks.

## Accessibility [accessibility]

Both are off by default.

ARIA labels
: Add ARIA attributes that describe the structure of the HTML Apex emits.

Header anchors
: Emit an `<a>` anchor on each heading instead of only an `id` on the heading.
