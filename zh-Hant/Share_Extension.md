<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked 包含一個 macOS **共享延伸功能**，會出現在系統共享選單中。您可以用它將檔案或選取的文字傳送到 Marked，而無需切換 App 或手動複製 URL。

共享延伸功能**隨 Marked 3 一併提供**。無需另行下載或安裝。Direct、Mac App Store、Marked Pro 與 Setapp 版本皆包含此功能。

## 運作方式

在共享選單中選擇 **Marked** 後，Marked 會立即開啟。沒有中間的撰寫視窗。

### 共享檔案

在 **Finder**（或其他可共享檔案的 App）中選擇 **共享 → Marked**。

Marked 接收檔案路徑，並以與其他流程相同的 `x-marked-3://open` URL 處理常式開啟。檔案會像在 Marked 中拖曳到 Dock 圖像或使用 {% appmenu File, Open... ({{cmd}}O) %} 開啟一樣。

支援檔案 URL、本機檔案，以及來源 App 提供的 Web URL。

### 共享選取文字

在 **TextEdit**、**Safari** 或 **Mail** 等 App 中選取文字，然後選擇 **共享 → Marked**。

Marked 將文字放入剪貼簿，並透過 `x-marked-3://paste` 處理常式開啟**暫時預覽**。這與 {% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %} 的未儲存預覽相同。之後可使用 {% appmenu File, Save Transient Preview %} 儲存。

當來源 App 提供時，支援純文字、HTML、RTF 與 Markdown。

底層命令的詳情請參閱 [URL Handler](URL_Handler.html)。

## 使用共享選單

### 從 Finder

1. 在 Markdown 或文字檔上按右鍵（或選取檔案後按 Finder 工具列中的**共享**按鈕）。
2. 在共享選單中選擇 **Marked**。

若看不到 **Marked**，請參閱下方的[啟用共享延伸功能](#enable-the-share-extension)。

### 從文字選取

1. 選取要預覽的文字。
2. 開啟 App 的**共享**選單（選單列共享項目、工具列共享按鈕或右鍵選單）。
3. 選擇 **Marked**。

Marked 會啟動（或移到最上層）並顯示共享內容的預覽。

## 啟用共享延伸功能

Marked 必須安裝在 `/Applications`（或您常用的應用程式資料夾）中，且至少啟動一次，macOS 才會列出其共享延伸功能。

### 在系統設定中啟用 Marked

1. 開啟**系統設定**。
2. 前往**一般 → 登入項目與延伸功能**（部分 macOS 版本為**隱私權與安全性 → 延伸功能**）。
3. 按一下**延伸功能**（或延伸功能旁的 **ⓘ** 按鈕）。
4. 選擇**共享**（或 **Sharing**）。
5. 啟用 **Marked**。

### 將 Marked 加入 App 的共享選單

即使延伸功能已在系統層級啟用，每個 App 仍可選擇要顯示哪些共享目標：

1. 開啟支援共享的 App（Finder 與 TextEdit 便於測試）。
2. 開啟**共享**選單。
3. 選擇**編輯延伸功能…**（較舊 macOS 可能顯示**更多…**或**延伸功能偏好設定…**）。
4. 在**共享**下勾選 **Marked**。
5. 可選：將 **Marked** 拖到列表較上方以便存取。

在大多數 App 中，變更會立即生效。

## 若共享選單中沒有 Marked

W> 共享延伸功能自 Marked 3.1.9 起提供。請確認已升級至至少該版本。

請依序嘗試以下步驟：

1. 安裝或更新後**啟動 Marked 一次**。若剛完成升級，請結束並重新開啟 Marked。
2. **確認延伸功能已在系統設定中啟用**，如上所述。
3. **自訂來源 App 的共享選單**。macOS 會隱藏不常用的共享目標，直到您啟用它們。
4. **檢查是否安裝了多個 Marked。** 若同時安裝 Direct 與 Mac App Store 版本，只有正在執行的副本會註冊延伸功能。移除或重新命名不用的副本，然後啟動需要的版本。
5. 若更新後延伸功能仍不出現，請**重新啟動 Mac**。macOS 會快取共享延伸功能註冊資訊。
6. 若您測試的是從 Xcode 或磁碟映像手動複製的建置，請**重新安裝 Marked 到 `/Applications`**。共享延伸功能必須嵌入 `Marked.app/Contents/PlugIns/`。

## 提示

- 共享延伸功能適合在不先建立檔案的情況下快速預覽網頁片段、郵件段落或筆記。
- 對於整頁或瀏覽器中的複雜選取，[瀏覽器延伸功能](Using_the_Browser_Extensions.html)可能提供更多控制（區塊選取、Markdownify URL 等）。
- 共享的檔案以一般 Marked 文件開啟並啟用檔案監看。共享的文字以暫時預覽開啟，直到您儲存。
