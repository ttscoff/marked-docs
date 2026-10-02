# <%= @title %>

以*你自己*的方式檢視文件。

## 使用自訂樣式 [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

探索自訂樣式最簡單的方式，就是透過
[自訂樣式庫][2]。你可以在那裡瀏覽現有樣式的
實際效果，只需點一下按鈕就能安裝，甚至可以
[提交你自己的作品][6]供其他人使用。

若要將本機硬碟中的自訂樣式表加入 Marked，
請使用 {% prefspane Style %}。新增的樣式會出現在
「視窗設定」的下拉選單以及每個視窗中，並根據
所加入 CSS 檔案的基本檔名命名。請將自訂 CSS 檔案
存放在硬碟上安全的位置。如果檔案在硬碟上被移動，
它們就會從 Marked 中移除，直到你從新位置重新加入
為止。建議在刪除或重新命名 Marked 所使用的 CSS
檔案之前，先關閉已開啟的文件並從「設定」中移除該
樣式。就算不這麼做也不會造成任何損壞，只是能省去
一些困擾。

你可以使用樣式管理員中的「加入」按鈕來新增自訂樣式，
或是將一個以上的 CSS 檔案拖放到「設定」面板中。

## 使用樣式管理員管理樣式 [managing-styles-with-the-style-manager]

開啟樣式管理員後，你可以在單一地方整理所有內建
與自訂主題。點一下 {% prefspane Style %} 面板中的
**管理樣式…** 按鈕，或直接將 CSS 檔案拖放到偏好設定
視窗上——Marked 會將它們匯入、開啟樣式管理員，
並自動選取新加入的那一列。直接將 CSS 檔案拖放到
樣式管理員視窗上也同樣有效；當你拖放多個檔案時，
覆蓋提示會更新為「加入 N 個自訂樣式」，讓你清楚知道
正在批次匯入。

![][img-style-manager]

在樣式管理員中，你會看到一個可排序的表格，
混合列出內建與自訂樣式。每一列都提供：

- **啟用**核取方塊：立即將該樣式加入或移出「樣式」選單、
  預設樣式彈出選單，以及鍵盤快捷鍵。停用目前使用中的
  樣式時，會自動切換到下一個可用項目。
- **名稱**欄位：可直接在原地編輯；變更會被保留，並套用到
  所有選單。點一下樣式名稱即可就地編輯。
- **來源**欄位：標示為內建、自訂或重複。
- **操作**按鈕群組：**編輯**（在你的編輯器中開啟 CSS 檔案）、
  **複製**（建立副本並在硬碟上產生新的 CSS 檔案）、
  **顯示**（在 Finder 中顯示該檔案），以及**刪除**
  （可選擇僅移除參照，或將 CSS 檔案移到垃圾桶）。

各列可透過拖放重新排序，順序會決定「樣式」選單
以及 `⌘/#` 快捷鍵的指派，因此你可以直接把樣式
拖到你想要的位置。你也可以將外部 CSS 檔案拖曳到
特定位置；拖放時的指示線會決定新樣式插入的位置。

### 即時預覽 [live-preview]

右側面板會顯示所選樣式的預覽，並以一份包含各種
標題、清單、表格、程式碼區塊等完整元素的 HTML 文件
呈現。預覽使用的是硬碟上實際的 CSS 檔案，因此你在
外部編輯器所做的修改會立即反映出來。核取方塊可切換
深色模式預覽。

你可以在 [GitHub][1] 上找到更多可用的樣式
（也可以參考[範例][2]快速瀏覽現有內容），
或作為建立自己樣式時的參考。詳情與技巧請參閱
[建立自訂 CSS][3]。

## 額外 CSS [additional-css]

在 {% prefspane Style %} 中，你會找到一個名為
「額外 CSS」的選項，旁邊有個標示「編輯 CSS」的按鈕。
點一下這個按鈕會開啟一個視窗，你可以在其中加入
會套用到所有樣式的通用 CSS 規則。請注意，在覆蓋
Marked 部分預設樣式時，規則的優先度（specificity）
可能很重要。文件的主要內容區塊是包在 id 為
「#wrapper」的 div 中。在選擇器前加上這個前綴，
可以更容易覆蓋樣式，例如：

    #wrapper img { width: 100%; height: auto; }

這個欄位中的 CSS 會**附加到目前使用中的主題後面**。
它並不能取代完整的自訂樣式：只針對此欄位撰寫的
樣式表本質上是不完整的，若透過樣式管理員把它當作
主題載入，其未涵蓋的部分將完全沒有樣式。

Marked 會在注入前**改寫**額外 CSS 的選擇器。像
`.mkprinting` 這樣位於開頭的 body class 會被合併到
`body` 上，而不是巢狀在 `#wrapper` 之下，因此此欄位中
的列印規則應使用 `body.mkprinting #wrapper …`（完整改寫規則請參閱
[建立自訂 CSS](Writing_Custom_CSS.html#additional-css-settings)）。
此欄位沒有大小限制，也不會做有效性檢查——無效的
CSS 只是不會產生任何效果而已。

這個欄位中的 CSS 會套用到每一份文件，無論使用的是
哪一種樣式——包括匯出 HTML 且有包含樣式時也一樣。
如果你想根據條件式判斷來套用自訂 CSS，請使用
{% prefspane Processor %} 自訂規則中的「設定樣式」、「插入 CSS
檔案」或「插入 CSS」動作。

## 列印與 PDF 匯出 [print-and-pdf-export]

Marked 會在每次預覽時注入內建的 `@media print` 區塊
（`mkprintstyles`）。它會設定一些預設值，例如
`html`、`body` 與 `#wrapper` 使用 **10pt** 的基準字級
（若已啟用 {% prefspane Export %} 中的「匯出／列印自訂字級」選項，
則使用該處設定的大小），並透過 `p { font-size: 1em; }` 與
`li p { font-size: 1em; }` 正規化段落文字，避免像 `p { font-size: 1.1429em; }` 這類僅限
螢幕顯示的規則，在 PDF 與列印輸出中放大本文字級。

PDF 匯出在用來產生檔案的隱藏 WebView 中，可能會使用
**print**（列印）或 **screen**（螢幕）媒體類型。內建
主題通常使用列印媒體；**自訂樣式**與
[Fountain](Fountain_for_Screenwriters.html) 文件則常使用
螢幕媒體，以便版面與預覽一致。也就是說，`@media print { ... }`
規則並不一定會在 PDF 匯出時套用。

若要讓 PDF 與「列印／PDF 預覽」的樣式穩定可靠，
請在選擇器前加上 Marked 於匯出期間加到 `<body>` 的
`mkprinting` class（詳情與範例請參閱
[撰寫自訂 CSS](Writing_Custom_CSS.html#printstyles)）。
在**自訂樣式**檔案中，可以單獨使用 `.mkprinting`。在
**額外 CSS** 中，因為該欄位會改寫選擇器，所以請使用
帶有 body 前綴的形式 `body.mkprinting #wrapper …`。當你需要同時涵蓋兩種
路徑時，也可以將兩種形式與 `@media print` 搭配使用。

若要設定與 Marked 列印預設值不同的字級，請在你的
自訂 CSS（或額外 CSS）中加入明確的規則。當你需要
覆蓋 Marked 注入的列印樣式時，請使用 `!important`——
例如：

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

沒有加上 `!important` 的規則，可能會輸給 `mkprintstyles` 中
較後面的規則，或是你樣式表中其他仍在列印時生效的
無限定選擇器。將僅限列印的微調規則放在 `@media print`
與（或）`.mkprinting` / `body.mkprinting` 規則中（而不是只放在
螢幕規則裡），能讓預覽與匯出的行為更容易掌握。

## 監看 CSS 變更 [watching-css-changes]

你可以在 {% prefspane Style %} 的「自訂樣式」區段中勾選一個
選項，讓 Marked 除了監看你正在編輯的 Markdown
檔案之外，也一併監看目前使用中的 CSS 檔案。當偵測
到任一檔案有變更時，預覽就會更新。這對於編輯自訂
樣式時不必一直手動重新整理很有幫助，也可以用於
簡單的網頁開發工作。

這對一些基本的網頁設計工作與 CSS 實驗（例如建立
自訂樣式）也很有用。載入一份包含你想要設計樣式的
所有標記元素的 Markdown 檔案，建立一個自訂樣式，
然後在編輯時觀察預覽即時變化。

## 撰寫自訂 CSS [writing-custom-css]

如果你熟悉 CSS，就可以自行建立供 Marked 使用的
樣式表。詳情請參閱[撰寫自訂 CSS][3]。每次做出新的
成果時，別忘了考慮[提交][6]到[樣式庫][2]，
與其他使用者分享。請務必涵蓋指南中列出的基本要點，
並在檔案開頭加上中繼資料註解。

### 使用 StyleStealer 自動產生自訂樣式 [automatic-custom-styles-with-stylestealer]

你甚至可以使用 [Style Stealer][4] 根據現有網站
自動產生樣式。它可以載入一個網頁，抓取 Markdown
中所有主要元素的計算樣式，然後將其儲存為自訂樣式。

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


從[樣式管理員](Style_Manager.html)管理自訂樣式
（重新命名、重新排序、複製與刪除）。

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
