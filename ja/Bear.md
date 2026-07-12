<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Bear][bear] はライブ プレビューを Marked に直接送信できます。

## クマから送信

Bear では、**表示** メニューから **マーク付きでプレビュー** を選択します (表現は Bear のバージョンによって若干異なる場合があります)。 Marked は TextBundle を受け取るため、埋め込まれた画像とアセットは通常、テキストと一緒に送信されます。

絶対パスまたは `https` URL で参照されている画像も、Marked が到達できる限り解決されます。

## Mac App Store に関するメモ

Marked の **Mac App Store** ビルドを使用しており、Bear からプレビューするときに macOS がディレクトリを開く許可を求め続ける場合は、[Marked サポートにお問い合わせ](http://support.markedapp.com)、直接ダウンロード版への無料のクロスグレードを入手してください。これにより、特定のサンドボックスの摩擦が回避されます。

## タグ

{% prefspane Processor %} で **#Text is tag** と **Style tags** をオンにすることで、クマ スタイルのタグをそのようにレンダリングできます。

W> `#` の後にスペースを入れずに通常の見出しを書く場合、この設定は Marked を混乱させる可能性があります。

## ファイル名とエクスポート

{% prefspane Export %} で **最初の H1 をフォールバック タイトルとして使用** をオンにすると、Marked から PDF を印刷またはエクスポートするときに、そのタイトルによってファイル名と `%title` プレースホルダーが決定されることがあります。

I> Bear 自身の外観に近いプレビュー スタイル [markedapp.com/styles で入手可能](https://markedapp.com/styles/preview?style=bear)。

Bear からのストリーミング プレビューについては、[ストリーミング プレビュー](Streaming_Preview.html) ページおよび [追加のアプリ統合](Additional_Application_Support.html) にまとめられています。

[bear]: https://bear.app/