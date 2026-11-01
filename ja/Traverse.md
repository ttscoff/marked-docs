# <%= @title %>

[Traverse][traverse] には **Stream to Marked** コマンドがあります。Marked 2 または Marked 3 が入っていると、書き出しメニューに表示されます。

## Stream to Marked [stream-to-marked]

書き出しメニュー（上向き矢印のボタン）を開き、**Stream to Marked** を選びます。

![Traverse の書き出しメニューにある Stream to Marked][stream]

Traverse が送る内容はアウトラインによって変わります。

- **Type** 属性を追加している場合、Traverse は Markdown 書き出しと同じ Markdown を送ります。
- Traverse の形式が **[Fountain](Fountain_for_Screenwriters.html)** に設定されていると、プレビューは Fountain の処理を自動的に有効にします。Traverse は送信するテキストの先頭に `<!--format:fountain-->` を付け、このコメントが処理を有効にします。[Streaming Preview](Streaming_Preview.html) を参照してください。
- どちらでもない場合、Traverse は簡単な Markdown リストを送ります。

[stream]: images/traverse-stream-to-marked.jpg @2x width=368px height=297px class=center

[traverse]: https://apps.shakingthehabitual.com/traverse/
