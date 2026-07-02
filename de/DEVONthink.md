# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) kann ausgewählte Markdown-Dateien mithilfe eines AppleScript direkt in Marked öffnen.

## Ausgewähltes Markdown in Marked öffnen

Verwenden Sie dieses Skript in DEVONthink, um die aktuelle Auswahl an Marked zu senden. Es prüft, ob etwas ausgewählt ist, bestätigt, dass es sich um Markdown handelt, und öffnet die Datei dann über `x-marked-3://` mit URL-codiertem Dateipfad.

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

## Im DEVONthink-Skriptmenü installieren

1. Kopieren Sie das obige Skript in den **Skript-Editor**.
2. Speichern Sie es als `Open in Marked.scpt`.
3. Öffnen Sie in DEVONthink das Menü **Skripte** und wählen Sie **Skriptordner öffnen**.
4. Verschieben Sie `Open in Marked.scpt` in den Ordner `Contextual Menu`.
5. Klicken Sie in DEVONthink mit der rechten Maustaste auf eine Datei und wählen Sie **Skripte -> In Marked.scpt öffnen**.

I> Marked kann auch `hook://`-Assets auflösen, wenn dies in {% prefspane Apps %} aktiviert ist; siehe [Hookmark](Hookmark.html).
