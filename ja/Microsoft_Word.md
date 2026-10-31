# <%= @title %>

Marked は Microsoft Word (`.docx`) ファイルを Markdown として開き、その Markdown を再び DOCX に書き出せます。

## 往復 [round-trip]

DOCX ファイルを開くと、Marked は見出しやリストなどの書式付きテキストを Markdown に変換します。変更履歴とコメントは CriticMarkup に、ハイライトは `<mark>` タグになります。DOCX に書き出すと、CriticMarkup を変更履歴として Word に戻せます。

読み込みと書き出し、ヘッダーとフッター、数式、独自の Word スタイルについては、[DOCX の扱い](Working_With_DOCX.html)を参照してください。
