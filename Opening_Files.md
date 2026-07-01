# <%= @title %>

Marked gives you options.

## Live preview workflow

1. Drag a Markdown file onto Marked (or use {% appmenu File, Open... ({{cmd}}O) %}).
2. Edit the file in your preferred editor.
3. Save --- Marked updates the preview automatically.

See [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) for vault watching, streaming preview, and editor-specific guides.

## Drag to Dock Icon

The easiest way to use Marked on a file you're already editing is to drag the document icon from the toolbar of your editor or from Finder to the Marked icon in your Dock. Marked will immediately start tracking any Markdown file (or text file) dropped on it. You can also drag files directly from the Finder.

## Using the Menu

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

You can, of course, open Markdown files directly using the {% appmenu File, Open... ({{cmd}}O) %} menu option. Marked works fine _without_ a text editor, too. You can preview and convert your Markdown with just a click.

Marked can also open **`.rtf` and `.rtfd`** files directly (for example exports from Pages or TextEdit). They are converted to Markdown for preview and update when you save in the original app. See [RTF and RTFD Support](RTF_Support.html) for details, including images and limitations.

Marked can open **`.pdf`** files the same way: conversion runs in the background, then the preview updates when finished. This works best for shorter, text-based PDFs; large manuals and scanned documents are slower and less accurate. See [PDF Support](PDF_Support.html) for details and limitations.

## From the Clipboard

If you have compatible (e.g. Markdown) text in your clipboard, you can open an instant preview by selecting {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. If you copied a selection from a web browser or other app that put HTML or RTF on the clipboard, Marked converts it to Markdown for preview. When you paste RTF from an app like TextEdit or Pages, larger font sizes are roughly converted to heading levels (e.g. very large text becomes a level 1 heading, smaller large text becomes level 2, and so on). You can have multiple clipboard previews open at once, and you can save them to a new file by choosing {% appmenu File, Save Clipboard Preview %}.

## Creating a New Document

Marked allows you to create a new, empty text file with the {% appmenu File, New ({{cmd}}N) %} command. It will immediately ask you for a location to save the file, and you can enable the "Edit new files automatically" option in the {% prefspane Apps %}, next to the Text editor button to automatically open the newly-created file in your default editor.

## Open Recent

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked keeps track of recent documents, too. The {% appmenu File, Open Recent %} menu option will show you the files you"ve had open and let you jump back to them. You can quickly re-open the last file you were viewing with {% kbd shift cmd R %}. Use {% kbd shift cmd P %} or [Quick Actions](Quick_Actions.html) to run menu and preview commands from the keyboard. There are a lot of other keyboard shortcuts, too. If you care to learn them, you can find a chart under [Keyboard Shortcuts](Keyboard_Shortcuts.html).

## Quick Open ##

You can quickly switch between open documents, open recent documents, or open the File->Open dialog with the [Quick Open panel](Quick_Open.html) ({% kbd cmd shift o %}).