<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Marked のインクルード構文または IA Writer ブロック構文][include] によってインクルードされたファイルに CSV または TSV 拡張子がある場合、Marked はそれを解析して MultiMarkdown テーブルに変換しようとします。これは、カンマ区切りやタブ区切りのほか、自動的に検出される追加の区切り記号や引用符の形式など、ほとんどの標準形式で機能します。

Markdown テーブルを作成する代わりに CSV ファイルを使用する利点の 1 つは、セル内の改行が自動的に `<br>` タグに変換されることです。 MultiMarkdown テーブルを作成するときに改行を含めるにはこれを手動で行う必要があるため、さらに時間が節約されます。

余談ですが、ドキュメント内の表を簡単に編集できる [TableFlip][] という優れたアプリがあります。表形式のデータを頻繁に操作する場合は、チェックしてみる価値があります。

含まれている CSV ファイルの変更が監視されるため、元の CSV ファイルで追加の編集を行うことができ、Marked は保存時にプレビューを自動的に更新します。

変換されたテーブルは Markdown エクスポートに含まれるため、Marked を使用して構造化データを含むドキュメントをコンパイルし、単一のファイルをエクスポートできます。

[include]: Multi-File_Documents.html
[TableFlip]: http://tableflipapp.com/