# <%= @title %>

Marked gives you options.

## Live preview workflow [live-preview-workflow]

1. Drag a Markdown file onto Marked (or use {% appmenu File, Open... ({{cmd}}O) %}).
2. Edit the file in your preferred editor.
3. Save --- Marked updates the preview automatically.

See [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html) for vault watching, streaming preview, and editor-specific guides.

## Drag to Dock Icon [drag-to-dock-icon]

The easiest way to use Marked on a file you're already editing is to drag the document icon from the toolbar of your editor or from Finder to the Marked icon in your Dock. Marked will immediately start tracking any Markdown file (or text file) dropped on it. You can also drag files directly from the Finder.

## Using the Menu [using-the-menu]

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

You can, of course, open Markdown files directly using the {% appmenu File, Open... ({{cmd}}O) %} menu option. Marked works fine _without_ a text editor, too. You can preview and convert your Markdown with just a click.

Marked can also open **`.rtf` and `.rtfd`** files directly (for example exports from Pages or TextEdit). They are converted to Markdown for preview and update when you save in the original app. See [RTF and RTFD Support](RTF_Support.html) for details, including images and limitations.

Marked can open **`.pdf`** files the same way: conversion runs in the background, then the preview updates when finished. This works best for shorter, text-based PDFs; large manuals and scanned documents are slower and less accurate. See [PDF Support](PDF_Support.html) for details and limitations.

## From the Clipboard [from-the-clipboard]

If you have compatible (e.g. Markdown) text in your clipboard, you can open an instant preview by selecting {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. If you copied a selection from a web browser or other app that put HTML or RTF on the clipboard, Marked converts it to Markdown for preview. When you paste RTF from an app like TextEdit or Pages, larger font sizes are roughly converted to heading levels (e.g. very large text becomes a level 1 heading, smaller large text becomes level 2, and so on). You can have multiple clipboard previews open at once, and you can save them to a new file by choosing {% appmenu File, Save Transient Preview %}.

## Creating a New Document [creating-a-new-document]

Marked allows you to create a new, empty text file with the {% appmenu File, New ({{cmd}}N) %} command. It will immediately ask you for a location to save the file, and you can enable the "Edit new files automatically" option in the {% prefspane Apps %}, next to the Text editor button to automatically open the newly-created file in your default editor.

## Open Recent [open-recent]

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked keeps track of recent documents, too. The {% appmenu File, Open Recent %} menu option will show you the files you"ve had open and let you jump back to them. You can quickly re-open the last file you were viewing with {% kbd shift cmd R %}. Use {% kbd shift cmd P %} or [Quick Actions](Quick_Actions.html) to run menu and preview commands from the keyboard. There are a lot of other keyboard shortcuts, too. If you care to learn them, you can find a chart under [Keyboard Shortcuts](Keyboard_Shortcuts.html).

## New View into Current File [multiview]

Use {% appmenu File, New View into Current File %} ({% kbd
shift cmd N %}, also in the preview context menu) to open a
second preview window on the same saved file. Both windows
watch the file on disk and update when you save in your
editor, but each view keeps its own scroll position,
bookmarks, preview style, and [Custom Rule
overrides](Custom_Processor.html#manuallyenabled).

**Example use case:** You are editing a long manuscript in
MultiMarkdown with your usual style and processor. Open a
second view, switch it to a proofing style, pin a Process
rule that runs a different built-in processor, and enable a
manual rule that highlights revision markup. You compare
draft and proof layouts side by side without maintaining two
copies of the file.

When more than one view of a file is open, the window title
includes **View 2**, **View 3**, and so on so you can tell
windows apart in the Window menu and Mission Control.

Alternate views are not available for unsaved documents,
clipboard previews, streaming previews, or folder-based
projects that do not map to a single file on disk.

## Quick Open ## [quick-open]

You can quickly switch between open documents, open recent documents, or open the File->Open dialog with the [Quick Open panel](Quick_Open.html) ({% kbd cmd shift o %}).