# <%= @title %>

[MarsEdit][me] stores posts inside its database, not as loose files on disk. Marked therefore uses a dedicated preview workflow that talks to the running MarsEdit application.

## MarsEdit Preview window [marsedit-preview-window]

Choose {% appmenu File, New, MarsEdit Preview %}. Marked asks AppleScript to read the **front post in MarsEdit** (Red Sweater's bundle IDs for direct, Mac App Store, Setapp, and MarsEdit 4/5 are recognized). Keep MarsEdit running with a document open while you work.

- **Manual refresh:** save from Marked's preview if you want to force an update.
- **Automatic updates:** enable watching so each MarsEdit autosave refreshes Marked.

If no post is available, Marked surfaces a short error in the preview instead of stale text.

### Extended posts [extended-posts]

Content in MarsEdit's **extended** field is separated in Marked's preview and source using a WordPress-style `<!--more-->` divider so pagination-oriented sites (WordPress, Jekyll, etc.) still see the break. The comment is harmless elsewhere.

### Tags and categories in metadata [tags-and-categories-in-metadata]

MarsEdit's tags and categories are exposed to the MultiMarkdown metadata block. With the MultiMarkdown processor ({% prefspane Processor %}), you can reference them like:

    Tagged: [%tags]
    Posted In: [%categories]

[me]: https://www.red-sweater.com/marsedit/
