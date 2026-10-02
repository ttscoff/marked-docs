# <%= @title %>

{% prefspane Style %}中的選項：

![設定：樣式][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### 版面配置與字體排印 [layout-and-typography]

限制預覽中的文字寬度
: 使用滑桿設定預覽內文的最大寬度（以像素為單位）。

段落自動斷字
: 允許文字以連字號自動換行。

避免標題與段落出現孤字
: 在標題與段落最後兩個字之間強制加入不斷行空格，以避免單一字詞換到下一行。

產生符合印刷規範的引號與標點
: 使用 SmartyPants 產生智慧型引號、刪節號轉換及其他排版功能（MultiMarkdown）。

以方括號包住註腳標記
: 若勾選，將使用 MultiMarkdown 預設的註腳標記格式（[1]）。取消勾選則移除方括號。

為特定副檔名啟用大綱模式
: 對列出的副檔名自動開啟大綱模式。

使用 APA 格式
: 使用 APA 樣式大綱，取代預設的十進位格式。

將逐字（程式碼）區塊以詩體樣式呈現
: 若勾選，以 Tab 縮排、圍籬或引入的程式碼會以詩體樣式顯示，而非程式碼區塊（不含語法醒目提示，並依主題套用特殊樣式）。

允許主題在程式碼區塊內換行
: 若勾選，主題可在`pre>code`區塊內換行顯示文字。若未勾選，水平溢出的內容一律以捲動方式顯示。

永遠換行顯示程式碼
: 強制程式碼區塊換行，不論主題設定為何（會覆寫主題的換行行為）。

偵測並以由右至左樣式顯示文字
: 依文件中每個元素偵測語言，並依需要以由右至左（RTL）樣式呈現。

### 樣式 [theme]

管理樣式
: 開啟[樣式管理員](Style_Manager.html)視窗。將硬碟中的 CSS 檔案加入，即可讓它們出現在樣式選單中。使用`Add New Style`按鈕，或將 CSS 檔案拖曳到此視窗中。拖曳可重新排序，並可使用核取方塊啟用或停用樣式。

更多主題
: 開啟線上主題藝廊，瀏覽並安裝其他樣式。

預設樣式
: 這裡選取的樣式會套用於所有新視窗，除非[文件中繼資料另有指定專屬樣式](Per-Document_Settings.html)（例如「Marked Style: Grump」）。

追蹤 CSS 變更
: 啟用後，Marked 會監看目前樣式的磁碟變更，方便自訂樣式編輯與網頁開發。

附加 CSS
: 這裡加入的 CSS 會附加在每個主題的一般樣式表之後，屬於部分覆蓋，而非完整主題替代方案。
: Marked 會重寫此欄位中的選擇器（例如，列印規則應使用`body.mkprinting #wrapper …`）。這裡不會進行大小或有效性檢查——請參閱[建立自訂 CSS](Writing_Custom_CSS.html#additional-css-settings)。
: 此設定適用於所有文件與所有樣式，包括匯出 HTML 時包含樣式的情況。若想依條件對文件套用自訂 CSS，請使用{% prefspane Processor %}下的自訂規則。

### 內含指令碼 [include-scripts]

語法醒目提示
: 為程式碼區塊開啟 highlight.js 的[語法醒目提示](Syntax_Highlighting.html)功能。從下拉選單中選擇主題。
: 若勾選**僅限指定語言時**，語法醒目提示將只套用於已指定語言的圍籬程式碼區塊。

啟用 MathJax
: 載入 [MathJax](MathJax.html) 以顯示 MathML 方程式。從下拉選單中選擇**本機**（內建）或 **CDN**。
: **附加套件**會開啟工作表，讓你加入額外的 MathJax 套件（例如物理與化學）。
: **進階設定**會開啟工作表，供你自訂 MathJax 設定。

啟用 KaTeX
: 載入 [KaTeX](MathJax.html#katex) 作為 MathJax 的替代方案。兩者只能擇一啟用。

方程式編號
: 若適用，Marked 會為渲染後的方程式加上圖號。選擇**左側**或**右側**作為編號位置。若使用 MathJax，可選擇**僅限 AMS**，只為 AMS 方程式編號。

Mermaid
: 從 CDN 載入 [mermaid.js](https://mermaid.js)，以啟用 Markdown 風格的圖表繪製功能。每次文件更新時繪製 Mermaid 圖表所需的掛勾會自動包含在內。

圖表平移與縮放
: 當文件中含有 Mermaid 圖表時，可透過{% kbd cmd %}+捲動來縮放，並以點按拖曳的方式平移畫面。
