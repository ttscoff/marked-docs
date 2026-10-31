# <%= @title %>

把 [Bike][bike] 大綱（`.bike`）拖到 Marked 上，即可預覽為巢狀 Markdown 清單，標題列用粗體，工作項目用核取方塊。

## 開啟 Bike 大綱 [opening-a-bike-outline]

開啟檔案時，Marked 會轉換這份大綱：

- 標成標題的列會變成**粗體**清單項目。
- 工作項目會變成 GitHub 樣式的核取方塊。Bike 存有完成時間，或把項目標成已完成時，核取方塊為選取。
- 列文字裡的連結和行內格式會保留為 Markdown。

開啟 `.bike` 檔案時一律使用這種清單。大綱不會變成 Mermaid 圖。

## 嵌入 Bike 大綱 [including-a-bike-outline]

`.bike` 檔案也可以嵌進另一份 Markdown 文稿。請參閱[嵌入心智圖和大綱](Embedding_Mind_Maps_and_Outlines.html)。

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下，**Bike outlines** 作用於嵌入的檔案：

- **開啟**（預設）— Mermaid 圖。去掉 `.bike` 後的檔名是根節點。
- **關閉** — 與開啟檔案時相同的巢狀 Markdown 清單，沒有文稿標題。

Mermaid 圖需要 MultiMarkdown、CommonMark (GFM) 或 Kramdown。Discount 處理器不會繪製它們。

[bike]: https://www.hogbaysoftware.com/bike/
