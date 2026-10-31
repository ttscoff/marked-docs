# <%= @title %>

Mind maps and outlines can be embedded in your Markdown preview using [Marked's include syntax][include] or the [IA Writer block syntax][ia]. Behavior depends on the file format and the per-format checkboxes under **Embed as Mermaid mind maps:** in {% prefspane Apps %} (*Mind Maps and Outlines*).

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## Supported Formats [supported-formats]

### iThoughts X (.itmz) [ithoughts-x-itmz]

iThoughts mind map files are zip archives containing map data and an optional preview image.

### MindManager (.mmap) [mindmanager-mmap]

MindManager files are zip archives containing `Document.xml`. Unzipped MindManager packages (a folder containing `Document.xml`) and direct paths to `Document.xml` are also supported.

### FreeMind (.mm) [freemind-mm]

FreeMind mind map files use the `.mm` extension and store data as XML. Marked detects FreeMind format by checking that the file content starts with `<map`; if not (e.g., a code snippet), the file is included as plain text. FreeMind files are supported for Mermaid mind map embedding.

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) is an XML format for hierarchical outlines, widely used by outliners and feed readers. iThoughts and other apps can export to OPML. Marked converts included OPML files to Mermaid mind map diagrams.

### Bike (.bike) [bike-bike]

See [Bike](Bike.html) for opening a `.bike` file. Included Bike outlines follow the **Bike outlines** checkbox: on renders a Mermaid mind map (the file name, without `.bike`, is the root node); off renders a nested Markdown list with no document title.

### OmniOutliner (.ooutline) [omnioutliner-ooutline]

OmniOutliner outlines can be included the same way. The **OmniOutliner outlines** checkbox under **Embed as Mermaid mind maps:** controls Mermaid vs Markdown list rendering. Opening an OmniOutliner file is covered in [OmniOutliner and OPML](OmniOutliner_and_OPML.html).

### Tree Outliner (.treeoutline) [tree-outliner-treeoutline]

See [Tree Outliner](Tree_Outliner.html). The **Tree Outliner outlines** checkbox controls both opening a `.treeoutline` file and including one. On renders a Mermaid mind map rooted at the document title. Off compiles headings and lists, using **Headings through level** in the *Tree Outliner* group.

## Embed as Mermaid mind maps [embed-as-mermaid-mind-maps]

In {% prefspane Apps %}, under *Mind Maps and Outlines*, the group **Embed as Mermaid mind maps:** has one checkbox per format:

- **Bike outlines**
- **Mind maps (iThoughts)** (also covers FreeMind and MindManager)
- **OPML files**
- **OmniOutliner outlines**
- **Tree Outliner outlines**

When a format's checkbox is **enabled** (the default for supported formats), Marked converts included files of that type to [Mermaid](https://mermaid.js.org/) diagrams:

**iThoughts, MindManager, FreeMind, OPML, Bike, OmniOutliner, and Tree Outliner** — Rendered as Mermaid mindmap diagrams with the tidy-tree layout. For iThoughts and MindManager, shape information (rounded, rectangle, hexagon, etc.) is preserved where available. FreeMind (`.mm`) and OPML use the same mind map format. Bike (`.bike`) outlines use the included filename (minus extension) as the mind map root node. Tree Outliner uses the document title as the root. Node labels are plain text (links become link text; tasks show as ☐ / ☑ prefixes). Mermaid is included by default in every Markdown preview.

**Limitation:** Mind map embedding (Mermaid diagrams) does not work with the Discount parser. Use MultiMarkdown, CommonMark (GFM), or Kramdown for mind map previews.

When a format's checkbox is **disabled**:

- **iThoughts** — The built-in preview image (`preview.png`) from the .itmz file is embedded as a base64 image. The image alt text uses the filename.
- **MindManager** — The outline is embedded as a nested Markdown list.
- **FreeMind** — The outline is embedded as a nested Markdown list.
- **OPML** — The outline is embedded as a nested Markdown list (no mind map).
- **Bike** — The outline is embedded as a nested Markdown list (no document title). Heading rows are bold, and tasks become GitHub checkboxes. See [Bike](Bike.html).
- **OmniOutliner** — The outline is embedded as a nested Markdown list/checklist.
- **Tree Outliner** — The outline is compiled to Markdown headings and lists. The document title is heading 1, and **Headings through level** sets how deep headings go. See [Tree Outliner](Tree_Outliner.html).

## Include Syntax [include-syntax]

Use the same syntax as for other file includes:

	<<[path/to/map.itmz]
	<<[path/to/map.mmap]
	<<[path/to/map.mm]
	<<[path/to/outline.opml]
	<<[path/to/outline.bike]
	<<[path/to/outline.treeoutline]

Or with iA Writer block syntax:

	/path/to/map.itmz

Paths can be relative to the main document or absolute (starting with `/` or `~`). See [Multi-File Documents](Multi-File_Documents.html) for details.

## OPML Conversion [opml-conversion]

OPML files use nested `<outline>` elements with a `text` attribute. When **OPML files** is enabled under **Embed as Mermaid mind maps:** (see [Settings: Apps](Settings_Apps.html)), conversion produces a Mermaid mind map using the same format as iThoughts and MindManager:

- Child outlines of `<body>` become the top level (or children of an "Outline" root if there are multiple top-level items)
- Nested outlines define the hierarchy
- Missing or empty `text` is shown as `(unnamed)`
- Text is sanitized; special characters are escaped for Mermaid

## Bike Conversion [bike-conversion]

Bike `.bike` files are HTML with a root `<ul>` and `<li>` items. In list mode, every row is a list item: `data-type="heading"` rows are bold, and `data-type="task"` rows are GitHub checkboxes (completed when `data-done` has a timestamp, or `data-checked` / `data-completed` is true). Inline formatting and links in node text are converted to Markdown. Opening a `.bike` file always uses this list. When an included file is embedded as a Mermaid mind map, the file name (minus extension) is the single root node and labels are plain text formatted for Mermaid mindmap syntax.
