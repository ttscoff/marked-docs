<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked は、コンパニオン **ダーク モード** ファイルと **Retina** ファイルが参照画像の隣にある場合、ローカル画像の応答性の高い `<picture>` 要素を自動的に構築できます。これは Apple の DocC ドキュメント カタログと同じ命名規則を使用しますが、ファイル拡張子を含む通常の画像パスを持つ **あらゆる Markdown または HTML ドキュメント**に対して機能します。

`.docc` バンドル内の拡張なしカタログ参照については、[DocC Support](DocC_Support.html) も参照してください。

## 画像バリアントの有効化 [enabling-image-variants]

{% prefspane Apps %} で、DocC 設定で **暗い画像と @2x の画像バリアントを解決** (デフォルトでオン) を有効にします。

この設定は、`.docc` カタログ内にのみ適用される **DocC イメージ参照の解決** とは別のものです。プロジェクトに応じて、一方を使用することも、両方を使用することも、どちらも使用しないこともできます。

## 命名規則 [naming-convention]

バリアント ファイルをプライマリ イメージと**同じフォルダー**に配置します。 Marked は、ベース名に基づいて 4 つの組み合わせを検索します。

|役割 |ファイル名の例 |
|------|-----------------|
|ライト (1x) | `icon.png` |
|ダーク (1x) | `icon~dark.png` |
|ライト (2x) | `icon@2x.png` |
|ダーク (2x) | `icon~dark@2x.png` |

接尾辞の順序は柔軟です。`icon@2x~dark.png` と `icon~dark@2x.png` は同じように扱われます。

サポートされている拡張子: `png`、`jpg`、`jpeg`、`gif`、`svg`、`webp`、`pdf`。

## 書き換えられる内容 [what-gets-rewritten]

マークは、最終プレビュー レンダリングの前**にドキュメントをスキャンします。

- **マークダウン:** `![Alt text](images/icon.png)`
- **HTML:** `<img src="images/icon.png" alt="Alt text">`

少なくとも **2** の一致するバリアント ファイルがディスク上に存在する場合、参照は `<picture>` ブロックに置き換えられます。 1 つの追加ファイルで十分です。4 つのバリアントすべてが必要なわけではありません。

ライト、ダーク、@2x ファイルが存在する場合の出力例:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/icon~dark.png 1x, images/icon~dark@2x.png 2x">
  <source srcset="images/icon.png 1x, images/icon@2x.png 2x">
  <img src="images/icon.png" alt="Alt text">
</picture>
```

プレビュー (および HTML エクスポート) は、ダーク バリアントのユーザー システムの外観と @2x アセットのデバイス ピクセル密度に従います。

## スキップされる内容 [what-is-skipped]

マークは**書き換えません**:

- リモート URL (`http://`、`https://`、`data:`)
- すでに `~dark` ファイルを指している参照
- `<img>` タグがすでに既存の `<picture>` 要素内にあります
- `![Diagram](diagram)` のような拡張子のない名前 — カタログ形式の参照には [DocC Support](DocC_Support.html) を使用します

## ライブ プレビューとファイルの視聴 [live-preview-and-file-watching]

バリアントが検出されると、Marked は **すべての既存のバリアント ファイル** をメイン ドキュメントと並んでウォッチ リストに追加します。外部エディターで `icon~dark.png` を保存すると、`icon.png` の編集と同じライブ画像のリロードがトリガーされます。

## ヒント [tips]

- 可能であれば、ソース内の **light 1x** 画像を参照してください (`icon~dark.png` ではなく、`icon.png`)。マークはその道から兄弟を発見します。
- `@2x` アセットしかない場合は、少なくとも 1 つの他のバリアント (通常は `~dark`) を含めます。そうしないと、マーク付きで参照が変更されないままになります。
- バリアント解決では、[複数ファイル ドキュメント](Multi-File_Documents.html) と同じ基本パス ルールである **ドキュメントに対する相対パス** (またはネストされたインクルードの場合はインクルード ファイルのフォルダー) を使用します。

## 関連トピック [related-topics]

- [DocC サポート](DocC_Support.html) — `.docc` カタログ内の拡張子なしのイメージ名
- [設定: アプリ](Settings_Apps.html) — DocC と画像バリアントの設定を切り替えます
- [プレビュー](Previewing.html) — ライブ プレビューとファイルの更新