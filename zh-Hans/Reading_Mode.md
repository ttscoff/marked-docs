<!-- MT draft for zh-Hans — Reading Mode help. Review before publishing. -->
# <%= @title %>

阅读模式可以保留您在长文档中的位置，聚焦当前块，并让您保存持久的亮点。

## 进入阅读模式 [entering-reading-mode]

选择{% appmenu Preview, Reading Mode %}或按{% kbd ctrl opt r %}。如果快速阅读正在运行，Marked 在进入阅读模式之前将其停止。

当前段落、标题、列表项、图像、代码块、表格或其他阅读单元接收左标记。键盘导航在块之间平滑移动，并将当前单元保持在预览的上三分之一附近。手动滚动可重新定位焦点，而无需捕捉页面。

## 导航和恢复 [navigation-and-resume]

当阅读模式处于活动状态时：

- {% kbd j %} 或{% kbd down %}：移至下一个读取单元。
- {% kbd k %}或{% kbd up %}：移至上一个读取单元。
- {% kbd h %}：突出显示所选内容，或在未选择文本时切换当前单位的突出显示。

Marked 保存每个文档的当前阅读位置。当保存的位置与当前视图不同时，进入阅读模式有两种选择：

- **恢复** 返回到保存的阅读位置。
- **从这里开始** 使用预览中当前可见的阅读单元。

## 专注模式 [focus-mode]

单击预览顶部的“聚焦模式”工具可以使除当前阅读单位之外的每个块变暗。导航时，焦点模式会跟随当前单位。再次单击该工具可恢复其他块，或离开阅读模式以自动清除焦点模式。

## 创建和编辑亮点 [creating-and-editing-highlights]

选择文本并按 {% kbd h %} 创建内嵌标记突出显示。在没有选择的情况下，按 {% kbd h %} 突出显示整个当前读数单位，或再次按下以删除该单位突出显示。第一个突出显示提示输入签名，Marked 在创建 CriticMarkup 时使用该签名。您可以在{% prefspane Preview %}中更改签名。

### 选择弹出窗口

选择文本以显示选择弹出窗口，其中图标按钮位于行中央：

- **荧光笔** 创建内联突出显示（或 **X** 在自动突出显示打开时删除最后一个自动突出显示）。
- **注释** 打开一个对话框来添加或编辑突出显示的注释。如果所选内容尚未突出显示，Marked 首先突出显示它。

当启用**显示选择字数**时，弹出窗口还会显示选择字数。

### 突出显示评论 [highlight-comments]

评论与签名是分开的。签名是亮点；评论是您对此的注释。

从选择弹出评论图标添加或编辑评论，或按住 Control 键单击突出显示并选择 **添加评论...** 或 **编辑评论...**。选择 **删除注释** 以删除注释而不删除突出显示。

带有评论的高亮会显示一个小指示点。当评论侧边栏可见时（**齿轮菜单 > 校对 > 显示评论**），阅读模式高亮的评论将显示在此处，并带有一条连接到父高亮的连接线，旁边还有 CriticMarkup 和其他文档评论。

### 自动突出显示

单击预览顶部的荧光笔工具可在您选择文本时自动突出显示文本。单击选择弹出窗口中的荧光笔以撤消上次自动突出显示，或再次单击顶部荧光笔工具以关闭自动突出显示。

当您指向或选择它们时，内联高亮显示开始和结束手柄。拖动任一手柄可扩展或缩小突出显示的范围。刷新或重新打开文档时，更改会自动保存并恢复。

单击突出显示以将其聚焦，然后按删除或退格键将其删除。按住 Control 键单击突出显示的部分，然后选择“**共享...**”打开包含文档标题和突出显示文本的 macOS 共享表，选择“**添加评论…**/**编辑评论…**”以附加注释，或选择“**删除评论**”以清除注释。

**阅读模式关闭时显示突出显示**设置控制在离开该模式后保存的突出显示是否仍然可见。

## 导出亮点 [exporting-highlights]

选择 **预览 > 导出突出显示...** 或单击阅读模式工具栏中的导出突出显示工具。格式：Markdown、HTML（当前预览样式）、纯文本、CSV（Readwise 兼容，**注释** 列中包含注释，**签名** 中包含签名）和 JSON（每个突出显示上包含一个 `comment` 字段）。

HTML 导出嵌套将注释突出显示为每个突出显示的段落下方的块引用。

JSON 格式是 Marked 的交换文件。将其保存在 Markdown 文档旁边作为 `Document.markedhighlights.json`，或在导出 TextBundle 时自动包含它。

## 导入亮点 [importing-highlights]

选择 **预览 > 导入突出显示...** 并选择 Marked 突出显示 JSON 文件。按 ID 合并高亮显示：添加新的 ID，更新匹配的 ID，并且保留文件中不存在的现有高亮显示。

当您打开包含 `highlights.json` 的 TextBundle 时，Marked 会自动合并这些突出显示。当 TextBundle 打开时，Marked 还会将突出显示和注释更改保存回包中的 `highlights.json`（不修改 `text.md`）。

## TextBundle 亮点 [textbundle-highlights]

在 **保存 TextBundle** 上，启用 **包括突出显示** 以将 `highlights.json` 嵌入到捆绑包（或 TextPack）中。共享该捆绑包，以便协作者可以在 Marked 中打开它并保留组合的突出显示集。

## CriticMarkup 行动 [criticmarkup-actions]

与高亮导出和导入不同，预览菜单为保存的高亮提供了两个 CriticMarkup 操作：

- **将突出显示复制为 CriticMarkup** 以 CriticMarkup 格式复制每个突出显示，而不更改源文件。
- **将突出显示插入文档...** 要求确认，然后将明确的匹配源文本包装在 CriticMarkup 中。 Marked 跳过缺失、重复或重叠的匹配项并报告结果。

通过签名和注释，生成的标记使用<code>{=<span>=</span>highlighted text==}{&gt;&gt;signature: comment&lt;&lt;}</code>。仅使用注释，Marked 使用 <code>{=<span>=</span>highlighted text==}{&gt;&gt;comment&lt;&lt;}</code>。只有签名时，它使用<code>{=<span>=</span>highlighted text==}{&gt;&gt;signature&lt;&lt;}</code>。如果没有其中任何一个，Marked 只会创建 <code>{=<span>=</span>highlighted text==}</code> 标记。

## 印刷亮点 [printing-highlights]

默认情况下，打印或另存为 PDF 时会包含阅读模式突出显示。使用打印表中的 **包括阅读模式突出显示** 将其更改为当前输出。 {% prefspane Export %} 中的匹配设置控制未来打印和 PDF 作业的默认值。
