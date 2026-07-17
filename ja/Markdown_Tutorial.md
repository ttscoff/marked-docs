<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## マークダウンとは何ですか? [what-is-markdown]

Markdown は、読みやすく書きやすいプレーン テキスト形式を使用して記述し、構造的に有効な HTML に変換できる軽量のマークアップ言語です。 Markdown の書式設定構文の最も重要な設計目標は、構文をできるだけ読みやすくすることです。

## 基本的な構文 [basic-syntax]

### ヘッダー [headers]

ハッシュ記号 (`#`) を使用してヘッダーを作成します。ハッシュの数によってヘッダー レベルが決まります。

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### 強調 [emphasis]

**太字テキスト** 二重アスタリスクまたは二重アンダースコアを使用:

```markdown
**Bold text**
__Bold text__
```

単一のアスタリスクまたは単一のアンダースコアを使用した *斜体のテキスト*:

```markdown
*Italic text*
_Italic text_
```

### リスト [lists]

**アスタリスク、プラス記号、またはハイフンを使用した順序なしリスト**:

```markdown
* Item 1
* Item 2
* Item 3

+ Item 1
+ Item 2
+ Item 3

- Item 1
- Item 2
- Item 3
```

**順序付きリスト** 数字の後にピリオドが続くもの:

```markdown
1. First item
2. Second item
3. Third item
```

### リンク [links]

**インライン リンク**。角括弧内のテキストと括弧内の URL が含まれます。

```markdown
[Link text](http://example.com)
```

**参考リンク**。角括弧内のテキストと角括弧内の参照が含まれます。

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**自動リンク**: URL を山括弧で囲みます:

```markdown
<http://example.com>
<user@example.com>
```

### 画像 [images]

画像はリンクと同様の構文を使用しますが、先頭に感嘆符が付いています。

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### ブロック引用符 [blockquotes]

各行の先頭に大なり記号 (`>`) を使用してブロック引用符を作成します。

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### コード [code]

バッククォートを使用した **インライン コード**:

```markdown
Use ⟦4⟧ in your text.
```

**コード ブロック** は、4 つのスペースまたは 1 つのタブでインデントします。

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### 横罫線 [horizontal-rules]

3 つ以上のハイフン、アスタリスク、またはアンダースコアを使用して水平罫線を作成します。

```markdown
---

***

___
```

### 改行 [line-breaks]

**ハード改行**は、行を 2 つ以上のスペースで終了します。

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Enter キーを押すだけでソフト改行** (HTML 内にスペースが作成されます):

```markdown
This line
continues on the next line with a space.
```

### エスケープ文字 [escaping-characters]

バックスラッシュを使用して特殊文字をエスケープします。

```markdown
\*This text is not italic\*
\[This is not a link\]
```

エスケープできる一般的な文字:
- `\` バックスラッシュ
- `` ` `` バッククォート
- `*` アスタリスク
- `_` アンダースコア
- `{}` 中括弧
- `[]` 角括弧
- `()` かっこ
- `#`ハッシュ
- `+`プラス
- `-` マイナス
- `.`期
- `!` 感嘆符

## ベストプラクティス [best-practices]

1. **空白行を使用**して、読みやすくするためにさまざまな要素を区切ります
2. **書式設定の選択に一貫性を保つ** (例: 強調には `*` または `_` を使用します)
3. **シンプルにしてください** - マークダウンはプレーンテキストとして読めるように設計されています
4. **出力をテスト**して、期待どおりにレンダリングされることを確認します
5. **「ここをクリック」のような一般的なフレーズの代わりに、意味のあるリンク テキストを使用します**

## 一般的なパターン [common-patterns]

### ネストされたリスト [nested-lists]

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### 段落のあるリスト [lists-with-paragraphs]

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### 他の要素を含むブロック引用符 [blockquotes-with-other-elements]

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## 概要 [summary]

Markdown は、HTML に簡単に変換できるテキストをフォーマットするためのシンプルで読みやすい方法を提供します。重要なのは、基本的な構文要素を一貫して使用しながら、シンプルで読みやすいものに保つことです。練習すると、Markdown が自然になり、構造化されたコンテンツを書くのがはるかに簡単になることがわかります。

---

*このチュートリアルでは、元の仕様で定義されているコアの Markdown 構文について説明します。より高度な機能については、CommonMark (GFM)、MultiMarkdown、GitHub Flavored Markdown などの特定の Markdown プロセッサのドキュメントを参照してください。*