# <%= @title %>

Marked 内置样式编辑器，并可以应用自定义 CSS 文件。

你可以使用编辑器创作漂亮的样式，或者，如果你懂一点 CSS（够用但不精通），也可以按自己的想法定制 Marked 的外观。

## 快速上手 [getting-started]

开发者和用户在 [markedapp.com/styles](https://markedapp.com/styles/) 上创建了一个自定义样式（Custom Styles）画廊。该画廊允许你直接在 Marked 中预览并安装样式。任何已安装的样式都可以在 Finder 中显示，以便查看和修改。你可以使用 {% appmenu Style, Generate a Custom Style %} 通过内置查看器打开该画廊，或者点击样式管理器中任意可编辑样式旁的铅笔（编辑）图标。如果你想编辑内置样式，需要先在管理器中复制一份。

GitHub 上还有一个 [自定义样式仓库](https://github.com/ttscoff/MarkedCustomStyles)，里面提供了示例。欢迎浏览、使用并贡献代码。如果你基于某个基础主题发布了自己的主题，也欢迎把自己加入贡献者名单中。

借助 Marked 使用自定义 CSS 文件的能力，定制预览效果几乎没有上限。任何能在 Safari 中生效的 CSS3 特性，在 Marked 中同样有效。对于默认的 Markdown 文件，Marked 中只有少数几个 HTML 元素需要处理；所有内容都位于 id 为 "wrapper" 的 div 中，其余部分则完全由你的文档标记决定。

如果你只是为个人使用而设计样式，那就没有任何规则限制。在自定义 CSS 选择器下方勾选 CSS 跟踪复选框，之后每次编辑并保存自定义 CSS 时，预览会自动更新。

**这里提供了一个 [骨架主题](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css)，方便你快速上手。**

如果你打算分享自己制作的 CSS，需要注意以下几点。首先，有一些 body 类必须应用相应的样式：

## Body 类 [body-classes]

以下样式必须包含在任何要分享的 Marked CSS 中。这些 body 类可让你针对不同偏好设置选项，定位并修改相应的选择器。

### 反转（Inverted） [inverted]

当用户选择 {% appmenu Preview, Dark Mode %} 时，body 标签会被添加一个名为 "inverted" 的类。你可以用它来定位高对比度、暗底亮字的样式。

你通常只希望反转样式作用于预览，而不影响打印，因此需要使用媒体查询（@media screen）来限制其范围。下面这段代码相当通用，多数情况下你可以直接放入自己的样式表以保持兼容，但也欢迎根据需要调整。

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### 诗歌模式（Poetry） [poetry]

用户可以选择将 Tab 缩进的文本视为诗歌还是代码。两者唯一的区别在于：选择诗歌模式时，pre/code 代码块的样式会更……嗯，更有诗意。"poetry" 类会被添加到 body 标签上。

你可以在样式上尽情发挥创意，下面是一个基础示例：

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## 特殊情况 [special-cases]

表格、Figure/Figcaption，以及 `a.footnote` 和 `div.footnotes>a` 这种特殊情况，也都需要考虑到。对于如何处理它们并没有固定规则，但可以参考默认样式，了解 Marked 需要哪些 CSS 规则。

所有默认样式中标准的表格样式，都是通过给交替行设置透明度，使表格能柔和地融入任意背景。你可以直接复用这些样式，也可以走自己的路线，但一定要记得为它们设置样式！figure 和 figcaption 也是同理；在文档中插入一张带 alt 文本的图片，看看生成的标记是什么样子，再据此设置合适的样式。

文档中包含的脚注会在正文中渲染出一个链接（a.footnote），并在末尾生成一个包含引用文本的 div（div.footnotes）。同样，可参考默认样式作为参照。为避免包含脚注引用编号的行改变行高，请务必加入类似下面的规则：

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

要让返回箭头保持在同一行，请加入：

```css
.footnotes p {display:inline}
```

另外，最好为所有图片设置一条通用规则，让它们不超出页面宽度。比如：

```css
#wrapper img { max-width: 100% }
```

如果你的主题有额外的内边距或固定宽度，请相应调整 max-width。

## 打印样式 [printstyles]

务必加入打印样式，以移除所有背景色、固定滚动效果以及仅在预览中使用的界面元素。Marked 提供了两种方式来定位打印和 PDF 输出。

### `@media print` [media-print]

从 Marked 打印，或使用打印媒体方式导出 PDF 时，标准的 CSS 打印规则同样适用：

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### `.mkprinting` 类 [the-mkprinting-class]

当 Marked 为 **PDF 导出** 或 **打印/PDF 预览**（{% kbd cmd P %}）准备文档时，会在 `<body>` 标签上添加 `mkprinting` 类（与导出相关的其他类，如 `bandw`、`breakAfterTOC`，以及你的样式自身的 `mkstyle--*` 类并存）。Marked 内置主题中大多数打印专用规则都使用这个类，而不是单纯依赖 `@media print`。

PDF 导出通常会以 **screen** 媒体方式加载隐藏的渲染 WebView（尤其是自定义样式和 [Fountain](Fountain_for_Screenwriters.html) 文档），因此样式表中的 `@media print` 代码块可能 **不会** 应用到 PDF 输出。而以 `.mkprinting` 为前缀的规则在导出时始终生效，因为它们是普通的类选择器，而非媒体查询。

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

对于必须在浏览器打印和 Marked PDF 导出 **两种情况下** 都生效的样式，可以重复关键规则，或将选择器组合起来：

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**自定义样式与附加 CSS 的区别。** 在自定义样式（Custom Style）样式表中，请按上面所示的方式书写 `.mkprinting #wrapper …`。而在 **附加 CSS（Additional CSS）** 字段中，Marked 会在注入前重写选择器——此时应改用带 body 限定的写法：

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

关于重写机制的运作方式，以及为什么单独使用 `.mkprinting #wrapper …` 在这里不生效，请参阅 [附加 CSS 设置](#additional-css-settings)。

调试自定义打印 CSS 时，可以打开打印/PDF 预览或直接导出为 PDF，然后使用 [Safari 的 Web 检查器](#webkitinspector) 检查文档——在打印布局生效期间，`<body>` 会带有 `mkprinting` 类。

打印时隐藏链接的处理独立于主题本身，用户可以自行选择是否在打印输出中隐藏链接的高亮和下划线。只要你为文本设置了基础样式，就无需为此额外操心。

那么，开始动手吧。改造你的博客主题、为 PDF 文档打造一个惊艳的打印样式，或为你惯用的写作风格量身定制完美的预览效果。如果你做出了出色的作品，欢迎 [与社区分享](https://markedapp.com/styleshare/)。

## 附加 CSS 设置 [additional-css-settings]

在 {% prefspane Style %} 中，你可以编辑 **附加 CSS（Additional CSS）**。这些规则会 **追加到当前加载的主题之后**。它们是刻意设计的局部叠加层，而非完整主题。如果你把一份完整的样式表粘贴进这个字段——或者通过 [样式管理器](Custom_Styles.html) 把同一份局部样式表当作主题导入——凡是这份样式表没有覆盖到的部分，都会保持无样式状态。

### 选择器重写 [additional-css-selector-rewriting]

Marked 会在注入附加 CSS 之前重写其中的选择器（作为 `body.mk-has-additional-css …`），以确保规则始终局限于预览范围内：

- 已经以 `body` 或 `#wrapper` 开头的选择器部分，会被加上 `body.mk-has-additional-css` 前缀，其中的 body 类会被合并而非嵌套。
- 其他任何选择器部分，都会被限定在 `body.mk-has-additional-css #wrapper …` 之内。
- Marked 设置在 `<body>` 上的前置 body 类——包括 `.mkprinting`、`.inverted`、`.poetry`、`.bandw`、`.breakAfterTOC` 和 `.mkstyle--*`——会被当作 `body` 处理，直接合并到 body 选择器上，而不会嵌套在 `#wrapper` 之下。

| 在附加 CSS 中输入 | 结果 |
| :-- | :-- |
| `#wrapper h2` | 匹配（正确限定范围） |
| `body.mkprinting #wrapper p` | 在打印/PDF 时匹配 |
| `.mkprinting #wrapper p` | **不** 匹配（需要嵌套的 `#wrapper`） |
| `:root { --x: 1; }` | **不** 匹配（对于自定义属性，建议使用 `body` 或 `#wrapper`） |

对于这个字段中的打印规则，建议优先使用 `body.mkprinting #wrapper …`。而在自定义样式文件中，若要表达相同的视觉效果，可以沿用更简短的 `.mkprinting #wrapper …` 形式。

附加 CSS **没有大小限制，也不会做 CSS 合法性检查**。Marked 会原样存储并注入你输入的内容；无效的 CSS 在预览中只是不会产生任何效果。

### HTML 及其他导出格式 [additional-css-exports]

附加 CSS 会应用于实时预览、打印/PDF 预览、PDF 导出，以及在包含样式时的 **HTML 导出**——导出的 `<body>` 会带有 `mk-has-additional-css` 类，以便重写后的选择器能够匹配。DOCX、ODT 和 EPUB 使用各自独立的样式处理方式，不会以相同方式应用附加 CSS。

只要具备一点 CSS 知识，结合使用 [高特异性选择器](#overridingspecificity)、针对打印和屏幕的 `@media` 查询，以及（在此字段中的）`body.mkprinting` 选择器或（在自定义样式中的）`.mkprinting` 选择器，你几乎可以控制样式的方方面面。

## Web 检查器 [webkitinspector]

Safari 的 Web 检查器是查看 Marked 实际生成的 HTML 和 CSS，并实时调试自定义样式的最简便方法。

### 在 Safari 中启用「开发」菜单 [enabling-the-develop-menu-in-safari]

1. 打开 Safari，选择 {% appmenu Safari, Settings… %}。
2. 切换到 **高级** 选项卡。
3. 启用 **显示网页开发者功能**（在较旧版本的 macOS 中为 **在菜单栏中显示「开发」菜单**）。

启用后，Safari 菜单栏中会出现 **开发（Develop）** 菜单。

![Safari 中显示 Marked 文档的开发菜单][develop-menu]

### 检查 Marked 文档 [inspecting-a-marked-document]

1. 在 Marked 中打开一个预览窗口，然后切换到 Safari。
2. 在菜单栏中依次选择 **开发 → _\<你的 Mac 名称\>_ → Marked → _\<文档标题\>_**。
3. Safari 会打开一个 Web 检查器窗口，并附加到所选的 Marked 预览上。

在这里你可以：

- 使用 **元素（Elements）** 选项卡检查 `#wrapper` div 内的 DOM 结构，查看应用了哪些 CSS 规则。
- 在 DOM 树中悬停某个元素，即可在 Marked 窗口中高亮对应内容。
- 使用 **样式（Styles）** 侧边栏实时调整规则，再把可用的代码片段复制回自定义样式或 **附加 CSS** 中。
    - 在「元素」选项卡中编辑 CSS 后，可以切换到「更改（Changes）」选项卡查看编辑摘要

	![更改][css-changes]
- 使用 **控制台（Console）** 选项卡针对实时预览运行 JavaScript。完整的 [Marked JavaScript API](https://markedapp.com/help/jsapi/) 在该控制台中均可使用。
- 调试文档加载的资源时，也可以查看 **网络（Network）** 等其他选项卡。

![使用 Safari Web 检查器检查 Marked 预览][inspecting]

## 分享自定义 CSS [sharing-custom-css]

使用 {% appmenu Style, Share a Custom Style %} 在浏览器中打开分享应用。将你的 CSS 拖入放置区域（或点击从磁盘选取文件），即可上传你的自定义样式对应的 CSS。

分享的样式需要经过开发者审核后才会出现在画廊中，因此不会立即显示出来。

## 其他小贴士 [other-tips]

### 覆盖特异性 [overridingspecificity]

在 Marked 预览中，会根据当前样式的文件名添加一个 body 类。如果预览设置为 "Swiss"，那么 `<body>` 标签上会有一个名为 `mkstyle--swiss` 的类。如果你的自定义 CSS 名为 MyCustom.css，那么对应的 body 类就是 `mkstyle--mycustom`。你可以在规则前加上这个类，以覆盖基础样式中定义的规则。若要在某条规则中获得绝对特异性，还可以同时使用容器 div 的 #wrapper ID：

	.mkstyle--mycustom #wrapper p+p { ... }

### 目录样式设置 [table-of-contents-styling]

如果你使用 `<!--toc-->` 标记来 [插入目录](Special_Syntax.html#tableofcontents)，可以在自定义样式中使用 "#wrapper" 提高特异性，从而覆盖目录层级标识符的相关设置：

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

这样一来，当你的自定义样式生效时，目录中所有的列表项都会使用方形项目符号，而不是「设置」中定义的样式。

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
