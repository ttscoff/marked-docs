# <%= @title %>

Marked exports fully compliant EPUB files from your Markdown preview --- styled with the same built-in and custom themes you use on screen, and readable in **Apple Books**, **Kobo**, and other standard EPUB readers.

The typical workflow is **preview first, export EPUB second**: open or compile your document in Marked, choose a theme, proofread in the live preview, then export when the book is ready.

## Exporting an EPUB

Open the [Export Panel](Exporting.html#drawer) ({% kbd shift cmd e %}) or use **Save as** from the gear menu and choose **EPUB**.

The EPUB save dialog lets you set:

* **Title** --- defaults to MultiMarkdown metadata or the filename
* **Author** --- defaults to your macOS user name; the last author you enter is remembered for the next export
* **Date** --- ISO format; editable at save time
* **Cover image** --- optional PNG or JPG; Marked generates a default cover preview when none is set

Marked embeds local images in the EPUB and can download remote images so the finished file is self-contained. Exported EPUBs are validated as well-formed XHTML before saving, producing files that meet EPUB standards for distribution and accessibility.

See [Export Profiles](Exporting.html#export-profiles) to save EPUB metadata and export settings for repeat use.

## Styling with built-in themes

The **preview style** selected for your document drives EPUB appearance. Every built-in Marked theme --- Swiss, GitHub, Manuscript, and the rest --- can be applied to EPUB export.

1. Choose a style from the Preview window style menu (or set a default in {% prefspane Style %}).
2. Review typography, headings, code blocks, and images in the live preview.
3. Export to EPUB --- Marked bundles the theme's CSS into the EPUB package.

Marked also applies export-specific CSS on top of your preview theme so elements like footnotes, tables, and syntax-highlighted code blocks render correctly in e-readers. Outline-mode documents use outline-optimized export styles; [Leanpub](Multi-File_Documents.html) `Book.txt` indexes use Leanpub-oriented export styling automatically.

I> EPUB readers ignore some web-only CSS (fixed positioning, viewport tricks, etc.). What you see in Marked's preview is the goal, but e-reader layout engines may simplify spacing and fonts. Test in Apple Books or your target reader before publishing.

## Styling with custom themes

[Custom Styles](Custom_Styles.html) work the same way for EPUB as for preview and PDF:

* Add CSS files in {% prefspane Style %} or the [Style Manager](Custom_Styles.html).
* Select the custom theme before exporting.
* Marked embeds your stylesheet in the exported EPUB.

Tips for EPUB-friendly custom CSS:

* Keep layouts fluid --- use relative units and `max-width: 100%` on images (`#wrapper img { max-width: 100%; }` is a good baseline).
* Avoid `@media print` rules for ebook styling; EPUB uses the main screen styles plus Marked's export stylesheet.
* [Dark Mode](Previewing.html) inversion in preview uses `@media screen` queries; most EPUB readers use the light stylesheet unless the reader app applies its own dark theme.
* Use [Additional CSS](Custom_Styles.html) in Style settings to tweak all themes at once (for example, uniform body font size across exports).

For authoring guidance, see [Creating Custom CSS](Writing_Custom_CSS.html).

## Syntax highlighting and math

If **Include syntax highlighting in export** is enabled in {% prefspane Export %}, code blocks export with the same syntax colors as your preview. Math rendered with [MathJax](MathJax.html) is included in the EPUB as appropriate for e-reader support.

## Metadata in your source file

You can set EPUB metadata in the document instead of the save dialog. At the top of a Markdown file (or in a Scrivener metadata page), use MultiMarkdown-style keys:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

`cover image` accepts a path relative to the document or an absolute path. PNG and JPG are supported. Dialog values override or fill in missing metadata at export time.

## Multi-file books

For long works, compile chapters with [Multi-File Documents](Multi-File_Documents.html) --- index files, Scrivener exports, Leanpub `Book.txt`, or GitBook-style indexes. Marked watches included files, previews the full book, and exports one EPUB from the compiled HTML.

Headings in the compiled document become the EPUB [table of contents](Document_Navigation.html) for navigation in Apple Books and other readers.

## Reading and publishing

Exported EPUBs open directly in **Apple Books** (double-click the file or use **File → Add to Library**). They also work in Kobo, Thorium, Calibre, and most EPUB 3-compatible apps.

### Apple Books

Drag an exported `.epub` onto the Books app or add it through **File → Import**. Custom typography and cover art from your Marked theme carry through. Use Apple Books on Mac, iPad, or iPhone to verify layout before sharing.

### Kindle Direct Publishing (KDP)

EPUB is an accepted upload format for [Kindle Direct Publishing](https://kdp.amazon.com/). Export from Marked and upload the `.epub` file; Amazon converts it for Kindle delivery. KDP also accepts [DOCX](Working_with_DOCX.html). See Amazon's [supported eBook formats](https://kdp.amazon.com/en_US/help/topic/G200634390) for current requirements.

**MOBI is not required** for new KDP titles. Marked does not export MOBI.

Optional: preview Kindle layout with Amazon's free [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170) before uploading.

## Related

* [HTML Export](HTML_Export.html) --- standalone HTML with embedded styles and images
* [Exporting](Exporting.html) --- export panel, profiles, and other formats
* [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) --- preview workflow before export
* [Custom Styles](Custom_Styles.html) and [Custom Style Generator](Custom_Style_Generator.html)
* [Multi-File Documents](Multi-File_Documents.html) --- books and chapter indexes
* [AppleScript export](AppleScript_Support.html) --- automate EPUB export
