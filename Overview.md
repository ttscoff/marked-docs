# <%= @title %>

{% apponly div %}
*For the latest version of this documentation, visit the [online version][help].*
{% endapponly %}

**Be sure to check out the growing collection of [Marked tutorial videos](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ).**

## What's Markdown?

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown is a basic markup language using simple symbols, allowing you to write HTML (and export to other formats) with simple syntax like `*italics*` and `**bold**`. Markdown was created by John Gruber, and is rapidly becoming the defacto standard for web publishing, note taking, and even book publishing. It lets you write without a bunch of toolbars and formatting fiddling, just getting words on the page and letting your processors (like Marked) handle styling and formatting.

Marked works with GitHub Flavored Markdown, CommonMark (GFM), Kramdown, and MultiMarkdown, and can convert syntax from several variants for preview (it can also be extended to work with just about any processor you need, including Textile, reStructuredText, Wikitext and more). I assume that --- since you're here --- you know what at least one of these markup languages are. If not, you should start at John Gruber's [Markdown Basics][daringfireball], check out [MarkdownGuide.org][mdguide]. Marked includes a full Markdown syntax guide under the help menu.

You can use the [Markdown Dingus](x-marked-3://dingus) to experiment with the different flavors of Markdown that Marked supports.

## What's Marked?

Marked is a live Markdown preview app for macOS --- an editor-agnostic (Multi)Markdown Preview application which watches a file for changes, updating the preview every time you save. By separating and automating the details of formatting it allows you to concentrate more on writing and less on presentation, all while still keeping tabs on your final product.

For setup workflows and editor-specific quick starts, see [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html). For a shorter product overview, visit [markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/).

Marked works with any file accessible locally, including iCloud documents. Just drag a text document from any editor's toolbar to Marked and it will render it as an HTML preview and start tracking changes, updating the preview as you write. It can even compile [multi-file documents](Multi-File_Documents.html) using a basic "include" syntax, or from Scrivener, Leanpub and mmd_merge index formats.

Marked has additional features, including word count and other document statistics, the ability to float above other applications or dim in the background, and it can display your work in a variety of well-crafted styles. It can output to print or PDF, Word documents, complete HTML documents (including styles and images) or copy HTML source or RTF data to your clipboard with a keystroke. Marked also has a basic AppleScript dictionary and a [URL handler](URL_Handler.html) which make it easy to integrate into your workflow.

Oh yeah, and it works with a ton of your favorite apps: text editors ranging from Vim and Emacs to Sublime Text and TextMate, Markdown editors like MultiMarkdown Composer, Byword, and iA Writer, even apps you might not expect like Ulysses, Scrivener, VoodooPad, MarsEdit, and more.

## Example Uses

Marked turns any text editor into a Markdown-enabled editor. Your preview is always available and it updates as you work.

* If your favorite editor doesn't offer a live Markdown preview, open the document you're working on in Marked and float the window off to the side for a full-featured Markdown writing experience.
* Do you like writing or blogging in MacVim or other terminal-based editor? Now you have a synced Markdown preview while you work.
* Marked also offers display capabilities above and beyond any existing Markdown preview, and can be used instead to provide full word count and document stats, writing suggestions, and even highlight mistakes in your Markdown formatting.
* You can also use Marked without an editor. Just drag Markdown files to the icon to preview them, print them and export them to PDF, DOC, RTF or HTML source code. Marked can also **open `.rtf` and `.rtfd` files** as source documents ([RTF and RTFD Support](RTF_Support.html)).
* In apps that autosave, you'll find the preview keeps up with your writing without any help. Use it with any editor... or *all* of your editors.
* Writing a book? Marked can compile multiple files for a full preview of your work, and even watch those included files for changes, updating the main document with every save. It can even watch an entire folder for changes, automatically switching the preview to whatever file you're currently updating. When you're ready, you can publish to EPUB, DOCX, or TextBundle formats.
* Working with an AI coding platform? Open a plan or documentation folder in Marked and whenever a Markdown file in that folder changes, Marked will display it, scrolling to the point of the most recent edit automatically. Marked displays Mermaid diagrams, and can handle all kinds of extended syntax. Keep track of plans and documentation while you work, without switching between files.
