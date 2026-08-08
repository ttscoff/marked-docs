# <%= @title %>

Marked provides defaults for improving typography and export layout, as well as offering finite control over the options if you need more customization.

## Typography [typography]

### Hyphenation and widows [hyphenation-and-widows]

The _Auto-hyphenate in paragraphs_ option allows Marked to determine where a line would best be hyphenated to improve the "rag" of a paragraph. This is most useful when using a style with justified alignment, but can improve reading flow in longer paragraphs as well.

The _Prevent widows in headlines and paragraphs_ option, if enabled, will force breaks in headlines and paragraphs to prevent single, short words from ending up on a line by themselves.

Marked automatically connects headlines with the following element, to prevent orphaned headlines when exporting to a paginated format (PDF, print).

### Punctuation marks [punctuation-marks]

If your processor is set to MultiMarkdown, you'll have the option to enable or disable "smart punctuation" using the _Generate typographically correct quotes and punctuation_ option. If enabled, paired double and single quotes will be turned into "curly" quotes, apostrophes will be replaced with typographically correct symbols, and other automatic adjustments are performed.

### Footnote markers [footnote-markers]

In the Layout and Typography section of the {% prefspane Style %}, _Surround footnote markers with square brackets_ is enabled by default when using the MultiMarkdown processor, and creates footnote markers within the document which are surrounded by square brackets (e.g. "[1]"). To disable the creation of the square brackets, uncheck this option.

## Outline mode [outline-mode]

Outline mode will display any file containing a hierarchical series of headers as an APA or decimal outline. The default is APA style, but this can be toggled off.

In the {% prefspane Style %} under "Layout and typography," you can add filename extensions for which Outline mode is automatically enabled. This is especially useful for OPML and supported mind map files (such as iThoughtsX and MindNode). The extension should be only the alphanumeric portion of the filename appearing after the last dot character.

Toggle the default outline mode with the _Use APA Style_ checkbox. This can be toggled temporarily from the Gear menu of a document window.


## Poetry [poetry]

The _Style verbatim code blocks as poetry_ option in the {% prefspane Style %} will cause blocks indented by 4 or more spaces to display using the theme's "poetry" styling. This is usually a non-syntax-highlighted, italicized section.

Line breaks are preserved in these blocks by default, so it provides an easy way to incorporate poetry and lyrical sections into a document that doesn't have other need for code blocks.

> This setting adds a "poetry" body class that can be used in custom themes to style code blocks and other elements when "poetry mode" is enabled.

## Code block wrapping [code-block-wrapping]

The _Allow themes to wrap text inside code blocks_ lets the Preview Style determine how to format code blocks. Disabling this option forces all code blocks to scroll horizontal overflow rather than wrapping it, regardless of the current preview style.

## Working full screen [working-full-screen]

When using Marked in full screen mode (Control-Command-F), you may want to limit the width of displayed text to create a centered column of readable content. The _Limit text width in Preview_ checkbox will enable a slider with which you can define the maximum width of the displayed content. This affects non-full-screen display as well.

