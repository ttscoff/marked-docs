<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked は 2 つの方法で [Obsidian][obsidian-app] ノートを操作します。**保管庫フォルダー**を開いて自動フォローするか、**コミュニティ プラグイン**を使用してより緊密に同期します。

Obsidian の組み込みプレビューは、アプリを終了しない場合に最適です。公開品質のエクスポート、高度な校正、カスタム CSS テーマ、または複数のエディタ間で同じライブ プレビュー ワークフローが必要な場合は、「マーク付き」を選択します。完全な比較については、[Marked vs Obsidian プレビュー](Marked_vs_Obsidian_Preview.html) を参照してください。

## ボールト全体を開く [open-an-entire-vault]

**vault フォルダ** (vault ルートにある Obsidian の隠し設定フォルダを含むディレクトリ) を Dock のマークにドラッグします。 Marked はそのツリーを監視し、**最近編集した** メモをプレビューに保持し、Obsidian に保存すると更新します。

Vault 固有のデフォルト (スタイル、プロセッサ、画像のベース URL など) の場合は、その Vault の下のパスと一致する [カスタム ルール](http://support.markedapp.com) を追加します。

## 黒曜石コールアウト構文 [obsidian-callout-syntax]

MultiMarkdown プロセッサが実行されると、Marked は一般的な **Obsidian スタイルの吹き出し** (`> [!note]` パターン) をスタイル付きのブロック マークアップに変換して、プレビューの残りの部分と一致するようにします。

## Marked 3 Obsidian プラグイン [marked-3-obsidian-plugin]

[Marked 3 Obsidian プラグイン][プラグイン] は、コマンドまたはホットキーを使用して現在のノートまたはボールト全体を開くことができるため、Marked ウィンドウは編集内容を追跡します。コマンド パレット (**⌘P**) を使用して **マーク付き** を検索するか、Obsidian の **ホットキー** 設定でホットキーを割り当てます。

### コミュニティプラグインからのインストール [installing-from-community-plugins]

Obsidian で、**[設定] → [コミュニティ プラグイン]** を開き、**マーク付き**を参照または検索して、**マーク付きで開く**をインストールします。

### プラグインを手動でインストールする [manually-installing-the-plugin]

GitHub からインストールする場合:

1. GitHub の [最新リリース][プラグインリリース] から `main.js` と `manifest.json` をダウンロードします (または [Marked3-obsidian][plugin] リポジトリからビルドします)。
2. Vault の Vault ルートにある Obsidian の構成ディレクトリ内の `plugins/` にプラグイン フォルダーを作成します。フォルダー名は、`manifest.json` のプラグイン `id` と一致する必要があります (フルパスについては、[プラグインの README][プラグイン] を参照してください)。
3. `main.js` と `manifest.json` をそのフォルダーにコピーします。
4. Obsidian で、**設定 → コミュニティ プラグイン** を開き、必要に応じて **制限付きモード** をオフにし、**マークで開く** を有効にします。

[obsidian-app]: https://obsidian.md/
[plugin]: https://github.com/ttscoff/Marked3-obsidian
[plugin-releases]: https://github.com/ttscoff/Marked3-obsidian/releases/latest