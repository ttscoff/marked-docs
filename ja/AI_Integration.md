<!-- MT-DRAFT: machine translation; human review required -->
# <%= @title %>

LLM エージェントに skill ファイルを渡すと、Marked でファイルやフォルダを開き、設定のセクションへ移動し、環境設定を変更できます。エージェントは Marked の [URLハンドラー](URL_Handler.md) を使います。別のプラグインやサーバーは不要です。

## skill をダウンロードする [download-the-skill]

{% download "SKILL.md" "Marked でファイルを開き、環境設定を変更するためのエージェント skill です。ファイル名は SKILL.md のまま保存してください。" %}

このファイルは、エージェントが動作する前に読む短いヘッダを持つプレーンな Markdown です。skill または常設の指示を受け付けるエージェントなら、同じファイルを渡せます。

## インストールする [install-it]

skill の名前を付けたフォルダに置き、ファイル名は `SKILL.md` のままにします。

Cursor では、次のどちらの場所でも使えます。

```
~/.cursor/skills/open-in-marked/SKILL.md
```

```
.cursor/skills/open-in-marked/SKILL.md
```

1 つ目はすべてのプロジェクトで使えます。2 つ目はそのプロジェクトだけに適用されます。skill 用のフォルダがないエージェントは、同じ文章をプロジェクトの指示として使えます。

インストールしたあと、エージェントに Marked でファイルまたはフォルダを開くよう頼んでください。次のようなコマンドを実行するはずです。

```bash
open "x-marked-3://open?file=/Users/me/Notes/draft.md"
```

フォルダも同じコマンドです。パスは既に存在している必要があり、空白やその他の予約文字はパーセントエンコードします。refresh、Streaming Preview、コールバックを含む完全なスキームは [URLハンドラー](URL_Handler.md) を参照してください。

## 環境設定 [preferences]

この skill は、環境設定用のコマンドも 2 つ扱います。

`pref`
: 名前を指定したセクションで設定を開きます。URL 内の名前は英語のままです。たとえば `Preview` や `Style` です。値は変更しません。

`defaults`
: Marked がすでに保存している環境設定を書き、開いているプレビューを再読み込みします。プレビューをそのままにするには `refresh=0` を渡します。未知のキーは無視されるため、エージェントは書き込む前に現在の環境設定を読む必要があります。

```bash
open "x-marked-3://pref?page=Preview"
open "x-marked-3://defaults?syntaxHighlight=0&refresh=0"
```

## 関連項目 [related]

[エージェントティックコーディングによるマークの使用](Using_Marked_with_Agentic_Coding.md) では、エージェントが計画やメモを書いているあいだ、そのフォルダを Marked で監視する方法を説明しています。[コマンドラインユーティリティ](Command_Line_Utility.md) は、エージェントを使わず、シェルから同じ種類の操作を行います。
