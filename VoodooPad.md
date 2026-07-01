# <%= @title %>

[VoodooPad][vp] bundles each page into a single database file. Drag the `.vpdoc` onto Marked to preview whichever page is currently frontmost in VoodooPad; use {% kbd cmd S %} in VoodooPad whenever you need Marked to reload from disk.

Marked watches the document on disk and swaps the preview when you change pages inside VoodooPad.

## Embedded images

When you reference images with Markdown or HTML and the binary lives **inside** the VoodooPad database, Marked can extract it for the preview. Images that are only **aliases** (files dragged in by reference) are not stored in the bundle&#8212;point to those with absolute paths or paths relative to the `.vpdoc` on disk so Marked can resolve them.

[vp]: https://www.voodoopad.com/
