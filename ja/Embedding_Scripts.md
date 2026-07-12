<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked に追加の JavaScript を埋め込む方法はいくつかあります。

## ドキュメントごとの JavaScript を含む

コンテンツ自体の `<script>` タグを使用して、単一のドキュメントにスクリプトを含めることができます。これは、特定のドキュメントでのみ必要なデータ視覚化用の [D3](https://d3js.org/) のようなライブラリに役立ちます。

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

MultiMarkdown をプロセッサとして使用している場合は、メタデータにスクリプトを含めることができ、スクリプトはドキュメントに挿入されます。 Marked は「スニペット」のみを出力するため、キー `XHTML Header` は理想的ではありません。代わりに、`CSS Header` を使用すると、スクリプトがドキュメントの最後に挿入されます。

	CSS ヘッダー: <script src="file.js"></script>

コンテンツが変更されたときに含まれるスクリプトを更新するには、[フック](#hooks) を参照してください。

## JavaScript を含む

ローカル ファイル、CDN から、または生のコードを貼り付けることで、独自の JavaScript を組み込むことができます。これにアクセスするには、{% prefspane Style %} を開き、*カスタム ルール* ボタンをクリックします。

新しいカスタム ルールを設定するか、既存のカスタム ルールにスクリプトを追加します。すべてのファイルにスクリプトを追加するには、述語を「ファイル名に * が含まれる」に設定します。

カスタム ルールのアクション エディターには、スクリプトを含めるための 3 つのオプションがあります。

JavaScriptファイルを挿入
: ドキュメントの最後に挿入するローカル ファイルを選択できます。

URLからJavaScriptを挿入
: CDN またはその他のリモート URL を含めることができます。これにより、URL がリンクされたドキュメントの末尾に `<script>` タグが作成されます。

JavaScript を挿入する
: 独自の JavaScript コードを作成/貼り付けることができるコード エディターが開きます。

これらのスクリプトは、プレビューの最後、ドキュメント タグの前に挿入されます。 init 関数を呼び出す必要がある場合、またはプレビューが更新されるたびに更新する必要がある場合は、[Raw JavaScript を含む](#rawjs) を参照し、Marked の [フック](#hooks) についてよく理解してください。

## マーメイドとその他のスクリプト {#mermaid}

jQuery はデフォルトで含まれており、以下のいずれかの方法を使用して Marked に追加するスクリプトでそれを使用できます。

マークダウン風の図作成用の [Mermaid](https://mermaid.js.org/intro/) がデフォルトですべてのドキュメントに含まれるようになりました。 `mermaid` 言語を含むフェンスで囲まれたコード ブロックは、自動的に図としてレンダリングされます。

Mermaid コンテンツが存在する場合、{% prefspane Style %} の下部にある「図のパンとズーム」のチェックボックスが使用可能になります。このボックスをチェックすると、図は {% kbd cmd %} スクロールでズームし、クリックしてドラッグするとパンします。この機能のスクリプトは CDN から含まれており、インターネット接続が必要です。

デフォルトで含めたい特定のライブラリがある場合は、[BrettTerpstra.com フォーラム](https://forum.brettterpstra.com/) または [サポート サイト](https://support.markedapp.com/questions/add) でお知らせください。

## フック [フック]

最近のバージョンでは、Marked はコンテンツを更新するときにページ全体の更新を実行しなくなり、ページの読み込みを必要とせずに新しいコンテンツを DOM に挿入します。これは、ページの読み込み時にトリガーされるスクリプトが含まれており、コンテンツが更新されても再トリガーされないことを意味します。 Marked は、これに対応する「フック」機能を提供します。フックを登録するには、[`Marked.hooks.register()` 関数](https://markedapp.com/jsapi/Marked.hooks.html#.register__anchor) を呼び出す 2 番目のスクリプト ブロックを含める必要があります。このブロックはトリガー (この場合は「update」) と実行する関数を受け取ります。

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<script>
	Marked.hooks.register('update', function() {
		// Re-run your D3 visualization when content updates
		d3.selectAll('.chart').each(function() {
			// your D3 render logic here
		});
	});
</script>
```

このフィールドでは、Marked の [API 機能](https://markedapp.com/jsapi/) がすべて使用できます。 (ロードされたスクリプトで API を使用することもできます。) ライブ プレビューでの API のインタラクティブなデバッグと実験については、マーク付きで Safari の [開発] メニューを使用する方法の詳細については、[WebKit インスペクター](Writing_Custom_CSS.html#webkitinspector) セクションを参照してください。

これで、更新が実行されるたびに (監視されているソース ファイルが保存されるたびに)、渡された関数が実行されます。実行しているスクリプトに何らかの init または render 関数がある限り、それをフックで呼び出して、ドキュメントが保存され更新がトリガーされるたびにレンダリングすることができます。



*[CDN]: コンテンツ配信ネットワーク