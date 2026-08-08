<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[DEVONthink](https://www.devontechnologies.com/apps/devonthink) は、AppleScript を使用して、選択した Markdown ファイルを Marked で直接開くことができます。

## 選択したマークダウンをマークで開く [open-selected-markdown-in-marked]

DEVONthink でこのスクリプトを使用して、現在の選択内容を Marked に送信します。何かが選択されていることを確認し、それが Markdown であることを確認してから、URL エンコードされたファイル パスを指定した `x-marked-3://` を使用してそのファイルを開きます。

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

## DEVONthink Scripts メニューにインストール [install-in-devonthink-scripts-menu]

1. 上記のスクリプトを **スクリプト エディタ** にコピーします。
2. `Open in Marked.scpt` として保存します。
3. DEVONthink で、**スクリプト** メニューを開き、**スクリプト フォルダーを開く** を選択します。
4. `Open in Marked.scpt` を `Contextual Menu` フォルダーに移動します。
5. DEVONthink で、ファイルを右クリックし、**スクリプト -> Marked.scpt で開く** を選択します。

I> Marked は、{% prefspane Apps %} で有効になっている場合、`hook://` アセットも解決できます。 [フックマーク](Hookmark.html)を参照してください。