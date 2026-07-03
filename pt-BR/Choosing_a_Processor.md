<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marked pode visualizar o mesmo arquivo com vários processadores Markdown integrados. Cada um faz trocas diferentes entre **fluxo de trabalho de escrita** (livros, blogs, READMEs do GitHub) e **controle de saída** (IDs, classes, metadados). Você escolhe o padrão em {% prefspane Processor %}; você também pode substituir o processador por documento.

Esta página resume como os quatro processadores principais diferem. Para obter detalhes completos de sintaxe, consulte as páginas de referência em **Ajuda → Referência de Markdown** (por exemplo, [Especificação MultiMarkdown v5](MultiMarkdown_v5_Spec.html), [Especificação Kramdown](Kramdown_Spec.html), [Especificação CommonMark](CommonMark_Spec.html), [Especificação GFM de desconto](Discount_GFM_Spec.html)).

---

## MultiMarkdown (v5)

**Melhor para:** prosa longa, redação acadêmica ou técnica e qualquer coisa que dependa de **metadados**, **citações** e recursos **específicos do MultiMarkdown**.

Marked vem com **MultiMarkdown 5** (consulte o [Guia do usuário do MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/) para obter a documentação original).

### Pontos fortes

- **Documentos narrativos e com muitas referências:** Notas de rodapé, bibliografia/citações e tabelas são de primeira classe.
- **Metadados:** Blocos de metadados MultiMarkdown padrão (`Key: Value` cabeçalhos) mais **transclusão** e outras conveniências MMD descritas no guia v5.
- **Substituição de metadados:** Chaves de metadados podem ser inseridas no corpo com substituição no estilo `[%key]` para que títulos, strings de autor e valores semelhantes permaneçam sincronizados com o cabeçalho.
- **Tabelas, imagens e referências cruzadas:** Alinhados com os recursos documentados para MultiMarkdown 5.

### IDs e cabeçalhos manuais

- Os IDs de cabeçalho são **normalizados** de uma forma que tende a produzir slugs **minúsculas e concatenadas** (sem espaços — as palavras ficam juntas).
- Para **IDs de cabeçalho manuais**, MultiMarkdown usa o formato: `## Headline Text [my-id]` (o identificador entre colchetes após o texto do título).

### Quando escolher outra coisa

Se você precisar de listas de tarefas **com sabor do GitHub** e do comportamento exato do analisador atual do GitHub, prefira **CommonMark (GFM)**. Se você precisar de **classes/IDs HTML refinados** em elementos arbitrários, considere **Kramdown**.

---

## Kramdown

**Ideal para:** Documentos onde você deseja **controle preciso sobre a saída HTML** — **classes**, **IDs** e atributos personalizados, para que seu CSS possa direcionar blocos e extensões específicos.

A [referência de sintaxe do kramdown](https://kramdown.gettalong.org/syntax.html) é o guia oficial.

### Pontos fortes

- **Principalmente compatível** com hábitos no estilo MultiMarkdown para Markdown diário, ao mesmo tempo que adiciona suas próprias extensões.
- **Listas de atributos de bloco e inline (IALs):** Anexe `{: #id .class key="value"}` a parágrafos, cabeçalhos, blocos de código, links, imagens e muito mais --- ideal para sites no estilo Jekyll e folhas de estilo personalizadas.
- **IDs de cabeçalho:** kramdown normaliza IDs de cabeçalho gerados automaticamente para palavras **em minúsculas e separadas por hífen** (por exemplo, `my-section-title`). Para **IDs manuais**, use o formato `{#id}` após o texto do título — por exemplo, Setext: `My Section {#my-section}` depois o sublinhado, ou ATX: `# My Section {#my-section}` (veja os [cabeçalhos](https://kramdown.gettalong.org/syntax.html#headers) do kramdown para posicionamento exato e regras IAL).
- **Listas de definições, notas de rodapé, tipografia inteligente, blocos matemáticos:** Conjunto rico de recursos para pipelines de publicação que precisam de mais do que Markdown "simples".

### Quando escolher outra coisa

Se você depende de substituição de metadados **somente MultiMarkdown** (`[%key]`) ou fluxos de trabalho de citação específicos de MMD, **MultiMarkdown** pode ser uma opção melhor. Para **README e documentos de repositório** que devem corresponder ao GitHub online, **CommonMark (GFM)** geralmente é mais próximo.

---

## CommonMark (Markdown com sabor do GitHub / cmark-gfm)

**Melhor para:** **arquivos README**, **descrições de problemas/PR** e **documentação do projeto** que devem corresponder ao **comportamento atual do Markdown do GitHub** o mais próximo possível.

Marked usa um mecanismo orientado a **GFM** (cmark-gfm). A especificação formal é [GitHub Flavored Markdown Spec](https://github.github.com/gfm/), construída em [CommonMark](https://commonmark.org/).

### Pontos fortes

- **Correspondência mais próxima do GitHub:** tabelas, tachados, itens da lista de tarefas, blocos de código protegidos com tags de idioma e links automáticos se comportam como a renderização moderna do GitHub.
- **Análise inequívoca:** CommonMark define precedência de bloco/inline e regras de lista com precisão - mais rigoroso em alguns casos extremos do que o comportamento "clássico" do Markdown.pl, mas **mais previsível** depois que você aprende as regras.
- **Prático para texto encapsulado:** As regras de parágrafo e lista são projetadas para se comportarem bem com prosa compactada (veja as seções das especificações sobre continuações lentas e listas).

### IDs de cabeçalho

As âncoras de título geradas automaticamente são normalmente **minúsculas e separadas por hífen**, consistente com o slugging comum no estilo GitHub.

### Quando escolher outra coisa

O GFM não replica fluxos de trabalho de **metadados MultiMarkdown**, **IALs kramdown** ou **citação MMD**. Para livros, teses ou metadados pesados, use **MultiMarkdown** ou **Kramdown** conforme apropriado.

---

## Desconto

**Ideal para:** Um processador **rápido baseado em C** que rastreia o **Markdown clássico** e um conjunto de recursos **antigo com sabor do GitHub** — útil quando você deseja um comportamento mais próximo do **Markdown original** além de tabelas, notas de rodapé e extensões relacionadas sem o livro de regras completo do CommonMark.

Casa do projeto: [Desconto](https://www.pell.portland.or.us/~orc/Code/discount/).

### Pontos fortes

- **Tabelas de estilo PHP Markdown Extra** e muitas extensões (notas de rodapé, código protegido quando ativado, etc. --- consulte [Especificação GFM de desconto](Discount_GFM_Spec.html) do Marked para saber o que o Marked permite).
- **Extras opcionais do "GitHub"** no desconto upstream (por exemplo, listas de caixas de seleção quando construídas com os sinalizadores corretos); Marcado documenta a combinação enviada na página de especificações de desconto.
- **Tipografia estilo SmartyPants** e outras conveniências descritas no site de descontos (embora todos os processadores incluídos forneçam recursos de tipografia).
- Filosoficamente próximo do **Markdown de John Gruber** mais extensões práticas, em vez do conjunto de testes CommonMark completo.

### Quando escolher outra coisa

Para **paridade perfeita de pixels com o github.com atual**, prefira **CommonMark (GFM)**. Para **metadados e citações do MultiMarkdown**, use **MultiMarkdown**.

---

## Comparação rápida

| Preocupação | MultiMarkdown | Kramdown | Marca Comum (GFM) | Desconto |
|--------|---------------|--------|-------|----------|
| **Uso principal** | Prosa, artigos, livros | HTML estilizado, sites do tipo Jekyll | READMEs, documentos semelhantes ao GitHub | Extensões clássicas MD + |
| **Citações/metadados MMD** | Forte | Através de sintaxe diferente | Não | Não |
| **Estilo de ID de título manual** | `## Title [id]` | `## Title {: #id }` (IAL) | Regras de slug de especificações/GitHub | Nenhum |
| **IDs de cabeçalho automáticos** | Letras minúsculas concatenadas | Minúsculas hifenizadas | Minúsculas hifenizadas | Hifenizado em minúsculas |
| **Atributos extras (classes/ids)** | Mecanismos MMD limitados | **IALs** — muito fortes | Limitado | Limitado |

---

## Veja também

- [Configurações: Processador](Settings_Processor.html) — processador padrão e opções relacionadas
- [Markdown Dingus](Markdown_Dingus.html) — experimente processadores lado a lado em Marked
- [Processador personalizado](Custom_Processor.html) — conecte seu próprio conjunto de ferramentas quando necessário