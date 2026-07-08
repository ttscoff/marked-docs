<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>


標記讓您可以完全控制自訂規則、文本
轉換，以及運行您自己的命令或運行的能力
基於匹配檔案屬性的不同處理器。


## 使用自訂預處理器/處理器

若要新增自訂處理器，請前往 {% prefspane Processor %}
然後按一下「**自訂規則**」。

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


在規則編輯器（又稱“Conductor”）中，您可以新增自訂
具有根據文件名匹配文件的標準的規則，
路徑、內容、元資料的匹配，甚至是否
其他文件與該文件存在於同一樹中
打開。當規則匹配時，為該規則定義的操作
規則在該文件上運行。

> 在「處理器」欄位下方，「新建」中的複選框
> 文件使用custom:"決定是否測試規則
> 完全適用於預處理器和處理器階段。一般來說，
> 保留這些選取狀態，但如果您想完全覆寫
> 任何自訂處理器，請在此處設定。

![規則編輯器][2]

  [2]: images/CustomRules-800.jpg @2x width=800

若要建立新規則，請使用 `+`
左側規則清單底部的按鈕。給
規則一個名稱並將其設定為預處理器或處理器。

規則旁邊的三個點表示預處理器、處理器和已啟用。只能突出顯示預處理器或處理器之一，並且您可以單擊點來更改規則的狀態。

預處理器
：在檔案最初處理之後、Marked 新增包含的檔案、處理 GitHub 換行符等樣式首選項時執行，但在處理階段之前執行。此時文件仍然是原始 Markdown，您可以對內容進行更改以傳遞給處理器。如果沒有匹配的自訂處理器，或者在匹配的自訂處理器中沒有運行運行處理器操作，則將運行預設處理器。

處理器
：自訂處理器取代了{% prefspane Processor %}中定義的內建處理器。它可以處理預處理器可以執行的所有操作，並添加運行命令和運行處理器操作。這允許您執行自訂命令，例如Pandoc，或對符合條件的檔案執行不同的內建處理器。

自訂規則編輯器中的所有表格都可以透過以下方式重新排序
拖放，這樣您就可以影響其中的順序
規則運行時，謂詞中條件的順序
編輯器，以及要按順序運行的操作的順序。

### 謂詞編輯器

![謂詞編輯器][謂詞]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

新增規則後，使用謂詞編輯器來定義
確定規則是否運行的標準
給定的文件。使用左側下拉式選單選擇
標準，然後使用比較器和值字段來構建
謂詞。

- _Filename_ 僅符合檔案的檔案名
- _Extension_ 僅符合檔案的副檔名
- _Path_ 符合檔案的完整 POSIX (Unix) 路徑
- _Tree_ 搜尋檔案名稱符合的任何位置
  檔案的目錄樹
- _Text_ 匹配文件中的文字內容。使用轉發
  文字值周圍有斜線以使其成為常規值
  表達式搜尋。
-_Fileincludes_測試檔案是否包含includes
  文件（使用任何[標記的包括
  語法](Multi-File_Documents.html)）。
-_元資料型別_測試檔案是否包含YAML，
  MultiMarkdown 或 Pandoc 元數據
- _元資料：_欄位（例如_元資料：作者_，
  _元資料：日期_，_元資料：標題_）特定的測試
  元資料鍵。任何元資料鍵都會在下拉清單中顯示為
  _元資料：_ 後跟欄位名稱。
- _手動啟用_在規則被改變時匹配
  當前預覽視窗開啟（請參閱[手動啟用
  規則]（#manuallyenabled）如下）。將其與其他組合起來
  所有 (AND) 組中的條件，因此規則僅在以下情況下運行
  您選擇加入並且該文件符合您的其他條件。

匹配所有文件（即始終匹配的自訂處理器
運行），將 _Filename_ 設定為 `contains` `*`。星號將
充當通配符並匹配所有檔案。

[加上謂詞][加謂詞]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

按一下謂詞行上的加號 (+) 以新增另一個謂詞。按住 Option 鍵的同時點選 + 可新增可設定為全部 (AND) 或任意 (OR) 的布林群組。

### 手動啟用的規則 [manuallyenabled]

某些規則不應在與其匹配的每個文件上運行
標準。如果需要，請添加 **手動啟用** 標準
僅在當前打開它後才運行的規則
預覽。

使用謂詞下方的 **新增手動啟用** 按鈕
編輯器插入此標準。每個規則都可以包含它
只有一次。如果存在，該規則將顯示在該預覽的 {% appmenu
Preview, Enable Custom Rule %} 子選單中
視窗。

**範例用例：** 您維護一條注入規則
列印 CSS、刪除註釋並移動標題級別
PDF 導出。你不希望每個人都進行這種轉變
起草時保存，但您確實需要按需保存。給
規則正常文件匹配標準加上**手動啟用**，
然後從預覽選單（或觸發器快捷方式）切換它
當您準備好校對列印佈局時。

#### 觸發快速鍵

當選定的規則包含**手動啟用**時，
**觸發快捷方式**欄位出現在**手動新增旁邊
已啟用**。按一下錄音機，然後按 鍵
你想要的組合。此捷徑切換規則
最前面的標記預覽（如果關閉則啟用，如果開啟則停用）。的
快捷方式與規則一起儲存並在啟動後持續存在。
清除該欄位以刪除快捷方式。

![在 Conductor 中觸發快捷方式錄音器][手動快捷方式]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### 預覽選單中的按預覽覆蓋

兩個預覽選單子選單控制活動的覆蓋
僅預覽。設定按 [視圖](#multiview) 儲存
多個視窗顯示同一個檔案。

**啟用自訂規則**
：列出每個已啟用的規則，其中包括 **手動
  啟用**標準。檢查規則以為此啟用它
  預覽；取消選取將其關閉。預覽刷新
  立即。

**自訂規則覆蓋**
：列出流程階段規則。選擇一個來*固定*它：期間
  處理階段，僅評估該規則（其他
  跳過流程規則）。選擇**無（自動）**
  傳回正常的規則匹配。當您
  想要強制使用特定的處理器管道
  預覽而不更改全域自訂規則。

#### 預覽工具列中的覆蓋按鈕

當預覽至少有一個手動啟用的規則或
固定的進程覆蓋，底部會出現一個分支圖標
工具列（位於匯出和抽屜控制的左側）。
填充的強調色圖示表示覆蓋處於活動狀態；
輪廓圖示表示覆蓋已暫停。

![預覽工具列中的自訂規則覆蓋按鈕][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

按一下按鈕可暫停或重新啟用此覆蓋
預覽而不清除手動規則複選標記或
固定的流程規則。暫停的超控將在以下情況下恢復：
你再次點擊。這比取消選取規則更快
當您想要將正常預覽與您的預覽進行比較時，選單
覆蓋管道。

### 行動

使用 *+ 操作* 按鈕將操作新增至規則。

![添加動作][添加]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

可用的操作包括：

設定風格
：設定預覽的樣式。您新增的任何內建樣式或自訂樣式都可用。

運行命令
：這需要一個命令列命令，包括任何參數，並將在 STDIN 上傳遞檔案的內容。該命令應在 STDOUT 上傳回結果輸出。

> **Mac App Store 沙盒**：Marked 的 Mac App Store (MAS) 版本在限制外部二進位執行的沙盒環境中運行。如果您需要在 MAS 版本中使用 Pandoc 等外部處理器，則必須將二進位檔案複製到應用程式套件中。為此：
>
> 1. 右鍵點選Marked.app → 顯示包內容
> 2. 導覽至目錄/資源/
> 3. 如果`bin`資料夾不存在，則建立一個
> 4. 將您的二進位檔案（例如 `pandoc`）複製到此
> `bin`資料夾
> 5. 使其可執行：`chmod +x` 二進位文件
> 6. 在執行命令操作中，將其引用為：
>
> `YOUR_BINARY_NAME [arguments]`
> 或使用完整路徑：
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **注意**：具有外部 shebang 的腳本（例如指向 `/opt/homebrew/bin/python` 的 Python 腳本）在複製到捆綁包時將透過系統解釋器自動執行。 MAS 版本在執行實際上是 Python 或 Ruby 腳本而不是二進位檔案的二進位時可能仍然存在問題。
> 每次應用程式更新後，您都需要重新複製二進位文件，因為更新會替換整個捆綁包。或者，使用 **Help->Crossgrade** 取得沒有此類限制的非沙盒版本。

運行嵌入腳本
：在內建程式碼編輯器中編輯完整腳本。與 Run Command 一樣，這應該在 STDIN 上取得輸入並在 STDOUT 上傳回輸出。

設定元數據
：新增或設定元資料。提供一個鍵和一個值。如果該鍵存在，則更新其值，如果不存在，則新增該鍵。使用的元資料類型將由文件內容（或元資料轉換操作的結果）自動決定。
：如果沒有找到現有元數據，元數據將以 MultiMarkdown 格式新增至 HTML 註解。標記可以讀取此元數據，但無論使用什麼處理器，它都不會出現在您的預覽中。

刪除元數據
：根據元資料的鍵刪除元資料。

剝離元數據
：刪除所有元資料。影響 YAML、MultiMarkdown 和 Pandoc 元資料。

將 YAML 元轉換為 MMD
：將檔案頂部的 YAML 元資料塊轉換為 MultiMarkdown 樣式元資料。

將 MMD 元轉換為 YAML
：將 MultiMarkdown 元資料塊轉換為 YAML。

搜尋和替換
：對文件內容執行搜尋和取代。
：如果搜尋字串被正斜線包圍（例如`/Project \w+/`），它將被視為正規表示式。您可以使用 `$1`、`$2` 等在替換字串中包含匹配組。
：替換字段支援一些轉義序列（後跟反斜杠）：`\n`插入換行符，`\t`插入製表符，`\\`插入文字反斜杠，`\$`插入文字美元符號（而不是匹配組）
：任何其他`\X`序列都被視為`X`（反斜線被刪除），因此`\e`變為`e`。後面沒有任何字元的尾隨 \ 被保留為文字反斜線。
：在替換字串中使用 `[%key]` 插入來自文檔元資料、環境變數或上下文的值（例如 `[%title]`、`[%MARKED_PATH]`）。由同一規則中的較早操作或先前規則設定的鍵可用。不匹配的鍵將替換為空字串。

插入標題 H1
：在文檔中插入 H1。這可以從元資料或檔案名稱中提取。

移位標題
：調整標題級別，從-5--+5。例如，如果將其設為 -1，則所有 H1 都會變成 H2，H2 會變成 H3，等等。將其設為正數可將標頭等級提升該數量。

標準化標頭
：如果可能的話，此操作將確保文件中只有一個 H1，並調整所有標題級別，以便它們按語義順序排列並且不會跳過級別，例如從H2到H4。如果原始文件一開始就在語義上排序，這將很好地完善層次結構。

插入目錄
：插入目錄。 TOC 可以位於第一個 H1、第一個 H2 之後，也可以位於檔案頂部（將插入到任何元資料之後）。

插入文件
：在文件中的給定點插入選定的文字檔。這可以在第一個 H1、第一個 H2、頂部、底部或文字匹配之後（使用 `/pattern/` 搜尋正規表示式）。

插入文字
：提供彈出編輯器，您可以使用它直接將文字嵌入到操作中。定位選項與_插入檔案_相同。
：在插入文字中的任意位置使用`[%key]`從文檔元資料、環境變數或標記上下文中提取值（例如`[%author]`、`[%MARKED_PATH]`）。無論您使用哪種處理器，這都有效，因此您不需要 MultiMarkdown 來替換元資料。包含來自同一規則中較早操作（例如**設定元資料**）或來自先前規則的值。不匹配的鍵將替換為空字串。

插入 CSS 文件
：將選定的 CSS 檔案插入到文件中。這將在選擇任何樣式後加載，並可用於覆蓋現有樣式或新增樣式。

插入CSS
：提供彈出式 CSS 編輯器，您可以在其中將自己的 CSS 直接添加到操作中。該 CSS 將會被注入到文件頂部、任何現有樣式之後。注入樣式的順序將與規則中操作的順序相符。

插入 JavaScript 文件
：在文件末尾插入選定的 JavaScript 文件。請注意，如果您希望腳本在每次更新時重新加載，則需要將 *Insert JavaScript* 操作與 [update hook](#updatehook) 一起使用。

從 URL 插入 JavaScript
：使用它在文件末尾插入連結到 CDN 或其他遠端 URL 的 `<script>` 標籤。請注意，如果您希望腳本在每次更新時重新加載，則需要將 *Insert JavaScript* 操作與 [update hook](#updatehook) 一起使用。

插入 JavaScript
：提供彈出式 JavaScript 編輯器，您可以使用它直接在操作中嵌入自訂 JavaScript。這將被注入到文件的末尾，規則運行的 JavaScript 順序將由操作的順序決定，最後新增的操作最後。
：請注意，如果您希望腳本在每次更新時運行，則需要使用[更新掛鉤](#updatehook)。

自連結 URL
：將任何裸 URL 轉換為 `<url>`，這將在任何處理器中產生超連結。

運行快捷方式
：運行 Apple 快捷方式。任何快捷方式運行都應從 STDIN 獲取輸入並在最後返回輸出（停止並返回輸出）。如果要執行不修改文字的操作，請將輸入設為變量，運行操作，然後在最後輸出原始文字變數。

運行系統服務
：運行`~/Library/Services`中的任何系統服務。服務應該接受輸入並返回輸出。

執行 Automator 工作流程
：運行任何 Automator `.workflow` 檔案。輸入將在 STDIN 上傳遞，輸出預計在 STDOUT 上。

運行規則
：從目前規則執行另一個自訂規則的操作。
  從彈出視窗中選擇目標規則。呼叫的規則
  在同一階段（預處理器或進程）運行，無需
  重新評估它的謂詞，這使得它有用
  可重複使用的「成分」規則。

  **用例範例：**定義一個名為「Strip
  HTML 註釋”，帶有搜尋和替換操作，並給出
  它是一個 **手動啟用** 標準，因此它永遠不會運行
  自動。在您的主要書籍處理規則中，添加
  **依序運行規則**操作：第一個“標準化標頭”
  然後是“刪除 HTML 註解”，然後是呼叫的運行命令
  潘多克。您可以保持每個步驟的可維護性，而無需重複
  跨規則的行動。

  **巢狀：**由**運行規則**調用的規則無法調用
  另一條規則。如果目標規則包含 **執行規則**
  動作，該動作被跳過；中的所有其他行動
  目標規則仍在運作。您可以新增多個**運行規則**
  對單一規則執行的操作，並且它們按順序執行。

  規則不能呼叫自身，Marked 檢測循環
  （例如，規則 A 呼叫規則 B，規則 B 再呼叫規則 A）
  並跳過巢狀呼叫。參見【自訂規則】
  Log](#customprocessorlog) 用來跳過訊息。

繼續
：預設情況下，一旦匹配到規則，處理就會停止（預處理器和處理器是分開的，因此一個預處理器和一個處理器可以匹配）。此操作將強制規則匹配在規則執行其操作後繼續。

### 更新掛鉤

標記不會在每次更新時進行完全刷新，所以如果
你有渲染 DOM 部分的腳本，它們需要
使用 Marked 的 Hook API 運行其渲染函數。

下面的例子使用了美人魚，但你實際上從未使用過它
需要做的，因為現在預設包含美人魚。但是
如果您手動包含它，您將按照以下方式執行此操作。

新增 **插入 JavaScript** 操作，並在「編輯 JS」中
窗口，初始化腳本並添加鉤子：

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

這會導致`mermaid.run()`每次都會被執行
標記執行部分更新。

### 測試規則

規則清單下的_測試規則_按鈕將會開啟一個
您可以在其中選擇任何 Markdown 文件的對話框，它將
根據您的所有規則進行測試。符合的規則將會得到
左側以綠色標籤突出顯示。匹配時
針對文件，將出現一個 X 按鈕，可用於
清除測試並取消突出顯示行。

## 拖放

Conductor 視窗支援增強的拖放功能
智慧型檢測文件類型的功能和
根據拖曳的文件提供適當的操作。的
實作包括文本的分割覆蓋系統
允許使用者在測試文件之間進行選擇的文件
違反規則或將其新增為操作。

![拖曳自訂規則][拖曳]

[drag]: images/draganddropconductor.jpg @2x width=800

### 檔案類型檢測

系統自動檢測不同的文件類型並
顯示適當的覆蓋訊息：

- **CSS 檔案** (`.css`)：顯示「插入 CSS 檔案」疊加層
- **JavaScript 檔案** (`.js`、`.javascript`)：顯示「插入
  JS 檔案」疊加
- **腳本檔案**（任何可執行檔））：顯示「執行
  指令”疊加
- **文字檔案**：顯示分割疊加
- **可執行檔**：顯示「運行指令」疊加層
- **未知擴充**：預設為「文字」類型並顯示
  分割疊加

## 自訂處理器日誌 [customprocessorlog]

如果您得到奇怪的結果並想了解發生了什麼，自訂規則日誌將向您顯示哪些規則按什麼順序運行。使用**幫助->顯示自訂規則日誌**將其開啟。呼叫的 **運行規則** 操作和跳過的巢狀呼叫也記錄在此。

![自訂規則日誌][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## 執行多個命令

一條規則可以依序包含多個命令。的輸出
每個命令都會傳遞到下一個命令。如果你想擁有
命令與 Marked 的命令同時輸出一些內容
預覽更新，一定要傳回原來的內容
到 STDOUT 以處理下一個命令或內建
處理器。

例如，如果您想要使用指令更新 PDF
使用Pandoc的文檔，只需傳遞原始文件路徑
（從環境變數）到 Pandoc 並使用適當的
命令列選項，然後回顯 STDIN 內容
輸出到標準輸出。

## 動態繞過自訂處理器

如果自訂處理器在 STDOUT 上返回“NOCUSTOM”，則標記為
將終止自訂處理器並回退到
預設內部處理器。這允許您創建一個
可以決定是否需要的客製化處理器
使用[環境變數](#environmentvariables)運行
下面，文檔檔案名稱或副檔名，內容相符
或其他邏輯。

如果自訂處理器返回而不是`NOCUSTOM`
`MULTIMARKDOWN` 或 `DISCOUNT`（或 `GFM`）、`KRAMDOWN`，或
`COMMONMARK`，那麼該內部處理器將用於
只是那個文件。此更改不會影響預設值
在“設定”中設定處理器。

## 環境變數

運行命令操作有一個環境編輯器，您可以在其中
可以設定自己的環境變數
可用於命令或腳本。除了這些
自訂變量，Marked 包括一些它自己的。

Marked 在自己的 shell 中運行自訂處理器，這意味著
標準環境變數不會自動傳遞。
您可以使用 Marked 的環境變數來增強您的
在你的腳本中擁有自己的。標記使以下變數
可在您的 shell 腳本中使用：

**標記_來源**
：主要工作文件（工作文字、Scrivener 或索引文件的資料夾）的位置（基本目錄）。

**路徑**
：標記設定包含預設可執行資料夾的路徑，並將該目錄附加到上面的`MARKED_ORIGIN`中。預設值為：`/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`。您可以根據需要設定 PATH 變數並附加或覆寫 Marked 的路徑（例如 `PATH=/usr/local/yourfolder:$PATH`）來新增自己的路徑。

**首頁**
：登入使用者的主目錄。 Python 和其他依賴設定的 HOME 變數的腳本將自動選擇該變量，但它也可用於腳本中的其他用途。

**MARKED_EXT**
：正在處理的主檔案的副檔名。此變數可讓您根據正在查看的檔案類型編寫不同的進程腳本。例如，如果 `$MARKED_EXT == "md"` 運行您首選的 Markdown 處理器，但如果 `$MARKED_EXT == "textile"` 則執行 Textile 處理器。

**標記路徑**
：這是在載入時標記為開啟的主文件的完整 UNIX 路徑。

**標記_包括**
：使用各種 [include 語法](Special_Syntax.html#pagebreaks) 傳遞的文字中包含的已標記檔案的引用、逗號分隔清單。

**標記_階段**
：這將設定為“PROCESS”或“PREPROCESS”，讓您可以使用單一腳本來處理基於此變數的兩個階段。

**MARKED_CSS_PATH**
：目前樣式表的完整路徑

### 元資料環境變數

當在 Marked 中執行 Run Command 操作時
指揮系統，文件元資料自動
提取並作為環境變數提供給
命令。

#### 它是如何運作的

1. **元資料擷取**：系統使用現有的`extractMetaDataFromString:`方法從文件中擷取元數據，支援：
   - YAML 前面的內容（`---` 塊）
   - MultiMarkdown 元資料（關鍵：值線）
   - Pandoc 元資料（`%` 標題區塊）
   - HTML 評論元資料 (`<!-- key: value -->`)

2. **密鑰標準化**：元資料密鑰被標準化以用作環境變數：
   - 轉換為小寫
   - 所有非字母數字字元均被刪除
   - 空格和特殊字元被刪除

3. **環境變數格式**：每個元資料鍵成為一個帶有`MD_`前綴的環境變數：
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### 範例

給定一個包含此元資料的文件：

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

以下環境變數可用於
命令：

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### 指令中的用法

現在您可以在運行中使用這些環境變量
命令動作：

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### 支援的操作

這種元資料到環境變數的功能是
可用於：

- **運行命令**操作
- **執行嵌入式腳本**操作

元資料自動從文件中提取
內容並可供任何命令或腳本使用
貫穿這些動作。

## 啟用和停用

定制處理器可以打開和關閉
使用 {% kbd opt cmd C %} 的單一文件。你
也可以為文件開啟預處理器或處理器
自動[使用元資料](#perdocument) 在頂部
該文件。

每個文件的處理器的目前狀態是
顯示為指示燈（僅當處理器
已啟用）位於底部工具列項目的左側
預覽的右側工具列。

### 預處理器

如果您設定預處理器規則，它們將在標記後運行
處理任何特定於標記的任務，例如包括外部
文件和程式碼，但在運行處理器之前
（內部或自訂）。這使您有機會渲染
自訂模板變數，處理替換或註入
透過任何其他方式獲取您自己的內容。

標記為工作設定環境變數
目錄 (`MARKED_ORIGIN`) 到父目錄
正在預覽文件。您可以使用它來更改工作
腳本的目錄並包含具有相對路徑的文件
到原始文檔。舉個例子，在 Ruby 中你可以
使用：

	Dir.chdir(ENV['MARKED_ORIGIN'])

啟用後，可以開啟自訂預處理器並
關閉單一文件使用
{% kbd ctrl opt cmd C %}。

#### 每個文件處理器/預處理器 [每個文件]

還可以根據每個文件設定自訂處理器
使用元資料格式 [Per-Document
設定](Per-Document_Settings.html)。

您可以指定是否使用自訂處理器設定以及
使用 [Per-Document
設定](Per-Document_Settings.html)（`Custom Processor:`
和`Custom Preprocessor:`）。除“true”之外的任何設置
或“yes”將停用自訂預處理器/處理器。

用法範例：

    客製化處理器：true
    自訂預處理器： false

正如[每份文件
設定](Per-Document_Settings.html#hidingmeta)頁面，您
可以用 HTML 註解標記包圍此元資料以隱藏
從 GitHub 和其他不刪除它的處理器中刪除它
從輸出：

    <!--
    客製化處理器：true
    自訂預處理器：true
    -->

## 使用替代 Markdown 處理器

任何可以從命令列渲染的 Markdown 風格都可以
與標記一起使用。它需要能夠接受輸入
STDIN，與透過「管道」將 Markdown 傳輸到它相同
命令行，即`cat myfile.md | myprocessor`。它需要
在 STDOUT 上傳回產生的 HTML，其中每個
我曾經使用過的處理器預設是這樣的。

在終端中使用`which YOUR_PROCESSOR`來確定路徑
到可執行文件，然後將其貼上到運行命令路徑中
字段，或只需將可執行檔拖到“自訂規則”窗口
以及要新增所選操作的規則。

如果您的處理器需要命令列上的參數，
您還需要在欄位中輸入這些內容。一些
處理器需要連字符才能在 STDIN 和/或 STDOUT 上運行，
例如`-o - -` 通常訊號從 STDIN 輸入，輸出到
標準輸出。有關詳細信息，請參閱處理器的文檔。

我已經使用 Pandoc 測試了自訂處理器功能，
Kramdown、marked（折扣）、MultiMarkdown 6、Maruku 和
各種其他口味。

### 關於 Pandoc 和沙盒的說明

Pandoc（和其他一些命令列工具）將無法運行
Marked 的 Mac App Store（沙盒）版本。
如果您需要運行 Pandoc，請使用 **Help->Crossgrade** 獲取
直接（Paddle）版本的免費授權。這是真的
遇到沙箱問題的任何處理器：如果標記
由於 MAS 權限問題無法執行它，它將
提供跨層級的步驟。如果您遇到問題
但這並沒有發生，請透過以下方式與我聯繫
[支援網站](https://support.markedapp.com/questions/add)。

### Pandoc 作為瑞士陸軍 Markdown 處理器

[Pandoc](https://pandoc.org/) 是迄今為止最靈活的
用於處理一系列標記格式的通用工具。由
加入 `-f` 參數與以下之一，Pandoc 可以
成為以下任何一項的客製化處理者：

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

還有其他一些人。參見[潘多克
文件](https://pandoc.org/MANUAL.html) 了解更多
資訊。要使用其中一種作為輸入格式，只需添加
在「運行命令」欄位中輸入以下內容：

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc 非常適合編寫使用以下內容的腳本
`$MARKED_EXT`環境變數來決定哪一種格式
運行 Pandoc，或使用一系列規則
擴展匹配。如果副檔名是 `md`，則使用
`pandoc -f gfm` 或 `pandoc -f markdown_mmd` （或直接返回
STDOUT 上的 `NOCUSTOM` 使用預設處理器）。但如果是
`textile`，在腳本中運行`pandoc -f textile`。如果
它是 `wiki`，使用 wiki 標記處理器之一。你得到
這個想法。

Pandoc 愛好者都知道，Pandoc 還可以處理
廣泛的參考書目和 LaTeX 場景。大多數功能
您可以透過命令列存取即可
透過在 Marked 中使用傳遞參數。

## 使用紡織品

有幾個人問如何讓 Textile 工作
標記。您需要有一個紡織轉換器，可從
命令行。有幾個選項，包括 Pandoc
（請參閱上文），但如果您還沒有安裝 Pandoc，
另外兩個選項是用於 Ruby 的 RedCloth 和 Perl 的 Textile
（需安裝開發人員工具）。安裝
一個或另一個：

1. 從下列位置安裝 Textile
   <https://github.com/bradchoate/text-textile> **或**
   航廈`sudo gem install RedCloth`
2. 使用`which textile`或`which redcloth`確定
   自訂處理器路徑設定中使用的路徑

Now Marked 是一款適合您的紡織品預覽器！

## 使用 AsciiDoc

1.安裝【AsciiDoctor】(http://asciidoctor.org/)。
2. 在 {% prefspane Processor %} 中啟用自訂規則以符合您的 AsciiDoc 檔案。
3. 將規則設定為處理器並新增運行命令操作
    1. 確定到`asciidoc`的路徑，即
       像 `/usr/bin/asciidoc` 或
       `/opt/local/bin/asciidoc`。如果不確定，請使用
       `which asciidoc` 定位
    2. 輸入 `[PATH To asciidoc] --backend html5 -o - -` 作為
       命令（末尾的 - 發送輸出為
       標準輸出）

這會將當前文件傳送到 STDIN 並顯示
產生 HTML 作為 STDOUT。

請參閱[此要點](https://gist.github.com/mojavelinux/6324279)
來自 [丹艾倫](https://gist.github.com/mojavelinux) 的
更多資訊。