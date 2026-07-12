<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[MarsEdit][me] は、投稿をディスク上のルース ファイルとしてではなく、データベース内に保存します。したがって、Marked は、実行中の MarsEdit アプリケーションと通信する専用のプレビュー ワークフローを使用します。

## MarsEdit プレビュー ウィンドウ

Choose {% appmenu File, New, MarsEdit Preview %}. Marked asks AppleScript to read the **front post in MarsEdit** (Red Sweater's bundle IDs for direct, Mac App Store, Setapp, and MarsEdit 4/5 are recognized).作業中はドキュメントを開いた状態で MarsEdit を実行し続けてください。

- **手動更新:** 強制的に更新する場合は、Marked のプレビューから保存します。
- **自動更新:** 監視が有効になり、MarsEdit の自動保存が更新されるたびにマークが付けられます。

利用可能な投稿がない場合、「マーク付き」では、古いテキストの代わりに短いエラーがプレビューに表示されます。

### Extended posts

Content in MarsEdit's **extended** field is separated in Marked's preview and source using a WordPress-style `<!--more-->` divider so pagination-oriented sites (WordPress, Jekyll, etc.) still see the break.コメントは他の場所では無害です。

### メタデータのタグとカテゴリ

MarsEdit のタグとカテゴリは、MultiMarkdown メタデータ ブロックに公開されます。 MultiMarkdown プロセッサ ({% prefspane Processor %}) を使用すると、次のように参照できます。

    Tagged: [%tags]
    Posted In: [%categories]

[me]: https://www.red-sweater.com/marsedit/