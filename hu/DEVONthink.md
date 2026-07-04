<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A [DEVONthink](https://www.devontechnologies.com/apps/devonthink) AppleScript segítségével közvetlenül megnyithatja a kiválasztott Markdown fájlokat a Marked alkalmazásban.

## Nyissa meg a kijelölt Markdown-t a Jelölve

Használja ezt a szkriptet a DEVONthinkben, hogy elküldje az aktuális kijelölést a Marked-nek. Ellenőrzi, hogy kiválasztottál-e valamit, megerősíti, hogy az Markdown, majd megnyitja a `x-marked-3://` használatával egy URL-kódolt fájlútvonallal.

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

## Telepítés a DEVONthink Scripts menüben

1. Másolja a fenti szkriptet a **Script Editor**-ba.
2. Mentse el `Open in Marked.scpt` néven.
3. A DEVONthink programban nyissa meg a **Scripts** menüt, és válassza az **Open Scripts Folder** lehetőséget.
4. Helyezze át a `Open in Marked.scpt` elemet az `Contextual Menu` mappába.
5. A DEVONthink programban kattintson jobb gombbal egy fájlra, és válassza a **Scripts -> Open in Marked.scpt** menüpontot.

Az I> Megjelölve a `hook://` eszközöket is fel tudja oldani, ha engedélyezve van a {% prefspane Apps %}-ben; lásd: [Hookmark](Hookmark.html).