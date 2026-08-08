<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

## O que é Markdown? [what-is-markdown]

Markdown é uma linguagem de marcação leve que permite escrever usando um formato de texto simples fácil de ler e escrever e, em seguida, convertê-lo em HTML estruturalmente válido. O principal objetivo de design da sintaxe de formatação do Markdown é torná-la o mais legível possível.

## Sintaxe Básica [basic-syntax]

### Cabeçalhos [headers]

Crie cabeçalhos usando símbolos hash (`#`). O número de hashes determina o nível do cabeçalho:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Ênfase [emphasis]

**Texto em negrito** usando asteriscos duplos ou sublinhados duplos:

```markdown
**Bold text**
__Bold text__
```

*Texto em itálico* usando asteriscos ou sublinhados simples:

```markdown
*Italic text*
_Italic text_
```

### Listas [lists]

**Listas não ordenadas** usando asteriscos, sinais de adição ou hífens:

```markdown
* Item 1
* Item 2
* Item 3

+ Item 1
+ Item 2
+ Item 3

- Item 1
- Item 2
- Item 3
```

**Listas ordenadas** usando números seguidos de pontos:

```markdown
1. First item
2. Second item
3. Third item
```

###Links

**Links embutidos** com o texto entre colchetes e o URL entre parênteses:

```markdown
[Link text](http://example.com)
```

**Links de referência** com o texto entre colchetes e uma referência entre colchetes:

```markdown
[Link text][reference]

[reference]: http://example.com "Optional title"
```

**Links automáticos** colocando URLs entre colchetes angulares:

```markdown
<http://example.com>
<user@example.com>
```

### Imagens [links]

As imagens usam sintaxe semelhante aos links, mas com um ponto de exclamação no início:

```markdown
![Alt text](http://example.com/image.jpg)
![Alt text][image-reference]

[image-reference]: http://example.com/image.jpg "Optional title"
```

### Citações em bloco [images]

Crie aspas usando o símbolo maior que (`>`) no início de cada linha:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> You can have multiple paragraphs in a blockquote.
```

### Código [blockquotes]

**Código embutido** usando crases:

```markdown
Use ⟦4⟧ in your text.
```

**Blocos de código** recuando com quatro espaços ou uma tabulação:

```markdown
    This is a code block.
    It preserves formatting and spacing.
    Multiple lines are supported.
```

### Regras horizontais [code]

Crie regras horizontais usando três ou mais hífens, asteriscos ou sublinhados:

```markdown
---

***

___
```

### Quebras de linha [horizontal-rules]

**Quebras de linha rígidas** finalizando uma linha com dois ou mais espaços:

```markdown
This line ends with two spaces.
This creates a hard line break.
```

**Quebras suaves de linha** simplesmente pressionando Enter (cria um espaço em HTML):

```markdown
This line
continues on the next line with a space.
```

### Personagens de fuga [line-breaks]

Escape de caracteres especiais usando barras invertidas:

```markdown
\*This text is not italic\*
\[This is not a link\]
```

Caracteres comuns que podem ser escapados:
- `\` barra invertida
- `` ` `` crase
- `*` asterisco
- `_` sublinhado
- `{}` aparelho encaracolado
- `[]` colchetes
- `()` parênteses
- `#` hash
- `+` mais
- `-` menos
- `.` período
- `!` ponto de exclamação

## Melhores práticas [best-practices]

1. **Use linhas em branco** para separar diferentes elementos para melhor legibilidade
2. **Seja consistente** com suas escolhas de formatação (por exemplo, use `*` ou `_` para dar ênfase)
3. **Mantenha a simplicidade** - Markdown foi projetado para ser legível como texto simples
4. **Teste sua saída** para garantir que ela seja renderizada conforme o esperado
5. **Use um texto de link significativo** em vez de frases genéricas como "clique aqui"

## Padrões Comuns [common-patterns]

### Listas aninhadas [nested-lists]

```markdown
1. First item
   - Nested item
   - Another nested item
2. Second item
   - More nested content
```

### Listas com parágrafos [lists-with-paragraphs]

```markdown
1. First item

   This is a paragraph under the first item.

2. Second item

   This is a paragraph under the second item.
```

### Blockquotes com outros elementos [blockquotes-with-other-elements]

```markdown
> This is a blockquote with **bold text** and *italic text*.
>
> - It can contain lists
> - And other Markdown elements
>
> > Nested blockquotes are also possible.
```

## Resumo [summary]

Markdown fornece uma maneira simples e legível de formatar texto que pode ser facilmente convertido em HTML. A chave é mantê-lo simples e legível enquanto usa os elementos básicos da sintaxe de forma consistente. Com a prática, você descobrirá que o Markdown se torna uma segunda natureza e torna a escrita de conteúdo estruturado muito mais fácil.

---

*Este tutorial cobre a sintaxe principal do Markdown conforme definido na especificação original. Para recursos mais avançados, consulte a documentação de processadores Markdown específicos, como CommonMark (GFM), MultiMarkdown ou GitHub Flavored Markdown.*