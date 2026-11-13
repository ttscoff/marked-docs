# <%= @title %>

Drag a Finis project onto Marked to preview the compiled book. A Finis project is a `.finis` package. Each chapter is a Markdown file, and `.finis/project.json` stores the reading order and compile rules.

## Opening a project [opening-a-project]

Open the `.finis` package itself. Marked compiles the book and shows it in one preview. The window title is the project title, or the package name when the project has no title.

Press **⌘E** to open the project in Finis.

Saving `project.json` or a chapter that is part of the book refreshes the preview.

## What Marked leaves out [what-marked-leaves-out]

Marked follows the compile rules Finis uses for the book:

- Documents and folders that are not included are omitted. Leaving a folder out also omits everything inside it.
- Notes and guide documents are omitted.
- Statuses on the project's exclude list are omitted.
- Items in the Finis trash are omitted.

Marked does not offer a panel for choosing chapters by hand, and it does not apply Finis page size, cover, or media settings. The preview is the compiled Markdown.

## Parts and chapters [parts-and-chapters]

When the project compiles folders as parts, each first-level folder is a part. Its heading is level 1, and each document inside it starts on a new page.

When the project compiles folders as chapters, each first-level folder is a chapter. Documents inside it are scenes and stay on the same page.

If the project does not set a folder mode, Marked uses parts when a first-level folder contains another folder that itself contains included documents. Otherwise it uses chapters. A book made only of documents, with no folders, has no part or chapter headings and no page breaks between those documents.

## Page breaks [page-breaks]

A document set to its own page starts and ends with a page break. Marked removes the first Markdown heading in that document so it is not repeated under the generated title. Setext headings are left as they are.

Adjacent page breaks collapse into one.

## Headings [headings]

Folder headings use the folder name, or the heading text the project sets for that folder. The level starts at 1 and increases by one for each nested folder, stopping at level 6. If the project asks for a warning when a heading is deeper than level 6, the preview still uses level 6 and shows a one-line note.

A document gets a generated heading only when the project asks for document titles, or when that document asks for a heading and the project does not turn document titles off. Marked strips a trailing `.md` only when it uses the file name as a heading. If the file already starts with the same heading, Marked does not add it again.

Numbering applies only to headings Marked inserts. The style follows the project's numbering setting: none, arabic, roman, or words. Labels follow the project's language for English, Italian, French, German, Spanish, and Portuguese. Other languages use English labels and arabic numerals.

## Front matter [front-matter]

When the project includes front matter, Marked adds a MultiMarkdown block with the title, subtitle, author, and language that have values. If the first included document already starts with YAML or MultiMarkdown metadata, Marked leaves that block as it is and does not add another.

## Images [images]

Relative image and link paths are rewritten from the chapter's folder to the project package, so images stored in the project still appear in the joined preview. Web addresses, mail links, and links that start with `#` are left unchanged. A path that would leave the package is left unchanged.
