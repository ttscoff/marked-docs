# <%= @title %>

Turning your Markdown into a finished document.

## Export after preview [export-after-preview]

Marked's preview is the basis for export --- what you see in the preview window is what you get in PDF, DOCX, EPUB, and other formats (modulo export-specific settings such as margins, headers, and pagination). Set up your style and proofread in preview first, then export when the document is ready. See [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) for the full preview workflow.

## The Export Panel [drawer]

![Export Panel][export-panel]

The **Export Panel** is a keyboard-driven, spotlight-style panel that provides quick access to all export options. Open it by clicking the export icon in the status bar or by pressing {% kbd shift cmd e %}.

![Export Button][expbut]

The Export Panel allows you to save your document as HTML, single-page PDF, paginated PDF, RTF package, or a Microsoft Word DOC or DOCX file. You can also save to a new Markdown file (Marked-specific features will be rendered and their results included), an Open Document (ODT), or as OPML for use in other applications.

## Copy HTML [copyhtml]

Use the Copy HTML feature to put the HTML source code for your preview into your clipboard without any hassle. You can select it from the gear menu, or just hit {% kbd shift cmd C %}. The copied HTML will be a snippet ready for insertion into a blog, forum or HTML document.

You don't need to be in the source view to copy. With the preview focused (click on it), just type {% kbd shift cmd C %} and you'll see a popup message letting you know that the source is in your clipboard.

## Save HTML [save-html]

![][exporthtmlaccessory]



The Save HTML command--accessible from the gear menu or by simply typing **{% kbd cmd S %}**--will allow you to save a full document ready for sharing or publishing.

You can optionally include any of Marked's styles (or one of your [custom styles][custom]) in your export, giving you a ready-to-go document with necessary formatting already embedded.

Additionally, you can choose to embed any local images included in the document within the exported HTML, allowing you to have a standalone document that can be hosted anywhere without needing to move the images with it. This only works with images referenced on your local drive with relative or absolute paths. Avoid using `file:///` paths if you want to make use of this feature.

## Export Markdown to PDF on Mac [export-markdown-to-pdf-on-mac]

Print/PDF Preview ({% kbd cmd P %}) will bring up a standard print dialog. Each preview style in Marked has its own accompanying print styles which remove backgrounds, modify type sizes and provide borders. The preview will print based on the currently-selected style.

Prominent on the print dialog box are the PDF and Preview buttons. PDF will give you a variety of options for exporting to PDF (based on your available applications) and Preview will export a PDF version directly to Preview.app where you can save or email it.

Printing to PDF using this method will include pagination. When printing to paper or PDF, page breaks may be inserted manually by using the [`<!--BREAK-->` syntax][break] or by setting options in the {% prefspane Export %} to use level one and/or level two headers as section dividers.

There is also a preference for turning horizontal rules (`<hr>`) into page breaks when printing. Doing so will replace the line created by the tag with a page break, removing it from the final output. The preview is unaffected by this setting.

![Print Margins][printmargins]

Page margins may be set in the {% prefspane Export %} and will affect Print and Paginated PDF output.

You can override margin settings per document using the `Margins:` metadata key. Values are interpreted as points; unit suffixes such as `px`, `pt`, and `em` are ignored. Use two numbers for vertical and horizontal margins (`10 20`), or four numbers for top, right, bottom, and left (`10, 20, 10, 20` or `10 20 10 20`). Metadata margins override {% prefspane Export %} settings.

### Headers and Footers [headers-and-footers]

Headers and footers defined in the the {% prefspane Export %} will appear at the top and bottom of any page printed or saved to paginated PDF, and in DOCX export. You can put any text in the upper left, upper center, upper right, lower left, lower center, and lower right. Center text is center-aligned on the page. The following variables will be replaced in the strings if used:

    %title = Document Title
    %date = Current Date
    %time = Current Time
    %page = Current Page Number
    %total = Total Page Number
    %path = Filesystem path to document
    %filename = Just the filename of the document
    %basename = The filename with no extension
    %logo/%image = A logo set in the image well in Header/Footer preferences
    %%(text) = Text to print only on the first page
    %h1/h2/h3/h4/h5/h6 = Section titles based on Markdown headers
    %sep(X) = Text to place between section titles if a subsection exists

**Print and paginated PDF** resolve `%h1`--`%h6` using Marked's pagination, so each page shows the heading hierarchy visible on that page. `%sep(X)` and `%md_*` metadata variables are also supported in print/PDF output.

**DOCX export** embeds `%logo`/`%image` in the Word header or footer (scaled to about 50px tall, matching print preview). Heading placeholders become Word **STYLEREF** fields that reference the exported `Heading 1`--`Heading 6` styles. Word updates those fields when the document is opened, based on Word's own layout and page breaks --- not Marked's preview pagination. `%md_*` metadata variables are substituted once at export time, the same as in print/PDF. `%sep(X)` is not converted in DOCX headers/footers.

`%title` will use any "Title:" info defined in MultiMarkdown Metadata headers, otherwise it will fall back to the filename without the file extension. To define a title using MMD Metadata, place the following on the first line of the document:

    Title: The title of your document

Follow the line with a blank line (or any other Metadata you want to define, followed by a blank line).

You can also use any MMD Metadata key as a variable by prefixing it with `%md_`, and combining the key's words as a lowercase string. For example, if your document has a metadata key at the top such as:

    Funky Monkey: The funkiest monkey

Then using `%md_funkymonkey` in a header field would put "The funkiest monkey" into the exported document in that header's location. Documents that do not contain that particular key will leave the field blank, allowing you to selectively add headers based on Metadata.

See [Date and Time Formats](Exporting.html#dateandtimeformats) for `%date` and `%time` format codes.

The "Page numbering offset" setting can be used to adjust what number the page numbers start at. For example, if you have a table of contents on the first page and want the numbering to start on the second page as page 1, set the offset to -1. Page 2 will now be page 1 in the header/footer (`%page`) and the total pages (`%total`) will be adjusted accordingly.

You can also specify a header/footer font for a specific document by using MMD metadata at the top of the file:

    Header Font: Mensch

Note that if you use a font family name, a default fontface will be selected. You can specify a variation by using the system name of the font. For example, in the case of Helvetica Neue Ultralight, you would use "Header Font: HelveticaNeueUltralight".

Additionally, you can specify a per-document header/footer font size with the metadata:

    Header Font Size: 10

### Date and Time Formats [dateandtimeformats]

The **Date format** and **Time format** fields in the {% prefspane Export %} control how `%date` and `%time` are rendered in headers and footers. Both fields use strftime-style format codes: a `%` followed by a letter. Literal text (such as `-`, `:`, or spaces) is copied as-is.

**Examples**

    %m-%d-%Y     → 06-20-2026   (Marked's default date format)
    %I:%M %p     → 3:45 PM      (Marked's default time format)
    %Y-%m-%d     → 2026-06-20
    %B %d, %Y    → June 20, 2026
    %a %H:%M     → Fri 15:45

**Common format codes**

| Code | Example | Description |
| ---- | ------- | ----------- |
| `%Y` | 2026 | Four-digit year |
| `%y` | 26 | Two-digit year |
| `%m` | 06 | Month (01--12) |
| `%B` | June | Full month name |
| `%b` | Jun | Abbreviated month name |
| `%d` | 20 | Day of month (01--31) |
| `%e` | 20 | Day of month (space-padded) |
| `%A` | Friday | Full weekday name |
| `%a` | Fri | Abbreviated weekday name |
| `%H` | 15 | Hour, 24-hour (00--23) |
| `%I` | 03 | Hour, 12-hour (01--12) |
| `%M` | 45 | Minute (00--59) |
| `%S` | 07 | Second (00--59) |
| `%p` | PM | AM or PM |
| `%x` | (locale) | Locale's preferred date |
| `%X` | (locale) | Locale's preferred time |
| `%c` | (locale) | Locale's preferred date and time |

**Print and paginated PDF** support the full strftime-style set above, plus additional codes such as `%j` (day of year), `%U`/`%W` (week number), `%z` (timezone offset), and `%Z` (timezone name). See the [Open Group strftime specification](https://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html) for a complete reference.

**DOCX export** supports the codes listed in the table above. Less common codes may be ignored or passed through unchanged.

Use **Restore Default Formats** in {% prefspane Export %} to reset to `%m-%d-%Y` and `%I:%M %p`.

### Per-Document Headers and Footers [per-document-headers-and-footers]

You can specify headers and footers on a per-document basis using MultiMarkdown metadata at the very top of the document:

    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date
    Print Footer Right: %page/%total

These will override any settings in preferences. Note that if you're using a processor other than MultiMarkdown and don't want your headers to show up in the document itself, you can use HTML comments, making sure you leave a blank line before the closing of the comment:

    <!--
    Print Header Left: %title
    Print Header Center: %basename
    Print Header Right: %date

    -->

## Save PDF [save-pdf]

This option saves your Preview directly to a PDF file on your drive. Your document will be rendered in its entirety, without page breaks. To include pagination in your output, use the Print/PDF options in the [Export Panel](#drawer).

## RTF export options [rtfexportoptions]

Marked can export RTF (Rich Text Format) data directly to your clipboard. Just choose the Copy Rich Text command from the gear menu.

Marked can also save your file as an **RTFD** (Rich Text Format) file. The RTFD format is a bundle format that includes an RTF file and any images embedded in the document.

## DOCX export [docx-export]

Exporting as DOCX will create a valid Microsoft Word document, with elements like headlines, headers/footers, emphasis, lists, etc. all mapped to valid Word styles. This means you can easily apply your own theme in Word.

See [Working with DOCX][DOCX] for more details about Word import and export.

## Export Markdown to EPUB [export-markdown-to-epub]

Marked can export 100% valid, 100% accessible EPUB documents. Select the EPUB export type, specify metadata like title, author, and date, and optionally add a cover photo. The saved file will be readable in any EPUB viewer.

The metadata needed for EPUB export can be included in the file itself, whether it's a Markdown document, Scrivener file (include a `metadata` page), or other book format. The keys to use are:

```yaml
title: Your Document Title
author: Your Name
cover image: path/to/image.jpg
```

The Cover Image key can include a path relative to the base document, or an absolute path. PNG or JPG files are acceptable.

If title is not set, it will default to the filename of the original document, and if author is not set, it will default to your macOS user's full name.

Date will always be set to the current date, and cannot currently be modified with metadata. It can be altered at the time of saving, though, as long as the formatting (ISO) remains intact.

### Publishing to Amazon Kindle (KDP) [publishing-to-amazon-kindle-kdp]

EPUB is an open format used by many reading apps and stores (Apple Books, Kobo, and others), not only Kindle. If you are publishing through [Kindle Direct Publishing (KDP)](https://kdp.amazon.com/), export EPUB from Marked and upload that file to KDP. Amazon converts it to its own Kindle delivery format (KFX) for readers.

KDP accepts several manuscript formats, including EPUB and DOCX (which Marked can also export). See Amazon's [supported eBook formats](https://kdp.amazon.com/en_US/help/topic/G200634390) and [eBook manuscript formatting guide](https://kdp.amazon.com/en_US/help/topic/G200645680) for requirements.

**MOBI is not required.** KDP no longer accepts MOBI uploads for new titles (including fixed-layout books, as of March 2025). Marked does not export MOBI, and you do not need a separate "Kindle" or Mobipocket file for KDP. If you prefer Amazon's layout tools, you can also prepare a book with [Kindle Create](https://kdp.amazon.com/help/topic/G8UZKZD45RTQNNVT), which produces KPF files.

Before uploading, you may want to check how your EPUB will look on Kindle devices using Amazon's free [Kindle Previewer](https://kdp.amazon.com/help/topic/G202131170). That is optional third-party software from Amazon, not part of Marked.

## Export Profiles [export-profiles]

Export Profiles allow you to save and quickly switch between different sets of export preferences. This is especially useful if you regularly export documents for different purposes — for example, one profile for print-ready PDFs with specific margins and headers, and another for web-ready HTML with embedded styles.

### Using Export Profiles [using-export-profiles]

When you first launch Marked, a "Default" profile is automatically created with your current export settings. You can see and select profiles in the export dialogs (PDF Export, Save HTML, etc.) using the profile popup menu at the top of the dialog.

**Creating a New Profile:**

1. Adjust your export settings in the {% prefspane Export %} or in any export dialog
2. In the export dialog, click the profile popup menu and choose "Add Profile…"
3. Enter a name for your profile (e.g., "Print Quality" or "Web Export")
4. The current settings are saved as that profile

**Loading a Profile:**

- Select a profile from the popup menu in any export dialog
- All export settings will immediately update to match that profile's saved values

**Saving Changes to a Profile:**

- After making changes to export settings, a "Save" button appears next to the profile popup
- Click "Save" to update the current profile with your changes
- The button is only enabled when there are unsaved changes

**Managing Profiles:**

- Choose "Manage Profiles…" from the profile popup menu to open the profile management window
- From there you can:
  - **Rename** profiles by double-clicking the name
  - **Duplicate** a profile to create a new one based on it
  - **Delete** profiles (the "Default" profile cannot be deleted)
  - View all available profiles in a list

### What Export Profiles Capture [what-export-profiles-capture]

Export Profiles save all export-related preferences, including:

- **PDF Settings**: Page size, margins, headers/footers, fonts, page breaks, table of contents
- **HTML Export**: Style embedding, image embedding, syntax highlighting, math rendering
- **Markdown Processing**: Text wrapping, link formatting, processor rules
- **CriticMarkup**: Export type and processing options
- **Syntax Highlighting**: Language detection and highlighting preferences
- **Math Rendering**: MathJax/KaTeX integration and equation numbering
- **Image Handling**: Embedding options, copy behavior, path settings
- **Typography**: Hyphenation, widows/orphans, font sizes
- **Export Behavior**: File naming preferences, conflict resolution

Profiles work across all export types: Markdown, HTML, Continuous PDF, Paginated PDF, EPUB, DOCX, ODT, TextBundle, RTF, and OPML.

### Profile Storage [profile-storage]

Profiles are stored in your Application Support folder at:

    ~/Library/Application Support/Marked/ExportProfiles.plist

This means your profiles persist even if you reset app preferences, and they survive app updates. You can back up this file to preserve your profiles across installations.

### Tips for Using Export Profiles [tips-for-using-export-profiles]

- **Create profiles for common workflows**: If you regularly export for print vs. web, create separate profiles for each
- **Use descriptive names**: Profile names like "Print - Letter" or "Web - Embedded Styles" make it clear what each profile is for
- **Save frequently**: The "Save" button appears whenever you've made changes — click it to preserve your adjustments
- **Start from existing profiles**: Use "Duplicate" in the management window to create variations of existing profiles rather than starting from scratch

[break]: Special_Syntax.html#pagebreaks
[DOCX]: Working_With_DOCX.html
[custom]: Custom_Styles.html
[dropbox]: http://dropbox.com
[expbut]: images/ExportButton.png @2x width=534px height=256px class=center
[export-panel]: images/export-panel-800.jpg @2x width=800 class=center
[exporthtmlaccessory]: images/SaveHTML.png @2x width=740px height=229px class=center
[printmargins]: images/PrintMargins.jpg @2x width=329px height=144px class=center
