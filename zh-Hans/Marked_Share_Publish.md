<!-- MT draft for zh-Hans — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** 是Marked 的在线发布服务，位于[share.markedapp.com](https://share.markedapp.com)。连接 Mac 一次，然后将正面文档发布为 **TextPack**，其中包含图像和可选的阅读模式亮点。知道该链接的任何人都可以在网络上查看该文档。

此功能独立于 macOS **共享扩展**（系统共享菜单）。有关从其他应用程序将文件或选择发送到 Marked 的信息，请参阅 [Using the Share Extension](Share_Extension.html)。

## 连接您的帐户[connect-your-account]

在首次发布之前，将 Marked 连接到您的共享帐户：

1. 选择{% appmenu 文件, 发布, 连接账户… %}。
2. Marked 打开您的默认浏览器以登录 share.markedapp.com。
3. 批准连接后，浏览器将返回到 Marked，并显示安全登录链接。确认对话框中显示的帐户标签。

Marked 将 API 令牌和设备密钥存储在此 Mac 上的 macOS 钥匙串中。凭证不会写入日志或崩溃报告中。

要断开连接，请选择{% appmenu 文件, 发布, 断开账户… %}。已发布的文件保持在线；如果需要，可以随时通过 share.markedapp.com 撤销访问权限。

## 发布文档[publish-a-document]

在预览中打开文档后，选择 {% appmenu 文件, 发布, 发布… %}。

第一次发布文档时，Marked 显示一个小选项表：

- **标题** — 显示在共享上（默认为不带扩展名的文档名称）。
- **可见性** — 私有、不公开或公开。新发布默认为**不公开**（可通过链接访问，不公开列出）。
- **阅读风格** — 社论、手稿、瑞士语、对比、打字机或 **无**。尽可能使用文档预览样式的默认值。 Share将此作为建议；读者可以覆盖它。选择 **无** 以在没有建议样式的情况下发布。
- **包括亮点和评论** — 在 TextPack 中嵌入阅读模式亮点。当文档有突出显示时默认为打开。
- **允许其他人重新混合** - 启用后，查看者可以在共享上分叉文档。

Marked 在后台构建 TextPack（Markdown、资产和可选的 `highlights.json`），上传它，并在这台 Mac 上记录共享 URL。

### 更新现有发布[update-an-existing-publish]

将文档链接到“共享”后，菜单项会显示“**更新已发布的文档**”，而不是“**发布...**”。选择它来上传新的 TextPack 版本。 Marked 发送服务器的内容哈希，以便检测来自另一台 Mac 或 Web 的并发编辑。

如果其他人首先在“共享”上更新了文档，Marked 会询问是否使用此 Mac 的版本**覆盖**、**在 Web 上打开**或**取消**。

## 发布后[after-publishing]

发布完成后，Marked 确认成功并提供：

- **复制分享链接** — {% appmenu 文件, 发布, 拷贝 Share 链接 %}
- **在网络上打开** — {% appmenu 文件, 发布, 在网页中打开 %}

当前端文档具有链接的发布记录时，这些命令适用于前端文档。

## 已发布文档窗口 [published-documents-window]

选择 {% appmenu 文件, 发布, 已发布文稿… %} 打开从此 Mac 发布并从您的共享帐户同步的文档列表。

对于每个条目，您可以：

- 当 Marked 在磁盘上仍然有指向本地文件的链接时，**打开**本地文件。
- **导入**当没有本地文件时TextPack（将其保存在任何地方并在Marked中打开）。
- **在网络上打开**或**复制链接**作为共享 URL。
- **当本地路径已知时，在 Finder 中显示**。
- **忘记** 从此 Mac 中删除记录，而不删除在线文档。

连接后，列表将从“共享”中刷新。如果您离线或断开连接，Marked 会显示缓存的记录，并可能提示您重新连接。

## 你可以发布什么[what-you-can-publish]

您可以发布 Marked 可以呈现的任何文档，包括：

- 保存的 Markdown 和文本文件
- 瞬时预览（剪贴板、流媒体或未保存的文档）
- TextBundles 和其他支持的格式

每个文档窗口一次仅运行一个发布操作；上传过程中菜单项被禁用。

## 提示[tips]

- 发布包括预览引用的图像。非常大的捆绑包可能会在上传前被拒绝；如果达到大小限制，请减少嵌入资产。
- 以 TextPack 导出的突出显示使用 Marked 的突出显示 JSON 格式。有关创建和导出高光的信息，请参阅[Reading Mode](Reading_Mode.html)。
- Marked Share 可在 Direct、Mac App Store、Setapp 和 Marked Pro 版本中使用。发布不需要单独订阅。
