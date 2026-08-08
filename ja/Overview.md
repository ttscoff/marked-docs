<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% apponly div %}
*このドキュメントの最新バージョンについては、[オンライン版][ヘルプ]をご覧ください。*
{% endapponly %}

**増え続ける[マーク付きチュートリアルビデオ](https://www.youtube.com/playlist?list=PLNoOPRHOBV0ptk_ka386xltm3VyVw6QgZ)のコレクションを必ずチェックしてください。**

## マークダウンとは何ですか? [whats-markdown]

[daringfireball]: http://daringfireball.net/projects/markdown/basics
[mmd5]: https://fletcher.github.io/MultiMarkdown-5/
[mdguide]: https://www.markdownguide.org/
[help]: http://markedapp.com/help/

Markdown は単純なシンボルを使用する基本的なマークアップ言語で、`*italics*` や `**bold**` のような単純な構文で HTML を作成 (および他の形式にエクスポート) できます。 Markdown は John Gruber によって作成され、急速に Web パブリッシング、メモ作成、さらには書籍出版の事実上の標準になりつつあります。これにより、大量のツールバーや書式設定をいじることなく、ページ上に単語を取得し、プロセッサ (Marked など) にスタイルと書式設定を処理させるだけで書くことができます。

Marked は GitHub Flavored Markdown、CommonMark (GFM)、Kramdown、および MultiMarkdown で動作し、プレビューのためにいくつかのバリアントから構文を変換できます (Textile、reStructuredText、Wikitext など、必要なほぼすべてのプロセッサで動作するように拡張することもできます)。ここに来ているので、これらのマークアップ言語の少なくとも 1 つが何であるかはご存知だと思います。そうでない場合は、John Gruber の [Markdown Basics][daringfireball] から始めて、[MarkdownGuide.org][mdguide] をチェックしてください。 Marked には、ヘルプ メニューの下に完全な Markdown 構文ガイドが含まれています。

[Markdown Dingus](x-marked-3://dingus) を使用して、Marked がサポートするさまざまな種類の Markdown を試すことができます。

## 何がマークされていますか? [whats-marked]

Marked は、macOS 用のライブ Markdown プレビュー アプリです。ファイルの変更を監視し、保存するたびにプレビューを更新する、エディターに依存しない (マルチ)Markdown プレビュー アプリケーションです。書式設定の詳細を分離して自動化することで、最終的な成果物を常に監視しながら、プレゼンテーションではなく執筆に集中できるようになります。

セットアップのワークフローとエディター固有のクイック スタートについては、「Mac でのライブ Markdown プレビュー」(Live_Markdown_Preview_on_Mac.html) を参照してください。短い製品概要については、[markedapp.com/markdown-preview](https://markedapp.com/markdown-preview/) にアクセスしてください。

マークは、iCloud ドキュメントなど、ローカルでアクセス可能なあらゆるファイルで動作します。テキスト ドキュメントをエディタのツールバーから [マーク] にドラッグするだけで、HTML プレビューとしてレンダリングされ、変更の追跡が開始され、作成中にプレビューが更新されます。基本的な「インクルード」構文を使用して、または Scrivener、Leanpub、mmd_merge インデックス形式を使用して [マルチファイル ドキュメント](Multi-File_Documents.html) をコンパイルすることもできます。

Marked には、ワードカウントやその他のドキュメント統計、他のアプリケーションの上に表示したり、背景で薄暗くしたりする機能などの追加機能があり、巧妙に作成されたさまざまなスタイルで作品を表示できます。印刷、PDF、Word ドキュメント、完全な HTML ドキュメント (スタイルや画像を含む) に出力したり、キーストロークで HTML ソースや RTF データをクリップボードにコピーしたりできます。 Marked には、基本的な AppleScript 辞書と [URL ハンドラー](URL_Handler.html) もあり、ワークフローに簡単に統合できます。

そうそう、Vim や Emacs から Sublime Text や TextMate までのテキスト エディター、MultiMarkdown Composer、Byword、iA Writer などの Markdown エディター、さらには Ulysses、Scrivener、VoodooPad、MarsEdit などの予想外のアプリなど、お気に入りのアプリをたくさん使用できます。

## 使用例 [example-uses]

Marked は、あらゆるテキスト エディタを Markdown 対応エディタに変えます。プレビューはいつでも利用でき、作業に応じて更新されます。

* お気に入りのエディターがライブ Markdown プレビューを提供していない場合は、Marked で作業中のドキュメントを開き、ウィンドウを横にフローティングして、フル機能の Markdown 書き込みエクスペリエンスを実現します。
* MacVim または他のターミナルベースのエディタで書いたりブログを書いたりするのは好きですか?これで、作業中に同期された Markdown プレビューが表示されます。
* Marked は、既存の Markdown プレビューを超える表示機能も提供しており、代わりに完全な単語数とドキュメントの統計情報を提供したり、提案を書いたり、Markdown 書式設定の間違いを強調表示するために使用することもできます。
※エディタなしでMarkedを使用することもできます。 Markdown ファイルをアイコンにドラッグするだけで、プレビュー、印刷、PDF、DOC、RTF、または HTML ソース コードにエクスポートできます。 Marked は、**`.rtf` および `.rtfd` ファイル** をソース ドキュメントとして開くこともできます ([RTF および RTFD のサポート](RTF_Support.html))。
* 自動保存するアプリでは、何もしなくてもプレビューが執筆に追いつきます。任意のエディタ...または *すべて* のエディタで使用します。
*本を書いていますか？ Marked は、複数のファイルをコンパイルして作業の完全なプレビューを表示したり、保存するたびにメイン ドキュメントを更新して、それらに含まれるファイルの変更を監視したりすることもできます。フォルダー全体の変更を監視し、現在更新中のファイルにプレビューを自動的に切り替えることもできます。準備ができたら、EPUB、DOCX、または TextBundle 形式で公開できます。
* AI コーディング プラットフォームを使用していますか? Marked でプランまたはドキュメントのフォルダーを開くと、そのフォルダー内の Markdown ファイルが変更されるたびに、Marked がそのファイルを表示し、最新の編集点まで自動的にスクロールします。 Marked は人魚図を表示し、あらゆる種類の拡張構文を処理できます。作業中にファイルを切り替えることなく、計画と文書を追跡します。