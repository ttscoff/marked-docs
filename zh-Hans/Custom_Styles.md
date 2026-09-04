# <%= @title %>

按*你自己*的方式查看文档。

## 使用自定义样式 [using-custom-styles]

![][img1]

  [img1]: images/custom_styles.jpg @2x width=544px height=196px class=center

探索自定义样式最简单的方法是通过[自定义样式库][2]。在那里你可以浏览各种样式的实际效果,点击按钮即可安装,甚至还能[提交你自己的作品][6]供收录。

要将本地磁盘上的自定义样式表添加到 Marked,请使用{% prefspane Style %}。新样式会被添加到「窗口」设置以及每个窗口的下拉菜单中,并根据所添加 CSS 文件的基础文件名命名。请将自定义 CSS 文件保存在磁盘上一个安全的位置。如果它们在磁盘上被移动,就会从 Marked 中移除,直到你从新位置重新添加它们为止。在删除或重命名 Marked 使用的 CSS 文件之前,最好先关闭已打开的文档,并从设置中移除该样式。即使不这样做也不会造成任何问题,但这样可以避免一些混淆。

使用样式管理器中的「添加」按钮来添加自定义样式,或者将一个或多个 CSS 文件拖放到设置面板上。

## 使用样式管理器管理样式 [managing-styles-with-the-style-manager]

启动样式管理器可以让你在一个地方集中管理所有内置和自定义主题。点击{% prefspane Style %}面板中的**管理样式…**按钮,或者直接将 CSS 文件拖放到偏好设置窗口 --- Marked 会导入它们,打开样式管理器,并为你选中新添加的那一行。将 CSS 文件直接拖放到样式管理器窗口上同样有效;当拖入多个文件时,叠加提示会更新为「添加 N 个自定义样式」,让你清楚知道自己正在批量导入。

![][img-style-manager]

在样式管理器中,你会看到一个可排序的表格,内置样式与自定义样式混合列出。每一行都提供以下操作:

- 一个**启用**复选框,可立即在「样式」菜单、默认样式弹出菜单以及键盘快捷键中添加或移除该样式。禁用当前正在使用的样式会自动切换到下一个可用的样式。
- 一个可就地编辑的**名称**列;更改会被保存,并同步到所有菜单。点击样式名称即可就地编辑。
- 一个**来源**列,标明该样式是内置、自定义还是重复项。
- 一组**操作**按钮,包括**编辑**(在你的编辑器中打开 CSS 文件)、**复制**(在磁盘上创建一份副本和新的 CSS 文件)、**显示**(在访达中显示该文件),以及**删除**(可选择仅移除引用,或将 CSS 文件移到废纸篓)。

行可以通过拖放重新排序,排序结果会决定「样式」菜单以及`⌘/#`快捷键的分配顺序,因此你可以直接将样式拖到想要的位置。你也可以将外部 CSS 文件拖放到指定位置;放置指示线会决定新样式插入的位置。

### 实时预览 [live-preview]

右侧面板中是一个预览区域,会在一个包含丰富标题、列表、表格、代码块等元素的完整 HTML 文档中渲染所选样式。预览使用的是磁盘上实际的 CSS 文件,因此你在外部编辑器中所做的修改会立即生效。一个复选框可用于切换深色模式预览。

你可以在 [GitHub][1] 上找到更多可用样式(或作为创作你自己样式的参考示例)(可以看看 [示例][2] 快速了解那里都有些什么)。详情和技巧请参阅[创建自定义 CSS][3]。

## 附加 CSS [additional-css]

在{% prefspane Style %}中,你会看到一个名为「附加 CSS」的选项,旁边有一个标有「编辑 CSS」的按钮。点击此按钮会打开一个窗口,你可以在其中添加通用的 CSS 规则,这些规则会应用到所有样式上。请注意,在覆盖 Marked 的部分默认样式时,规则的优先级(specificity)可能很重要。文档的主体被包裹在一个 id 为 "#wrapper" 的 div 中。在选择器前加上这个前缀可以更方便地进行覆盖,例如:

    #wrapper img { width: 100%; height: auto; }

此字段中的 CSS 会**附加到当前启用的主题之上**。它并不能替代完整的自定义样式:专门为此字段编写的样式表本身就是不完整的,如果通过样式管理器将其作为主题加载,它未覆盖到的部分都会没有样式。

Marked 会在注入之前**重写**附加 CSS 的选择器。像 `.mkprinting` 这样开头的 body 类会被合并到 `body` 上,而不是嵌套在 `#wrapper` 之下,因此该字段中的打印规则应使用 `body.mkprinting #wrapper …`(完整的重写规则参见[创建自定义 CSS](Writing_Custom_CSS.html#additional-css-settings))。该字段没有大小限制,也不做有效性检查 --- 无效的 CSS 只是不会产生任何效果。

此字段中的 CSS 会应用于每一篇文档,无论它使用的是哪种样式 --- 包括包含样式的 HTML 导出。如果你想根据条件匹配来应用自定义 CSS,可以在{% prefspane Processor %}自定义规则中使用「设置样式」「插入 CSS 文件」或「插入 CSS」操作。

## 打印和 PDF 导出 [print-and-pdf-export]

Marked 会在每次预览时注入一个内置的 `@media print` 代码块(`mkprintstyles`)。它会设置一些默认值,例如在 `html`、`body` 和 `#wrapper` 上使用 **10pt** 的基础字号(如果启用了{% prefspane Export %}中的**导出/打印自定义字体大小**选项,则使用该选项指定的大小),并使用 `p { font-size: 1em; }` 和 `li p { font-size: 1em; }` 规范化段落文本,这样像 `p { font-size: 1.1429em; }` 这样的仅屏幕规则就不会在 PDF 和打印输出中把正文放大。

PDF 导出时,用于生成的隐藏 WebView 可能使用 **print** 或 **screen** 媒介。内置主题通常使用 print 媒介;**自定义样式**以及 [Fountain](Fountain_for_Screenwriters.html) 文档则经常使用 screen 媒介,以使布局与预览保持一致。这意味着在 PDF 导出过程中,`@media print { ... }` 规则并不总是会生效。

为了确保 PDF 及打印/PDF 预览的样式生效可靠,请在选择器前加上 Marked 在导出期间添加到 `<body>` 上的 `mkprinting` 类(详情和示例参见[编写自定义 CSS](Writing_Custom_CSS.html#printstyles))。在**自定义样式**文件中,你可以单独使用 `.mkprinting`。在**附加 CSS**中,由于该字段会重写选择器,应使用带 body 限定的形式 `body.mkprinting #wrapper …`。当你需要同时覆盖两种路径时,也可以将其中任意一种形式与 `@media print` 结合使用。

如果要设置与 Marked 打印默认值不同的字号,请在你的自定义 CSS(或附加 CSS)中添加明确的规则。当需要覆盖 Marked 注入的打印样式时,请使用 `!important` --- 例如:

```css
@media print {
  #wrapper p,
  body p,
  p {
    font-size: 9pt !important;
    line-height: 1.4 !important;
  }

  h1 {
    font-size: 16pt !important;
  }
}

/* Custom Style (and most theme stylesheets) */
.mkprinting #wrapper p,
.mkprinting body p,
.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

.mkprinting h1 {
  font-size: 16pt !important;
}

/* Additional CSS field (selector rewriting) */
body.mkprinting #wrapper p,
body.mkprinting p {
  font-size: 9pt !important;
  line-height: 1.4 !important;
}

body.mkprinting #wrapper h1,
body.mkprinting h1 {
  font-size: 16pt !important;
}
```

没有 `!important` 的规则,可能会被 `mkprintstyles` 中后出现的规则,或者你样式表中其他在打印时仍然生效的无限定选择器规则所覆盖。将仅用于打印的调整放在 `@media print` 和/或 `.mkprinting` / `body.mkprinting` 规则中(而不是只放在屏幕规则里),可以让预览与导出行为更容易理解和把控。

## 监听 CSS 变更 [watching-css-changes]

你可以在{% prefspane Style %}的「自定义样式」部分勾选一个选项,让 Marked 除了监听你正在编辑的 Markdown 文件外,也监听当前使用的 CSS 文件。当任一文件发生变化时,预览都会自动更新。这在编辑自定义样式时非常有用,可以避免不断手动刷新,也可以用于一些简单的网页开发任务。

这对一些基础的网页设计工作和 CSS 实验(比如创建自定义样式)也很有帮助。加载一个包含你想要设置样式的所有标记的 Markdown 文件,创建一个自定义样式,然后在编辑过程中实时查看预览的变化。

## 编写自定义 CSS [writing-custom-css]

如果你熟悉 CSS,就可以创建属于自己的样式表在 Marked 中使用。详情请参阅[编写自定义 CSS][3]。每当你创建出新样式时,不妨考虑将其[提交][6]到[样式库][2],与其他用户分享。请务必按照指南中列出的基本要求进行编写,并在文件顶部包含元数据注释。

### 使用 StyleStealer 自动生成自定义样式 [automatic-custom-styles-with-stylestealer]

你甚至可以使用 [Style Stealer][4] 根据现有网站自动生成样式。它可以让你加载一个网页,抓取 Markdown 中常见各主要元素的计算样式,然后将其保存为自定义样式。

![Style Stealer][stylestealer]

  [stylestealer]: images/style-stealer-800.jpg @2x width=800


你可以在[样式管理器](Style_Manager.html)中管理自定义样式(重命名、重新排序、复制和删除)。

[1]: https://github.com/ttscoff/MarkedCustomStyles
[2]: https://markedapp.com/styles/
[3]: Writing_Custom_CSS.html
[4]: Style_Stealer.html
[6]: https://markedapp.com/styleshare/
[img-style-manager]: images/screenshots/style-manager.jpg @2x width=1009px height=517px class=center
