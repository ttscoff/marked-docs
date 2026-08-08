# <%= @title %>

Use your two favorite writing tools together.

> Marked can still read Scrivener 2.0 files, but development will be focused on version 3 after Marked 2.5.11.

## Scrivener 3.0 Basics [scrivener-30-basics]

Drag a Scrivener project (.scriv) to Marked and it will be compiled and previewed. If you choose the option to open .scriv files in Scrivener (above), Marked will also launch Scrivener when you drag the file to Marked.

As with other documents, changes to Scrivener files are updated live on save. Also, when a Scrivener document is in the foreground in Marked, {% kbd cmd E %} will open it in Scrivener for you.

## Filtering binder documents [filtering-binder-documents]

When you open a Scrivener project in Marked, preview content is built only from the binder documents you select. Filtering is always active for `.scriv` files; the filter panel is just a convenient way to change what is included.

Open the panel from **Proofing > Filter Scrivener Documents** ({% kbd opt-cmd-f %}). The menu item shows a checkmark while the panel is visible. Closing the panel does not turn filtering off or reset your selections.

The filter panel lists your project's binder sections (Draft, Research, and other top-level binders except Trash). Each section is collapsed by default. Expand a section to see its documents and folders in an outline:

- Check or uncheck any **text document** to include or exclude it from the preview.
- Click a **folder** row to select or deselect all of its descendants. A dash in the checkbox means only some descendants are selected.
- Rows with **Include in Compile** turned off in Scrivener appear grayed, but you can still check them to preview them in Marked.
- **Images, PDFs, and other non-text** binder items appear in the list but cannot be selected.
- **Missing RTF** files still appear; if you add content in Scrivener while Marked is open, the preview updates on save like any other Scrivener change.

Use **Select All** and **Deselect All** at the top of the panel for the whole project. Each section header has **All** and **None** buttons for that section only. **Deselect All** means no documents are checked.

If nothing is selected, the preview shows a short message with a link to open the filter panel (`x-marked://scrivenerfilter`). You can use that URL in scripts or other apps to raise the panel for the front Scrivener document in Marked.

Your checkbox selections are saved per Scrivener project (by the project identifier in the `.scrivx` file) and restored the next time you open that project in Marked. The first time you open a project, Marked selects only **Draft** binder documents whose **Include in Compile** flag is Yes (or unset, which Scrivener treats as Yes). Research and other binders start unchecked; compile-excluded Draft items start unchecked but remain selectable in the list.

Scrivener 2 projects show only the **Draft** binder in the filter panel. Scrivener 3 projects include all binders except Trash.

The filter panel can stay open alongside other tools such as **Visualize Word Repetition**. Changing a checkbox recompiles the preview after a short delay; if a large project is still compiling, Marked cancels the in-progress import and starts again with your new selection.

## Markdown Headers From Scrivener Titles [markdown-headers-from-scrivener-titles]

Marked can also create hierarchical Markdown headers for you based on your Scrivener file's pages. To enable this, just check the option shown above.

## MultiMarkdown metadata [multimarkdown-metadata]

If the first document in your Draft folder is named "metadata", it will be treated as MultiMarkdown metadata at the beginning of the preview document. No header will be inserted for this section, regardless of the "Markdown Headers from Scrivener Titles" setting (described above), allowing the MultiMarkdown processor to read it as metadata and allow replacements and export options accordingly.

You can make this file YAML-formatted if your processor is one that handles YAML.

If you do not use a `metadata` document, Marked can also prepend MultiMarkdown metadata from your project's compile settings (`Settings/compile.xml`), using the same **Title** and **Author** fields Scrivener would export to MultiMarkdown. This is enabled by default (preference key `scrivenerCompileMetadata`). Custom metadata fields are only included when they appear in the project's **MMD Metadata** compile settings, not from per-document custom fields.

## Links [links]

For external (HTTP) links, you can use either Markdown syntax or Scrivener's link formatting. Marked will convert Scrivener format to Markdown before processing.

## Comments [comments]

Marked can process comments and footnotes created inline within the document.

## Tables [tables]

Marked can convert basic Scrivener tables. If you want to include a table in your output, however, it's best to do it in [MultiMarkdown table format](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#tables). (An app called [TableFlip](http://tableflipapp.com/) can make generating these a simple task.)

## Additional Scrivener Features [additional-scrivener-features]

In addition to the basic compiling and preview features, Marked also supports some Scrivener-specific conventions. First, in your Scrivener document, you can use "Preserve Formatting" inline or on a block of standalone text and it will be converted to code blocks in the preview.

Marked also reads _inline_ footnotes from Scrivener. If you enter a footnote within or at the end of a paragraph, it will be converted to a MultiMarkdown footnote in the preview.

## Using images in your Scrivener document [using-images-in-your-scrivener-document]

Images can be embedded in the Scrivener document, or referenced with Markdown image syntax. The Markdown version of an image tag is `![alt text](path/to/image.ext "optional title/description")`. Reference format may be used as well:

    ![alt text][img1]

    [img1]: /path/to/image.ext "optional description"

The base path for the HTML output in the Preview will be set to the folder containing the Scrivener document. Thus, placing images in the same folder as the working document will allow them to be accessed directly. If your Scrivener document is in `~/Desktop/TestDoc.scriv`, and you have an image called "testimage.png" in `~/Desktop/testimage.png`, you can add the image to your document by using:

    ![Test image](testimage.png)

Relative paths based on the parent folder of the document will work, and absolute paths will allow access to images anywhere but may not be as portable for HTML output.

## Security Note [security-note]

A cache folder will be created in ~/Library/Application Support/Marked when you open your .scriv file in Marked. This is not a protected folder, so if your original document is on an encrypted disk or otherwise protected, note that its contents will be unencrypted in the cache. For limited protection, you can ensure this cache doesn't show up in Spotlight by adding ~/Library/Application Support/Marked to your privacy settings in Spotlight.

See [Additional app integrations](Additional_Application_Support.html) for clipboard preview, wiki links, scripting, and the full list of per-app guides.

