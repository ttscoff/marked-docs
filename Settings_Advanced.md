# <%= @title %>

Options in the {% prefspane Advanced %}:

![Settings: Advanced][1]

[1]: images/screenshots/preferences-Advanced.jpg @2x width=689px height=1031px class=preferencepane-scroll

YAML and Pandoc Metadata
: - __Ignore:__ Leaves it exactly as it exists in the document, useful if your processor or preprocessor actually uses the YAML.
: - __Remove before rendering__: The YAML block is stripped
: - __Treat as MMD metadata:__ Converts the YAML or Pandoc metadata block to the MultiMarkdown format.

Strip MultiMarkdown Metadata headers
: If this is enabled, MultiMarkdown metadata at the top of the document will be removed before rendering.
: This can be useful if you're using a non-MultiMarkdown processor that would otherwise display the metadata in the rendered document. The metadata is still read prior to removal, so Marked-specific syntax will still be recognized.

Cache hosted images
: Marked does not cache images in the preview by default, because it watches those images for changes and updates them instantly. If you're using images that are referenced via a web URL, you can turn on caching of those images to speed up rendering on slower connections.

Analyze readability statistics
: If you prefer not to have [statistics](Document_Statistics.html) calculated, this will disable that processing. This can provide some performance enhancements on very large documents. Character, word, and sentence counts will continue to function.

Use system-wide Find pasteboard
: This option will allow Marked to pick up whatever search term you most recently used in another editor, and anything searched in Marked will become the search in other applications as well. Disabling it makes Marked's search function independently.

Use {% kbd cmd E %} for Find With Selection
: By default, {% kbd cmd E %} opens the default editor. If this option is enabled, then {% kbd cmd E %} will function as it does in most text editing applications, using the selected text for Find, and Open in Editor can be triggered with {% kbd opt cmd E %}.

Debug mode
: Enables debug logging. Use this for your own troubleshooting, and when reporting an issue. Select __Help->Open Debug Log__ to view activity.
: Setting to _All_ will show info messages, warnings, and error messages. You can also set it to show only errors, or errors and warnings.

Settings Backup
: You can back up your Settings to a JSON file that can be used to restore settings or port them to a new machine.