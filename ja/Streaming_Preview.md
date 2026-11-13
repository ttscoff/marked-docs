<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% appmenu File, New, Streaming Preview %} を開くと、Marked はディスク上のファイルを監視する代わりに、名前付きペーストボードを介してライブ更新を受け取ります。ソース アプリは Marked と統合する必要があります。

[Curio](Curio.html)、[Drafts](Drafts.html)、および [The Archive](The_Archive.html) と [Traverse](Traverse.html) では、独自のトグルとメニュー コマンドが文書化されています。 nvUltra、nvALT、Bear などは同じチャネルを使用します。Marked でストリーミング プレビューを開き、エディターで統合を有効にして、入力を開始します。更新はほぼリアルタイムで届きます。

## 開発者 [developers]

ストリーミング プレビューをアプリと統合するには、プレビューするマークダウン テキストを名前付きクリップボードに置くだけです。次のコード (Objective-C) を使用して更新します (できれば、didEndEditing メソッドまたは調整された間隔で)。

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### 送信元アプリと形式を宣言する [declaring-the-origin-app-and-format]

送るテキストの先頭で、HTML コメントにキーワード `source` または `format` を置きます。Marked はそのコメントを読み、プレビューから取り除くので、メモは GFM と MultiMarkdown のプロセッサと互換のままです。コロンの後の空白は省略できます（`source:Bear.app` と `source: Bear.app` は同じです）。キーワードの大文字と小文字は区別しません。

どちらの値も自由な文字列です。一部には Marked の組み込みの動作があり、すべての値は [Custom Processor](Custom_Processor.html)（Conductor）の **ストリーミングプレビューのソース** と **ストリーミングプレビューの形式** として使えます。これらの条件は **等しい**、**等しくない**、**含む**、**含まない** を受け付けます。

**`source: APP_NAME`** は送信元アプリを、アプリ名または bundle id で示します。Marked はこれで、そのアプリ向けの特別な処理を加えます。`source: Bear.app` と `source: Drafts.app` は、それらのアプリのプレビュー動作を有効にします。それ以外の名前も Conductor のルールで照合できるので、そのアプリ向けの処理を自分で実行できます。

```html
<!--source:Bear.app-->
```

**`format: fountain`** は [Fountain](Fountain_for_Screenwriters.html) の処理を有効にし、ストリームを Markdown ではなく脚本としてプレビューします。それ以外の形式の値はプロセッサを変えません。Conductor のルールが照合するためのものです。たとえば **ストリーミングプレビューの形式** `等しい` `fountain` です。

```html
<!--format:fountain-->
```

1 つのコメントに両方のキーワードを置けます。

```html
<!--
source: Bear.app
format: fountain
-->
```

### プログラムでストリーミング プレビューを開く [opening-the-streaming-preview-programatically]

アプリは、`x-marked-3://stream/` URL ハンドラー メソッドを使用してプログラムでストリーミング プレビューを開くことができます。このメソッドは、完了時にアクティブ化するアプリのバンドル ID を渡すことができる `x-success` パラメーターも受け入れます。