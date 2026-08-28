<!-- MT draft for zh-Hant — Marked Share publish help. Review before publishing. -->
# <%= @title %>

**Marked Share** 是Marked 的線上發布服務，位於[share.markedapp.com](https://share.markedapp.com)。連接 Mac 一次，然後將正面文件發佈為 **TextPack**，其中包含圖像和可選的閱讀模式亮點。知道該連結的任何人都可以在網路上查看該文件。

此功能獨立於 macOS **共用擴充功能**（系統共用選單）。有關從其他應用程式將文件或選擇發送到 Marked 的信息，請參閱 [Using the Share Extension](Share_Extension.html)。

## 連接您的帳戶[connect-your-account]

在首次發布之前，將 Marked 連接到您的共享帳戶：

1. 選擇{% appmenu 檔案, 發佈, 連接帳號… %}。
2. Marked 開啟您的預設瀏覽器以登入 share.markedapp.com。
3. 批准連線後，瀏覽器將返回 Marked，並顯示安全登入連結。確認對話方塊中顯示的帳戶標籤。

Marked 将 API 令牌和设备密钥存储在此 Mac 上的 macOS 钥匙串中。憑證不會寫入日誌或崩潰報告中。

若要斷開連接，請選擇{% appmenu 檔案, 發佈, 斷開帳號… %}。已發布的文件保持在線；如果需要，可以隨時透過 share.markedapp.com 撤銷存取權限。

## 發布文件[publish-a-document]

在預覽中開啟文件後，選擇 {% appmenu 檔案, 發佈, 發佈… %}。

第一次發佈文件時，Marked 顯示一個小選項表：

- **標題** — 顯示在共用上（預設為不含副檔名的文件名稱）。
- **可見性** — 私有、不公開或公開。新發布預設**不公開**（可透過連結訪問，不公開列出）。
- **閱讀風格** — 社論、手稿、瑞士語、對比、打字機或 **無**。尽可能使用文档预览样式的默认值。 Share將此作為建議；讀者可以覆蓋它。選擇 **無** 以在沒有建議樣式的情況下發布。
- **包括亮点和评论** — 在 TextPack 中嵌入阅读模式亮点。當文件有突出顯示時預設為開啟。
- **允許其他人重新混合** - 啟用後，檢視者可以在共用上分叉文件。

Marked 在背景建置 TextPack（Markdown、資產和可選的 `highlights.json`），上傳它，並在這台 Mac 上記錄共用 URL。

### 更新現有發布[update-an-existing-publish]

將文件連結到“共用”後，選單項目會顯示“**更新已發佈的文件**”，而不是“**發佈...**”。選擇它來上傳新的 TextPack 版本。 Marked 發送伺服器的內容雜湊，以便偵測來自另一台 Mac 或 Web 的並發編輯。

如果其他人先在「共用」上更新了文檔，Marked 會詢問是否使用此 Mac 的版本**覆蓋**、**在 Web 上開啟**或**取消**。

## 發布後[after-publishing]

發布完成後，Marked 確認成功並提供：

- **複製分享連結** — {% appmenu 檔案, 發佈, 拷貝 Share 連結 %}
- **在網路上開啟** — {% appmenu 檔案, 發佈, 在網頁中開啟 %}

當前端文件具有連結的發布記錄時，這些命令適用於前端文件。

## 已發佈文件視窗 [published-documents-window]

選擇 {% appmenu 檔案, 發佈, 已發佈文件… %} 開啟從此 Mac 發布並從您的共用帳戶同步的文件清單。

對於每個條目，您可以：

- 當 Marked 在磁碟上仍有指向本機檔案的連結時，**開啟**本機檔案。
- **導入**當沒有本機檔案時TextPack（將其保存在任何地方並在Marked中開啟）。
- **在網路上開啟**或**複製連結**作為共享 URL。
- **當本機路徑已知時，在 Finder 中顯示**。
- **忘記** 從此 Mac 中刪除記錄，而不刪除線上文件。

連接後，清單將從「共享」中刷新。如果您離線或斷開連接，Marked 會顯示快取的記錄，並可能提示您重新連線。

## 你可以發布什麼[what-you-can-publish]

您可以發布 Marked 可以呈現的任何文檔，包括：

- 儲存的 Markdown 和文字文件
- 瞬時預覽（剪貼簿、串流媒體或未儲存的文件）
- TextBundles 和其他支援的格式

每個文件視窗一次僅執行一個發佈操作；上傳過程中選單項目已停用。

## 提示[tips]

- 發布包括預覽引用的圖像。非常大的捆綁包可能會在上傳前被拒絕；如果達到大小限制，請減少嵌入資產。
- 以 TextPack 匯出的反白顯示使用 Marked 的反白 JSON 格式。有關創建和導出高光的信息，請參閱[Reading Mode](Reading_Mode.html)。
- Marked Share 可在 Direct、Mac App Store、Setapp 和 Marked Pro 版本中使用。發布不需要單獨訂閱。
