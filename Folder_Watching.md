# <%= @title %>

Drop a **folder** of plain-text notes onto Marked. Marked opens a preview window that always tracks the **most recently edited** eligible file inside that folder (.md, .txt, .markdown, etc., matching Marked's file-type filters).

Updates run whenever any watched file saves: if the newest file matches the previous one, Marked scrolls toward the detected edit region; when you switch documents, the entire preview swaps to the active file.

## Works well with nvUltra, nvALT, and similar tools [works-well-with-nvultra-nvalt-and-similar-tools]

Notebook apps that leave individual files on disk (classic **nvALT**, **nvUltra**, **Notational Velocity**-style libraries, synced Git folders, Dropbox scratch folders, etc.) pair naturally with folder watching — you write in one window and keep Marked pinned beside it without manually reopening previews.

**nvUltra** also offers **[Preview File(s) in Marked](nvUltra.html)** in its contextual menu when you want to open specific notes in Marked directly, and **[Enable Marked Streaming Preview](nvUltra.html#streaming-preview)** in the View menu for a live preview as you type. **nvALT** streams automatically while it is open; see [nvALT](nvALT.html).

Marked also exposes the same watcher behavior under other menu names when you consolidate many small chapters into what feels like one reading experience; see also [Multi-File Documents](Multi-File_Documents.html) for manuscripts that intentionally merge multiple Markdown sources.

## Review a folder [review-a-folder]

When you need to read a batch of files in order, such as a set of generated prompts or chapter drafts, turn on review mode for the folder. Choose **History > Review This Folder** in a folder window. If you're viewing a single file, the same command opens its folder in review mode.

In review mode:

- Marked opens the first file you haven't reviewed yet, in Finder-style name order (`file2.md` comes before `file10.md`).
- **History > Mark Reviewed and Next** (⌃⌘↩) checks off the current file and opens the next unreviewed one.
- The window title and the review sidebar show your progress, such as "42 / 118".
- Click a file in the sidebar to open it, or click its checkbox to mark it reviewed or unreviewed. A dash in the checkbox means the file changed after you reviewed it, so it counts as unreviewed again.
- The sidebar's popup shows all files, only unreviewed files, or only reviewed files. **History > Show Review Sidebar** hides or shows the sidebar.
- Saving other files in the folder updates the count without switching away from the file you're reading.

Marked remembers review progress for each folder, and a folder you were reviewing reopens in review mode. Review mode lists only files directly inside the folder, not files in subfolders. Choose **Review This Folder** again to turn review mode off; your progress is kept.
