# <%= @title %>

Drop a **folder** of plain-text notes onto Marked. Marked opens a preview window that always tracks the **most recently edited** eligible file inside that folder (.md, .txt, .markdown, etc., matching Marked's file-type filters).

Updates run whenever any watched file saves: if the newest file matches the previous one, Marked scrolls toward the detected edit region; when you switch documents, the entire preview swaps to the active file.

## Works well with nvUltra, nvALT, and similar tools

Notebook apps that leave individual files on disk (classic **nvALT**, **nvUltra**, **Notational Velocity**-style libraries, synced Git folders, Dropbox scratch folders, etc.) pair naturally with folder watching — you write in one window and keep Marked pinned beside it without manually reopening previews.

**nvUltra** also offers **[Preview File(s) in Marked](nvUltra.html)** in its contextual menu when you want to open specific notes in Marked directly instead of attaching Marked to the whole-folder watcher flow described above.

Marked also exposes the same watcher behavior under other menu names when you consolidate many small chapters into what feels like one reading experience; see also [Multi-File Documents](Multi-File_Documents.html) for manuscripts that intentionally merge multiple Markdown sources.
