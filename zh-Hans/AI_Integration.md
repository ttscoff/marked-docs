<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

把一份 skill 文件交给 LLM 代理，它就可以在 Marked 中打开文件和文件夹、跳到设置的某个部分，并更改偏好设置。代理使用 Marked 的 [URL Handler](URL_Handler.md)。不需要单独的插件或服务器。

## 下载 skill [download-the-skill]

{% download "SKILL.md" "供代理在 Marked 中打开文件并更改偏好设置的 skill。请保存为 SKILL.md。" %}

这个文件是纯 Markdown，开头有一小段代理在行动前会阅读的说明。任何接受 skill 或常驻指示的代理都可以使用同一份文件。

## 安装 [install-it]

把文件放进一个以该 skill 命名的文件夹，并保持文件名为 `SKILL.md`。

在 Cursor 中，下面两个位置都可以：

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

第一个对所有项目可用。第二个只用于该项目。如果其他代理没有 skill 文件夹，可以把同一段文字当作项目指示。

安装之后，请代理在 Marked 中打开一个文件或文件夹。它应当运行类似这样的命令：

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

文件夹使用同一条命令。路径必须已经存在，空格和其他保留字符必须百分号编码。完整方案，包括 refresh、Streaming Preview 和回调，见 [URL Handler](URL_Handler.md)。

## 偏好设置 [preferences]

这份 skill 还说明了两条偏好设置命令：

`pref`
: 打开设置中指定名称的部分。URL 里的名称保持英文，例如 `Preview` 或 `Style`。它不会更改任何值。

`defaults`
: 写入 Marked 已经保存的一项偏好设置，然后重新加载打开的预览。传入 `refresh=0` 可以不刷新预览。代理在写入之前应当先读取当前偏好设置，因为未知的键会被忽略。

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## 相关内容 [related]

[Using Marked with Agentic Coding](Using_Marked_with_Agentic_Coding.md) 说明如何在代理编写计划和笔记时监视那个文件夹。[Command Line Utility](Command_Line_Utility.md) 是从 shell 进行的同类操作，不经过代理。
