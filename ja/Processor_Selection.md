<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## プロセッサの選択 [processor-selection]

[MultiMarkdown](http://fletcherpenney.net/multimarkdown/ "MultiMarkdown") (Fletcher Penney 著) は、[Markdown](http://daringfireball.net/projects/markdown/ "Daring Fireball: Markdown") (John Gruber 著) の拡張です。すべての標準的な Markdown 書式設定が守られており、MultiMarkdown は表や脚注などの要素に追加の構文を提供します。

## 構文 [syntax]

ヘルプ メニューの下に Markdown 構文ガイドがあります。または、[John Gruber のオリジナル ドキュメント](http://daringfireball.net/projects/markdown/syntax) を参照することもできます。

MultiMarkdown 拡張機能は、Fletcher Penney によって [このドキュメント](https://github.com/fletcher/MultiMarkdown/blob/master/Documentation/MultiMarkdown%20User%27s%20Guide.md) に文書化されています。

## 代替レンダリング [alternative-rendering]

{% prefspane Processor %} では、MultiMarkdown、Kramdown、CommonaMark、Discount から選択できます。それぞれが若干異なる構文で追加機能を提供します (詳細については、{% appmenu Help, Markdown Reference %} を参照)。ほとんどの場合、MultiMarkdown が優先されますが、既にプロセッサー固有の構文を使用しているファイルがある場合、または MultiMarkdown を使用して Markdown ファイルをレンダリングする際に問題が発生した場合は、デフォルトのプロセッサーとして Commonmark を選択してください。