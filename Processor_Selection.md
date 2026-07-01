# <%= @title %>

## Processor selection

[MultiMarkdown](http://fletcherpenney.net/multimarkdown/ "MultiMarkdown") (by Fletcher Penney) is an extension of [Markdown](http://daringfireball.net/projects/markdown/ "Daring Fireball: Markdown") (by John Gruber). All standard Markdown formatting is observed, and MultiMarkdown provides additional syntaxes for elements such as tables and footnotes.

## Syntax

There's a Markdown Syntax guide under the help menu, or you can refer to [John Gruber's original documentation](http://daringfireball.net/projects/markdown/syntax).

MultiMarkdown extensions are documented by Fletcher Penney in [this document](https://github.com/fletcher/MultiMarkdown/blob/master/Documentation/MultiMarkdown%20User%27s%20Guide.md).

## Alternative rendering

You can choose between MultiMarkdown, Kramdown, CommonaMark, and Discount in the {% prefspane Processor %}. Each offers additional features with a slightly different syntax (see {% appmenu Help, Markdown Reference %} for more details). In most cases, MultiMarkdown is preferred, but if you have files already using processor-specific syntax or you run into trouble rendering a Markdown file with MultiMarkdown, select Commonmark as your default processor.
