# <%= @title %>

Options in the {% prefspane Processor %}:

![Settings: Processor][1]

[1]: images/screenshots/preferences-Processor.jpg @2x width=689px height=1031px class=preferencepane


### Process Markdown with

Default Markdown processor. The Discount processor is preferred for GitHub users, MultiMarkdown is ideal for writers. Marked compensates for some differences between syntax. See __Help->Markdown Reference__ for additional information.

Custom Rules
: Use the Custom Rules button to open the Custom Rules editor, allowing you to determine processing options and document transformations based on criteria. See the [Custom Processor documentation](Custom_Processor.html) for details.

New documents use custom
: Select preprocessor and/or processor to automatically enable rule processing on new documents. If you're using Custom Rules, you likely want both of these enabled.

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

\#Text is tag
: Allows hashtags, (`#` immediately followed by text with no space) to be interpreted as tags, not headlines. This functionality is default for Bear users.
: __Style tags__ causes tags to be displayed with "capsule" formatting to distinguish them from text. When this is enabled, tags can be shown/hidden using {% appmenu {{gear}}, Proofing, Show Comments %}.

![#Text is tag enabled][textistag]

[textistag]: images/textistag.jpg @2x width=896px height=274px class=center

Render `==highlight==` and `~~delete~~`
: If this option is enabled, then `==highlight==` text will be rendered as an HTML `<mark>` tag, which will appear as a yellow highlight unless otherwise modified by a Style. Additionally, `~~delete~~` syntax will be rendered with a `<del>` tag.

: If __Render as CriticMarkup__ is enabled, then `==highlight==` and `~~delete~~` syntax will be converted to CriticMarkup, which can then be displayed in original, markup, and edited views.

Render `~text~` as underscore
: If this option is enabled, `~text~` surrounded by single tildes will be rendered as underlined. This conflicts with MultiMarkdown syntax for subscript and is disabled by default.