# <%= @title %>

Marked includes native **Shortcuts** actions (App Intents) for opening files, changing preview styles, and exporting documents. These actions appear in the Shortcuts app when you search for **Marked** and are available on **macOS 13 (Ventura)** or later.

For script-based automation with a full object model, see [AppleScript Support](AppleScript_Support.html). For URL-based workflows from the shell, see the [URL Handler](URL_Handler.html).

## Finding actions

1. Open the **Shortcuts** app.
2. Create a new shortcut or edit an existing one.
3. Search the action library for **Marked**.

Actions are grouped under **Documents** and **Export**. Marked also registers Siri phrases such as "Export file with Marked" and "Open in Marked" for quick shortcuts.

## Actions overview

| Action | Purpose |
| --- | --- |
| **Open File in Marked** | Open a Markdown or text file in a preview window. |
| **Set Preview Style** | Change the preview theme for an open document (or open a file first). |
| **Open and Export File** | Open a file, then export it to another format. |
| **Export Document** | Export an open document (front window or a specific file). |
| **Export Open Documents** | Export every document currently open in Marked. |

All export actions return the exported file (or files) as Shortcuts **File** output so you can pass them to the next step (Mail, Finder, another app).

## Open File in Marked

**Parameter:** **File** -- the document to open (from Finder, Share Sheet, or a previous Shortcuts step).

Marked opens the file in a preview window. Use this when you want to preview or edit in Marked before doing anything else.

## Set Preview Style

**Parameters:**

- **Style** -- preview style from a picker (same names as the preview style menu and Style Manager).
- **File** (optional) -- a specific file. If omitted, Marked uses the front document. If the file is not already open, Marked opens it first.

Setting a style reloads the preview with that theme (same as choosing a style from the preview style menu).

## Export actions

Export actions share the same core options:

| Parameter | Description |
| --- | --- |
| **Format** | Markdown, HTML, Paginated PDF, Continuous PDF, EPUB, DOCX, ODT, RTF, RTFD, TextBundle, TextPack, or OPML. |
| **Profile** (optional) | A saved export profile from {% prefspane Export %}. |
| **Style** (optional) | Preview style to apply before export (full preview reload). |
| **Page Size** (optional) | Print page size name, such as `A4` or `Letter`. |
| **Margins** (optional) | Margin shorthand (see below). |
| **Font Size** (optional) | Base font size in points for PDF export, such as `14` or `12pt`. |
| **Output File** / **Output Folder** (optional) | Destination path. If omitted, Marked writes beside the source file using the correct extension. |

**Notes**

- **Paginated PDF** uses the same print-layout pipeline as {% appmenu File, Export, Paginated PDF %}. It is not available for raw HTML preview documents.
- **HTML** export uses the rendered preview (what you see in the WebView), not the raw Markdown source file.
- **Continuous PDF** captures the current preview WebView layout.
- **Font Size** enables the same custom export/print font size option from {% prefspane Export %}. It does not affect Fountain documents.

### Open and Export File

Best for Finder workflows: pick a Markdown file, open it in Marked, and export in one step.

**Parameters:** **File** (required), plus the export options above.

Example use: a Quick Action that takes files from Finder and exports **Paginated PDF** with a chosen profile and style.

### Export Document

Export a document that is **already open** in Marked.

**Parameters:**

- **File** (optional) -- a specific open file. If omitted, Marked exports the front document.
- Export options and **Output File** as above.

Use this when Marked is already running and you want to export the current preview without reopening the file.

### Export Open Documents

Export **every** preview document currently open in Marked.

**Parameters:**

- **Format** and export options (profile, style, page size, margins, font size).
- **Output Folder** (optional) -- directory for exported files. If omitted, each file is exported beside its source document.

Useful for batch export after reviewing multiple chapters or notes in Marked.

## Margin shorthand

When **Margins** is set on an export action, use a string with one to four measurements. Units: `in`, `cm`, `mm`, `pt`, or `"` for inches. A number without a unit is treated as points.

| Value | Meaning |
| --- | --- |
| `1in` | All sides |
| `1in 2in` | Top and bottom `1in`, left and right `2in` |
| `1in 2in 1in` | Top `1in`, left and right `2in`, bottom `1in` |
| `1in 2in 1in 2in` | Top, right, bottom, left |

This matches the `margins` key in [AppleScript](AppleScript_Support.html#with-options-properties-record) export records.

## Example workflows

### Finder file to PDF

1. **Open and Export File**
2. **File** -- input from Share Sheet or Finder Quick Action.
3. **Format** -- Paginated PDF.
4. **Style** -- optional theme (for example Amblin).
5. **Profile** -- optional saved export profile.
6. **Output File** -- optional; leave empty to write `filename.pdf` next to the source.

### Export what is open in Marked

1. **Export Document**
2. Leave **File** empty to use the front window.
3. Choose **Format** and optional profile or style.

### Batch export open documents

1. **Export Open Documents**
2. Choose **Format** (for example EPUB).
3. Optionally set **Output Folder** to collect all exports in one directory.

### Style then export (two steps)

1. **Set Preview Style** -- pick a style (optionally target a specific **File**).
2. **Export Document** -- same file or front document, with desired **Format**.

You can also pass **Style** directly on an export action; Marked applies the theme and waits for the preview reload before exporting.

## Export paths and sandboxing

- If **Output File** or **Output Folder** is omitted, Marked writes beside the source document.
- Marked can create intermediate folders when the export path is **inside the folder of the open document**.
- Exports outside the document's folder require a writable path Marked can access (saved document location, security-scoped bookmarks, or folders you have granted via Open dialogs).

See [AppleScript Support](AppleScript_Support.html#export-paths-and-sandboxing) for the same sandbox rules.

## Legacy `convert_to` action

The AppleScript dictionary still exposes **`convert_to`** for converting Markdown text or files without an open preview. Native Shortcuts actions above are preferred: they open documents properly, wait for preview load, and support paginated PDF export asynchronously.

See [Shortcuts and `convert_to` in AppleScript Support](AppleScript_Support.html#shortcuts-and-convert_to) for details on the legacy command.

## Troubleshooting: actions not appearing in Shortcuts

Shortcuts indexes **one** Marked install per bundle identifier (`com.brettterpstra.marked`). It prefers the copy with the **highest build number** (`CFBundleVersion`), not necessarily the app you just built in Xcode.

If Marked does not appear under **Apps** in the Shortcuts action library:

1. List every copy on disk:
   ```bash
   mdfind 'kMDItemCFBundleIdentifier == "com.brettterpstra.marked"'
   ```
2. Remove or rename stale copies (for example an old `Marked.app` on the Desktop or in `/Applications` that was copied from a build **without** Shortcuts metadata).
3. Run the build you want Shortcuts to use (Xcode **Run**, or open the `.app` in DerivedData directly).
4. Quit and reopen the **Shortcuts** app.

A build that includes Shortcuts contains `Contents/Resources/Metadata.appintents`. You can verify:

```bash
ls "/path/to/Marked.app/Contents/Resources/Metadata.appintents"
```

On launch, Marked logs `[MKShortcuts] Registering App Intents` in Console.app when registration runs (macOS 13+).

## Debugging

Enable **Debug mode** in {% prefspane Advanced %}. Marked logs export steps at Info level with the prefix `[AppleScript]` in Console.app and Marked's log viewer (the export pipeline is shared with AppleScript).

## Errors

Common messages when an action fails:

- No Marked document is available (nothing open and no file specified).
- That file is not open in Marked (use **Open File** or **Open and Export File**).
- Unknown export profile or preview style name.
- Timed out waiting for preview to load or reload.
- Export path permission errors or paginated PDF generation failure.
