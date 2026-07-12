<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

CDN から、または生のコードを貼り付けることで、独自の JavaScript を含めることができます。

## マークされた導体に関する注意

ドキュメントの種類や場所によって異なるカスタム JavaScript を実装する最も簡単な方法は、[Marked Conductor][conductor] を使用することです。 YAML 構成を使用して、「フィルター」を使用してスクリプトを追加できるようになります。詳細については [Conductor ページ][conductor] を、例については [sample config][sample config] を参照してください。

[conductor]: https://brettterpstra.com/projects/conductor/
[sample config]: https://github.com/ttscoff/conductor-config/

## CDN からの JavaScript の追加 [cdns]

![][1]

   [1]: 画像/スクリーンショット/AdditionalJavascript.jpg @2x width=592px height=576px class=center

{% prefspane Style %} からアクセスできる「追加スクリプト」ウィンドウで JavaScript CDN URL を追加できます。 CDN URL を 1 行に 1 つずつ入力します。 `<script>` タグは含めず、URL のみを含めます。

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
https://cdn.jsdelivr.net/npm/micromark-extension-gfm-strikethrough@2.1.0/lib/html.min.js
```

> jQuery はすでにプレビュー ウィンドウに含まれていることに注意してください。

これらのスクリプトは、プレビューの最後、ドキュメント タグの前に挿入されます。 init 関数を呼び出す必要がある場合、またはプレビューが実行されるたびに更新する必要がある場合は、[Raw JavaScript を含む](#rawjs) を参照してください。 DOM を検査し、マークされたライブ プレビューでこれらのスクリプトをデバッグするには、[WebKit Inspector](Writing_Custom_CSS.html#webkitinspector) で説明されているように Safari の Web Inspector をアタッチできます。


### Raw JavaScript を含む [rawjs]

[追加スクリプト] ウィンドウの下部のテキスト フィールドに、生の JavaScript を挿入できます。これは `<script></script>` ペアに含まれるため、入力に含めないでください。このフィールドには、組み込まれたライブラリの初期化、DOM 変更の実行、または WebKit ビュー内で実行するために必要な JavaScript コマンドを含めることができます。 DOM 操作を容易にするために、jQuery がすでに組み込まれています。

これらのスクリプトは、ウィンドウが最初に読み込まれるときにのみ実行されます。プレビューが更新されると、DOM の一部を置き換えることによって適切に更新されるため、更新されたコンテンツに対して動作する必要があるスクリプトは、[フック](Embedding_Scripts.html#hooks) を使用して更新する必要があります。

生の JavaScript フィールドに次のような呼び出しを含めます。

```javascript
Marked.hooks.register('update', function() { myCustomFunction(); });
```
