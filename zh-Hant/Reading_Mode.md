<!-- MT draft for zh-Hant — Reading Mode help. Review before publishing. -->
# <%= @title %>

閱讀模式可以保留您在長文件中的位置，聚焦當前區塊，並讓您保存持久的亮點。

## 進入閱讀模式 [entering-reading-mode]

選擇{% appmenu Preview, Reading Mode %}或按{% kbd ctrl opt r %}。如果快速閱讀正在運行，Marked 在進入閱讀模式之前將其停止。

目前段落、標題、清單項目、圖像、程式碼區塊、表格或其他閱讀單元接收左標記。鍵盤導航在區塊之間平滑移動，並將目前單元保持在預覽的上三分之一附近。手動捲動可重新定位焦點，而無需捕捉頁面。

## 導航和恢復 [navigation-and-resume]

當閱讀模式處於活動狀態時：

- {% kbd j %} 或{% kbd down %}：移至下一個讀取單元。
- {% kbd k %}或{% kbd up %}：移至上一個讀取單元。
- {% kbd h %}：反白顯示所選內容，或在未選取文字時切換目前單位的反白顯示。

Marked 儲存每個文件的目前閱讀位置。當儲存的位置與目前視圖不同時，進入閱讀模式有兩種選擇：

- **恢復** 返回已儲存的閱讀位置。
- **從這裡開始** 使用預覽中目前可見的閱讀單元。

## 專注模式 [focus-mode]

點擊預覽頂部的“聚焦模式”工具可以使除當前閱讀單位之外的每個區塊變暗。導航時，焦點模式會跟隨目前單位。再次按一下該工具可恢復其他區塊，或離開閱讀模式以自動清除焦點模式。

## 建立和編輯亮點 [creating-and-editing-highlights]

選擇文字並按 {% kbd h %} 建立內嵌標記突出顯示。在沒有選擇的情況下，按 {% kbd h %} 突出顯示整個當前讀數單位，或再次按下以刪除該單位突出顯示。第一個反白顯示提示輸入簽名，Marked 在建立 CriticMarkup 時使用該簽名。您可以在{% prefspane Preview %}中更改簽名。

### 選擇彈出視窗

選擇文字以顯示選擇彈出窗口，其中圖示按鈕位於行中央：

- **螢光筆** 建立內嵌反白（或 **X** 在自動反白開啟時刪除最後一個自動反白顯示）。
- **註釋** 開啟一個對話方塊來新增或編輯反白的註釋。如果所選內容尚未反白顯示，Marked 首先突出顯示它。

啟用**顯示選擇字數**時，彈出視窗也會顯示選擇字數。

### 突出顯示評論 [highlight-comments]

評論與簽名是分開的。簽名是亮點；評論是您對此的註釋。

從選擇彈出評論圖示新增或編輯評論，或按住 Control 鍵點擊反白並選擇 **新增評論...** 或 **編輯評論...**。選擇 **刪除註釋** 以刪除註釋而不刪除突出顯示。

帶有註釋的突出顯示顯示一個小指示點。當註釋側邊欄可見時（**預覽 > 顯示註釋**），閱讀模式突出顯示註釋將顯示在此處，並帶有一條連接到父突出顯示的連接線，旁邊還有 CriticMarkup 和其他文件註釋。

### 自動反白顯示

點擊預覽頂部的螢光筆工具可在您選擇文字時自動反白文字。按一下選擇彈出視窗中的螢光筆以撤銷上次自動反白顯示，或再次按一下頂部螢光筆工具以關閉自動反白顯示。

當您指向或選擇它們時，內聯高亮顯示開始和結束手柄。拖曳任一手把可擴展或縮小突出顯示的範圍。刷新或重新開啟文件時，變更會自動儲存並恢復。

按一下反白以將其對焦，然後按刪除或退格鍵將其刪除。按住 Control 键单击突出显示的部分，然后选择“**共享...**”打开包含文档标题和突出显示文本的 macOS 共享表，选择“**添加评论…**/**编辑评论…**”以附加注释，或选择“**删除评论**”以清除注释。

**閱讀模式關閉時顯示突出顯示**設定控制在離開該模式後儲存的突出顯示是否仍然可見。

## 導出亮點 [exporting-highlights]

選擇 **預覽 > 匯出反白...** 或按一下閱讀模式工具列中的匯出反白工具。格式：Markdown、HTML（目前預覽樣式）、純文字、CSV（Readwise 相容，**註釋** 列中包含註釋，**簽名** 中包含簽名）和 JSON（每個反白顯示上包含一個 `comment` 欄位）。

HTML 匯出巢狀將註釋突出顯示為每個突出顯示的段落下方的區塊引用。

JSON 格式是 Marked 的交換檔。將其保存在 Markdown 文件旁邊作為 `Document.markedhighlights.json`，或在匯出 TextBundle 時自動包含它。

## 導入亮點 [importing-highlights]

選擇 **預覽 > 匯入反白...** 並選擇 Marked 反白顯示 JSON 檔案。按 ID 合併高亮顯示：新增新的 ID，更新符合的 ID，並且保留檔案中不存在的現有高亮顯示。

當您開啟包含 `highlights.json` 的 TextBundle 時，Marked 會自動合併這些反白顯示。當 TextBundle 開啟時，Marked 也會將反白顯示和註解變更儲存回封包中的 `highlights.json`（不修改 `text.md`）。

## TextBundle 亮點 [textbundle-highlights]

在 **儲存 TextBundle** 上，啟用 **包含反白** 以將 `highlights.json` 嵌入到捆綁包（或 TextPack）中。共用該捆綁包，以便協作者可以在 Marked 中開啟它並保留組合的突出顯示集。

## CriticMarkup 行動 [criticmarkup-actions]

與高亮導出和導入不同，預覽選單為保存的高亮提供了兩個 CriticMarkup 操作：

- **將反白顯示複製為 CriticMarkup** 以 CriticMarkup 格式複製每個反白顯示，而不更改來源檔案。
- **將反白顯示插入文件...** 要求確認，然後將明確的匹配來源文字包裝在 CriticMarkup 中。 Marked 跳過缺失、重複或重疊的匹配項並報告結果。

透過簽名和註釋，產生的標記使用<code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>。僅使用註釋，Marked 使用 <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>。只有簽名時，它使用<code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>。如果沒有其中任何一個，Marked 只會建立 <code>{=<span>=</span>highlighted text==}</code> 標記。

## 印刷亮點 [printing-highlights]

預設情況下，列印或另存為 PDF 時會包含閱讀模式反白顯示。使用列印表中的 **包括閱讀模式反白** 將其變更為目前輸出。 {% prefspane Export %} 中的匹配設定控制未來列印和 PDF 作業的預設值。
