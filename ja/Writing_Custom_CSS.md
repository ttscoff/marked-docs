# <%= @title %>

Markedにはビルトインのスタイルエディタが搭載されており、カスタムCSSファイルを適用することもできます。

エディタを使って美しいスタイルを作成することも、危険な目に遭わない程度にCSSの知識があれば、Markedの見た目を好きなように変えることもできます。

## はじめに [getting-started]

開発者およびユーザーによって作成されたカスタムスタイルのギャラリーが[markedapp.com/styles](https://markedapp.com/styles/)にあります。このギャラリーでは、Marked上で直接スタイルをプレビューしてインストールできます。インストール済みのスタイルはFinderで表示し、内容を確認・変更することができます。ギャラリーは内蔵ビューアで{% appmenu Style, Generate a Custom Style %}を使って開くか、スタイルマネージャで編集可能なスタイルの横にある鉛筆（編集）アイコンをクリックして開くことができます。ビルトインスタイルを編集したい場合は、まずマネージャ内で複製する必要があります。

サンプルを掲載したGitHub上の[カスタムスタイル用リポジトリ](https://github.com/ttscoff/MarkedCustomStyles)もあります。自由に閲覧・利用し、貢献していただいて構いません。ベーステーマを元にしたテーマを配布する場合は、ぜひコントリビューターとしてクレジットに自分の名前を加えてください。

MarkedのカスタムCSSファイル機能を使えば、プレビューのカスタマイズは思いのままです。Safariで動作するCSS3のオプションはすべてMarkedでも動作します。Markedのデフォルトのマークダウンファイルでは、扱う必要のあるHTML要素はごくわずかです。すべてのコンテンツはidが「wrapper」のdiv内にあり、それ以外はすべてドキュメントのマークアップによって決まります。

個人用にデザインするのであれば、ルールは一切ありません。カスタムCSSセレクタの下にあるチェックボックスでCSSトラッキングをオンにすれば、カスタムCSSを編集して保存するたびにプレビューが更新されます。

**[スケルトンテーマ](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css)を使うと簡単に始められます。**

作成したCSSを共有する予定がある場合、いくつか押さえておくべきポイントがあります。まず、スタイルを適用する必要のあるbodyクラスがいくつか存在します。

## Bodyクラス [body-classes]

共有するMarkedのCSSには、以下のスタイルを必ず含める必要があります。これらのbodyクラスを使うことで、さまざまな環境設定オプションに応じてセレクタをターゲットにし、変更を加えることができます。

### 反転（Inverted） [inverted]

ユーザーが{% appmenu Preview, Dark Mode %}を選択すると、bodyタグに「inverted」というクラスが追加されます。これを使って、ハイコントラストの「ライト・オン・ダーク」スタイルをターゲットにできます。

反転スタイルはプレビューのみに適用し、印刷には適用したくないはずなので、メディアクエリ（@media screen）で制限してください。以下のコードは汎用的なもので、多くの場合そのままスタイルシートに組み込むだけで互換性が保てますが、自由に調整してください。

```css
@media screen {
	.inverted, .inverted #wrapper { background:#111 !important }
	.inverted p,.inverted td,.inverted li,.inverted h1,.inverted h2,
	.inverted h3,.inverted h4, .inverted h5, .inverted h6, .inverted pre,
	.inverted code,.inverted th {
		color:#eee !important;
	}
	.inverted a { color:#fff;text-decoration:underline }
	#wrapper {
		background: transparent;
		padding:20px;
	}
}
```

### 詩（Poetry） [poetry]

ユーザーは、タブインデントされたテキストを「詩」として扱うか「コード」として扱うかを選択できます。両者の違いは、詩モードが選択されている場合、pre/codeブロックがより……詩的に、スタイリングされる点だけです。「poetry」クラスがbodyタグに適用されます。

フォーマットは好きなだけ凝ってもらって構いませんが、基本的なスニペットは以下の通りです。

```css
.poetry pre code {
	font-family:Georgia, Garamond, serif;
	font-style:italic;
	font-size:110% !important;
	line-height:1.6em;
	display:block;
	margin-left:1em;
}
```

## 特殊なケース [special-cases]

テーブル、Figure/Figcaption、そして`a.footnote`と`div.footnotes>a`という特殊なケースについても考慮する必要があります。これらの扱い方に決まったルールはありませんが、デフォルトスタイルを参照して、Markedがどのようなcssルールを必要としているか把握してください。

すべてのデフォルトスタイルに共通する標準的なテーブルスタイリングでは、交互の行に透明度を設定することで、どんな背景色にもソフトになじむようにしています。これらのスタイルをコピーしても、独自の方法でスタイリングしても構いませんが、必ずスタイルを設定してください。figureとfigcaptionについても同様です。alt textを付けた画像をドキュメントに追加して、マークアップがどのように出力されるかを確認し、適切にスタイリングしてください。

ドキュメントに含まれる脚注は、コンテンツ内にリンク（a.footnote）としてレンダリングされ、末尾に参照テキストを含むdiv（div.footnotes）が生成されます。こちらもデフォルトスタイルを参考にしてください。脚注参照番号を含む行の行の高さが変わってしまわないようにするには、以下のような指定を含めてください。

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

戻り矢印を同じ行に保つには、以下を含めてください。

```css
.footnotes p {display:inline}
```

また、すべての画像がページの幅内に収まるよう、一般的なルールを設定しておくのもよいでしょう。例えば以下のようにします。

```css
#wrapper img { max-width: 100% }
```

テーマに追加のパディングや固定幅がある場合は、max-widthを合わせて調整してください。

## 印刷スタイル [printstyles]

背景色、固定スクロール、プレビュー専用UIを除去する印刷スタイルは必ず含めるようにしてください。Markedでは、印刷とPDF出力をターゲットにする方法が2つ用意されています。

### `@media print` [media-print]

Markedから印刷する場合や、PDFエクスポートが印刷用メディアを使用する場合は、標準的なCSSの印刷ルールが適用されます。

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### `.mkprinting`クラス [the-mkprinting-class]

Markedがドキュメントを**PDFエクスポート**または**印刷/PDFプレビュー**（{% kbd cmd P %}）用に準備する際、`<body>`タグに`mkprinting`というクラスが追加されます（`bandw`や`breakAfterTOC`といったエクスポート用クラス、およびお使いのスタイルの`mkstyle--*`クラスと並んで付与されます）。Markedのビルトインテーマでは、印刷固有のルールの大半に`@media print`だけに頼るのではなく、このクラスを使用しています。

PDFエクスポートでは、非表示のレンダリング用WebViewが**screen**メディアで読み込まれることがよくあります（特にカスタムスタイルや[Fountain](Fountain_for_Screenwriters.html)ドキュメントの場合）。そのため、スタイルシート内の`@media print`ブロックがPDF出力に**適用されない**場合があります。`.mkprinting`を前置したルールは、通常のクラスセレクタでありメディアクエリではないため、エクスポート時にも常に適用されます。

```css
/* Hide preview UI during print/PDF */
.mkprinting #generated-toc,
.mkprinting #criticnav,
.mkprinting .mkscrollmeter {
  display: none !important;
}

/* Print/PDF typography */
.mkprinting #wrapper {
  background: white;
  padding: 0;
}

.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

ブラウザでの印刷とMarkedのPDFエクスポートの**両方**で機能させたいスタイルについては、重要なルールを複製するか、セレクタを組み合わせてください。

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

**カスタムスタイル vs 追加CSS。** カスタムスタイルのスタイルシートでは、上記のように`.mkprinting #wrapper …`と記述します。一方、**追加CSS**フィールドでは、Markedが注入前にセレクタを書き換えるため、代わりにbody修飾形式を使用してください。

```css
body.mkprinting #wrapper p {
  font-size: 10pt;
  line-height: 1.4;
}
```

書き換えの仕組みと、なぜ`.mkprinting #wrapper …`単体ではそこでマッチしないのかについては、[追加CSSの設定](#additional-css-settings)を参照してください。

カスタムの印刷用CSSをデバッグする際は、印刷/PDFプレビューを開くかPDFにエクスポートしてから、[SafariのWeb Inspector](#webkitinspector)を使ってドキュメントを検証してください。印刷レイアウトが有効な間、`<body>`には`mkprinting`クラスが付与されます。

印刷時のリンク非表示はメインテーマの外側で処理されるため、ユーザーは印刷時にリンクのハイライトや下線を非表示にするかどうかを選択できます。テキストに対するベーススタイルさえ設定されていれば、これについて気にする必要はありません。

というわけで、あとはご自由に。ブログテーマを移植したり、PDFドキュメント用の強力な印刷スタイルを作ったり、自分が書く文章に最適なプレビューを作り込んだりしてください。何か素晴らしいものができたら、ぜひ[コミュニティと共有](https://markedapp.com/styleshare/)してください。

## 追加CSSの設定 [additional-css-settings]

{% prefspane Style %}内で、**追加CSS**を編集できます。これらのルールは、**読み込まれているテーマに追加される**形になります。これは意図的な部分的オーバーレイであり、完全なテーマではありません。このフィールドに完全なスタイルシートを貼り付けたり、同じ部分的なシートを[スタイルマネージャ](Custom_Styles.html)を通じてテーマであるかのようにインポートしたりすると、そのシートがカバーしていない部分はスタイルが適用されないままになります。

### セレクタの書き換え [additional-css-selector-rewriting]

Markedは、追加CSSのセレクタを注入前（`body.mk-has-additional-css …`として）に書き換え、ルールがプレビューにスコープされた状態を保つようにします。

- すでに`body`または`#wrapper`で始まるセレクタ部分には`body.mk-has-additional-css`というプレフィックスが付与され、bodyクラスはネストされるのではなくマージされます。
- それ以外のセレクタ部分は`body.mk-has-additional-css #wrapper …`の配下にスコープされます。
- Markedが`<body>`に設定する先頭のbodyクラス（`.mkprinting`、`.inverted`、`.poetry`、`.bandw`、`.breakAfterTOC`、`.mkstyle--*`を含む）は`body`と同様に扱われ、`#wrapper`の下にネストされるのではなく、bodyセレクタにマージされます。

| 追加CSSに入力した内容 | 結果 |
| :-- | :-- |
| `#wrapper h2` | マッチする（正しくスコープされる） |
| `body.mkprinting #wrapper p` | 印刷/PDF時にマッチする |
| `.mkprinting #wrapper p` | マッチ**しない**（ネストされた`#wrapper`が必要になるため） |
| `:root { --x: 1; }` | マッチ**しない**（カスタムプロパティには`body`または`#wrapper`を推奨） |

このフィールドで印刷用ルールを記述する場合は、`body.mkprinting #wrapper …`を使うことをお勧めします。カスタムスタイルファイル内であれば、同じ見た目の意図をより短い`.mkprinting #wrapper …`形式で実現できます。

追加CSSには**サイズ制限もCSSの妥当性チェックもありません**。Markedは入力された内容をそのまま保存・注入します。無効なCSSはプレビューに単に影響を与えないだけです。

### HTMLおよびその他のエクスポート [additional-css-exports]

追加CSSは、ライブプレビュー、印刷/PDFプレビュー、PDFエクスポート、そしてスタイルが含まれる場合の**HTMLエクスポート**に適用されます。エクスポートされた`<body>`には`mk-has-additional-css`クラスが付与されるため、書き換えられたセレクタがマッチします。DOCX、ODT、EPUBは独自のスタイリング経路を使用しており、追加CSSは同じようには適用されません。

[高い詳細度](#overridingspecificity)、印刷用・画面用の`@media`クエリ、そして（このフィールドでの）`body.mkprinting`セレクタや（カスタムスタイルでの）`.mkprinting`セレクタを活用することで、多少のCSS知識があれば、ほぼあらゆるスタイリングの側面をコントロールできます。

## WebKit Inspector [webkitinspector]

SafariのWeb Inspectorは、Markedが実際に生成しているHTMLとCSSを正確に確認し、カスタムスタイルをライブで試すのに最も手軽な方法です。

### SafariでDevelopメニューを有効にする [enabling-the-develop-menu-in-safari]

1. Safariを開き、{% appmenu Safari, Settings… %}を選択します。
2. **詳細**タブを選択します。
3. **Webデベロッパ用の機能を表示**（macOSの古いバージョンでは**メニューバーに"develop"メニューを表示**）を有効にします。

有効にすると、Safariのメニューバーに**Develop**メニューが表示されるようになります。

![Markedのドキュメントが表示されたSafariのDevelopメニュー][develop-menu]

### Markedドキュメントの検証 [inspecting-a-marked-document]

1. Markedでプレビューウィンドウを開いた状態で、Safariに切り替えます。
2. メニューバーから **Develop → _\<お使いのMacの名前\>_ → Marked → _\<ドキュメントのタイトル\>_** を選択します。
3. Safariが、選択したMarkedのプレビューに接続されたWeb Inspectorウィンドウを開きます。

ここからできることは以下の通りです。

- **Elements**タブを使って、`#wrapper`div内のDOMを検証し、どのCSSルールが適用されているかを確認する。
- DOMツリー内の要素にマウスオーバーすると、Markedのウィンドウ内で該当要素がハイライトされる。
- **Styles**サイドバーを使ってルールをライブで調整し、うまくいったスニペットをカスタムスタイルや**追加CSS**にコピーして戻す。
    - Elementsタブ内でCSSを編集した後は、Changesタブを選択すると編集内容の概要を確認できます

	![変更内容][css-changes]
- **Console**タブを使って、ライブプレビューに対してJavaScriptを実行する。このコンソールでは、[Marked JavaScript API](https://markedapp.com/help/jsapi/)がフルに利用できます。
- ドキュメントが読み込むリソースをデバッグする際は、**Network**タブなど他のタブも活用する。

![Safari Web Inspectorを使ったMarkedプレビューの検証][inspecting]

## カスタムCSSの共有 [sharing-custom-css]

{% appmenu Style, Share a Custom Style %}を使って、Webブラウザで共有アプリを開きます。ドロップゾーンにCSSをドラッグする（またはクリックしてディスクから選択する）と、カスタムスタイル用のCSSをアップロードできます。

共有されたスタイルは、ギャラリーに表示される前に開発者による承認が必要なため、すぐには結果が反映されません。

## その他のヒント [other-tips]

### 詳細度をオーバーライドする [overridingspecificity]

Markedのプレビュー内では、現在のスタイルのファイル名に基づいたbodyクラスが追加されます。プレビューが「Swiss」に設定されている場合、`<body>`タグには`mkstyle--swiss`というクラスが付与されます。カスタムCSSがMyCustom.cssという名前であれば、そのbodyクラスは`mkstyle--mycustom`になります。これをベーススタイルで定義されているルールより前に使うことで、それらを上書きできます。ルールに絶対的な詳細度を持たせたい場合は、コンテナdivの#wrapper IDも併用してください。

	.mkstyle--mycustom #wrapper p+p { ... }

### 目次のスタイリング [table-of-contents-styling]

`<!--toc-->`トークンを使って[目次を挿入](Special_Syntax.html#tableofcontents)している場合、カスタムスタイルで「#wrapper」を使って詳細度を上げることで、目次のレベルインジケーターの設定を上書きできます。

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

こうすることで、カスタムスタイルが有効な間、目次内のすべてのリスト項目が、環境設定で定義されていたものではなく、四角い箇条書き記号を使うようになります。

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px
