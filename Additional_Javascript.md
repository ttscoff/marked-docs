# <%= @title %>

You can include your own JavaScript from CDNs or by pasting raw code.

## A Note About Marked Conductor

The easiest way to implement custom JavaScript that varies between document types and locations is with the [Marked Conductor][conductor]. It allows you to use a YAML configuration to append scripts using "filters." Check out the [Conductor page][conductor] for details, and see the [sample config][sample config] for examples.

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## Adding JavaScript's from CDNs [cdns]

![][1]

   [1]: images/screenshots/AdditionalJavascript.jpg @2x width=592px height=576px class=center

You can add JavaScript CDN URLs in the "Additional scripts" window, accessible from {% prefspane Style %}. Enter CDN URLs, one per line. Don't include any `<script>` tags, just the URL:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> Note that jQuery is already included in the preview window.

These scripts will be inserted at the end of the preview, before the document tag. If you need to call an init function or update every time the preview does, see [Including Raw JavaScript](#rawjs). To inspect the DOM and debug these scripts in a live Marked preview, you can attach Safari's Web Inspector as described in [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).


### Including Raw JavaScript [rawjs]

In the lower text field of the Additional Scripts window, you can insert raw JavaScript. This will be included within a `<script></script>` pair, so don't include that in the input. This field can contain any JavaScript command you need to initialize an included library, perform DOM alterations, or anything you want to do within a WebKit view. jQuery is already included for DOM manipulation convenience.

These scripts will only run when the window is first loaded. When the Preview updates, it's done in place by replacing parts of the DOM, so scripts that need to act on the updated content should do so using [Hooks](Embedding_Scripts.html#hooks).

Include in the raw JavaScript field a call like this:

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
