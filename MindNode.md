# <%= @title %>

Drag a [MindNode][mn] document onto Marked (or use MindNode's **Open in Marked** / preview command, depending on MindNode version). Marked treats the file like MindNode's Markdown export, so the hierarchy of your map becomes headings and lists in the preview.

## Streaming preview (MindNode 2026.3+) [streaming-preview-mindnode-20263]

I> **MindNode 2026.3** and newer add Marked [streaming preview](Streaming_Preview.html). In MindNode, choose **View → Preview in Marked** to open it; the preview updates live as you change the map.

## MindNode Classic versus MindNode 7+ [mindnode-classic-versus-mindnode-7]

W> The current integration targets **MindNode Classic** bundles. Newer MindNode releases use a different package format; if opening a map fails or Marked shows a **"Please open from MindNode"** sheet, prepare the map from MindNode's **Advanced** menu (often **Open in another application** / Marked), or export a compatible bundle, rather than dragging a raw `.mindnode` package that has not been prepared for preview.

Because the file is prepared by MindNode before Marked reads it, always save in MindNode before expecting an update in Marked.

[mn]: https://mindnode.com/
[mn-beta]: https://testflight.apple.com/join/jSvVBpnt
