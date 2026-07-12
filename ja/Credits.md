<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked は、オープンソース コミュニティからの多大な支援を受けて構築されています。このページには、Marked 内に同梱されるサードパーティのコードがリストされています。 Markdown プロセッサの完全なライセンス テキストは、[Markdown について](MultiMarkdown_Information.html) のリンク先ページで入手できます。

## Markdown プロセッサと変換

|コンポーネント |著者 |ライセンス |用途 |
| --- | --- | --- | --- |
| [マルチマークダウン](MultiMarkdown_License.html) | [ジョン・グルーバー](http://daringfireball.net/)、[フレッチャー・ペニー](http://fletcherpenney.net/) | BSD スタイル |デフォルトの Markdown プロセッサ |
| [割引](Discount_License.html) | [デビッド・ローレン・パーソンズ](http://www.pell.portland.or.us/~orc/) | BSD |代替の Markdown プロセッサ (GHMarkdownParser 経由) |
| [GHMarkdownParser](Discount_License.html) | [オリバー・レタラー](https://github.com/OliverLetterer) |マサチューセッツ工科大学 | Objective-C ラッパーの割引 |
| [cmark-gfm](CommonMark_License.html) | [ジョン・マクファーレン](https://github.com/jgm) と寄稿者 | BSD-2 条項 | GitHub フレーバード マークダウン解析 |
| [クラムダウン](Kramdown_License.html) | [カールステン・ボルマン](https://github.com/gettalong) |マサチューセッツ工科大学 | Kramdown プロセッサ オプション (Ruby バンドル) |
| [pdf22md](PDF22MD_License.html) | [アダム・トワードック](https://github.com/twardoch) |マサチューセッツ工科大学 | PDF から Markdown へのインポート |

## ネイティブ コードとフレームワーク

|コンポーネント |著者 |ライセンス |用途 |
| --- | --- | --- | --- |
| [噴水](https://fountain.io/) |ニマ・ユセフィとジョン・オーガスト |マサチューセッツ工科大学 |ファウンテンの脚本解析 |
| [ココアランバージャック](https://github.com/CocoaLumberjack/CocoaLumberjack) | Deusty, LLC | BSD-3 条項 |デバッグログ |
| [スパークル](https://sparkle-project.org/) |スパークルプロジェクト |マサチューセッツ工科大学 |自動更新 (直接ダウンロード ビルド) |
| [YACYAML](https://github.com/yaml/YACYAML) |ジェームズ・モンゴメリーBSD-2 条項 | YAML メタデータの解析 |
| [リビアムル](https://github.com/yaml/libyaml) |キリル・シモノフ |マサチューセッツ工科大学 | YAML ライブラリ (YACYAML で使用) |
| [CHCSVParser](https://github.com/davedelong/CHCSVParser) |デイブ・デロング |マサチューセッツ工科大学 | CSV テーブルのインポート |
| [RNTextStatistics](https://github.com/rnystrom/RNTextStatistics) |ライアン・ニストロムマサチューセッツ工科大学 |読みやすさとテキストの統計 |
| [RegexKitLite](http://regexkit.sourceforge.net/) |ジョン・エンゲルハート | BSD |正規表現ユーティリティ |
| [正規表現カテゴリ](https://github.com/bendytree/Objective-C-RegEx-Categories) |ジョシュ・ライト |マサチューセッツ工科大学 |正規表現のカテゴリ |
| [AppSandboxファイルアクセス](https://github.com/leighmcculloch/AppSandboxFileAccess) |リー・マカロック | BSD-2 条項 |サンドボックス ファイル アクセス ヘルパー |
| [VDKキュー](https://github.com/bdkjones/VDKQueue) |ブライアン・D・K・ジョーンズ |カスタム許容 |ファイル変更通知 |
| [ミニジップ](https://www.winimage.com/zLibDll/minizip.html) |ジル・ヴォラン情報ZIP | zlib スタイル | ZIP アーカイブの処理 |
| [JNWScrollView](https://github.com/jonathonjohnson/JNWScrollView) |バターキット |マサチューセッツ工科大学 |スクロールビューユーティリティ |
| [DBPrefsWindowController](http://www.mere-mortal-software.com/blog/) |デイブ・バトン | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) |環境設定ウィンドウのツールバー |
| [NTYCSVテーブル](https://github.com/naotokano/NTYCSVTable) |金子直人 |プロジェクトを参照 | CSV テーブルのレンダリング |
| [DJProgressHUD](https://github.com/DanielJackson-DJ/DJProgressHUD) |ダニエル・ジャクソン |プロジェクトを参照 |進行状況インジケータ |
| [IAPManager](https://github.com/mruegenberg/IAPManager) |マルセル・リューゲンバーグ |プロジェクトを参照 |アプリ内購入ヘルパー (レガシー) |

## JavaScript をプレビューする

これらのライブラリは、Marked のプレビュー バンドル (`marked.min.js` および関連リソース) に連結されています。

|コンポーネント |著者 |ライセンス |用途 |
| --- | --- | --- | --- |
| [jQuery](https://jquery.com/) | jQuery財団 |マサチューセッツ工科大学 | DOM およびイベント ユーティリティ |
| [Hammer.js](https://hammerjs.github.io/) |ジョリック・タンゲルダー |マサチューセッツ工科大学 |タッチとジェスチャーの処理 |
| [ハイライト.js](https://highlightjs.org/) | Josh Goebel と寄稿者 | BSD-3 条項 |構文の強調表示 |
| [MathJax](MathJax.html) | MathJax コンソーシアム | Apache-2.0 |数学レンダリング (ローカルバンドル) |
| [KaTeX](https://katex.org/) |カーンアカデミーと貢献者 |マサチューセッツ工科大学 |数式レンダリング (KaTeX オプション) |
| [人魚](https://mermaid.js.org/) |人魚の寄稿者 |マサチューセッツ工科大学 |ダイアグラムのレンダリング |
| [モダンズル](https://modernizr.com/) |ファルク・エイツ、ポール・アイリッシュ、アレックス・セクストンマサチューセッツ工科大学 |特徴検出 |
| [html5shiv](https://github.com/aFarkas/html5shiv) |アレクサンダー・ファルカス | MIT/GPL2 | HTML5 要素のサポート (Modernizr ビルド経由) |
| [はいのぺ](https://github.com/SlexAxton/yepnope) |アレックス・セクストンとポール・アイリッシュ | MIT/WTFPL |スクリプトの読み込み (Modernizr ビルド経由) |
| [ブックブロック](https://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/) |コドロップス |マサチューセッツ工科大学 |ページめくりプレゼンテーション モード |
| [jwerty](https://github.com/keithamus/jwerty) |キース・サーケル;ベン・アルマン (スロットル/デバウンス) |マサチューセッツ工科大学 |キーボード ショートカット |
| [ビディウェブ](https://github.com/tylergaw/js-bidiweb) |ハセン エル ジュディ | WTFPL |双方向テキスト検出 |
| [strftime.js](https://github.com/phillipTellis/strftime-js) |フィリップ・S・テリス | BSD |日付の形式 |
| [viewport.js](https://github.com/tuupola/jquery_viewport) |ミカ・トゥポラ |マサチューセッツ工科大学 |ビューポートの検出 |
| [wordhighlight.js](https://github.com/bartaz/sandbox.js) |バルテック・ショプカ |マサチューセッツ工科大学 |文書内検索の強調表示 |

## ローカリゼーション

Marked はボランティアの翻訳者のおかげで複数の言語で利用できます。

- アキラ
- ブレット・クローリー
- エノク・コ
- フレミング・マーラー
- ハンス・タンメン
- マティアス・モール
- ミゲル・マルティネス・デ・ラ・トーレ
- ノルマン・プリモー
- PG ニューロモナコ
- リチャード・クラネンドンク
- セバスチャン・ガイデ
- たまりゆき
- 王亮

## 謝辞

また、長年指導してくれた Daniel Jalkut と、Marked アイコンを作成してくれた Felippe van Eekhout にも感謝します。