# <%= @title %>

View your documents *your* way.

## Using custom styles [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

The easiest way to explore Custom Styles is through the
[Custom Style Gallery][2]. From there you can browse the
available styles in action, install them with the click of a
button, and even [submit your own creations][6] for
inclusion.

To add custom stylesheets from your local drive to Marked,
use the {% prefspane Style %}. New styles will be added to
the dropdown menus in Window settings and on each window,
and will be named based on the base filename of the CSS file
added. Store your custom CSS files in a safe place on your
drive. If they move on your drive, they'll be removed from
Marked until you add them again from the new location. It's
a good idea to close open documents and remove the style
from Settings before deleting or renaming a CSS file used by
Marked. It won't break anything if you don't, but it saves
some confusion.

Add Custom Styles using the Style Manager with the Add Button, or by dragging one or more CSS files onto the Settings
pane.

## Managing styles with the Style Manager [managing-styles-with-the-style-manager]

Launching the Style Manager gives you a single place to curate every built‑in
and custom theme. Click the **Manage Styles…** button in the {% prefspane Style %}
pane,
or simply drop CSS files onto the preferences window --- Marked will import them,
open the Style Manager, and select the newly added row for you. Dragging CSS
files directly onto the Style Manager window works as well; when multiple files
are dragged you'll see the overlay update to "Add N Custom Styles" so it's clear
you're importing a batch.

![][img-style-manager]

Inside the Style Manager you'll find a sortable table that mixes built‑in and
custom styles. Each row offers:

- An **Enabled** checkbox that immediately adds/removes the style from the Style
  menu, Default Style popup, and keyboard shortcuts. Disabling the currently
  active style automatically switches to the next available entry.
- A **Name** column you can edit inline; changes persist and propagate to every
  menu. Click on the Style's name to edit it in place.
- A **Source** column that calls out Built‑in, Custom, or Duplicated.
- An **Actions** stack with buttons to **Edit** (opens the CSS file in your
  editor), **Duplicate** (creates a copy and a new CSS file on disk), **Reveal**
  (shows the file in Finder), and **Delete** (with options to remove the reference or
  move the CSS file to the Trash).

Rows reorder via drag and drop, and the order drives the Style menu as well as
the `⌘/#` shortcut assignments, so you can literally drag styles into the slots
you want. You can also drag external CSS files into specific positions; the drop
indicator determines where the new style is inserted.

### Live preview [live-preview]

The right pane holds a preview that renders the selected style
inside a full HTML document with a comprehensive set of headings, lists, tables, code blocks, etc. The
preview uses the actual CSS on disk, so edits you make in your external editor update instantly. A checkbox toggles Dark Mode preview.

You can find additional styles for use (or as examples for
creating your own) [on GitHub][1] (see the [examples][2] for
a quick peek at what's there). See [Creating Custom CSS][3]
for details and tips.

## Additional CSS [additional-css]

Under the {% prefspane Style %}, you'll find an option
titled Additional CSS with a button labeled "Edit CSS."
Clicking this button opens a window where you can add
universal CSS rules that will be applied to all styles. Note
that specificity of the rules can be important when
overriding some of Marked's default styling. The main body
of the document is wrapped in a div with the id "#wrapper".
Prefixing a selector with this can allow for easier
overrides, e.g.:

    #wrapper img { width: 100%; height: auto; }

CSS in this field will be applied to every document, no
matter what Style it"s using. If you want to apply custom
CSS based on conditional matches, use the Set Style, Insert
CSS File, or Insert CSS actions in {% prefspane Processor %}
Custom Rules.

## Print and PDF export [print-and-pdf-export]

Marked injects a built-in `@media print` block (`mkprintstyles`) on every
preview. It sets defaults such as a **10pt** base on `html`, `body`, and
`#wrapper` (or the size from **Custom font size for export/print** in
{% prefspane Export %} when that option is enabled), and normalizes paragraph
text with `p { font-size: 1em; }` and `li p { font-size: 1em; }` so
screen-only rules like `p { font-size: 1.1429em; }` do not inflate body copy
in PDFs and printed output.

PDF export may use **print** or **screen** media on the hidden WebView used for
generation. Built-in themes typically use print media; **custom styles** and
[Fountain](Fountain_for_Screenwriters.html) documents often use screen media so
layout matches the preview. That means `@media print { ... }` rules are not
always applied during PDF export.

For reliable PDF and Print/PDF Preview styling, prefix selectors with the
`mkprinting` class Marked adds to `<body>` during export (see [Writing Custom
CSS](Writing_Custom_CSS.html#printstyles) for details and examples). You can use
`.mkprinting` alone, or combine it with `@media print` when you need both paths
covered.

To set sizes that differ from Marked's print defaults, add explicit rules in
your custom CSS (or in Additional CSS). Use `!important` when you need to
override Marked's injected print styles --- for example:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}
```

Rules without `!important` may lose to later rules in `mkprintstyles` or to
other unqualified selectors in your sheet that still apply in print. Putting
print-only tweaks in `@media print` and/or `.mkprinting` rules (rather than
only in screen rules) keeps the preview and export behavior easier to reason
about.

## Watching CSS changes [watching-css-changes]

You can check a box in the Custom Styles section of the {% prefspane Style %}
to have Marked watch the active CSS file
in addition to the Markdown file you're editing. When
changes are detected on either file, the preview will
update. This is useful for editing custom styles without
constantly refreshing and can also be used for simple web
development tasks.

This is also useful for some basic web design work and CSS
experimentation (like creating custom styles). Load a
Markdown file containing all the markup you want to style
for, create a custom style, and watch the preview for live
changes as you edit it.

## Writing custom CSS [writing-custom-css]

If you're familiar with CSS, you can create your own style
sheets for use in Marked. See [Writing Custom CSS][3] for
details. Any time you create something new, consider
[submitting it][6] to the [gallery][2] to share with other
users. Be sure to cover the basics listed in the guide, and
include the metadata comment at the top.

### Automatic Custom Styles with StyleStealer [automatic-custom-styles-with-stylestealer]

You can even automatically generate a style based on an
existing website using the [Style Stealer][4]. This allows you to load a web page and grab the calculated styles for all major elements found in Markdown, then save it to a custom style.

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


Manage Custom Styles (rename, re-order, duplicate, and delete) from the [Style Manager](Style_Manager.html).

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center

