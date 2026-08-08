# <%= @title %>

Marked has special handling for comments and annotations.

## Annotation sources [annotation-sources]

Marked recognizes comments coming from:

- Markdown Footnotes
- CriticMarkup comments
- Microsoft Word comments and changes

## The Comments sidebar [the-comments-sidebar]

All annotations are shown in a sidebar and hidden in the document preview. To show the annotations sidebar, use the **Gear Menu -> Proofing -> Show Comments**, or press {% kbd ctrl cmd C %}.

![A footnote in the Comments  Sidebar][sidebar]

  [sidebar]: images/comment-sidebar-800.jpg @2x width=800

Hovering over a comment in the sidebar will draw a line to its location in the document. In the case of footnotes, this will point to where the footnote occurs in the text. In the case of comments, it will point to the original location of the comment, which may be blank space in the preview.

Clicking a comment in the sidebar will draw a highlighted animation pointing to its location.

The font and style of the sidebar is dependent on the current Style, so it may look different with different Styles.