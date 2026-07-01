# <%= @title %>

## Callouts

## Bear/Obsidian ##

Marked supports callouts with the syntax used by Obsidian and Bear, which is a specially formatted block quote:

	> [!NOTE] Note title
	> Additional text

The "NOTE" in `[!NOTE]` is case-insensitive. It can be any of:

- NOTE
- ABSTRACT, SUMMARY, TLDR
- INFO
- TODO
- TIP, HINT, IMPORTANT
- SUCCESS, CHECK, DONE
- QUESTION, HELP, FAQ
- WARNING, CAUTION, ATTENTION
- FAILURE, FAIL, MISSING
- DANGER, ERROR
- BUG
- EXAMPLE
- QUOTE, CITE

These will create specially-formatted blocks.

You can use a `+` or `-` to make the callout collapsible. A plus sign (`+`) means the callout is collapsible but defaults to open. A minus sign (`-`) means the callout is collapsible but defaults to closed.

  ![Callouts in Marked][callouts]

[callouts]: images/callouts-800.jpg @2x width=800

### Xcode Playground ###

When previewing Xcode Playground files, Marked supports the native Xcode Playground callout syntax:

	- Attention: Optional title
	Callout content goes here.

The callout type (e.g., "Attention") is case-insensitive and can be any of the following Xcode Playground callout types:

- **Attention** - Styled as info callout
- **Author** - Metadata callout
- **Authors** - Metadata callout
- **Bug** - Error/danger callout
- **Complexity** - Note-style callout
- **Copyright** - Metadata callout
- **Custom Callout** - Example-style callout
- **Date** - Metadata callout
- **Example** - Example callout
- **Experiment** - Tip-style callout
- **Important** - Info-style callout
- **Invariant** - Note-style callout
- **Note** - Note callout
- **Precondition** - Note-style callout
- **Postcondition** - Note-style callout
- **Remark** - Note-style callout
- **Requires** - Note-style callout
- **See Also** - Info-style callout
- **Since** - Metadata callout
- **Version** - Metadata callout
- **Warning** - Warning callout

The optional title after the colon will be used as the callout title. If no title is provided, the callout type name will be used as the title.

The callout content immediately follows on the next line (no blank line required). Content continues until a blank line, the next callout, a fenced code block, or the end of the document.

Example:

````markdown
- Important: Performance Note
This algorithm has O(n log n) complexity.

- Example: Quick Sort
Here's how to implement it:

```swift
func quickSort(_ array: [Int]) -> [Int] {
   // implementation
}
```
````

You can also omit the title entirely:

	- Warning
	This is a warning without a custom title.

These callouts are automatically converted to Marked's callout format and styled appropriately. The original callout type is preserved in the `data-callout` attribute, allowing for custom CSS styling if desired.

> This feature only works when previewing Xcode Playground files (`.playground`). Regular markdown files will not process this syntax.


## Table of Contents

You can specify where in the document the Table of Contents should appear using `<!--TOC-->`. If this is set, it overrides the option in Preferences and will always show in the preview window as well as when saving and printing. The Table of Contents will display only once, even if there are multiple `<!--TOC-->` specifiers in the content.

If you add `max#` to the above tag (where # is a digit from 1-5) it will control the depth of the displayed Table of Contents. For example `<!--TOC max2-->` will only display first and second-level headers in the list. You can also specify a minimum header level with `<!--TOC min2-->`. Maximums and minimums are based on actual headline levels, not nesting levels. Maximum and minimum can be used together.

Marked also recognizes MultiMarkdown-style `{{TOC}}`, and Pandoc-style `{{TOC:2-6}}`, where `2-6` is the range of minimum and maximum levels of headers to include.

By default, the Table of Contents will print on the first page of the document if "Print Table of Contents" is enabled under the {% prefspane Export %}. If a marker exists in the document it will be placed at that point instead.

I> You can specify the type of numbering or lettering of each level of a nested Table of Contents hierarchy in the {% prefspane Export %}.

## Page breaks

You can force a page break for print/PDF output by using the syntax:

```html
<!--BREAK-->
```

Put the token on a line by itself and it will generate markup that will force a new page at that point. Marked also understands the Leanpub format:

	{::pagebreak /}

## Autoscroll pauses [pauses]

Marked can function as a Teleprompter using the [Autoscroll](Autoscroll.html) feature (you should add the [Teleprompter style](https://markedapp.com/styles/preview?style=teleprompter)). When doing so, it may be useful to include pauses in the document. Do this using:

```html
<!--PAUSE:X-->
```

Where `X` is the number of seconds for which Marked should pause. So inserting `<!--PAUSE:15-->` would give you a 15-second pause when that point in the document reaches the middle of the screen.

## File includes

The contents of additional files can be inserted by using the syntax:

	<<[folder/filename]

The path to the file can be relative to the index file or absolute. Includes can be nested; you can use this same syntax inside of an included file. If you're using relative paths, includes in nested files should be relative to that file. ***However,*** MultiMarkdown will process everything based on the location of the first file opened, so all image paths or other embeds should be relative to the first parent file, even when they exist in child documents.

MultiMarkdown metadata and YAML headers are automatically stripped from included files before rendering. This will prevent the headers from showing up in the document, but be aware that metadata such as "base header level" will be ignored in included documents.

T> Note that when viewing documents with included files, you can type "I" (shift-i) to see which included file is in the visible area.

See ["Multi-File Documents"][ext] for more information.

[ext]: Multi-File_Documents.html

## Including code

Marked can include external files as code using a syntax similar to file includes above:

	<<(folder/filename)

Note the parenthesis instead of square brackets. For compatibility with Leanpub syntax, Marked will also recognize a preceding set of square brackets containing a title, but right now nothing is done with it in Marked:

	<<[Code title](folder/filename)

The contents of the specified file will be inserted within a pre>code block in your document and will be available for automatic syntax highlighting if it's enabled. Code blocks can not be nested and will not be processed with MultiMarkdown. Custom processors will still be run over the pre>code block created.

## Including unprocessed text or html

E> **Note:** This feature is for advanced users.

If you want to include raw HTML or other text that should not be processed by MultiMarkdown (or your custom processor), you can use curly brackets (`{}`) to include a file *after* processing the rest of the document:

	<<{folder/raw_file.html}

No include syntax will be recognized within these files (no nesting) and the **raw** contents of the file will be inserted in the final HTML output. This is great for inserting HTML without bogging down the text processor or having things converted/escaped when you don't want them to be, but be careful as there are few safeguards to ensure formatting of the document is preserved around what you insert.
