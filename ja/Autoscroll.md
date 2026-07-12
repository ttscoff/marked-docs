<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

自動スクロールによりプレビューがゆっくりと移動するので、ハンズフリーで読んだり校正したりできます。 [目次](Document_Navigation.html)、[ミニマップ](Document_Navigation.html#minimap)とは別のものです。現在のビューを自動的にスクロールします。

## 起動と停止

{% kbd s %} を押して自動スクロールをトリガーします。プレビューは現在の速度で前方にスクロールします。

左下のインジケーターは速度を示します。 **上**および**下**矢印キーを使用して調整します。大きなステップを実行するには、矢印を押しながら **Shift** を押します。

戻る ({% kbd return %}) はスクロールを一時停止または再開します。

{% kbd shift s %} は、自動スクロールがアクティブなときにスクロール方向を逆にします。

自動スクロール モードを終了するには、もう一度 {% kbd s %} を押すか、Esc キーを押します。

Marked をテレプロンプターのように使用する場合、Markdown ソースにスクリプトによる一時停止を追加できます。[Marked Special Syntax](Special_Syntax.html) の [Autoscroll Pauses](Special_Syntax.html#pauses) を参照してください。