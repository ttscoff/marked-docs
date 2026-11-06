<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

把一份 skill 檔案交給 LLM 代理，它就可以在 Marked 中開啟檔案和檔案夾、跳到設定的某個部分，並更改偏好設定。代理使用 Marked 的 [URL Handler](URL_Handler.md)。不需要另外的外掛或伺服器。

## 下載 skill [download-the-skill]

{% download "SKILL.md" "供代理在 Marked 中開啟檔案並更改偏好設定的 skill。請儲存為 SKILL.md。" %}

這個檔案是純 Markdown，開頭有一小段代理在行動前會閱讀的說明。任何接受 skill 或常駐指示的代理都可以使用同一份檔案。

## 安裝 [install-it]

把檔案放進一個以該 skill 命名的檔案夾，並保持檔名為 `SKILL.md`。

在 Cursor 中，下面兩個位置都可以：

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

第一個對所有專案可用。第二個只用於該專案。如果其他代理沒有 skill 檔案夾，可以把同一段文字當作專案指示。

安裝之後，請代理在 Marked 中開啟一個檔案或檔案夾。它應當執行類似這樣的指令：

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

檔案夾使用同一條指令。路徑必須已經存在，空格和其他保留字元必須百分號編碼。完整方案，包括 refresh、Streaming Preview 和回呼，見 [URL Handler](URL_Handler.md)。

## 偏好設定 [preferences]

這份 skill 還說明了兩條偏好設定指令：

`pref`
: 開啟設定中指定名稱的部分。URL 裡的名稱保持英文，例如 `Preview` 或 `Style`。它不會更改任何值。

`defaults`
: 寫入 Marked 已經儲存的一項偏好設定，然後重新載入開啟的預覽。傳入 `refresh=0` 可以不重新整理預覽。代理在寫入之前應當先讀取目前的偏好設定，因為未知的鍵會被忽略。

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## 相關內容 [related]

[Using Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.md) 說明如何在代理撰寫計畫和筆記時監看那個檔案夾。[Command Line Utility](Command_Line_Utility.md) 是從 shell 進行的同類操作，不經過代理。
