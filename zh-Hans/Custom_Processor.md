<!-- MT-DRAFT: machine translation; human review required -->

#<%= @title %>


标记让您可以完全控制自定义规则、文本
转换，以及运行您自己的命令或运行的能力
基于匹配文件属性的不同处理器。


## 使用自定义预处理器/处理器 [using-custom-preprocessorsprocessors]

要添加自定义处理器，请转到 {% prefspane Processor %}
然后单击“**自定义规则**”。

![][1]

[1]: images/custom-rules-button-800.jpg @2x width=800


在规则编辑器（又名“Conductor”）中，您可以添加自定义
具有根据文件名匹配文件的标准的规则，
路径、内容、元数据的匹配，甚至是否
其他文件与该文档存在于同一树中
打开。当规则匹配时，为该规则定义的操作
规则在该文件上运行。

> 在“处理器”字段下方，“新建”中的复选框
> 文档使用custom:"确定是否测试规则
> 完全适用于预处理器和处理器阶段。一般来说，
> 保留这些选中状态，但如果您想完全覆盖
> 任何自定义处理器，请在此处设置。

![规则编辑器][2]

  [2]: images/CustomRules-800.jpg @2x width=800

要创建新规则，请使用 `+`
左侧规则列表底部的按钮。给
规则一个名称并将其设置为预处理器或处理器。

规则旁边的三个点表示预处理器、处理器和已启用。只能突出显示预处理器或处理器之一，并且您可以单击点来更改规则的状态。

预处理器
：在文件最初处理之后、Marked 添加包含的文件、处理 GitHub 换行符等样式首选项时运行，但在处理阶段之前运行。此时文档仍然是原始 Markdown，您可以对内容进行更改以传递给处理器。如果没有匹配的自定义处理器，或者在匹配的自定义处理器中没有运行运行处理器操作，则将运行默认处理器。

处理器
：自定义处理器取代了{% prefspane Processor %}中定义的内置处理器。它可以处理预处理器可以执行的所有操作，并添加运行命令和运行处理器操作。这允许您运行自定义命令，例如Pandoc，或对符合条件的文件运行不同的内置处理器。

自定义规则编辑器中的所有表格都可以通过以下方式重新排序
拖放，这样您就可以影响其中的顺序
规则运行时，谓词中条件的顺序
编辑器，以及要按顺序运行的操作的顺序。

### 谓词编辑器 [predicate-editor]

![谓词编辑器][谓词]

[predicate]: images/custom-rules-predicate-800.jpg @2x width=800

添加规则后，使用谓词编辑器来定义
确定规则是否运行的标准
给定的文件。使用左侧下拉菜单选择
标准，然后使用比较器和值字段来构建
谓词。

- _Filename_ 仅匹配文件的文件名
- _Extension_ 仅匹配文件的扩展名
- _Path_ 匹配文件的完整 POSIX (Unix) 路径
- _Tree_ 搜索文件名匹配的任何位置
  文件的目录树
- _Text_ 匹配文件中的文本内容。使用转发
  文本值周围有斜杠以使其成为常规值
  表达式搜索。
-_Fileincludes_测试文件是否包含includes
  文件（使用任何[标记的包括
  语法](Multi-File_Documents.html)）。
-_元数据类型_测试文件是否包含YAML，
  MultiMarkdown 或 Pandoc 元数据
- _元数据：_字段（例如_元数据：作者_，
  _元数据：日期_，_元数据：标题_）特定的测试
  元数据键。任何元数据键都会在下拉列表中显示为
  _元数据：_ 后跟字段名称。
- _手动启用_在规则被改变时匹配
  当前预览窗口打开（请参阅[手动启用
  规则]（#manuallyenabled）如下）。将其与其他组合起来
  所有 (AND) 组中的条件，因此规则仅在以下情况下运行
  您选择加入并且该文件符合您的其他条件。

匹配所有文件（即始终匹配的自定义处理器
运行），将 _Filename_ 设置为 `contains` `*`。星号将
充当通配符并匹配所有文件。

[添加谓词][添加谓词]

[addpredicate]: images/custom-rules-add-predicate-800.jpg @2x width=800

单击谓词行上的加号 (+) 以添加另一个谓词。按住 Option 键的同时单击 + 可添加可设置为全部 (AND) 或任意 (OR) 的布尔组。

### 手动启用的规则 [manuallyenabled]

某些规则不应在与其匹配的每个文件上运行
标准。如果需要，添加 **手动启用** 标准
仅在当前打开它后才运行的规则
预览。

使用谓词下方的 **添加手动启用** 按钮
编辑器插入此标准。每个规则都可以包含它
只有一次。如果存在，该规则将显示在该预览的 {% appmenu
Preview, Enable Custom Rule %} 子菜单中
窗口。

**示例用例：** 您维护一条注入规则
打印 CSS、删除注释并移动标题级别
PDF 导出。你不希望每个人都进行这种转变
起草时保存，但您确实需要按需保存。给
规则正常文件匹配标准加上**手动启用**，
然后从预览菜单（或触发器快捷方式）切换它
当您准备好校对打印布局时。

#### 触发快捷键 [trigger-shortcut]

当选定的规则包含**手动启用**时，
**触发快捷方式**字段出现在**手动添加旁边
已启用**。单击录音机，然后按 键
你想要的组合。该快捷方式切换规则
最前面的标记预览（如果关闭则启用，如果打开则禁用）。的
快捷方式与规则一起存储并在启动后持续存在。
清除该字段以删除快捷方式。

![在 Conductor 中触发快捷方式录音器][手动快捷方式]

[manualshortcut]: images/conductor-manual-rule-shortcut.jpg @2x width=800

#### 预览菜单中的按预览覆盖 [per-preview-overrides-in-the-preview-menu]

两个预览菜单子菜单控制活动的覆盖
仅预览。设置按 [视图](Opening_Files.html#multiview) 保存
多个窗口显示同一个文件。

**启用自定义规则**
：列出每个已启用的规则，其中包括 **手动
  启用**标准。检查规则以为此启用它
  预览；取消选中将其关闭。预览刷新
  立即。

**自定义规则覆盖**
：列出流程阶段规则。选择一个来*固定*它：期间
  处理阶段，仅评估该规则（其他
  跳过流程规则）。选择**无（自动）**
  返回正常的规则匹配。当您
  想要强制使用特定的处理器管道
  预览而不更改全局自定义规则。

#### 预览工具栏中的覆盖按钮 [override-button-in-the-preview-toolbar]

当预览至少有一个手动启用的规则或
固定的进程覆盖，底部会出现一个分支图标
工具栏（位于导出和抽屉控件的左侧）。
填充的强调色图标表示覆盖处于活动状态；
轮廓图标表示覆盖已暂停。

![预览工具栏中的自定义规则覆盖按钮][conductoroverride]

[conductoroverride]: images/conductor-override-toolbar.jpg @2x width=800

单击按钮可暂停或重新启用此覆盖
预览而不清除手动规则复选标记或
固定的流程规则。暂停的超控将在以下情况下恢复：
你再次点击。这比取消选中规则更快
当您想要将正常预览与您的预览进行比较时，菜单
覆盖管道。

### 行动 [actions]

使用 *+ 操作* 按钮将操作添加到规则。

![添加动作][添加]

[addaction]: images/custom-rules-add-action-800.jpg @2x width=800

可用的操作包括：

设置风格
：设置预览的样式。您添加的任何内置样式或自定义样式都可用。

运行命令
：这需要一个命令行命令，包括任何参数，并将在 STDIN 上传递文件的内容。该命令应在 STDOUT 上返回结果输出。

> **Mac App Store 沙盒**：Marked 的 Mac App Store (MAS) 版本在限制外部二进制文件执行的沙盒环境中运行。如果您需要在 MAS 版本中使用 Pandoc 等外部处理器，则必须将二进制文件复制到应用程序包中。为此：
>
> 1. 右键单击Marked.app → 显示包内容
> 2. 导航至目录/资源/
> 3. 如果`bin`文件夹不存在，则创建一个
> 4. 将您的二进制文件（例如 `pandoc`）复制到此
> `bin`文件夹
> 5. 使其可执行：`chmod +x` 二进制文件
> 6. 在运行命令操作中，将其引用为：
>
> `YOUR_BINARY_NAME [arguments]`
> 或者使用完整路径：
> `/Applications/Marked.app/Contents/Resources/bin/YOUR_BINARY_NAME [arguments]`
>
> **注意**：具有外部 shebang 的脚本（例如指向 `/opt/homebrew/bin/python` 的 Python 脚本）在复制到捆绑包时将通过系统解释器自动执行。 MAS 版本在执行实际上是 Python 或 Ruby 脚本而不是二进制文件的二进制文件时可能仍然存在问题。
> 每次应用程序更新后，您都需要重新复制二进制文件，因为更新会替换整个捆绑包。或者，使用 **Help->Crossgrade** 获取没有此类限制的非沙盒版本。

运行嵌入脚本
：在内置代码编辑器中编辑完整脚本。与 Run Command 一样，这应该在 STDIN 上获取输入并在 STDOUT 上返回输出。

设置元数据
：添加或设置元数据。提供一个键和一个值。如果该键存在，则更新其值，如果不存在，则添加该键。使用的元数据类型将由文件内容（或元数据转换操作的结果）自动确定。
：如果没有找到现有元数据，元数据将以 MultiMarkdown 格式添加到 HTML 注释中。标记可以读取此元数据，但无论使用什么处理器，它都不会出现在您的预览中。

删除元数据
：根据元数据的键删除元数据。

剥离元数据
：删除所有元数据。影响 YAML、MultiMarkdown 和 Pandoc 元数据。

将 YAML 元转换为 MMD
：将文件顶部的 YAML 元数据块转换为 MultiMarkdown 样式元数据。

将 MMD 元转换为 YAML
：将 MultiMarkdown 元数据块转换为 YAML。

搜索和替换
：对文件内容执行搜索和替换。
：如果搜索字符串被正斜杠包围（例如`/Project \w+/`），它将被视为正则表达式。您可以使用 `$1`、`$2` 等在替换字符串中包含匹配组。
：替换字段支持一些转义序列（后跟反斜杠）：`\n`插入换行符，`\t`插入制表符，`\\`插入文字反斜杠，`\$`插入文字美元符号（而不是匹配组）
：任何其他`\X`序列都被视为`X`（反斜杠被删除），因此`\e`变为`e`。后面没有任何字符的尾随 \ 被保留为文字反斜杠。
：在替换字符串中使用 `[%key]` 插入来自文档元数据、环境变量或上下文的值（例如 `[%title]`、`[%MARKED_PATH]`）。由同一规则中的较早操作或先前规则设置的键可用。不匹配的键将替换为空字符串。

插入标题 H1
：在文档中插入 H1。这可以从元数据或文件名中提取。

移位标题
：调整标题级别，从-5--+5。例如，如果将其设置为 -1，则所有 H1 都会变成 H2，H2 会变成 H3，等等。将其设置为正数可将标头级别提升该数量。

标准化标头
：如果可能的话，此操作将确保文档中只有一个 H1，并调整所有标题级别，以便它们按语义顺序排列并且不会跳过级别，例如从H2到H4。如果原始文档一开始就在语义上排序，这将很好地完善层次结构。

插入目录
：插入目录。 TOC 可以位于第一个 H1、第一个 H2 之后，也可以位于文件顶部（将插入到任何元数据之后）。

插入文件
：在文档中的给定点插入选定的文本文件。这可以在第一个 H1、第一个 H2、顶部、底部或文本匹配之后（使用 `/pattern/` 搜索正则表达式）。

插入文本
：提供弹出编辑器，您可以使用它直接将文本嵌入到操作中。定位选项与_插入文件_相同。
：在插入文本中的任意位置使用`[%key]`从文档元数据、环境变量或标记上下文中提取值（例如`[%author]`、`[%MARKED_PATH]`）。无论您使用哪种处理器，这都有效，因此您不需要 MultiMarkdown 来替换元数据。包含来自同一规则中较早操作（例如**设置元数据**）或来自先前规则的值。不匹配的键将替换为空字符串。

插入 CSS 文件
：将选定的 CSS 文件插入到文档中。这将在选择任何样式后加载，并可用于覆盖现有样式或添加新样式。

插入CSS
：提供弹出式 CSS 编辑器，您可以在其中将自己的 CSS 直接添加到操作中。该 CSS 将被注入到文档顶部、任何现有样式之后。注入样式的顺序将与规则中操作的顺序相匹配。

插入 JavaScript 文件
：在文档末尾插入选定的 JavaScript 文件。请注意，如果您希望脚本在每次更新时重新加载，则需要将 *Insert JavaScript* 操作与 [update hook](#updatehook) 一起使用。

从 URL 插入 JavaScript
：使用它在文档末尾插入链接到 CDN 或其他远程 URL 的 `<script>` 标签。请注意，如果您希望脚本在每次更新时重新加载，则需要将 *Insert JavaScript* 操作与 [update hook](#updatehook) 一起使用。

插入 JavaScript
：提供弹出式 JavaScript 编辑器，您可以使用它直接在操作中嵌入自定义 JavaScript。这将被注入到文档的末尾，规则运行的 JavaScript 顺序将由操作的顺序决定，最后添加的操作最后。
：请注意，如果您希望脚本在每次更新时运行，则需要使用[更新挂钩](#updatehook)。

自链接 URL
：将任何裸 URL 转换为 `<url>`，这将在任何处理器中生成超链接。

运行快捷方式
：运行 Apple 快捷方式。任何快捷方式运行都应从 STDIN 获取输入并在最后返回输出（停止并返回输出）。如果要执行不修改文本的操作，请将输入设置为变量，运行操作，然后在最后输出原始文本变量。

运行系统服务
：运行`~/Library/Services`中的任何系统服务。服务应该接受输入并返回输出。

运行 Automator 工作流程
：运行任何 Automator `.workflow` 文件。输入将在 STDIN 上传递，输出预计在 STDOUT 上。

运行规则
：从当前规则运行另一个自定义规则的操作。
  从弹出窗口中选择目标规则。调用的规则
  在同一阶段（预处理器或进程）运行，无需
  重新评估它的谓词，这使得它有用
  可重复使用的“成分”规则。

  **用例示例：**定义一个名为“Strip
  HTML 注释”，带有搜索和替换操作，并给出
  它是一个 **手动启用** 标准，因此它永远不会运行
  自动。在您的主要书籍处理规则中，添加
  **按顺序运行规则**操作：第一个“标准化标头”
  然后是“删除 HTML 注释”，然后是调用的运行命令
  潘多克。您可以保持每个步骤的可维护性，而无需重复
  跨规则的行动。

  **嵌套：**由**运行规则**调用的规则无法调用
  另一条规则。如果目标规则包含 **运行规则**
  动作，该动作被跳过；中的所有其他行动
  目标规则仍在运行。您可以添加多个**运行规则**
  对单个规则执行的操作，并且它们按顺序执行。

  规则不能调用自身，Marked 检测循环
  （例如，规则 A 调用规则 B，规则 B 又调用规则 A）
  并跳过嵌套调用。参见【自定义规则】
  Log](#customprocessorlog) 用于跳过消息。

继续
：默认情况下，一旦匹配到规则，处理就会停止（预处理器和处理器是分开的，因此一个预处理器和一个处理器可以匹配）。此操作将强制规则匹配在规则执行其操作后继续。

### 更新挂钩 [updatehook]

标记不会在每次更新时进行完全刷新，所以如果
你有渲染 DOM 部分的脚本，它们需要
使用 Marked 的 Hook API 运行其渲染函数。

下面的例子使用了美人鱼，但你实际上从未使用过它
需要做的，因为现在默认包含美人鱼。但是
如果您手动包含它，您将按照以下方式执行此操作。

添加 **插入 JavaScript** 操作，并在“编辑 JS”中
窗口，初始化脚本并添加钩子：

```javascript
mermaid.initialize({ startOnLoad: true });

Marked.hooks.register('update', function() {
    mermaid.run();
});
```

这会导致`mermaid.run()`每次都会被执行
标记执行部分更新。

### 测试规则 [test-rules]

规则列表下的_测试规则_按钮将打开一个
您可以在其中选择任何 Markdown 文件的对话框，它将
根据您的所有规则进行测试。匹配的规则将得到
左侧以绿色标签突出显示。匹配时
针对文件，将出现一个 X 按钮，可用于
清除测试并取消突出显示行。

## 拖放 [drag-and-drop]

Conductor 窗口支持增强的拖放功能
智能检测文件类型的功能和
根据拖动的文件提供适当的操作。的
实现包括文本的分割覆盖系统
允许用户在测试文件之间进行选择的文件
违反规则或将其添加为操作。

![拖放自定义规则][拖动]

[drag]: images/draganddropconductor.jpg @2x width=800

### 文件类型检测 [file-type-detection]

系统自动检测不同的文件类型并
显示适当的覆盖消息：

- **CSS 文件** (`.css`)：显示“插入 CSS 文件”叠加层
- **JavaScript 文件** (`.js`、`.javascript`)：显示“插入
  JS 文件”叠加
- **脚本文件**（任何可执行文件））：显示“运行
  命令”叠加
- **文本文件**：显示分割叠加
- **可执行文件**：显示“运行命令”叠加层
- **未知扩展**：默认为“文本”类型并显示
  分割叠加

## 自定义处理器日志 [customprocessorlog]

如果您得到奇怪的结果并想了解发生了什么，自定义规则日志将向您显示哪些规则按什么顺序运行。使用**帮助->显示自定义规则日志**将其打开。调用的 **运行规则** 操作和跳过的嵌套调用也记录在此处。

![自定义规则日志][crlog]

[crlog]: images/CustomRulesLog.jpg @2x width=809

## 执行多个命令 [executing-multiple-commands]

一条规则可以按顺序包含多个命令。的输出
每个命令都会传递到下一个命令。如果你想拥有
命令与 Marked 的命令同时输出一些内容
预览更新，一定要传回原来的内容
到 STDOUT 以处理下一个命令或内置
处理器。

例如，如果您想要使用命令更新 PDF
使用Pandoc的文档，只需传递原始文件路径
（从环境变量）到 Pandoc 并使用适当的
命令行选项，然后回显 STDIN 内容
输出到标准输出。

## 动态绕过自定义处理器 [dynamically-bypassing-custom-processors]

如果自定义处理器在 STDOUT 上返回“NOCUSTOM”，则标记为
将终止自定义处理器并回退到
默认内部处理器。这允许您创建一个
可以决定是否需要的定制处理器
使用[环境变量](#environmentvariables)运行
下面，文档文件名或扩展名，内容匹配
或其他逻辑。

如果自定义处理器返回而不是`NOCUSTOM`
`MULTIMARKDOWN` 或 `DISCOUNT`（或 `GFM`）、`KRAMDOWN`，或
`COMMONMARK`，那么该内部处理器将用于
只是那个文件。此更改不会影响默认值
在“设置”中设置处理器。

## 环境变量 [environmentvariables]

运行命令操作有一个环境编辑器，您可以在其中
可以设置自己的环境变量
可用于命令或脚本。除了这些
自定义变量，Marked 包括一些它自己的。

Marked 在自己的 shell 中运行自定义处理器，这意味着
标准环境变量不会自动传递。
您可以使用 Marked 的环境变量来增强您的
在你的脚本中拥有自己的。标记使以下变量
可在您的 shell 脚本中使用：

**标记_来源**
：主要工作文件（工作文本、Scrivener 或索引文件的文件夹）的位置（基本目录）。

**路径**
：标记设置包含默认可执行文件夹的路径，并将该目录附加到上面的`MARKED_ORIGIN`中。默认值为：`/Developer/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`。您可以通过根据需要设置 PATH 变量并附加或覆盖 Marked 的路径（例如 `PATH=/usr/local/yourfolder:$PATH`）来添加自己的路径。

**首页**
：登录用户的主目录。 Python 和其他依赖于设置的 HOME 变量的脚本将自动选择该变量，但它也可用于脚本中的其他用途。

**MARKED_EXT**
：正在处理的主文件的扩展名。该变量允许您根据正在查看的文件类型编写不同的进程脚本。例如，如果 `$MARKED_EXT == "md"` 运行您首选的 Markdown 处理器，但如果 `$MARKED_EXT == "textile"` 则运行 Textile 处理器。

**标记路径**
：这是在加载时标记为打开的主文件的完整 UNIX 路径。

**标记_包括**
：使用各种 [include 语法](Special_Syntax.html#pagebreaks) 传递的文本中包含的已标记文件的引用、逗号分隔列表。

**标记_阶段**
：这将设置为“PROCESS”或“PREPROCESS”，允许您使用单个脚本来处理基于此变量的两个阶段。

**MARKED_CSS_PATH**
：当前样式表的完整路径

### 元数据环境变量 [metadata-environment-variables]

当在 Marked 中执行 Run Command 操作时
指挥系统，文档元数据自动
提取并作为环境变量提供给
命令。

#### 它是如何工作的 [how-it-works]

1. **元数据提取**：系统使用现有的`extractMetaDataFromString:`方法从文档中提取元数据，支持：
   - YAML 前面的内容（`---` 块）
   - MultiMarkdown 元数据（关键：值线）
   - Pandoc 元数据（`%` 标题块）
   - HTML 评论元数据 (`<!-- key: value -->`)

2. **密钥标准化**：元数据密钥被标准化以用作环境变量：
   - 转换为小写
   - 所有非字母数字字符均被删除
   - 空格和特殊字符被删除

3. **环境变量格式**：每个元数据键成为一个带有`MD_`前缀的环境变量：
   - `Author` → `MD_author`
   - `XHTML header` → `MD_xhtmlheader`
   - `Custom Processor` → `MD_customprocessor`

#### 示例 [example]

给定一个包含此元数据的文档：

```markdown
title: My Document
author: John Doe
date: 2024-01-15
Custom Processor: true
Marked Style: amblin
XHTML header: <meta name="viewport" content="width=device-width">
Status: Draft
Priority: High
```

以下环境变量可用于
命令：

```bash
MD_title="My Document"
MD_author="John Doe"
MD_date="2024-01-15"
MD_customprocessor="true"
MD_markedstyle="amblin"
MD_xhtmlheader="<meta name=\"viewport\" content=\"width=device-width\">"
MD_status="Draft"
MD_priority="High"
```

#### 命令中的用法 [usage-in-commands]

您现在可以在运行中使用这些环境变量
命令动作：

```bash
# Print the document title
echo "Processing: $MD_title"

# Use metadata in conditional logic
if [ "$MD_status" = "Draft" ]; then
    echo "Document is still in draft status"
fi

# Pass metadata to other tools
pandoc "$MARKED_PATH" \
  --metadata title="$MD_title" \
  --metadata author="$MD_author" \
  --metadata date="$MD_date" \
  -o output.pdf

# Use metadata for file naming
if [ -n "$MD_title" ]; then
    output_file="${MD_title// /_}.html"
else
    output_file="output.html"
fi
```

#### 支持的操作 [supported-actions]

这种元数据到环境变量的功能是
可用于：

- **运行命令**操作
- **运行嵌入式脚本**操作

元数据自动从文档中提取
内容并可供任何命令或脚本使用
贯穿这些动作。

## 启用和禁用 [enabling-and-disabling]

定制处理器可以打开和关闭
使用 {% kbd opt cmd C %} 的单个文档。你
还可以为文档打开预处理器或处理器
自动[使用元数据](#perdocument) 在顶部
该文件。

每个文档的处理器的当前状态是
显示为指示灯（仅当处理器
已启用）位于底部工具栏项目的左侧
预览的右侧工具栏。

### 预处理器 [preprocessor]

如果您设置预处理器规则，它们将在标记后运行
处理任何特定于标记的任务，例如包括外部
文档和代码，但在运行处理器之前
（内部或自定义）。这使您有机会渲染
自定义模板变量，处理替换或注入
通过任何其他方式获取您自己的内容。

标记为工作设置环境变量
目录 (`MARKED_ORIGIN`) 到父目录
正在预览文件。您可以使用它来更改工作
脚本的目录并包含具有相对路径的文件
到原始文档。举个例子，在 Ruby 中你可以
使用：

	Dir.chdir(ENV['MARKED_ORIGIN'])

启用后，可以打开自定义预处理器并
关闭单个文档使用
{% kbd ctrl opt cmd C %}。

#### 每个文档处理器/预处理器 [每个文档] [perdocument]

还可以根据每个文档设置自定义处理器
使用元数据格式 [Per-Document
设置](Per-Document_Settings.html)。

您可以指定是否使用自定义处理器设置以及
使用 [Per-Document
设置](Per-Document_Settings.html)（`Custom Processor:`
和`Custom Preprocessor:`）。除“true”之外的任何设置
或“yes”将禁用自定义预处理器/处理器。

用法示例：

    定制处理器：true
    自定义预处理器： false

正如[每份文件
设置](Per-Document_Settings.html#hidingmeta)页面，您
可以用 HTML 注释标记包围此元数据以隐藏
从 GitHub 和其他不删除它的处理器中删除它
从输出：

    <!--
    定制处理器：true
    自定义预处理器：true
    -->

## 使用替代 Markdown 处理器 [using-an-alternative-markdown-processor]

任何可以从命令行渲染的 Markdown 风格都可以
与标记一起使用。它需要能够接受输入
STDIN，与通过“管道”将 Markdown 传输到它相同
命令行，即`cat myfile.md | myprocessor`。它需要
在 STDOUT 上返回生成的 HTML，其中每个
我曾经使用过的处理器默认情况下是这样的。

在终端中使用`which YOUR_PROCESSOR`来确定路径
到可执行文件，然后将其粘贴到运行命令路径中
字段，或者只需将可执行文件拖到“自定义规则”窗口
以及要添加所选操作的规则。

如果您的处理器需要命令行上的参数，
您还需要在字段中输入这些内容。一些
处理器需要连字符才能在 STDIN 和/或 STDOUT 上运行，
例如`-o - -` 通常信号从 STDIN 输入，输出到
标准输出。有关详细信息，请参阅处理器的文档。

我已经使用 Pandoc 测试了自定义处理器功能，
Kramdown、marked（折扣）、MultiMarkdown 6、Maruku 和
各种其他口味。

### 关于 Pandoc 和沙盒的说明 [a-note-about-pandoc-and-sandboxing]

Pandoc（和其他一些命令行工具）将无法运行
Marked 的 Mac App Store（沙盒）版本。
如果您需要运行 Pandoc，请使用 **Help->Crossgrade** 获取
直接（Paddle）版本的免费许可证。这是真的
遇到沙箱问题的任何处理器：如果标记
由于 MAS 权限问题无法执行它，它将
提供跨级的步骤。如果您遇到问题
但这并没有发生，请通过以下方式与我联系
[支持网站](https://support.markedapp.com/questions/add)。

### Pandoc 作为瑞士陆军 Markdown 处理器 [pandoc-as-swiss-army-markdown-processor]

[Pandoc](https://pandoc.org/) 是迄今为止最灵活的
用于处理一系列标记格式的通用工具。由
添加 `-f` 参数与以下之一，Pandoc 可以
成为以下任何一项的定制处理者：

- `commonmark`
- `docbook`
- `dokuwiki`
- `gfm`
- `markdown_phpextra`
- `mediawiki`
- `textile`
- `twiki`
- `vimwiki`

还有其他一些人。参见[潘多克
文档](https://pandoc.org/MANUAL.html) 了解更多
信息。要使用其中一种作为输入格式，只需添加
在“运行命令”字段中输入以下内容：

    /usr/local/bin/pandoc -f INPUT_FORMAT

Pandoc 非常适合编写使用以下内容的脚本
`$MARKED_EXT`环境变量来确定哪种格式
运行 Pandoc，或使用一系列规则
扩展匹配。如果扩展名是 `md`，则使用
`pandoc -f gfm` 或 `pandoc -f markdown_mmd` （或者直接返回
STDOUT 上的 `NOCUSTOM` 使用默认处理器）。但如果是
`textile`，在脚本中运行`pandoc -f textile`。如果
它是 `wiki`，使用 wiki 标记处理器之一。你得到
这个想法。

Pandoc 爱好者都知道，Pandoc 还可以处理
广泛的参考书目和 LaTeX 场景。大多数功能
您可以通过命令行访问即可
通过在 Marked 中使用传递参数。

## 使用纺织品 [using-textile]

有几个人问如何让 Textile 工作
标记。您需要有一个纺织转换器，可从
命令行。有几个选项，包括 Pandoc
（见上文），但如果您还没有安装 Pandoc，
另外两个选项是用于 Ruby 的 RedCloth 和用于 Perl 的 Textile
（需要安装开发人员工具）。安装
一个或另一个：

1. 从以下位置安装 Textile
   <https://github.com/bradchoate/text-textile> **或**
   航站楼`sudo gem install RedCloth`
2. 使用`which textile`或`which redcloth`确定
   自定义处理器路径设置中使用的路径

Now Marked 是一款适合您的纺织品预览器！

## 使用 AsciiDoc [using-asciidoc]

1.安装【AsciiDoctor】(http://asciidoctor.org/)。
2. 在 {% prefspane Processor %} 中启用自定义规则以匹配您的 AsciiDoc 文件。
3. 将规则设置为处理器并添加运行命令操作
    1. 确定到`asciidoc`的路径，即
       像 `/usr/bin/asciidoc` 或
       `/opt/local/bin/asciidoc`。如果不确定，请使用
       `which asciidoc` 定位
    2. 输入 `[PATH To asciidoc] --backend html5 -o - -` 作为
       命令（末尾的 - 发送输出为
       标准输出）

这会将当前文档发送到 STDIN 并显示
生成 HTML 作为 STDOUT。

请参阅[此要点](https://gist.github.com/mojavelinux/6324279)
来自 [丹·艾伦](https://gist.github.com/mojavelinux) 的
更多信息。