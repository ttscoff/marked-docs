# <%= @title %>

[Traverse][traverse] 內建 **Stream to Marked** 指令。安裝了 Marked 2 或 Marked 3 時，它會出現在匯出選單裡。

## Stream to Marked [stream-to-marked]

開啟匯出選單（帶向上箭頭的按鈕），選擇 **Stream to Marked**。

![Traverse 匯出選單中的 Stream to Marked][stream]

Traverse 送出的內容取決於大綱：

- 如果加入了 **Type** 屬性，Traverse 會送出與 Markdown 匯出相同的 Markdown。
- 如果大綱使用 **[Fountain](Fountain_for_Screenwriters.html)**，Traverse 會送出那段文字供預覽。
- 如果兩者都沒有，Traverse 會送出一份簡單的 Markdown 清單。

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
