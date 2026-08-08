<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

Marcado compreende catálogos de documentação [Apple DocC](https://www.swift.org/documentation/docc/) (pacotes `.docc`). Quando você visualiza o Markdown que fica dentro ou ao lado de um catálogo, o Marked pode resolver referências de imagem **sem extensão** para arquivos na pasta `Resources` do catálogo — incluindo as variantes `~dark` e `@2x`.

Para documentos Markdown normais que usam **caminhos com extensões de arquivo** (`images/icon.png`), consulte [Variantes de imagem](Image_Variants.html). Esse recurso funciona em qualquer lugar; A resolução DocC é específica do catálogo.

## Habilitando resolução DocC [enabling-docc-resolution]

Em {% prefspane Apps %}, habilite **Resolver referências de imagem DocC** (ativado por padrão).

A detecção DocC é executada quando Marcado encontra um ancestral de catálogo `.docc` do documento aberto. Nenhum esquema de URL especial ou integração com Xcode é necessário – abra o Markdown do catálogo da mesma forma que faria com qualquer outro arquivo.

## Referências sem extensão [extensionless-references]

Dentro de um catálogo DocC, os autores normalmente fazem referência a imagens **sem** um caminho ou extensão:

```markdown
![Order flow](OrderStateTransitions)
```

Marcado resolve `OrderStateTransitions` a `Resources/OrderStateTransitions.png` (ou outro tipo suportado) quando esse arquivo existe no catálogo.

Referências que já incluem um caminho e uma extensão — `images/chart.png` — são deixadas para [Variantes de imagem](Image_Variants.html) e não são reescritas pela resolução DocC.

## Modo escuro e variantes Retina [dark-mode-and-retina-variants]

Os catálogos DocC geralmente enviam vários arquivos por imagem:

| Função | Exemplo em `Resources/` |
|------|-------------|
| Luz (1x) | `diagram.png` |
| Escuro (1x) | `diagram~dark.png` |
| Luz (2x) | `diagram@2x.png` |
| Escuro (2x) | `diagram~dark@2x.png` |

Quando existe mais de uma variante, Marked emite a mesma marcação responsiva `<picture>` descrita em [Variantes de imagem](Image_Variants.html). Uma referência de arquivo único ainda resolve um caminho normal `<img>` ou `![](Resources/...)`.

## HTML e Markdown [html-and-markdown]

A resolução DocC se aplica durante a passagem de inclusão de Marked:

- **Fontes de markdown** — `![alt](ImageName)` referências
- **Fontes HTML** — `<img src="ImageName">` sem extensão

Ambos são atualizados antes da renderização da visualização.

## Observação de arquivos [file-watching]

As imagens resolvidas na pasta do catálogo `Resources` são adicionadas à lista de observação de Marked. A edição de um arquivo de variante atualiza externamente a visualização sem atualização manual.

## Tópicos relacionados [related-topics]

- [Variantes de imagem] (Image_Variants.html) — detecção `~dark` e `@2x` para caminhos baseados em extensão em qualquer projeto
- [Xcode Playgrounds](Xcode_Playgrounds.html) — visualização dos comentários do Swift Playground
- [Configurações: Aplicativos] (Settings_Apps.html) — DocC e preferências de variantes de imagem