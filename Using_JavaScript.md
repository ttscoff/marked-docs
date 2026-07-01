# <%= @title %>

Marked uses a lot of JavaScript to provide the features it offers in the preview. For this reason, quite a few complications can arise when scripts are included within the body of the document.

## External scripts

You can include some external scripts using a "CSS Header:" metadata line at the top of your document. These scripts will be inserted not in the header, though, but in the footer after jQuery and Marked's scripts have already loaded. This is ideal in most cases. You may still experience unexpected behavior, as Marked can't compensate for every possible scripting conflict. DOM changes can be especially problematic.

    CSS Header: <script src="file.js"></script>

## Inline includes

There are many applications for having JavaScript appear in the body of a document, such as graph generators or other Canvas tools. Depending on configuration settings and the processor you're using, these are often mangled. The solution is to put your script and extra DOM elements into an external file and use Marked's syntax for ["raw" include files][syntax]. These files are not processed in any way; their contents are added into the file after the rest of the processing is complete.

    Markdown text.

    <<{file.html}

    More Markdown text...

For experimenting with and debugging the JavaScript that runs in Marked's preview, you can attach Safari's Web Inspector to the preview window using the steps in [WebKit Inspector](Writing_Custom_CSS.html#webkitinspector).

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml
