# <%= @title %>

Marked includes a wiki navigation system that allows you to quickly jump between related text files using simple `[[wiki]]` links. This system is designed for seamless navigation and works best when configured to open links in the current window.

## Optimal Settings

To use wiki linking, enable **Convert `[[wiki links]]`** in {% prefspane Preview %}, and set the default extension that Marked will use when searching for matching files.

For the best experience, set **"Links to text files should open in:"**  to *"the current window"* in {% prefspane Apps %}. This ensures that navigation feels natural and history is preserved.

If **Highlight Markdown syntax errors** is enabled in {% prefspane Proofing %}, `[[wiki link]]` syntax that doesn't match a filename in the current directory will be highlighted in red to indicate that a referenced file doesn't exist. These highlights will update as files are added, but only after the current file is saved or reloaded. Clicking a highlighted missing file link will offer to create a new file for you, appending the default extension if needed. The new empty file will be opened in Marked, and if Edit New Documents is enabled, your editor will be opened with the new file.

## How Wiki Links Work

- **Wiki links** use the format: `[[wiki link]]`.
- When you click a wiki link, Marked will search for a matching file in the **same directory** as the current document.
- The file must have the extension specified in Marked's settings (e.g., `.md`), unless you provide a full filename with extension in the link (e.g., `[[notes.txt]]`).
- If you want to use text for the link that differs from the filename, add it after a pipe (`|`) in the link, e.g. `[[wiki linking|A note about linking]]`, which will display as `[A note about linking](wiki-link.md)`.
- If a wiki link starts with a `#`, it will be seen as an anchor link on the same page. Anchor names are normalized by lower casing and replacing all spaces with dashes. For processors that create header IDs without dashes (like MultiMarkdown), e.g. `## wiki links` gets an id of `wikilinks`, this navigation could break. In those cases, specify the correct link id, with a pipe and title if needed, e.g. `[[#wikilinks|#wiki links]]`.

### Matching File Names

When you use a link like `[[wiki link]]`, Marked will look for a file with any of the following names (assuming your default extension is `.md`):

- `wiki link.md`
- `WikiLink.md`
- `wiki-link.md`
- `Wiki-Link.md`
- `wiki_link.md`
- `Wiki_Link.md`
- `wikilink.md`
- `WikiLink.md`
- (and other combinations of spaces, dashes, underscores, and InterCaps)

**All matching is case-insensitive and flexible with separators.**
If you specify an extension in the link (e.g., `[[notes.txt]]`), Marked will look for that exact file.

## Backlinks

When a text file is opened and wiki navigation is enabled, the rest of the files in the directory will be scanned for `[[links]]` to the current file. This will happen in the background and the open document will be updated with a list of backlinks if any are found. To view the backlinks, the comments sidebar must be open. If it's closed, use the Gear menu (**Proofing->Show Comments**) or press {% kbd ^@c %} to open it.


## Navigation History

Marked tracks your navigation through wiki links, allowing you to move **backward and forward** through your file history — just like a web browser.

- **Back:** {% kbd @[ %}
- **Forward:** {% kbd @] %}

You can also use the **History** menu to jump to any previously visited file.
