# <%= @title %>

W> **O suporte ao Apex no Marked está em beta.** O comportamento pode mudar conforme a integração evolui. Relate problemas, renderizações inesperadas ou sintaxes ausentes em [support.markedapp.com](https://support.markedapp.com).

O Apex é um **processador de Markdown unificado**: um único mecanismo que busca cobrir os recursos pelos quais as pessoas normalmente escolhem CommonMark, GitHub Flavored Markdown (GFM), MultiMarkdown ou Kramdown --- sem abandonar as outras variantes.

No Marked, o **Apex (beta)** sempre funciona no modo **unificado** do Apex (todas essas famílias de recursos habilitadas juntas). Ainda não é possível escolher um "modo CommonMark" ou "modo Kramdown" separado do Apex dentro do Marked; isso pode vir mais adiante.

Confira o [Markdown Dingus](x-marked-3://dingus?processor=apex) para experimentar o Apex, ou abra {% appmenu Help, Markdown Reference %} e escolha a aba **Apex** para uma referência rápida e compacta.

---

## Por que o Apex existe [why-apex-exists]

As "variantes" de Markdown se diferenciaram por boas razões --- o GitHub precisava de listas de tarefas e tabelas, o MultiMarkdown precisava de notas de rodapé e metadados, o Kramdown precisava de listas de atributos --- mas escolher um processador geralmente significa abrir mão da sintaxe de outro.

O objetivo do Apex é **consolidar** essas extensões para que um único documento possa usar:

- Hábitos comuns de CommonMark / GFM (blocos de código, listas de tarefas, tachado, tabelas GFM)
- Hábitos de notas de rodapé, abreviações e metadados no estilo MultiMarkdown
- Listas de definição, matemática e (para uso avançado) listas de atributos no estilo Kramdown
- Recursos voltados ao Marked, como chamadas de destaque (callouts), Critic Markup e marcadores de sumário

A documentação completa do projeto original está disponível no [wiki do Apex](https://github.com/ApexMarkdown/apex/wiki). Esta página cobre o que você precisa no dia a dia na pré-visualização do Marked.

---

## Ativando o Apex no Marked [enabling-apex-in-marked]

1. Abra {% prefspane Processor %}.
2. Defina **Processador de Markdown padrão** como **Apex (beta)**.
3. Ou substitua por documento usando metadados como `Processor: apex` (apelidos: `apex-beta`, `unified`).

Os apelidos também funcionam a partir do AppleScript, das ações "Run Processor" do Conductor, da saída stdout de processadores personalizados (`APEX`) e de URLs de padrões do `x-marked://`.

T> Nesta versão beta, o Marked ainda expande suas próprias inclusões de arquivo (`<<[file]`, e caminhos de inclusão relacionados do Marked) antes de o Apex ser executado. O mecanismo nativo de inclusão do Apex é desativado no Marked por motivos de sandboxing. Use os recursos de inclusão do Marked como você já faz.

---

## Sintaxe básica que o Apex adiciona ou unifica [basic-syntax]

O Markdown padrão (títulos, ênfase, links, imagens, listas, citações, código) funciona como esperado. Os itens abaixo são os extras que as pessoas mais costumam precisar ao migrar para o Apex.

### Listas de tarefas [task-lists]

```markdown
- [ ] Todo
- [x] Done
```

### Tachado [strikethrough]

```markdown
~~removed text~~
```

### Tabelas [tables]

Tabelas em pipe no estilo GFM, com separadores de cabeçalho e alinhamento de colunas:

```markdown
| Left | Center | Right |
| :--- | :----: | ----: |
| a    | b      | c     |
```

Recursos avançados de tabela (rowspan `^^`, colspan, legendas, tabelas em grade, CSV) estão documentados no wiki: [Tables](https://github.com/ApexMarkdown/apex/wiki/Tables).

### Notas de rodapé [footnotes]

Estilo por referência:

```markdown
See the note[^1].

[^1]: Footnote text.
```

Os estilos inline conhecidos do MultiMarkdown / Kramdown também são suportados. Detalhes: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Listas de definição [definition-lists]

```markdown
Apple
: A fruit.
: A computer company.
```

### Sobrescrito e subscrito [superscript-and-subscript]

```markdown
Text^super^ and H~2~O
```

### Matemática [math]

Inline `$x^2$` e em bloco `$$...$$` (as preferências de MathJax / KaTeX do Marked continuam controlando a aparência na pré-visualização).

### Chamadas de destaque (callouts) [callouts]

No estilo Obsidian / Bear:

```markdown
> [!NOTE]
> Something worth highlighting.
```

Veja também a [Sintaxe Especial](Special_Syntax.html) do Marked e a página do wiki do Apex sobre [Callouts](https://github.com/ApexMarkdown/apex/wiki/Callouts).

### Critic Markup [critic-markup]

```markdown
{++insertion++}
{--deletion--}
{==highlight==}
{>>comment<<}
```

Ative o Critic Markup no Marked normalmente; o Apex pode renderizar a sintaxe critic no pipeline do processador. Veja [CriticMarkup](CriticMarkup.html).

### Abreviações [abbreviations]

```markdown
*[HTML]: HyperText Markup Language

The HTML spec is long.
```

### Códigos curtos de emoji [emoji-shortcodes]

```markdown
Ship it :rocket:
```

### Metadados [metadata]

Front matter em YAML, cabeçalhos no estilo MultiMarkdown `Key: Value` e blocos de título do Pandoc são reconhecidos. Insira valores com `[%key]` onde houver suporte.

Detalhes de configuração: [Configuration](https://github.com/ApexMarkdown/apex/wiki/Configuration) e [Metadata Transforms](https://github.com/ApexMarkdown/apex/wiki/Metadata-Transforms) no wiki.

### Marcadores de sumário [table-of-contents-markers]

O Apex reconhece marcadores comuns de sumário, incluindo:

- `<!--TOC-->`
- `{{TOC}}` ou `{{TOC:2-4}}`
- Estilo Kramdown `{:toc}`

Exclua um título com `{:.no_toc}` onde o IAL estiver disponível. Mais informações: [Syntax](https://github.com/ApexMarkdown/apex/wiki/Syntax).

### Marcadores especiais [special-markers]

Comentários HTML voltados ao Marked, como `<!--BREAK-->` (quebra de página) e `<!--PAUSE:N-->` (rolagem automática), continuam funcionando nas pré-visualizações com o Apex.

---

## Tópicos avançados (wiki) [advanced-topics-wiki]

Consulte o [wiki do Apex](https://github.com/ApexMarkdown/apex/wiki) para recursos poderosos, porém menos comuns no uso diário da pré-visualização:

| Tópico | Wiki |
|------|------|
| Geração de índice | [Indices](https://github.com/ApexMarkdown/apex/wiki/Indices) |
| Citações / bibliografia | [Citations](https://github.com/ApexMarkdown/apex/wiki/Citations) |
| Listas de atributos inline, spans, divs com fences | [Inline Attribute Lists](https://github.com/ApexMarkdown/apex/wiki/Inline-Attribute-Lists) |
| Documentos multiarquivo e inclusões | [Multi-File Documents](https://github.com/ApexMarkdown/apex/wiki/Multi-File-Documents) |
| Formatos de ID de cabeçalho | [Header IDs](https://github.com/ApexMarkdown/apex/wiki/Header-IDs) |
| Imagens multiformato | [Multi-Format Images](https://github.com/ApexMarkdown/apex/wiki/Multi-Format-Images) |
| Modos de compatibilidade (CLI) | [Modes](https://github.com/ApexMarkdown/apex/wiki/Modes) |
| Plugins e filtros | [Plugins](https://github.com/ApexMarkdown/apex/wiki/Plugins), [Filters](https://github.com/ApexMarkdown/apex/wiki/Filters) |
| Quarto / Pandoc / Jekyll | [Quarto Mode](https://github.com/ApexMarkdown/apex/wiki/Quarto-Mode), [Pandoc Integration](https://github.com/ApexMarkdown/apex/wiki/Pandoc-Integration), [Jekyll](https://github.com/ApexMarkdown/apex/wiki/Using-Apex-with-Jekyll) |

---

## Veja também [see-also]

- [Escolhendo um Processador](Choosing_a_Processor.html) --- quando escolher MultiMarkdown, CommonMark, Kramdown, Discount ou Apex
- [Configurações: Processador](Settings_Processor.html)
- [Markdown Dingus](Markdown_Dingus.html)
- [Página inicial do wiki do Apex](https://github.com/ApexMarkdown/apex/wiki)
- Relate problemas: [support.markedapp.com](https://support.markedapp.com)
