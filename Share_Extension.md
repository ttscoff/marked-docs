# <%= @title %>

Marked includes a macOS **Share extension** that appears in the system Share menu. Use it to send a file or selected text to Marked without switching apps or copying URLs by hand.

The Share extension is **bundled with Marked 3**. You do not download or install it separately. It ships with the Direct, Mac App Store, Marked Pro, and Setapp builds.

## How it works

When you choose **Marked** from a Share menu, Marked opens immediately. There is no intermediate compose window.

### Share a file

From **Finder** (or another app that shares files), choose **Share → Marked**.

Marked receives the file path and opens it with the same `x-marked-3://open` URL handler used elsewhere. The file opens in Marked like a document you dragged to the Dock icon or chose with {% appmenu File, Open... ({{cmd}}O) %}.

Supported inputs include file URLs, local files, and web URLs when the sending app provides them.

### Share selected text

Select text in an app such as **TextEdit**, **Safari**, or **Mail**, then choose **Share → Marked**.

Marked places the text on the clipboard and opens a **transient preview** using the `x-marked-3://paste` handler. This is the same kind of unsaved preview you get from {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}. You can save it later with {% appmenu File, Save Transient Preview %}.

Plain text, HTML, RTF, and Markdown selections are supported when the source app provides them.

See [URL Handler](URL_Handler.html) for details on the underlying commands.

## Using the Share menu

### From Finder

1. Right-click a Markdown or text file (or select it and click the **Share** button in the Finder toolbar).
2. Choose **Marked** from the Share menu.

If **Marked** is not visible, see [Enable the Share extension](#enable-the-share-extension) below.

### From a text selection

1. Select the text you want to preview.
2. Open the app’s **Share** menu (menu bar **Share** item, toolbar Share button, or right-click context menu).
3. Choose **Marked**.

Marked launches (or comes to the front) with a preview of the shared content.

## Enable the Share extension

Marked must be installed in `/Applications` (or your usual Applications folder) and launched at least once before macOS lists its Share extension.

### Turn on Marked in System Settings

1. Open **System Settings**.
2. Go to **General → Login Items & Extensions** (on some macOS versions this appears as **Privacy & Security → Extensions**).
3. Click **Extensions** (or the **ⓘ** button next to Extensions).
4. Select **Sharing** (or **Share**).
5. Enable **Marked**.

### Add Marked to an app’s Share menu

Even when the extension is enabled system-wide, each app lets you choose which Share destinations appear:

1. Open an app that supports Share (Finder and TextEdit are easy tests).
2. Open the **Share** menu.
3. Choose **Edit Extensions…** (wording may be **More…** or **Extensions Preferences…** on older macOS versions).
4. Under **Share**, check **Marked**.
5. Optionally drag **Marked** higher in the list so it is easier to reach.

Changes apply to that Share menu immediately in most apps.

## If Marked does not appear in Share

W> The Share extension first became available in Marked 3.1.9. Make sure you've upgraded to at least that version.

Try these steps in order:

1. **Launch Marked once** after installing or updating. Quit and reopen Marked if you just upgraded.
2. **Confirm the extension is enabled** in System Settings as described above.
3. **Customize the Share menu** in the app you are sharing from. macOS hides infrequently used Share destinations until you enable them.
4. **Check for multiple Marked copies.** If both a Direct and Mac App Store build are installed, only the copy you are running registers its extension. Remove or rename the copy you are not using, then launch the one you want.
5. **Restart the Mac** if the extension still does not appear after an update. macOS caches Share extension registration and occasionally needs a restart to refresh it.
6. **Reinstall Marked** to `/Applications` if you are testing a build copied manually from Xcode or a disk image. The Share extension must be embedded inside the app bundle at `Marked.app/Contents/PlugIns/`.

## Tips

- The Share extension is ideal for quick previews of web snippets, email paragraphs, or notes without creating a file first.
- For whole pages or complex selections from a browser, the [browser extensions](Using_the_Browser_Extensions.html) may give more control (section selection, Markdownify URL, and so on).
- Shared files open as normal Marked documents with file watching enabled. Shared text opens as a transient preview until you save it.
