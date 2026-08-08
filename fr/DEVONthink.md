# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) peut ouvrir les fichiers Markdown sélectionnés directement dans Marked à l'aide d'un AppleScript.

## Ouvrir le Markdown sélectionné dans Marked [open-selected-markdown-in-marked]

Utilisez ce script dans DEVONthink pour envoyer la sélection actuelle à Marked. Il vérifie que vous avez sélectionné quelque chose, confirme qu'il s'agit de Markdown, puis l'ouvre en utilisant `x-marked-3://` avec un chemin de fichier codé en URL.

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

## Installer dans le menu DEVONthink Scripts [install-in-devonthink-scripts-menu]

1. Copiez le script ci-dessus dans **Éditeur de script**.
2. Enregistrez-le sous `Open in Marked.scpt`.
3. Dans DEVONthink, ouvrez le menu **Scripts** et choisissez **Ouvrir le dossier des scripts**.
4. Déplacez `Open in Marked.scpt` dans le dossier `Contextual Menu`.
5. Dans DEVONthink, cliquez avec le bouton droit sur un fichier et choisissez **Scripts -> Ouvrir dans Marked.scpt**.

I> Marked peut également résoudre les liens `hook://` actifs lorsqu'il est activé dans {% prefspane Apps %} ; voir [Hookmark](Hookmark.html).
