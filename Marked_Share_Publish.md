# <%= @title %>

**Marked Share** is Marked's online publishing service at [share.markedapp.com](https://share.markedapp.com). Connect your Mac once, then publish the front document as a **TextPack** with images and optional Reading Mode highlights. Anyone with the link can view the document on the web.

For full web documentation, including highlight sets, reader reviews, passwords, and API reference, see the [Marked Share Documentation](https://share.markedapp.com/docs).

This feature is separate from the macOS **Share extension** (system Share menu). See [Using the Share Extension](Share_Extension.html) for sending files or selections into Marked from other apps.

## Connect your account [connect-your-account]

Before your first publish, connect Marked to your Share account:

1. Choose {% appmenu File, Publish, Connect Account… %}.
2. Marked opens your default browser to sign in at share.markedapp.com.
3. After you approve the connection, the browser returns to Marked with a secure login link. Confirm the account label shown in the dialog.

Marked stores the API token and device key in the macOS Keychain on this Mac. Credentials are not written to logs or crash reports.

To disconnect, choose {% appmenu File, Publish, Disconnect Account… %}. Published documents stay online; revoke access anytime at share.markedapp.com if needed.

## Publish a document [publish-a-document]

With a document open in the preview, choose {% appmenu File, Publish, Publish… %}.

The first time you publish a document, Marked shows an options sheet:

- **Title** — shown on Share (defaults to the document name without its extension).
- **Visibility** — Private, Unlisted, or Public. New publishes default to **Unlisted** (reachable by link, not listed publicly). Documents added to public collections are automatically set to **Public**.
- **Collection** — choose an existing collection to publish directly to it, or select **Create New Collection…** to create one in your browser.
- **Reading style** — Editorial, Manuscript, Swiss, Contrast, Typewriter, or **None**. Defaults from the document preview style when possible. Share uses this as a suggestion; readers can override it. Choose **None** to publish without a suggested style.
- **Include highlights and comments** — embeds Reading Mode highlights in the TextPack. Defaults to on when the document has highlights.
- **Allow others to remix** — when enabled, viewers can fork the document on Share.

Marked builds a TextPack in the background (Markdown, assets, and optional `highlights.json`), uploads it, and records the share URL on this Mac.

### Publish to Collection [publish-to-collection]

To publish directly to a specific collection, choose {% appmenu File, Publish, Publish to Collection %} and select your collection from the submenu.

You can also choose **Create New Collection…**, **Manage Collections…**, or **Manage Domains…** directly from the menu to configure your collections on [share.markedapp.com](https://share.markedapp.com).

### Update an existing publish [update-an-existing-publish]

After a document is linked to Share, the menu item reads **Update Published Document** instead of **Publish…**. Choose it to upload a new TextPack version. Marked sends the server's content hash so concurrent edits from another Mac or the web are detected.

If someone else updated the document on Share first, Marked asks whether to **Overwrite** with this Mac's version, **Open on Web**, or **Cancel**.

## Post to Micro.blog [post-to-microblog]

If you have connected your Micro.blog account in [Marked Share Settings](https://share.markedapp.com/settings), you can syndicate published documents directly to Micro.blog:

1. Publish the document to Marked Share first.
2. Choose {% appmenu File, Publish, Post to Micro.blog… %}.
3. Select your post format:
   - **Full Document** — publishes the complete Markdown content to your blog.
   - **Summary Excerpt with Link** — publishes a summary snippet linking back to your Marked Share document.
4. Click **Post**. Marked publishes the post and lets you immediately copy the link or open the post in your browser.

You can also post previously published documents to Micro.blog by right-clicking them in the **Published Documents** window.

## After publishing [after-publishing]

When a publish finishes, Marked confirms success and offers:

- **Copy Share Link** — {% appmenu File, Publish, Copy Share Link %}
- **Open on Web** — {% appmenu File, Publish, Open on Web %}

These commands apply to the front document when it has a linked publish record.

## Published Documents window [published-documents-window]

Choose {% appmenu File, Publish, Published Documents… %} to open a list of documents published from this Mac and synced from your Share account. For each entry you can:

- **Search** — Use the search field at the top of the window to search across your published titles, local file paths, and document content with live snippets.
- **Open** — Opens the local file when Marked still has a link to it on disk.
- **Import from Marked Share…** — Downloads the TextPack when there is no local file so you can save and edit it locally.
- **Open on Web** or **Copy Share Link** — View or share the document's web link.
- **Post to Micro.blog…** / **Open on Micro.blog** — Syndicate the document to Micro.blog or open an existing syndicated post.
- **Forget** — Removes the local link from this Mac without deleting the online document.

The list refreshes from Share when you are connected. If you are offline or disconnected, Marked shows cached records and may prompt you to reconnect.

## What you can publish [what-you-can-publish]

You can publish any document Marked can render, including:

- Saved Markdown and text files
- Transient previews (clipboard, streaming, or unsaved documents)
- TextBundles and other supported formats

Only one publish operation runs at a time per document window; the menu item is disabled while an upload is in progress.

## Tips [tips]

- Publishing includes images referenced by the preview. Very large bundles may be rejected before upload; reduce embedded assets if you hit a size limit.
- Highlights exported in the TextPack use Marked's highlight JSON format. See [Reading Mode](Reading_Mode.html) for creating and exporting highlights.
- Marked Share is available in Direct, Mac App Store, Setapp, and Marked Pro builds. No separate subscription is required for publish.
