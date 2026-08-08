# <%= @title %>

Marked has a built-in style editor, and can apply custom CSS files.

You can use the editor to create beautiful styles, or if you know just enough CSS to be dangerous, you can make Marked look however you like.

## Getting started [getting-started]

There"s a gallery of Custom Styles created by the developer and by users at [markedapp.com/styles](https://markedapp.com/styles/). The gallery allows you to preview and install Styles directly in Marked. Any installed Style can be revealed in Finder for examination and modification. The gallery can be opened using an internal viewer with {% appmenu Style, Generate a Custom Style %}, or click the pencil (edit) icon next to any editable style in the Style Manager. If you want to edit a built-in style, you'll first need to duplicate it in the manager.

There's also a [repository for Custom Styles](https://github.com/ttscoff/MarkedCustomStyles) on GitHub with examples. Feel free to browse, use, and contribute there. If you distribute your theme based on one of the base themes, please feel free to add yourself to the credits as a contributor.

With Marked's ability to use custom CSS files, the sky's the limit when customizing your Preview. All CSS3 options that work in Safari will work in Marked. With default Markdown files in Marked there are only a few HTML elements you need to handle; all of the content is in a div with the id of "wrapper", everything else is determined by your document markup.

If you're designing for personal use, there are no rules. Turn on CSS tracking with the checkbox below the custom CSS selector and when you edit and save your custom CSS, it will update the preview.

**A [skeleton theme is available](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) for getting started.**

If you're planning to share your CSS creation, there are a few points you need to cover. First, there are some body classes that need to have styles applied:

## Body classes [body-classes]

The following styles must be included in any Marked CSS to be shared. The body classes allow you to target and modify any selector under different preference options.

### Inverted [inverted]

 When the user selects {% appmenu Preview, Dark Mode %}, a class of "inverted" is added to the body tag. You can use this to target the high-contrast, light on dark styles.

You only want inverted styles to apply to the preview, not to print, so use a media query (@media screen) to restrict it. The code below is fairly all-purpose and in most cases you can just drop it into your stylesheet for compatibility, but feel free to tweak it.

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### Poetry [poetry]

The user can choose whether tab-indented text is poetry or code. The only difference is that pre/code blocks are styled more, um, poetically if poetry mode is chosen. The "poetry" class is applied to the body tag.

Get as creative as you like with the formatting, but here's a basic snippet:

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## Special cases [special-cases]

Tables, Figure/Figcaption, and the special case of `a.footnote` and `div.footnotes>a` also need to be considered. There are no set rules on how you handle them, but take a look at the default styles to get an idea what CSS rules Marked needs.

The standard table styling across all of the default styles uses transparency on the alternating rows to make it blend softly with any background. You can copy those styles, or go your own route, just make sure you've styled them! Same for figure and figcaption; add an image to a document with alt text to see how the markup will come out and style appropriately.

Footnotes included in a document will render a link within the content (a.footnote), and a div at the end with the referenced text (div.footnotes). Again, see the default styles for reference. To avoid changing the line height on lines containing a footnote reference number, be sure to include something like:

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

To keep the return arrow on the same line, include:

```css
.footnotes p {display:inline}
```

It's also a good idea to include a general rule for all images to keep them within the width of the page. Something like:

```css
#wrapper img { max-width: 100% }
```

If your theme has additional padding or a fixed width, modify the max-width to fit.

## Print styles [printstyles]

Be sure to include print styles that remove any background colors, fixed scrolling, and preview-only UI. Marked gives you two ways to target print and PDF output.

### `@media print` [media-print]

Standard CSS print rules apply when printing from Marked or when PDF export uses print media:

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### The `.mkprinting` class [the-mkprinting-class]

When Marked prepares a document for **PDF export** or **Print/PDF Preview** ({% kbd cmd P %}), it adds the class `mkprinting` to the `<body>` tag (alongside export classes such as `bandw`, `breakAfterTOC`, and your style's `mkstyle--*` class). Marked's built-in themes use this class for most print-specific rules instead of relying on `@media print` alone.

PDF export often loads the hidden rendering WebView with **screen** media (especially for custom styles and [Fountain](Fountain_for_Screenwriters.html) documents), so `@media print` blocks in your stylesheet may **not** apply to PDF output. Rules prefixed with `.mkprinting` always apply during export because they are ordinary class selectors, not media queries.

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

For styles that must work in **both** browser printing and Marked PDF export, duplicate critical rules or combine selectors:

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

When debugging custom print CSS, open Print/PDF Preview or export to PDF, then use [Safari's Web Inspector](#webkitinspector) to inspect the document --- the `<body>` will have the `mkprinting` class while print layout is active.

Link-hiding in print is handled outside of the main theme, allowing users to choose to have link highlights and underlines hidden in printout. As long as you have a base style set for the text, you don't need to worry about this.

So, have at it. Convert your blog theme, create a killer print style for PDF documents, or craft the perfect preview for the style of writing you do. If you make something awesome, [share it with the community](https://markedapp.com/styleshare/).

## Additional CSS Settings [additional-css-settings]

In the {% prefspane Style %}, you can edit additional CSS. These styles will be appended to any theme loaded, and can be used to make universal changes to all themes.

Using [high specificity](#overridingspecificity), `@media` queries for print and screen, and `.mkprinting` selectors for PDF export, you can control just about every styling aspect with a bit of CSS knowledge.

## WebKit Inspector [webkitinspector]

Safari's Web Inspector is the easiest way to see exactly what HTML and CSS Marked is generating, and to experiment with Custom Styles live.

### Enabling the Develop menu in Safari [enabling-the-develop-menu-in-safari]

1. Open Safari and choose {% appmenu Safari, Settings… %}.
2. Select the **Advanced** tab.
3. Enable **Show features for web developers** (or **Show Develop menu in menu bar** on older macOS versions).

Once enabled, a **Develop** menu will appear in Safari's menu bar.

![Safari Develop menu showing Marked documents][develop-menu]

### Inspecting a Marked document [inspecting-a-marked-document]

1. With a preview window open in Marked, switch to Safari.
2. From the menu bar, choose **Develop → _\<your Mac name\>_ → Marked → _\<document title\>_**.
3. Safari will open a Web Inspector window attached to the selected Marked preview.

From here you can:

- Use the **Elements** tab to inspect the DOM inside the `#wrapper` div and see which CSS rules are applied.
- Hover elements in the DOM tree to highlight them in the Marked window.
- Use the **Styles** sidebar to tweak rules live, then copy working snippets back into a Custom Style or **Additional CSS**.
    - After editing CSS in the Elements tab, you can get a summary of your edits by selecting the Changes tab

	![Changes][css-changes]
- Use the **Console** tab to run JavaScript against the live preview. The full [Marked JavaScript API](https://markedapp.com/help/jsapi/) is available in this console.
- Explore other tabs such as **Network** when debugging resources loaded by your document.

![Inspecting a Marked preview with Safari Web Inspector][inspecting]

## Sharing Custom CSS [sharing-custom-css]

Use {% appmenu Style, Share a Custom Style %} to open the sharing app in your web browser. Drag your CSS to the drop zone (or click to select from disk) and upload the CSS for your Custom Style.

Shared styles have to be approved by the developer before to they show up in the gallery, so you won't see immediate results.

## Other tips [other-tips]

### Overriding specificity [overridingspecificity]

Within the Marked preview, a body class based on the filename of the current style is added. If the preview is set to "Swiss", then there will be a class on the `<body>` tag called `mkstyle--swiss`. If your custom CSS is called MyCustom.css, then the body class will be `mkstyle--mycustom`. You can use this before rules defined in the base styles to override them. To get absolute specificity in a rule, use the #wrapper ID from the container div as well:

	.mkstyle--mycustom #wrapper p+p { ... }

### Table of contents styling [table-of-contents-styling]

If you use the `<!--toc-->` token to [insert a table of contents](Special_Syntax.html#tableofcontents), you can override the settings for Table of Contents level indicators in a Custom Style using the "#wrapper" to increase specificity:

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

This would make all of the list items in the Table of Contents use a square bullet instead of what was defined in Settings when your Custom Style is active.

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
