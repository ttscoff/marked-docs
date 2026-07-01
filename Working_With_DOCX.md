# <%= @title %>

Marked has extensive support for working with Microsoft Word files. The typical workflow is **preview first, export DOCX second**: open or watch your Markdown in Marked, refine styles and proofreading in the live preview, then export to Word when the document is ready.

## Opening DOCX files

Marked can read a DOCX file and convert it to clean
Markdown. Valid style elements like headlines and lists will
be converted to their Markdown equivalent.

Change tracking and comments  will be converted to
CriticMarkup. Highlights will be converted to `<mark>` tags,
with colors where appropriate.

## Exporting DOCX files

Use the Export palette to generate a DOCX file from your
Markdown. In the save dialog you can specify a built-in
styles --- this style can easily be changed in Word just by
opening the theme selector and selecting a new theme.

### Headers and footers

If you configure headers and footers in {% prefspane Export %}, they are included in the exported DOCX. Standard placeholders such as `%title`, `%date`, `%page`, and `%total` are substituted at export time. `%logo` and `%image` embed the logo from Header/Footer preferences. `%md_*` metadata variables resolve from the document's MultiMarkdown metadata. `%h1`--`%h6` become Word **STYLEREF** fields tied to the exported heading styles; Word fills them in when you open the document. See [Exporting](Exporting.html#headers-and-footers) for the full variable list and differences between DOCX and print/PDF behavior.

## Change Tracking

CriticMarkup syntax in a Markdown document will be converted
to Word Change Tracking when exported to DOCX. Comments
following insertions, deletions, and substitutions will
appear in the right hand column in Word when change tracking
is enabled.

When importing a DOCX file in Marked, change tracking will
be converted to CriticMarkup and `<mark>` tags as
appropriate.

## Math

MathJax and Katex equations displayed in the document will be converted to MathML for display in Word. This conversion isn't perfect, but in most cases will render a valid math block in the word document. This only applies to export --- math blocks in Word documents will not be converted when importing.

## Adding Custom Export Styles

You can add your own export styles by including a template and a styles.xml file in `~/Library/Application Support/Marked/Custom Word Styles/`. To create these:

1. Open a Marked-generated DOCX file in Word
2. Edit the styles there in the Style editor for each element, selecting "Add to template" for each one.
3. Save the DOCX file.
4. Generate a template by going to **Design** in the top bar, and from the *Template* dropdown on the left, click **Save current template**. Name it as you want it to appear in the Marked style menu and save it to `~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx`, where `STYLENAME` is the name of your style.
5. Go to Finder and locate the DOCX file you saved from Word. Duplicate it and rename the copy to `FILENAME.zip` and double click it to unzip.
6. In the unzipped document, you'll see a "word" folder containing a styles.xml file. Copy that styles.xml file to the same folder as above, and name it `STYLENAME.xml` (where `STYLENAME` is the name of your style). The `.thmx` and `.xml` files should have the same base name (just different extensions).

The next time you export a DOCX from Marked, you'll see your new style in the Style menu of the Save dialog.