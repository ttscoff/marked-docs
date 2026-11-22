# <%= @title %>

FerventMind のマップ (`.fvmd`) は Marked で開きます。Marked はパッケージを展開し、FerventMind が保存した `text.md` をプレビューします。

## マップの中の Markdown [markdown-in-the-map]

その Markdown の書き方は、FerventMind の **Settings > Files And Export** にある **Markdown** グループで決めます。Marked は保存されたファイルをそのまま表示します。

![FerventMind Files And Export][fm-export]

**Headings** は見出しのままにする階層の数です。**Visible topics only** は、折りたたまれた枝の中のトピックを省きます。**Notes** と **Task checkboxes** は、ノートとタスクをその Markdown に書くかどうかを決めます。これらの設定は、Markdown の書き出し、Copy As、そして Marked のようなアプリのために各マップへ保存される Markdown に使われます。マップごとに **Definitions • MAP** で上書きできます。

古いマップに `text.md` がないときは、Marked が `map.xml` からアウトラインを作ります。タイトルは見出し 1、次の階層は見出し 2、それより深いトピックは入れ子の箇条書きになります。ノートは節の本文になります。完了したタスクはチェック済みの箱になり、途中のタスクはパーセントを示します。画像は `assets/` 以下のファイルで、ファイル名のキャプションは付きません。

## マップを取り込む [including-a-map]

`.fvmd` の取り込みは、{% prefspane Apps %} の **Embed as Mermaid mind maps:** にある **FerventMind files** を使います。オンではマップから Mermaid 図を作ります。オフではマップの `preview.png` を埋め込みます。[マインド マップとアウトラインの埋め込み](Embedding_Mind_Maps_and_Outlines.html) を参照してください。

## エディタで開く [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) は FerventMind を起動します。

[fm-export]: images/screenshots/ferventmind-files-and-export.jpg @2x width=808px height=640px
