# <%= @title %>

把 [Bike][bike] 大綱拖到 Marked 上，即可預覽為巢狀 Markdown 清單，標題列用粗體，工作項目用核取方塊。單獨的大綱是 `.bike` 檔案。大綱含有嵌入圖片時，Bike 2 會儲存 `.biked` 套件。

## 開啟 Bike 大綱 [opening-a-bike-outline]

開啟檔案時，Marked 會轉換這份大綱：

- 標成標題的列會變成**粗體**清單項目。
- 工作項目會變成 GitHub 樣式的核取方塊。Bike 存有完成時間，或把項目標成已完成時，核取方塊為選取。
- 列文字裡的連結和行內格式會保留為 Markdown。

開啟 `.bike` 檔案時一律使用這種清單。大綱不會變成 Mermaid 圖。`.biked` 套件遵循下面說明的 **Bike outlines** 設定。

## 嵌入 Bike 大綱 [including-a-bike-outline]

`.bike` 檔案也可以嵌進另一份 Markdown 文稿。請參閱[嵌入心智圖和大綱](Embedding_Mind_Maps_and_Outlines.html)。

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下，**Bike outlines** 作用於嵌入的檔案：

- **開啟**（預設）— Mermaid 圖。去掉 `.bike` 後的檔名是根節點。
- **關閉** — 與開啟檔案時相同的巢狀 Markdown 清單，沒有文稿標題。

## 含有圖片的大綱 [outlines-with-images]

大綱含有嵌入圖片時，Bike 2 會儲存 `.biked` 套件。這個套件是 TextBundle：`text.bike` 和一個 `assets` 資料夾。請開啟 `.biked` 檔案本身。Marked 會讀取裡面的大綱，並用套件名稱作為視窗標題。

要保留圖片，請關閉 **Bike outlines**。預覽就是巢狀清單。設為**開啟**時，大綱會變成 Mermaid 圖。

[bike]: https://www.hogbaysoftware.com/bike/
