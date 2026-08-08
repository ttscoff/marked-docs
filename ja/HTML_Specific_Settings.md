<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## 自動ヘッダー ID を無効にする [disable-automatic-header-ids]

マークには、ヘッダー ID の自動生成を無効にするオプションが含まれています。このオプションは {% prefspane Processor %} にあります。

## ランダムな脚注 ID [random-footnote-ids]

[**プロセッサ**] ペインで、[ランダムな脚注 ID を使用する] をオンにすると、ランダムな脚注 ID が生成されます。これにより、複数の文書が 1 つの Web ページに表示される場合の競合を回避できます。このオプションは、MultiMarkdown プロセッサを使用している場合にのみ使用できます。

## HTML 内のマークダウンの処理 [process-markdown-inside-of-html]

デフォルトでは、HTML ブロック タグ内の Markdown 構文は通常、Markdown プロセッサによって無視されます。このオプションは、Marked にブロック要素内での処理を強制的に継続させます。マークアップによっては問題が発生する可能性があることに注意してください。