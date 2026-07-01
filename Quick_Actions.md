# <%= @title %>

The Quick Actions palette is a searchable command launcher for Marked. It collects actions from the main menu bar and the preview **gear menu**, plus preview-only keyboard commands that do not appear in menus (such as **Autoscroll**). Use it when you know what you want to do but cannot remember which menu holds it.

## Opening the Quick Actions Palette

Open the palette with {% kbd shift cmd P %} or from {% appmenu File, Quick Actions… %}. The panel appears as a floating window above your current document.

Press the same shortcut again, or press **Escape**, to close the palette. If the palette is already open, choosing **Quick Actions…** from the menu also closes it.

## Customizing the Shortcut

The default shortcut is {% kbd shift cmd P %}. To change it, open {% prefspane General %} and record a new combination under **Open Action Palette** in the **Shortcuts** section.

Unlike **Activate Marked** and **Raise first window**, the Quick Actions shortcut works only when Marked is the active application. It updates the {% appmenu File, Quick Actions… %} menu shortcut to match your setting.

## Search and Filter

Type in the search field at the top of the panel to filter commands in real time. Matching is fuzzy and forgiving:

- Word order does not matter (`view source` matches **Toggle Source View**)
- Initials work well (`sv` matches **Source View**)
- Collapsed matching finds commands without spaces (`akdoc` matches **Ask About Document**)

Each result shows the command name on the left and its keyboard shortcut (when available) on the right in gray. Some commands also show a breadcrumb path (for example `Preview › Autoscroll`) when the action comes from a submenu or the preview engine.

## What Appears in the List

The palette includes:

- **Menu commands** from the main menu bar, including dynamic menus such as **Style**, **History**, and open **Window** tabs
- **Gear menu** commands from the preview window
- **Preview shortcuts** from the in-preview keyboard map (the same commands shown in the preview help HUD), including navigation, autoscroll, bookmarks, search, and other preview-only actions

When the same command appears in more than one place, Marked shows the shortest menu path and merges shortcut information from duplicates.

## Keyboard Navigation

Navigate the Quick Actions palette entirely from the keyboard:

- **↑/↓ Arrow Keys**: Move through the filtered list
- **Return**: Run the selected command
- **Escape**: Close the palette
- **⌘-key shortcuts**: Close the palette and run the matching menu command (for example, press {% kbd cmd U %} to run **Toggle Source View** instead of selecting it in the list)

Plain typing (without the Command key) filters the search field. Preview-only single-key shortcuts such as `s` for Autoscroll filter the list; press **Return** to run the selected command.

## Running Commands

Selecting a menu command dispatches it the same way as choosing it from the menu, including dynamic and gear-menu items.

Selecting a **preview shortcut** runs the associated action in the active preview (for example, toggling autoscroll or jumping to the next header). These commands require an open document with a preview; if no preview is available, the palette still opens but preview-only actions will have no effect.

For related file switching, see [Quick Open](Quick_Open.html). For the full preview keyboard reference, see [Keyboard Shortcuts](Keyboard_Shortcuts.html) or press {% kbd h %} in the preview to show the help HUD.
