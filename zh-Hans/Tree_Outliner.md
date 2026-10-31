# <%= @title %>

把 [Tree Outliner][tree] 文稿（`.treeoutline`）拖到 Marked 上，即可预览为标题和列表，或预览为 Mermaid 图。

## 标题和列表 [headings-and-lists]

这是默认方式。Marked 把大纲编译成 Markdown：

- 文稿标题是 1 级标题。
- 大纲各行继续作为标题，直到 {% prefspane Apps %} 里 *Tree Outliner* 分组中的 **Headings through level** 所设级别。默认是 **2**，因此大纲的第一行是 2 级标题，更深的行变成嵌套列表。
- 某一行上的笔记会变成该标题或列表项下的段落。

## Mermaid 图 [mermaid-diagram]

在 {% prefspane Apps %} 的 *Mind Maps and Outlines* 下打开 **Tree Outliner outlines**，即可把文件预览为 Mermaid 图。文稿标题是根节点。打开 `.treeoutline` 文件，以及把它[嵌入](Embedding_Mind_Maps_and_Outlines.html)另一份文稿时，用的是同一个开关。

只有这个开关关闭时，才会用到 **Headings through level**。

Mermaid 图需要 MultiMarkdown、CommonMark (GFM) 或 Kramdown。Discount 处理器不会绘制它们。

[tree]: https://noteifyapp.com/tree-outliner/
