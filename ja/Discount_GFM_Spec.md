<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

[Markdown Dingus](x-marked-3://dingus?processor=discount) をチェックして、割引プロセッサを試してください。

## 割引 GFM とは何ですか? [what-is-discount-gfm]

割引 GFM (GitHub Flavored Markdown) は、GitHub の拡張 Markdown 構文を実装する C ベースの Markdown プロセッサです。これはオリジナルのDiscountライブラリに基づいていますが、テーブル、タスクリスト、取り消し線テキスト、自動URLリンクなどのGitHub固有の機能で強化されています。

## 主な特徴 [key-characteristics]

- **C ベースのパフォーマンス**: 最適なパフォーマンスを実現する高速なネイティブ C 実装
- **GitHub 互換性**: 互換性を最大限に高めるために GitHub の Markdown 拡張機能を実装します。
- **軽量**: 最小限の依存関係と小さいフットプリント
- **拡張可能**: さまざまな Markdown 拡張機能とカスタム オプションをサポート
- **HTML5 サポート**: 適切なセマンティック マークアップを使用して最新の HTML5 出力を生成します。

## 標準マークダウンとの主な違い [major-differences-from-standard-markdown]

### 1. **GitHub 風味のマークダウン拡張機能** [1-github-flavored-markdown-extensions]

**テーブル**

- 配置オプションを備えた GitHub スタイルのテーブルの完全サポート
- 適切な HTML テーブル構造を備えたヘッダー、セパレーター、データ行
- 区切り行にコロン (`:`) を使用した列の配置

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**タスクリスト**

- リスト内の GitHub スタイルのチェックボックスのサポート
- インタラクティブなチェックボックス (HTML 入力要素としてレンダリング)
- チェックされた状態とチェックされていない状態の両方がサポートされています

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**取り消し線のテキスト**

- 二重チルダ (`~~`) で囲まれたテキストは取り消し線になります
- セマンティック マークアップに HTML `<del>` タグを使用します
- 強調のため複数のチルダをサポート

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **強化されたコード ブロックのサポート** [2-enhanced-code-block-support]

**フェンスで囲まれたコードブロック**

- コードブロックのトリプルバックティック (```` ``` ````)
- 構文強調表示の言語仕様
- インデントは必要ありません (標準のマークダウンとは異なります)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatic Language Detection**

- Support for many programming languages
- Proper syntax highlighting when supported
- Fallback to plain text for unsupported languages

### 3. **Automatic URL Linking** [3-automatic-url-linking]

**URL Autolinking**

- Automatic conversion of URLs to clickable links
- Support for http, https, and ftp protocols
- Email addresses automatically converted to mailto links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**スマートリンク検出**

- 明示的なマークアップなしで URL を認識します
- さまざまな URL 形式とプロトコルを処理します
- 設定可能なリンク安全オプション

### 4. **高度なリスト機能** [4-advanced-list-features]

**アルファベット順リスト**

- アルファベットのマーカー (a、b、c など) が付いた順序付きリスト
- アルファベットの自動進行
- 適切な HTML `<ol type="a">` 出力

```markdown
a. First item
b. Second item
c. Third item
```

**強化されたリスト処理**

- ネストされたリストの処理の改善
- 間隔とインデントの改善
- 混合リストタイプのサポート

### 5. **脚注のサポート** [5-footnotes-support]

**参考文献形式の脚注**

- 自動脚注番号付け
- `[^1]` 構文による参照リンク
- 文書末尾の脚注の定義

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**脚注の自動処理**

- 適切な HTML 脚注構造を生成します
- 参照と定義の間のリンク
- ドキュメント全体に連番を付ける

### 6. **HTML の統合** [6-html-integration]

**HTML5 のサポート**

- 完全な HTML5 タグ認識
- 適切なセマンティックマークアップの生成
- 最新の HTML 構造と属性

**生の HTML ブロック**

- マークダウン内の HTML のサポート
- 適切なエスケープとサニタイズ
- マークダウン構文との統合

### 7. **強化された強調ルール** [7-enhanced-emphasis-rules]

**リラックスした強調**

- 単一のアンダースコア (`_`) は単語の途中で強調されません。
- コードと技術的な内容の文書化に適しています
- 識別子の不要な強調を防止します

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**複数の強調レベル**

- 太字、斜体、および複合強調のサポート
- 標準のマークダウン強調ルールとの一貫性
- `<strong>` タグと `<em>` タグを使用した適切な HTML 出力

### 8. **目次の生成** [8-table-of-contents-generation]

**自動目次**

- 見出しから目次を生成します
- 見出しレベルに基づく階層構造
- 構成可能な TOC 生成オプション

**見出し ID の生成**

- 見出しのID自動生成
- 簡単にナビゲーションできるアンカーリンク
- 一貫した ID 形式

## 割引 GFM と他のマークダウン フレーバー [discount-gfm-vs-other-markdown-flavors]

|特集 |割引 |コモンマーク (GFM) |クラムダウン |マルチマークダウン |標準 |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
|テーブル |はい |いいえ |はい |はい |いいえ |
|取り消し線 |はい |いいえ |いいえ |はい |いいえ |
|タスクリスト |はい |いいえ |いいえ |はい |いいえ |
|フェンスで囲まれたコード |はい |はい |はい |はい |いいえ |
|数学 |いいえ |いいえ |はい |はい |いいえ |
|脚注 |はい |いいえ |はい |はい |いいえ |
|定義リスト |いいえ |いいえ |はい |はい |いいえ |
|略語 |いいえ |いいえ |はい |いいえ |いいえ |
|属性リスト |いいえ |いいえ |はい |いいえ |いいえ |
|拡張機能 |限定 |いいえ |はい |はい |いいえ |
|タイポグラフィ |基本 |いいえ |はい |いいえ |いいえ |
|オートリンク |はい |いいえ |いいえ |いいえ |いいえ |
|アルファベット順リスト |はい |いいえ |いいえ |いいえ |いいえ |

## 割引 GFM の主な利点 [key-advantages-of-discount-gfm]

1. **GitHub 互換性**: GitHub で動作する必要があるコンテンツに最適
2. **パフォーマンス**: 高速な C ベースの実装
3. **シンプルさ**: 複雑さを排除し、GitHub のコア機能に重点を置いています。
4. **信頼性**: 安定した、十分にテストされた実装
5. **標準への準拠**: GitHub の Markdown 仕様に従います。
6. **軽量**: リソースの使用量と依存関係を最小限に抑える

## 一般的な使用例 [common-use-cases]

**GitHub ドキュメント**

- README ファイルとプロジェクト ドキュメント
- GitHub ページとウィキ
- 発行リクエストとプルリクエストの説明

**テクニカル ライティング**

- コードのドキュメントとチュートリアル
- APIドキュメント
- 技術仕様

**コンテンツ管理**

- ブログ投稿と記事
- ドキュメント Web サイト
- 知識ベース

**共同編集**

- チームのドキュメント
- プロジェクト計画書
- 会議のメモと議事録

## 構成オプション [configuration-options]

割引 GFM はさまざまな構成オプションをサポートしています。

- **自動リンク**: 自動 URL 検出を有効/無効にします。
- **脚注**: 脚注の処理を制御します
- **目次**: TOC 生成設定
- **HTML の安全性**: リンクの検証とサニタイズ
- **厳密モード**: 強化された解析ルール
- **スマート見積もり**: 自動見積もり変換

## 実装の詳細 [implementation-details]

**パーサー オプション**

- `kGHMarkdownAutoLink`: 自動 URL リンクを有効にする
- `kGHMarkdownFootnotes`: 脚注処理を有効にする
- `kGHMarkdownTOC`: 目次の生成を有効にする
- `kGHMarkdownSafeLinks`: リンクを安全なプロトコルに制限する
- `kGHMarkdownNoHTMLTags`: HTMLタグ処理を無効にします

**出力機能**

- HTML5 セマンティック マークアップ
- 適切な見出し階層
- アクセス可能なテーブル構造
- クリーンで有効な HTML 出力

## ベストプラクティス [best-practices]

1. **テーブルの使用は控えめに**: テーブルは強力ですが、保守が複雑になる場合があります。
2. **タスク リストの活用**: プロジェクト管理と文書化に最適
3. **オートリンクを利用する**: プロセッサに URL 変換を自動的に処理させます
4. **見出しを含む構造**: 適切な見出し階層を使用して目次をより適切に生成します
5. **GitHub でテスト**: GitHub のレンダリングとの互換性を確認します

## 標準マークダウンからの移行 [migration-from-standard-markdown]

ほとんどの標準的な Markdown は、変更を加えることなく、Discount GFM で動作します。 GFM 機能を活用するには:

1. **テーブルの追加**: データを GitHub スタイルのテーブル形式に変換します
2. **タスク リストを使用**: 必要に応じて箇条書きをチェックボックスに置き換えます。
3. **取り消し線を有効にする**: 取り消し線を引いたコンテンツには `~~text~~` を使用します
4. **自動リンクの活用**: 単純な URL の手動リンク マークアップを削除します。
5. **構造見出し**: 目次生成のために適切な見出し階層を確保する

## リソース [resources]

- [GitHub フレーバーマークダウン仕様](https://github.github.com/gfm/)
- [割引ライブラリドキュメント](https://www.pell.portland.or.us/~orc/Code/discount/)
- [GitHub マークダウン ガイド](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [マークダウンチートシート](https://www.markdownguide.org/cheat-sheet/)

---

*このドキュメントでは、Marked で実装されているディスカウント GFM について説明します。最新の情報については、常に公式の GitHub Flavored Markdown 仕様を参照してください。*