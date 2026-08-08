<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked には、プレビュー、エクスポート、ワークフロー統合を自動化するための AppleScript 辞書が含まれています。ドキュメントを開き、プレビューの制御 (再読み込み、スクロール、ハイライト、自動スクロール、高速読み取り)、統計の読み取り、プロセッサーとスタイルの変更、HTML または RTF のクリップボードへのコピー、および {% appmenu File, Export %} メニューで使用できるほとんどの同じ形式へのエクスポートが可能です。 **AppleScript による見出し/目次のプレビューは進行中です** (下記を参照)。

URL ベースの自動化 (シェル スクリプト、`open` コマンド、およびコールバック) については、[URL ハンドラー](URL_Handler.html) を参照してください。 AppleScript と URL ハンドラーは相互に補完します。特定のドキュメントまたはウィンドウをターゲットにする必要がある場合は AppleScript を使用し、単純な `open 'x-marked://...'` 呼び出しで十分な場合は URL を使用します。

## 辞書の表示 [viewing-the-dictionary]

**スクリプト エディタ**で、**ファイル → 辞書を開く…** を選択し、マーク済みを選択します。このディクショナリには、**application**、**document**、**window** オブジェクトのコマンドと、Marked スイートのエクスポート コマンドがリストされています。

macOS では、**スクリプト エディタ** を使用してスクリプト定義を参照できます。

## ターゲットをマークしました [targeting-marked]

標準インストールの場合:

```applescript
tell application "Marked"
	-- commands here
end tell
```

## ドキュメントとウィンドウ [documents-and-windows]

**アプリケーション**

- `documents` -- プレビュードキュメント (順序付きリスト) を開きます。
- `windows` -- プレビュー ウィンドウ。

**ドキュメント**

- `name` -- 表示名。
- `path` -- ドキュメントがディスクに保存されるときのファイル パス。
- `modified` -- ドキュメントに保存されていない編集者の変更があるかどうか。
- `processor` -- このプレビューのマークダウン プロセッサ (読み取り/書き込み)。有効な名前: `MultiMarkdown`、`Discount`、`CommonMark (GFM)`、`Kramdown`。 `processor` を設定すると、ドキュメントごとのオーバーライドが適用され、プレビューがリロードされます。 {% prefspane Processor %} のグローバルデフォルトは変更されません。
- `preprocessor` -- このプレビューのプリプロセッサ (読み取り/書き込み)。 `true` または `false` を使用して、カスタム プリプロセッサ、または該当する場合はプリプロセッサ名を有効または無効にします。
- `source text` -- 生の Markdown ソース (読み取り専用)。
- `critic markup mode` -- CriticMarkup 処理が有効かどうか (読み取り/書き込み)。変更するとプレビューが再ロードされます。
- `is autoscrolling` -- 自動スクロールがアクティブかどうか (読み取り専用)。
- `is speed reading` -- 高速読み取りモードがアクティブかどうか (読み取り専用)。
- プレビュー、リーダー、統計、およびエクスポートのコマンド (以下を参照)。

**窓**

- `document` -- そのウィンドウに表示されている `MarkdownDocument`。
- `style` -- 現在のプレビュー スタイル名 (読み取り/書き込み)。 `style` を設定すると、選択したテーマでプレビューが再ロードされます (プレビュー スタイル メニューからスタイルを選択するのと同じです)。
- `close`、`save`、`print` -- 標準ウィンドウコマンド。
- ドキュメントと同じプレビュー、リーダー、統計、エクスポート コマンド (ウィンドウのドキュメントに転送されます)。

特定のプレビューをエクスポートする場合は、`tell document 1` または `tell window 1's document` を優先します。アプリケーションのエクスポート コマンドは、受信者が指定されていない場合、キー ウィンドウまたは現在のドキュメントを使用します。

### 例: パスを開いて読み取る [example-open-and-read-path]

```applescript
tell application "Marked"
	open POSIX file "/Users/you/Documents/report.md"
	set docPath to path of document 1
end tell
```

### 例: プレビュー スタイルを変更する [example-change-preview-style]

```applescript
tell application "Marked"
	tell window 1
		set style to "Amblin"
	end tell
end tell
```

スタイル名は、プレビュー スタイル メニュー (表示名、`swiss` などの CSS リソース名、または内部識別子) と一致します。スタイル マネージャーで追加したカスタム スタイルがサポートされています。

有効なスタイル表示名を一覧表示するには、アプリケーション オブジェクトで **`get preview style names`** を使用します。

### 例: プロセッサとソース テキスト [example-processor-and-source-text]

```applescript
tell application "Marked"
	tell document 1
		set processor to "Kramdown"
		set md to source text
		set critic markup mode to true
	end tell
end tell
```

## アプリケーションコマンド [application-commands]

これらのコマンドは **アプリケーション** オブジェクト (特定のドキュメントではありません) に適用されます。

|コマンド |説明 |
| --- | --- |
| `open streaming preview` | [ストリーミング クリップボード プレビュー](Streaming_Preview.html) ウィンドウを開きます。 |
| `preview clipboard` |現在のクリップボードの内容の[クリップボード プレビュー](Opening_Files.html)を開きます（{% appmenu File, New, Clipboard Preview ({{shift}}{{cmd}}V) %}と同じ）。 |
| `close all` |開いているプレビュー ドキュメントをすべて閉じます (保存プロンプトは表示されません。マークするとソース ファイルは編集されません)。 |
| `get available processors` |プロセッサ名をリストします: `MultiMarkdown`、`Discount`、`CommonMark (GFM)`、`Kramdown`。 |
| `get preview style names` |有効なプレビュー スタイルの表示名をリストします。 |
| `get_available_formats` |サポートされている `convert_to` 形式名のリストを表示します。 |
| `get_available_profiles` |エクスポート プロファイル名をリストします (`profiles` プロパティと同じ)。 |

標準の AppleScript **`activate`** コマンドを使用して Marked を前面に表示します。

```applescript
tell application "Marked"
	activate
	open streaming preview
end tell
```

## プレビュー コントロール [preview-control]

**ドキュメント**と**ウィンドウ**で利用できます。これらのほとんどでは、ロードされたプレビュー WebView が必要です。

|コマンド |パラメータ |説明 |
| --- | --- | --- |
| `refresh preview` | — |ソースファイルからプレビューを再読み込みします（{% appmenu Preview, Refresh %}と同じ）。 |
| `reveal in finder` | — | Finder でドキュメント ファイルを表示します。 |
| `show highlights` | — |キーワードの強調表示を有効にします (単語、代替語、受動態、カスタム リストを避けます)。 |
| `full screen` |オプション `enabled` ブール値 |全画面プレビュー モードに入る、終了する、または切り替えます。 |
| `scroll to heading` | `title` または `id` |表示されているタイトル テキストまたは DOM `id` で見出しまでスクロールします。 |
| `scroll to position` | `percent` または `line` |文書の高さのパーセンテージまたはおおよその行番号でスクロールします。 |
| `copy html` | — |プレビュー HTML をクリップボードにコピーします (歯車メニューまたは {% kbd shift cmd C %}; [HTML のコピー](Exporting.html#copyhtml) を参照)。 |
| `copy rtf` | — |リッチテキストをクリップボードにコピーします。 |

```applescript
tell application "Marked"
	tell document 1
		refresh preview
		show highlights
		scroll to heading id "introduction"
		scroll to position percent 50
		full screen with enabled true
	end tell
end tell
```

## 自動スクロールと高速読み取り [autoscroll-and-speed-read]

|コマンド |説明 |
| --- | --- |
| `autoscroll` |自動スクロールを開始します。オプションの `wpm` 整数は、開始前に 1 分あたりの単語数を設定します。 |
| `stop autoscroll` |自動スクロールを停止します。 |
| `pause autoscroll` |自動スクロールを一時停止または再開します。 |
| `speed read` | [速度読み取り](Speed_Reading.html)を開始または切り替えます。 |
| `stop speed read` |速度読み取りを停止します。 |
| `pause speed read` |高速読み取りを一時停止または再開します。 |

`is autoscrolling` および `is speed reading` ドキュメント プロパティで状態を確認します。

```applescript
tell application "Marked"
	tell document 1
		autoscroll with wpm 250
		-- or: speed read
	end tell
end tell
```

## 統計 [statistics]

**`get statistics`** は、現在の Markdown ソース (統計ドロワーに表示される書式設定された文字列ではない) から計算された数値を含む `statistics_record` を返します。

|プロパティ |説明 |
| --- | --- |
| `word_count` |単語数 |
| `sentence_count` |文数 |
| `character_count` |文字数 |
| `paragraph_count` |段落数 |
| `average_words_per_sentence` |文あたりの平均単語数 |
| `average_syllables_per_word` |単語ごとの平均音節 |
| `complex_word_percentage` |複雑な単語の割合 |
| `reading_ease` |フレッシュな読みやすさ |
| `fog_index` |ガンニングフォグインデックス |
| `grade_level` |フレッシュ・キンケイドの学年レベル |
| `gulpease` | Gulpease インデックス (イタリア語の可読性; 該当しない場合は `0`) |
| `gulpease_band` |ガルピーズ バンド `1`–`4` (該当する場合) |
| `reading_time_minutes` | **250 WPM** での読書時間 |

```applescript
tell application "Marked"
	set stats to get statistics of document 1
	set wc to stats's word_count
	set fog to stats's fog_index
end tell
```

## 目次 (作業中) [table-of-contents-work-in-progress]

{% note %}
**WIP — まだ信頼できません。** ディクショナリには、ネストされたプレビュー見出し (`heading_item` レコード) を読み取るための **`headings`** プロパティと **`headings`** コマンドが含まれています。この自動化は、現在のビルドでは **正しく動作しません** (空の結果、強制エラー、または「結果が返されませんでした」)。今後のリリースで修正される予定です。それまでは既知のタイトルまたは ID を持つ **`scroll to heading`** を優先します。
{% endnote %}

**計画された動作** (完了時): 生の Markdown からではなく、**プレビュー** (`h1`–`h6`) の見出しからネストされた `heading_item` レコード。

|プロパティ |説明 |
| --- | --- |
| `title` |見出しテキスト |
| `id` | DOM `id` 属性 (存在しない場合は空の文字列) |
| `level` |見出しレベル `1`–`6` |
| `children` | `heading_item` レコードのネストされたリスト |

**`headings`** (ドキュメント プロパティ) — すべてのレベル。 **`headings levels {2, 3}`** (コマンド) — オプションのフィルター: 見出しの深さのみ (範囲ではありません)。

```applescript
-- Planned; do not rely on this yet
tell application "Marked"
	set toc to headings of document 1
	set filtered to headings levels {2, 3} of document 1
end tell
```

見出しの自動化が安定したら、**`scroll to heading id "..."`** とともに `id` 値を使用します。

## プロファイルを使用して印刷する [print-with-profile]

**`print with profile`** は、エクスポート プロファイルの印刷設定を一時的に適用してから、ドキュメントを印刷します ({% prefspane Export %} のエクスポート プロファイルと同じ環境設定バンドル)。

```applescript
tell application "Marked"
	tell document 1
		print with profile "Print Letter"
	end tell
end tell
```

プロファイル名では大文字と小文字が区別されます。印刷後、Marked は以前にアクティブだったエクスポート プロファイルを復元します。

## プロファイルをエクスポートする [export-profiles]

エクスポート プロファイルには、エクスポート/印刷設定 (マージン、ヘッダー、目次オプション、および{% prefspane Export %} の同様の設定) のバンドルが保存されます。

**プロファイル名の読み取り**

```applescript
tell application "Marked"
	set profileList to profiles
	-- or: get_available_profiles
end tell
```

**プロファイルを使用してエクスポート**

```applescript
tell application "Marked"
	tell document 1
		export html to "/Users/you/Desktop/report.html" with profile "My Profile"
	end tell
end tell
```

プロファイル名は大文字と小文字が区別され、保存されたプロファイルと正確に一致する必要があります。

## エクスポートコマンド [export-commands]

エクスポート コマンドは、**アプリケーション**、**ドキュメント**、**ウィンドウ** オブジェクトで使用できます。各コマンドには、出力パス (POSIX パス文字列または `file` オブジェクト) を含む **`to`** パラメーターが必要です。

|コマンド |出力 |
| --- | --- |
| `export markdown` |マークダウン (.md) |
| `export html` | HTML |
| `export paginated pdf` |ページ分割された PDF (印刷レイアウト) |
| `export continuous pdf` |連続スクロールPDF |
| `export epub` | EPUB |
| `export docx` | Microsoft Word (.docx) |
| `export odt` | OpenDocument テキスト |
| `export textbundle` |テキストバンドル |
| `export rtf` | RTF |
| `export opml` | OPML |

**注意事項**

- ページ分割された PDF は、{% appmenu File, Export As, Save PDF (Paginated) %} と同じ HTML から PDF へのパイプラインを使用します。未処理の HTML プレビュー ドキュメントには使用できません。
- HTML エクスポートでは、生の Markdown ソース ファイルではなく、**レンダリングされたプレビュー** (WebView に表示されるもの) が使用されます。
- 連続 PDF は、現在のプレビュー WebView レイアウトをキャプチャします。

### 基本的なエクスポート [basic-export]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Desktop/report.pdf"
	end tell
end tell
```

### エクスポート パスとサンドボックス [export-paths-and-sandboxing]

- 宛先ファイルには完全な POSIX パスを使用します。
- エクスポート パスが **開いているドキュメントのフォルダー内** にある場合、マークを付けると中間フォルダーを作成できます (たとえば、`.../MyProject/chapter.md` をプレビュー中に `.../MyProject/build/output.pdf` にエクスポートする場合)。
- ドキュメントのフォルダー外にエクスポートするには、マークがアクセスできる書き込み可能なパス (保存されたドキュメントの場所、セキュリティ対象のブックマーク、または [開く] ダイアログで許可したフォルダー) が必要です。パスが書き込み可能でない場合、コマンドはエクスポートが開始される前にエラーを返します。

## `with` オプション (プロパティ レコード) [with-options-properties-record]

`with profile` の代わりに、**`with`** または **`with properties`** を使用してオプションのレコードを渡すことができます。

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in", fontSize:"14"}
```

AppleScript はこれらのキーを直接認識します (エクスポート前にマッピングされます)。

|キー |説明 |例 |
| --- | --- | --- |
| `style` |エクスポート前に適用するプレビュー スタイル (完全なプレビューのリロード) | `"Amblin"`、`"Swiss"` |
| `pageSize` |印刷ページ サイズ名 | `"A4"`、`"Letter"` |
| `margins` |印刷余白 (下記を参照) | `"1in"`、`"1in 2in"` |
| `fontSize` |エクスポート/印刷の基本フォント サイズをポイント単位でオーバーライドします (ページ分割された連続 PDF)。 `"14"`、`"12pt"` |

`fontSize` は、{% prefspane Export %} と同じ **エクスポート/印刷用のカスタム フォント サイズ** オプションを有効にします。固定スクリーンプレイ サイズを使用する Fountain ドキュメントには影響しません。

`style` が含まれている場合、Marked はそのテーマを適用し、プレビューの再読み込みが完了するのを待ってからエクスポートします。個別の `set style` ステップは必要ありません。

レコード内の他のキーは、プロファイルの **エクスポート設定** 名と一致する可能性があります (`printBackgrounds`、`printTOC`、`topPrintMargin` など、{% prefspane Export %} に保存されている同じキー)。これらの値はエクスポートに一時的に適用されます。

競合するソースを不用意に結合することはできません。`with profile` を使用する場合は、最初にそのプロファイルをロードしてください。 `with` レコードを使用する場合、レコード内のプロファイル キーは、そのエクスポートの現在の設定をオーバーライドします。

### マージンの省略表記 [margin-shorthand]

`margins` 値は、1 ～ 4 つの測定値を含む文字列です。単位: `in`、`cm`、`mm`、`pt`、または`"` (インチ)。単位のない数値はポイントとして扱われます。

|値 |意味 |
| --- | --- |
| `1in` |すべての面 |
| `1in 2in` |上下`1in`、左右`2in` |
| `1in 2in 1in` |上`1in`、左右`2in`、下`1in` |
| `1in 2in 1in 2in` |上、右、下、左 |

```applescript
export paginated pdf to "/path/out.pdf" with {pageSize:"A4", margins:"1in 2in"}
export paginated pdf to "/path/out.pdf" with {style:"Amblin", margins:"1in 2in 1in 2in"}
```

### 組み合わせ例 [combined-example]

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/Users/you/Documents/MyBook/build/book.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

## `convert_to` [convert_to]

アプリケーション オブジェクトは、従来のスクリプト コマンドも公開します。

- **`convert_to`** -- Markdown テキストまたはファイル パスを形式 (`html`、`pdf`、`epub`、`docx`、`rtf` など) に変換します。オプションで `profile` および `output_path` も使用できます。
- **`get_available_formats`** -- サポートされている変換形式名のリストを表示します。
- **`get_available_profiles`** -- エクスポート プロファイル名をリストします (`profiles` プロパティと同じ)。

`convert_to` は、古いワークフローと AppleScript のみの自動化で引き続き利用できます。

## デバッグ [debugging]

{% prefspane Advanced %} で **デバッグ モード** を有効にします (または [設定] のデバッグ設定)。 Marked は、Console.app と Marked のログ ビューアにプレフィックス `[AppleScript]` を付けて情報レベルで AppleScript エクスポート ステップをログに記録します。

ページ分割された PDF エクスポートをトレースするときに役立つログ行:

- `paginated PDF: fetching preview HTML`
- `HTMLToPDFGenerator: loadHTMLString`
- `HTMLToPDFGenerator: didFinishLoadForFrame`
- `paginated PDF: generator finished`

長いエクスポート (特にページ分割された PDF) は、クライアントがエクスポート中にタイムアウトしないように、完了するまで AppleScript イベントを一時停止します。

## エラー [errors]

エクスポートが失敗すると、コマンドにスクリプト エラー文字列が設定されます (スクリプト エディターおよび `on error` ハンドラーで表示されます)。一般的なメッセージ:

- エクスポート パスは必須です。
・エクスポートディレクトリが存在しません（ドキュメントフォルダ外）。
- エクスポート ディレクトリを作成できないか、ファイルの書き込み時に権限エラーが発生しました。
- 不明なプレビュー スタイル名。
- スタイル変更後のプレビューのリロードを待機中にタイムアウトしました。
- ページ分割された PDF エクスポートがタイムアウトしたか、ページの生成中に失敗しました。

## 他のツールとの統合 [integration-with-other-tools]

html) の方が単純です。 [Marked Bonus Pack](Workflow_Integration.html#marked-bonus-pack) には、追加のスクリプトとサービスが含まれています。