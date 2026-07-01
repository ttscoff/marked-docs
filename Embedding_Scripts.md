# <%= @title %>

There are several ways to embed additional JavaScripts in Marked.

## Including JavaScript Per-Document

You can include scripts in a single document using `<script>` tags in the content itself. This can be useful for libraries like [D3](https://d3js.org/) for data visualizations that you only need in specific documents:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

If you're using MultiMarkdown as your Processor, you can include scripts in the metadata and they'll be inserted in the document. Because Marked outputs "snippet" only, the key `XHTML Header` is not ideal. Instead, use `CSS Header` and the scripts will be inserted at the bottom of the document.

	CSS Header: <script src="file.js"></script>

To make included scripts refresh when the content changes, see [Hooks](#hooks).

## Including JavaScript

You can include your own JavaScript from local files, CDNs, or by pasting raw code. To access this, open {% prefspane Style %} and click the *Custom Rules* button.

Set up a new Custom Rule or add scripts to an existing one. To have scripts added to every file, set the predicate to "filename contains *".

The Actions editor for a Custom Rule has three options for including scripts:

Insert JavaScript File
: Lets you select a local file to insert at the end of the document

Insert JavaScript from URL
: Lets you include a CDN or other remote URL, which will create a `<script>` tag at the end of the document with the URL linked

Insert JavaScript
: Opens a code editor where you can write/paste your own JavaScript code

These scripts will be inserted at the end of the preview, before the document tag. If you need to call an init function or update every time the preview updates, see [Including Raw JavaScript](#rawjs), and familiarize yourself with Marked's [hooks](#hooks).

## Mermaid and Other Scripts {#mermaid}

jQuery is included by default, and you can use it in any scripts you add to Marked using any of the below methods.

[Mermaid](https://mermaid.js.org/intro/) for Markdown-like diagramming is now included by default in every document. Any fenced code block with the `mermaid` language will be automatically rendered as a diagram.

At the bottom of the {% prefspane Style %}, a checkbox for "Pan and zoom diagrams" is available when Mermaid content is present. Checking this box will cause diagrams to zoom with {% kbd cmd %}-scroll, and pan by clicking and dragging. The script for this feature is included from a CDN and requires an internet connection.

If there's a particular library you'd like to see included by default, please let me know on the [BrettTerpstra.com forum](https://forum.brettterpstra.com/) or via [the support site](https://support.markedapp.com/questions/add).

## Hooks [hooks]

As of recent versions, Marked no longer performs a full page refresh when updating content, but rather injects the new content into the DOM without requiring a page load. This means that scripts that were included that trigger on page load won't be re-triggered when content is updated. Marked provides a "hooks" feature to accommodate this. To register a hook, you need to include a second script block calling the [`Marked.hooks.register()` function](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor), which accepts a trigger, in this case 'update', and a function to execute.

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

All of Marked's [API functionality](https://markedapp.com/jsapi/) can be used in this field. (You can also use the API in any loaded scripts.) For interactive debugging and experimentation with the API in a live preview, see the [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) section for details on using Safari's Develop menu with Marked.

Now, whenever an update is performed (whenever the watched source file is saved), the passed function will be executed. As long as the script you're running has an init or render function of some kind, you can call it with a hook and have it render every time your document saves and an update is triggered.



*[CDN]: Content Distribution Network