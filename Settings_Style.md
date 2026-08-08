# <%= @title %>

Options in the {% prefspane Style %}:

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Layout and typography [layout-and-typography]

Limit text width in Preview
: Set a maximum width for the body of the preview using the slider (in pixels).

Auto-hyphenate in paragraphs
: Allow words to break with hyphenation automatically.

Prevent widows in headlines and paragraphs
: Forces a non-breaking space between the last two words of headlines and paragraphs to prevent single words from wrapping to a new line.

Generate typographically correct quotes and punctuation
: Use SmartyPants for smart quotes, ellipses conversion, and other typography features (MultiMarkdown).

Surround footnotes markers with square brackets
: If checked, use the default MultiMarkdown formatting for footnote markers ([1]). Uncheck to strip square brackets.

Enable Outline for extensions
: Automatically turn on Outline mode for files with listed extensions.

Use APA Style
: Use APA style outlines instead of the default Decimal format.

Style verbatim (code) blocks as poetry
: If checked, tab-indented, fenced or included code is displayed as poetry instead of a code block (no syntax highlighting, and special styling depending on the theme).

Allow themes to wrap text inside code blocks
: If checked, themes are allowed to cause wrapping within `pre>code` blocks. If unchecked, horizontal overflow will always scroll.

Always wrap code
: Force code blocks to wrap regardless of theme settings (overrides theme wrapping behavior).

Detect and style RTL text
: Detect language per element in document and style Right To Left accordingly.

### Theme [theme]

Manage Styles
: Opens the [Style Manager](Style_Manager.html) window. Add CSS files from your drive to have them appear in Style picker menus. Use the `Add New Style` button or drag CSS files to this window. Drag to reorder, and use the checkboxes to enable or disable Styles.

More Themes
: Open the online theme gallery to browse and install additional styles.

Default style
: The style selected here will be loaded for all new windows, unless a [document-specific style is indicated in metadata](Per-Document_Settings.html) (e.g. "Marked Style: Grump").

Track CSS changes
: When this is enabled, Marked will watch the current Style for disk changes, aiding in custom style editing and web development.

Additional CSS
: CSS added here will be included after the normal stylesheet with all themes. Among other things, you can use it to override settings across the board without editing internal styles.
: This applies to all documents and all styles. If you want to apply custom CSS to documents based on conditions, use Custom Rules under {% prefspane Processor %}.

### Include Scripts [include-scripts]

Syntax Highlighting
: Turn on highlight.js [syntax highlighting](Syntax_Highlighting.html) for code blocks. Select a theme from the dropdown.
: If **Only if language specified** is checked, syntax highlighting will only be applied to fenced code blocks with a language specified.

Enable MathJax
: Loads [MathJax](MathJax.html) for displaying MathML equations. Choose **Local** (bundled) or **CDN** from the dropdown.
: **Additional Packages** opens a sheet to include extra MathJax packages (for example Physics and Chemistry).
: **Advanced Configuration** opens a sheet for custom MathJax configuration.

Enable KaTeX
: Loads [KaTeX](MathJax.html#katex) as an alternative to MathJax. Only one or the other may be selected.

Number equations
: If applicable, Marked will add figure numbers to rendered equations. Choose **Left Side** or **Right Side** for numbering. If using MathJax, you can choose **AMS only** to number only AMS equations.

Mermaid
: Loads [mermaid.js](https://mermaid.js) from a CDN to enable Markdown-style diagramming. The hook required to render Mermaid diagrams on every document update is included automatically.

Pan and zoom diagrams
: When Mermaid diagrams are present, enable zoom with {% kbd cmd %}-scroll and pan by clicking and dragging.
