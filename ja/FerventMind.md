# <%= @title %>

FerventMind のマップ (`.fvmd`) は Marked で開きます。Marked はパッケージを展開します。中に `text.md` があれば、そのファイルがプレビューです。なければ、Marked は `map.xml` からアウトラインを作ります。

## マップから作るアウトライン [outline-from-the-map]

トピックの文字は **Headings through level** で決めたレベルまで見出しになります (既定は 2)。それより深いトピックは入れ子の箇条書きになるので、その階層のタスクはリストのチェックボックスを保ちます。ノートは節の本文になります。完了したタスクはチェック済みの箱になり、途中のタスクはパーセントを示します。画像は `assets/` 以下のファイルで、ファイル名のキャプションは付きません。

## 見えているトピックだけを表示 [display-only-visible-topics]

{% prefspane Apps %} の *FerventMind* にある **Display only visible topics** は、Marked がそのアウトラインを作るとき、折りたたまれた枝の中のトピックを飛ばします。アプリがすでに保存した `text.md` は変えません。

## マップを取り込む [including-a-map]

`.fvmd` の取り込みは、{% prefspane Apps %} の **Embed as Mermaid mind maps:** にある **FerventMind files** を使います。オンでは、上のチェックボックスに合わせて、見えている木か全体の木の Mermaid 図になります。オフではマップの `preview.png` を埋め込みます。[マインド マップとアウトラインの埋め込み](Embedding_Mind_Maps_and_Outlines.html) を参照してください。

## エディタで開く [open-in-editor]

**Open in Editor** ({% kbd cmd E %}) は FerventMind を起動します。
