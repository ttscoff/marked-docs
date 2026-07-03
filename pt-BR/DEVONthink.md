<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) pode abrir arquivos Markdown selecionados diretamente no Marked usando um AppleScript.

## Abra Markdown selecionado em Marcado

Use este script no DEVONthink para enviar a seleção atual para Marked. Ele verifica se você selecionou algo, confirma que é Markdown e abre usando `x-marked-3://` com um caminho de arquivo codificado em URL.

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

## Instalar no menu DEVONthink Scripts

1. Copie o script acima no **Editor de Scripts**.
2. Salve como `Open in Marked.scpt`.
3. No DEVONthink, abra o menu **Scripts** e escolha **Abrir pasta de scripts**.
4. Mova `Open in Marked.scpt` para a pasta `Contextual Menu`.
5. No DEVONthink, clique com o botão direito em um arquivo e escolha **Scripts -> Abrir em Marked.scpt**.

I> Marcado também pode resolver ativos `hook://` quando habilitado em {% prefspane Apps %}; veja [Marcador](Hookmark.html).