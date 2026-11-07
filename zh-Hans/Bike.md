# <%= @title %>

把 [Bike][bike] 大纲（`.bike`）拖到 Marked 上，即可预览为嵌套的 Markdown 列表，标题行用粗体，任务用复选框。

## 打开 Bike 大纲 [opening-a-bike-outline]

打开文件时，Marked 会转换这份大纲：

- 标为标题的行变成**粗体**列表项。
- 任务变成 GitHub 样式的复选框。Bike 保存了完成时间，或把任务标为已完成时，复选框为选中。
- 行文字里的链接和行内格式会保留为 Markdown。

打开 `.bike` 文件时始终使用这种列表。大纲不会变成 Mermaid 图。

## 嵌入 Bike 大纲 [including-a-bike-outline]

`.bike` 文件也可以嵌进另一份 Markdown 文稿。请参阅[嵌入思维导图和大纲](Embedding_Mind_Maps_and_Outlines.html)。

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下，**Bike outlines** 作用于嵌入的文件：

- **打开**（默认）— Mermaid 图。去掉 `.bike` 后的文件名是根节点。
- **关闭** — 与打开文件时相同的嵌套 Markdown 列表，没有文稿标题。

Mermaid 图需要 MultiMarkdown、CommonMark (GFM) 或 Kramdown。Discount 处理器不会绘制它们。

[bike]: https://www.hogbaysoftware.com/bike/
