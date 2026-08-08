# <%= @title %>

This page describes how to move around long previews: the [Table of Contents](#table-of-contents), [fast search](#fast-search), [bookmarks](#bookmarks-and-mini-map), and the [Mini Map](#minimap). For scrolling shortcuts that apply everywhere (such as {% kbd j %}/{% kbd k %}), see [Keyboard Navigation](Interface_Features.html#keyboardnavigation) under [Interface Features](Interface_Features.html).

## Table of Contents [table-of-contents]

![][8]

   [8]: images/tableofcontentsbutton.jpg @2x width=740px height=238px class=center

If your document has headers in it, a list button appears in the toolbar. Click it to expand the Table of Contents; click a headline to jump to that section of the preview. Use {% kbd j %}/{% kbd k %} (down/up) to move through the list, and {% kbd Enter %} or {% kbd o %} to jump to the highlighted header.

**Filter bar:** With the Table of Contents open, press {% kbd Space %} (Space bar) to open the type-ahead field. Type any part of a headline name (Marked uses TextMate-style matching&#8212;for example you can type the first letter of each word) and press Tab ({% kbd ⇥ %}) or the Down Arrow ({% kbd ↓ %}) to move through the filtered list.

Pressing {% kbd cmd T %} also opens (or closes) the Table of Contents.

If ["Headlines Collapse Sections"](Interface_Features.html#collapsibleheadlines) is enabled in the {% prefspane General %}, holding the Command key while clicking an item in the Table of Contents will collapse or expand that section, revealing parent sections as necessary.

When in full-screen mode, the table of contents appears as a fixed side bar instead of a popup menu. To use that layout in a regular windowed preview, use the full-screen toggle in the lower-right of the TOC panel.

![Toggle Full Screen][12]

   [12]: images/tableofcontentsfullscreentoggle.jpg @2x width=740px height=238px class=center


For a condensed list of keys, see [Keyboard Shortcuts](Keyboard_Shortcuts.html#TableofContentsNavigation).

See also the [Document Navigation video on YouTube](https://www.youtube.com/watch?v=Z2p5BvBpbmA&list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ&index=2).

### Full-screen mode for the Table of Contents [full-screen-mode-for-the-table-of-contents]

When a Marked preview window is full screen, the Table of Contents can stay fixed on the left for constant navigation. It still toggles with {% kbd cmd T %}; clicking outside the TOC often will not dismiss it while in this layout.

In a normal window, click the icon at the bottom of the TOC panel to dock it as a sidebar; click the icon at the top of the sidebar to return it to popup mode.

### Customizing where the TOC appears [customizing-where-the-toc-appears]

The Table of Contents can be injected in the exported document using the [special syntax](Special_Syntax.html#tableofcontents) `<!--TOC-->`.

Add `max#` (for example `<!--TOC max2-->`) to limit how many heading levels appear.

## Fast search [fast-search]

**Fast navigation** combines the Table of Contents with the filter focused so you can jump with minimal typing:

- Press {% kbd f %} in the preview to open the TOC with the **filter field focused** (same idea as opening the TOC and then pressing {% kbd Space %}, without the extra step).
- Type part of any headline title; the list filters to matches.
- If only one headline remains, pressing Return ({% kbd ↩ %}) jumps straight to it.
- If multiple headlines remain, press Tab ({% kbd ⇥ %}) to leave the filter field, move with {% kbd j %}/{% kbd k %} or the arrow keys, then press {% kbd o %} or Return ({% kbd ↩ %}) to go to the headline and close the TOC.
- Tab again returns focus to the search field.

> **Shortcut reminder:** Opening the TOC and pressing {% kbd Space %} opens the filter bar&#8212;handy whenever the TOC is already visible.

(Earlier docs referred to this as "Fast Switcher"; it is the same feature.)

## Bookmarks and Mini Map [bookmarks-and-mini-map]

Use the {% appmenu Gear %} preview menu and {% kbd Tab %} ({% kbd ⇥ %}) focusing the document alongside [search](Interface_Features.html#search) to place and revisit bookmarks while you skim.

### Setting bookmarks [setting-bookmarks]

Set bookmarks on scroll position using {% kbd shift 1 %}--{% kbd shift 9 %} and jump back using {% kbd 1 %}--{% kbd 9 %} alone. Use {% kbd n %} and {% kbd p %} for next/previous in **document order**; {% kbd shift n %} and {% kbd shift p %} for next/previous in **numeric** order.

Changing the Style or page size can move where a bookmark appears. Bookmarks are meant as temporary review aids: they do not persist between document sessions, but they do survive preview refreshes and edits.

**Headline bookmarks:** Hold Option and press {% kbd opt 1 %}--{% kbd opt 9 %} to bookmark the headline nearest the top of the viewport (or the last headline before the top).

**Next free slot:** {% kbd cmd D %} (or backtick {% kbd \`\` %}, for vim users) adds a bookmark in the next available numbered slot.

Press {% kbd 0 %} to expand the bookmark strip (headline titles where available). When the [Mini Map](#minimap) is enabled, {% kbd 0 %} shows it at the same time. Press Escape or {% kbd 0 %} again to collapse.

Press {% kbd x %} twice ({% kbd xx %}) to clear all bookmarks.

There are [more preview shortcuts](Keyboard_Shortcuts.html); press {% kbd h %} in the preview for a heads-up list, or {% kbd opt cmd K %} for the full reference.

### Mini Map [minimap]

If the Mini Map is enabled in the {% prefspane Preview %} settings, {% kbd 0 %} opens a scaled thumbnail of the whole document along the bookmarks strip. Click anywhere on the map to scroll the full preview there. Saved bookmarks appear as horizontal lines with numbers (and headings when relevant).

Hold **Command** and move over the Mini Map for a magnified loupe; hold **Option** and drag to scroll as if dragging the scrollbar.

The map regenerates when the window size or layout changes. On very long documents, pressing {% kbd 0 %} once may take a moment; Marked avoids building the Mini Map automatically on initial load until you request it.

Press {% kbd 0 %} or Escape to close the Mini Map.

**Performance note:** Generating the map can briefly pause the preview on huge documents; this only runs when the map is visible or after a resize.

### Zoom overview (related) [zoom-overview-related]

For a text-scale overview without the Mini Map, see [Zoom Overview](Zoom_Overview.html) ({% kbd z %}).
