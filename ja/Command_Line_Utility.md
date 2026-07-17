<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

`mk` コマンド ライン ツールを使用すると、ターミナルから Marked の機能に簡単にアクセスでき、ワークフローの自動化や、シェル スクリプトや他のコマンド ライン ツールとの統合が可能になります。

## インストール [installation]

`mk` をインストールする推奨方法は Homebrew を使用することです。

```bash
brew tap ttscoff/thelab
brew install ttscoff/thelab/mk
```

Homebrew を使用しない場合は、署名付きパッケージをダウンロードしてインストールします。

{% download "https://github.com/ttscoff/mk/releases/latest/download/mk.pkg" "Signed PKG installer for mk. Double-click to launch Installer and follow the prompts." %}

`mk.pkg` をダウンロードしたら、それをダブルクリックし、インストーラーのプロンプトに従います。

## 基本的な使い方 [basic-usage]

### ファイルを開く [opening-files]

コマンド ラインから Marked でマークダウン ファイルを開きます。

```bash
mk file.md
mk ~/Documents/notes.md
mk --raise document.md  # Open and raise window above all others
```

### STDIN からのコンテンツのストリーミング [streaming-content-from-stdin]

コンテンツを Marked のストリーミング プレビューに直接ストリーミングします。

```bash
echo "# Hello World" | mk
cat notes.md | mk
mk -  # Explicitly use STDIN
```

[ストリーミング プレビュー] ウィンドウが開き、他のコマンドからパイプされたコンテンツがリアルタイムで表示されます。

## コマンドリファレンス [command-reference]

### ファイル操作 [file-operations]

**`mk [file]`** — Marked でマークダウン ファイルを開く

**`mk [file] --raise`** — ファイルを開き、ウィンドウを他のウィンドウよりも上に上げます

### STDIN とストリーミング [stdin-and-streaming]

**`mk`** または **`mk -`** — STDIN から読み取り、ストリーミング プレビューを開きます

**`mk --stream`** — STDIN を読み取らずにストリーミング プレビュー ウィンドウを開きます

### プレビュー管理 [preview-management]

**`mk --refresh`** — 最前面のプレビュー ウィンドウを更新します

**`mk --refresh all`** — 開いているすべてのプレビュー ウィンドウを更新します

**`mk --refresh file.md`** — 特定のファイルのプレビューを更新します (開いている場合)

### 設定 [preferences]

**`mk --pref`** — マークされた設定を開く ([全般] ページ)

**`mk --pref Advanced`** — 特定のページの設定を開きます

**`mk --defaults KEY=VALUE [KEY=VALUE...]`** — ユーザー設定を設定します (複数のペアが許可されます)

```bash
mk --defaults syntaxHighlight=1 includeMathJax=0 processor=multimarkdown
```

### スタイル管理 [style-management]

**`mk --style NAME`** — 開いているウィンドウのプレビュー スタイルを設定する

**`mk --add-style FILE`** — CSS ファイルをカスタム スタイルとしてマーク付きに追加します

```bash
mk --add-style ~/Styles/custom.css
```

### JavaScriptの実行 [javascript-execution]

**`mk --dojs "JAVASCRIPT_COMMAND"`** — 最前面のウィンドウで JavaScript を実行します

**`mk --dojs "SCRIPT" all`** — すべてのウィンドウで JavaScript を実行します

**`mk --dojs "SCRIPT" file.md`** — 特定のファイルで JavaScript を実行する

```bash
mk --dojs "window.scrollTo(0,0)"
mk --dojs "alert('Hello')" all
```

### コンテンツの抽出とインポート [content-extraction-and-import]

**`mk --extract URL`** — URL からコンテンツを抽出し、マーク付きで開きます

```bash
mk --extract https://example.com/article
```

**`mk --importurl [URL]`** — URL のインポート ウィンドウを開きます (オプションで URL を指定)

**`mk --stylestealer [URL]`** — オープン スタイル スティーラー HUD (オプションで URL 付き)

### ユーティリティコマンド [utility-commands]

**`mk --paste`** — クリップボードから新しいドキュメントを作成

**`mk --preview TEXT`** — 新しいドキュメントでテキストを直接プレビューする

**`mk --dingus`** — プロセッサーをテストするための Open Markdown Dingus

**`mk --help`** または **`mk -h`** — 使用状況情報を表示

**`mk --version`** または **`mk -v`** — バージョン情報を表示します

## 例 [examples]

```bash
# Open a file
mk document.md

# Stream markdown from a file
cat notes.md | mk

# Process and preview
grep -i "important" notes.md | mk

# Refresh all previews
mk --refresh all

# Add a custom style
mk --add-style ~/Documents/MyTheme.css

# Set preferences
mk --defaults syntaxHighlight=1 processor=multimarkdown

# Run JavaScript in all windows
mk --dojs "window.scrollTo(0,0)" all

# Extract content from a webpage
mk --extract https://blog.example.com/article

# Preview text directly
mk --preview "## Hello\n\nThis is **markdown** text!"
```

## 統合 [integration]

### シェルエイリアス [shell-aliases]

`~/.zshrc` または `~/.bash_profile` に追加:

```bash
alias mko='mk --raise'      # Open with raise
alias mkr='mk --refresh all' # Refresh all
```

### スクリプト [scripts]

自動化のためのシェル スクリプトで `mk` を使用します。

```bash
#!/bin/bash
# Watch a file and stream changes to Marked
fswatch -o document.md | while read; do
  cat document.md | mk
done
```

### ワークフロー [workflows]

他のツールと組み合わせる:

```bash
# Convert clipboard to markdown and preview
pbpaste | markdown | mk

# Search and preview
grep -r "TODO" . | head -20 | mk
```

## オープンソース [open-source]

`mk` コマンドライン ツールはオープン ソースであり、GitHub で入手できます。

**https://github.com/ttscoff/mk**

次のことができます。
- ソースコードを表示する
- 改善に貢献する
- 問題を報告する
- 必要に応じてソースからビルドする

このツールは Swift で書かれており、Xcode を使用してコンパイルできます。ビルド手順については、[README](https://github.com/ttscoff/mk) を参照してください。

## バージョン [version]

インストールされている `mk` のバージョンを次のコマンドで確認します。

```bash
mk --version
```

## 関連機能 [related-features]

- Marked の URL スキームの詳細については、[URL ハンドラー](URL_Handler) を参照してください。
- ストリーミングプレビュー機能の詳細については、「ストリーミングプレビュー」(Streaming_Preview)を参照してください。
- 自動化の例については、「ワークフロー統合」(Workflow_Integration) を参照してください。