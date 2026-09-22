# <%= @title %>

Marked 会从你的**实时预览**导出 HTML —— 也就是你在屏幕上看到的渲染结果。当你需要粘贴到博客或 CMS 中的代码片段，或者需要一个包含内嵌样式和图片的独立 `.html` 文件（可在任意浏览器中打开或托管到任意位置）时，就可以使用 HTML 导出。

典型的工作流程是**先预览、后导出 HTML**：在 Marked 中打开或编译你的文档，选择一个主题，在实时预览中校对，等排版没问题后再导出。

## 获取 HTML 的两种方式 [two-ways-to-get-html]

### 复制 HTML（代码片段） [copy-html-snippet]

**复制 HTML** 会把预览的 HTML 源码放到剪贴板中 —— 可以直接粘贴到 WordPress、Ghost、Squarespace、论坛、邮件模板，或任何接受 HTML 片段的应用中。

* 齿轮菜单 → **复制 HTML**，或在预览获得焦点时按 {% kbd shift cmd C %}
* 复制的是**渲染后的正文 HTML**（不是带有 `<html>` 包装的完整文档）
* 可选：在 {% prefspane Export %} 中启用**复制 HTML 时嵌入图片**，可将本地图片编码为 Base64 格式的 `data:` URL 写入粘贴的源码中

当目标位置已经有自己的样式表、你只需要内容标记时，复制 HTML 是最合适的选择。

### 保存 HTML（文件） [save-html-file]

**保存 HTML** 会把完整的 `.html` 文件写入磁盘。

* 导出 → **保存 HTML**、{% kbd cmd S %}，或在[导出面板](Exporting.html#drawer)（{% kbd shift cmd e %}）中选择 **HTML**
* 在保存对话框中选择文件名和保存位置
* 在对话框的附加选项中配置导出设置（见下文）

保存 HTML 适合用来归档、分享独立文件，或直接在浏览器中打开查看结果。

## 保存 HTML 选项 [save-html-options]

保存 HTML 对话框包含一个导出配置选择器，以及以下选项：

![Save HTML options][savehtml]

**在输出中包含样式**

勾选此项后，Marked 会把所选预览主题的 CSS 内嵌到导出文件中的 `<style>` 代码块里。你可以从复选框旁边的样式菜单中选择任意内置主题或[自定义样式](Custom_Styles.html)。输出结果是一个完整的 HTML 文档，包含 `<!DOCTYPE html>`、`<head>`，以及包裹内容的 `#wrapper` 容器 —— 与你在预览中看到的效果一致。

取消勾选时，Marked 只保存一个仅含渲染内容的极简 HTML 文档（不含 Marked 主题 CSS）。当你需要把原始 HTML 粘贴或导入到自带样式的其他系统中时，可以使用这个选项。

**为独立 HTML 嵌入本地图片**

启用**在输出中包含样式**后，你还可以将本地图片以 Base64 格式的 `data:` URL 嵌入 HTML 文件中。这样得到的是单个文件，无需单独的 `images/` 文件夹即可发送邮件、上传或托管。

* 适用于通过**相对或绝对路径**引用的本地磁盘上的图片
* 避免使用 `file:///` 格式的 URL —— 它们无法被可靠地嵌入
* 远程图片（http/https）会保留为外部 URL，除非你先将其下载下来
* Base64 嵌入可能会生成较大的文件；当可移植性比文件大小更重要时再使用此选项

**包含语法高亮 JavaScript**

当 {% prefspane Preview %} 中启用了语法高亮时，此选项会从 CDN 添加 highlight.js 的 CSS 和 JavaScript，使代码块在导出的文件中保留颜色。导出的 HTML 需要联网才能加载这些 CDN 资源。

**包含 MathJax 或 KaTeX CDN 链接**

当预览中启用了 [MathJax](MathJax.html) 或 KaTeX 时，你可以在保存的 HTML 中包含对应的 CDN 脚本，使公式能在浏览器中正常渲染。与语法高亮一样，除非你自行托管这些脚本，否则查看该文件时需要联网。

**CriticMarkup 导出类型**

包含 [CriticMarkup](CriticMarkup.html) 的文档可以选择导出时显示已编辑文本、原始文本，还是完整标记。

**导出配置**

选择一个已保存的[导出配置](Exporting.html#export-profiles)，一步恢复你偏好的 HTML 导出设置（内嵌样式、图片、语法高亮、数学公式）。

## 使用内置和自定义主题设置样式 [styling-with-built-in-and-custom-themes]

当勾选**在输出中包含样式**时，**预览样式**决定了 HTML 的外观：

1. 从预览窗口的样式菜单中选择一个样式（或在 {% prefspane Style %} 中设置默认样式）。
2. 在实时预览中检查排版、标题、代码块和图片效果。
3. 保存 HTML 时，在导出对话框中选择相同的样式。

所有 Marked 内置主题 —— Swiss、GitHub、Manuscript 等等 —— 都可以被嵌入。[自定义样式](Custom_Styles.html)以及来自[样式管理器](Custom_Styles.html)的样式也是同样的用法。

嵌入样式时，{% prefspane Style %} 中的**附加 CSS** 也会包含在 HTML 导出结果中。导出的 `<body>` 会带有 `mk-has-additional-css` 类，以便与 Marked 重写后的附加 CSS 选择器相匹配。参见[创建自定义 CSS](Writing_Custom_CSS.html#additional-css-settings)。

I> 部分仅用于预览的 CSS（固定定位、视口相关技巧、深色模式下的 `@media screen` 反色处理）在 Marked 之外可能无法完全一致地呈现。发布前建议在浏览器中打开保存的文件核实效果。

关于编写指南，参见[创建自定义 CSS](Writing_Custom_CSS.html)。

## 元数据与 MultiMarkdown 头部信息 [metadata-and-multimarkdown-headers]

源文件顶部的 MultiMarkdown 元数据可能会影响 HTML 导出：

* **`Title:`** —— 保存完整 HTML 文档时用作 `<title>` 元素的内容
* **`XHTML Header:`** / **`HTML Header:`** —— 向导出的 `<head>` 中注入额外的标签（脚本、link 标签、meta 标签）
* 其他元数据键会根据你所用的 [Markdown 处理器](Choosing_a_Processor.html)进行处理

如果你使用元数据来设置导出选项，但不希望这些键出现在其他输出中，可以将它们包裹在 HTML 注释里 —— Marked 会在文档任意位置查找并处理被注释的元数据。参见[单文档设置](Per-Document_Settings.html)。

## 多文件文档 [multi-file-documents]

对于书籍和分章合集，可以使用[多文件文档](Multi-File_Documents.html)。Marked 会预览合并后的文档，并从编译结果导出单个 HTML 文件。合并进来的文件会用 HTML 注释标注其源文件路径 —— 在核查各章节内容来源时很有用。

## 粘贴到其他应用中 [pasting-into-other-applications]

| 目标位置 | 建议方法 |
| :-- | :-- |
| 有自带主题的博客 / CMS | **复制 HTML**（代码片段，不含内嵌 Marked CSS） |
| 静态网站或归档 | **保存 HTML**，并启用**在输出中包含样式** |
| 邮件或文件分享（单个附件） | **保存 HTML**，并启用**嵌入本地图片** |
| WordPress、Ghost、Notion 等 | **复制 HTML**；如果编辑器无法解析本地路径，可启用**复制 HTML 时嵌入图片** |
| 在代码编辑器中进一步编辑 | **保存 HTML** 时不嵌入样式，或复制代码片段后手动包装 |

如果目标应用接受格式化文本而非 HTML 源码，[复制富文本](Exporting.html#rtfexportoptions)（齿轮菜单）是另一种选择。

## 相关主题 [related-topics]

* [导出](Exporting.html) —— 导出面板、导出配置及其他格式
* [EPUB 导出](EPUB_Export.html) —— 带内嵌 CSS 的电子书输出
* [Mac 上的实时 Markdown 预览](Live_Markdown_Preview_on_Mac.html) —— 导出前的预览工作流程
* [自定义样式](Custom_Styles.html) 和 [设置：导出](Settings_Export.html)
* [HTML 专属设置](HTML_Specific_Settings.html) —— 针对 HTML 输出的处理器选项
* [AppleScript 导出](AppleScript_Support.html) —— 自动化 HTML 复制与保存

[savehtml]: images/SaveHTML.png @2x width=740px height=229px
