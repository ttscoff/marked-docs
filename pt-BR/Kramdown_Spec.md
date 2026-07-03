<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Confira o [Markdown Dingus](x-marked-3://dingus?processor=kramdown) para experimentar o processador Kramdown.

## O que é Kramdown?

Kramdown é um conversor rápido e puro de Ruby Markdown-superset que estende a sintaxe original do Markdown com recursos encontrados em outras implementações como Maruku, PHP Markdown Extra e Pandoc. Ele fornece uma sintaxe estrita com regras definidas, mantendo a compatibilidade com a maioria dos documentos Markdown.

## Principais características

- **Ruby Rápido e Puro**: Escrito inteiramente em Ruby para desempenho e portabilidade
- **Sintaxe estrita**: fornece regras definidas e especificações claras
- **Recursos aprimorados**: Inclui muitas extensões não encontradas no Markdown padrão
- **Integração Jekyll**: Processador Markdown padrão para gerador de site estático Jekyll
- **Abrangente**: suporta elementos de nível de bloco e de extensão com ampla personalização

## Principais diferenças do Markdown padrão

### 1. **Elementos aprimorados em nível de bloco**

**Listas de definições**

- Kramdown suporta listas de definição (não no Markdown padrão)
- Usa `:` para separar termos de definições

```markdown
Term 1
: Definition 1

Term 2
: Definition 2a
: Definition 2b
```

**Tabelas**

- Suporte completo a tabelas com cabeçalhos, alinhamento e formatação
- Mais abrangente do que a sintaxe básica da tabela Markdown

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Blocos Matemáticos**

- Suporte para expressões matemáticas usando sintaxe LaTeX
- Suporte matemático inline e em bloco

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 2. **Marcação de texto avançada**

**Notas de rodapé**

- Suporte completo para notas de rodapé com numeração automática
- Notas de rodapé em estilo de referência com sintaxe `[^1]`

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Abreviações**

- Suporte para abreviações de estilo HTML
- Expansão automática de abreviaturas definidas

```markdown
*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets

This uses HTML and CSS.
```

**Símbolos tipográficos**

- Conversão automática de caracteres tipográficos comuns
- Citações inteligentes, travessões, reticências, etc.

```markdown
"Smart quotes" and -- em dashes -- and ... ellipses
Even << guillemets >>
```

### 3. **Listas de atributos e extensões**

**Definições de lista de atributos (ALDs)**

- Definir conjuntos de atributos reutilizáveis
- Suporte para IDs, classes e atributos personalizados

```markdown
{:ref-name: #myid .my-class title="My Title"}

A paragraph with attributes.
{: #para-one .highlight}
```

**Listas de atributos embutidos (IALs)**

- Anexar atributos a elementos específicos
- Suporte em nível de bloco e em nível de extensão

```markdown
This *is*{:.underline} some ⟦3⟧{:#id}{:.class}.
A [link](test.html){:rel='something'} and some **tools**{:.tools}.
```

**Extensões**

- Sistema de extensão personalizado para funcionalidade adicional
- Extensões integradas para comentários e opções

```markdown
{::comment}
This text is completely ignored by kramdown.
{:/comment}

{::options key="val" /}
```

### 4. **Suporte aprimorado para bloco de código**

**Especificação do idioma**

- Destaque automático de sintaxe para blocos de código protegidos
- Suporte para muitas linguagens de programação

    ```rubi
    definitivamente olá
      coloca "Olá, mundo!"
    fim
    ```

**Blocos de código padrão**

- Melhor manipulação de blocos de código recuados
- Melhor integração com outros elementos do bloco

### 5. **Regras de análise mais rígidas**

**Quebra de linha**

- Suporte para conteúdo empacotado (sintaxe lenta)
- Regras claras para quando a quebra de linha é permitida
- Não recomendado para facilitar a leitura, mas compatível com compatibilidade

**Manuseio de guias**

- Assume paradas de tabulação em múltiplos de quatro
- Tabulações permitidas apenas no início das linhas para recuo
- Não deve ser precedido de espaços

**Limites de bloco**

- Regras claras para quando os elementos devem começar/terminar nos limites do bloco
- Comportamento consistente em diferentes tipos de elementos

### 6. **Suporte avançado para links e imagens**

**Links automáticos**

- Detecção automática de link aprimorada
- Melhor tratamento de URLs e endereços de e-mail

**Links de referência**

- Processamento de link de referência aprimorado
- Melhor resolução de conflitos para múltiplas definições

**Atributos de imagem**

- Suporte para atributos de imagem através de IALs
- Largura, altura, texto alternativo e outros atributos HTML

```markdown
![Alt text](image.jpg){:width="300" height="200" class="responsive"}
```

### 7. **Integração HTML**

**Blocos HTML**

- Melhor manuseio de HTML dentro do Markdown
- Suporte para atributos e processamento HTML
- Mais flexível do que o manuseio HTML Markdown padrão

**Espanços HTML**

- HTML embutido com suporte a atributos
- Melhor integração com sintaxe Markdown

### 8. **Expressões Matemáticas**

**Matemática embutida**

- `$...$` sintaxe para expressões matemáticas embutidas
- Sintaxe compatível com LaTeX

**Bloquear Matemática**

- `$$...$$` sintaxe para expressões matemáticas de bloco
- Suporte para equações e fórmulas complexas

## Kramdown vs outros sabores de Markdown

| Recurso | Kramdown | Marca Comum (GFM) | GitHub com sabor | MultiMarkdown | Padrão |
| ---------------- | -------- | ---------- | --------------- | ------------- | -------- |
| Tachado | Não | Sim | Não | Não | Não |
| Listas de tarefas | Não | Não | Sim | Sim | Não |
| Código Cercado | Sim | Sim | Sim | Sim | Não |
| Matemática | Sim | Não | Sim | Sim | Não |
| Notas de rodapé | Sim | Sim | Sim | Sim | Não |
| Listas de definição | Sim | Não | Não | Sim | Não |
| Abreviaturas | Sim | Não | Não | Não | Não |
| Listas de atributos | Sim | Não | Não | Não | Não |
| Tipografia | Sim | Não | Não | Sim | Não |

## Principais vantagens do Kramdown

1. **Conjunto abrangente de recursos**: Inclui muitas extensões não encontradas em outras implementações
2. **Integração Jekyll**: Integração perfeita com o gerador de site estático Jekyll
3. **Ecossistema Ruby**: Implementação Ruby pura com bom suporte de ferramentas Ruby
4. **Extensibilidade**: Sistema de extensão personalizado para funcionalidade adicional
5. **Suporte a atributos**: Sistema rico de atributos para personalização de saída HTML
6. **Suporte matemático**: suporte integrado para expressões matemáticas LaTeX
7. **Análise estrita**: regras de análise claras e inequívocas

## Casos de uso comuns

**Sites Jekyll**

- Processador padrão para geração de sites estáticos Jekyll
- Excelente para documentação e sites de blog

**Documentação Técnica**

- Suporte matemático para redação científica e técnica
- Listas de atributos para personalização avançada de HTML

**Escrita Acadêmica**

- Suporte de notas de rodapé para citações e referências
- Expressões matemáticas para fórmulas e equações

**Gerenciamento de conteúdo**

- Extensões para funcionalidade personalizada
- Listas de atributos para metadados e estilos

## Recursos

- [Documentação de sintaxe Kramdown](https://kramdown.gettalong.org/syntax.html)
- [Documentação do conversor Kramdown](https://kramdown.gettalong.org/converter.html)
- [Guia de integração Jekyll](https://jekyllrb.com/docs/configuration/markdown/)
- [Repositório Kramdown GitHub](https://github.com/gettalong/kramdown)

## Migração do Markdown padrão

A maioria dos documentos padrão do Markdown funcionam com o Kramdown sem modificação. Para aproveitar as vantagens dos recursos do Kramdown:

1. **Adicionar listas de definições**: converta glossários e listas de termos
2. **Use listas de atributos**: adicione IDs, classes e atributos personalizados
3. **Implementar notas de rodapé**: converter referências entre parênteses

## Melhores práticas

1. **Evite sintaxe preguiçosa**: não confie no empacotamento rígido para facilitar a leitura
2. **Use listas de atributos**: aproveite IALs para estilização e metadados
3. **Recuo Consistente**: Use espaços em vez de tabulações quando possível

---

*Esta documentação cobre o Kramdown 2.5.1. Para obter informações mais atuais, consulte sempre a documentação oficial em [kramdown.gettalong.org](https://kramdown.gettalong.org/).*