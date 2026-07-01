# <%= @title %>

[vim-marked][vimrepo] is a Vim plugin that opens the current Markdown buffer in Marked. It adds `:MarkedOpen`, `:MarkedQuit`, `:MarkedToggle`, and `:MarkedPreview` so you can send the file (or a range) to Marked without leaving the editor.

## Setup

Install with your plugin manager; see the [project README][vimrepo] for `vim-plug` and other options. The default `g:marked_filetypes` includes `markdown` and common variants; extend the list if you use a custom `filetype`.

## macOS and app name

Marked is macOS-only, so the plugin does not load on other systems. The default app name is **Marked 2**; if your copy of Marked is installed under a different name or path, set `g:marked_app` to match (for example a full path to the app bundle). The README covers quits, auto-quit, and focus behavior.

I> This help topic is not part of the vim-marked project; for the latest commands and options, use the [GitHub repository][vimrepo].


[vimrepo]: https://github.com/itspriddle/vim-marked
