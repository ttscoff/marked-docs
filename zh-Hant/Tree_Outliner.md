# <%= @title %>

把 [Tree Outliner][tree] 文稿（`.treeoutline`）拖到 Marked 上，即可預覽為標題和清單，或預覽為 Mermaid 圖。

## 標題和清單 [headings-and-lists]

這是預設方式。Marked 把大綱編譯成 Markdown：

- 文稿標題是 1 級標題。
- 大綱各列繼續作為標題，直到 {% prefspane Apps %} 裡 *Tree Outliner* 群組中的 **Headings through level** 所設層級。預設是 **2**，因此大綱的第一列是 2 級標題，更深的列變成巢狀清單。
- 某一列上的筆記會變成該標題或清單項目下的段落。

## Mermaid 圖 [mermaid-diagram]

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下打開 **Tree Outliner outlines**，即可把檔案預覽為 Mermaid 圖。文稿標題是根節點。開啟 `.treeoutline` 檔案，以及把它[嵌入](Embedding_Mind_Maps_and_Outlines.html)另一份文稿時，用的是同一個開關。

只有這個開關關閉時，才會用到 **Headings through level**。

Mermaid 圖需要 MultiMarkdown、CommonMark (GFM) 或 Kramdown。Discount 處理器不會繪製它們。

[tree]: https://noteifyapp.com/tree-outliner/
