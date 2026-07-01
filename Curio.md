# <%= @title %>

[Curio][curio] is a visual brainstorming and note-taking app that can stream the item you are editing into Marked's **streaming preview** channel.

## Stream Selected to Marked

1. In Marked, choose {% appmenu File, New, Streaming Preview %} so a streaming preview window is ready.
2. In Curio, turn on **View → Stream Selected to Marked**.

When you double-click to edit a figure, note, list, or other item in Curio, its Markdown flows to the streaming preview and updates as you write.

Marked updates in near real time, following the same `mkStreamingPreview` clipboard contract as other integrated apps&#8212;see [Technical details](Streaming_Preview.html#developers) under [Streaming Preview](Streaming_Preview.html).

If previews stop updating, confirm a streaming preview window is open in Marked and toggle **Stream Selected to Marked** once in Curio.

[curio]: https://www.zengobi.com/products/curio/
