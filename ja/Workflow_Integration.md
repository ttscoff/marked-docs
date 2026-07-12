<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## AppleScript

マークには、ファイルを開く、プレビューの制御 (リロード、スクロール、ハイライト、自動スクロール、高速読み取り)、統計の読み取り、プロセッサの設定、HTML または RTF のコピー、プレビュー スタイルの変更、Markdown、HTML、PDF、EPUB、DOCX、ODT、TextBundle、RTF、および OPML へのエクスポートのための完全な [AppleScript 辞書](AppleScript_Support.html) が含まれています。 AppleScript による **見出し/目次のプレビュー** は [進行中の作業として文書化されています](AppleScript_Support.html#table-of-contents-work-in-progress) であり、まだ信頼できません。

アプリケーション、特定のウィンドウ、またはドキュメントをターゲットにできます。アプリケーション コマンドには、**ストリーミング プレビューを開く**、**クリップボードをプレビュー**、**すべて閉じる**などがあります。ドキュメント コマンドには、**統計の取得** と **プロファイルを使用して印刷** が含まれます。エクスポート コマンドは、オプションのエクスポート **プロファイル**、またはプレビュー **スタイル**、**ページサイズ**、**マージン**などのオプションの **`with`** レコードを受け入れます。たとえば:

```applescript
tell application "Marked"
	tell document 1
		export paginated pdf to "/path/to/output.pdf" with {style:"Amblin", pageSize:"A4", margins:"1in"}
	end tell
end tell
```

コマンドリスト、マージンの省略表現、サンドボックスのメモ、およびデバッグのヒントについては、[AppleScript サポート](AppleScript_Support.html) を参照してください。

AppleScript の統合により、Tags.app などのアプリケーションが Marked 内で直接機能できるようになります。

{% note %}
## ショートカット

マークには、macOS 13 以降のネイティブの [ショートカット アクション](Shortcuts_Integration.html) が含まれます。 Finder から PDF へのワークフローには **ファイルを開いてエクスポート** を使用し、マークで既に開いているものには **ドキュメントのエクスポート** を使用し、エクスポート前にテーマを変更するには **プレビュー スタイルの設定** を使用します。エクスポート アクションは、**プロファイル**、プレビュー **スタイル**、**ページ サイズ**、**余白**、**フォント サイズ** などのオプションを受け入れます (AppleScript `with` レコードと同じセマンティクス)。

[shortcuts]: Shortcuts_Integration.html
{% endnote %}

## URL ハンドラー

[マークされた URL ハンドラー][urlhandler] を使用すると、AppleScript から、またはシェル スクリプトの基本的な `open` コマンドを使用して URL を呼び出すだけで、広範な統合が可能になります。

## マーク付きボーナスパック

Marked Bonus Pack は、スクリプト、コマンド、サービスのコレクションです。複数のエディタで動作するものもあれば、特定のエディタに固有のものもあります。サービスは通常、必要な機能を持つエディターで動作します。残りは、使用するアプリケーションに基づいてフォルダーに編成されます。

ボーナス パックをダウンロードし、インストールして使用する手順については、この [ナレッジベース記事](http://support.markedapp.com/kb/how-to-tips-and-tricks/marked-bonus-pack-scripts-commands-and-bundles) で確認できます。

[urlhandler]: URL_Handler.html
[applescript]: AppleScript_Support.html