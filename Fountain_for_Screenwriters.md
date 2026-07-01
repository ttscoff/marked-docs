# <%= @title %>

[Fountain](http://fountain.io/) is a specialized text markup language that is designed for writing screenplays. Screenwriters who write using Fountain's syntax can use Marked to preview their work. 

Opening any file with a ".fountain" extension will automatically enable Fountain support for the window. A default Fountain stylesheet will be applied for preview and export.

You can force any document to be processed as Markdown by opening the Gear menu in the lower right of the Preview window and selecting **Process as Fountain**.

Section and scene headers will show up in the Table of Contents for quick navigation of your screenplay.

## Scrippets

You can also use "scrippets" in a regular document to have individual sections processed and styled with Fountain. Simply surround your Fountain markup inside of the main document with `[scrippet]` tags:

    [scrippet]
    Your screenplay text...
    [/scrippet]

You can also use standard Marked-style tags:

    <!--SCRIPPET-->
    Your screenplay text...
    <!--/SCRIPPET-->
