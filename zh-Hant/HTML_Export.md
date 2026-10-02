# <%= @title %>

Marked 會從你的**即時預覽**匯出 HTML──也就是螢幕上顯示的同一份渲染輸出。當你需要把片段貼到部落格或 CMS，或需要一個內嵌樣式與圖片、可在任何瀏覽器開啟或部署到任何地方的獨立 `.html` 檔案時，就可以使用 HTML 匯出。

典型的工作流程是**先預覽、後匯出 HTML**：在 Marked 中開啟或編譯你的文件，選擇主題，在即時預覽中校對，等版面看起來沒問題後再匯出。

## 取得 HTML 的兩種方式 [two-ways-to-get-html]

### 複製 HTML（片段） [copy-html-snippet]

**複製 HTML**會把預覽的 HTML 原始碼放到剪貼簿──可直接貼到 WordPress、Ghost、Squarespace、論壇、電子郵件範本，或任何接受 HTML 片段的應用程式。

* 齒輪選單 → **複製 HTML**，或在預覽視窗聚焦時按 {% kbd shift cmd C %}
* 複製的是**渲染後的內文 HTML**（而非包含 `<html>` 外層的完整文件）
* 選用：在 {% prefspane Export %} 中啟用**複製 HTML 時內嵌圖片**，將本機圖片以 Base64 編碼為貼上原始碼中的 `data:` 網址

當目的地已有自己的樣式表、你只需要內容標記時，複製 HTML 是最理想的選擇。

### 儲存 HTML（檔案） [save-html-file]

**儲存 HTML**會把完整的 `.html` 檔案寫入磁碟。

* 匯出 → **儲存 HTML**、{% kbd cmd S %}，或從[匯出面板](Exporting.html#drawer)選擇 **HTML**（{% kbd shift cmd e %}）
* 在儲存對話框中選擇檔名與位置
* 在對話框的附加選項中設定匯出選項（見下文）

儲存 HTML 適合用來封存、分享獨立檔案，或直接在瀏覽器中開啟結果。

## 儲存 HTML 選項 [save-html-options]

「儲存 HTML」對話框包含一個匯出設定檔選擇器與以下選項：

![Save HTML options][savehtml]

**在輸出中包含樣式**

勾選後，Marked 會把目前選取的預覽主題 CSS 內嵌到匯出檔案中的 `<style>` 區塊內。你可以在核取方塊旁的樣式選單中選擇任何內建主題或[自訂樣式](Custom_Styles.html)。輸出結果是一份完整的 HTML 文件，包含 `<!DOCTYPE html>`、`<head>`，以及包住你內容的 `#wrapper` div──與你在預覽中看到的一致。

未勾選時，Marked 只會儲存包含渲染內容的精簡 HTML 文件（不含 Marked 主題 CSS）。當你想要原始 HTML，用來貼到或匯入其他會提供自身樣式的系統時，可以使用這個選項。

**為獨立 HTML 內嵌本機圖片**

啟用**在輸出中包含樣式**後，你也可以將本機圖片以 Base64 `data:` 網址的形式內嵌到 HTML 檔案中。這樣產生的單一檔案就能直接透過電子郵件寄送、上傳或代管，而不需要另外附上 `images/` 資料夾。

* 適用於本機磁碟上以**相對或絕對路徑**參照的圖片
* 避免使用 `file:///` 網址──這類圖片無法可靠地內嵌
* 遠端圖片（http/https）除非事先下載，否則仍會保持為外部網址
* Base64 內嵌可能會產生較大的檔案；當可攜性比檔案大小更重要時再使用

**包含語法高亮 JavaScript**

當 {% prefspane Preview %} 中啟用了語法高亮時，這個選項會從 CDN 加入 highlight.js 的 CSS 與 JavaScript，讓程式碼區塊在匯出的檔案中保留原本的顏色。匯出的 HTML 需要網路連線才能載入 CDN 資源。

**包含 MathJax 或 KaTeX CDN 連結**

當預覽啟用了 [MathJax](MathJax.html) 或 KaTeX 時，你可以在儲存的 HTML 中包含對應的 CDN 指令碼，讓方程式能在瀏覽器中呈現。與語法高亮一樣，除非你自行代管這些指令碼，否則檢視檔案時需要網路連線。

**CriticMarkup 匯出類型**

含有 [CriticMarkup](CriticMarkup.html) 的文件可以選擇匯出時要顯示編輯後文字、原始文字，或完整標記。

**匯出設定檔**

選擇已儲存的[匯出設定檔](Exporting.html#export-profiles)，一次套用你偏好的 HTML 匯出設定（內嵌樣式、圖片、語法高亮、數學公式）。

## 使用內建與自訂主題設定樣式 [styling-with-built-in-and-custom-themes]

當勾選**在輸出中包含樣式**時，**預覽樣式**會決定 HTML 的外觀：

1. 從預覽視窗的樣式選單中選擇樣式（或在 {% prefspane Style %} 中設定預設值）。
2. 在即時預覽中檢查字體排印、標題、程式碼區塊與圖片。
3. 儲存 HTML 時，在匯出對話框中選擇相同的樣式。

每一個 Marked 內建主題──Swiss、GitHub、Manuscript 等等──都可以被內嵌。[自訂樣式](Custom_Styles.html)以及來自[樣式管理員](Custom_Styles.html)的樣式運作方式相同。

當樣式為內嵌時，來自 {% prefspane Style %} 的**額外 CSS**也會包含在 HTML 匯出中。匯出的 `<body>` 會加上 `mk-has-additional-css` 類別，讓 Marked 重寫過的額外 CSS 選擇器能正確對應。詳見[建立自訂 CSS](Writing_Custom_CSS.html#additional-css-settings)。

I> 部分僅適用於預覽的 CSS（固定定位、視窗技巧、深色模式的 `@media screen` 反轉）在 Marked 之外可能無法一對一還原。發布前請先在瀏覽器中開啟儲存的檔案確認效果。

有關撰寫指引，請參閱[建立自訂 CSS](Writing_Custom_CSS.html)。

## 中繼資料與 MultiMarkdown 標頭 [metadata-and-multimarkdown-headers]

原始檔案開頭的 MultiMarkdown 中繼資料可能會影響 HTML 匯出：

* **`Title:`**──在儲存完整 HTML 文件時，用作 `<title>` 元素
* **`XHTML Header:`** / **`HTML Header:`**──在匯出的 `<head>` 中插入額外標籤（指令碼、link 標籤、meta 標籤）
* 其他中繼資料鍵會依你選用的 [Markdown 處理器](Choosing_a_Processor.html)進行處理

如果你使用中繼資料來設定匯出選項，但不希望這些鍵出現在其他輸出中，可以將它們包在 HTML 註解裡──Marked 會在文件中任何位置尋找並處理已加上註解的中繼資料。詳見[個別文件設定](Per-Document_Settings.html)。

## 多檔案文件 [multi-file-documents]

若是書籍或多章節彙編，請使用[多檔案文件](Multi-File_Documents.html)。Marked 會預覽合併後的文件，並從編譯結果匯出一份 HTML 檔案。被納入的檔案會以 HTML 註解標示其來源路徑──在稽核哪個章節提供了哪個段落時很有用。

## 貼到其他應用程式 [pasting-into-other-applications]

| 目的地 | 建議做法 |
| :-- | :-- |
| 有自己主題的部落格／CMS | **複製 HTML**（片段，不含內嵌的 Marked CSS） |
| 靜態網站或封存 | **儲存 HTML**並勾選**在輸出中包含樣式** |
| 電子郵件或檔案分享（單一附件） | **儲存 HTML**並勾選**內嵌本機圖片** |
| WordPress、Ghost、Notion 等 | **複製 HTML**；若編輯器無法解析本機路徑，啟用**複製 HTML 時內嵌圖片** |
| 在程式碼編輯器中進一步編輯 | **儲存 HTML**時不內嵌樣式，或複製片段後自行包裝 |

若目標應用程式接受的是格式化文字而非 HTML 原始碼，[複製為 RTF](Exporting.html#rtfexportoptions)（齒輪選單）是另一個選擇。

## 相關主題 [related-topics]

* [匯出](Exporting.html)──匯出面板、設定檔與其他格式
* [EPUB 匯出](EPUB_Export.html)──內嵌 CSS 的電子書輸出
* [Mac 上的即時 Markdown 預覽](Live_Markdown_Preview_on_Mac.html)──匯出前的預覽工作流程
* [自訂樣式](Custom_Styles.html)與[設定：匯出](Settings_Export.html)
* [HTML 專屬設定](HTML_Specific_Settings.html)──HTML 輸出的處理器選項
* [AppleScript 匯出](AppleScript_Support.html)──自動化 HTML 複製與儲存

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
