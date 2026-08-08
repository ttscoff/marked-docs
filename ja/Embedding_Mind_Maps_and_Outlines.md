<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

マインド マップとアウトラインは、[Marked のインクルード構文][include] または [IA Writer ブロック構文][ia] を使用して Markdown プレビューに埋め込むことができます。この動作は、ファイル形式と、*マインド マップ/アウトライン* の {% prefspane Apps %} にある [マップを人魚図として埋め込む] 設定によって異なります。

[include]: Multi-File_Documents.html
[ia]: Multi-File_Documents.html#ia-writer-block-syntax

## サポートされている形式 [supported-formats]

### iThoughts X (.itmz) [ithoughts-x-itmz]

iThoughts マインド マップ ファイルは、マップ データとオプションのプレビュー イメージを含む zip アーカイブです。

### MindManager (.mmap) [mindmanager-mmap]

MindManager ファイルは、`Document.xml` を含む zip アーカイブです。解凍された MindManager パッケージ (`Document.xml` を含むフォルダー) および `Document.xml` への直接パスもサポートされています。

### フリーマインド (.mm) [freemind-mm]

FreeMind マインド マップ ファイルは、`.mm` 拡張子を使用し、データを XML として保存します。 Marked は、ファイルの内容が `<map` で始まることを確認することで FreeMind フォーマットを検出します。そうでない場合 (コード スニペットなど)、ファイルはプレーン テキストとして含まれます。 FreeMind ファイルは、Mermaid マインド マップの埋め込みでサポートされています。

### OPML (.opml) [opml-opml]

OPML (Outline Processor Markup Language) は、アウトライナーやフィード リーダーで広く使用されている階層アウトラインの XML 形式です。 iThoughts およびその他のアプリは OPML にエクスポートできます。マークすると、含まれている OPML ファイルが Mermaid マインド マップ図に変換されます。

### バイク (.bike) [bike-bike]

Bike.app のアウトラインは独自の HTML ファイルとして保存されます (`.bike`)。 `.bike` ファイルを Marked で直接開くことができます。ドキュメントは、メイン見出し (H1) としてファイル名 (拡張子を除く)、トップレベルの見出し項目を H2 として、ネストされた見出しを太字のリスト項目として、タスクを GitHub スタイルのチェックボックスとしてマークダウンとしてレンダリングされます。 `.bike` ファイルが include 構文を介してインクルードされる場合、Bike の「マーメイド図として埋め込む」設定 (アプリ → マインド マップ/アウトライン内) によって、ファイルがマーメイド マインド マップ (ルート ノードとしてファイル名を持つ) になるか、ネストされたマークダウン リスト (H1 なし) になるかが制御されます。

## 地図を人魚図として埋め込む [embed-maps-as-mermaid-diagrams]

**有効** (デフォルト) の場合、マークは含まれているマインド マップとアウトラインを [マーメイド](https://mermaid.js.org/) 図に変換します。

**iThoughts、MindManager、FreeMind、OPML、Bike** — 整ったツリー レイアウトを使用してマーメイド マインドマップ図としてレンダリングされます。 iThoughts および MindManager の場合、形状情報 (円形、長方形、六角形など) が利用可能な場合には保存されます。 FreeMind (`.mm`) と OPML は同じマインド マップ形式を使用します。 Bike (`.bike`) のアウトラインでは、含まれているファイル名 (拡張子を除く) がマインド マップのルート ノードとして使用されます。ノード ラベルはプレーン テキストです (リンクはリンク テキストになり、タスクは ☐ / ☑ プレフィックスとして表示されます)。 Mermaid は、すべての Markdown プレビューにデフォルトで含まれています。

**制限事項:** マインド マップの埋め込み (人魚図) は、Discount パーサーでは機能しません。マインド マップのプレビューには、MultiMarkdown、CommonMark (GFM)、または Kramdown を使用します。

**無効**の場合:

- **iThoughts** — .itmz ファイルの組み込みプレビュー イメージ (`preview.png`) は、base64 イメージとして埋め込まれます。画像の代替テキストにはファイル名が使用されます。
- **MindManager** — アウトラインはネストされた Markdown リストとして埋め込まれます。
- **FreeMind** — アウトラインはネストされたマークダウン リストとして埋め込まれます。
- **OPML** — アウトラインはネストされたマークダウン リストとして埋め込まれます (マインド マップはありません)。
- **Bike** — アウトラインはネストされたマークダウン リスト (H1 なし) として埋め込まれます。最上位の見出し項目は H2 になり、ネストされた見出しは太字になり、タスクは GitHub チェックボックスになります。

## インクルード構文 [include-syntax]

他のファイルの場合と同じ構文を使用します。

	<<[パス/map.itmz]
	<<[パス/to/map.mmap]
	<<[パス/to/map.mm]
	<<[パス/to/outline.opml]
	<<[パス/to/outline.bike]

または、iA Writer ブロック構文を使用します。

	/path/to/map.itmz

パスはメインドキュメントを基準とした相対パスまたは絶対パス (`/` または `~` で始まる) にすることができます。詳細については、「複数ファイル文書」(Multi-File_Documents.html)を参照してください。

## OPML 変換 [opml-conversion]

OPML ファイルは、`text` 属性を持つネストされた `<outline>` 要素を使用します。 「マーメイド図として埋め込む」が有効になっている場合 ([設定: アプリ](Settings_Apps.html) を参照)、変換により、iThoughts および MindManager と同じ形式を使用してマーメイド マインド マップが生成されます。

- `<body>` の子アウトラインが最上位になります (複数の最上位項目がある場合は、「アウトライン」ルートの子)
- ネストされたアウトラインが階層を定義します
- 欠落または空の `text` は `(unnamed)` として表示されます
- テキストはサニタイズされています。 Mermaid では特殊文字がエスケープされます

## バイクの変換 [bike-conversion]

Bike `.bike` ファイルは、ルート `<ul>` および `<li>` 項目を含む HTML です。項目には、`data-type="heading"` (開いたときまたはリストモードでトップレベル→ H2、ネスト→太字) または `data-type="task"` (GitHub チェックボックス、`data-done` にタイムスタンプがあるか、`data-checked` / `data-completed` が true のときに完了) を含めることができます。ノードテキスト内のインライン書式設定とリンクはマークダウンに変換されます。 Mermaid マインドマップとして埋め込む場合、ファイル名 (拡張子を除く) が単一のルート ノードとして使用され、ラベルは Mermaid マインドマップ構文用にフォーマットされたプレーン テキストになります。