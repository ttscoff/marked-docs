<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

{% appmenu File, New, Streaming Preview %} を開くと、Marked はディスク上のファイルを監視する代わりに、名前付きペーストボードを介してライブ更新を受け取ります。ソース アプリは Marked と統合する必要があります。

[Curio](Curio.html)、[Drafts](Drafts.html)、および [The Archive](The_Archive.html) では、独自のトグルとメニュー コマンドが文書化されています。 nvUltra、nvALT、Bear などは同じチャネルを使用します。Marked でストリーミング プレビューを開き、エディターで統合を有効にして、入力を開始します。更新はほぼリアルタイムで届きます。

## 開発者 [developers]

ストリーミング プレビューをアプリと統合するには、プレビューするマークダウン テキストを名前付きクリップボードに置くだけです。次のコード (Objective-C) を使用して更新します (できれば、didEndEditing メソッドまたは調整された間隔で)。

```obj-c
NSString *rawString = @"the text to process";
// pasteboard *must* be named 'mkStreamingPreview'
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb setString:rawString forType:(NSString*)kUTTypeUTF8PlainText];
```

### 相対アセットのベース URL の宣言 [declaring-a-base-url-for-relative-assets]

ストリーミング プレビューのベース URL を指定することもでき、画像やその他のアセット内の相対 URL がソース アプリ内と同様に機能できるようになります。ベース URL にファイル名が含まれている場合、その名前と拡張子はカスタム プロセッサで使用できるようになりますが、必須ではありません。ベース URL を含めるには、NSURL オブジェクトをクリップボードに入れるだけです。

```obj-c
NSString *rawString = @"The text to be processed\\n\\n![](images/screenshots/mainwindow-feature-stats.jpg)";
NSURL *baseURL = [NSURL fileURLWithPath:@"/Users/username/Documents/HelpDocs/Main Window.md"];
NSPasteboard* pb = [NSPasteboard pasteboardWithName:@"mkStreamingPreview"];
[pb clearContents];
[pb writeObjects:@[rawString, baseURL]];
```

または、Swift では次のようになります。

```swift
let rawString = "The text to be processed\n\n![](images/screenshots/mainwindow-feature-stats.jpg)"
let baseURL = URL(fileURLWithPath: "/Users/username/Documents/HelpDocs/Main Window.md")
let pb = NSPasteboard(name: "mkStreamingPreview")
pb.clearContents()
pb.writeObjects([rawString, baseURL])
```

Mac App Store バージョンの Marked が使用されており、サンドボックス経由でベース URL にアクセスできない場合は、URL が初めてプレビューに読み込まれるときに許可が要求されます。

### ソース アプリケーションの宣言 [declaring-the-source-application]

アプリは、`source` メタデータ行を含めることで、自身をプレビュー コンテンツのソースとして宣言することもできます。これは通常、GFM プロセッサと MultiMarkdown プロセッサの両方との互換性を可能にするために HTML コメント内で実行されます。アプリの名前またはバンドル ID を指定するだけです。

```html
<!--
source: Bear.app
-->
```

### プログラムでストリーミング プレビューを開く [opening-the-streaming-preview-programatically]

アプリは、`x-marked-3://stream/` URL ハンドラー メソッドを使用してプログラムでストリーミング プレビューを開くことができます。このメソッドは、完了時にアクティブ化するアプリのバンドル ID を渡すことができる `x-success` パラメーターも受け入れます。