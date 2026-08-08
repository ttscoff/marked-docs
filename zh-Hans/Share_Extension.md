<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked 包含一个 macOS **共享扩展**，会出现在系统共享菜单中。您可以通过它把文件或选中的文本发送到 Marked，而无需切换应用或手动复制 URL。

共享扩展**随 Marked 3 一并提供**。无需单独下载或安装。Direct、Mac App Store、Marked Pro 和 Setapp 版本均包含此扩展。

## 工作原理 [how-it-works]

在共享菜单中选择 **Marked** 后，Marked 会立即打开。没有中间的撰写窗口。

### 共享文件 [share-a-file]

在 **Finder**（或其他支持共享文件的应用）中选择 **共享 → Marked**。

Marked 接收文件路径，并通过与其他流程相同的 `x-marked-3://open` URL 处理程序打开。文件会像拖到 Dock 图标或使用 {% appmenu File, Open... ({{cmd}}O) %} 打开一样在 Marked 中显示。

支持文件 URL、本地文件，以及来源应用提供的 Web URL。

### 共享选中文本 [share-selected-text]

在 **TextEdit**、**Safari** 或 **Mail** 等应用中选中文本，然后选择 **共享 → Marked**。

Marked 将文本放入剪贴板，并通过 `x-marked-3://paste` 处理程序打开**临时预览**。这与 {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} 的未保存预览相同。之后可使用 {% appmenu File, Save Transient Preview %} 保存。

当来源应用提供时，支持纯文本、HTML、RTF 和 Markdown。

有关底层命令的详情，请参阅 [URL Handler](URL_Handler.html)。

## 使用共享菜单 [using-the-share-menu]

### 从 Finder [from-finder]

1. 右键点按 Markdown 或文本文件（或选中文件后点按 Finder 工具栏中的**共享**按钮）。
2. 在共享菜单中选择 **Marked**。

如果看不到 **Marked**，请参阅下方的[启用共享扩展](#enable-the-share-extension)。

### 从文本选择 [from-a-text-selection]

1. 选中要预览的文本。
2. 打开应用的**共享**菜单（菜单栏共享项、工具栏共享按钮或右键菜单）。
3. 选择 **Marked**。

Marked 会启动（或置于前台）并显示共享内容的预览。

## 启用共享扩展 [enable-the-share-extension]

Marked 必须安装在 `/Applications`（或您常用的应用程序文件夹）中，且至少启动一次，macOS 才会列出其共享扩展。

### 在系统设置中启用 Marked [turn-on-marked-in-system-settings]

1. 打开**系统设置**。
2. 前往**通用 → 登录项与扩展**（部分 macOS 版本为**隐私与安全性 → 扩展**）。
3. 点按**扩展**（或扩展旁的 **ⓘ** 按钮）。
4. 选择**共享**（或 **Sharing**）。
5. 启用 **Marked**。

### 将 Marked 添加到应用的共享菜单 [add-marked-to-an-apps-share-menu]

即使扩展已在系统范围内启用，每个应用仍可选择显示哪些共享目标：

1. 打开支持共享的应用（Finder 和 TextEdit 便于测试）。
2. 打开**共享**菜单。
3. 选择**编辑扩展…**（较旧 macOS 可能显示**更多…**或**扩展偏好设置…**）。
4. 在**共享**下勾选 **Marked**。
5. 可选：将 **Marked** 拖到列表更上方以便访问。

在大多数应用中，更改会立即生效。

## 如果共享菜单中没有 Marked [if-marked-does-not-appear-in-share]

W> 共享扩展自 Marked 3.1.9 起提供。请确保已升级到至少该版本。

请按顺序尝试以下步骤：

1. 安装或更新后**启动 Marked 一次**。若刚完成升级，请退出并重新打开 Marked。
2. **确认扩展已在系统设置中启用**，如上所述。
3. **自定义来源应用的共享菜单**。macOS 会隐藏不常用的共享目标，直到您启用它们。
4. **检查是否安装了多个 Marked。** 若同时安装 Direct 和 Mac App Store 版本，只有正在运行的副本会注册扩展。删除或重命名不用的副本，然后启动需要的版本。
5. 若更新后扩展仍不出现，请**重新启动 Mac**。macOS 会缓存共享扩展注册信息。
6. 若您测试的是从 Xcode 或磁盘映像手动复制的构建，请**重新安装 Marked 到 `/Applications`**。共享扩展必须嵌入 `Marked.app/Contents/PlugIns/`。

## 提示 [tips]

- 共享扩展适合在不先创建文件的情况下快速预览网页片段、邮件段落或笔记。
- 对于整页或浏览器中的复杂选择，[浏览器扩展](Using_the_Browser_Extensions.html)可能提供更多控制（区块选择、Markdownify URL 等）。
- 共享的文件作为普通 Marked 文档打开并启用文件监视。共享的文本作为临时预览打开，直到您保存。
