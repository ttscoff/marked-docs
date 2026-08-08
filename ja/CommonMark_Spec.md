<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

CommonMark (GFM) プロセッサを試してみるには、[Markdown Dingus](x-marked-3://dingus?processor=commonmark) をチェックしてください。


## CommonMark とは何ですか? [what-is-commonmark]

CommonMark は、厳密に指定された、互換性の高い Markdown の実装です。これは、John Gruber のオリジナルの Markdown 仕様のあいまいさと矛盾に対処するために作成されました。そのため、さまざまなプラットフォームやツール間での実装が多岐にわたりました。

## CommonMark が存在する理由 [why-commonmark-exists]

John Gruber による元の Markdown 仕様は、多くの領域で意図的に曖昧であり、さまざまな実装によって異なる解釈が生じていました。これにより、同じ Markdown ドキュメントが異なるプラットフォーム (GitHub、StackOverflow、Reddit など) で異なるレンダリングを行うという問題が発生しました。

CommonMark は以下を提供します。

- すべての Markdown 構文に対する **明確な仕様**
- **包括的なテストスイート**により、一貫した動作を保証します
- **競合する構文の優先順位ルールを明確にする**
- **一貫して実装できる詳細な解析アルゴリズム**

## 標準マークダウンとの主な違い [key-differences-from-standard-markdown]

### 1. **より厳格な解析ルール** [1-stricter-parsing-rules]

CommonMark は、より一貫した解析動作を強制します。

**ブロック要素の前の空白行**

- CommonMark では、見出し、ブロック引用符、およびリストの前に空行が必要です
- 標準のマークダウンでは、多くの場合、空白行なしでこれらが許可されます。

```markdown
Text
# Heading
```

*CommonMark: 見出しの前に空行が必要です*

*標準マークダウン: 多くの場合、空白行なしで許可されます*

### 2. **リスト項目の解析** [2-list-item-parsing]

**インデントの要件**

- CommonMark にはリスト項目のインデントに関する特定のルールがあります
- サブリストは一貫してインデントする必要があります (通常は 4 つのスペース)
- 標準のマークダウン実装はこれに応じて異なります

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**リストの続き**

- CommonMark には、リスト項目が「緩い」場合と「きつい」場合について明確なルールがあります。
- 緩やかなリストでは項目が `<p>` タグで囲まれますが、タイトなリストではラップされません。

### 3. **コード ブロックの処理** [3-code-block-handling]

**フェンスで囲まれたコードブロック**

- CommonMark は、バッククォートまたはチルダを使用してフェンスで囲まれたコード ブロック構文を標準化します。
- 一貫したインデントと終了マーカーが必要です


    ```language
    コードはここにあります
    ```


**インデントされたコード ブロック**

- CommonMark では、インデントされたコード ブロックの前に空白行が必要です
- 標準のマークダウンでは、多くの場合、空白行なしで使用できます。

### 4. **リンクと画像処理** [4-link-and-image-processing]

**参照リンクの優先順位**

- CommonMark には、参照定義が優先される明確なルールがあります。
- 同じ参照に対する複数の定義が一貫して処理されます。

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**リンク解析順序**

- CommonMark は強調前にリンクを処理します
- これは、ネストされた構文の解釈方法に影響します。

### 5. **強調と強い強調** [5-emphasis-and-strong-emphasis]

**ネストされた強調ルール**

- CommonMark には、ネストされた `*` および `_` マーカーを処理するための特定のアルゴリズムがあります
- 複雑な強調パターンのあいまいな解析を防止します

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**区切り文字処理**

- CommonMark は、一貫した強調解析のために「デリミタ スタック」アルゴリズムを使用します
- 標準の Markdown 実装はアプローチが異なります

### 6. **HTML ブロックの処理** [6-html-block-processing]

**HTML ブロックの検出**

- CommonMark には、特定のルールを持つ 7 種類の HTML ブロックがあります
- タイプごとに開始/終了条件の要件が異なります。

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **改行の処理** [7-line-break-handling]

**ハードラインブレイク**

- CommonMark ではハードブレークの場合、行末に 2 つのスペースが必要です
- 単一の改行はソフトブレークになります (HTML では無視されます)。

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **エンティティと文字の参照** [8-entity-and-character-references]

**数値文字参照**

- CommonMark は 10 進数と 16 進数の両方の数値参照をサポートします
- 標準のマークダウンのサポートは異なります

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## CommonMark 解析アルゴリズム [commonmark-parsing-algorithm]

CommonMark は 2 段階の解析アプローチを使用します。

### フェーズ 1: ブロック構造 [phase-1-block-structure]

1. **ライン処理**: 各ラインはブロックレベルのマーカーについて分析されます。
2. **コンテナ ブロック**: ブロック引用符、リスト、およびその他のコンテナが識別されます
3. **リーフ ブロック**: 見出し、コード ブロック、段落が処理されます
4. **参照リンク**: リンク定義は後で使用するために収集されます。

### フェーズ 2: インライン構造 [phase-2-inline-structure]

1. **インライン処理**: ブロック内のテキストはインライン要素に対して解析されます。
2. **強調解析**: 区切り文字スタック アルゴリズムを使用して一貫した強調を実現します。
3. **リンク解決**: 参照リンクは、収集された定義を使用して解決されます。
4. **エンティティ処理**: 文字参照が実際の文字に変換されます

## CommonMark の利点 [benefits-of-commonmark]

1. **予測可能な動作**: 同じ入力は常に同じ出力を生成します
2. **クロスプラットフォーム互換性**: さまざまなツール間で一貫して動作します。
3. **包括的なテスト**: 広範なテストスイートにより信頼性を確保
4. **明確なドキュメント**: 詳細な仕様により推測を排除
5. **将来性**: 新機能用の明確に定義された拡張ポイント

## 実装メモ [implementation-notes]

CommonMark は次のように設計されています。

- **仕様準拠**: CommonMark の公式仕様に正確に従っています。
- **テスト主導**: 公式 CommonMark テスト スイートに合格
- **拡張可能**: 互換性を維持しながら追加機能で拡張できます。
- **高速**: パフォーマンスのために最適化された解析アルゴリズム

## リソース [resources]

- [CommonMark仕様](https://spec.commonmark.org/0.31.2/)
- [CommonMark テストスイート](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - オンラインテストツール
- [CommonMark ディスカッション フォーラム](https://talk.commonmark.org/)

---

*このドキュメントでは CommonMark 0.31.2 (2024-01-28) について説明します。最新の情報については、必ず公式仕様を参照してください。*
