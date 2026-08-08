# <%= @title %>

## AppleScript [applescript]

Marked includes a full [AppleScript dictionary](AppleScript_Support.html) for opening files, controlling the preview (reload, scroll, highlights, autoscroll, speed read), reading statistics, setting processors, copying HTML or RTF, changing preview styles, and exporting to Markdown, HTML, PDF, EPUB, DOCX, ODT, TextBundle, RTF, and OPML. **Preview headings / table of contents** via AppleScript is [documented as work in progress](AppleScript_Support.html#table-of-contents-work-in-progress) and is not reliable yet.

You can target the application, a specific window, or a document. Application commands include **open streaming preview**, **preview clipboard**, and **close all**. Document commands include **get statistics** and **print with profile**. Export commands accept an optional export **profile** or a **`with`** record for options such as preview **style**, **pageSize**, and **margins**. For example:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

See [AppleScript Support](AppleScript_Support.html) for the command list, margin shorthand, sandbox notes, and debugging tips.

The AppleScript integration also allows applications such as Tags.app to function directly within Marked.

## URL Handler [url-handler]

The [Marked URL handler][urlhandler] allows extensive integration simply by calling URLs, either from AppleScript or with a basic `open` command in a shell script.

## Marked Bonus Pack [marked-bonus-pack]

The Marked Bonus Pack is a collection of scripts, commands and services. Some work with multiple editors, some are specific to certain editors. The Services will generally work with any editor that has the necessary capabilities. The rest are organized in folders based on the application they work with.

You can download the Bonus Pack and find instructions for installing and using it in this [knowledge base article](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles).

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html

