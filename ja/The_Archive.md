<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[アーカイブ][アーカイブ] は、メモをディスク上のファイルとして管理し、編集中のメモを Marked の **ストリーミング プレビュー** チャンネルに直接ミラーリングできます。

## マークされたものにプレビューをストリーム

1. [マーク] で、{% appmenu File, New, Streaming Preview %} を開きます (または、既存のストリーミング プレビュー ウィンドウを再利用します)。
2. アーカイブに切り替えて、**メモ → マーク付きにプレビューをストリーム** を選択します。これにより、アーカイブがマーク付きをアクティブ化し、最前面のノート テキストの送信を開始します。

他の統合アプリと同じ `mkStreamingPreview` クリップボード契約に従って、The Archive に入力すると更新がマークされます。[ストリーミング プレビュー](Streaming_Preview.html) の [技術詳細](Streaming_Preview.html#developers) を参照してください。

プレビューが古いように見える場合は、ストリーミング ウィンドウがまだマーク済みの最前面にあることを確認し、[アーカイブ] メニュー コマンドを 1 回切り替えます。

[archive]: https://www.zettelkasten.de/the-archive/