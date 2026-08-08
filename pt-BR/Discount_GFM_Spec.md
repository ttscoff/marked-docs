<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Confira o [Markdown Dingus](x-marked-3://dingus?processor=discount) para experimentar o processador de desconto.

## O que é Desconto GFM? [what-is-discount-gfm]

Discount GFM (GitHub Flavored Markdown) é um processador Markdown baseado em C que implementa a sintaxe Markdown estendida do GitHub. É baseado na biblioteca Discount original, mas aprimorado com recursos específicos do GitHub, como tabelas, listas de tarefas, texto tachado e link automático de URL.

## Principais características [key-characteristics]

- **Desempenho baseado em C**: implementação C rápida e nativa para desempenho ideal
- **Compatibilidade com GitHub**: implementa extensões Markdown do GitHub para máxima compatibilidade
- **Leve**: Dependências mínimas e tamanho reduzido
- **Extensível**: Suporta várias extensões Markdown e opções personalizadas
- **Suporte HTML5**: gera saída HTML5 moderna com marcação semântica adequada

## Principais diferenças do Markdown padrão [major-differences-from-standard-markdown]

### 1. **Extensões de Markdown com sabor do GitHub** [1-github-flavored-markdown-extensions]

**Tabelas**

- Suporte completo para tabelas estilo GitHub com opções de alinhamento
- Cabeçalhos, separadores e linhas de dados com estrutura de tabela HTML adequada
- Alinhamento de colunas usando dois pontos (`:`) nas linhas separadoras

```markdown
| Header 1 | Header 2 | Header 3 |
| :------- | :------: | -------: |
| Left     |  Center  |    Right |
| Aligned  | Aligned  |  Aligned |
```

**Listas de Tarefas**

- Suporte para caixas de seleção estilo GitHub em listas
- Caixas de seleção interativas (renderizadas como elementos de entrada HTML)
- Suporta estados marcados e desmarcados

```markdown
- [x] Completed task
- [ ] Pending task
- [x] Another completed task
```

**Texto tachado**

- O texto entre tis duplos (`~~`) fica tachado
- Usa tags HTML `<del>` para marcação semântica
- Suporta vários tis para dar ênfase

```markdown
~~This text is crossed out~~
~~Mistaken text that should be removed~~
```

### 2. **Suporte aprimorado para bloco de código** [2-enhanced-code-block-support]

**Blocos de código protegidos**

- Crases triplos (```` ``` ````) para blocos de código
- Especificação de linguagem para destaque de sintaxe
- Não é necessário recuo (ao contrário do Markdown padrão)

```markdown
```javascript
function hello() {
  console.log("Hello, World!");
}
```
```

**Automatic Language Detection**

- Support for many programming languages
- Proper syntax highlighting when supported
- Fallback to plain text for unsupported languages

### 3. **Automatic URL Linking** [3-automatic-url-linking]

**URL Autolinking**

- Automatic conversion of URLs to clickable links
- Support for http, https, and ftp protocols
- Email addresses automatically converted to mailto links

```markdown
Visit http://example.com for more information.
Contact us at user@example.com
```

**Detecção de link inteligente**

- Reconhece URLs sem marcação explícita
- Lida com vários formatos e protocolos de URL
- Opções configuráveis de segurança de link

### 4. **Recursos avançados da lista** [4-advanced-list-features]

**Listas Alfabéticas**

- Listas ordenadas com marcadores alfabéticos (a, b, c, etc.)
- Progressão automática através do alfabeto
- Saída HTML `<ol type="a">` adequada

```markdown
a. First item
b. Second item
c. Third item
```

**Processamento de lista aprimorado**

- Melhor manipulação de listas aninhadas
- Melhor espaçamento e recuo
- Suporte para tipos de lista mista

### 5. **Suporte para notas de rodapé** [5-footnotes-support]

**Notas de rodapé em estilo de referência**

- Numeração automática de notas de rodapé
- Links de referência com sintaxe `[^1]`
- Definições de notas de rodapé no final do documento

```markdown
This is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

**Processamento automático de notas de rodapé**

- Gera estrutura de notas de rodapé HTML adequada
- Links entre referências e definições
- Numeração sequencial em todo o documento

### 6. **Integração HTML** [6-html-integration]

**Suporte HTML5**

- Reconhecimento completo de tags HTML5
- Geração adequada de marcação semântica
- Estrutura e atributos HTML modernos

**Blocos HTML brutos**

- Suporte para HTML dentro do Markdown
- Escape e higienização adequados
- Integração com sintaxe Markdown

### 7. **Regras de ênfase aprimoradas** [7-enhanced-emphasis-rules]

**Ênfase relaxada**

- Sublinhados únicos (`_`) não criam ênfase no meio das palavras
- Melhor para documentar código e conteúdo técnico
- Evita ênfase indesejada em identificadores

```markdown
This is a variable_name that won't be emphasized.
This is _emphasized text_ that will be styled.
```

**Vários níveis de ênfase**

- Suporte para negrito, itálico e ênfase combinada
- Consistente com as regras de ênfase padrão do Markdown
- Saída HTML adequada com tags `<strong>` e `<em>`

### 8. **Geração de índice** [8-table-of-contents-generation]

**ÍNDICE automático**

- Gera índice a partir de títulos
- Estrutura hierárquica baseada em níveis de títulos
- Opções configuráveis de geração de TOC

**Geração de ID de título**

- Geração automática de ID para títulos
- Links âncora para fácil navegação
- Formatação de ID consistente

## Desconto GFM vs outros sabores de redução [discount-gfm-vs-other-markdown-flavors]

| Recurso | Desconto | Marca Comum (GFM) | Kramdown | MultiMarkdown | Padrão |
| ---------------- | ------------ | ---------- | -------- | ------------- | -------- |
| Tabelas | Sim | Não | Sim | Sim | Não |
| Tachado | Sim | Não | Não | Sim | Não |
| Listas de tarefas | Sim | Não | Não | Sim | Não |
| Código Cercado | Sim | Sim | Sim | Sim | Não |
| Matemática | Não | Não | Sim | Sim | Não |
| Notas de rodapé | Sim | Não | Sim | Sim | Não |
| Listas de definição | Não | Não | Sim | Sim | Não |
| Abreviaturas | Não | Não | Sim | Não | Não |
| Listas de atributos | Não | Não | Sim | Não | Não |
| Extensões | Limitado | Não | Sim | Sim | Não |
| Tipografia | Básico | Não | Sim | Não | Não |
| Links automáticos | Sim | Não | Não | Não | Não |
| Listas Alfabéticas | Sim | Não | Não | Não | Não |

## Principais vantagens do desconto GFM [key-advantages-of-discount-gfm]

1. **Compatibilidade com GitHub**: Perfeito para conteúdo que precisa funcionar no GitHub
2. **Desempenho**: Implementação rápida baseada em C
3. **Simplicidade**: Focado nos principais recursos do GitHub sem complexidade
4. **Confiabilidade**: Implementação estável e bem testada
5. **Conformidade com os padrões**: segue a especificação Markdown do GitHub
6. **Leve**: uso mínimo de recursos e dependências

## Casos de uso comuns [common-use-cases]

**Documentação do GitHub**

- Arquivos README e documentação do projeto
- Páginas e wikis do GitHub
- Descrições de solicitações de emissão e pull

** Redação Técnica **

- Documentação de código e tutoriais
- Documentação API
- Especificações técnicas

**Gerenciamento de conteúdo**

- Postagens e artigos de blogs
- Sites de documentação
- Bases de conhecimento

**Edição Colaborativa**

- Documentação da equipe
- Documentos de planejamento do projeto
- Notas e atas de reuniões

## Opções de configuração [configuration-options]

O Discount GFM oferece suporte a várias opções de configuração:

- **Link automático**: ativar/desativar a detecção automática de URL
- **Notas de rodapé**: controle o processamento de notas de rodapé
- **Índice**: Configurações de geração de TOC
- **Segurança HTML**: validação e higienização de links
- **Modo estrito**: regras de análise aprimoradas
- **Cotações inteligentes**: conversão automática de cotações

## Detalhes de implementação [implementation-details]

**Opções do analisador**

- `kGHMarkdownAutoLink`: Habilitar link automático de URL
- `kGHMarkdownFootnotes`: Ativar processamento de notas de rodapé
- `kGHMarkdownTOC`: Ativar geração de índice
- `kGHMarkdownSafeLinks`: Restringir links para protocolos seguros
- `kGHMarkdownNoHTMLTags`: Desativar processamento de tags HTML

**Recursos de saída**

- Marcação semântica HTML5
- Hierarquia de títulos adequada
- Estruturas de mesa acessíveis
- Saída HTML limpa e válida

## Melhores práticas [best-practices]

1. **Use tabelas com moderação**: tabelas são poderosas, mas podem ser complexas de manter
2. **Aproveite listas de tarefas**: ótimo para gerenciamento e documentação de projetos
3. **Utilize Autolinks**: deixe o processador lidar com a conversão de URL automaticamente
4. **Estrutura com títulos**: Use hierarquia de títulos adequada para melhor geração de TOC
5. **Teste no GitHub**: Verifique a compatibilidade com a renderização do GitHub

## Migração do Markdown padrão [migration-from-standard-markdown]

A maioria dos Markdown padrão funciona com Discount GFM sem alterações. Para aproveitar os recursos do GFM:

1. **Adicionar tabelas**: converta dados em formato de tabela estilo GitHub
2. **Use listas de tarefas**: substitua os marcadores por caixas de seleção quando apropriado
3. **Ativar Tachado**: Use `~~text~~` para conteúdo riscado
4. **Aproveite os links automáticos**: remova a marcação manual de links para URLs simples
5. **Estrutura de títulos**: Garanta uma hierarquia de títulos adequada para geração de TOC

## Recursos [resources]

- [Especificações de Markdown com sabor do GitHub] (https://github.github.com/gfm/)
- [Documentação da Biblioteca de Descontos](https://www.pell.portland.or.us/~orc/Code/discount/)
- [Guia de redução do GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Folha de dicas do Markdown](https://www.markdownguide.org/cheat-sheet/)

---

*Esta documentação cobre o Discount GFM conforme implementado em Marked. Para obter as informações mais atuais, consulte sempre a especificação oficial do GitHub Flavored Markdown.*