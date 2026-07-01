# <%= @title %>

Marked can open Rich Text Format (`.rtf`) and RTFD (`.rtfd`) documents directly. Drag a file to Marked or use {% appmenu File, Open... ({{cmd}}O) %}. The document is converted to Markdown for preview and export.

This works well with documents from **Pages**, **TextEdit**, **Word**, and other apps that save RTF or RTFD. Marked is still a **preview** tool: you edit in the original application and Marked updates when you save.

## How conversion works

Marked converts RTF to HTML using the system text engine, then to Markdown. The converter:

- Maps **large paragraph font sizes** to heading levels (relative to the most common body size in the document)
- Preserves **bold**, *italic*, and links where possible
- Extracts **images** from RTFD bundles and embedded attachments
- Does **not** treat RTF filenames as image captions (see Images below)

The same conversion pipeline is used for Scrivener RTF compile and for RTF files included in other documents.

## Live preview

When you save the RTF or RTFD file in another application, Marked detects the change and refreshes the preview automatically.

## Images

RTF does not define a separate "caption" field in a way Cocoa exports to HTML. What looks like a caption in your layout is usually **normal text** in the next paragraph, and Marked keeps that as body text.

Embedded images and images inside RTFD bundles (for example `pastedGraphic.png` in a Pages export) are copied to a cache folder under `~/Library/Caches/Marked/Watchers/`. Preview image paths point at those cached files until you export.

Marked does **not** use the image filename as alt text or a MultiMarkdown figure caption. You should not see `pastedGraphic.png` under the image unless you typed that text in the document.

## Export and other features

After conversion, Marked treats the document like other compiled sources (similar to [Scrivener](Scrivener_Support.html) and [DOCX](Working_with_DOCX.html)): export, statistics, and most preview features run against the generated Markdown stored in the Watchers cache.

## Limitations

Conversion quality depends on the source application. In general:

- **Headings** are inferred from font size, not from Word/Pages outline styles
- **Complex layout** (multi-column tables used only for positioning, text boxes) may not map cleanly to Markdown
- **Equations** in RTF are not supported in the preview (see [MathJax](MathJax.html) for Markdown math)
- **Legacy `.doc`** (binary Word) is not supported; save as DOCX or RTF first

For a one-off paste without saving a file, use [Clipboard Preview](Opening_Files.html#from-the-clipboard) instead.

## Related topics

- [PDF Support](PDF_Support.html) -- open PDF documents as Markdown sources
- [Working with DOCX](Working_with_DOCX.html) -- Word documents with change tracking and comments
- [Opening Files](Opening_Files.html) -- drag and drop, Open Recent, clipboard
- [Exporting](Exporting.html) -- Copy Rich Text and save RTFD (export), distinct from opening RTF as a source file
