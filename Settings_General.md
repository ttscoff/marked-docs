# <%= @title %>

Options in the {% prefspane General %}:

![Settings: General][1]

[1]: images/screenshots/preferences-General.jpg @2x width=689px height=1031px class=preferencepane-scroll

### Window [window]

Keep new windows on top
: Automatically set new windows to "float" above other applications.

Raise window on update
: When a change is detected in a watched file, the preview window for that document will rise above other windows on your Desktop without activating Marked.

Translucent in background
: Fade the window when it's not focused. Use the slider to set the opacity.

Disable memory-intensive features on large documents
: Disable some processor-intensive features such as collapsible headlines when documents are over 100k.

New documents open in
: Choose **windows**, **tabs**, or **automatic** (follow the macOS system setting for tabbing). When using tabs, navigate with {% kbd cmd shift [/] %} and the [Quick Open panel](Quick_Open.html).

Bring updated document to front
: When a preview is updated, select its tab or order its window to the front **within Marked only**. If another application is frontmost (e.g. your text editor), Marked stays in the background — the correct tab is selected so it is ready when you switch back to Marked. To pop the preview above all applications without activating Marked, use **Raise window on update** instead.

Return focus to previous app
: When enabled, if a raise/bring-on-update action causes Marked to take foreground focus, keyboard focus is returned to the app that was frontmost before the update (such as your text editor). When disabled, Marked never performs this focus handoff. If Marked does not become frontmost, this option has no effect.

### Status bar [status-bar]

Show style picker
: Shows the style picker in the bottom bar of the preview window.

Show word count
: Show word count (and statistics button) in the bottom bar of the preview window.

Word count excludes
: Word count calculations can ignore any combination of:

- **Footnotes/Citations**
- **Blockquotes**
- **Indented code blocks** (fenced code blocks are always excluded)
- **Image captions**

### Shortcuts [shortcuts]

Click the shortcut field to record a hotkey combination that triggers an event:

Activate Marked
: Switch to Marked when this hotkey is pressed in any application.

Raise first window
: Raise the frontmost (last active) Marked preview window to the foreground without leaving the current application.

Open Action Palette
: Open the [Quick Actions](Quick_Actions.html) command palette while Marked is active. This shortcut applies to {% appmenu File, Quick Actions… %} and works only within Marked (not from other applications).

Reset Alerts
: Restore any alert dialogs you have previously dismissed so they can appear again.
