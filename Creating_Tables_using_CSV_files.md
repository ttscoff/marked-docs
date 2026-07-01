# <%= @title %>

If a file included via [Marked's include syntax or IA Writer block syntax][include] has a CSV or TSV extension, Marked will attempt to parse it and convert it to a MultiMarkdown table. This works with most standard formats, including comma and tab-separated, as well as additional separators and quoting formats which are automatically detected.

One benefit of using CSV files instead of writing Markdown tables is that line breaks within cells are automatically converted to `<br>` tags. This has to be done manually to include line breaks when writing MultiMarkdown tables, so it's an additional time-saver.

As a side note, there's an excellent app called [TableFlip][] that makes editing tables within your document much easier. It's worth checking out if you frequently work with tabular data.

Included CSV files will be watched for changes, so additional editing can be done in the original CSV file and Marked will automatically update the preview on save.

Converted tables will be included in Markdown export, so Marked can be used to compile documents containing structured data and export a single file.

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/
