# <%= @title %>

W> **Marked における Apex サポートはベータ版です。** 統合が進むにつれて動作が変更される可能性があります。問題や予期しない表示、不足している構文については [support.markedapp.com](https://support.markedapp.com) までご報告ください。

Apex は**統合 Markdown プロセッサ**です。CommonMark、GitHub Flavored Markdown(GFM)、MultiMarkdown、Kramdown のいずれかを選ぶ理由となっている機能を、他のフレーバーを手放すことなく一つのエンジンでカバーすることを目指しています。

Marked では、**Apex(ベータ)** は常に Apex の**統合(unified)**モードで動作します(これらすべての機能ファミリーが同時に有効になります)。現時点では、Marked 内で個別に Apex の「CommonMark モード」や「Kramdown モード」を選択することはできませんが、将来的に対応する可能性があります。

Apex を試すには [Markdown Dingus](x-marked-3://dingus?processor=apex) を開くか、{% appmenu Help, Markdown Reference %} を開いて **Apex** タブを選択すると、簡潔なチートシートが表示されます。

---

## Apex が存在する理由 [why-apex-exists]

Markdown の「フレーバー」が枝分かれしてきたのには正当な理由があります --- GitHub はタスクリストとテーブルを必要とし、MultiMarkdown は脚注とメタデータを必要とし、Kramdown は属性リストを必要としました --- しかし、どれか一つのプロセッサを選ぶと、通常は他のプロセッサの構文を諦めることになります。

Apex の目標は、それらの拡張機能を**統合**し、1 つのドキュメントで次のようなものを使えるようにすることです。

- 日常的な CommonMark / GFM の書き方(フェンス付きコード、タスクリスト、取り消し線、GFM テーブル)
- MultiMarkdown スタイルの脚注、略語、メタデータの書き方
- Kramdown になじみのある定義リスト、数式、(高度な用途向けの)属性リスト
- コールアウト、Critic Markup、TOC マーカーなど、Marked 向けの便利な機能

完全な本家ドキュメントは [Apex wiki](https://github.com/ApexMarkdown/apex/wiki) にあります。このページでは、Marked のプレビューで日常的に必要となる内容を扱います。

---

## Marked で Apex を有効にする [enabling-apex-in-marked]

1. {% prefspane Processor %} を開きます。
2. **デフォルトの Markdown プロセッサ**を **Apex(ベータ)** に設定します。
3. または、`Processor: apex` のようなメタデータ(エイリアス: `apex-beta`、`unified`)を使って、ドキュメントごとに上書きすることもできます。

エイリアスは、AppleScript、Conductor の「Run Processor」アクション、カスタムプロセッサの標準出力(`APEX`)、`x-marked://` の defaults URL からも使用できます。

T> このベータ版では、Apex が実行される前に Marked が独自のファイルインクルード(`<<[file]`、および関連する Marked のインクルードパス)を展開します。サンドボックス化のため、Marked では Apex ネイティブのインクルードエンジンはオフになっています。これまで通り Marked のインクルード機能を使用してください。

---

## Apex が追加・統合する基本構文 [basic-syntax]

標準的な Markdown(見出し、強調、リンク、画像、リスト、引用、コード)は期待通りに動作します。以下の項目は、Apex に切り替える際に多くの人が必要とする追加機能です。

### タスクリスト [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### 取り消し線 [strikethrough]

```markdown
~~removed text~~
```

### テーブル [tables]

見出し区切りと列の配置を備えた GFM のパイプテーブル:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

高度なテーブル機能(rowspan `^^`、colspan、キャプション、グリッドテーブル、CSV)については、wiki の [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables) で解説されています。

### 脚注 [footnotes]

参照形式:

```markdown
See the note[^1].

[^1]: Footnote text.
```

MultiMarkdown / Kramdown でおなじみのインライン形式もサポートされています。詳細: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax)。

### 定義リスト [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### 上付き文字と下付き文字 [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### 数式 [math]

インライン `$x^2$` とディスプレイ `$$...$$`(プレビューの表示については、引き続き Marked の MathJax / KaTeX 設定が制御します)。

### コールアウト [callouts]

Obsidian / Bear スタイル:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Marked の [Special Syntax](Special_Syntax.html) と、Apex の [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts) wiki ページも参照してください。

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

いつも通り Marked で Critic Markup を有効にしてください。Apex はプロセッサのパイプライン内で critic 構文をレンダリングできます。[CriticMarkup](CriticMarkup.html) を参照してください。

### 略語 [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### 絵文字ショートコード [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### メタデータ [metadata]

YAML フロントマター、MultiMarkdown スタイルの `Key: Value` ヘッダー、Pandoc タイトルブロックが認識されます。対応している箇所では `[%key]` で値を挿入できます。

設定の詳細については、wiki の [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) と [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) を参照してください。

### 目次マーカー [table-of-contents-markers]

Apex は、以下のような一般的な TOC マーカーを認識します。

- `<!--TOC-->`
- `{{TOC}}` または `{{TOC:2-4}}`
- Kramdown スタイルの `{:toc}`

IAL が利用可能な場合は、`{:.no_toc}` を使って見出しを除外できます。詳細: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax)。

### 特殊マーカー [special-markers]

`<!--BREAK-->`(改ページ)や `<!--PAUSE:N-->`(自動スクロール)といった Marked 向けの HTML コメントは、引き続き Apex のプレビューでも機能します。

---

## 高度なトピック(wiki) [advanced-topics-wiki]

強力ではあるものの、日常のプレビューではあまり使われない機能については、[Apex wiki](https://github.com/ApexMarkdown/apex/wiki) を参照してください。

| トピック | Wiki |
|------|------|
| 索引生成 | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| 引用/参考文献 | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| インライン属性リスト、スパン、フェンス付きディビジョン | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| 複数ファイルドキュメントとインクルード | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| 見出し ID の形式 | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| マルチフォーマット画像 | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| 互換モード(CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| プラグインとフィルター | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins)、[Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode)、[Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration)、[Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## 関連項目 [see-also]

- [プロセッサの選択](Choosing_a_Processor.html) --- MultiMarkdown、CommonMark、Kramdown、Discount、Apex のどれを選ぶか
- [設定: プロセッサ](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Apex wiki ホーム](https://github.com/ApexMarkdown/apex/wiki)
- 問題を報告: [support.markedapp.com](https://support.markedapp.com)
