# <%= @title %>

Marked works with [Obsidian][obsidian-app] notes in two ways: open a **vault folder** for automatic following, or use the **community plugin** for tighter sync.

Obsidian's built-in preview is ideal when you never leave the app. Choose Marked when you want publish-quality export, advanced proofreading, custom CSS themes, or the same live preview workflow across multiple editors. See [Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) for a full comparison.

## Open an entire vault [open-an-entire-vault]

Drag the **vault folder** (the directory that contains Obsidian’s hidden configuration folder at the vault root) onto Marked in the Dock. Marked watches that tree, keeps the **most recently edited** note in the preview, and updates as you save in Obsidian.

For vault-specific defaults (style, processor, base URL for images, and so on), add a [Custom Rule](http://support.markedapp.com) that matches paths under that vault.

## Obsidian callout syntax [obsidian-callout-syntax]

When the MultiMarkdown processor runs, Marked converts common **Obsidian-style callouts** (the `> [!note]` pattern) into styled block markup so they match the rest of your preview.

## Marked 3 Obsidian plugin [marked-3-obsidian-plugin]

The [Marked 3 Obsidian plugin][plugin] can open the current note or the whole vault with commands or hotkeys so the Marked window tracks what you are editing. Use the Command Palette (**⌘P**) and search for **Marked**, or assign hotkeys in Obsidian’s **Hotkeys** settings.

### Installing from Community Plugins [installing-from-community-plugins]

In Obsidian, open **Settings → Community plugins**, browse or search for **marked**, and install **Open in Marked**.

### Manually installing the plugin [manually-installing-the-plugin]

If you prefer to install from GitHub:

1. Download `main.js` and `manifest.json` from the [latest release][plugin-releases] on GitHub (or build them from the [Marked3-obsidian][plugin] repository).
2. In your vault, create the plugin folder under `plugins/` inside Obsidian’s configuration directory at the vault root. The folder name must match the plugin `id` in `manifest.json` (see the [plugin README][plugin] for the full path).
3. Copy `main.js` and `manifest.json` into that folder.
4. In Obsidian, open **Settings → Community plugins**, turn off **Restricted mode** if needed, and enable **Open in Marked**.

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest
