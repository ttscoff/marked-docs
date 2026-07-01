# <%= @title %>

Flexibility is key.

## Gear Menu

![][4]

   [4]: images/gearmenu.jpg @2x width=740px height=235px class=center

The Gear menu provides most of the features found in the menubar, plus some preview-specific functions. Just click the gear in the lower right of the window to access these functions.

## Keep on Top

![][5]

   [5]: images/KeepOnTopPin.jpg @2x width=740px height=345px class=center

The lock icon in the lower left will bring the Preview window to the front and keep it there (float it) when switching to other applications. You can set a transparency on the window in the {% prefspane General %} which will allow the window to fade when using other applications.

This feature can also be toggled with {% kbd shift-opt-cmd-f %}.

## Window level defaults

In the {% prefspane General %} you can use "Keep new windows on top" to set new windows to always remain above other windows, and/or set windows to rise to the top when their associated document is updated. Windows set to rise on update will not "steal focus" from your editor, they will only rise to be visible without becoming active.

## View Source

![][6]

   [6]: images/view_source.jpg @2x width=740px height=345px class=center

You can switch between preview and source code views with the button in the upper right corner. This view can also be toggled with U.

## Search

![][7]

   [7]: images/SearchBarFull.jpg @2x width=818px height=195px class=center

The find bar can be accessed with {% kbd cmd F %} and allows you to search through the preview for a word or phrase. Once you search, you can use {% kbd cmd G %} and {% kbd shift cmd G %} to navigate forward and backward through additional results.

The checkboxes on the right side of the search bar allow you to narrow the search down by case sensitivity, whole words only and regular expressions. In addition to regular expression search, wildcard (*?) searches always work, even when the regex option is off.

You can also surround a search term or phrase with slashes to interpret it as a regular expression automatically (e.g. '/term.+?\b/').


Use the search feature in combination with bookmarking to save locations as you find them. Press Tab ({% kbd ⇥ %}) to focus the document, then type Shift-[1-9] to set a bookmark on that number. You can jump back to the bookmark by just typing the number (without the Shift key), or by using n/p to navigate through them in document order. N/P will navigate in numeric order. For bookmarks, the Table of Contents, the Mini Map, and fast header search, see [Document Navigation](Document_Navigation.html). See the [Preview Navigation](Keyboard_Shortcuts.html#previewnavigation) section for more options, or type "?" any time in the Preview.

> **Note:** The search cannot wrap between elements, meaning that a search string cannot continue between a paragraph and a headline, across list items, etc.

You can toggle the "Whole words," "Case sensitive," and "Regex" checkboxes using {% kbd ctrl shift 1 %}, {% kbd 2 %} and {% kbd 3 %}, respectively.

### Advanced search ###

You can use wildcards in a non-regex search. `*` will match any series of non-space characters and `?` will match any single character.

Starting a search with a `*` will make it a jQuery selector search. You can use any jQuery selector and all matching elements will be highlighted and navigable with {% kbd cmd G %} and {% kbd shift cmd G %}. To limit the scope of a text search to a certain element type, add the search terms in double quotes after the selector definition:

    *h2 "Alice"

This is the equivalent of `*h2:contains(Alice)`

## Document navigation (TOC, bookmarks, Mini Map)

The [Document Navigation](Document_Navigation.html) page covers the Table of Contents (including opening the filter with {% kbd Space %}), fast search with {% kbd f %}, bookmarks, and the Mini Map.

## Keyboard Navigation

The preview window can be navigated quickly using keyboard shortcuts. Use {% kbd j %} and {% kbd k %} to move up and down, and hold down Shift ({% kbd J %}/{% kbd K %}) to move faster. {% kbd t %} and {% kbd b %} will move to the top and bottom of the document (as will {% kbd gg %} and {% kbd G %}, for Vim fans). {% kbd u %} and {% kbd d %} will move 1/2 page up and down.

### Header jumping

Pressing the comma ({% kbd , %}) and period ({% kbd . %}) keys will jump backward and forward through any headers in the document. Holding down Shift ({% kbd shift  %}) will jump only between level 1 and 2 headers.


## Full-Screen

Full-screen mode can be toggled from the Preview menu or by typing {% kbd ctrl cmd F %}.

## Clicking external links

![][10]

[10]: images/linkpopover.png @2x width=706px height=213px class=center

Clicking an external link in your document's preview will open it in your default browser. If you click and hold, when you release Marked will give you three options: you can copy the link's URL to your clipboard, validate the link, or open the link in your default browser. Just click anywhere in your preview to dismiss the window. This feature can be disabled in the {% prefspane Preview %} ("Enable link popovers").

See an [overview video on YouTube](https://www.youtube.com/watch?v=nrt7YZPrnv0&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=1).

## Collapsible headlines ##

When "Headlines collapse sections" is enabled in the {% prefspane Preview %}, clicking headlines will collapse the section between that headline and the next headline at the same level. Sub-sections within that section are hidden. Optionally, you can limit this behavior to {% kbd cmd %}-clicking.

![][13]

[13]: images/headlines.jpg @2x width=740px height=287px class=center

Holding down {% kbd opt  %} when clicking (or {% kbd cmd %}-clicking) will expand/collapse all of the child sections below the clicked heading. Holding down the {% kbd shift  %} (Shift) key while clicking will collapse all other sections at the same level, revealing only the clicked section.

Collapsed sections are marked with a yellow highlight to the right of the title, and the cursor will indicate what will happen when the item is clicked.

If an edit is made that needs to be visible, or a table of contents section is clicked that is currently within a collapsed section, the necessary parent sections will be expanded to reveal it.

You can collapse/expand all of the sections in a document at once with the "Collapse all sections" ({% kbd opt cmd left  %}) and "Expand all sections" ({% kbd opt cmd right  %}).

See the [Document Navigation video on YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2) for more details.

## Custom Processor indicators/toggles ##

![][indicators]

[indicators]: images/processorindicators.png @2x width=874px height=255px class=center

When the custom processor and/or preprocessor are enabled, indicator lights appear in the toolbar. These can be used to see whether or not the processor is turned on for the current document (indicator will be highlighted) and clicking them will toggle the use of the custom preprocessor and processor, respectively.

## Scroll To Edit

The "scroll to edit" feature in Marked keeps track of differences between the latest update and the last, trying to find the point where you made your most recent changes. Marked always tracks this, and a small red line appears in the preview to show you the location of the first change detected. In the {% prefspane Preview %}, you can turn on "Scroll to first edit" and when a preview updates it will gently scroll the view to that location.

With "Scroll to first edit" turned off, you can still press the "e" key at any time in the preview to go to the last stored edit point.

## Autoscroll

See the dedicated [Autoscroll](Autoscroll.html) page. When using Autoscroll as a teleprompter, [special syntax can insert pauses](Special_Syntax.html#pauses).

## Zoom Overview

See the [Zoom Overview](Zoom_Overview.html) page ({% kbd z %} in the preview; also works in Word Repetition with {% kbd ctrl cmd w %}).

## Markdown Reference

![][11]

   [11]: images/markdown_reference.jpg @2x width=1148px height=267px class=center

Select Markdown Reference from the {% appmenu Help %} menu to display a guide that floats over your other windows. This is handy for those who are still learning Markdown's syntax. You can open this panel via the keyboard using {% kbd opt cmd M %}.

## Global Keyboard Shortcuts

In the {% prefspane General %}, you can designate a custom keyboard shortcut for activating Marked, and one for raising just the front window to the top without leaving your editor.
