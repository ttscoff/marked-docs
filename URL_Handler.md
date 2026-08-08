# <%= @title %>

Marked's URL handler provides additional scripting and workflow capabilities. You can include a url in the notes of another application, for example, that will open a file in Marked when clicked. You can perform several actions, as listed below.

## The URL scheme [the-url-scheme]

Marked's URL scheme is `x-marked`, called with options like `x-marked://open?file=/Users/username/Desktop/report.md`.

You can specifically target Marked 3 by using `x-marked-3` instead of `x-marked`. The methods and parameters are exactly the same as `x-marked`, but only Marked 3 will respond to `x-marked-3`.

## Calling from the command line/scripts [calling-from-the-command-linescripts]

Calling the url handler from the command line or a script can be done using the macOS [`open` command](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/):

	open 'x-marked://open?file=filename.md'
	open 'x-marked://refresh?file=filename.md'

### Calling in the background [calling-in-the-background]

You can call the `open` command with the `-g` flag to perform the result in the background without switching focus. To perform the command in the background and raise the window to the top without stealing focus:

	open -g 'x-marked://open?file=filename.md&raise=true'

## Optional parameters [optional-parameters]

### x-success [x-success]

Any command can provide an **x-success** query parameter. Set this to a url to be called after performing the command. For example: `x-marked://open/?file=filename.md&x-success=ithoughts:`. You can also provide a bundle identifier (such as `com.googlecode.iterm`) to open an application that doesn't have a URL scheme.

### raise [raise]

A **raise** parameter can be passed with any command that accepts a `file` parameter or affects all windows. After the action is performed, the affected window(s) will raise above all other windows (all applications) before returning or executing a callback.

	"x-marked://refresh?file=filename.md&raise=true"

### speedread [speedread]

A **speedread** parameter can be passed with URL handler commands that open a preview document (`open`, `paste`, `preview`, and `stream`). Set `speedread=1` to automatically start Speed Read as soon as the target preview is ready.

Examples:

	x-marked://open?file=/Users/username/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	x-marked://paste?speedread=1

# Available commands [available-commands]

The following commands are available to the `x-marked` URL handler.

## addstyle [addstyle]

Add a new custom style to Marked.

##### Parameters: [parameters]

**css**: URL encoded CSS text to write to a custom style. Required unless passing a **file** parameter.

**file**: Full path (POSIX) to a CSS file to add to Marked. Required unless passing a **css** parameter.

**name**: The name of the style to generate.

With the **css** parameter, this will be used as both the filename when writing to disk, with ".css" added, and the menu item name. It's required for **css** parameter, and optional for **file** (filename will be used as if the name parameter is empty).

	x-marked://addstyle?name=My+new+style&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

If you include a name with the file parameter, the menu item will get that name instead of the filename. If you use the same name again with a different path, the menu item will be updated with the new path rather than adding a second item with the same name.

## defaults [defaults]

Set user Settings. Accepts a list of keys and values as query parameters. Only existing keys will be set. If the preference change requires a refresh, all windows will refresh automatically unless `refresh=0` is passed.

Use 1 for true and 0 for false on boolean values.

##### Parameters: [parameters-2]

**refresh** _(optional)_: if set to 0, automatic refresh of open preview windows is disabled

* Default: 1 (true)

##### Example: [example]

	x-marked://defaults?syntaxHighlight=1&includeMathJax=0

The `defaults` method is mostly designed so that the developer can add links to esoteric features that might not otherwise be available in Settings. There might be some standard options you'd want to toggle when automating, though. Some common Settings you might want to control during automation:

syntaxHighlight
: enable or disable syntax highlighting

includeMathJax
: enable or disable internal MathJax handling

processor
: set to `multimarkdown` or `mmd` to change the processor to MultiMarkdown, `discount` or `gfm` to use the Discount processor

h1IsPageBreak, h2IsPageBreak, breakBeforeFootnotes
: Automatic page breaks in export before header levels 1 and 2, and footnotes.


## dingus [dingus]

Open the Markdown Dingus for testing different Markdown processors.

	x-marked://dingus

##### Parameters: [parameters-3]

**processor** (optional): Specify which processor to select by default. Valid values:

- `multimarkdown` - MultiMarkdown processor
- `commonmark` - CommonMark (GFM) processor
- `discount` or `discount (gfm)` - Discount processor
- `kramdown` - Kramdown processor

Examples:

- `x-marked://dingus?processor=kramdown` - Opens with Kramdown selected
- `x-marked://dingus?processor=commonmark` - Opens with CommonMark (GFM) selected

*Note:* This opens the Markdown Dingus window, which allows you to test and compare different Markdown processors (MultiMarkdown, CommonMark (GFM), Discount, and Kramdown) side by side. Perfect for experimenting with Markdown syntax and understanding processor differences.

## stylestealer / steal [stylestealer-steal]

Open the Style Stealer HUD. Useful when you want to capture CSS from a live page or run a manual content extraction session without launching it through the UI.

	Synonyms: x-marked://stylestealer … , x-marked://steal …

##### Parameters: [parameters-4]

**url** _(optional)_: A URL to pre-populate in the Style Stealer window. If omitted the HUD opens blank.

Examples:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify [importurl-markdownify]

Open the "Import URL" (Content Extractor) window so you can run the Markdownifier pipeline manually. This does **not** perform the extraction automatically — that is handled by the `extract` command below.

	Synonyms: x-marked://importurl … , x-marked://markdownify …

##### Parameters: [parameters-5]

**url** _(optional)_: Prefills the Import URL field. If omitted the window opens with an empty field waiting for you to paste a link.
**html** _(optional, markdownify only)_: When provided on `x-marked://markdownify`, this should be URL-encoded raw HTML. Marked will convert the HTML to Markdown using the same rules as Clipboard Preview and open it in a transient document, as if you had pasted that HTML into a Clipboard Preview window.

Examples:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## do [do]

Run a JavaScript command in a document window. Marked's entire JavaScript API is [documented here](https://markedapp.com/help/jsapi/).

##### Parameters: [parameters-6]

**js** _(required)_: query string containing a JavaScript command

* Accepts path parameters referencing names of files, or "all"
* Paths split by / will search multiple files
* Partial filenames will complete best match

		x-marked://do/filename1/filename2?js=...
		x-marked://do/all?js=...

**file**: query parameter containing comma-separated paths/filenames

	x-marked://do?file=filename1,filename2&js=...

Will operate on frontmost window if a filename is not given (or "all" is not passed)

## help [help]

Open the Marked internal help system, optionally specifying a topic. This is primarily for use internally, but accessible via URL. A url to any given section can be copied by right clicking on the bookmark icon to the right of a headline and selecting __Copy Link__. **Marked 3** in-app help and search use the `x-marked-3` scheme for these links so macOS opens them in Marked 3 when Marked 2 is also installed; the examples below use that form.

##### dingus [dingus-2]

Open the Markdown Dingus for testing different Markdown processors.

	x-marked://dingus

######## Parameters:

**processor** (optional): Specify which processor to select by default. Valid values:

- `multimarkdown` - MultiMarkdown processor
- `commonmark` - CommonMark (GFM) processor
- `discount` or `discount (gfm)` - Discount processor
- `kramdown` - Kramdown processor

Examples:

- `x-marked://dingus?processor=kramdown` - Opens with Kramdown selected
- `x-marked://dingus?processor=commonmark` - Opens with CommonMark (GFM) selected

*Note:* This opens the Markdown Dingus window, which allows you to test and compare different Markdown processors (MultiMarkdown, CommonMark (GFM), Discount, and Kramdown) side by side. Perfect for experimenting with Markdown syntax and understanding processor differences.

##### Parameters: [parameters-7]

**page** _(optional)_: The exact title of an existing page, with optional anchor hash

	x-marked-3://help?page=Document_Statistics

Spaces are replaced with underscores, per the Marked help file naming convention. A colon (:) may be used in place of a hash (#) when specifying an anchor.

The target may be specified by path alone (without query string):

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## extract [extract]

Extract content from a web URL and open it as a new document in Marked.

	x-marked://extract?url=https://example.com

##### Parameters: [parameters-8]

**url** _(required)_: The web URL to extract content from. Must start with `http://` or `https://`

**window** _(optional)_: Name for the window

**id** _(optional)_: Namespace identifier

**base** _(optional)_: Base URL for relative links

**raise** _(optional)_: Set to `true` to raise the window after opening

**manual** _(optional)_: Set to `true` to open the Style Stealer manual extraction window instead of performing automatic extraction.

- When `manual=true`, Marked opens the Style Stealer, pre-fills the URL field (if provided), suppresses any automatic Open dialog, and lets you interactively select and extract styles/content before saving.
- When omitted or `false`, Marked runs the automatic extractor (Markdownifier) and opens the result directly as a new temporary document.

##### Examples: [examples]

	x-marked://extract?url=https://news.ycombinator.com

	x-marked://extract?url=https://github.com&window=GitHub&raise=true

	x-marked://extract?url=https://example.com/article&manual=true

	x-marked://extract?url=https://blog.example.com/post-title

*Note:* This command uses Marked's content extraction service to fetch web pages, extract clean content using Readability, convert to Markdown format, and open the result in a new temporary document. The extracted content includes metadata (title, source URL, date) and is formatted as clean Markdown. Perfect for quickly capturing and editing web content.

## open [open]

Opens the specified document in Marked.

	x-marked://open?file=/Users/username/Desktop/report.md

##### Parameters: [parameters-9]

**file** *(required)*: The full POSIX path to the document to be opened, or a comma-separated list of paths. Commas inside a filename are allowed; Marked only treats a comma as a multi-file separator when it follows a file extension (for example `.md,`) or when the next path starts with `/` or `~`.

**speedread** *(optional)*: Set to `1` to start Speed Read automatically after opening.

`open` also accepts a path whose components will be combined into a single url

	x-marked://open/~/nvALT2.2

If the file path provided doesn't exist or can't be opened, Marked will still come to the forefront. Running without the *file* parameter or with a blank value will simply open Marked.

Marked will also open files if only the path of a file is called on the URL handler, e.g. `x-marked:///Users/username/Desktop/report.md`.

## paste [paste]

Create a new document from the current contents of the clipboard.

	x-marked://paste

##### Parameters: [parameters-10]

**speedread** *(optional)*: Set to `1` to start Speed Read automatically after opening the clipboard preview.

*Note:* This creates a temporary document using the "Preview Clipboard" command. Any text in your clipboard is added to a new, blank document, which is then opened in Marked. If closed without saving, it's discarded.

## preview [preview]

Preview specified text in a new document.

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### Parameters: [parameters-11]

**text** *(required)*: The text to insert into the preview. Percent-encoded text will be unencoded prior to viewing the document.

**speedread** *(optional)*: Set to `1` to start Speed Read automatically after opening the preview text.

## stream [stream]

Open a streaming clipboard preview window.

	x-marked://stream

##### Parameters: [parameters-12]

**speedread** *(optional)*: Set to `1` to start Speed Read automatically after opening the streaming preview.

*Note:* This creates a temporary document using the "Preview Clipboard" command. The passed text is added to a new, blank document, which is then opened in Marked. If closed without saving, it's discarded.

## refresh [refresh]

Refresh a document preview or all open previews.

##### Parameters: [parameters-13]

**file**: query parameter containing comma-separated paths/filenames (files must be currently open in Marked). Calling with no `file` parameter or `?file=all` will refresh all open windows.

The *file* parameter can be partial, Marked will refresh all open windows with a partial match in the *filename* (not the full path). Passing "all" will refresh all windows.

	x-marked://refresh

	x-marked://refresh?file=/Users/username/Desktop/report.md

	x-marked://refresh?file=report.md

If called with no `file` parameter but document paths specified in the url, paths split by / will search multiple files, and partial filenames will complete the best match.

	x-marked://refresh/filename1/filename2

## style [style]

Set the preview style (CSS) for one or more documents.

##### Parameters: [parameters-14]

**css** _(required)_: query string containing the name or path of a style. Styles must be present in Marked's style menu as default or manually-added custom styles.

* Accepts path parameters referencing names of files, or "all"
* Paths split by / will search multiple files
* Partial filenames will complete best match

		x-marked://style/filename1/filename2?css=...
		x-marked://style/all?css=...

**file**: query parameter containing comma-separated paths/filenames

	x-marked://style?file=filename1,filename2&css=...

This method will operate on the frontmost window if a filename is not given (or "all" is not passed).


