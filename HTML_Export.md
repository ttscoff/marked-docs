# <%= @title %>

Marked exports HTML from your **live preview** --- the same rendered output you see on screen. Use HTML export when you need a snippet to paste into a blog or CMS, or a self-contained `.html` file with embedded styles and images you can open in any browser or host anywhere.

The typical workflow is **preview first, export HTML second**: open or compile your document in Marked, choose a theme, proofread in the live preview, then export when the markup looks right.

## Two ways to get HTML [two-ways-to-get-html]

### Copy HTML (snippet) [copy-html-snippet]

**Copy HTML** puts the preview's HTML source on the clipboard --- ready to paste into WordPress, Ghost, Squarespace, a forum, an email template, or any app that accepts HTML fragments.

* Gear menu → **Copy HTML**, or {% kbd shift cmd C %} with the preview focused
* Copies the **rendered body HTML** (not a full document with `<html>` wrapper)
* Optional: enable **Embed images when copying HTML** in {% prefspane Export %} to Base64-encode local images as `data:` URLs in the pasted source

Copy HTML is ideal when your destination already has its own stylesheet and you only need the content markup.

### Save HTML (file) [save-html-file]

**Save HTML** writes a complete `.html` file to disk.

* Export → **Save HTML**, {% kbd cmd S %}, or **HTML** from the [Export Panel](Exporting.html#drawer) ({% kbd shift cmd e %})
* Choose filename and location in the save dialog
* Configure export options in the dialog accessory (see below)

Save HTML is ideal for archiving, sharing a standalone file, or opening the result directly in a browser.

## Save HTML options [save-html-options]

The Save HTML dialog includes an export profile picker and these options:

![Save HTML options][savehtml]

**Include style in output**

When checked, Marked embeds the selected preview theme's CSS in a `<style>` block inside the exported file. Pick any built-in theme or [Custom Style](Custom_Styles.html) from the style menu next to the checkbox. The output is a complete HTML document with `<!DOCTYPE html>`, `<head>`, and a `#wrapper` div around your content --- matching what you previewed.

When unchecked, Marked saves a minimal HTML document with your rendered content only (no Marked theme CSS). Use this when you want raw HTML to paste or import into another system that supplies its own styling.

**Embed local images for standalone HTML**

When **Include style in output** is enabled, you can also embed local images as Base64 `data:` URLs inside the HTML file. The result is a single file you can email, upload, or host without a separate `images/` folder.

* Works with images referenced by **relative or absolute paths** on your local drive
* Avoid `file:///` URLs --- they cannot be embedded reliably
* Remote images (http/https) stay as external URLs unless you download them first
* Base64 embedding can produce large files; use it when portability matters more than file size

**Include Syntax Highlighting JavaScript**

When syntax highlighting is enabled in {% prefspane Preview %}, this option adds highlight.js CSS and JavaScript from a CDN so code blocks keep their colors in the exported file. The exported HTML needs an internet connection for the CDN resources to load.

**Include MathJax or KaTeX CDN link**

When [MathJax](MathJax.html) or KaTeX is enabled for preview, you can include the matching CDN scripts in the saved HTML so equations render in a browser. Like syntax highlighting, this requires network access when viewing the file unless you host the scripts yourself.

**CriticMarkup export type**

Documents with [CriticMarkup](CriticMarkup.html) can choose whether the export shows edited text, original text, or full markup.

**Export profile**

Select a saved [Export Profile](Exporting.html#export-profiles) to restore your preferred HTML export settings (embedded styles, images, syntax highlighting, math) in one step.

## Styling with built-in and custom themes [styling-with-built-in-and-custom-themes]

The **preview style** drives HTML appearance when **Include style in output** is checked:

1. Choose a style from the preview window style menu (or set a default in {% prefspane Style %}).
2. Review typography, headings, code blocks, and images in the live preview.
3. Save HTML with the same style selected in the export dialog.

Every built-in Marked theme --- Swiss, GitHub, Manuscript, and the rest --- can be embedded. [Custom Styles](Custom_Styles.html) and styles from the [Style Manager](Custom_Styles.html) work the same way.

I> Some preview-only CSS (fixed positioning, viewport tricks, Dark Mode `@media screen` inversion) may not translate one-to-one outside Marked. Open the saved file in a browser to verify before publishing.

For authoring guidance, see [Creating Custom CSS](Writing_Custom_CSS.html).

## Metadata and MultiMarkdown headers [metadata-and-multimarkdown-headers]

MultiMarkdown metadata at the top of your source file can affect HTML export:

* **`Title:`** --- used for the `<title>` element when saving a full HTML document
* **`XHTML Header:`** / **`HTML Header:`** --- injects additional tags into the exported `<head>` (scripts, link tags, meta tags)
* Other metadata keys are processed according to your [Markdown processor](Choosing_a_Processor.html)

If you use metadata for export settings but do not want keys visible in other outputs, wrap them in HTML comments --- Marked finds and processes commented metadata anywhere in the document. See [Per-Document Settings](Per-Document_Settings.html).

## Multi-file documents [multi-file-documents]

For books and chapter compilations, use [Multi-File Documents](Multi-File_Documents.html). Marked previews the merged document and exports one HTML file from the compiled result. Included files are marked with HTML comments showing their source paths --- useful when auditing which chapter contributed which section.

## Pasting into other applications [pasting-into-other-applications]

| Destination | Suggested approach |
| :-- | :-- |
| Blog / CMS with its own theme | **Copy HTML** (snippet, no embedded Marked CSS) |
| Static site or archive | **Save HTML** with **Include style in output** |
| Email or file share (one attachment) | **Save HTML** with **Embed local images** |
| WordPress, Ghost, Notion, etc. | **Copy HTML**; enable **Embed images when copying HTML** if the editor does not resolve local paths |
| Further editing in a code editor | **Save HTML** without embedded style, or copy snippet and wrap manually |

[Copy Rich Text](Exporting.html#rtfexportoptions) (gear menu) is an alternative when the target app accepts formatted text rather than HTML source.

## Related topics [related-topics]

* [Exporting](Exporting.html) --- export panel, profiles, and other formats
* [EPUB Export](EPUB_Export.html) --- ebook output with embedded CSS
* [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) --- preview workflow before export
* [Custom Styles](Custom_Styles.html) and [Settings: Export](Settings_Export.html)
* [HTML Specific Settings](HTML_Specific_Settings.html) --- processor options for HTML output
* [AppleScript export](AppleScript_Support.html) --- automate HTML copy and save

[savehtml]: images/SaveHTML.png @2x width=740px height=229px 
r
