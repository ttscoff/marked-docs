# <%= @title %>

**Marked Quick Look** is a separate Mac App Store app that adds a Quick Look preview extension for Markdown and plain-text files. Press Spacebar in Finder (or use Quick Look anywhere macOS supports it) to see a styled HTML preview instead of raw source.

Marked Quick Look is **not included with Marked 3**. It is a separate purchase (**$4.99** on the Mac App Store). <!-- MAS link: add App Store URL here when available -->

I> Marked Quick Look and Marked 3 are independent products. Buying Marked does not install the Quick Look extension, and buying Marked Quick Look does not include a Marked license. The preview includes an optional **Open in Marked** button when Marked is installed.

## What you get

Marked Quick Look registers a **Quick Look Preview extension** that renders `.md`, `.markdown`, `.mmd`, and many plain-text files with the same visual polish Marked is known for:

- **Apex processing** — powered by [Apex](https://github.com/ApexMarkdown/apex), an open-source Markdown processor that supports CommonMark, GitHub Flavored Markdown, MultiMarkdown, Kramdown, and a **Unified** mode that combines features from multiple flavors
- **Marked preview styles** — nine built-in themes (GitHub by default) plus custom CSS import
- **Syntax highlighting**, **MathJax**, and **Mermaid** diagrams (bundled scripts; no network required)
- **CriticMarkup** in markup view
- **Open in Marked** — jump from Quick Look to the full Marked preview when Marked is installed

W> Quick Look previews are read-only. File includes (`<<[file]`, `{{file}}`, and similar syntax) are **not expanded** in Quick Look. They appear as highlighted placeholders (`Included file: path`) so you can see where content would be pulled in. Open the document in Marked for full multi-file rendering.

## Installation

1. Install **Marked Quick Look** from the Mac App Store.
2. **Launch the app once** from `/Applications`. This registers the Quick Look extension with macOS.
3. Press **Spacebar** on a Markdown file in Finder to preview it.

The container app includes a **Settings** window ({% kbd cmd %},{% kbd , %}) where you can choose the Apex processor mode, preview style, syntax-highlighting theme, and toggles for MathJax and Mermaid.

## Apex and Markdown flavors

Marked Quick Look uses [Apex](https://github.com/ApexMarkdown/apex) for all rendering. Apex is developed as a standalone processor and is also embedded in Marked 3.

In Settings, choose an **Apex mode** to match your writing style:

| Mode | Best for |
| --- | --- |
| **Unified** (default) | Mixed Markdown features across flavors |
| **CommonMark** | Strict CommonMark |
| **GFM** | GitHub Flavored Markdown |
| **MultiMarkdown** | Metadata, transclusion, footnotes |
| **Kramdown** | Kramdown-style extensions |

Unified mode is the best default for most documents. Switch modes if a file was written for a specific processor and something renders unexpectedly.

## Open in Marked

When Marked 3 is installed, the Quick Look preview can show an **Open in Marked** button in the toolbar. Click it to hand the file off to Marked for live preview, export, proofreading, and full include expansion.

If Marked is not installed, the button appears disabled.

## Troubleshooting Quick Look conflicts

macOS allows multiple apps to register Quick Look preview extensions for Markdown. Only one extension handles each preview, and **another app's plugin may take precedence** over Marked Quick Look.

### How to tell which extension is active

Marked Quick Look previews include an **Open in Marked** toolbar when that option is enabled. If you see a different layout, raw monospace source, or another app's styling, a different Quick Look handler is probably winning.

### Restore Marked Quick Look precedence

After installing or updating, or after resetting the Quick Look cache, run these steps:

1. **Launch Marked Quick Look** once from `/Applications` (or Run from Xcode if you are testing a development build).
2. In Terminal, register and prefer the extension:

```bash
pluginkit -a "/Applications/Marked Quick Look.app/Contents/PlugIns/MarkedQuickLookPreview.appex"
pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview
```

3. Reset Quick Look services:

```bash
killall quicklookd QuickLookUIService 2>/dev/null
```

4. Press **Spacebar** on a `.md` file again.

To clear cached previews:

```bash
qlmanage -r cache
```

### Temporarily disable a conflicting extension

To confirm another app is overriding Marked Quick Look, disable its extension with `pluginkit -e ignore -i BUNDLE_ID`, preview a file, then restore with `pluginkit -e default -i BUNDLE_ID`.

Example — disable **Folder Quick Look**'s Markdown extension:

```bash
pluginkit -e ignore -i studio.appahead.AA7.Markdown-Quick-Look-Extension
```

### Common conflicting apps

These apps (and others) register Quick Look preview extensions that may handle `.md` files:

| App | Bundle ID (preview extension) |
| --- | --- |
| **Folder Quick Look** | `studio.appahead.AA7.Markdown-Quick-Look-Extension` |
| **QLMarkdown** | `org.sbarex.QLMarkdown.QLExtension` |
| **Peek** | `com.bigzlabs.peek.peekextension` |
| **Highland Pro** | `com.quoteunquoteapps.highland.pro.qlplugin` |
| **Bear** | `net.shinyfrog.bear.Bear-Quicklook-Extension` |
| **Ulysses** | `com.soulmen.ulysses-setapp.quicklookextension` (Setapp) / `com.soulmen.ulysses.quicklookextension` |
| **Drafts** | `com.agiletortoise.Drafts-OSX.Drafts-OSX-QuickLookPreview` |
| **Scrivener** | `com.literatureandlatte.scrivener3.ScrivQuickLook` |
| **Black Ink** | `com.red-sweater.blackink2.quicklook` |

W> **iA Writer** assigns its own UTI (`net.ia.markdown`) to `.md` files when installed. Marked Quick Look 1.0.2+ handles that UTI. **Folder Quick Look**, **QLMarkdown**, and **Peek** are also frequent sources of conflicts.

List registered preview extensions:

```bash
pluginkit -m -D -p com.apple.quicklook.preview -A -v | grep -i MarkedQuickLook
```

W> Do not grep for `markdown` to verify Marked Quick Look. Its bundle ID is `com.brettterpstra.MarkedQuickLook.preview` and does not contain the word "markdown". A `grep -i markdown` can return no results even when Marked Quick Look is installed and enabled. To list other Markdown handlers, run the full `pluginkit` command without grep, or grep for a specific bundle ID from the table above.

Extensions marked with `+` are explicitly enabled; use `pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview` to move Marked Quick Look to the front.

### Still seeing plain text?

If the preview shows **unstyled monospace source**, macOS is falling back to the built-in **Text.qlgenerator** because no preview extension matched the file's UTI.

1. Confirm registration with `pluginkit ... | grep -i MarkedQuickLook` (not `markdown`).
2. Check the file's assigned UTI: `mdls -name kMDItemContentType -name kMDItemContentTypeTree /path/to/file.md`
3. Check **Console.app** for errors from `MarkedQuickLookPreview`.
4. Reinstall Marked Quick Look to `/Applications` and launch it once.

See the [Marked Quick Look troubleshooting guide](https://github.com/ttscoff/MarkedQuickLook/blob/main/TROUBLESHOOTING.md) for a full step-by-step checklist.

### Development builds

Debug builds from Xcode live in DerivedData and **do not register automatically**. Run the **Marked Quick Look** container app from Xcode (Cmd+R) after each clean build, then re-run the `pluginkit -a` and `pluginkit -e use` commands with the DerivedData path to your `.appex`.

## Related topics

- [Opening Files](Opening_Files.html) — how Marked opens and watches documents
- [Multi-file Documents](Multi-File_Documents.html) — include syntax and full expansion in Marked
- [Choosing a Processor](Choosing_a_Processor.html) — processor options inside Marked 3
- [Share Extension](Share_Extension.html) — send files to Marked from the system Share menu
