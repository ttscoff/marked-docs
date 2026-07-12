<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked にはスタイル エディターが組み込まれており、カスタム CSS ファイルを適用できます。

エディターを使用して美しいスタイルを作成することも、CSS が危険であることを十分に知っている場合は、Marked の外観を好きなように変更することもできます。

## はじめに

開発者とユーザーによって作成されたカスタム スタイルのギャラリーが [markedapp.com/styles](https://markedapp.com/styles/) にあります。ギャラリーを使用すると、Marked でスタイルを直接プレビューしてインストールできます。インストールされているスタイルはすべて、調査および変更のために Finder で表示できます。ギャラリーは、{% appmenu Style, Generate a Custom Style %} の内部ビューアを使用して開くか、スタイル マネージャーで編集可能なスタイルの横にある鉛筆 (編集) アイコンをクリックします。組み込みスタイルを編集したい場合は、まずマネージャーでそれを複製する必要があります。

GitHub には [カスタム スタイルのリポジトリ](https://github.com/ttscoff/MarkedCustomStyles) と例もあります。自由に閲覧、使用、投稿してください。基本テーマのいずれかに基づいてテーマを配布する場合は、貢献者としてご自身をクレジットに自由に追加してください。

Marked ではカスタム CSS ファイルを使用できるため、プレビューをカスタマイズする際に限界はありません。 Safari で機能するすべての CSS3 オプションは、Marked でも機能します。 Marked のデフォルトの Markdown ファイルでは、処理する必要がある HTML 要素はわずかです。すべてのコンテンツは「wrapper」という ID を持つ div 内にあり、それ以外はすべてドキュメントのマークアップによって決まります。

個人使用を目的としたデザインの場合、ルールはありません。カスタム CSS セレクターの下にあるチェックボックスを使用して CSS トラッキングをオンにすると、カスタム CSS を編集して保存すると、プレビューが更新されます。

**開始するには [スケルトン テーマが利用可能](https://github.com/ttscoff/MarkedCustomStyles/blob/master/Custom.css) です。**

CSS 作成物を共有する予定がある場合は、いくつかの点をカバーする必要があります。まず、スタイルを適用する必要がある本文クラスがいくつかあります。

## ボディクラス

共有するには、次のスタイルをマークされた CSS に含める必要があります。本体クラスを使用すると、さまざまな設定オプションで任意のセレクターをターゲットにして変更できます。

### 反転

 ユーザーが{% appmenu Preview, Dark Mode %}を選択すると、bodyタグに「inverted」のクラスが追加されます。これを使用して、ハイコントラスト、明るい、暗いスタイルをターゲットにすることができます。

反転スタイルは印刷ではなくプレビューにのみ適用したいので、メディア クエリ (@media screen) を使用して制限します。以下のコードはかなり汎用性があり、ほとんどの場合、互換性のためにスタイルシートにドロップするだけで済みますが、自由に調整してください。

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

### 詩

ユーザーは、タブでインデントされたテキストが詩であるかコードであるかを選択できます。唯一の違いは、詩モードが選択されている場合、プリ/コード ブロックがより詩的にスタイル設定されることです。 bodyタグには「poetry」クラスが適用されます。

書式設定を自由に創造的にしてください。ただし、基本的なスニペットは次のとおりです。

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

## 特殊なケース

表、図/図キャプション、および `a.footnote` と `div.footnotes>a` の特殊なケースも考慮する必要があります。それらの処理方法について決まったルールはありませんが、デフォルトのスタイルを見て、Marked にどのような CSS ルールが必要かを理解してください。

すべてのデフォルト スタイルにわたる標準のテーブル スタイルでは、交互の行に透明度を使用して、背景と柔らかくブレンドします。これらのスタイルをコピーすることも、独自のルートを進むこともできますが、必ずスタイルを設定したことを確認してください。図と図のキャプションも同様です。代替テキストを含む画像をドキュメントに追加して、マークアップがどのように表示され、適切にスタイル設定されるかを確認します。

文書に含まれる脚注は、コンテンツ内のリンク (a.footnote) と、参照されたテキストを含む末尾の div (div.footnotes) をレンダリングします。繰り返しになりますが、デフォルトのスタイルを参照してください。脚注参照番号を含む行の行の高さを変更しないようにするには、必ず次のような内容を含めてください。

```css
sup,sub,a.footnote {
	font-size: 1.4ex;
	height: 0;
	line-height: 1;
	vertical-align: super;
	position: relative;
}
```

戻る矢印を同じ行に保つには、以下を含めます。

```css
.footnotes p {display:inline}
```

すべての画像をページの幅内に収めるという一般的なルールを含めることもお勧めします。次のようなもの:

```css
#wrapper img { max-width: 100% }
```

テーマに追加のパディングまたは固定幅がある場合は、それに合わせて最大幅を変更します。

## 印刷スタイル

背景色を削除する印刷スタイル、固定スクロール、プレビュー専用 UI を必ず含めてください。マークを付けると、印刷出力と PDF 出力をターゲットにする 2 つの方法が提供されます。

### `@media print`

標準 CSS 印刷ルールは、マーク付きから印刷する場合、または PDF エクスポートで印刷メディアを使用する場合に適用されます。

```css
@media print {
  .inverted, .inverted #wrapper { background: white !important; }
  #wrapper { padding: 0; }
}
```

### `.mkprinting` クラス

Marked が **PDF エクスポート** または **印刷/PDF プレビュー** ({% kbd cmd P %}) 用にドキュメントを準備すると、クラス `mkprinting` が `<body>` タグに追加されます (`bandw`、`breakAfterTOC` などのエクスポート クラス、およびスタイルの `mkstyle--*` クラスとともに)。 Marked の組み込みテーマは、`@media print` のみに依存するのではなく、ほとんどの印刷固有のルールにこのクラスを使用します。

PDF エクスポートでは、**画面** メディアを使用して非表示のレンダリング WebView が読み込まれることが多いため (特にカスタム スタイルや [Fountain](Fountain_for_Screenwriters.html) ドキュメントの場合)、スタイルシート内の `@media print` ブロックは PDF 出力に**適用されない**場合があります。 `.mkprinting` というプレフィックスが付いたルールは、メディア クエリではなく通常のクラス セレクターであるため、エクスポート中に常に適用されます。

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

ブラウザ印刷とマーク付き PDF エクスポートの**両方**で機能する必要があるスタイルの場合は、重要なルールを複製するか、セレクターを結合します。

```css
@media print {
  #wrapper img { max-width: 100%; }
}

.mkprinting #wrapper img {
  max-width: 100%;
}
```

カスタム印刷 CSS をデバッグする場合は、印刷/PDF プレビューを開くか PDF にエクスポートし、[Safari の Web インスペクター](#webkitinspector) を使用してドキュメントを検査します。印刷レイアウトがアクティブな間、`<body>` には `mkprinting` クラスが含まれます。

印刷時のリンクの非表示はメインテーマの外で処理されるため、ユーザーは印刷時にリンクのハイライトと下線を非表示にすることを選択できます。テキストの基本スタイルが設定されている限り、これについて心配する必要はありません。

それでは、やってみましょう。ブログのテーマを変換したり、PDF ドキュメントの素晴らしい印刷スタイルを作成したり、執筆スタイルに最適なプレビューを作成したりできます。素晴らしいものを作成したら、[コミュニティと共有](https://markedapp.com/styleshare/)。

## 追加の CSS 設定

{% prefspane Style %}では、追加のCSSを編集できます。これらのスタイルは読み込まれたテーマに追加され、すべてのテーマに共通の変更を加えるために使用できます。

[高度な特異性](#overridingspecity)、印刷および画面用の `@media` クエリ、PDF エクスポート用の `.mkprinting` セレクターを使用すると、CSS の知識があればほぼすべてのスタイル設定を制御できます。

## WebKit インスペクター

Safari の Web インスペクターは、マークされた HTML と CSS が生成しているものを正確に確認し、カスタム スタイルをライブで試す最も簡単な方法です。

### Safari で [開発] メニューを有効にする

1. Safari を開き、{% appmenu Safari, Settings… %} を選択します。
2. [**詳細**] タブを選択します。
3. **Web 開発者向けの機能を表示** (または、古い macOS バージョンでは **メニュー バーに開発メニューを表示**) を有効にします。

有効にすると、**開発** メニューが Safari のメニュー バーに表示されます。

![マークされたドキュメントを表示する Safari 開発メニュー][開発メニュー]

### マークされたドキュメントの検査

1. Marked でプレビュー ウィンドウが開いた状態で、Safari に切り替えます。
2. メニュー バーから、**開発 → _\<Mac 名\>_ → マーク → _\<ドキュメント タイトル\>_** を選択します。
3. Safari は、選択したマーク付きプレビューに関連付けられた Web インスペクター ウィンドウを開きます。

ここから次のことができます。

- **要素** タブを使用して、`#wrapper` div 内の DOM を検査し、どの CSS ルールが適用されているかを確認します。
- DOM ツリー内の要素にカーソルを合わせると、マークされたウィンドウで要素が強調表示されます。
- **スタイル** サイドバーを使用してルールをライブで調整し、作業中のスニペットをカスタム スタイルまたは **追加の CSS** にコピーして戻します。
    - [要素] タブで CSS を編集した後、[変更] タブを選択すると、編集内容の概要を取得できます。

	![変更][css-変更]
- [**コンソール**] タブを使用して、ライブ プレビューに対して JavaScript を実行します。完全な [Marked JavaScript API](https://markedapp.com/help/jsapi/) は、このコンソールで利用できます。
- ドキュメントによって読み込まれたリソースをデバッグするときに、[**ネットワーク**] などの他のタブを探索します。

![Safari Web Inspector でマークされたプレビューを検査する][検査]

## カスタム CSS の共有

{% appmenu Style, Share a Custom Style %} を使用して、Web ブラウザで共有アプリを開きます。 CSS をドロップ ゾーンにドラッグし (またはクリックしてディスクから選択し)、カスタム スタイルの CSS をアップロードします。

共有スタイルはギャラリーに表示される前に開発者によって承認される必要があるため、すぐには結果が表示されません。

## その他のヒント

### 特異性のオーバーライド

マーク付きプレビュー内に、現在のスタイルのファイル名に基づいた本文クラスが追加されます。プレビューが「スイス」に設定されている場合、`<body>` タグに `mkstyle--swiss` というクラスが存在します。カスタム CSS の名前が MyCustom.css の場合、本文クラスは `mkstyle--mycustom` になります。これを基本スタイルで定義されたルールの前に使用して、ルールをオーバーライドできます。ルールの絶対的な特異性を取得するには、コンテナ div の #wrapper ID も使用します。

	.mkstyle--mycustom #wrapper p+p { ... }

### 目次のスタイル

`<!--toc-->` トークンを使用して [目次を挿入](Special_Syntax.html#tableofcontents) を使用する場合、「#wrapper」を使用してカスタム スタイルの目次レベル インジケーターの設定をオーバーライドして、具体性を高めることができます。

```css
#wrapper #mkreplaced-toc li {
 list-style-type: square;
}
```

これにより、カスタム スタイルがアクティブな場合、目次内のすべてのリスト項目で、設定で定義されたものではなく四角形の箇条書きが使用されます。

[develop-menu]: images/develop-menu-600.jpg @2x width=600px height=273px "Safari Develop menu" class=center
[inspecting]: images/inspecting-600.jpg @2x width=600px height=367px "Inspecting a Marked document in Safari" class=center

[css-changes]: images/css-changes.jpg @2x width=322px height=207px