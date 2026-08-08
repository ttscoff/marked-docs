# <%= @title %>

Marked can open PDF documents (`.pdf`) directly. Drag a file to Marked or use {% appmenu File, Open... ({{cmd}}O) %}. The document is converted to Markdown for preview and export.

PDF import works best on **smaller, text-based PDFs** (slides, articles, short reports). Large manuals, books, and scanned documents are supported but often convert slowly or imperfectly — see **Limitations** below.

Marked is still a **preview** tool: you do not edit the PDF inside Marked. Use {% kbd cmd E %} to open the PDF in **Preview** (or your system default), and Marked refreshes when the file changes on disk.

## How conversion works [how-conversion-works]

PDF import uses the [pdf22md](https://github.com/twardoch/pdf22md) library (MIT License; see [pdf22md License](PDF22MD_License.html)). Marked runs conversion in the background while showing a short **Converting** notice.

The converter:

- Extracts **text** from digital PDFs using PDFKit
- Uses **Vision OCR** on pages where embedded text is missing (common with scans)
- Detects **headings** from font size when possible
- Saves **images** into an `assets` folder next to the generated Markdown

Marked does **not** enable pdf22md's optional AI cleanup in the app. Conversion quality depends on how the PDF was created.

## Cache and live preview [cache-and-live-preview]

Converted Markdown and images are stored under Marked's Watchers cache (`~/Library/Caches/Marked/Watchers/PDF/`). The original PDF path stays the document source for file watching.

When you save or replace the PDF in another application, Marked detects the change and re-converts automatically (same coalesced reload behavior as [RTF](RTF_Support.html) and [Scrivener](Scrivener_Support.html)).

## Export and other features [export-and-other-features]

After conversion, Marked treats the document like other compiled sources: export, statistics, and most preview features run against the generated Markdown. Image paths in the preview point at cached assets until you export.

## Limitations [limitations]

Set your expectations accordingly — PDF-to-Markdown is useful, not perfect.

**What works well**

- **Vector and text-based PDFs** with real embedded text (exported from Word, Pages, InDesign, etc.)
- **Moderate length** — a few dozen pages usually convert in reasonable time with good structure

**What is unreliable**

- **OCR (scanned PDFs)** — Vision fills in missing text, but accuracy is often poor compared with a dedicated OCR tool; expect typos, broken words, and missed columns
- **Tables** — layout is guessed from text positions; merged cells, nested tables, and complex grids rarely survive as clean Markdown tables
- **Image placement** — figures are extracted to `assets/`, but alignment, captions, and text wrap around images are not preserved reliably

**Size and performance**

- **Large PDFs** (user guides, textbooks, long manuals) may take a **very long time** to convert, use substantial memory, or fail to produce useful Markdown. Marked stays responsive while conversion runs in the background, but there is no guarantee a 500-page manual will finish successfully
- If conversion completes with little or no content, Marked shows an error rather than leaving a blank preview

**Other limits**

- **Password-protected PDFs** are not supported in v1
- **Embedded PDF images in Markdown** (`![]()` referencing a `.pdf` file) are unrelated to PDF import — only opening a `.pdf` as the main document triggers conversion

For Word documents, use [Working with DOCX](Working_With_DOCX.html). For Rich Text, use [RTF and RTFD Support](RTF_Support.html).

## Related topics [related-topics]

- [Opening Files](Opening_Files.html) — drag and drop, Open Recent, clipboard
- [Exporting](Exporting.html) — save HTML, PDF, DOCX, and Markdown from the preview
- [pdf22md License](PDF22MD_License.html) — third-party MIT license text
