<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) può aprire i file Markdown selezionati direttamente in Marked utilizzando un AppleScript.

## Apri Markdown selezionato in Contrassegnato [open-selected-markdown-in-marked]

Utilizza questo script in DEVONthink per inviare la selezione corrente a Marked. Verifica che tu abbia selezionato qualcosa, conferma che è Markdown, quindi lo apre utilizzando `x-marked-3://` con un percorso file con codifica URL.

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

## Installa nel menu DEVONthink Scripts [install-in-devonthink-scripts-menu]

1. Copia lo script sopra in **Script Editor**.
2. Salvalo come `Open in Marked.scpt`.
3. In DEVONthink, apri il menu **Script** e scegli **Apri cartella script**.
4. Sposta `Open in Marked.scpt` nella cartella `Contextual Menu`.
5. In DEVONthink, fare clic con il pulsante destro del mouse su un file e scegliere **Script -> Apri in Marked.scpt**.

I> Marked può anche risolvere `hook://` asset se abilitato in {% prefspane Apps %}; vedere [Segno](Hookmark.html).