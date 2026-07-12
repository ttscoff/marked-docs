<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked は、プレビューで提供する機能を提供するために JavaScript を大量に使用します。このため、ドキュメントの本文にスクリプトが含まれている場合、かなりの複雑な問題が発生する可能性があります。

## 外部スクリプト

ドキュメントの先頭にある「CSS Header:」メタデータ行を使用して、いくつかの外部スクリプトを含めることができます。ただし、これらのスクリプトはヘッダーではなく、jQuery と Marked のスクリプトが読み込まれた後でフッターに挿入されます。ほとんどの場合、これが理想的です。 Marked はスクリプトの競合の可能性をすべて補うことはできないため、予期しない動作が発生する可能性があります。 DOM の変更は特に問題となる可能性があります。

    CSS ヘッダー: <script src="file.js"></script>

## インラインインクルード

グラフ ジェネレーターや他の Canvas ツールなど、ドキュメントの本文に JavaScript を表示するためのアプリケーションは数多くあります。構成設定と使用しているプロセッサによっては、これらは壊れることがよくあります。解決策は、スクリプトと追加の DOM 要素を外部ファイルに置き、["raw" include files][syntax] に Marked の構文を使用することです。これらのファイルはいかなる方法でも処理されません。残りの処理が完了した後、その内容がファイルに追加されます。

    マークダウンテキスト。

    <<{file.html}

    さらにマークダウン テキスト...

Marked のプレビューで実行される JavaScript を実験およびデバッグするには、[WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) の手順を使用して、Safari の Web Inspector をプレビュー ウィンドウに接続できます。

[syntax]: Special_Syntax.html#includingunprocessedtextorhtml