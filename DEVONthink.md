# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) can open selected Markdown files directly in Marked using an AppleScript.

## Open selected Markdown in Marked

Use this script in DEVONthink to send the current selection to Marked. It checks that you selected something, confirms it is Markdown, then opens it using `x-marked-3://` with a URL-encoded file path.

```applescript
-- Open selected DEVONthink Markdown file in Marked 3

tell application id "DNtp"
	activate
	
	set sel to selection
	if sel is {} then
		display alert "No selection" message "Select a Markdown document in DEVONthink first."
		return
	end if
	
	set theRecord to item 1 of sel
	
	-- Must be a file-backed item
	set p to path of theRecord
	if p is missing value or p is "" then
		display alert "Not a file" message "The selected item does not have a file path."
		return
	end if
	
	-- Check Markdown by extension
	set ext to my lowercaseExtension(p)
	set mdExts to {"md", "markdown", "mdown", "mkd", "mkdn", "mdtxt"}
	if mdExts does not contain ext then
		display alert "Not Markdown" message "Selected item is not a Markdown document."
		return
	end if
end tell

set encodedPath to my urlEncode(p)
set markedURL to "x-marked-3://" & encodedPath
open location markedURL


on lowercaseExtension(posixPath)
	set oldTIDs to AppleScript's text item delimiters
	set AppleScript's text item delimiters to "."
	set parts to text items of posixPath
	set AppleScript's text item delimiters to oldTIDs
	
	if (count of parts) < 2 then return ""
	set ext to item -1 of parts
	return do shell script "printf %s " & quoted form of ext & " | tr '[:upper:]' '[:lower:]'"
end lowercaseExtension

on urlEncode(s)
	-- URL-encode path safely for x-marked-3://
	set py to "import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe='/'))"
	return do shell script "/usr/bin/python3 -c " & quoted form of py & " " & quoted form of s
end urlEncode
```

## Install in DEVONthink Scripts menu

1. Copy the script above into **Script Editor**.
2. Save it as `Open in Marked.scpt`.
3. In DEVONthink, open the **Scripts** menu and choose **Open Scripts Folder**.
4. Move `Open in Marked.scpt` into the `Contextual Menu` folder.
5. In DEVONthink, right-click a file and choose **Scripts -> Open in Marked.scpt**.

I> Marked can also resolve `hook://` assets when enabled in {% prefspane Apps %}; see [Hookmark](Hookmark.html).
