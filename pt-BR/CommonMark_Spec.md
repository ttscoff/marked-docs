<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Confira o [Markdown Dingus](x-marked-3://dingus?processor=commonmark) para experimentar o processador CommonMark (GFM).


## O que é CommonMark? [what-is-commonmark]

CommonMark é uma implementação de Markdown fortemente especificada e altamente compatível. Ele foi criado para resolver as ambiguidades e inconsistências na especificação Markdown original de John Gruber, que levou a implementações divergentes em diferentes plataformas e ferramentas.

## Por que o CommonMark existe [why-commonmark-exists]

A especificação Markdown original de John Gruber era intencionalmente ambígua em muitas áreas, levando a diferentes interpretações por várias implementações. Isso criou problemas onde o mesmo documento Markdown seria renderizado de forma diferente em plataformas diferentes (GitHub, StackOverflow, Reddit, etc.).

CommonMark fornece:

- **Especificações inequívocas** para toda a sintaxe Markdown
- **Conjunto de testes abrangente** para garantir um comportamento consistente
- **Regras de precedência claras** para sintaxe conflitante
- **Algoritmo de análise detalhado** que pode ser implementado de forma consistente

## Principais diferenças do Markdown padrão [key-differences-from-standard-markdown]

### 1. **Regras de análise mais rígidas** [1-stricter-parsing-rules]

CommonMark impõe um comportamento de análise mais consistente:

**Linhas em branco antes dos elementos do bloco**

- CommonMark requer linhas em branco antes de títulos, citações e listas
- O Markdown padrão geralmente permite isso sem linhas em branco

```markdown
Text
# Heading
```

*CommonMark: Requer linha em branco antes do título*

*Marcação padrão: geralmente permite sem linha em branco*

### 2. **Análise de itens de lista** [2-list-item-parsing]

**Requisitos de recuo**

- CommonMark possui regras específicas para recuo de itens de lista
- As sublistas devem ser recuadas de forma consistente (normalmente 4 espaços)
- As implementações de Markdown padrão variam de acordo com isso

```markdown
1. First item
   - Sublist item (4 spaces required in CommonMark)
2. Second item
```

**Continuação da lista**

- CommonMark tem regras claras para quando os itens da lista são "soltos" ou "apertados"
- Listas soltas envolvem itens em tags `<p>`, listas restritas não

### 3. **Manuseio de bloco de código** [3-code-block-handling]

**Blocos de código protegidos**

- CommonMark padroniza sintaxe de bloco de código protegido com crases ou tils
- Requer recuo consistente e marcadores de fechamento


    ```linguagem
    código aqui
    ```


**Blocos de código recuados**

- CommonMark requer linhas em branco antes dos blocos de código recuados
- O Markdown padrão geralmente permite sem linhas em branco

### 4. **Link e processamento de imagem** [4-link-and-image-processing]

**Precedência do link de referência**

- CommonMark tem regras claras para as quais a definição de referência tem precedência
- Múltiplas definições para a mesma referência são tratadas de forma consistente

```markdown
[link1]: /url1
[link1]: /url2
[link1]  <!-- Uses /url2 in CommonMark -->
```

**Ordem de análise de link**

- CommonMark processa links antes da ênfase
- Isso afeta como a sintaxe aninhada é interpretada

### 5. **Ênfase e forte ênfase** [5-emphasis-and-strong-emphasis]

**Regras de ênfase aninhadas**

- CommonMark possui algoritmos específicos para lidar com marcadores `*` e `_` aninhados
- Impede a análise ambígua de padrões de ênfase complexos

```markdown
*foo *bar* baz*  <!-- Clear precedence rules in CommonMark -->
```

**Processamento de delimitador**

- CommonMark usa um algoritmo de "pilha delimitadora" para análise de ênfase consistente
- As implementações de Markdown padrão variam em sua abordagem

### 6. **Processamento de bloco HTML** [6-html-block-processing]

**Detecção de bloco HTML**

- CommonMark possui 7 tipos diferentes de blocos HTML com regras específicas
- Cada tipo tem requisitos diferentes para condições de início/fim

```html
<div>
This is an HTML block in CommonMark
</div>
```

### 7. **Tratamento de quebra de linha** [7-line-break-handling]

**Quebras de linha dura**

- CommonMark requer dois espaços no final da linha para quebras bruscas
- Quebras de linha única tornam-se quebras suaves (ignoradas em HTML)

```markdown
Line one
Line two  <!-- Two spaces before line break -->
```

### 8. **Referências de entidades e caracteres** [8-entity-and-character-references]

**Referências de caracteres numéricos**

- CommonMark suporta referências numéricas decimais e hexadecimais
- O suporte Markdown padrão varia

```html
&#8212;  <!-- Decimal -->
&#x2014; <!-- Hexadecimal -->
```

## Algoritmo de análise CommonMark [commonmark-parsing-algorithm]

CommonMark usa uma abordagem de análise em duas fases:

### Fase 1: Estrutura do Bloco [phase-1-block-structure]

1. **Processamento de linha**: cada linha é analisada em busca de marcadores em nível de bloco
2. **Blocos de Contêiner**: Blockquotes, listas e outros contêineres são identificados
3. **Blocos de folhas**: títulos, blocos de código e parágrafos são processados
4. **Links de referência**: as definições de link são coletadas para uso posterior

### Fase 2: Estrutura Inline [phase-2-inline-structure]

1. **Processamento Inline**: o texto dentro dos blocos é analisado para elementos inline
2. **Análise de ênfase**: usa algoritmo de pilha delimitadora para ênfase consistente
3. **Resolução de link**: links de referência são resolvidos usando definições coletadas
4. **Processamento de entidades**: as referências de caracteres são convertidas em caracteres reais

## Benefícios do CommonMark [benefits-of-commonmark]

1. **Comportamento Previsível**: A mesma entrada sempre produz a mesma saída
2. **Compatibilidade entre plataformas**: funciona de forma consistente em diferentes ferramentas
3. **Testes Abrangentes**: Conjunto de testes extenso garante confiabilidade
4. **Documentação clara**: especificações detalhadas eliminam suposições
5. **Preparado para o futuro**: pontos de extensão bem definidos para novos recursos

## Notas de implementação [implementation-notes]

CommonMark foi projetado para ser:

**Compatível com as especificações**: segue exatamente as especificações oficiais do CommonMark
- ** Orientado a testes **: passa no conjunto de testes oficial do CommonMark
- **Extensível**: pode ser estendido com recursos adicionais, mantendo a compatibilidade
- **Rápido**: algoritmos de análise otimizados para desempenho

## Recursos [resources]

- [Especificação CommonMark](https://spec.commonmark.org/0.31.2/)
- [Suíte de testes CommonMark](https://github.com/commonmark/commonmark-spec)
- [CommonMark Dingus](https://spec.commonmark.org/dingus/) - Ferramenta de teste on-line
- [Fórum de discussão CommonMark](https://talk.commonmark.org/)

---

*Esta documentação cobre CommonMark 0.31.2 (28/01/2024). Para obter as informações mais atuais, consulte sempre a especificação oficial.*