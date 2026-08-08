# <%= @title %>

## Disable Automatic Header IDs [disable-automatic-header-ids]

Marked includes an option to disable automatic header ID generation. You can find this option in the {% prefspane Processor %}.

## Random Footnote IDs [random-footnote-ids]

In the **Processor** pane, you can check the "Use Random Footnote IDs" to generate random footnote identifiers, which helps avoid conflicts when multiple documents are displayed on one web page. This option is only available when using the MultiMarkdown processor.

## Process Markdown Inside of HTML [process-markdown-inside-of-html]

By default, Markdown syntax inside of HTML block tags is usually ignored by Markdown processors. This option forces Marked to continue processing within block elements. Note that some markup may cause issues.
