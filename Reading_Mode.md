# <%= @title %>

Reading Mode keeps your place in long documents, focuses the current block, and lets you save persistent highlights.

## Entering Reading Mode [entering-reading-mode]

Choose **Preview > Reading Mode** or press {% kbd {{ctrl}}{{opt}}R %}. If Speed Read is running, Marked stops it before entering Reading Mode.

The current paragraph, heading, list item, image, code block, table, or other reading unit receives a left marker. Keyboard navigation moves smoothly between blocks and keeps the current unit near the upper third of the preview. Scrolling manually retargets the focus without snapping the page.

## Navigation and resume [navigation-and-resume]

While Reading Mode is active:

- {% kbd j %} or {% kbd down %}: Move to the next reading unit.
- {% kbd k %} or {% kbd up %}: Move to the previous reading unit.
- {% kbd h %}: Highlight the selection, or toggle a highlight on the current unit when no text is selected.

Marked saves the current reading position for each document. When a saved position differs from the current view, entering Reading Mode offers two choices:

- **Resume** returns to the saved reading position.
- **Start from Here** uses the reading unit currently visible in the preview.

## Focus mode [focus-mode]

Click the Focus mode tool at the top of the preview to dim every block except the current reading unit. Focus mode follows the current unit as you navigate. Click the tool again to restore the other blocks, or leave Reading Mode to clear Focus mode automatically.

## Creating and editing highlights [creating-and-editing-highlights]

Select text and press {% kbd h %} to create an inline marker highlight. With no selection, press {% kbd h %} to highlight the entire current reading unit, or press it again to remove that unit highlight. The first highlight prompts for a signature, which Marked uses when creating CriticMarkup. You can change the signature in {% prefspane Preview %}.

### Selection popup

Select text to show the selection popup, then click its highlighter to create an inline highlight. The popup also includes the selection word count when **Show word count on selection** is enabled.

### Automatic highlights

Click the highlighter tool at the top of the preview to automatically highlight text as you select it. Click the highlighter in the selection popup to undo the last automatic highlight, or click the top highlighter tool again to turn automatic highlighting off.

Inline highlights display start and end handles when you point to or select them. Drag either handle to extend or contract the highlighted range. Changes are saved automatically and restored when the document is refreshed or reopened.

Click a highlight to focus it, then press Delete or Backspace to remove it. Control-click a highlight and choose **Share...** to open the macOS Share sheet with the document title and highlighted text.

The **Show highlights when Reading Mode is off** setting controls whether saved highlights remain visible after you leave the mode.

## CriticMarkup actions [criticmarkup-actions]

The Preview menu provides two actions for saved highlights:

- **Copy Highlights as CriticMarkup** copies every highlight in CriticMarkup format without changing the source file.
- **Inject Highlights into Document...** asks for confirmation, then wraps unambiguous matching source text in CriticMarkup. Marked skips missing, duplicate, or overlapping matches and reports the result.

With a signature, generated markup uses <code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>. Without one, Marked creates only the <code>{=<span>=</span>highlighted text==}</code> marker.

## Printing highlights [printing-highlights]

Reading Mode highlights are included when printing or saving as PDF by default. Use **Include Reading Mode highlights** in the print sheet to change it for the current output. The matching setting in {% prefspane Export %} controls the default for future print and PDF jobs.
