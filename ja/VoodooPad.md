<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[VoodooPad][vp] は、各ページを 1 つのデータベース ファイルにバンドルします。 `.vpdoc` を [マーク] にドラッグして、VoodooPad で現在最前面にあるページをプレビューします。マークを付けてディスクからリロードする必要があるときはいつでも、VoodooPad で {% kbd cmd S %} を使用してください。

Marked はディスク上のドキュメントを監視し、VoodooPad 内でページを変更するとプレビューを切り替えます。

## 埋め込み画像 [embedded-images]

Markdown または HTML で画像を参照し、そのバイナリが VoodooPad データベースの **内部** に存在する場合、Marked はプレビュー用にそれを抽出できます。 **エイリアス** (参照によってドラッグされたファイル) のみのイメージはバンドルに保存されません。絶対パスまたはディスク上の `.vpdoc` に対する相対パスを持つイメージを指すため、Marked はそれらを解決できます。

[vp]: https://www.voodoopad.com/