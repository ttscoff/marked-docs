<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked には、ページ URL または選択したコンテンツを Marked 3 に直接送信できるブラウザ拡張機能が含まれています。

## インストール [install]

[https://markedapp.com/extensions](https://markedapp.com/extensions)] からダウンロードしてインストールします。

- Firefox / Zen
- クローム / ブレイブ / エッジ
- サファリ（バンドル）

## 拡張機能の仕組み [how-the-extension-works]

拡張機能ボタンをクリックすると、Marked 3 が `x-marked-3://markdownify` スキームを使用して処理するカスタム URL が開きます。

### `Markdownify URL` [markdownify-url]

拡張機能のポップアップで、**`Markdownify URL`** をクリックして、現在のページの URL をマーク済みに送信します。

### `Markdownify Selection` [markdownify-selection]

拡張機能のポップアップで、ページ内で選択項目があるときに **`Markdownify Selection`** をクリックします。

Marked は、現在の選択範囲の HTML を受け取り、それを Markdown に変換します。

### セクションの選択 (ブロック選択モード) [select-section-block-selection-mode]

![][1]

[1]: images/marked-3-chrome-1.jpg width=1280px height=800px class=center

**セクションの選択** をクリックして、「セクション選択モード」に入ります。

- ページ上にカーソルを置くと、選択できるブロック要素が強調表示されます。
- ブロックをクリックすると、すぐにマーク済みに送信されます (単一送信)。
- Cmd キーを押しながらブロックをクリックして複数のブロックを選択します (ブロックを削除するには Cmd キーを押しながらもう一度クリックします)。
- 現在選択されているブロックを送信するには、Return キーを押します。
- Esc を押してセクション選択モードをキャンセルします。

選択中に、ポップアップには、小さいセクションまたは密集したセクションをクリックするのに役立つズーム コントロールも表示されます。

![][2]

[2]: images/marked-3-chrome-2.jpg width=1280px height=800px class=center

- `-` ズームアウト
- **高さを合わせる** ページがビューポートの高さに合わせてズームします
- `+` ズームイン