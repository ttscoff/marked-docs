<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>

标记为您提供选项。

## 实时预览工作流程

1. 将 Markdown 文件拖到 Marked 上（或使用 {% appmenu File, Open... ({{cmd}}O) %}）。
2. 在您喜欢的编辑器中编辑文件。
3. 保存---标记为自动更新预览。

请参阅 [Mac 上的实时 Markdown 预览](Live_Markdown_Preview_on_Mac.html) 了解 Vault 观看、流媒体预览和特定于编辑器的指南。

## 拖至 Dock 图标

在已编辑的文件上使用“标记”的最简单方法是将文档图标从编辑器的工具栏或从 Finder 拖动到 Dock 中的“标记”图标。 Marked 将立即开始跟踪放置在其上的任何 Markdown 文件（或文本文件）。您还可以直接从 Finder 中拖动文件。

## 使用菜单

![][2]

   [2]: images/file_open.jpg @2x width=300px height=118px class=center

当然，您可以使用 {% appmenu File, Open... ({{cmd}}O) %} 菜单选项直接打开 Markdown 文件。标记也可以在没有文本编辑器的情况下正常工作。只需单击一下即可预览和转换 Markdown。

Marked 还可以直接打开 **`.rtf` 和 `.rtfd`** 文件（例如从 Pages 或 TextEdit 导出）。当您保存在原始应用程序中时，它们会转换为 Markdown 以便预览和更新。请参阅[RTF 和 RTFD 支持](RTF_Support.html) 了解详细信息，包括图像和限制。

标记可以以相同的方式打开 **`.pdf`** 文件：转换在后台运行，完成后预览会更新。这最适合较短的、基于文本的 PDF；大型手册和扫描文档速度较慢且不太准确。有关详细信息和限制，请参阅 [PDF 支持](PDF_Support.html)。

## 从剪贴板

如果您的剪贴板中有兼容的（例如 Markdown）文本，您可以通过选择 {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} 打开即时预览。如果您从 Web 浏览器或其他将 HTML 或 RTF 放在剪贴板上的应用程序复制了选定内容，Marked 会将其转换为 Markdown 以供预览。当您从 TextEdit 或 Pages 等应用程序粘贴 RTF 时，较大的字体大小将粗略地转换为标题级别（例如，非常大的文本变为 1 级标题，较小的大文本变为 2 级标题，依此类推）。您可以一次打开多个剪贴板预览，并且可以通过选择 {% appmenu File, Save Transient Preview %} 将它们保存到新文件中。

## 创建一个新文档

标记允许您使用 {% appmenu File, New ({{cmd}}N) %} 命令创建一个新的空文本文件。它会立即询问您保存文件的位置，您可以在“文本编辑器”按钮旁边的{% prefspane Apps %}中启用“自动编辑新文件”选项，以在默认编辑器中自动打开新创建的文件。

## 打开最近的

![][3]

   [3]: images/open_recent.jpg @2x width=300px height=174px class=center

Marked 也会跟踪最近的文档。 {% appmenu File, Open Recent %} 菜单选项将向您显示已打开的文件，并让您跳回到它们。您可以快速重新打开使用{% kbd shift cmd R %}查看的最后一个文件。使用{% kbd shift cmd P %}或[快速操作](Quick_Actions.html)从键盘运行菜单和预览命令。还有很多其他键盘快捷键。如果您想了解它们，可以在[键盘]下找到图表快捷方式](Keyboard_Shortcuts.html)。

## 当前文件的新视图 [多视图]

使用 {% appmenu File, New View into Current File %}（{% kbd
shift cmd N %}，也在预览上下文菜单中）打开
同一保存文件的第二个预览窗口。两个窗户
观看磁盘上的文件并在保存时更新
编辑器，但每个视图保留自己的滚动位置，
书签、预览样式和[自定义规则
覆盖](Custom_Processor.html#manuallyenabled)。

**用例示例：** 您正在编辑一篇长稿件
MultiMarkdown 具有您常用的风格和处理器。打开一个
第二个视图，将其切换到校对样式，固定流程
运行不同内置处理器的规则，并启用
突出显示修订标记的手动规则。你比较
并排草稿和校样布局，无需维护两个
文件的副本。

当打开一个文件的多个视图时，窗口标题
包括 **视图 2**、**视图 3** 等，以便您可以辨别
窗口菜单和任务控制中的窗口分开。

备用视图不适用于未保存的文档，
剪贴板预览、流式预览或基于文件夹的预览
不映射到磁盘上的单个文件的项目。

## 快速打开 ##

您可以在打开的文档之间快速切换、打开最近使用的文档或使用[快速打开面板](Quick_Open.html)（{% kbd cmd shift o %}）打开文件->打开对话框。