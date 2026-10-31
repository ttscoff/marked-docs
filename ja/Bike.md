# <%= @title %>

[Bike][bike] のアウトライン (`.bike`) を Marked にドラッグすると、見出し行は太字、タスクはチェックボックスの入れ子の Markdown リストとしてプレビューできます。

## Bike のアウトラインを開く [opening-a-bike-outline]

ファイルを開くと、Marked はアウトラインを変換します。

- 見出しとして印の付いた行は、**太字**のリスト項目になります。
- タスクは GitHub 形式のチェックボックスになります。Bike が完了時刻を保存しているか、チェック済みになっているとき、タスクはオンになります。
- 行のテキストにあるリンクとインラインの書式は Markdown のまま残ります。

`.bike` ファイルを開いたときは、常にこのリストになります。アウトラインは Mermaid 図にはなりません。

## Bike のアウトラインを取り込む [including-a-bike-outline]

`.bike` ファイルは、別の Markdown 文書に取り込むこともできます。[マインドマップとアウトラインの埋め込み](Embedding_Mind_Maps_and_Outlines.html)を参照してください。

{% prefspane Apps %} の *Mind Maps and Outlines* にある **Bike outlines** は、取り込んだファイルに適用されます。

- **オン**（既定）— Mermaid 図。`.bike` を除いたファイル名がルートノードになります。
- **オフ** — ファイルを開いたときと同じ入れ子の Markdown リスト。文書タイトルは付きません。

Mermaid 図には MultiMarkdown、CommonMark (GFM)、または Kramdown が必要です。Discount プロセッサでは描画されません。

[bike]: https://www.hogbaysoftware.com/bike/
