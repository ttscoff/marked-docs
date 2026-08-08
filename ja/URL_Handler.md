<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked の URL ハンドラーは、追加のスクリプト機能とワークフロー機能を提供します。別のアプリケーションのメモに URL を含めることができます。たとえば、クリックするとマークされたファイルが開きます。以下に示すように、いくつかのアクションを実行できます。

## URL スキーム [the-url-scheme]

Marked の URL スキームは `x-marked` で、`x-marked://open?file=/Users/username/Desktop/report.md` のようなオプションで呼び出されます。

`x-marked` の代わりに `x-marked-3` を使用すると、マーク 3 を具体的にターゲットにすることができます。メソッドとパラメータは`x-marked`とまったく同じですが、Marked 3のみが`x-marked-3`に応答します。

## コマンドライン/スクリプトからの呼び出し [calling-from-the-command-linescripts]

コマンドラインまたはスクリプトから URL ハンドラーを呼び出すには、macOS [`open` コマンド](http://brettterpstra.com/2014/08/06/shell-tricks-the-os-x-open-command/) を使用します。

	「xマークの://open?file=ファイル名.md」を開きます
	「xマークの://refresh?file=ファイル名.md」を開きます

### バックグラウンドでの通話 [calling-in-the-background]

`-g` フラグを指定して `open` コマンドを呼び出して、フォーカスを切り替えずにバックグラウンドで結果を実行できます。バックグラウンドでコマンドを実行し、フォーカスを奪わずにウィンドウを最上部に上げるには:

	open -g 'x-marked://open?file=filename.md&raise=true'

## オプションのパラメータ [optional-parameters]

### ×-成功 [x-success]

どのコマンドでも **x-success** クエリ パラメーターを指定できます。コマンド実行後に呼び出されるURLを設定します。例: `x-marked://open/?file=filename.md&x-success=ithoughts:`。バンドル識別子 (`com.googlecode.iterm` など) を指定して、URL スキームを持たないアプリケーションを開くこともできます。

### レイズ [raise]

**raise** パラメータは、`file` パラメータを受け入れるコマンド、またはすべてのウィンドウに影響を与えるコマンドとともに渡すことができます。アクションが実行された後、影響を受けるウィンドウは、コールバックを返すか実行する前に、他のすべてのウィンドウ (すべてのアプリケーション) の上に表示されます。

	「xマーク://refresh?file=ファイル名.md&raise=true」

### 速読 [speedread]

**speedread** パラメーターは、プレビュー ドキュメント (`open`、`paste`、`preview`、および `stream`) を開く URL ハンドラー コマンドで渡すことができます。 `speedread=1` を設定すると、ターゲットのプレビューの準備ができたらすぐに Speed Read が自動的に開始されます。

例:

	x-marked://open?file=/Users/username/Desktop/report.md&speedread=1

	x-marked://preview?text=Some%20text&speedread=1

	xマーク://paste?speedread=1

# 利用可能なコマンド [available-commands]

`x-marked` URL ハンドラーでは次のコマンドを使用できます。

## スタイルを追加 [addstyle]

新しいカスタム スタイルを Marked に追加します。

##### パラメータ: [parameters]

**css**: カスタム スタイルに書き込む URL エンコードされた CSS テキスト。 **file** パラメータを渡す場合を除き、必須です。

**file**: マークに追加する CSS ファイルへのフルパス (POSIX)。 **css** パラメータを渡す場合を除き、必須です。

**name**: 生成するスタイルの名前。

**css** パラメータを使用すると、これはディスクに書き込むときのファイル名 (「.css」が追加されたもの) とメニュー項目名の両方として使用されます。 **css** パラメータには必須ですが、**file** にはオプションです (ファイル名は、name パラメータが空であるかのように使用されます)。

	x-marked://addstyle?name=My+new+style&css=...

	x-marked://addstyle?file=/Users/myuser/Custom+Styles/Unicorn.css

file パラメータに名前を含めると、メニュー項目はファイル名の代わりにその名前を取得します。別のパスで同じ名前を再度使用すると、メニュー項目は同じ名前の 2 番目の項目を追加するのではなく、新しいパスで更新されます。

## デフォルト [defaults]

ユーザー設定を設定します。キーと値のリストをクエリ パラメーターとして受け入れます。既存のキーのみが設定されます。環境設定の変更に更新が必要な場合、`refresh=0` が渡されない限り、すべてのウィンドウが自動的に更新されます。

ブール値の true には 1、false には 0 を使用します。

##### パラメータ: [parameters-2]

**更新** _(オプション)_: 0 に設定すると、開いているプレビュー ウィンドウの自動更新が無効になります

* デフォルト: 1 (真)

##### 例: [example]

x-marked://defaults?syntaxHighlight=1&includeMathJax=0

`defaults` メソッドは主に、開発者が設定で使用できない難解な機能へのリンクを追加できるように設計されています。ただし、自動化するときに切り替えたい標準オプションがいくつかあるかもしれません。自動化中に制御したい一般的な設定は次のとおりです。

構文ハイライト
: 構文の強調表示を有効または無効にします

includeMathJax
: 内部 MathJax 処理を有効または無効にします。

プロセッサー
: プロセッサを MultiMarkdown に変更するには `multimarkdown` または `mmd` に設定し、割引プロセッサを使用するには `discount` または `gfm` に設定します

h1IsPageBreak、h1IsPageBreak、breakBefore脚注
: エクスポート時にヘッダー レベル 1 と 2、および脚注の前に自動改ページします。


## ディンガス [dingus]

さまざまな Markdown プロセッサをテストするには、Markdown Dingus を開いてください。

	xマーク付き：://dingus

##### パラメータ: [parameters-3]

**プロセッサ** (オプション): デフォルトで選択するプロセッサを指定します。有効な値:

- `multimarkdown` - MultiMarkdown プロセッサ
- `commonmark` - CommonMark (GFM) プロセッサー
- `discount` または `discount (gfm)` - 割引プロセッサー
- `kramdown` - Kramdown プロセッサー

例:

- `x-marked://dingus?processor=kramdown` - Kramdown が選択された状態で開きます
- `x-marked://dingus?processor=commonmark` - CommonMark (GFM) が選択された状態で開きます

*注意:* これにより、Markdown Dingus ウィンドウが開き、さまざまな Markdown プロセッサ (MultiMarkdown、CommonMark (GFM)、Discount、および Kramdown) を並べてテストおよび比較できるようになります。 Markdown 構文を実験し、プロセッサの違いを理解するのに最適です。

## スタイルスティーラー / 盗む [stylestealer-steal]

スタイル スティーラー HUD を開きます。ライブ ページから CSS をキャプチャする場合、または UI から起動せずに手動コンテンツ抽出セッションを実行する場合に便利です。

	同義語: x-marked://stylestealer … 、x-marked://steal …

##### パラメータ: [parameters-4]

**url** _(オプション)_: [スタイル スティーラー] ウィンドウに事前に入力する URL。省略した場合、HUD は空白で開きます。

例:

- `x-marked://stylestealer?url=https%3A%2F%2Fmarkedapp.com`
- `x-marked://steal/https:%2F%2Fexample.com`

## importurl / markdownify [importurl-markdownify]

「URL のインポート」(Content Extractor) ウィンドウを開いて、Markdownifier パイプラインを手動で実行できるようにします。これは抽出を自動的に実行しません**。これは以下の `extract` コマンドによって処理されます。

	同義語: x-marked://importurl …、x-marked://markdownify …

##### パラメータ: [parameters-5]

**url** _(オプション)_: [インポート URL] フィールドに事前入力します。省略した場合、ウィンドウが開き、リンクの貼り付けを待機する空のフィールドが表示されます。
**html** _(オプション、markdownify のみ)_: `x-marked://markdownify` で提供される場合、これは URL エンコードされた生の HTML である必要があります。 Marked は、クリップボード プレビューと同じルールを使用して HTML を Markdown に変換し、その HTML をクリップボード プレビュー ウィンドウに貼り付けたかのように、一時的なドキュメントで開きます。

例:

- `x-marked://importurl?url=https%3A%2F%2Fexample.com%2Farticle`
- `x-marked://markdownify/https:%2F%2Fnews.ycombinator.com`

## する [do]

ドキュメント ウィンドウで JavaScript コマンドを実行します。 Marked の JavaScript API 全体は [ここに文書化されています](https://markedapp.com/help/jsapi/)。

##### パラメータ: [parameters-6]

**js** _(必須)_: JavaScript コマンドを含むクエリ文字列

* ファイル名または「すべて」を参照するパスパラメータを受け入れます
* / で分割されたパスは複数のファイルを検索します
* 部分的なファイル名が完全に一致します

		xマーク://do/ファイル名1/ファイル名2?js=...
		xマーク://do/all?js=...

**file**: カンマ区切りのパス/ファイル名を含むクエリパラメータ

	xマーク://do?file=ファイル名1,ファイル名2&js=...

ファイル名が指定されていない場合（または「all」が渡されていない場合）、最前面のウィンドウで動作します。

## 助けて [help]

オプションでトピックを指定して、マークされた内部ヘルプ システムを開きます。これは主に内部で使用するためのものですが、URL 経由でアクセスできます。見出しの右側にあるブックマーク アイコンを右クリックし、[__リンクのコピー__] を選択すると、特定のセクションへの URL をコピーできます。 **マーク 3** のアプリ内ヘルプと検索では、これらのリンクに `x-marked-3` スキームが使用されるため、マーク 2 もインストールされている場合、macOS はマーク 3 でリンクを開きます。以下の例ではその形式を使用しています。

##### ディンガス [dingus-2]

さまざまな Markdown プロセッサをテストするには、Markdown Dingus を開いてください。

	xマーク付き：://dingus

######## パラメータ:

**プロセッサ** (オプション): デフォルトで選択するプロセッサを指定します。有効な値:

- `multimarkdown` - MultiMarkdown プロセッサ
- `commonmark` - CommonMark (GFM) プロセッサー
- `discount` または `discount (gfm)` - 割引プロセッサー
- `kramdown` - Kramdownプロセッサ

例:

- `x-marked://dingus?processor=kramdown` - Kramdown が選択された状態で開きます
- `x-marked://dingus?processor=commonmark` - CommonMark (GFM) が選択された状態で開きます

*注意:* これにより、Markdown Dingus ウィンドウが開き、さまざまな Markdown プロセッサ (MultiMarkdown、CommonMark (GFM)、Discount、および Kramdown) を並べてテストおよび比較できるようになります。 Markdown 構文を実験し、プロセッサの違いを理解するのに最適です。

##### パラメータ: [parameters-7]

**ページ** _(オプション)_: 既存のページの正確なタイトル (オプションのアンカー ハッシュ付き)

	x-marked-3://help?page=Document_Statistics

マーク付きヘルプ ファイルの命名規則に従って、スペースはアンダースコアに置き換えられます。アンカーを指定する場合、ハッシュ (#) の代わりにコロン (:) を使用できます。

ターゲットはパスのみで (クエリ文字列なしで) 指定できます。

	x-marked-3://help/Keyword_Highlighting:editingkeywords


## 抽出 [extract]

Web URL からコンテンツを抽出し、Marked で新しいドキュメントとして開きます。

	xマーク://extract?url=https://example.com

##### パラメータ: [parameters-8]

**url** _(必須)_: コンテンツを抽出する Web URL。 `http://` または `https://` で始まる必要があります

**window** _(オプション)_: ウィンドウの名前

**id** _(オプション)_: 名前空間識別子

**base** _(オプション)_: 相対リンクのベース URL

**上げる** _(オプション)_: 開いた後にウィンドウを上げるには、`true` に設定します。

**manual** _(オプション)_: `true` に設定すると、自動抽出を実行する代わりに Style Stealer 手動抽出ウィンドウが開きます。

- `manual=true` の場合、マークはスタイル スティーラーを開き、URL フィールド (指定されている場合) を事前に入力し、自動の開くダイアログを抑制し、保存する前にスタイル/コンテンツを対話的に選択して抽出できるようにします。
- 省略または `false` の場合、Marked は自動抽出ツール (Markdownifier) を実行し、結果を新しい一時ドキュメントとして直接開きます。

##### 例: [examples]

	xマーク://extract?url=https://news.ycombinator.com

	xマーク://extract?url=https://github.com&window=GitHub&raise=true

	xマーク://extract?url=https://example.com/article&manual=true

	xマーク://extract?url=https://blog.example.com/post-title

*注意:* このコマンドは、Marked のコンテンツ抽出サービスを使用して Web ページを取得し、Readability を使用してクリーンなコンテンツを抽出し、Markdown 形式に変換し、結果を新しい一時ドキュメントで開きます。抽出されたコンテンツにはメタデータ (タイトル、ソース URL、日付) が含まれており、クリーンなマークダウンとしてフォーマットされます。 Web コンテンツをすばやくキャプチャして編集するのに最適です。

## 開く [open]

指定されたドキュメントをマークで開きます。

	xマーク://open?file=/Users/ユーザー名/Desktop/report.md

##### パラメータ: [parameters-9]

**file** *(必須)*: 開くドキュメントへの完全な POSIX パス、またはパスのカンマ区切りリスト

**speedread** *(オプション)*: 開いた後に Speed Read を自動的に開始するには、`1` に設定します。

`open` は、コンポーネントが 1 つの URL に結合されるパスも受け入れます

	×マーク://open/~/nvALT2.2

指定されたファイル パスが存在しないか、開けない場合でも、Marked が最前面に表示されます。 *file* パラメーターを指定せずに実行するか、値を空白にして実行すると、単にマーク付きが開きます。

URL ハンドラーでファイルのパスのみが呼び出された場合にも、Marked はファイルを開きます。 `x-marked:///Users/username/Desktop/report.md`。

## ペースト [paste]

クリップボードの現在の内容から新しいドキュメントを作成します。

	xマーク://貼り付け

##### パラメータ: [parameters-10]

**speedread** *(オプション)*: `1` に設定すると、クリップボードのプレビューを開いた後に Speed Read が自動的に開始されます。

*注意:* これにより、「クリップボードのプレビュー」コマンドを使用して一時ドキュメントが作成されます。クリップボード内のテキストはすべて、新しい空の文書に追加され、マーク付きで開かれます。保存せずに閉じると破棄されます。

## プレビュー [preview]

新しいドキュメント内の指定したテキストをプレビューします。

	x-marked://preview?text=Some%20text%20to%20%2A%2Apreview%2A%2A%0A

##### パラメータ: [parameters-11]

**テキスト** *(必須)*: プレビューに挿入するテキスト。パーセントエンコードされたテキストは、ドキュメントを表示する前にエンコードされません。

**speedread** *(オプション)*: `1` に設定すると、プレビュー テキストを開いた後に Speed Read が自動的に開始されます。

## ストリーム [stream]

ストリーミング クリップボードのプレビュー ウィンドウを開きます。

	x マークの付いた://ストリーム

##### パラメータ: [parameters-12]

**speedread** *(オプション)*: `1` に設定すると、ストリーミング プレビューを開いた後に Speed Read が自動的に開始されます。

*注意:* これにより、「クリップボードのプレビュー」コマンドを使用して一時ドキュメントが作成されます。渡されたテキストは新しい空のドキュメントに追加され、それがマーク付きで開かれます。保存せずに閉じると破棄されます。

## リフレッシュ [refresh]

ドキュメントのプレビューまたは開いているすべてのプレビューを更新します。

##### パラメータ: [parameters-13]

**file**: カンマ区切りのパス/ファイル名を含むクエリ パラメータ (ファイルは現在マーク済みで開いている必要があります)。 `file` パラメータを指定せずに呼び出すか、`?file=all` を呼び出すと、開いているすべてのウィンドウが更新されます。

*file* パラメータは部分的なものにすることができます。マークすると、*filename* (完全パスではない) の部分一致で開いているすべてのウィンドウが更新されます。 「all」を渡すと、すべてのウィンドウが更新されます。

	xマーク://refresh

	xマーク://refresh?file=/Users/ユーザー名/Desktop/report.md

	xマーク://refresh?file=report.md

`file` パラメータを指定せず、URL にドキュメント パスを指定して呼び出された場合、/ で分割されたパスで複数のファイルが検索され、部分的なファイル名が最も一致するものを完成させます。

	x マーク://refresh/ファイル名1/ファイル名2

## スタイル [style]

1 つ以上のドキュメントのプレビュー スタイル (CSS) を設定します。

##### パラメータ: [parameters-14]

**css** _(必須)_: スタイルの名前またはパスを含むクエリ文字列。スタイルは、デフォルトまたは手動で追加されたカスタム スタイルとして Marked のスタイル メニューに存在する必要があります。

* ファイル名または「すべて」を参照するパスパラメータを受け入れます
* / で分割されたパスは複数のファイルを検索します
* 部分的なファイル名が完全に一致します

		xマーク://style/filename1/filename2?css=...
		x-marked://style/all?css=...

**file**: カンマ区切りのパス/ファイル名を含むクエリパラメータ

	x-marked://style?file=filename1,filename2&css=...

ファイル名が指定されていない場合 (または "all" が渡されていない場合)、このメソッドは最前面のウィンドウで動作します。