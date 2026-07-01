# <%= @title %>

Options in the {% prefspane Export %}:

(See [Exporting](Exporting.html) for more info)

![Settings: Export][1]

[1]: images/screenshots/preferences-Export.jpg @2x width=920px height=1031px class=preferencepane-scroll

### Export Profile

Export Profile
: Select a saved profile from the popup menu. Profiles store a complete set of export preferences for quick switching between workflows (for example, print PDF vs. web HTML). See [Export Profiles](Exporting.html#export-profiles).

New
: Create a new profile from the current settings.

Manage
: Open the profile manager to rename, duplicate, or delete profiles.

### Print/PDF

Disable links/highlights when exporting PDF or Printing
: Removes formatting (underline and color) from links when printing.

Include URL as text annotation
: When printing or exporting PDF, the URL for a link will appear after the linked text.

Replace horizontal rules with page breaks
: Turn horizontal rules in document into page breaks (this will additionally force footnotes onto a new page).

Embed images when copying HTML
: When enabled, copying HTML to the clipboard will scan for local images and Base64 encode them to include as data URLs in the source code.

Print background colors and images
: By default Marked will print/export with a white background. If you want to include background colors and images from custom themes, enable this option.

Prevent orphaned headlines
: This option prevents headlines for the next section from appearing at the bottom of a page without succeeding content.

Exclude first H1
: Ignore the first level-one headline in the document when using H1s as page breaks.

Use first H1 as fallback title
: When using apps like Bear or the streaming preview, this option allows you to override the filename with the content of the first H1 in the document. If metadata for "title" is specified, that will always take precedence.

Add page breaks before
: Use level 1/2 headers as section dividers, always starting them on a new page. Select "Footnotes" to always add a page break before any footnotes in the document.

Indicate page breaks in preview
: Show a light dashed line where breaks are inserted with &lt;!\--BREAK\--&gt; syntax or by checking auto-break options in Export settings.

Custom font size for export/print
: If set, all text will be scaled based on the point setting selected (defaults to a base of 10 points).

Margins
: Define print margins (specified in points) for top, bottom, left, and right.

Print table of contents
: Include automatic table of contents in print/PDF.

Page Break after
: Automatically break to a new page after an inserted Table of Contents.

Table of contents level markers
: Use the dropdowns to set the list item marker for each level of indentation in a table of contents.

### Headers and Footers

Configure font, logo, header/footer fields, date and time formats, first-page inclusion, page numbering offset, and borders. Field placeholders include `%title`, `%logo`, `%page`, `%total`, `%date`, `%time`, `%h1`, `%h2`, and others.

See [Headers and Footers](Exporting.html#headersandfooters) in [Exporting](Exporting.html) for placeholder reference and examples. See [Date and Time Formats](Exporting.html#dateandtimeformats) for `%date` and `%time` format codes.

Include on First Page
: If the option for header and/or footer are unchecked, the first page will not print the specified type.

Date format
: strftime-style format string for `%date` in headers and footers. See [Date and Time Formats](Exporting.html#dateandtimeformats).

Time format
: strftime-style format string for `%time` in headers and footers. See [Date and Time Formats](Exporting.html#dateandtimeformats).

Page numbering offset
: Used to adjust what number the page numbers start at. For example, if you have a table of contents on the first page and want the numbering to start on the second page, set the offset to -1. Page 2 will now be page 1 and the total pages will be adjusted accordingly.

Border
: Print a horizontal line below the header and/or above the footer.

Restore Default Formats
: Reset date and time format strings to Marked's defaults (`%m-%d-%Y` and `%I:%M %p`). See [Date and Time Formats](Exporting.html#dateandtimeformats).
