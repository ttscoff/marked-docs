# <%= @title %>

[nvUltra][nvu] indexes plain-text notebooks on disk and can hand the selected note(s) to Marked with a built-in shortcut, or stream the note you are editing.

## Preview File(s) in Marked [preview-files-in-marked]

In nvUltra's **Folder Navigator** (or wherever you browse notes), **control-click** file(s) to open the contextual menu and choose **Preview File(s) in Marked**.

![][nvultramenu]

Marked opens normal file-backed previews so your MultiMarkdown renders with Marked styles, bookmarks, minimap toggles, and export options. Use this when you want to jump straight from nvUltra without dragging files to the Dock.

## Streaming Preview [streaming-preview]

nvUltra can also send the note you are editing to Marked as you type.

1. In nvUltra, choose **Enable Marked Streaming&nbsp;Preview** from the **View** menu.
2. In Marked, choose {% appmenu File, New, Streaming Preview %}.

![Enable Marked Streaming Preview in the nvUltra View menu][nvultrastream]

The preview updates as you edit the current note.

## Alternative: folder watching [alternative-folder-watching]

Need Marked to follow **whichever note you touched most recently** in a whole folder? Drop that notebook folder onto Marked instead; see **[Folder Watching](Folder_Watching.html)** for nvALT-style watching, scrolling to edits, and how that workflow differs from opening explicit files.


[nvultramenu]: images/nvUltra_preview_in_marked_menu.png width=854px height=264px class=center

[nvultrastream]: images/nvUltra_enable_marked_streaming_preview.jpg @2x width=455px height=205px class=center

[nvu]: https://nvultra.com/
