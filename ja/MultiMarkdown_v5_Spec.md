<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) をチェックして、MultiMarkdown プロセッサを試してください。

## MultiMarkdown とは何ですか? [what-is-multimarkdown]

MultiMarkdown は、Web ページの断片だけではなく完全なドキュメントを処理するように設計された拡張 Markdown プロセッサです。元の Markdown 構文を拡張し、HTML、LaTeX、PDF、ODF、Microsoft Word ドキュメントなどの複数の出力形式への変換を可能にします。

## 主な特徴 [key-characteristics]

- **ドキュメント重視**: Web スニペットだけでなく、完全なドキュメント向けに設計されています。
- **マルチフォーマット出力**: HTML、LaTeX、PDF、ODF、RTF、Word に変換
- **プレゼンテーションよりもコンテンツ**: ドキュメントの構造と意味に重点を置きます
- **クロスプラットフォーム**: あらゆるテキスト エディタを備えたあらゆるオペレーティング システムで動作します。
- **拡張性**: 複雑なドキュメント要件に対応する豊富な機能セット
- **バージョン 5**: パフォーマンスと信頼性が向上した完全な書き換え

## 哲学と設計目標 [philosophy-and-design-goals]

MultiMarkdown は、**コンテンツはプレゼンテーションよりも重要である**という原則に従っています。フォント、色、スタイルを指定するのではなく、ドキュメントの意味 (これはリスト、あれは表など) を表現することに重点が置かれています。

目標は、80% の人が書く文書の 80% に使用可能であり、小説、論文、技術文書、その他のほとんどの文書コンテンツに適していることです。

## 主な機能と拡張機能 [major-features-and-extensions]

### 1. **メタデータのサポート** [1-metadata-support]

- ファイルの先頭にあるドキュメントのメタデータ
- タイトル、著者、日付、カスタム変数
- 出力ヘッダーへの自動組み込み

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**メタデータ変数**

- ドキュメント全体でメタデータ値を使用する
- 構文: `[%variable_name]`
- 処理中の自動置換

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **高度なテーブル** [2-advanced-tables]

**完全なテーブルのサポート**

- ヘッダー、配置、および複雑なテーブル構造
- 表のキャプションとラベルのサポート
- 表への相互参照

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**テーブルの機能**

- コロンを使用した列の配置
- 表のキャプションとラベル
- `[Table 1]` との相互参照
- 複雑なテーブル構造のサポート

### 3. **脚注と引用** [3-footnotes-and-citations]

**脚注**

- `[^1]` 構文を使用した参照形式の脚注
- 自動番号付けとリンク
- インライン脚注のサポート

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**引用サポート**

- 学術引用の書式設定
- 参考文献の生成
- さまざまな引用スタイルのサポート

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

そして、以下は参照の説明です。
参考文献で使用されます。

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

HTML 出力では、引用と脚注は区別できません。

ロケーターを使用する必要はありません (例: p. 23)。ロケーターを使用することを選択した場合、ロケーターとして使用できるものについて特別な規則はありません。ロケーターを省略したい場合は、引用の前に空の角かっこを使用します。

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

使用する引用キーの形式 (例: Doe:2006) に関する規則はありませんが、脚注で `^` を使用するのと同様に、その前に `#` を付ける必要があります。

### 4. **相互参照** [4-cross-references]

**自動相互参照**

- 見出し、表、図、方程式へのリンク
- ラベルの自動生成
- カスタムラベルのサポート

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1
```

**参照タイプ**

- 見出し: `[Section 1]`、`[Heading Title]`
- テーブル: `[Table 1]`、`[Table: Caption]`
- 数字: `[Figure 1]`、`[Figure: Caption]`
- 方程式: `[Equation 1]`

### 5. **定義リスト** [5-definition-lists]

**用語定義のペア**

- 定義リストのサポート
- 用語ごとに複数の定義
- 適切な HTML `<dl>` 出力

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **フェンスで囲まれたコードブロック** [6-fenced-code-blocks]

**言語固有のコード ブロック**

- 言語仕様によるトリプルバッククォート
- 構文強調表示のサポート
- 自動言語検出

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML ⟦14⟧ output

### 7. **Math Support** [7-math-support]

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **画像とリンクの属性** [8-image-and-link-attributes]

**強化されたリンクと画像**

- HTML属性のサポート
- 幅、高さ、代替テキストなど
- 出力形式との統合の改善

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **トランスクルージョン** [9-transclusion]

**ファイルのインクルード**

- ドキュメント内に他のファイルを含める
- ネストされたインクルードのサポート
- 自動パス解決

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**トランスクルージョン機能**

- `{{filename}}` によるファイルのインクルード
- 相対パスと絶対パスのサポート
- ネストされたトランスクルージョンのサポート
- インクルードファイルのマニフェスト生成

### 10. **CriticMarkup の統合** [10-criticmarkup-integration]

**変更追跡**

- CriticMarkup 構文のサポート
- 追加、削除、コメントを追跡する
- 共同編集機能

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **目次** [11-table-of-contents]

**自動目次生成**

- `{{TOC}}` 目次のプレースホルダー
- 見出しによる階層構造
- カスタマイズ可能な目次生成

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **略語** [12-abbreviations]

**HTML スタイルの略語**

- 自動展開用の略語を定義
- ツールチップと説明のサポート
- 適切な HTML `<abbr>` 出力

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 と他の Markdown フレーバーの比較 [multimarkdown-v5-vs-other-markdown-flavors]

|特集 |マルチマークダウン v5 |コモンマーク (GFM) |割引 |クラムダウン |標準 |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
|テーブル |はい |いいえ |はい |はい |いいえ |
|取り消し線 |はい |いいえ |はい |いいえ |いいえ |
|タスクリスト |はい |いいえ |はい |いいえ |いいえ |
|フェンスで囲まれたコード |はい |はい |はい |はい |いいえ |
|数学 |はい |いいえ |いいえ |はい |いいえ |
|脚注 |はい |いいえ |はい |はい |いいえ |
|定義リスト |はい |いいえ |いいえ |はい |いいえ |
|略語 |はい |いいえ |いいえ |はい |いいえ |
|属性リスト |はい |いいえ |いいえ |はい |いいえ |
|拡張機能 |はい |いいえ |限定 |はい |いいえ |
|タイポグラフィ |はい |いいえ |基本 |はい |いいえ |
|オートリンク |はい |いいえ |はい |いいえ |いいえ |
|相互参照 |はい |いいえ |いいえ |いいえ |いいえ |
|引用 |はい |いいえ |いいえ |いいえ |いいえ |
|トランスクルージョン |はい |いいえ |いいえ |いいえ |いいえ |
|メタデータ |はい |いいえ |いいえ |いいえ |いいえ |

## MultiMarkdown v5 の主な利点 [key-advantages-of-multimarkdown-v5]

1. **ドキュメント重視**: Web スニペットだけでなく、完全なドキュメント向けに設計されています。
2. **マルチフォーマット出力**: HTML、LaTeX、PDF、ODF、RTF、Word に変換
3. **学術サポート**: 引用、脚注、および相互参照
4. **プロフェッショナルな機能**: メタデータ、トランスクルージョン、および高度な書式設定
5. **クロスプラットフォーム**: どのオペレーティング システムでも動作します
6. **将来性**: プレーン テキスト形式により長期的な互換性が保証されます
7. **拡張性**: 複雑なドキュメント要件に対応する豊富な機能セット

## 一般的な使用例 [common-use-cases]

**アカデミックライティング**

- 論文、学位論文、研究論文
- 引用管理と参考文献の生成
- 相互参照と脚注

**技術文書**

- API ドキュメントとユーザー ガイド
- 技術仕様とマニュアル
- 構文を強調表示したコードドキュメント

**出版**

- 書籍、記事、レポート
- さまざまなプラットフォーム向けのマルチフォーマット出力
- プロフェッショナルな文書フォーマット

**コンテンツ管理**

- ドキュメント Web サイト
- ナレッジベースとウィキ
- 共同執筆プロジェクト

## ベストプラクティス [best-practices]

1. **メタデータの使用**: ドキュメント情報に YAML 前付を活用する
2. **見出しのある構造**: 目次の生成に適切な見出し階層を使用します。
3. **相互参照の活用**: 自動リンクを使用してナビゲーションを改善します
4. **トランスクルージョンを使用して整理**: 大きなドキュメントを管理可能なファイルに分割する
5. **出力のテスト**: さまざまな出力形式の形式を確認します。
6. **引用の使用**: 学術的な引用を適切に実践する

## 他のマークダウン フレーバーからの移行 [migration-from-other-markdown-flavors]

ほとんどの標準的な Markdown は、変更を加えることなく MultiMarkdown で動作します。 MMD の機能を利用するには:

1. **メタデータの追加**: ドキュメント情報の YAML 前付を含めます
2. **相互参照を使用**: 手動リンクを自動参照に置き換えます。
3. **引用の実装**: 適切な学術引用の書式を追加します。
4. **トランスクルージョンを含む構造**: 大きなドキュメントを小さなファイルに分割します
5. **テーブルの活用**: データのプレゼンテーションに高度なテーブル機能を使用する

## リソース [resources]

- [MultiMarkdown ユーザーガイド](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [MultiMarkdown 構文ガイド](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [MultiMarkdown GitHub リポジトリ](https://github.com/fletcher/MultiMarkdown-5)
- [MultiMarkdown ドキュメント](https://fletcher.github.io/MultiMarkdown-5/)

---

*このドキュメントでは MultiMarkdown v5.1.0 について説明します。最新情報については、[fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/) にある公式 MultiMarkdown ドキュメントを常に参照してください。