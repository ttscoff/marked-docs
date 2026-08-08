<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

マークは [Apple DocC](https://www.swift.org/documentation/docc/) ドキュメント カタログ (`.docc` バンドル) を理解しています。カタログ内またはカタログの横にある Markdown をプレビューすると、Marked は、カタログの `Resources` フォルダー内のファイル (`~dark` および `@2x` バリアントを含む) への **拡張子なし** の画像参照を解決できます。

**ファイル拡張子付きのパス** (`images/icon.png`) を使用する通常の Markdown ドキュメントについては、[画像バリアント](Image_Variants.html) を参照してください。この機能はどこでも機能します。 DocC の解決策はカタログ固有です。

## DocC 解決を有効にする [enabling-docc-resolution]

{% prefspane Apps %} で、**DocC イメージ参照の解決** (デフォルトでオン) を有効にします。

DocC 検出は、Marked が開いているドキュメントの `.docc` カタログ祖先を見つけたときに実行されます。特別な URL スキームや Xcode の統合は必要ありません。他のファイルと同じ方法でカタログの Markdown を開きます。

## 拡張子のない参照 [extensionless-references]

DocC カタログ内では、作成者は通常、パスや拡張子を**付けずに**画像を参照します。

```markdown
![Order flow](OrderStateTransitions)
```

マーク付きは、そのファイルがカタログに存在する場合、`OrderStateTransitions` から `Resources/OrderStateTransitions.png` (または別のサポートされているタイプ) を解決します。

パスと拡張子 (`images/chart.png`) が既に含まれている参照は、代わりに [Image Variants](Image_Variants.html) に残され、DocC 解像度によって書き換えられません。

## ダークモードと Retina のバリエーション [dark-mode-and-retina-variants]

DocC カタログでは、イメージごとに複数のファイルが同梱されることがよくあります。

|役割 | `Resources/`の例 |
|-----|--------------------------|
|ライト (1x) | `diagram.png` |
|ダーク (1x) | `diagram~dark.png` |
|ライト (2x) | `diagram@2x.png` |
|ダーク (2x) | `diagram~dark@2x.png` |

複数のバリアントが存在する場合、Marked は、[画像バリアント](Image_Variants.html) で説明されているのと同じ応答性の`<picture>` マークアップを発行します。単一ファイルの参照は、通常の `<img>` または `![](Resources/...)` パスに解決されます。

## HTML とマークダウン [html-and-markdown]

DocC 解決は、Marked のインクルード パス中に適用されます。

- **Markdown ソース** — `![alt](ImageName)` リファレンス
- **HTML ソース** — 拡張子なしの `<img src="ImageName">`

どちらもプレビュー レンダリング前に更新されます。

## ファイル監視 [file-watching]

カタログ `Resources` フォルダー内の解決された画像が Marked のウォッチ リストに追加されます。バリアント ファイルを外部で編集すると、手動で更新しなくてもプレビューが更新されます。

## 関連トピック [related-topics]

- [イメージ バリアント](Image_Variants.html) — プロジェクト内の拡張子ベースのパスに対する `~dark` および `@2x` の検出
- [Xcode Playgrounds](Xcode_Playgrounds.html) — Swift プレイグラウンドの解説をプレビュー
- [設定: アプリ](Settings_Apps.html) — DocC と画像バリアントの設定