<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

マークは多くのエディターやライティング アプリで動作します。このページでは、共有 **設定**、**クリップボード プレビュー**、**ストリーミング プレビュー**へのポインター、およびスクリプト リソースについて説明します。人気のあるアプリの詳細なガイドは、それぞれのヘルプ トピックに記載されています (サイドバーの **サポートされているアプリ** セクションを参照してください)。

## アプリごとのガイド [per-app-guides]

全体的なワークフローは、[Mac での Live Markdown プレビュー](Live_Markdown_Preview_on_Mac.html) から始めます。 Obsidian を使用する場合は、[Marked vs Obsidian Preview](Marked_vs_Obsidian_Preview.html) を参照して、Marked が Obsidian の組み込みプレビューとともに価値を追加するタイミングを決定してください。

|トピック |ヘルプページ |
| :-- | :-- |
| **クマ** | [クマ](Bear.html) |
| **キュリオ** (ストリーミング プレビュー) | [骨董品](Curio.html) |
| **下書き** (ストリーミング プレビュー + アクション) | [下書き](Drafts.html) |
| **DEVONthink** (スクリプト メニュー統合) | [デボン考える](DEVONthink.html) |
| **フォルダー監視** (nvALT、nvUltra など) | [フォルダーウォッチング](Folder_Watching.html) |
| **ハイランド** | 【ハイランド】(Highland.html) |
| **フックマーク** URL 解決 | [フックマーク](Hookmark.html) |
| **iA ライター** | [iAライター](iA_Writer.html) |
| **iThoughtsX** `.itmz` マップ | [iThoughtsX](iThoughtsX.html) |
| **MarsEdit** ライブ プレビュー | [マーズ編集](MarsEdit.html) |
| **マインドノード** | [マインドノード](MindNode.html) |
| **MultiMarkdown Composer** | [MultiMarkdown Composer](MultiMarkdown_Composer.html) |
| **nvUltra** | [nvウルトラ](nvUltra.html) |
| **黒曜石** ボールトとコールアウト | [黒曜石](Obsidian.html) |
| **オムニアウトライナー / OPML** | [OmniOutliner と OPML](OmniOutliner_and_OPML.html) |
| **RTF / RTFD** (ページ、テキストエディットなど) | [RTF および RTFD のサポート](RTF_Support.html) |
| **PDF** | [PDFサポート](PDF_Support.html) |
| **書士 3** | [Scrivener 3 サポート](Scrivener_Support.html) |
| **アーカイブ** ストリーミング プレビュー | [アーカイブ](The_Archive.html) |
| **Ulysses** エクスポート ワークフロー | [ユリシーズ](Ulysses.html) |
| **Vim** (vim マークのプラグイン) | [ヴィム](Vim.html) |
| **VS Code** (マークされた拡張機能で開く) | 【VSコード】(VS_Code.html) |
| **ヴードゥーパッド** | [ヴードゥーパッド](VoodooPad.html) |
| **Xcode プレイグラウンド** | [Xcode プレイグラウンド](Xcode_Playgrounds.html) |

## アプリケーションの設定 [application-settings]

I> いくつかの統合では、{% prefspane Apps %} と {% prefspane Preview %} 内のトグルが公開されています。

![アプリケーション設定][アプリ設定]

これらのペインは、Wiki リンクのデフォルト、Scrivener ハンドオフ、ストリーミング クリップボード設定、OPML/OmniOutliner のマインド マップ埋め込みオプション、Obsidian 統合、または連携エディターに依存するその他のプロセッサーに使用します。

## クリップボードのプレビュー [clipboard-preview]

![][クリップボードプレビューメニュー]

クリップボード内のマークダウン (または互換性のあるプレーン テキスト) は、{% appmenu File, New, Clipboard Preview %} ({% kbd shift cmd V %}) で開きます。クリップボードに **HTML または RTF** が保持されている場合、Marked はプレビューの前にそれを Markdown のようなソースに変換します。これには、RTF 段落で大きなスタイルシート フォント サイズが使用されている場合の大まかな見出し検出も含まれます。

## ストリーミングプレビュー [streaming-preview]

Bear、Curio、Drafts、The Archive、nvALT、nvUltra、およびその他のいくつかのエディターは、**ストリーミング プレビュー** を介して入力時に Markdown を Marked にプッシュできます。セットアップとトラブルシューティングについては、[ストリーミング プレビュー](Streaming_Preview.html) を参照してください。

## スクリプトとボーナス パック [scripts-and-bonus-pack]

BBEdit、TextMate、DEVONthink、Emacs、Vim などのオートメーションには、[マーク付きボーナス パック][ボーナス] が同梱されています。上記の統合を超えてメニュー バーまたはエディタ マクロが必要な場合は、これらのスクリプトをインストールまたは調整します。


[appsettings]: images/screenshots/preferences-Apps.jpg @2x width=689px height=1031px class=preferencepane
[ClipboardPreviewMenu]: images/ClipboardPreviewMenu.jpg @2x width=600px height=198px class=center
[bonus]: https://github.com/kotfu/marked-bonus-pack