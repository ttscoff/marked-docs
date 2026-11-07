# <%= @title %>

Marked 內建樣式編輯器，也可以套用自訂的 CSS 檔案。

你可以使用編輯器來製作精美的樣式，或者，如果你懂一點點「剛好夠用」的 CSS，也能讓 Marked 呈現出你想要的任何外觀。

## 快速上手 [getting-started]

開發者與使用者在 [markedapp.com/styles](https://markedapp.com/styles/) 建立了一個自訂樣式的作品集網站。這個作品集讓你可以直接在 Marked 中預覽並安裝樣式。任何已安裝的樣式都可以在 Finder 中顯示，以便檢視與修改。你可以透過 {% appmenu Style, Generate a Custom Style %} 使用內建檢視器開啟作品集，或者點按樣式管理器中任一可編輯樣式旁的鉛筆（編輯）圖示。如果你想編輯內建樣式，需要先在管理器中將它複製一份。

GitHub 上也有一個[自訂樣式儲存庫](https://github.com/ttscoff/MarkedCustomStyles)，內含各種範例。歡迎瀏覽、使用，也歡迎貢獻你的作品。如果你根據其中某個基礎主題散布你的主題，也歡迎將自己加入貢獻者名單。

由於 Marked 支援使用自訂 CSS 檔案，客製化預覽畫面幾乎沒有上限。所有能在 Safari 中運作的 CSS3 選項，在 Marked 中同樣適用。以 Marked 預設的 Markdown 檔案來說，你只需要處理少數幾個 HTML 元素：所有內容都包在 id 為「wrapper」的 div 中，其餘則完全取決於你的文件標記方式。

如果你是為了個人使用而設計，那就沒有任何規則限制。在自訂 CSS 選取器下方的核取方塊開啟 CSS 追蹤功能，這樣當你編輯並儲存自訂 CSS 時，預覽畫面就會即時更新。

**你可以參考[骨架主題](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css)來快速上手。**

如果你打算分享自己製作的 CSS，有幾個要點需要注意。首先，有幾個 body class 必須套用樣式：

## Body Class [body-classes]

以下樣式在任何要分享出去的 Marked CSS 中都必須包含。這些 body class 讓你能針對不同偏好設定選項，鎖定並修改對應的選取器。

### 反轉配色 [inverted]

當使用者選擇 {% appmenu Preview, Dark Mode %} 時，body 標籤會加上一個「inverted」的 class。你可以用它來鎖定高對比、深色底淺色字的樣式。

反轉樣式應該只套用在預覽畫面上，而不套用在列印時，因此請用媒體查詢（@media screen）來加以限制。下面的程式碼相當通用，大多數情況下你可以直接放進自己的樣式表中以確保相容性，但也歡迎自行調整。

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### 詩體格式 [poetry]

使用者可以選擇將 Tab 縮排的文字視為詩體格式還是程式碼。兩者唯一的差異在於，若選擇詩體模式，pre/code 區塊會套用……嗯，比較有詩意的樣式。「poetry」這個 class 會加在 body 標籤上。

你可以盡情發揮創意來設計樣式，但這裡提供一個基本範例：

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## 特殊情況 [special-cases]

表格、Figure/Figcaption，以及 `a.footnote` 與 `div.footnotes>a` 這種特殊情況，也都需要納入考量。這些沒有固定的處理規則，但你可以參考預設樣式，了解 Marked 需要哪些 CSS 規則。

所有預設樣式中，標準的表格樣式都是在交替列上使用透明度，讓表格能柔和地融入任何背景色。你可以直接複製這些樣式，也可以自己設計一套，只要記得幫它們加上樣式即可！figure 與 figcaption 也是同樣道理；在文件中加入一張帶有替代文字（alt text）的圖片，看看標記會如何呈現，再據此設計樣式。

文件中包含的註腳會在內文中產生一個連結（a.footnote），並在結尾產生一個包含對應文字的 div（div.footnotes）。同樣地，請參考預設樣式作為範例。為了避免含有註腳編號的那一行行高被改變，請務必加入類似以下的規則：

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

若要讓返回箭頭保持在同一行，請加入：

```css
.footnotes p {display:inline}
```

另外，建議加入一條通用規則，讓所有圖片都不超出頁面寬度。可以參考：

```css
#wrapper img { max-width: 100% }
```

如果你的主題有額外的內距或固定寬度，請自行調整 max-width 以符合需求。

## 列印樣式 [printstyles]

務必加入列印樣式，移除任何背景色、固定捲動效果，以及僅供預覽用的介面元素。Marked 提供兩種方式來鎖定列印與 PDF 輸出。

### `@media print` [media-print]

從 Marked 列印，或使用列印媒體進行 PDF 匯出時，會套用標準的 CSS 列印規則：

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### `.mkprinting` Class [the-mkprinting-class]

當 Marked 為 **PDF 匯出**或**列印／PDF 預覽**（{% kbd cmd P %}）準備文件時，會在 `<body>` 標籤上加入 `mkprinting` 這個 class（與其他匯出用 class，如 `bandw`、`breakAfterTOC`，以及你的樣式所帶的 `mkstyle--*` class 並列）。Marked 內建主題大多使用這個 class 來處理列印專屬規則，而非單純依賴 `@media print`。

PDF 匯出時，Marked 常會以 **screen** 媒體來載入隱藏的算圖用 WebView（尤其是自訂樣式與 [Fountain](Fountain_for_Screenwriters.html) 文件），因此樣式表中的 `@media print` 區塊可能**不會**套用到 PDF 輸出。以 `.mkprinting` 為前綴的規則因為是一般的 class 選取器、而非媒體查詢，所以在匯出期間一定會生效。

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

若某個樣式需要**同時**在瀏覽器列印與 Marked PDF 匯出中都正常運作，請複製一份關鍵規則，或合併選取器：

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**自訂樣式與 Additional CSS 的差異。** 在自訂樣式的樣式表中，請如上所示撰寫 `.mkprinting #wrapper …`。而在 **Additional CSS** 欄位中，Marked 會在注入前重寫選取器──請改用以 body 限定的寫法：

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

關於重寫的運作方式，以及為什麼單獨的 `.mkprinting #wrapper …` 在該欄位中無法比對成功，請參閱 [Additional CSS 設定](#additional-css-settings)。

在偵錯自訂列印 CSS 時，可開啟列印／PDF 預覽或匯出成 PDF，然後使用 [Safari 的 Web Inspector](#webkitinspector) 檢查文件──在列印版面配置生效期間，`<body>` 會帶有 `mkprinting` 這個 class。

列印時隱藏連結的功能是在主題之外另行處理的，讓使用者可以選擇在輸出時隱藏連結的醒目提示與底線。只要你已經為文字設定好基礎樣式，就不必特別擔心這一點。

所以，放手去做吧。把你的部落格主題轉換過來、為 PDF 文件打造一套殺手級的列印樣式，或是為你慣用的寫作風格量身打造完美的預覽樣式。如果做出令人驚艷的成果，[歡迎與社群分享](https://markedapp.com/styleshare/)。

## Additional CSS 設定 [additional-css-settings]

在 {% prefspane Style %} 中，你可以編輯 **Additional CSS**。這些規則會**附加在目前載入的主題之後**。它們是刻意設計的局部疊加層，而非完整主題。如果你把一份完整的樣式表貼進這個欄位──或是透過[樣式管理器](Custom_Styles.html)把同一份局部樣式表當成主題匯入──那麼樣式表未涵蓋到的部分將維持無樣式狀態。

### 選取器重寫 [additional-css-selector-rewriting]

Marked 會在注入 Additional CSS 之前重寫選取器（以 `body.mk-has-additional-css …` 的形式），讓規則的作用範圍限定在預覽畫面內：

- 若某個選取器部分本身已經以 `body` 或 `#wrapper` 開頭，會加上 `body.mk-has-additional-css` 前綴，並將 body class 合併而非巢狀化。
- 其他任何選取器部分，都會被限定在 `body.mk-has-additional-css #wrapper …` 之下。
- Marked 加在 `<body>` 上的前導 body class──包括 `.mkprinting`、`.inverted`、`.poetry`、`.bandw`、`.breakAfterTOC` 與 `.mkstyle--*`──都會被視為 `body` 並合併到 body 選取器上，而不會巢狀化在 `#wrapper` 之下。

| 在 Additional CSS 中輸入 | 結果 |
| :-- | :-- |
| `#wrapper h2` | 可比對成功（範圍限定正確） |
| `body.mkprinting #wrapper p` | 在列印／PDF 期間可比對成功 |
| `.mkprinting #wrapper p` | **無法**比對成功（需要巢狀的 `#wrapper`） |
| `:root { --x: 1; }` | **無法**比對成功（自訂屬性建議改用 `body` 或 `#wrapper`） |

在這個欄位中撰寫列印規則時，建議優先使用 `body.mkprinting #wrapper …`。在自訂樣式檔案中，相同的視覺效果則可以維持較簡短的 `.mkprinting #wrapper …` 寫法。

Additional CSS **沒有大小限制，也不會檢查 CSS 語法是否有效**。Marked 只會儲存並注入你輸入的內容；無效的 CSS 在預覽中就是不會產生任何效果。

### HTML 與其他匯出格式 [additional-css-exports]

Additional CSS 會套用於即時預覽、列印／PDF 預覽、PDF 匯出，以及在包含樣式時的 **HTML 匯出**──匯出的 `<body>` 會加上 `mk-has-additional-css` 這個 class，讓重寫後的選取器能正確比對。DOCX、ODT 與 EPUB 則使用各自的樣式處理方式，並不會以相同方式套用 Additional CSS。

只要善用[高優先度](#overridingspecificity)、針對列印與螢幕的 `@media` 查詢，以及（在此欄位中的）`body.mkprinting` 選取器或（在自訂樣式中的）`.mkprinting` 選取器，稍微懂一點 CSS，你幾乎可以掌控每一個樣式細節。

## WebKit Inspector [webkitinspector]

Safari 的 Web Inspector 是查看 Marked 產生的 HTML 與 CSS 內容最簡便的方式，也能即時試驗自訂樣式。

### 在 Safari 中開啟開發選單 [enabling-the-develop-menu-in-safari]

1. 開啟 Safari，選擇 {% appmenu Safari, Settings… %}。
2. 切換到**進階**分頁。
3. 開啟**顯示網頁開發者功能**（在較舊版本的 macOS 中則是**在選單列中顯示「開發」選單**）。

開啟之後，Safari 選單列中就會出現「開發」選單。

![Safari 的「開發」選單，顯示 Marked 文件][develop-menu]

### 檢查 Marked 文件 [inspecting-a-marked-document]

1. 在 Marked 中開啟一個預覽視窗後，切換到 Safari。
2. 從選單列選擇「**開發 → _〈你的 Mac 名稱〉_ → Marked → _〈文件標題〉_**」。
3. Safari 會開啟一個附加在所選 Marked 預覽視窗上的 Web Inspector 視窗。

在這裡你可以：

- 使用「**元素**」分頁檢查 `#wrapper` div 內的 DOM 結構，並查看套用了哪些 CSS 規則。
- 將滑鼠移到 DOM 樹狀結構中的元素上，即可在 Marked 視窗中將其標示出來。
- 使用「**樣式**」側邊欄即時調整規則，再將可行的程式碼片段複製回自訂樣式或 **Additional CSS** 中。
    - 在「元素」分頁編輯完 CSS 後，可以切換到「Changes」分頁查看編輯內容摘要

	![Changes][css-changes]
- 使用「**主控台**」分頁對即時預覽執行 JavaScript。完整的 [Marked JavaScript API](https://markedapp.com/help/jsapi/) 都可以在這個主控台中使用。
- 視需要探索其他分頁，例如在偵錯文件所載入的資源時使用「**網路**」分頁。

![使用 Safari Web Inspector 檢查 Marked 預覽畫面][inspecting]

## 分享自訂 CSS [sharing-custom-css]

使用 {% appmenu Style, Share a Custom Style %} 在瀏覽器中開啟分享網站。將你的 CSS 拖曳到拖放區（或點按以從磁碟選取檔案），即可上傳你自訂樣式的 CSS。

分享的樣式需要經過開發者審核後才會出現在作品集網站上，因此不會立即看到成果。

## 其他小技巧 [other-tips]

### 覆寫優先度 [overridingspecificity]

在 Marked 預覽畫面中，會依據目前樣式的檔案名稱加上一個 body class。如果預覽設定為「Swiss」，那麼 `<body>` 標籤上就會有一個叫做 `mkstyle--swiss` 的 class。如果你的自訂 CSS 檔案叫做 MyCustom.css，那麼對應的 body class 就會是 `mkstyle--mycustom`。你可以把這個 class 放在規則前面，用來覆寫基礎樣式中定義的規則。若要在某條規則中取得絕對優先度，也可以一併加上容器 div 的 #wrapper ID：

	.mkstyle--mycustom #wrapper p+p { ... }

### 目錄樣式設計 [table-of-contents-styling]

如果你使用 `<!--toc-->` 這個標記來[插入目錄](Special_Syntax.html#tableofcontents)，你可以在自訂樣式中利用「#wrapper」提高優先度，來覆寫目錄層級指示符號的設定：

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

如此一來，當你的自訂樣式套用時，目錄中所有的清單項目就會改用方形項目符號，而不是偏好設定中原本指定的樣式。

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
