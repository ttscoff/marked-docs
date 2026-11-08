# <%= @title %>

Drag a [Bike][bike] outline onto Marked to preview it as a nested Markdown list, with heading rows in bold and tasks as checkboxes. A single outline is a `.bike` file. Bike 2 saves a `.biked` package when the outline contains embedded images.

## Opening a Bike outline [opening-a-bike-outline]

Marked converts the outline when you open the file:

- Rows marked as headings become **bold** list items.
- Tasks become GitHub-style checkboxes. A task is checked when Bike stores a completion time or marks it checked.
- Links and inline formatting in row text are kept as Markdown.

Opening a `.bike` file always uses this list. It does not turn the outline into a Mermaid diagram. A `.biked` package follows the **Bike outlines** setting below.

## Including a Bike outline [including-a-bike-outline]

A `.bike` file can also be included in another Markdown document. See [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

In {% prefspane Apps %}, under *Mind Maps and Outlines*, **Bike outlines** applies to included files:

- **On** (the default) — a Mermaid diagram. The file name, without `.bike`, is the root node.
- **Off** — the same nested Markdown list used when you open the file, with no document title.

## Outlines with images [outlines-with-images]

Bike 2 saves a `.biked` package when the outline contains embedded images. The package is a TextBundle: `text.bike` plus an assets folder. Open the `.biked` file itself. Marked reads the outline inside and titles the window with the package name.

Turn **Bike outlines** off to preview that package as the nested list, which keeps the embedded images. **On** turns the outline into a Mermaid diagram.

[bike]: https://www.hogbaysoftware.com/bike/
