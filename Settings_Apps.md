# <%= @title %>

Options in the {% prefspane Apps %}:

(See [Additional App Support](Additional_Application_Support.html))

![Settings: Apps][1]

[1]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane-scroll

### General settings [general-settings]

Text Editor
: Select a text editor to receive the current document when you type {% kbd cmd E %}.

Edit new files automatically
: When using the "New File" command, this option will automatically open the created file in your chosen external editor.

Links to text files should open in:
: Determine Marked's behavior when a link clicked in a preview window leads to a local text file.

Image Editor
: Select an application to open when a local image is right clicked and "Edit image" is selected.

Image annotation/markup editor
: Select an application to open when a local image is right clicked and "Annotate image" is selected.

If no editor is chosen, Marked presents a menu of installed applications when you edit or annotate. The menu includes common Markdown, image, and annotation tools found on your Mac, an **Other…** option to pick any app from `/Applications`, and **Always use this app** (enabled by default) to save your choice as the default. Use the clear button (circle with an X) next to each Choose control in {% prefspane Apps %} to remove a selection and return to the picker.

### Application-specific settings [application-specific-settings]

Show comments and annotations by default
: If checked, annotations made in Scrivener, Fountain, Word, and CriticMarkup documents will show up highlighted in the preview. Uncheck to hide completely. These can also be toggled while reading a document from the {% appmenu Gear, Proofing ({{ctrl}}{{cmd}}C)%} menu.
: When comments are enabled, comments and footnotes will appear in a sidebar. Hovering over a comment will point to where it occurs in the document.

#### DocC [docc]

[(Info on DocC Support)](DocC_Support.html)

Resolve DocC image references
: Inside a `.docc` documentation catalog, resolve extensionless `![](ImageName)` references to images in the catalog `Resources` folder, including `~dark` and `@2x` variants.

Resolve dark and @2x image variants
: For local images with a file extension (`images/icon.png`), detect companion `~dark` and `@2x` files in the same folder and emit responsive `<picture>` markup. Works in any Markdown or HTML document, not only DocC catalogs. See [Image Variants](Image_Variants.html).

#### Hookmark [hookmark]

Resolve hook:// URLs in images and links
: Marked can read URLs created by Hookmark, resolving them to their path on disk.

#### Leanpub/GitBook [leanpubgitbook]

Enable Leanpub support
: Interpret files named `Book.txt` as index files and handle special Leanpub syntax.

Enable GitBook support
: Interpret files named `SUMMARY.md` as index files for GitBook documentation.

#### Markdownifier [markdownifier]

Use inline links
: Markdown documents created by the Markdownifier will use inline instead of reference links.

#### MarsEdit [marsedit]

Include post title as Markdown header (h1)
: Use the title of the selected post as a Markdown header.

Show metadata as table
: When enabled, metadata such as categories and titles will be displayed as a Markdown table in the preview.

#### Folders [folders]

Only preview these extensions
: When opening a folder, Marked will look for the most recently changed document, defaulting to extensions such as `md`, `mmd`, and `html`. The list here overrides the default.

#### Scrivener [scrivener]

[(Info on Scrivener Support)](Scrivener_Support.html)

Include document titles as Markdown headers
: Parse the title of pages and nested pages to create hierarchical Markdown headers.

Add compile metadata (title, author) when missing
: When a Scrivener project has no `metadata` document or existing MultiMarkdown header, prepend Title and Author from the project's compile settings (`Settings/compile.xml`).

Open .scriv files in Scrivener when opened in Marked
: When a Scrivener document is opened in Marked, automatically open it in Scrivener as well.

#### Word [word]

Convert change tracking <-> CriticMarkup
: If enabled, change tracking in Word documents will be converted to CriticMarkup when imported, and CriticMarkup will be converted to Word change tracking when exporting DOCX files.

#### Mind Maps/Outlines [MindMapsOutlines]

Embed as Mermaid mind maps
: Each checkbox controls one included format. When **on**, the included file is converted to a Mermaid mind map diagram (tidy-tree layout). When **off**, Marked uses the alternative for that format.
: **Mind maps** — iThoughts X (.itmz), MindManager (.mmap), FreeMind (.mm). If on: Mermaid mind map. If off: iThoughts embeds its preview image; MindManager and FreeMind convert to nested Markdown lists.
: **OPML files** (.opml). If on: Mermaid mind map. If off: nested Markdown list.
: **OmniOutliner outlines** (.ooutline). If on: Mermaid mind map. If off: nested Markdown list (or checklist where applicable).
: **Bike outlines**. If on: Mermaid mind map. If off: nested Markdown list.
