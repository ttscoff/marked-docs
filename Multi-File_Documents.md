# <%= @title %>

Marked allows several different syntaxes for including one file within another.

## Marked Syntax [marked-syntax]

You can include external files in a single preview document by using the special syntax `<<[path/file]` at the beginning of a line. The line should have blank lines above and below it, and the path is assumed to be relative to the main document unless it begins with a slash (`/`) or a tilde (`~`). Slash (root directory) and tilde (home directory) may be used to define absolute paths to files. No path is needed if the external files are in the same folder as the main document, just put the filename (case sensitive and including extension) in the square brackets.

You can use the metadata headers "Include Base" or "Transclude Base" to change the base location for included files, e.g.:

    Transclude Base: ~/Desktop

*Note that when viewing documents with included files, you can type "I" (shift-i) to see which included file is in the visible area. Pressing return while the included file path is displayed will open the included file in the default editor.*

Using this feature you can build large documents/books using multiple files (e.g. a file for each chapter) and then specify the document order in a single index file. It doesn't matter how any of the files are named or how the folders are organized; the file you open in Marked will be considered the index and the files listed inside it will be included. An example of an index file for a three-part document:

Folder structure:

![][1]

   [1]: images/multifiledocumentstructure.jpg @2x width=316px height=163px class=center

Index.md:

	# Document title

	## Section 1

	<<[sections/section1.md]

	## Section 2

	<<[sections/section2.md]

	## Section 3

	<<[sections/section3.md]

Opening Index.md in Marked will display its contents with all three included files expanded inside. All included files will be watched for changes. Unlike the open document in Marked, included file tracking depends on Spotlight to obtain updates and must exist in a Spotlight-indexed folder on your disk.

You can also include code snippets and raw html or text using [variations of this syntax](Special_Syntax.html#includingcode).

The final HTML export of a document containing includes will have HTML comments containing the relative path of the included file at the beginning and end of the imported text.

**Note:** the more files included in a document, the slower the overall compile time of the preview will be. Marked tries to optimize and cache the process, but expect some rendering delays as your document size increases.

## MultiMarkdown Transclude Syntax [multimarkdown-transclude-syntax]

You can also use `{{filename}}` syntax based on the newer MultiMarkdown spec. Marked will recognize `Transclude Base: path` in MMD metadata and use it as the base for file transclusion.

Transclude Base will only be recognized in the parent document, not in additional included documents. All nested includes must have paths based on the initial Transclude Base, or from the location of the parent document.

The fenced code syntax that MultiMarkdown provides for including files without processing will not work in Marked. To do this, please use the `<<(file)` (code block) or `<<{file}` (raw) syntax.

## IA Writer Block syntax [ia-writer-block-syntax]

Marked 2.5.11+ supports the IA Writer [Content Block][ia] syntax. This is a reference beginning with a forward slash (`/`) on its own line. It can be a code sample, an image, a markdown file, or a CSV file. All will be handled appropriately based on the extension of the included file, and CSVs will be [converted into Markdown][csv] tables if possible.

In IA writer, included files are brought into the iCloud container and don't always require "actual" paths. In Marked, unless included files already exist in the same folder as the file being previewed, this syntax should be used with a path, either absolute or relative. The first slash will be ignored, so if it's an absolute path, start with two slashes.

A code snippet in the same folder as the document being previewed:

    /snippet.h

Relative path to a subdirectory called "images":

    /images/image.png "optional title"

Absolute path to the Documents folder:

    //Users/username/Documents/content.csv

[ia]: https://github.com/iainc/Markdown-Content-Blocks
[csv]: Creating_Tables_using_CSV_files.html

## How outline, mind map, and CSV includes are converted [how-outline-mind-map-and-csv-includes-are-converted]

When you include certain file types with `<<[path]` or IA Writer block syntax, Marked converts them instead of inserting raw file contents. Outline and mind map behavior depends on the file extension and your [Settings: Apps → Mind Maps/Outlines][mindmaps] preferences. CSV/TSV files are always converted to Markdown tables (see [Creating Tables using CSV files][csv]).

| Format | Extension | When "Embed as Mermaid" is **on** | When **off** |
|--------|------------|-----------------------------------|--------------|
| **iThoughts X** | .itmz | Mermaid mindmap diagram (tidy-tree) | Preview image from the .itmz |
| **MindManager** | .mmap | Mermaid mindmap diagram | Nested Markdown list |
| **FreeMind** | .mm | Mermaid mindmap diagram | Nested Markdown list |
| **OPML** | .opml | Mermaid mindmap diagram | Nested Markdown list |
| **OmniOutliner** | .ooutline | Mermaid mindmap diagram | Nested Markdown list |
| **Bike** | .bike | Mermaid mindmap (filename as root node) | Nested Markdown list (no document title) |
| **CSV / TSV** | .csv, .tsv | Markdown table ||
| **RTF / RTFD** | .rtf, .rtfd | Markdown via RTF conversion (see [RTF and RTFD Support](RTF_Support.html)) ||
| **PDF** | .pdf | Markdown via PDF conversion when opened as the main document (see [PDF Support](PDF_Support.html)) ||

Each outline/mind map format has its own checkbox under *Mind Maps/Outlines* (Mind maps, OPML files, Bike outlines, OmniOutliner outlines). Toggling a format off uses the "off" behavior for that type only. See [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html) for format details and [Settings: Apps][mindmaps] to change these options. For CSV conversion details, see [Creating Tables using CSV files][csv].

[mindmaps]: Settings_Apps.html#MindMapsOutlines

## Book Formats [book-formats]

Marked also supports index files in formats like [Leanpub][lp], [GitBook][gb] and mmd\_merge (MultiMarkdown). Files included in book format indexes will be watched for changes and the result is a complete preview of your compiled document, just like the "Index.md" example above.

### Leanpub [leanpub]

If you enable the option in the {% prefspane Apps %} under Leanpub/GitBook support, files named "Book.txt" will be treated as Leanpub index files automatically. The older "frontmatter:" format is also recognized.

[Leanpub documentation.][lpdocs]

Leanpub Book.txt example:

    frontmatter:
    Acknowledgments.txt
    Preface.txt
    Introduction.txt
    mainmatter:
    Markdown.txt
    Sample Books.txt
    Inserting Images.txt


### mmd_merge [mmdmerge]

For mmd\_merge, Marked require that the first line be "#merge" (a special Marked trigger for mmd\_merge, treated as a comment and ignored by other processors).

[mmd_merge documentation.][mmdm]

mmd_merge example:

    #merge
    metadata.txt
    Chapter-1.md
        sub-chapter-1-1.md
        sub-chapter-1-2.md
    Chapter-2.md
        sub-chapter-2-1.md
        sub-chapter-2-2.md
    FAQ.md
    Acknowledgments.md

### GitBook [gitbook]

GitBook formatting uses a Markdown list to create the structure and Table of Contents. If GitBook support is enabled in the {% prefspane Apps %} under Leanpub/GitBook support, a file named SUMMARY.md will be read and automatically converted to mmd_merge format, allowing a full preview of your GitBook document.

[GitBook documentation.][gbdocs]

GitBook SUMMARY.md example:

    # Summary

    * [Part I](part1/README.md)
        * [Writing is nice](part1/writing.md)
        * [GitBook is nice](part1/gitbook.md)
    * [Part II](part2/README.md)
        * [We love feedback](part2/feedback_please.md)
        * [Better tools for authors](part2/better_tools.md)

GitBook allows for anchors to be used in SUMMARY.md table of contents, but Marked will ignore these and only include the base document one time.

[gbdocs]: https://github.com/GitbookIO/gitbook/blob/master/docs/pages.md
[lp]: http://leanpub.com/
[lpdocs]: https://leanpub.com/help/manual#leanpub-auto-how-to-set-the-books-structure
[mmdm]: http://fletcher.github.io/peg-multimarkdown/#howdoisplitamultimarkdowndocumentintoseveralparts
[gb]: https://www.gitbook.com/

## Multi-file Document Preview Features [multi-file-document-preview-features]

![Included File Boundaries][2]

   [2]: images/includeboundaries.png @2x width=859px height=239px class=center

When viewing a document containing included files, you can use two features to help figure out which file you're looking at.

* **Keyboard:** Pressing {% kbd shift I %} will briefly display a popup showing the title of the file currently visible at the scroll position of the preview.
    * Pressing {% kbd Return %} following {% kbd I %} will edit the displayed file with your external editor.
* **Mouse:** Selecting "Show Boundaries of Included Files" from the Gear menu ({% kbd ctrl cmd B %}) will add a colored bar to the left side of the preview, segmented to show the beginning and end of included files. It also shows nested includes. Hovering over a section of this bar will show the name of the file it represents, and clicking it will open that file in your chosen editor.
