# <%= @title %>

Drag a [Tree Outliner][tree] document (`.treeoutline`) onto Marked to preview it as headings and lists, or as a Mermaid diagram.

## Headings and lists [headings-and-lists]

This is the default. Marked compiles the outline as Markdown:

- The document title is a level 1 heading.
- Outline rows continue as headings through the level set by **Headings through level** in {% prefspane Apps %}, under *Tree Outliner*. The default is **2**, so the first row of the outline is a level 2 heading and deeper rows become a nested list.
- Notes on a row become paragraphs under that heading or list item.

## Mermaid diagram [mermaid-diagram]

In {% prefspane Apps %}, under *Mind Maps and Outlines*, turn on **Tree Outliner outlines** to preview the file as a Mermaid diagram. The document title is the root node. The same switch applies when you open a `.treeoutline` file and when you [include](Embedding_Mind_Maps_and_Outlines.html) one in another document.

**Headings through level** is used only when that switch is off.

Mermaid diagrams need MultiMarkdown, CommonMark (GFM), or Kramdown. They do not render with the Discount processor.

[tree]: https://noteifyapp.com/tree-outliner/
