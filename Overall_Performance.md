# <%= @title %>

Marked's overall rendering speed and performance can vary greatly based on your settings and the type of content you have in your document. There are several factors that can lead to slow rendering or long delays:

* **Time Machine.** If Time Machine is running and your system is experiencing a lot of disk activity, you may find Marked is slower to respond to changes in your document. The processing speed is not affected, just the reaction time.
* **Rendering a Markdown document containing a lot of HTML.** This will always take longer to process. Discount handles it a little better than MultiMarkdown, so if this is a necessity you might consider changing the default processor (**Caveat:** you'll lose footnotes and some other MultiMarkdown features).
* **Using many includes.** Whether it's code includes or an index merge file, picking up all the pieces takes Marked a second. The same is true of large Scrivener documents. There's not a lot you can do to fix this one, Marked will just do its best to keep up with the way you choose to structure your document.
* **Hard drive condition.** If your hard drive is almost full, your Spotlight index is corrupt or your permissions haven't been repaired in a while, Marked may have a harder time picking up the changes to the file it's watching. Optimizing your drive by repairing permissions will often help, and rebuilding the Spotlight index is often a fix for Marked issues.
