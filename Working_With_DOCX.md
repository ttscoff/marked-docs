# <%= @title %>

Marked has extensive support for working with Microsoft Word files. The typical workflow is **preview first, export DOCX second**: open or watch your Markdown in Marked, refine styles and proofreading in the live preview, then export to Word when the document is ready.

## Opening DOCX files [opening-docx-files]

Marked can read a DOCX file and convert it to clean
Markdown. Valid style elements like headlines and lists will
be converted to their Markdown equivalent.

Change tracking and comments  will be converted to
CriticMarkup. Highlights will be converted to `<mark>` tags,
with colors where appropriate.

## Exporting DOCX files [exporting-docx-files]

Use the Export palette to generate a DOCX file from your
Markdown. In the save dialog you can specify a built-in
styles --- this style can easily be changed in Word just by
opening the theme selector and selecting a new theme.

### Headers and footers [headers-and-footers]

If you configure headers and footers in {% prefspane Export %}, they are included in the exported DOCX. Standard placeholders such as `%title`, `%date`, `%page`, and `%total` are substituted at export time. `%logo` and `%image` embed the logo from Header/Footer preferences. `%md_*` metadata variables resolve from the document's MultiMarkdown metadata. `%h1`--`%h6` become Word **STYLEREF** fields tied to the exported heading styles; Word fills them in when you open the document. See [Exporting](Exporting.html#headers-and-footers) for the full variable list and differences between DOCX and print/PDF behavior.

## Change Tracking [change-tracking]

CriticMarkup syntax in a Markdown document will be converted
to Word Change Tracking when exported to DOCX. Comments
following insertions, deletions, and substitutions will
appear in the right hand column in Word when change tracking
is enabled.

When importing a DOCX file in Marked, change tracking will
be converted to CriticMarkup and `<mark>` tags as
appropriate.

## Math [math]

MathJax and Katex equations displayed in the document will be converted to MathML for display in Word. This conversion isn't perfect, but in most cases will render a valid math block in the word document. This only applies to export --- math blocks in Word documents will not be converted when importing.

## Adding Custom Export Styles [adding-custom-export-styles]

You can add your own export styles by placing a matching pair of files in `~/Library/Application Support/Marked/Custom Word Styles/`:

- `STYLENAME.xml` — the Word paragraph/character styles (from a document's `word/styles.xml`)
- `STYLENAME.thmx` — an optional Word theme for colors, fonts, and effects

A Word **theme** (`.thmx`) does **not** store the paragraph styles you edit in the document. Those live in the document (or a template such as `.dotx` / `Normal.dotm`). Marked needs the extracted `styles.xml` for the style definitions, and the `.thmx` only for theme colors/fonts/effects.

To create a custom export style:

1. Open a Marked-generated DOCX file in Word.
2. Edit the styles you care about: right-click a style in the Styles gallery or Styles pane and choose **Modify…** (there is no separate “Style editor”). Apply your fonts, spacing, and other formatting, then save the DOCX.
3. Optionally capture theme colors/fonts/effects: open the **Design** tab, open the Themes gallery, and choose **Save Current Theme…**. Save it as `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, using the name you want in Marked’s style menu.
4. In Finder, duplicate the saved DOCX, rename the copy to `FILENAME.zip`, and expand it.
5. Inside the unzipped package, copy `word/styles.xml` to `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.xml` (same base name as the `.thmx`, if you created one).

The next time you export a DOCX from Marked, your style appears in the Style menu of the Save dialog.