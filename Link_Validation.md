# <%= @title %>

Link validation pings the destination of a URL and tests for errors. This helps avoid broken and invalid links in your published document, and is especially useful for bloggers.

## Validating single links

![][1]

   [1]: images/validate_single.png @2x width=832px height=267px class=center

Click and hold on a link in the preview until it blinks, then release to open the link action menu. Choose "Validate link" to run the test. Results are displayed in the popup.

## Validating all links

![][2]

   [2]: images/screenshots/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Choose "Validate all links" (shortcut {% kbd ctrl cmd L %}) from the Gear menu or the right click menu. All remote links in the document will be checked, and the results are displayed in a popup. Clicking a link in the popup will scroll to and highlight its respective link in the document.

Valid URLs may be hidden from the popup with the "Hide Valid" button at the top of it. This will show only URLs that have returned an error status.

Pressing Escape will hide the validation results. They can be revealed again using {% kbd ctrl cmd L %} or the Gear menu.

## Validating automatically

Turn on "Automatically validate URLs on update" in the Preview settings (or at the bottom of the link validation popup). When the document loads, contained links will be tested in background. A dialog will only show if there are errors.

To disable the popup, turn it off in settings, or uncheck the box at the bottom of the popup window.
