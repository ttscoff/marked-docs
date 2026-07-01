# <%= @title %>

Marked will allow certain attributes of a document to be set in MultiMarkdown metadata format (detailed below). You can use these to define characteristics and styles that only affect that document without altering default settings.

Most MultiMarkdown headers are ignored by the preview, but the following are allowed and affect rendering. You can include other metadata to be rendered in the final output, Marked will just ignore keys not listed below. If you save as HTML and do *not* include a template, Marked will render all metadata keys as expected.

## Metadata format

Metadata is entered at the top of the Markdown file or immediately following any YAML headers. They consist of a key, followed by a colon, optional spaces or tabs and the value:

	Example metadata: example key

Multiple metadata entries should be on their own lines, but without any line breaks between them. The last metadata entry needs to be followed by a blank line before the start of the document text.

	First: this is the first metadata entry
	Second: this is the second entry
	Third: the last metadata entry

	# The beginning of the document text

## Marked metadata keys

### Hiding metadata for other processors [hidingmeta]

**Note:** If you're using a custom processor or posting you Markdown directly to a source that doesn't process this metadata, you can still use it by adding HTML comment markers before and after the Metadata. Unlike MultiMarkdown and other processors, Marked will locate these tags anywhere in the document and process/remove them from the output. Thus, the following in the header will provide the results you want in Marked, but not show up elsewhere:

	<!--
	Marked Style: My Custom Style
	Custom Processor: true
	-->

*Just make sure that the metadata key begins at the start of the line with no spaces or tabs, and don't put anything else on the line after the value.*

### Per-document styles

The "Marked Style:" key will set a preview style for the document. The value can be the name of a default style or a name or path for any [Custom Style](Custom_Styles.html) you have defined in the settings. If this key is found and matches a style that Marked knows about, that style will be used for the preview every time the document containing it is loaded.

**Example**

	Marked Style: Upstanding Citizen

### Quotes language

By default, Marked uses English-style quotation marks. You can modify this on a per-document basis with the "Quotes Language:" key. Available languages are:

* dutch
* english
* french
* german
* guillemets
* swedish

**Example**

	Quotes Language: french

	Creates French-language «quotation marks.»

### Base header level

You can set the header level that Marked starts counting from with the "Base Header Level:" key. This should be a number 1-6, and will modify the way that "#" headers are rendered. If you set the header level to 3, then what would normally be a first-level header (h1) is rendered as a third-level header (h3), and subsequent headers in the hierarchy are shifted up by 2.

**Example**

	Base Header Level: 3

	# This headline will render as an h3

	## This headline will be an h4

	Renders as:

	<h3>This headline will render as an h3</h3>

	<h4>This headline will be an h4</h4>

### Custom Processors

As detailed in the [Custom Processor](Custom_Processor.html#preprocessor), you can enable or disable a custom processor and custom preprocessor using metadata:

    Custom Processor: true
    Custom Preprocessor: false

"true" or "false" turn the pre/processor on and off.

The "Processor" value can be set to "multimarkdown" or "discount" to force one or the other of the internal processors to be used. This per-document setting will not change the default setting in {% prefspane Processor %}.

### Print Headers/Footers

You can override settings in {% prefspane Export %} for print headers and footers using the following keys:

	print header left:
	print header center:
	print header right:
	print footer left:
	print footer center:
	print footer right:

These can include [print variables](Exporting.html#headersandfooters) like `%title`, `%page`, `%total`, etc., as well as references to other metadata using `%md_[key without spaces]`.

### Print Margins

Set page margins for Print and paginated PDF output with the `Margins:` key. Values are in points; suffixes like `px`, `pt`, and `em` are ignored. Provide two numbers for vertical and horizontal margins, or four numbers for top, right, bottom, and left:

	Margins: 10 20
	Margins: 10, 20, 10, 20

Metadata margins override {% prefspane Export %} settings and the margin fields in the PDF export panel.

### Inserting JavaScript

This method specifies data that is included in the `<head>` tag of the document. Marked ignores most values for this key, except in full-document output, but will respect scripts included in this manner. Script tags defined here will not be in the header, however, they'll be appended before the closing `</body>` tag. jQuery is already loaded, and you can take advantage of that in any scripts you inject.

**Example**

	XHTML Header: <script>(function($){$('#wrapper').fadeOut();})(jQuery);</script>

		-or-

	XHTML Header: <script src="myfancyscript.js"></script>

