<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

**Marked Quick Look** は、Markdown およびプレーンテキスト ファイル用の Quick Look プレビュー拡張機能を追加する別の Mac App Store アプリです。 Finder でスペースバーを押すと (または macOS がサポートする場合はどこでも Quick Look を使用して)、生のソースではなくスタイル付きの HTML プレビューが表示されます。

Marked Quick Look は **Marked 3 には含まれていません**。これは別途購入する必要があります (Mac App Store で **$4.99**)。 <!-- MAS リンク: 利用可能な場合は、ここに App Store URL を追加します -->

I> Marked Quick Look と Marked 3 は独立した製品です。 Marked を購入しても Quick Look 拡張機能はインストールされません。また、Marked Quick Look を購入しても Marked ライセンスは含まれません。 Marked がインストールされている場合、プレビューにはオプションの **Open in Marked** ボタンが含まれます。

## 得られるもの

Marked Quick Look は、`.md`、`.markdown`、`.mmd`、および多くのプレーンテキスト ファイルを同じ視覚的に洗練された状態でレンダリングする **Quick Look Preview 拡張機能**を登録します。Marked は次のことで知られています。

- **Apex 処理** — CommonMark、GitHub Flavored Markdown、MultiMarkdown、Kramdown、および複数のフレーバーの機能を組み合わせる **Unified** モードをサポートするオープンソースの Markdown プロセッサである [Apex](https://github.com/ApexMarkdown/apex) を利用
- **マークされたプレビュー スタイル** — 9 つの組み込みテーマ (デフォルトでは GitHub) とカスタム CSS インポート
- **構文の強調表示**、**MathJax**、**Mermaid** の図 (バンドルされたスクリプト、ネットワークは不要)
- **CriticMarkup** マークアップ ビュー
- **マークで開く** — マークがインストールされている場合、クイック ルックからマークの完全なプレビューにジャンプします

W> Quick Look プレビューは読み取り専用です。ファイル インクルード (`<<[file]`、`{{file}}`、および同様の構文) は、Quick Look では**展開されません**。これらは強調表示されたプレースホルダー (`Included file: path`) として表示されるため、コンテンツがどこに取り込まれるかを確認できます。完全なマルチファイル レンダリングの場合は、「マーク」でドキュメントを開きます。

## インストール

1. Mac App Store から **マークされた Quick Look** をインストールします。
2. `/Applications` から **アプリを 1 回起動**します。これにより、Quick Look 拡張機能が macOS に登録されます。
3. Finder で Markdown ファイル上で **スペースバー** を押してプレビューします。

コンテナ アプリには **設定** ウィンドウ ({% kbd cmd %}、{% kbd , %}) が含まれており、Apex プロセッサ モード、プレビュー スタイル、構文強調表示のテーマ、MathJax と Mermaid の切り替えを選択できます。

## Apex および Markdown フレーバー

マークされた Quick Look はすべてのレンダリングに [Apex](https://github.com/ApexMarkdown/apex) を使用します。 Apex はスタンドアロン プロセッサとして開発されており、Marked 3 にも組み込まれています。

[設定] で、執筆スタイルに合わせて **Apex モード**を選択します。

|モード |こんな方に最適 |
| --- | --- |
| **統合** (デフォルト) |フレーバー間での混合 Markdown 機能 |
| **コモンマーク** |厳密な CommonMark |
| **GFM** | GitHub 風味のマークダウン |
| **マルチマークダウン** |メタデータ、トランスクルージョン、脚注 |
| **クラムダウン** | Kramdown スタイルの拡張機能 |

統合モードは、ほとんどのドキュメントにとって最適なデフォルトです。ファイルが特定のプロセッサ用に書き込まれ、予期せずレンダリングされる場合は、モードを切り替えます。

## マーク付きで開く

Marked 3 がインストールされている場合、Quick Look プレビューのツールバーに **Open in Marked** ボタンが表示されます。これをクリックすると、ライブ プレビュー、エクスポート、校正、および完全なインクルード拡張のためにファイルがマーク済みに渡されます。

Marked がインストールされていない場合、ボタンは無効になっているように見えます。

## Quick Look の競合のトラブルシューティング

macOS では、複数のアプリが Markdown の Quick Look プレビュー拡張機能を登録できます。各プレビューを処理できる拡張機能は 1 つだけであり、**別のアプリのプラグインが Marked Quick Look よりも優先される場合があります**。

### どの拡張機能がアクティブであるかを確認する方法

マーク付きクイック ルック プレビューには、このオプションが有効になっている場合、**マーク付きで開く** ツールバーが含まれます。別のレイアウト、生の等幅ソース、または別のアプリのスタイルが表示される場合は、おそらく別の Quick Look ハンドラーが優先されます。

### マークされた Quick Look の優先順位を復元する

インストールまたは更新した後、または Quick Look キャッシュをリセットした後、次の手順を実行します。

1. **マークされた Quick Look** を `/Applications` から 1 回起動します (開発ビルドをテストしている場合は、Xcode から実行します)。
2. ターミナルで、拡張子を登録して優先します。

```bash
pluginkit -a "/Applications/Marked Quick Look.app/Contents/PlugIns/MarkedQuickLookPreview.appex"
pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview
```

3. Quick Look サービスをリセットします。

```bash
killall quicklookd QuickLookUIService 2>/dev/null
```

4. `.md` ファイルで **スペースバー** をもう一度押します。

キャッシュされたプレビューをクリアするには:

```bash
qlmanage -r cache
```

### 競合する拡張機能を一時的に無効にする

別のアプリが Marked Quick Look をオーバーライドしていることを確認するには、`pluginkit -e ignore -i BUNDLE_ID` でその拡張機能を無効にし、ファイルをプレビューして、`pluginkit -e default -i BUNDLE_ID` で復元します。

例 — **Folder Quick Look** の Markdown 拡張機能を無効にします。

```bash
pluginkit -e ignore -i studio.appahead.AA7.Markdown-Quick-Look-Extension
```

### 一般的な競合するアプリ

これらのアプリ (およびその他) は、`.md` ファイルを処理できる Quick Look プレビュー拡張機能を登録します。

|アプリ |バンドル ID (プレビュー拡張機能) |
| --- | --- |
| **フォルダーのクイックルック** | `studio.appahead.AA7.Markdown-Quick-Look-Extension` |
| **QLMarkdown** | `org.sbarex.QLMarkdown.QLExtension` |
| **覗く** | `com.bigzlabs.peek.peekextension` |
| **ハイランド プロ** | `com.quoteunquoteapps.highland.pro.qlplugin` |
| **クマ** | `net.shinyfrog.bear.Bear-Quicklook-Extension` |
| **ユリシーズ** | `com.soulmen.ulysses-setapp.quicklookextension` (アプリ設定) / `com.soulmen.ulysses.quicklookextension` |
| **下書き** | `com.agiletortoise.Drafts-OSX.Drafts-OSX-QuickLookPreview` |
| **書士** | `com.literatureandlatte.scrivener3.ScrivQuickLook` |
| **ブラックインク** | `com.red-sweater.blackink2.quicklook` |

W> **iA Writer** は、インストール時に独自の UTI (`net.ia.markdown`) を `.md` ファイルに割り当てます。マークされた Quick Look 1.0.2+ は、その UTI を処理します。 **Folder Quick Look**、**QLMarkdown**、**Peek** も頻繁に競合の原因となります。

登録されているプレビュー拡張機能を一覧表示します。

```bash
pluginkit -m -D -p com.apple.quicklook.preview -A -v | grep -i MarkedQuickLook
```

W> マークされたクイックルックを確認するために `markdown` を grep しないでください。バンドル ID は `com.brettterpstra.MarkedQuickLook.preview` で、「マークダウン」という単語は含まれません。 `grep -i markdown` は、Marked Quick Look がインストールされ有効になっている場合でも、結果を返さないことがあります。他の Markdown ハンドラーをリストするには、grep を使用せずに完全な `pluginkit` コマンドを実行するか、上記の表の特定のバンドル ID に対して grep を実行します。

`+` のマークが付いた拡張機能は明示的に有効になっています。 `pluginkit -e use -i com.brettterpstra.MarkedQuickLook.preview` を使用して、Marked Quick Look を前面に移動します。

### まだプレーンテキストが表示されますか?

プレビューに **スタイルされていない等幅ソース**が表示される場合、ファイルの UTI に一致するプレビュー拡張子がないため、macOS は組み込みの **Text.qlgenerator** にフォールバックします。

1. `pluginkit ... | grep -i MarkedQuickLook` (`markdown` ではありません) で登録を確認します。
2. ファイルに割り当てられた UTI を確認します: `mdls -name kMDItemContentType -name kMDItemContentTypeTree /path/to/file.md`
3. **Console.app** で `MarkedQuickLookPreview` のエラーを確認します。
4. Marked Quick Look を `/Applications` に再インストールし、一度起動します。

完全なステップバイステップのチェックリストについては、[Marked Quick Look トラブルシューティング ガイド](https://github.com/ttscoff/MarkedQuickLook/blob/main/TROUBLESHOOTING.md) を参照してください。

### 開発ビルド

Xcode からのデバッグ ビルドは DerivedData に存在し、**自動的に登録されません**。各クリーン ビルド後に Xcode (Cmd+R) から **Marked Quick Look** コンテナ アプリを実行し、`.appex` への DerivedData パスを指定して `pluginkit -a` および `pluginkit -e use` コマンドを再実行します。

## 関連トピック

- [ファイルを開く](Opening_Files.html) — Marked がドキュメントを開いて監視する方法
- [マルチファイルドキュメント](Multi-File_Documents.html) — マークされた構文と完全な展開が含まれます
- [プロセッサの選択](Choosing_a_Processor.html) — マーク 3 内のプロセッサ オプション
- [拡張機能の共有](Share_Extension.html) — システムの共有メニューからマークされたファイルを送信します