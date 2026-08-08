# <%= @title %>

[Visual Studio Code][vscode] does not include Marked out of the box, but you can use a community extension for **live Markdown preview** in Marked --- preview, export, and proofing while you keep writing in VS Code.

## Quick start [quick-start]

1. Install a VS Code **Open in Marked** extension (see [Open in Marked extension][ext] below).
2. Open your Markdown file in VS Code.
3. Send the file to Marked --- the preview updates when you save.

## Open in Marked extension [open-in-marked-extension]

The [Open in Marked extension][ext] (Visual Studio Marketplace) adds an **Open in Marked** action: editor title button, **{% kbd shift cmd m %}**, context menus in the editor and file explorer, optional **open folder** for Marked's file browser, a status bar indicator, and optional auto-save before opening. Settings let you set the path to the Marked app if it is not in the default location.

I> The extension was originally published for Marked 2. Marked 3 uses the same style of file and URL handoff, so this integration continues to work; if anything changes, check the [extension page][ext] or the author's repository for updates.

## Requirements [requirements]

Marked runs only on macOS. Install [Marked 3][marked] and the extension, then point **app path** at your Marked app if needed.

[ext]: https://marketplace.visualstudio.com/items?itemName=vikgamov.vscode-open-in-marked2
[marked]: https://markedapp.com/
[vscode]: https://code.visualstudio.com/
