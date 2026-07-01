# <%= @title %>

The "scroll to edit" feature in Marked keeps track of differences between the latest update and the last, trying to find the point where you made your most recent changes. Marked always tracks this, and a small red line appears in the preview to show you the location of the first change detected. In the Behavior preference panel, you can turn on "Scroll to first edit" and when a preview updates it will gently scroll the view to that location.

With "Scroll to first edit" turned off, you can still press the "e" key at any time in the preview to go to the last stored edit point.


### Notes on "Scroll to Edit"

This is a feature that is great when it works, but there are a lot of complications. Especially the first few times the document updates, there may be some jerkiness in the scroll. If your changes are all inside of one very large element (an excessively long paragraph, for example), it will only be able to get close with the marker. Similarly, if you add one or two words to the end of the document, the change marker will be positioned in the element above until there is enough content to anchor in the new element.
