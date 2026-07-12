<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## フェンスで囲まれたコード ブロック

フェンスで囲まれたコード ブロックは、デフォルトで、組み込まれている両方のプロセッサ (MultiMarkdown とdiscount) で有効になっています。フェンスで囲まれたコード ブロックは、3 つ以上のチルダ (~) またはバッククォート (\`) で区切られます。 3 つ以上の区切り文字を使用できますが、開始区切り文字と終了区切り文字はまったく同じ数の文字である必要があります。

    ~~~~
    一部のコードは pre/code ブロックとしてレンダリングされます
    ~~~~

言語は、最初の行の区切り文字の後に言語タイトル (または短いタイトル) を使用するか、最後の区切り文字の後に中括弧 (先頭のピリオドの有無にかかわらず) を使用して指定できます。たとえば:

    ~~~~~ルビー
    いくつかの Ruby コード
    ~~~~~

次のようにレンダリングされます:

    <pre><code class="ruby">いくつかの Ruby コード</code></pre>


またはバッククォートを使用して:

    `````
    いくつかの Java コード
    `````{.java}

Marked は、Markdown Extra/Python Markdown (フェンスを閉じた後 `{.lang}`) とDiscount (最初のフェンスを閉じた後 `lang`) の両方の言語仕様を検出できます。次の (割引形式) は、上記 (Python マークダウン形式) と同じ結果を作成します。

    `````ジャワ
    いくつかの Java コード
    `````


Marked は、インデントされたフェンスで囲まれたコード ブロックも処理するため、ネストされたリスト内で使用できます。

組み込みの構文強調表示は **256** 言語指定子を認識します (下記の [サポートされている言語](#supported-langages) を参照)。言語が指定されていない場合は、自動的に検出されるため、プレビューには必要ありません。指定された言語文字列は、最終的な HTML の `<code>` タグのクラスとして出力されます。

文書に外部コード ファイルを含める方法については、[マークされた特殊な構文](Special_Syntax.html#includingcode) のセクションを参照してください。

## 構文の強調表示

![自動構文ハイライト][ハイライト]

[highlight]: images/screenshots/mainwindow-feature-code-crop.jpg @2x width=564px height=188px class=center

構文の強調表示は、{% prefspane Style %} で有効にできます。コード ブロックを認識し、言語を検出し、色分けされた出力をプレビューに表示します。利用可能なテーマは複数あり、設定のオプションの下のドロップダウンで選択できます。選択したテーマはすべてのドキュメントに適用されます。

Marked は [highlight.js](https://highlightjs.org/) を使用して、言語を指定できない標準の Markdown 構文を含む、あらゆる種類の埋め込みコードに一貫したカラー コーディングを提供します。 Highlight.js はうまく自動検出します。 Pygments (GitHub スタイル) などのカラーライザーとの間にはレンダリングに若干の違いがありますが、出力は似ています。たとえば、Ruby コードで github.css テーマを使用すると、GitHub で表示されるのとほぼ同じ出力がレンダリングされます。

> *GitHub スタイルシートは、Pygments でレンダリングされたブロックのバックアップ スタイルを提供します。 `<pre>` タグが「highlight」クラスの div 内にある場合、Marked のスタイルではなく、標準の GitHub スタイルを使用して表示されます。コードを外部でレンダリングして HTML を貼り付けることも、`pygmentize` を使用してコードを HTML ファイルにレンダリングし、[`<<(source.html)` 構文](Special_Syntax.html#includingcode)* に含めることもできます。

構文スタイル セレクターの右側にある [言語が指定されている場合のみ] オプションは、フェンスで囲まれたコード ブロックに適用されます。有効にすると、構文の強調表示は、開始フェンスの後の言語指定子を持つコード ブロックにのみ適用されます。

    ```js
    コード
    「」

構文の強調表示は、プレビュー、印刷および PDF エクスポートに表示されます。設定で有効になっており、HTML のエクスポート時にテーマが含まれている場合、Marked で使用される highlight.js ライブラリが HTML 出力に埋め込まれ、エクスポートされた HTML が Marked と同じように表示されるようになります。

### サポートされている言語

マークには、[highlight.js でサポートされている言語](https://highlightjs.readthedocs.io/en/latest/supported-languages.html) リストのすべてのコア言語とサードパーティの文法を含む **highlight.js 11.11.1** が同梱されています。開始フェンスの後に、以下の主言語名 (または JavaScript の場合は `js` などの文書化された別名) を指定します。

ハイライト.js サイトにリストされている 2 つの言語は、Marked のバンドルには含まれていません: **Pine Script** (アップストリーム パッケージは利用不可) と **Supercollider** (highlight.js 11 と互換性なし)。

    1c、4d、GN、abap、abnf、accesslog、actionscript、ada、alan、angelscript、apache、apex、
    applescript、アーケード、arduino、armasm、asciidoc、aspectj、autohotkey、autoit、avrasm、awk、
    axapta、バレリーナ、bash、ベーシック、bbcode、ブレード、bnf、bqn、brainfuck、c、c3、cal、capnproto、
    セイロン、カオス、チャペル、シスコ、クリーン、clojure、clojure-repl、cmake、cobol、coffeescript、
    coq、cos、cpc、cpp、crmsh、クリスタル、csharp、cshtml-razor、csp、css、curl、cypher、d、dafny、
    ダーツ、デルファイ、差分、ジャンゴ、DNS、dockerfile、dos、dsconfig、dts、ダスト、ディラン、ebnf、エリクサー、
    elm、erb、erlang、erlang-repl、excel、extempore、fix、flix、fortran、fsharp、func、gams、
    ガウス、gcode、gdscript、gf、ガーキン、グリマー、glsl、gml、go、golo、gradle、graphql、groovy、
    gsql、haml、ハンドルバー、haskell、haxe、hlsl、hsp、http、hy、inform7、ini、iptables、irpf90、
    isbl、java、javascript、jboss-cli、jolie、json、julia、julia-repl、kotlin、lang、lasso、
    ラテックス、ldif、リーフ、リーン、レス、lisp、livecodeserver、livescript、llvm、lookml、lsl、lua、
    macaulay2、makefile、マークダウン、mathematica、matlab、maxima、mel、mercury、mint、mipsasm、
    mirc、mizar、mkb、mlir、mojolicious、monkey、moonscript、motoko、n1ql、nestedtext、never、
    nginx、nim、nix、node-repl、nsis、oak、objectivec、ocaml、ocl、openscad、oxygen、papyrus、
    parser3、perl、pf、pgsql、php、php-template、プレーンテキスト、ポニー、powershell、処理、
    プロファイル、プロローグ、プロパティ、protobuf、puppet、purebasic、python、python-repl、q、qml、
    qsharp、r、reasonml、rebol、rib、riscript、riscvasm、roboconf、ロボット、routeros、
    rpm スペックファイル、rsl、ruby、ルール言語、rust、rvt スクリプト、sas、scala、スキーム、scilab、scss、
    sfz、シェル、shexc、smari、smalltalk、sml、solidity、spl、sqf、sql、stan、stata、step21、
    構造化テキスト、スタイラス、サブユニット、svelte、swift、taggerscript、tap、tcl、terraform、thrift、
    toit、tp、tsql、twig、typescript、unicorn-rails-log、vala、vba、vbnet、vbscript、
    vbscript-html、verilog、vhdl、vim、wasm、ミソサザイ、x86asm、x86asmatt、xl、xml、xquery、xsharp、
    yaml、yul、zenscript、zephir

### 構文強調表示テーマ

**239** 構文強調表示テーマは、{% prefspane Style %} ドロップダウンで利用できます。テーマは、Marked のバンドルされたスタイルシートから自動的にロードされます。名前は拡張子を除いた CSS ファイル名と一致します (たとえば、`github-dark` は `github-dark.css` をロードします)。

一般的なテーマ:

1c-light、a11y-dark、a11y-light、agate、an-old-hope、androidstudio、arduino-light、arta、
    atom-one-dark、atom-one-dark-reasonable、atom-one-light、codepen-embed、color-brewer、dark、
    デフォルト、ファンデーション、github、github-dark、github-dark-dimmed、googlecode、グレースケール、
    ハイブリッド、アイデア、Intellij-light、ir-black、isbl-editor-dark、isbl-editor-light、kimbie-dark、
    キンビーライト、モノブルー、モノカイ、モノカイサブライム、ナイトフクロウ、nnfx-ダーク、nnfx-ライト、ノルド、
    黒曜石、パンダ-シンタックス-ダーク、パンダ-シンタックス-ライト、パライソ-ダーク、パライソ-ライト、ポジョアクア、
    purebasic、qtcreator-dark、qtcreator-light、rainbow、rose-pine、rose-pine-dawn、
    ローズパインムーン、スクールブック、シェードオブパープル、srcery、スタックオーバーフローダーク、
    stackoverflow-light、サンバースト、tokyo-night-dark、tokyo-night-light、tomorrow-night-blue、
    明日の夜-明るい、vs、vs2015、xcode、xt256

Base16 テーマ (176 のバリアント、それぞれに接頭辞 `base16-` が付きます):

ベース16-3024、ベース16-無関心、ベース16-見習い、ベース16-灰、ベース16-アトリエ-洞窟、
    Base16-アトリエ-洞窟-ライト、ベース16-アトリエ-砂丘、ベース16-アトリエ-砂丘-ライト、
    Base16-アトリエ-河口、base16-アトリエ-河口-ライト、base16-アトリエ-フォレスト、
    base16-アトリエ-フォレスト-ライト、base16-アトリエ-ヒース、base16-アトリエ-ヒース-ライト、
    ベース16-アトリエ-レイクサイド、ベース16-アトリエ-レイクサイド-ライト、ベース16-アトリエ-プラトー、
    Base16-アトリエ-プラトー-ライト、Base16-アトリエ-サバンナ、Base16-アトリエ-サバンナ-ライト、
    ベース16-アトリエ-シーサイド、ベース16-アトリエ-シーサイド-ライト、ベース16-アトリエ-サルファープール、
    ベース16-アトリエ-サルファープール-ライト、ベース16-アトラス、ベース16-ベスピン、ベース16-ブラック-メタル、
    Base16-ブラックメタル-バーザリー、ベース16-ブラックメタル-バーザム、ベース16-ブラックメタル-ダーク-フューネラル、
    ベース16-ブラックメタル-ゴルゴロス、ベース16-ブラックメタル-イモータル、ベース16-ブラックメタル-ホールド、
    Base16-ブラックメタル-マルドゥク、BASE16-ブラックメタル-メイヘム、BASE16-ブラックメタル-ナイル、
    ベース16-ブラックメタル-ヴェノム、ベース16-ブリューワー、ベース16-ブライト、ベース16-ブログラマー、
    Base16-brush-trees、base16-brush-trees-dark、base16-チョーク、base16-circus、
    Base16-classic-dark、base16-classic-light、base16-codeschool、base16-colors、
    base16-カップケーキ、base16-クパチーノ、base16-ダンチン、base16-ダーキュラ、base16-ダークバイオレット、
    Base16-darkmoss、base16-darktooth、base16-decaf、base16-default-dark、base16-default-light、
    ベース16-ダーティシー、ベース16-ドラキュラ、ベース16-エッジ-ダーク、ベース16-エッジ-ライト、ベース16-80、
    Base16-embers、base16-equilibrium-dark、base16-equilibrium-gray-dark、
    base16-平衡-グレーライト、base16-平衡-ライト、base16-エスプレッソ、base16-eva、
    Base16-eva-dim、base16-フラット、base16-framer、base16-フルーツソーダ、base16-ギガボルト、
    Base16-github、base16-google-dark、base16-google-light、base16-grayscale-dark、
    base16-グレースケール-ライト、base16-グリーンスクリーン、base16-gruvbox-dark-hard、
    Base16-gruvbox-dark-medium、base16-gruvbox-dark-pale、base16-gruvbox-dark-soft、
    Base16-gruvbox-light-hard、base16-gruvbox-light-medium、base16-gruvbox-light-soft、
    ベース 16-ハードコア、ベース 16-高調波 16-ダーク、ベース 16-高調波 16-ライト、ベース 16-ヒーッチ-ダーク、
    Base16-heetch-light、base16-helios、base16-石けり遊び、base16-horizon-dark、
    Base16-horizon-light、base16-humanoid-dark、base16-humanoid-light、base16-ia-dark、
    Base16-ia-ライト、base16-icy-dark、base16-ir-black、base16-同位体、base16-kimber、
    ベース16-ロンドン-チューブ、ベース16-マッキントッシュ、ベース16-マラケシュ、ベース16-マテリアル、ベース16-マテリアル、
    ベース16-マテリアル-暗い、ベース16-マテリアル-明るい、ベース16-マテリアル-淡い、
    Base16-material-vivid、base16-mellow-purple、base16-mexico-light、base16-mocha、
    Base16-monokai、base16-nebula、base16-nord、base16-nova、base16-ocean、base16-oceanicnext、
    Base16-one-light、base16-onedark、base16-outrun-dark、base16-papercolor-dark、
    Base16-papercolor-light、base16-paraiso、base16-pasque、base16-phd、base16-pico、
    Base16-pop、base16-porple、base16-クオリア、base16-railscasts、base16-rebecca、
    Base16-ros-pine、base16-ros-pine-dawn、base16-ros-pine-moon、base16-sagelight、
    ベース16-サンドキャッスル、ベース16-セットウイ、ベース16-シェイプシフター、ベース16-シルク-ダーク、
    base16-シルクライト、base16-snazzy、base16-ソーラーフレア、base16-ソーラーフレアライト、
    Base16-solarized-dark、base16-solarized-light、base16-spacemacs、base16-サマーキャンプ、
    Base16-サマーフルーツ-ダーク、ベース16-サマーフルーツ-ライト、ベース16-シンセ-ミッドナイトターミナル-ダーク、
    Base16-シンセ-ミッドナイト-ターミナル-ライト、ベース16-タンゴ、ベース16-テンダー、ベース16-明日、
    base16-明日の夜、base16-トワイライト、base16-unikitty-dark、base16-unikitty-light、
    Base16-vulcan、base16-windows-10、base16-windows-10-light、base16-windows-95、
    Base16-windows-95-light、base16-windows-ハイコントラスト、base16-windows-ハイコントラスト-ライト、
    Base16-windows-nt、base16-windows-nt-light、base16-woodland、base16-xcode-dusk、
    Base16-ゼンバーン

## GitHub の改行

マークを付けると、段落内の改行を保持できます。段落内の改行を保持するには、{% prefspane Processor %} を選択してボックスにチェックを入れるだけです。

## GitHub チェックボックス

次の形式で項目をリストします。

    - [ ] 未完了のタスク
    - [x] 完了したタスク

レンダリングされたチェックボックス項目としてプレビューに表示されます。これらを操作することはできませんが、その状態はソース ドキュメント内の変更を反映します。

## コードブロックのラッピング

{% prefspane Style %} の [レイアウトとタイポグラフィ] の下に、[テーマでコード ブロック内でテキストを折り返すことを許可する] オプションがあります。これを無効にすると、現在のプレビュー スタイルに関係なく、すべてのコード ブロックが折り返すのではなく、水平方向のオーバーフローを強制的にスクロールします。