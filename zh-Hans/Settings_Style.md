# 设置样式面板中的选项：

![Settings: Style][1]

[1]: images/screenshots/preferences-Style.jpg @2x width=689px height=1031px class=preferencepane-scroll

### 版面与排版 [layout-and-typography]

限制预览中的文本宽度
: 使用滑块设置预览正文的最大宽度（以像素为单位）。

段落中自动连字
: 允许单词自动使用连字符换行。

防止标题和段落中出现孤行词
: 在标题和段落最后两个词之间强制插入不换行空格，防止单个词单独换到下一行。

生成排版正确的引号和标点
: 使用 SmartyPants 实现智能引号、省略号转换及其他排版功能（MultiMarkdown）。

用方括号包裹脚注标记
: 勾选后，使用 MultiMarkdown 默认格式显示脚注标记（[1]）。取消勾选可去除方括号。

为指定扩展名启用大纲
: 对列出扩展名的文件自动开启大纲模式。

使用 APA 样式
: 使用 APA 样式大纲，而非默认的十进制格式。

将逐字（代码）块显示为诗歌样式
: 勾选后，制表符缩进、围栏或包含的代码将以诗歌样式显示，而非代码块样式（无语法高亮，样式因主题而异）。

允许主题在代码块内换行
: 勾选后，允许主题在 `pre>code` 块内换行显示文本。取消勾选则始终以横向滚动方式处理溢出内容。

始终换行显示代码
: 强制代码块换行，无论主题设置如何（会覆盖主题的换行行为）。

检测并按 RTL 样式显示文本
: 按文档中每个元素检测语言，并相应地以从右到左方式显示。

### 主题 [theme]

管理样式
: 打开[样式管理器](Style_Manager.html)窗口。将磁盘上的 CSS 文件添加进来，即可使其出现在样式选择菜单中。使用 `Add New Style` 按钮，或将 CSS 文件拖入此窗口即可添加。拖动可调整顺序，使用复选框可启用或禁用样式。

更多主题
: 打开在线主题库，浏览并安装更多样式。

默认样式
: 除非[文档元数据中指定了专属样式](Per-Document_Settings.html)（例如 "Marked Style: Grump"），否则所有新窗口都会加载此处选择的样式。

跟踪 CSS 更改
: 启用后，Marked 会监视当前样式文件在磁盘上的更改，便于自定义样式编辑和 Web 开发。

附加 CSS
: 此处添加的 CSS 会附加在每个主题的常规样式表之后。它只是局部叠加层，并非完整主题的替代品。
: Marked 会重写此字段中的选择器（例如，打印规则应使用 `body.mkprinting #wrapper …`）。此处没有大小或有效性限制 —— 参见[创建自定义 CSS](Writing_Custom_CSS.html#additional-css-settings)。
: 这会应用于所有文档和所有样式，包括在导出 HTML 时包含样式的情况。如果想根据条件对文档应用自定义 CSS，请使用 {% prefspane Processor %} 下的自定义规则。

### 引入脚本 [include-scripts]

语法高亮
: 为代码块开启 highlight.js [语法高亮](Syntax_Highlighting.html)功能。从下拉菜单中选择一种主题。
: 若勾选**仅在指定语言时**，则只会对指定了语言的围栏代码块应用语法高亮。

启用 MathJax
: 加载 [MathJax](MathJax.html) 以显示 MathML 公式。从下拉菜单中选择**本地**（内置）或 **CDN**。
: **附加包**会打开一个表单，用于加入额外的 MathJax 包（例如物理和化学）。
: **高级配置**会打开一个表单，用于自定义 MathJax 配置。

启用 KaTeX
: 加载 [KaTeX](MathJax.html#katex) 作为 MathJax 的替代方案。两者只能选择其一。

公式编号
: 若适用，Marked 会为渲染的公式添加图号。可选择**左侧**或**右侧**进行编号。使用 MathJax 时，可选择**仅 AMS**，仅对 AMS 公式编号。

Mermaid
: 从 CDN 加载 [mermaid.js](https://mermaid.js)，以支持 Markdown 风格的图表绘制。每次文档更新时渲染 Mermaid 图表所需的钩子会自动包含在内。

图表平移与缩放
: 当页面中存在 Mermaid 图表时，可通过 {% kbd cmd %} 滚动进行缩放，点击并拖动进行平移。
