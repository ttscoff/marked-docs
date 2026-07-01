# <%= @title %>

Options in the {% prefspane Processor %}:

![Settings: Processor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Process Markdown with

Default Markdown processor. The CommonMark processor is preferred for GitHub users, MultiMarkdown is ideal for writers, and Discount and Kramdown have specialized purposes. Marked compensates for some differences between syntax. See __Help->Markdown Reference__ for additional information.

Custom Rules
: Click the Custom Rules button to open the Rules Editor, where you can specify different processors and document transformations to run based on matching criteria. See [Custom Processor](Custom_Processor.html) for details.

New documents use custom
: When checked, new documents automatically use your saved **preprocessor** and/or **processor** from Custom Rules without requiring per-document setup.

Full Disk Access
: Click **Grant** to give Marked permission to read files outside its sandbox when using custom processors or other features that need broader file access.

To explore the differences between the processors, check out the [Markdown Dingus](Markdown_Dingus.html).

### HTML

Generate IDs on headlines
: Generate header IDs based on contents of h1-h6 tag.

Use random footnote IDs
: Generate random footnote IDs to avoid conflicts when multiple documents are displayed on one page.

Process Markdown inside of HTML
: By default, Markdown inside of HTML tags is usually ignored. This option forces Marked to continue processing within block elements. Note that some markup may cause issues.

### Rendering

Retain line breaks in paragraphs
: Respect line breaks in paragraph text, replacing with hard breaks instead of concatenating with the previous line.

Render GitHub checkboxes
: Render `- [ ]` and `- [x]` for creating checkboxes in lists. Checkboxes are rendered for preview but not functional within Marked.

Render GitHub :emoji:
: Render `:name:` shortcodes as GitHub-style emoji in the preview.

\#Text is tag
: Allows hashtags (`#` immediately followed by text with no space) to be interpreted as tags, not headlines. This functionality is default for Bear users.

Style tags
: When **#Text is tag** is enabled, display recognized tags with capsule styling. Tags can be shown or hidden from {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Text is tag enabled][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Render `==highlight==` and `~~delete~~`
: If this option is enabled, then `==highlight==` text will be rendered as an HTML `<mark>` tag, which will appear as a yellow highlight unless otherwise modified by a Style. Additionally, `~~delete~~` syntax will be rendered with a `<del>` tag.

: If __Render as CriticMarkup__ is enabled, then `==highlight==` and `~~delete~~` syntax will be converted to CriticMarkup, which can then be displayed in original, markup, and edited views.

Render `~text~` as underscore
: If this option is enabled, `~text~` surrounded by single tildes will be rendered as underlined. This conflicts with MultiMarkdown syntax for subscript and is disabled by default.
