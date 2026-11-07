# <%= @title %>

[Tree Outliner][tree] の文書 (`.treeoutline`) を Marked にドラッグすると、見出しとリスト、または Mermaid 図としてプレビューできます。

## 見出しとリスト [headings-and-lists]

これが既定です。Marked はアウトラインを Markdown にまとめます。

- 文書タイトルはレベル 1 の見出しになります。
- アウトラインの行は、{% prefspane Apps %} の *Tree Outliner* グループにある **Headings through level** で決めたレベルまで見出しのままです。既定は **2** なので、アウトラインの最初の行はレベル 2 の見出しになり、それより深い行は入れ子のリストになります。
- 行のノートは、その見出しまたはリスト項目の下の段落になります。

## Mermaid 図 [mermaid-diagram]

{% prefspane Apps %} の *Mind Maps and Outlines* で **Tree Outliner outlines** をオンにすると、ファイルを Mermaid 図としてプレビューします。文書タイトルがルートノードです。同じスイッチは、`.treeoutline` ファイルを開くときと、別の文書に[取り込む](Embedding_Mind_Maps_and_Outlines.html)ときの両方に適用されます。

**Headings through level** が使われるのは、そのスイッチがオフのときだけです。

Mermaid 図には MultiMarkdown、CommonMark (GFM)、または Kramdown が必要です。Discount プロセッサでは描画されません。

[tree]: https://noteifyapp.com/tree-outliner/
