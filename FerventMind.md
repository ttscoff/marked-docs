# <%= @title %>

FerventMind maps (`.fvmd`) open in Marked. Marked unzips the package. If `text.md` is inside, that file is the preview. If it is not, Marked builds an outline from `map.xml`.

## Outline from the map [outline-from-the-map]

Topic text becomes headings through level 6. Deeper topics become nested bullets. Notes become the section body. A finished task becomes a checked box, and a partial task shows its percent. Images are the files under `assets/`.

## Display only visible topics [display-only-visible-topics]

**Display only visible topics**, in {% prefspane Apps %} under *FerventMind*, skips topics inside a folded branch when Marked builds that outline. It does not change a `text.md` the app already saved.

## Including a map [including-a-map]

Including a `.fvmd` uses **FerventMind files** under **Embed as Mermaid mind maps:** in {% prefspane Apps %}. On produces a Mermaid diagram of the visible or full tree, matching the checkbox above. Off embeds the map's `preview.png`. See [Embedding Mind Maps and Outlines](Embedding_Mind_Maps_and_Outlines.html).

## Open in Editor [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) launches FerventMind.
