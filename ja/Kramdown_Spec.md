<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Markdown Dingus](x-marked-3://dingus?processor=kramdown) をチェックして、Kramdown プロセッサを試してください。

## クラムダウンとは何ですか? [what-is-kramdown]

Kramdown は、高速で純粋な Ruby Markdown スーパーセット コンバータであり、Maruku、PHP Markdown Extra、Pandoc などの他の実装にある機能を使用して元の Markdown 構文を拡張します。ほとんどの Markdown ドキュメントとの互換性を維持しながら、明確なルールを備えた厳密な構文を提供します。

## 主な特徴 [key-characteristics]

- **高速で純粋な Ruby**: パフォーマンスと移植性のために完全に Ruby で書かれています
- **厳密な構文**: 明確なルールと明確な仕様を提供します
- **拡張機能**: 標準の Markdown にはない多くの拡張機能が含まれています
- **Jekyll Integration**: Jekyll 静的サイト ジェネレーターのデフォルトの Markdown プロセッサ
- **包括的**: 広範なカスタマイズによりブロックレベルとスパンレベルの両方の要素をサポート

## 標準マークダウンとの主な違い [major-differences-from-standard-markdown]

### 1. **拡張されたブロックレベル要素** [1-enhanced-block-level-elements]

**定義リスト**

- Kramdown は定義リストをサポートします (標準の Markdown にはありません)
- `:` を使用して用語と定義を区切ります

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**テーブル**

- ヘッダー、配置、書式設定を含む完全なテーブルのサポート
- 基本的な Markdown テーブル構文よりも包括的

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**数学ブロック**

- LaTeX構文を使用した数式のサポート
- インライン演算とブロック演算の両方をサポート

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **高度なテキスト マークアップ** [2-advanced-text-markup]

**脚注**

- 自動番号付けによる脚注の完全なサポート
- `[^1]` 構文を使用した参照形式の脚注

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**略語**

- HTML スタイルの略語のサポート
- 定義された略語の自動展開

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**活版印刷の記号**

- 一般的な活版文字の自動変換
- スマート引用符、全角ダッシュ、省略記号など。

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **属性リストと拡張機能** [3-attribute-lists-and-extensions]

**属性リスト定義 (ALD)**

- 再利用可能な属性セットを定義する
- ID、クラス、カスタム属性のサポート

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**インライン属性リスト (IAL)**

- 特定の要素に属性を付加する
- ブロックレベルとスパンレベルの両方をサポート

```markdown
This *is*{:.underline} some ⟦3⟧{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**拡張機能**

- 追加機能のためのカスタム拡張システム
- コメントとオプション用の組み込み拡張機能

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **コード ブロックのサポートの強化** [4-enhanced-code-block-support]

**言語仕様**

- フェンスで囲まれたコードブロックの自動構文ハイライト
- 多くのプログラミング言語のサポート

    ```ruby
    def hello
      puts "Hello, World!"
    end
    ```

**標準コードブロック**

- インデントされたコードブロックの処理の改善
- 他のブロック要素との統合が改善されました

### 5. **より厳格な解析ルール** [5-stricter-parsing-rules]

**行の折り返し**

- ハードラップされたコンテンツ (遅延構文) のサポート
- 行の折り返しが許可される場合の明確なルール
- 読みやすさの観点からは推奨されませんが、互換性のためにサポートされています

**タブの処理**

- タブストップが 4 の倍数であると仮定します
- タブはインデントの行頭にのみ許可されます
- 前にスペースを入れないでください

**ブロック境界**

- 要素がブロック境界で開始/終了する必要がある場合の明確なルール
- 異なる要素タイプ間での一貫した動作

### 6. **高度なリンクと画像のサポート** [6-advanced-link-and-image-support]

**自動リンク**

- 強化された自動リンク検出
- URL と電子メール アドレスの処理の改善

**参考リンク**

- 参照リンク処理の改善
- 複数の定義の競合解決の向上

**画像の属性**

- IAL による画像属性のサポート
- 幅、高さ、代替テキスト、およびその他の HTML 属性

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **HTML の統合** [7-html-integration]

**HTML ブロック**

- Markdown 内での HTML の処理が改善されました。
- HTML 属性と処理のサポート
- 標準の Markdown HTML 処理よりも柔軟です

**HTML スパン**

- 属性をサポートするインライン HTML
- Markdown 構文との統合の改善

### 8. **数学式** [8-mathematical-expressions]

**インライン数学**

- `$...$` インライン数式の構文
- LaTeX互換の構文

**ブロック数学**

- `$$...$$` ブロック数式の構文
- 複雑な方程式と公式のサポート

## Kramdown と他のマークダウン フレーバー [kramdown-vs-other-markdown-flavors]

|特集 |クラムダウン |コモンマーク (GFM) | GitHub 風味 |マルチマークダウン |標準 |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
|取り消し線 |いいえ |はい |いいえ |いいえ |いいえ |
|タスクリスト |いいえ |いいえ |はい |はい |いいえ |
|フェンスで囲まれたコード |はい |はい |はい |はい |いいえ |
|数学 |はい |いいえ |はい |はい |いいえ |
|脚注 |はい |はい |はい |はい |いいえ |
|定義リスト |はい |いいえ |いいえ |はい |いいえ |
|略語 |はい |いいえ |いいえ |いいえ |いいえ |
|属性リスト |はい |いいえ |いいえ |いいえ |いいえ |
|タイポグラフィ |はい |いいえ |いいえ |はい |いいえ |

## クラムダウンの主な利点 [key-advantages-of-kramdown]

1. **包括的な機能セット**: 他の実装には見られない多くの拡張機能が含まれています
2. **Jekyll 統合**: Jekyll 静的サイト ジェネレーターとのシームレスな統合
3. **Ruby エコシステム**: 優れた Ruby ツールのサポートを備えた純粋な Ruby 実装
4. **拡張性**: 追加機能のためのカスタム拡張システム
5. **属性サポート**: HTML 出力カスタマイズのための豊富な属性システム
6. **数学サポート**: LaTeX 数学式の組み込みサポート
7. **厳密な解析**: 明確で曖昧さのない解析ルール

## 一般的な使用例 [common-use-cases]

**ジキル サイト**

- Jekyll 静的サイト生成用のデフォルト プロセッサ
- ドキュメントやブログ サイトに最適

**技術文書**

- 科学的および技術的な文章の数学的サポート
- 高度な HTML カスタマイズのための属性リスト

**アカデミックライティング**

- 引用と参考文献の脚注サポート
- 数式や方程式の数学的表現

**コンテンツ管理**

- カスタム機能の拡張機能
- メタデータとスタイルの属性リスト

## リソース [resources]

- [Kramdown 構文ドキュメント](https://kramdown.gettalong.org/syntax.html)
- [Kramdown コンバーターのドキュメント](https://kramdown.gettalong.org/converter.html)
- [Jekyll 統合ガイド](https://jekyllrb.com/docs/configuration/markdown/)
- [Kramdown GitHub リポジトリ](https://github.com/gettalong/kramdown)

## 標準マークダウンからの移行 [migration-from-standard-markdown]

ほとんどの標準的な Markdown ドキュメントは、変更を加えることなく Kramdown で動作します。 Kramdown の機能を活用するには:

1. **定義リストの追加**: 用語集と用語リストを変換します。
2. **属性リストの使用**: ID、クラス、カスタム属性を追加します。
3. **脚注の実装**: 括弧内の参照を変換する

## ベストプラクティス [best-practices]

1. **遅延構文を避ける**: 読みやすさのためにハードラップに依存しないでください。
2. **属性リストの使用**: スタイルとメタデータに IAL を活用する
3. **一貫したインデント**: 可能な場合はタブではなくスペースを使用してください

---

*このドキュメントでは Kramdown 2.5.1 について説明します。最新の情報については、[kramdown.gettalong.org](https://kramdown.gettalong.org/) にある公式ドキュメントを常に参照してください。*
