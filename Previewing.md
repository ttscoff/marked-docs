# <%= @title %>

I> This page covers preview *appearance* --- styles, zoom, dark mode, and the status bar. For setting up live preview from your editor, see [Live Markdown Preview on Mac](Live_Markdown_Preview_on_Mac.html).

Changing the way you see things.

## Choosing a style

![][1]

   [1]: images/StylePicker.jpg @2x width=896px height=195px class=center

You can set a default style for new documents in the {% prefspane Style %}. If you have the style menu in the toolbar enabled in Window settings, you can adjust the style on a per-document basis right from the Preview window. Your style selection will be remembered and will be the first choice for export and print options.

Custom styles added in the Style settings will be available in both menus.

Styles can be selected with keyboard shortcuts. Open the style menu to see the keyboard shortcut for each style. Keyboard shortcuts are assigned in Style order: the first 9 styles in the list can be accessed with {% kbd cmd 1 %} -- {% kbd cmd 9 %}, the next 10 styles with {% kbd cmd opt 1 %} -- {% kbd cmd opt 0 %}, etc.

## Outline mode

If your document is a hierarchical list, such as one generated from a mind map or outlining application, you can enable Outline Mode from the Gear menu to apply special formatting in either APA or Decimal outlining style.

Automatic outline mode can be enabled for specific file extensions in the {% prefspane Style %}.

## Text Zoom

![][2]

   [2]: images/textzoom.jpg @2x width=800px height=414px class=center

You can change the text size using {% kbd cmd shift + %} and {% kbd cmd shift - %}, or use the Zoom menu under Preview in the menubar or in the gear menu on the document window. Marked will remember any changes you make for next time (and every time). Reset the zoom to 100% with {% kbd cmd 0 %} (or access **Zoom Reset** from the Zoom menu).

## Dark Mode/High Contrast

If you prefer light text on a dark background, Marked has you covered. In the __Preview__ menu you can use {% appmenu Preview, Dark Mode ({{opt}}{{cmd}}I) %} invert the colors any of the default schemes for a light on dark result, and if a custom theme is [built properly](Writing_Custom_CSS.html) it will work there as well.

## Show/Hide Status Bar

The status bar at the bottom of the preview window can be toggled with the {% appmenu Preview, Show Status Bar ({{ctrl}}/) %} menu item. When it's hidden, it can be viewed and interacted with by hovering over the space at the bottom of the preview.
