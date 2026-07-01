# <%= @title %>

The Style Manager provides a centralized interface for managing all of your
built‑in and Custom Styles. It gives you complete control over which
Styles appear in menus, their order, keyboard shortcuts, and more.

## Opening the Style Manager

To open the Style Manager, click the **Manage Styles…** button in the {% prefspane Style %}
pane, or use {% appmenu Style, Manage Styles (~@$m) %}. You can also drag CSS files directly onto the preferences window --- Marked
will import them, open the Style Manager, and select the newly added row for
you.

![Style Manager][img-style-manager]

  [img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

## The Style Table

The Style Manager displays all of your styles in a sortable table that mixes
built‑in and custom styles seamlessly. Each row in the table contains several
columns:

### Enabled Checkbox

The **Enabled** checkbox immediately adds or removes the style from the Style
menu, Default Style popup, and keyboard shortcuts. When you disable a style,
it's hidden from menus but remains in the Style Manager for easy re‑enablement.

If you disable the currently active style, Marked automatically switches to the
next available enabled style.

### Name Column

The **Name** column displays the style's display name. You can edit this name
inline by clicking directly on it; changes persist and propagate to every menu
where the style appears. This is especially useful for custom styles where you
might want a more descriptive name than the filename.

Built‑in styles have locked names that cannot be edited. To customize a
built‑in style's name, duplicate it first to create an editable copy.

### Source Column

The **Source** column indicates where the style comes from:

- **Built‑in**: Styles that come with Marked and are stored in the application
  bundle
- **Custom**: Styles you've added from CSS files on your drive
- **Duplicated**: Styles created by duplicating another Style (either built‑in
  or custom)

### Actions Column

Each row includes an **Actions** stack with buttons for managing that Style:

**Edit**: Opens the CSS file in your default editor. Built‑in styles cannot be
edited directly -- you'll need to duplicate them first to create an editable copy.

**Duplicate**: Creates a copy of the style and a new CSS file on disk. The
duplicate appears immediately below the original style in the table. This is
the recommended way to customize built‑in styles.

**Reveal**: Shows the CSS file in Finder, making it easy to locate the file on
your drive. This button is only available for custom styles with a file path.

**Delete**: Removes the style from Marked. For custom styles, you'll be given
the option to either remove just the reference (keeping the CSS file) or move
the CSS file to the Trash. Built‑in styles cannot be deleted, but they can be
disabled.

**Restore**: For built‑in styles, this button restores the style to its
default state if it has been modified. This button is only visible for
built‑in styles.

## Reordering Styles

Rows can be reordered via drag and drop. Simply drag a style row to a new
position in the table. The order you set here drives:

- The Style menu order in Marked's menus
- Keyboard shortcut assignments (`⌘1`–`⌘9` for the first nine enabled styles,
  `⌥⌘1`–`⌥⌘0` for the next ten, and so on)

Drag styles into the keyboard shortcut slots you want them to
occupy.

## Adding Styles

There are several ways to add new custom styles to the Style Manager:

### Add Button

Click the **Add New Style** button to open a file picker
where you can select one or more CSS files to import. Selected files will be
added to the Style Manager and enabled by default.

### Drag and Drop

You can drag CSS files directly onto the Style Manager window. When you drag
files over the window, an overlay will appear showing "Add a Custom Style" (or
"Add N Custom Styles" for multiple files). Drop the files to import them.

You can also drag CSS files onto specific positions in the table — the drop
indicator shows where the new style will be inserted, allowing you to control
both import and positioning in one action.

Dragging CSS files onto the {% prefspane Style %} preferences pane will also
import them and open the Style Manager automatically.

## Live Preview

The right pane of the Style Manager displays a live preview of the selected
style. The preview renders a comprehensive sample document with headings,
lists, tables, code blocks, blockquotes, and other common Markdown elements,
all styled with the actual CSS from the selected style.

The preview uses the CSS file directly from disk, so any edits you make in your
external editor will update instantly in the preview. This makes it easy to
see your changes in real time as you develop custom styles.

### Dark Mode Preview

A checkbox above the preview allows you to toggle between light and dark mode
previews. This is useful for testing how styles look in both appearance modes,
especially if you're creating styles that adapt to system appearance.

## Keyboard Shortcuts

The Style Manager displays a legend below the table showing how keyboard
shortcuts are assigned. The first nine enabled styles receive {% kbd cmd 1 %} through
{% kbd cmd 9 %} ({% kbd cmd 0 %} is reserved), the next ten receive {% kbd opt cmd 1 %} through {% kbd opt cmd 0 %}, and so on. You can see the assigned keyboard shortcuts in the Style popup menu on any Preview.

## Filtering Disabled Styles

A checkbox at the bottom of the window allows you to show or hide disabled
styles. When unchecked, only enabled styles are displayed, making it easier to
focus on and reorder your active styles. When checked, all styles (enabled and disabled)
are shown, allowing you to manage your complete style collection.

## Restoring Built‑in Styles

The **Restore All Built‑in Styles** button at the bottom of the window
restores all built‑in styles to their default state. This is useful if you've
disabled built‑in styles and want to re‑enable them, or if you want to reset
any modifications made to built‑in styles.

## Tips

- **Organize by frequency**: Drag your most‑used styles to the top to give
  them the easiest keyboard shortcuts ({% kbd cmd 1 %}, {% kbd cmd 2 %}, etc.)

- **Disable instead of delete**: Rather than deleting styles you're not using,
  disable them. They'll stay out of your way but remain available if you need
  them later.

- **Use duplicate for experimentation**: Duplicate a style before making major
  changes so you can always return to the original.

- **Preview while editing**: Keep the Style Manager open while editing CSS
  files to see your changes update in real time in the preview pane.

- **Batch import**: You can select multiple CSS files at once when using the
  Add button, or drag multiple files to import them all in one action.


