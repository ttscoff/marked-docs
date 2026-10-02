# <%= @title %>

[iA Writer][ia] files are ordinary Markdown documents on disk. Drag the active file from **Finder** or from the **title-bar proxy icon** onto Marked to open it.

Because the preview path matches the editor file, live updates behave like any other watched Markdown document.

iA Writer content blocks (a line starting with `/` and a file path) are converted to Marked includes when **iA Writer compatibility** is enabled in Processor settings, which it is by default. Text files are inserted, code files become code blocks, and images are displayed. Lines inside code blocks are left alone. Turn the setting off if you write lines that begin with paths and don't want them treated as includes.

Other optional Processor settings improve compatibility: **Treat +++ as page breaks**, **Convert // lines to comments** (lines must start at column 0), and **Remove iA Writer annotations**.

[ia]: https://ia.net/writer
