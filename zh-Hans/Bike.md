# <%= @title %>

把 [Bike][bike] 大纲拖到 Marked 上，即可预览为嵌套的 Markdown 列表，标题行用粗体，任务用复选框。单独的大纲是 `.bike` 文件。大纲含有嵌入图片时，Bike 2 会保存 `.biked` 包。

## 打开 Bike 大纲 [opening-a-bike-outline]

打开文件时，Marked 会转换这份大纲：

- 标为标题的行变成**粗体**列表项。
- 任务变成 GitHub 样式的复选框。Bike 保存了完成时间，或把任务标为已完成时，复选框为选中。
- 行文字里的链接和行内格式会保留为 Markdown。

打开 `.bike` 文件时始终使用这种列表。大纲不会变成 Mermaid 图。`.biked` 包遵循下面说明的 **Bike outlines** 设置。

## 嵌入 Bike 大纲 [including-a-bike-outline]

`.bike` 文件也可以嵌进另一份 Markdown 文稿。请参阅[嵌入思维导图和大纲](Embedding_Mind_Maps_and_Outlines.html)。

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下，**Bike outlines** 作用于嵌入的文件：

- **打开**（默认）— Mermaid 图。去掉 `.bike` 后的文件名是根节点。
- **关闭** — 与打开文件时相同的嵌套 Markdown 列表，没有文稿标题。

## 含有图片的大纲 [outlines-with-images]

大纲含有嵌入图片时，Bike 2 会保存 `.biked` 包。这个包是 TextBundle：`text.bike` 和一个 `assets` 文件夹。请打开 `.biked` 文件本身。Marked 读取里面的大纲，并用包名作为窗口标题。

要保留图片，请关闭 **Bike outlines**。预览就是嵌套列表。设为**打开**时，大纲会变成 Mermaid 图。

[bike]: https://www.hogbaysoftware.com/bike/
