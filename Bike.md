# <%= @title %>

Drag a [Bike][bike] outline (`.bike`) onto Marked to preview it as a nested Markdown list, with heading rows in bold and tasks as checkboxes.

## Opening a Bike outline [opening-a-bike-outline]

Marked converts the outline when you open the file:

- Rows marked as headings become **bold** list items.
- Tasks become GitHub-style checkboxes. A task is checked when Bike stores a completion time or marks it checked.
- Links and inline formatting in row text are kept as Markdown.

Opening a `.bike` file always uses this list. It does not turn the outline into a Mermaid diagram.

## Including a Bike outline [including-a-bike-outline]

A `.bike` file can also be included in another Markdown document. See [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

In {% prefspane Apps %}, under *Mind Maps and Outlines*, **Bike outlines** applies to included files:

- **On** (the default) — a Mermaid diagram. The file name, without `.bike`, is the root node.
- **Off** — the same nested Markdown list used when you open the file, with no document title.

Mermaid diagrams need MultiMarkdown, CommonMark (GFM), or Kramdown. They do not render with the Discount processor.

[bike]: https://www.hogbaysoftware.com/bike/
