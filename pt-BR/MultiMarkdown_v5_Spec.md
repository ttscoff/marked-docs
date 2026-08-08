<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Confira o [Markdown Dingus](x-marked-3://dingus?processor=multimarkdown) para experimentar o processador MultiMarkdown.

## O que é MultiMarkdown? [what-is-multimarkdown]

MultiMarkdown é um processador Markdown estendido projetado para funcionar com documentos completos, em vez de apenas fragmentos de páginas da web. Ele estende a sintaxe original do Markdown com recursos que permitem a conversão para vários formatos de saída, incluindo documentos HTML, LaTeX, PDF, ODF e Microsoft Word.

## Principais características [key-characteristics]

- **Focado em documentos**: projetado para documentos completos, não apenas trechos da web
- **Saída multiformato**: converte para HTML, LaTeX, PDF, ODF, RTF e Word
- **Conteúdo sobre apresentação**: concentra-se na estrutura e no significado do documento
- **Cross-Platform**: Funciona em qualquer sistema operacional com qualquer editor de texto
- **Extensível**: rico conjunto de recursos para requisitos de documentos complexos
- **Versão 5**: Reescrita completa com melhor desempenho e confiabilidade

## Filosofia e Metas de Design [philosophy-and-design-goals]

MultiMarkdown segue o princípio de que **o conteúdo é mais importante que a apresentação**. O foco está em representar o significado dos documentos (isto é uma lista, aquilo é uma tabela, etc.) em vez de ditar fontes, cores ou estilos.

O objetivo é ser utilizável em 80% dos documentos escritos por 80% das pessoas, tornando-o adequado para romances, teses, documentação técnica e a maioria dos outros conteúdos escritos.

## Principais recursos e extensões [major-features-and-extensions]

### 1. **Suporte a metadados** [1-metadata-support]

- Documente metadados na parte superior dos arquivos
- Título, autor, data e variáveis personalizadas
- Inclusão automática em cabeçalhos de saída

```markdown
title: My Document
author: John Doe
date: 2024-01-15
custom: value

<!-- A blank line ends the metadata -->
Content
---

# Document Content
```

**Variáveis de metadados**

- Use valores de metadados em todo o documento
- Sintaxe: `[%variable_name]`
- Substituição automática durante o processamento

```markdown
Title: [%title]
Author: [%author]
Date: [%date]
```

### 2. **Tabelas Avançadas** [2-advanced-tables]

**Suporte de mesa completo**

- Cabeçalhos, alinhamento e estruturas de tabelas complexas
- Suporte para legendas e rótulos de tabelas
- Referências cruzadas a tabelas

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |

Table: Sample Table with Alignment
```

**Recursos da tabela**

- Alinhamento de coluna usando dois pontos
- Legendas e rótulos de tabelas
- Referências cruzadas com `[Table 1]`
- Suporte para estruturas de tabelas complexas

### 3. **Notas de rodapé e citações** [3-footnotes-and-citations]

**Notas de rodapé**

- Notas de rodapé em estilo de referência com sintaxe `[^1]`
- Numeração e vinculação automáticas
- Suporte para notas de rodapé embutidas

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Suporte para citações**

- Formatação de citações acadêmicas
- Geração de bibliografia
- Suporte para vários estilos de citação

```
This is a statement that should be attributed to
its source[p. 23][#Doe:2006].
```

E a seguir está a descrição da referência a ser
usado na bibliografia.

```
[#Doe:2006]: John Doe. *Some Big Fancy Book*.  Vanity Press, 2006.
```

Na saída HTML, as citações são indistinguíveis das notas de rodapé.

Você não é obrigado a usar um localizador (por exemplo, p. 23) e não há regras especiais sobre o que pode ser usado como localizador se você decidir usar um. Se preferir omitir o localizador, basta usar um conjunto vazio de colchetes antes da citação:

```
This is a statement that should be attributed to its
source[][#Doe:2006].
```

Não há regras sobre o formato da chave de citação que você usa (por exemplo, Doe:2006), mas deve ser precedido por `#`, assim como as notas de rodapé usam `^`.

### 4. **Referências cruzadas** [4-cross-references]

**Referências cruzadas automáticas**

- Link para títulos, tabelas, figuras e equações
- Geração automática de etiquetas
- Suporte para etiquetas personalizadas

```markdown
See [Table 1] for details.
Refer to [Section 2.1] for more information.

## Section 2.1
```

**Tipos de referência**

- Títulos: `[Section 1]`, `[Heading Title]`
- Tabelas: `[Table 1]`, `[Table: Caption]`
- Números: `[Figure 1]`, `[Figure: Caption]`
- Equações: `[Equation 1]`

### 5. **Listas de definições** [5-definition-lists]

**Pares Termo-Definição**

- Suporte para listas de definição
- Múltiplas definições por termo
- Saída HTML `<dl>` adequada

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

### 6. **Blocos de código protegidos** [6-fenced-code-blocks]

**Blocos de código específicos do idioma**

- Backticks triplos com especificação de idioma
- Suporte para realce de sintaxe
- Detecção automática de idioma

```markdown
```python
def hello():
    print("Hello, World!")
```
```

**Code Block Features**

- Language specification for syntax highlighting
- Support for many programming languages
- Proper HTML ⟦14⟧ output

### 7. **Math Support** [7-math-support]

**Mathematical Expressions**

- LaTeX-compatible math syntax
- Both inline and block math support
- Integration with LaTeX output

```markdown
Inline math: $E = mc^2$

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 8. **Atributos de imagem e link** [8-image-and-link-attributes]

**Links e imagens aprimorados**

- Suporte para atributos HTML
- Largura, altura, texto alternativo e muito mais
- Melhor integração com formatos de saída

```markdown
[Link text]: url.html title="Link title" class="external"
```

### 9. **Transclusão** [9-transclusion]

**Inclusão de arquivo**

- Incluir outros arquivos nos documentos
- Suporte para inclusões aninhadas
- Resolução automática de caminho

```markdown
{{chapter1.md}}
{{../shared/intro.md}}
```

**Recursos de transclusão**

- Inclusão de arquivo com `{{filename}}`
- Suporte para caminhos relativos e absolutos
- Suporte para transclusão aninhada
- Geração de manifesto para arquivos incluídos

### 10. **Integração CriticMarkup** [10-criticmarkup-integration]

**Acompanhamento de alterações**

- Suporte para sintaxe CriticMarkup
- Rastreie adições, exclusões e comentários
- Recursos de edição colaborativa

```markdown
This is {>>deleted text<<} and this is {++added text++}.

This is a {~~deletion~>replacement~~}.
```

### 11. **Índice** [11-table-of-contents]

**Geração automática de TOC**

- `{{TOC}}` espaço reservado para índice
- Estrutura hierárquica baseada em títulos
- Geração de TOC personalizável

```markdown
# Document Title

{{TOC}}

## Section 1
Content here...

## Section 2
More content...
```

### 12. **Abreviações** [12-abbreviations]

**Abreviações em estilo HTML**

- Definir abreviaturas para expansão automática
- Suporte para dicas e explicações
- Saída HTML `<abbr>` adequada

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

## MultiMarkdown v5 vs outros sabores de Markdown [multimarkdown-v5-vs-other-markdown-flavors]

| Recurso | MultiMarkdown v5 | Marca Comum (GFM) | Desconto | Kramdown | Padrão |
| ---------------- | ---------------- | ---------- | ------------ | -------- | -------- |
| Tabelas | Sim | Não | Sim | Sim | Não |
| Tachado | Sim | Não | Sim | Não | Não |
| Listas de tarefas | Sim | Não | Sim | Não | Não |
| Código Cercado | Sim | Sim | Sim | Sim | Não |
| Matemática | Sim | Não | Não | Sim | Não |
| Notas de rodapé | Sim | Não | Sim | Sim | Não |
| Listas de definição | Sim | Não | Não | Sim | Não |
| Abreviaturas | Sim | Não | Não | Sim | Não |
| Listas de atributos | Sim | Não | Não | Sim | Não |
| Extensões | Sim | Não | Limitado | Sim | Não |
| Tipografia | Sim | Não | Básico | Sim | Não |
| Links automáticos | Sim | Não | Sim | Não | Não |
| Referências Cruzadas | Sim | Não | Não | Não | Não |
| Citações | Sim | Não | Não | Não | Não |
| Transclusão | Sim | Não | Não | Não | Não |
| Metadados | Sim | Não | Não | Não | Não |

## Principais vantagens do MultiMarkdown v5 [key-advantages-of-multimarkdown-v5]

1. **Focado em documentos**: projetado para documentos completos, não apenas trechos da web
2. **Saída multiformato**: Converta para HTML, LaTeX, PDF, ODF, RTF e Word
3. **Apoio Acadêmico**: Citações, notas de rodapé e referências cruzadas
4. **Recursos Profissionais**: Metadados, transclusão e formatação avançada
5. **Cross-Platform**: Funciona em qualquer sistema operacional
6. **Prova para o futuro**: o formato de texto simples garante compatibilidade de longo prazo
7. **Extensível**: rico conjunto de recursos para requisitos de documentos complexos

## Casos de uso comuns [common-use-cases]

**Escrita Acadêmica**

- Teses, dissertações e trabalhos de pesquisa
- Gerenciamento de citações e geração de bibliografia
- Referências cruzadas e notas de rodapé

**Documentação Técnica**

- Documentação da API e guias do usuário
- Especificações técnicas e manuais
- Documentação de código com destaque de sintaxe

**Publicação**

- Livros, artigos e relatórios
- Saída multiformato para diferentes plataformas
- Formatação profissional de documentos

**Gerenciamento de conteúdo**

- Sites de documentação
- Bases de conhecimento e wikis
- Projetos de escrita colaborativa

## Melhores práticas [best-practices]

1. **Use metadados**: aproveite o front-matéria YAML para informações de documentos
2. **Estrutura com títulos**: Use hierarquia de títulos adequada para geração de TOC
3. **Aproveite as referências cruzadas**: use links automáticos para melhor navegação
4. **Organize com transclusão**: divida documentos grandes em arquivos gerenciáveis
5. **Saída de teste**: verifique a formatação em diferentes formatos de saída
6. **Use citações**: implemente práticas adequadas de citações acadêmicas

## Migração de outros sabores de Markdown [migration-from-other-markdown-flavors]

A maioria dos Markdown padrão funciona com MultiMarkdown sem alterações. Para aproveitar os recursos do MMD:

1. **Adicionar metadados**: Incluir assunto YAML para informações do documento
2. **Use referências cruzadas**: substitua links manuais por referências automáticas
3. **Implementar citações**: adicione formatação adequada de citações acadêmicas
4. **Estrutura com Transclusão**: divida documentos grandes em arquivos menores
5. **Aproveitar tabelas**: use recursos avançados de tabela para apresentação de dados

## Recursos [resources]

- [Guia do usuário do MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html)
- [Guia de sintaxe MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/MMD_Users_Guide.html#syntax)
- [Repositório GitHub MultiMarkdown](https://github.com/fletcher/MultiMarkdown-5)
- [Documentação MultiMarkdown](https://fletcher.github.io/MultiMarkdown-5/)

---

*Esta documentação cobre o MultiMarkdown v5.1.0. Para obter as informações mais atuais, consulte sempre a documentação oficial do MultiMarkdown em [fletcher.github.io/MultiMarkdown-5](https://fletcher.github.io/MultiMarkdown-5/).*