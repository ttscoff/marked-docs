<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

標記為您提供選項。

## 即時預覽工作流程

1. 將 Markdown 檔案拖曳到 Marked 上（或使用 {% appmenu File, Open... ({{cmd}}O) %}）。
2. 在您喜歡的編輯器中編輯文件。
3. 儲存---標記為自動更新預覽。

請參閱 [Mac 上的即時 Markdown 預覽](Live_Markdown_Preview_on_Mac.html) 以了解 Vault 觀看、串流預覽和特定於編輯器的指南。

## 拖曳至 Dock 圖標

在已編輯的文件上使用「標記」的最簡單方法是將文件圖示從編輯器的工具列或從 Finder 拖曳到 Dock 中的「標記」圖示。 Marked 將立即開始追蹤放置在其上的任何 Markdown 文件（或文字檔案）。您也可以直接從 Finder 拖曳檔案。

## 使用選單

![][2]

   [2]: images/file_open.jpg @2x 寬度=300px 高度=118px 類別=center

當然，您可以使用 {% appmenu File, Open... ({{cmd}}O) %} 選單選項直接開啟 Markdown 檔案。標記也可以在沒有文字編輯器的情況下正常運作。只需單擊即可預覽和轉換 Markdown。

Marked 也可以直接開啟 **`.rtf` 和 `.rtfd`** 檔案（例如從 Pages 或 TextEdit 匯出）。當您儲存在原始應用程式中時，它們會轉換為 Markdown 以便預覽和更新。請參閱[RTF 和 RTFD 支援](RTF_Support.html) 以了解詳細信息，包括圖像和限制。

標記可以以相同的方式開啟 **`.pdf`** 檔案：轉換在背景運行，完成後預覽會更新。這最適合較短的、基於文字的 PDF；大型手冊和掃描文件速度較慢且不太準確。有關詳細資訊和限制，請參閱 [PDF 支援](PDF_Support.html)。

## 從剪貼簿

如果您的剪貼簿中有相容的（例如 Markdown）文本，您可以透過選擇 {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} 來開啟即時預覽。如果您從 Web 瀏覽器或其他將 HTML 或 RTF 放在剪貼簿上的應用程式複製了選定內容，Marked 會將其轉換為 Markdown 以供預覽。當您從 TextEdit 或 Pages 等應用程式貼上 RTF 時，較大的字體大小將粗略地轉換為標題層級（例如，非常大的文字變為 1 級標題，較小的大文字變為 2 級標題，依此類推）。您可以一次開啟多個剪貼簿預覽，並且可以透過選擇 {% appmenu File, Save Transient Preview %} 將它們儲存到新檔案中。

## 建立一個新文檔

標記允許您使用 {% appmenu File, New ({{cmd}}N) %} 指令建立一個新的空文本檔。它會立即詢問您儲存檔案的位置，您可以在「文字編輯器」按鈕旁邊的{% prefspane Apps %}中啟用「自動編輯新檔案」選項，以在預設編輯器中自動開啟新建立的檔案。

## 開啟最近的

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked 也會追蹤最近的文檔。 {% appmenu File, Open Recent %} 選單選項將向您顯示已開啟的文件，並讓您跳回它們。您可以快速重新開啟使用{% kbd shift cmd R %}查看的最後一個檔案。使用{% kbd shift cmd P %}或[快速操作](Quick_Actions.html)從鍵盤執行選單和預覽指令。還有很多其他鍵盤快捷鍵。如果您想了解它們，可以在[鍵盤]下找到圖表快捷方式](Keyboard_Shortcuts.html)。

## 目前檔案的新視圖 [多視圖]

使用 {% appmenu File, New View into Current File %}（{% kbd
shift cmd N %}，也在預覽上下文選單中）打開
同一儲存檔案的第二個預覽視窗。兩個窗戶
觀看磁碟上的檔案並在儲存時更新
編輯器，但每個視圖保留自己的滾動位置，
書籤、預覽樣式和[自訂規則
覆蓋](Custom_Processor.html#manuallyenabled)。

**用例範例：** 您正在編輯一篇長稿件
MultiMarkdown 有您常用的風格和處理器。打開一個
第二個視圖，將其切換到校對樣式，固定流程
運行不同內建處理器的規則，並啟用
反白顯示修訂標記的手動規則。你比較
並排草稿和校樣佈局，無需維護兩個
文件的副本。

當開啟一個文件的多個視圖時，視窗標題
包括 **視圖 2**、**視圖 3** 等，以便您可以辨別
視窗選單和任務控制中的視窗分開。

備用視圖不適用於未儲存的文檔，
剪貼簿預覽、串流預覽或基於資料夾的預覽
不映射到磁碟上的單一檔案的項目。

## 快速開啟 ##

您可以在開啟的文件之間快速切換、開啟最近使用的文件或使用[快速開啟面板](Quick_Open.html)（{% kbd cmd shift o %}）開啟檔案->開啟對話方塊。