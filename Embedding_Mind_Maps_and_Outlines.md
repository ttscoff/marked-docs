# <%= @title %>

Mind maps and outlines can be embedded in your Markdown preview using [Marked's include syntax][include] or the [IA Writer block syntax][ia]. The behavior depends on the file format and the "Embed maps as Mermaid diagrams" setting in {% prefspane Apps %} under *Mind Maps/Outlines*.

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Supported Formats

### iThoughts X (.itmz)

iThoughts mind map files are zip archives containing map data and an optional preview image.

### MindManager (.mmap)

MindManager files are zip archives containing `Document.xml`. Unzipped MindManager packages (a folder containing `Document.xml`) and direct paths to `Document.xml` are also supported.

### FreeMind (.mm)

FreeMind mind map files use the `.mm` extension and store data as XML. Marked detects FreeMind format by checking that the file content starts with `<map`; if not (e.g., a code snippet), the file is included as plain text. FreeMind files are supported for Mermaid mind map embedding.

### OPML (.opml)

OPML (Outline Processor Markup Language) is an XML format for hierarchical outlines, widely used by outliners and feed readers. iThoughts and other apps can export to OPML. Marked converts included OPML files to Mermaid mind map diagrams.

### Bike (.bike)

Bike.app outlines are stored as proprietary HTML files (`.bike`). You can open a `.bike` file directly in Marked: the document is rendered as Markdown with the filename (minus extension) as the main heading (H1), top-level heading items as H2, nested headings as bold list items, and tasks as GitHub-style checkboxes. When a `.bike` file is included via include syntax, the "Embed as Mermaid diagram" setting for Bike (in Apps → Mind Maps/Outlines) controls whether it becomes a Mermaid mind map (with the filename as the root node) or a nested Markdown list (no H1).

## Embed maps as Mermaid diagrams

When **enabled** (the default), Marked converts included mind maps and outlines to [Mermaid](https://mermaid.js.org/) diagrams:

**iThoughts, MindManager, FreeMind, OPML & Bike** — Rendered as Mermaid mindmap diagrams with the tidy-tree layout. For iThoughts and MindManager, shape information (rounded, rectangle, hexagon, etc.) is preserved where available. FreeMind (`.mm`) and OPML use the same mind map format. Bike (`.bike`) outlines use the included filename (minus extension) as the mind map root node. Node labels are plain text (links become link text; tasks show as ☐ / ☑ prefixes). Mermaid is included by default in every Markdown preview.

**Limitation:** Mind map embedding (Mermaid diagrams) does not work with the Discount parser. Use MultiMarkdown, CommonMark (GFM), or Kramdown for mind map previews.

When **disabled**:

- **iThoughts** — The built-in preview image (`preview.png`) from the .itmz file is embedded as a base64 image. The image alt text uses the filename.
- **MindManager** — The outline is embedded as a nested Markdown list.
- **FreeMind** — The outline is embedded as a nested Markdown list.
- **OPML** — The outline is embedded as a nested Markdown list (no mind map).
- **Bike** — The outline is embedded as a nested Markdown list (no H1); top-level heading items become H2, nested headings are bold, and tasks become GitHub checkboxes.

## Include Syntax

Use the same syntax as for other file includes:

	<<[path/to/map.itmz]
	<<[path/to/map.mmap]
	<<[path/to/map.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]

Or with iA Writer block syntax:

	/path/to/map.itmz

Paths can be relative to the main document or absolute (starting with `/` or `~`). See [Multi-File Documents](Multi-File_Documents.html) for details.

## OPML Conversion

OPML files use nested `<outline>` elements with a `text` attribute. When "Embed as Mermaid diagram" is enabled (see [Settings: Apps](Settings_Apps.html)), conversion produces a Mermaid mind map using the same format as iThoughts and MindManager:

- Child outlines of `<body>` become the top level (or children of an "Outline" root if there are multiple top-level items)
- Nested outlines define the hierarchy
- Missing or empty `text` is shown as `(unnamed)`
- Text is sanitized; special characters are escaped for Mermaid

## Bike Conversion

Bike `.bike` files are HTML with a root `<ul>` and `<li>` items. Items can have `data-type="heading"` (top level → H2 when opened or in list mode; nested → bold) or `data-type="task"` (GitHub checkboxes; completed when `data-done` has a timestamp, or `data-checked` / `data-completed` is true). Inline formatting and links in node text are converted to Markdown. When embedding as a Mermaid mind map, the file name (minus extension) is used as the single root node and labels are plain text formatted for Mermaid mindmap syntax.
