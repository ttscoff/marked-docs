<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[vim-marked][vimrepo] は、Marked で現在の Markdown バッファを開く Vim プラグインです。 `:MarkedOpen`、`:MarkedQuit`、`:MarkedToggle`、`:MarkedPreview` が追加されるため、エディターを離れることなくファイル (または範囲) を Marked に送信できます。

## セットアップ [setup]

プラグインマネージャーを使用してインストールします。 `vim-plug` およびその他のオプションについては、[プロジェクトの README][vimrepo] を参照してください。デフォルトの `g:marked_filetypes` には `markdown` と一般的なバリアントが含まれます。カスタム `filetype` を使用する場合は、リストを拡張します。

## macOS とアプリ名 [macos-and-app-name]

マークは macOS 専用であるため、プラグインは他のシステムにはロードされません。デフォルトのアプリ名は **Marked 2** です。 Marked のコピーが別の名前またはパスでインストールされている場合は、`g:marked_app` を一致するように設定します (たとえば、アプリ バンドルへのフル パス)。 README では、終了、自動終了、フォーカス動作について説明しています。

I> このヘルプ トピックは、vim マークが付けられたプロジェクトの一部ではありません。最新のコマンドとオプションについては、[GitHub リポジトリ][vimrepo] を使用してください。


[vimrepo]: https://github.com/itspriddle/vim-marked