<!-- MT draft for zh-Hans — Marked Share publish help. Review before publishing. -->
# <%= @title %>

* * Marked Share * *是Marked在⟦P0的在线发布服务⟧。连接Mac一次，然后将正面文档作为带有图像和可选阅读模式亮点的* * TextPack * *发布。任何知道该链接的人都可以在网上查看该文档。

此功能独立于macOS * *共享扩展* * （系统共享菜单）。有关从其他应用⟧程序将文件或选择发送到Marked的信息，请参阅⟦P0。

# #关联您的账号[connect-your-account]

在首次发布之前，请将“已标记”关联到您的共享帐户：

1.选择{% appmenu 文件, 发布, 连接账户… %}。
2.标记打开默认浏览器以登录share.markedapp.com。
3.在您批准连接后，浏览器将返回带有安全登录链接的“已标记”页面。 确认对话框中显示的帐户标签。

Marked将API令牌和设备密钥存储在此Mac上的macOS钥匙串中。凭据不会写入日志或崩溃报告。

要断开连接，请选择{% appmenu 文件, 发布, 断开账户… %}。已发布的文档保持在线；如有需要，可随时在share.markedapp.com撤销访问权限。

# #发布文档[publish-a-document]

在预览中打开文档后，选择{% appmenu 文件, 发布, 发布… %}。

首次发布文档时， “已标记”会显示一个小选项表：

- * * Title * * —显示在Share （共享）上（默认为没有扩展名的文档名称）。
- * *可见性* * —私密、未发布或公开。 新发布默认为* *未发布* * （可通过链接访问，未公开发布）。
- * *包括亮点和注释* * —在TextPack中嵌入阅读模式亮点。 当文档具有突出显示时，默认为开启。
- * *允许其他人混音* * —启用后，查看者可以在“共享”上分叉文档。

Marked在后台（ Markdown、资产和可选`highlights.json` ）生成TextPack ，上传并在此Mac上记录共享URL。

# # #更新现有发布[update-an-existing-publish]

将文档链接到“共享”后，菜单项显示* *更新已发布文档* * ，而不是* *发布… * *。选择它以上传新的TextPack版本。Marked发送服务器的内容哈希，以便检测来自另一台Mac或Web的并发编辑。

如果其他人先在“共享”上更新了文档，则Marked会询问是否使用此Mac的版本* *覆盖* *、* *在Web上打开* *或* *取消* *。

# #发布后[after-publishing]

发布完成后， Marked确认成功并提供：

- * *复制分享链接* * — {% appmenu 文件, 发布, 拷贝 Share 链接 %}
- * *在网页上打开* * — {% appmenu 文件, 发布, 在网页中打开 %}

当正面文档具有链接的发布记录时，这些命令适用于正面文档。

# # Published Documents窗口[published-documents-window]

选择{% appmenu 文件, 发布, 已发布文稿… %}打开从此Mac发布并从您的共享帐户同步的文档列表。

对于每个条目，您可以：

- * *打开* *本地文件，当标记仍然有一个链接到它在磁盘上。
- * *导入* *没有本地文件时的文本包（将其保存在任何地方并在Marked中打开）。
- * *在Web上打开* *或* *复制链接* *共享URL。
- * *当已知本地路径时，在Finder中显示* *。
- * *忘记* *从此Mac中删除记录，而不删除在线文档。

连接后，列表将从共享中刷新。如果您处于离线状态或断开连接， Marked会显示缓存的记录，并可能提示您重新连接。

# #您可以发布的内容[what-you-can-publish]

您可以发布Marked可以呈现的任何文档，包括：

-保存的Markdown和文本文件
-瞬态预览（剪贴板、流式传输或未保存的文档）
- TextBundle和其他支持的格式

每个文档窗口一次只运行一个发布操作；在上传过程中禁用菜单项。

# # Tips [tips]

-发布包括预览引用的图像。 上传前可能会拒绝非常大的捆绑包；如果达到大小限制，请减少嵌入式资源。
-在TextPack中导出的突出显示使用Marked的突出显示JSON格式。 有关创建和导⟧出亮点的信息，请参阅⟦P0。
- Marked Share可在Direct、Mac App Store、Setapp和Marked Pro版本中使用。 发布无需单独订阅。
