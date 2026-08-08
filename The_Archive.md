# <%= @title %>

[The Archive][archive] maintains your notes as files on disk and can mirror the note you are editing straight into Marked's **streaming preview** channel.

## Stream Preview to Marked [stream-preview-to-marked]

1. In Marked, open {% appmenu File, New, Streaming Preview %} (or reuse an existing streaming preview window).
2. Switch to The Archive and choose **Note &#8594; Stream Preview to Marked** so The Archive activates Marked and begins sending the frontmost note text.

Marked updates as you type in The Archive, following the same `mkStreamingPreview` clipboard contract as other integrated apps&#8212;see [Technical details](Streaming_Preview.html#developers) under [Streaming Preview](Streaming_Preview.html).

If previews look out of date, confirm the streaming window is still frontmost in Marked and toggle the Archive menu command once.

[archive]: https://www.zettelkasten.de/the-archive/
