# <%= @title %>

FerventMind maps (`.fvmd`) open in Marked. Marked unzips the package and previews the `text.md` FerventMind saved.

## Markdown in the map [markdown-in-the-map]

How that Markdown is written is set in FerventMind, under **Settings > Files And Export**, in the **Markdown** group. Marked shows the saved file as it is.

![FerventMind Files And Export][fm-export]

**Headings** sets how many levels stay headings. **Visible topics only** skips topics inside a folded branch. **Notes** and **Task checkboxes** control whether notes and tasks are written into that Markdown. These choices apply to Markdown export, Copy As, and the Markdown copy stored in every map for apps such as Marked. A map can override them under **Definitions • MAP**.

If an older map has no `text.md`, Marked builds an outline from `map.xml`: the title is heading 1, the next level is heading 2, and deeper topics become nested bullets. Notes become the section body. A finished task becomes a checked box, and a partial task shows its percent. Images are the files under `assets/`, without a filename caption.

## Including a map [including-a-map]

Including a `.fvmd` uses **FerventMind files** under **Embed as Mermaid mind maps:** in {% prefspane Apps %}. On produces a Mermaid diagram from the map. Off embeds the map's `preview.png`. See [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

## Open in Editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) launches FerventMind.

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
