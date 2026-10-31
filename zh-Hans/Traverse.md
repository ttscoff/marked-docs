# <%= @title %>

[Traverse][traverse] 自带 **Stream to Marked** 命令。安装了 Marked 2 或 Marked 3 时，它会出现在导出菜单里。

## Stream to Marked [stream-to-marked]

打开导出菜单（带向上箭头的按钮），选择 **Stream to Marked**。

![Traverse 导出菜单中的 Stream to Marked][stream]

Traverse 发送的内容取决于大纲：

- 如果添加了 **Type** 属性，Traverse 会发送与 Markdown 导出相同的 Markdown。
- 如果大纲使用 **[Fountain](Fountain_for_Screenwriters.html)**，Traverse 会发送那段文字供预览。
- 如果两者都没有，Traverse 会发送一份简单的 Markdown 列表。

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
