<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked は、Microsoft Word ファイルの操作を広範にサポートしています。一般的なワークフローは、*最初にプレビュー、2 番目に DOCX をエクスポート**です。Marked で Markdown を開くか確認し、ライブ プレビューでスタイルと校正を調整し、ドキュメントの準備ができたら Word にエクスポートします。

## DOCX ファイルを開く [opening-docx-files]

マークは DOCX ファイルを読み取り、クリーンなファイルに変換できます
マークダウン。見出しやリストなどの有効なスタイル要素は、
同等のマークダウンに変換されます。

変更追跡とコメントはに変換されます
CriticMarkup。ハイライトは`<mark>` タグに変換されます。
必要に応じて色を付けます。

## DOCX ファイルのエクスポート [exporting-docx-files]

エクスポート パレットを使用して、ファイルから DOCX ファイルを生成します。
マークダウン。保存ダイアログでは、組み込みのファイルを指定できます。
スタイル --- このスタイルは Word で次のように簡単に変更できます。
テーマセレクターを開いて新しいテーマを選択します。

### ヘッダーとフッター [headers-and-footers]

{% prefspane Export %} でヘッダーとフッターを設定すると、エクスポートされた DOCX にそれらが含まれます。 `%title`、`%date`、`%page`、`%total` などの標準のプレースホルダーは、エクスポート時に置き換えられます。 `%logo` と `%image` は、ヘッダー/フッター設定からロゴを埋め込みます。 `%md_*` メタデータ変数は、ドキュメントの MultiMarkdown メタデータから解決されます。 `%h1`--`%h6` は、エクスポートされた見出しスタイルに関連付けられた Word **STYLEREF** フィールドになります。文書を開いたときに Word によって入力されます。完全な変数リストと DOCX と印刷/PDF の動作の違いについては、[エクスポート](Exporting.html#headers-and-footers) を参照してください。

## 変更追跡 [change-tracking]

Markdown ドキュメント内の CriticMarkup 構文は変換されます
DOCX にエクスポートすると Word Change Tracking に変換されます。コメント
次の挿入、削除、置換により、
変更追跡時に Word の右側の列に表示されます
有効になっています。

Marked に DOCX ファイルをインポートすると、変更追跡が行われます。
CriticMarkup と `<mark>` タグに変換されます
適切です。

## 数学 [math]

ドキュメントに表示される MathJax および Katex 方程式は、Word で表示するために MathML に変換されます。この変換は完全ではありませんが、ほとんどの場合、Word 文書内の有効な数式ブロックがレンダリングされます。これはエクスポートにのみ適用されます。Word 文書内の数式ブロックはインポート時に変換されません。

## カスタムエクスポートスタイルの追加 [adding-custom-export-styles]

`~/Library/Application Support/Marked/Custom Word Styles/` にテンプレートとstyles.xml ファイルを含めることで、独自のエクスポート スタイルを追加できます。これらを作成するには:

1. マーク付きで生成された DOCX ファイルを Word で開きます
2. スタイルエディターで各要素のスタイルを編集し、それぞれの「テンプレートに追加」を選択します。
3. DOCX ファイルを保存します。
4. 上部バーの [**デザイン**] に移動し、左側の [*テンプレート*] ドロップダウンから [**現在のテンプレートを保存**] をクリックしてテンプレートを生成します。 「マークされたスタイル」メニューに表示する名前を付けて、`~/Library/Application Support/Marked/Custom Word Styles/STYLENAME.thmx` に保存します。ここで、`STYLENAME` はスタイルの名前です。
5. Finder に移動し、Word から保存した DOCX ファイルを見つけます。それを複製し、コピーの名前を `FILENAME.zip` に変更し、ダブルクリックして解凍します。
6. 解凍された文書に、styles.xml ファイルを含む「word」フォルダーが表示されます。そのstyles.xmlファイルを上記と同じフォルダーにコピーし、`STYLENAME.xml`という名前を付けます（`STYLENAME`はスタイルの名前です）。 `.thmx` と `.xml` ファイルは、同じベース名を持つ必要があります (拡張子が異なるだけです)。

次回、Marked から DOCX をエクスポートすると、[保存] ダイアログの [スタイル] メニューに新しいスタイルが表示されます。